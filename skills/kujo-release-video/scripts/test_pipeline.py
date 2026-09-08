"""Offline behavioral checks: intake, escaping, caching, budgets, locks and status.
Run with python3 scripts/test_pipeline.py. No API calls or rendered fixtures needed.
"""
import copy,importlib.util,json,tempfile,unittest,io,base64
from unittest.mock import patch
from pathlib import Path
spec=importlib.util.spec_from_file_location('pipeline',Path(__file__).with_name('release_video.py'))
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
class PipelineTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.w=Path(self.temp.name)/'film'
  p.init(self.w,p.SKILL/'examples/release.example.json')
  self.plan=p.read(p.SKILL/'examples/plan.example.json');p.save(self.w/'plan.json',self.plan)
 def tearDown(self):self.temp.cleanup()
 def test_release_facts_are_required_and_refs_known(self):
  self.plan['fact_refs']['proof']=['invented'];p.save(self.w/'plan.json',self.plan)
  with self.assertRaises(p.Stop):p.prepare(self.w)
 def test_long_or_missing_copy_refused(self):
  self.plan['task']='x'*31
  with self.assertRaises(p.Stop):p.validate(p.read(self.w/'release.json'),self.plan)
 def test_compiles_escaped_text_and_version_without_old_audio(self):
  self.plan['copy']['hook_1']='<b>new</b>';self.plan['task']='<script>x</script>'
  p.save(self.w/'plan.json',self.plan);p.prepare(self.w)
  self.assertIn('&lt;b&gt;new&lt;/b&gt;', (self.w/'index.html').read_text())
  self.assertIn('Style demo',(self.w/'index.html').read_text())
  self.assertNotIn('<script>x', (self.w/'content.js').read_text())
  self.assertFalse((self.w/'audio/master.wav').exists())
 def test_missing_speech_stops_before_credential_access(self):
  p.prepare(self.w)
  with self.assertRaisesRegex(p.Stop,'uncached ElevenLabs'):p.speech(self.w,False,750)
  with self.assertRaisesRegex(p.Stop,'exceeds'):p.speech(self.w,True,1)
 def test_pending_request_cannot_be_retried(self):
  p.prepare(self.w);p.save(self.w/'audio/takes/speed.pending.json',{'state':'request_started'})
  with self.assertRaisesRegex(p.Stop,'Uncertain prior'):p.speech(self.w,True,750)
 def test_lock_exclusion_and_release(self):
  with p.lock(self.w):
   with self.assertRaisesRegex(p.Stop,'locked'):
    with p.lock(self.w):pass
  self.assertFalse((self.w/'.pipeline.lock').exists())
 def test_prepare_preserves_custom_style_and_fingerprint_changes(self):
  p.prepare(self.w);a=p.fingerprint(self.w)
  style=self.w/'style.css';style.write_text(style.read_text()+'\n/* custom */')
  p.prepare(self.w);self.assertTrue(style.read_text().endswith('/* custom */'))
  self.assertNotEqual(a,p.fingerprint(self.w))
 def test_generation_time_license_not_upgraded_by_current_intent(self):
  p.prepare(self.w)
  for key,_,_ in p.CUES:p.save(self.w/'audio/takes'/f'{key}.json',{'generation_tier':'free'})
  r=p.read(self.w/'release.json');r['usage']='commercial';p.save(self.w/'release.json',r)
  with self.assertRaisesRegex(p.Stop,'Cached narration'):p.rights(self.w)
 def test_generation_receipts_cache_and_corruption(self):
  p.prepare(self.w);requests=[]
  def fake(request,timeout):
   requests.append(request.full_url)
   result={'tier':'free'} if request.full_url.endswith('/subscription') else {'audio_base64':base64.b64encode(b'ID3-test-only').decode(),'alignment':{}}
   return io.BytesIO(json.dumps(result).encode())
  with patch.dict(p.os.environ,{'ELEVENLABS_API_KEY':'test-only-not-a-credential'}),patch.object(p.urllib.request,'urlopen',side_effect=fake):
   result=p.speech(self.w,True,750)
   self.assertEqual(result['requests'],5);self.assertEqual(len(requests),6)
   self.assertEqual(p.speech(self.w,False,750)['requests'],0)
   release=p.read(self.w/'release.json');release['usage']='commercial';p.save(self.w/'release.json',release)
   with self.assertRaisesRegex(p.Stop,'generation-time provenance'):p.speech(self.w,True,750)
   self.assertEqual(len(requests),6)
   release['usage']='noncommercial';p.save(self.w/'release.json',release)
   (self.w/'audio/takes/goal.mp3').write_bytes(b'changed')
   with self.assertRaisesRegex(p.Stop,'uncached ElevenLabs'):p.speech(self.w,False,750)
   self.assertEqual(len(requests),6)
 def test_timeout_records_pending_and_stops(self):
  p.prepare(self.w)
  def fake(request,timeout):
   if request.full_url.endswith('/subscription'):return io.BytesIO(b'{"tier":"free"}')
   raise TimeoutError('test timeout')
  with patch.dict(p.os.environ,{'ELEVENLABS_API_KEY':'test-only-not-a-credential'}),patch.object(p.urllib.request,'urlopen',side_effect=fake):
   with self.assertRaisesRegex(p.Stop,'no automatic retry'):p.speech(self.w,True,750)
   self.assertTrue((self.w/'audio/takes/speed.pending.json').exists())
   with self.assertRaisesRegex(p.Stop,'Uncertain prior'):p.speech(self.w,True,750)
 def test_status_detects_changed_inputs_and_output(self):
  p.prepare(self.w);output=self.w/'output/release-complete.mp4';output.write_bytes(b'test-status-only')
  p.save(self.w/'run.json',{'status':'technical_pass','input_fingerprint':p.fingerprint(self.w),'output':str(output),'output_sha256':p.sha(output)})
  with patch.object(p.sys,'argv',['pipeline','status','--workspace',str(self.w)]),patch('sys.stdout',new_callable=io.StringIO) as out:
   self.assertEqual(p.main(),0);self.assertEqual(json.loads(out.getvalue())['status'],'technical_pass')
  output.write_bytes(b'changed')
  with patch.object(p.sys,'argv',['pipeline','status','--workspace',str(self.w)]),patch('sys.stdout',new_callable=io.StringIO) as out:
   self.assertEqual(p.main(),0);self.assertEqual(json.loads(out.getvalue())['status'],'stale')
 def test_existing_directory_not_overwritten(self):
  with self.assertRaises(p.Stop):p.init(self.w,p.SKILL/'examples/release.example.json')
if __name__=='__main__':unittest.main()
