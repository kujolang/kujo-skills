"""Structural and failure-path coverage; fixtures are explicitly synthetic test data."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import video_styles as v


def fixture(root,style,aspect='16:9'):
    b={'video_type':style,'source_kind':'product','source':'test-fixture', 'goal':'Exercise compiler','audience':'Maintainers','primary_message':'Compiler fixture only', 'cta':'Inspect fixtures','release_or_feature_name':'Fixture','version':'test','relationship':'test integration','aspect_ratio':aspect}
    v.init(b,root)
    b=v.read(root/'brief.json');p=v.read(root/'plan.json')
    (root/'proof.txt').write_text('Compiler fixture\nThis is test data, not product proof.\n')
    (root/'proof.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720"><rect width="1280" height="720" fill="#ddd"/><text x="100" y="350" font-size="48">COMPILER TEST FIXTURE</text></svg>')
    p['sources']=[{'id':'fact','source':'test fixture','range':'lines 1–2','claim':'Test fixture only','verification':'Read fixture'}]
    b['proof_assets']=[{'id':ident,'kind':'artifact','media_type':typ,'path':path,'source':'local fixture','timestamp_or_range':'whole fixture','claim_supported':['fact'],'verification':'Fixture generated for test','authentic':True,'rights':'Original test fixture'} for ident,typ,path in [('text','text','proof.txt'),('image','image','proof.svg')]]
    for beat in p['beats']:
        beat.update(purpose='Test component',copy='Compiler fixture',support='Test data only',source_of_truth=['fact'],proof_assets=['text'] if beat['visual'] in ('terminal','code','diff','quote') else ['image'],verification='Fixture inspection',nodes=['Input','Output'],steps=['Read fixture','Check compiler'])
        if beat['visual']=='contrast':beat['proof_assets']=['image','text']
    v.write(root/'brief.json',b);v.write(root/'plan.json',p)
    return b,p

class Styles(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'film'
    def tearDown(self):self.temp.cleanup()
    def test_all_styles_all_shapes_compile(self):
        for style in v.RECIPES:
            for shape in ('16:9','9:16','1:1'):
                with self.subTest(style=style,shape=shape):
                    root=Path(self.temp.name)/(style+shape.replace(':','-'))
                    fixture(root,style,shape); result=v.prepare(root)
                    self.assertEqual(result['status'],'structural-pass')
                    self.assertTrue((root/'composition/index.html').is_file())
                    self.assertEqual(v.read(root/'render-metadata.json')['status'],'not-rendered')
                    self.assertTrue(result['snapshot_times'])
                    self.assertNotIn('src="../',(root/'composition/index.html').read_text())
    def test_routes_preserve_intent_and_source(self):
        for b,style,base in [
            ({'single_interaction':True,'duration_target':10},'apple-style-micro-launch','motion-graphics'),
            ({'single_interaction':True,'duration_target':10,'voiceover':True},'apple-style-micro-launch','general-video'),
            ({'source_kind':'github_pr','video_type':'cinematic-hero-launch'},'cinematic-hero-launch','pr-to-video'),
            ({'source_kind':'changelog_md','multiple_changes':True},'release-notes-changelog','general-video'),
            ({'source_kind':'changelog_md','multiple_changes':True,'available_workflows':['changelog-video']},'release-notes-changelog','changelog-video'),
            ({'integration':True,'duration_target':8},'integration-partnership-launch','general-video'),
            ({'duration_target':10,'voiceover':True},'short-product-launch','general-video'),
        ]:
            with self.subTest(b=b):
                r=v.route(b);self.assertEqual((r['video_type'],r['base_workflow']),(style,base))
    def test_initial_plan_is_not_ready(self):
        v.init({'video_type':'kinetic-release-drop'},self.root)
        with self.assertRaises(v.Invalid):v.validate(self.root)
        with self.assertRaises(v.Invalid):v.init({},self.root)
    def mutate_plan(self,fn,style='short-product-launch'):
        b,p=fixture(self.root,style);fn(p);v.write(self.root/'plan.json',p)
        with self.assertRaises(v.Invalid):v.validate(self.root)
    def test_invalid_claim(self):self.mutate_plan(lambda p:p['beats'][0].update(source_of_truth=['missing']))
    def test_duplicate_source(self):self.mutate_plan(lambda p:p['sources'].append(p['sources'][0]))
    def test_timing_gap(self):self.mutate_plan(lambda p:p['beats'][0].update(duration=100))
    def test_invalid_audio_offset(self):self.mutate_plan(lambda p:p['beats'][0].update(audio=[{'event':'click','offset':99}]))
    def test_unproven_metrics(self):self.mutate_plan(lambda p:p['beats'][0].update(visual='metric',metric={'value':42,'unit':'ms'}))
    def test_proof_density(self):
        b,p=fixture(self.root,'real-product-proof-reel')
        for beat in p['beats']:beat['conceptual']=True
        v.write(self.root/'plan.json',p)
        with self.assertRaises(v.Invalid):v.validate(self.root)
    def test_asset_path_escape(self):
        b,p=fixture(self.root,'short-product-launch');b['proof_assets'][0]['path']='../escape.txt'
        v.write(self.root/'brief.json',b)
        with self.assertRaises(v.Invalid):v.validate(self.root)
    def test_no_fake_authentic_label(self):
        b,p=fixture(self.root,'short-product-launch');b['proof_assets'][1]['authentic']=False
        v.write(self.root/'brief.json',b)
        with self.assertRaises(v.Invalid):v.validate(self.root)
    def test_source_is_escaped_not_executed(self):
        b,p=fixture(self.root,'short-product-launch');p['beats'][0]['copy']='</script><script>alert(1)</script>'
        v.write(self.root/'plan.json',p);v.prepare(self.root)
        self.assertNotIn('<script>alert(1)',(self.root/'composition/index.html').read_text())
        self.assertNotIn('</script>',(self.root/'composition/content.js').read_text())
    def test_video_range_and_bundling(self):
        b,p=fixture(self.root,'short-product-launch')
        (self.root/'sample.mp4').write_bytes(b'test-only bytes; not a render fixture')
        b['proof_assets'][1].update(media_type='video',path='sample.mp4',media_duration=60,media_start=1)
        v.write(self.root/'brief.json',b);v.prepare(self.root)
        doc=(self.root/'composition/index.html').read_text()
        self.assertIn('data-media-start="1"',doc)
        b['proof_assets'][1]['media_duration']=1;v.write(self.root/'brief.json',b)
        with self.assertRaises(v.Invalid):v.validate(self.root)
    def test_rebuild_is_deterministic(self):
        fixture(self.root,'feature-reveal');v.prepare(self.root)
        files=['composition/index.html','composition/content.js','source-assets.json','audio-cues.json']
        original={f:(self.root/f).read_bytes() for f in files}
        v.prepare(self.root)
        self.assertEqual(original,{f:(self.root/f).read_bytes() for f in files})
    def test_native_pr_route_not_bypassed(self):
        with self.assertRaises(v.Invalid):v.route({'source_kind':'github_pr','base_workflow':'motion-graphics'})
    def test_unknown_style_and_nonfinite_duration(self):
        for b in ({'video_type':'bogus'},{'duration_target':float('nan')},{'duration_target':True}):
            with self.assertRaises(v.Invalid):v.route(b)


class Voices(unittest.TestCase):
    def test_every_style_has_a_distinct_default_without_enabling_speech(self):
        selections=[v.normalize({'video_type':style}) for style in v.RECIPES]
        self.assertEqual(len({b['resolved_voice']['voice_id'] for b in selections}),10)
        self.assertTrue(all(b['voiceover'] is False for b in selections))
        self.assertTrue(all(b['resolved_voice']['resolution']=='selected-id' for b in selections))

    def test_explicit_name_wins_but_style_delivery_is_retained(self):
        b=v.normalize({'video_type':'kinetic-release-drop','voice':'gEoRgE'})
        self.assertEqual(b['resolved_voice']['name'],'George')
        self.assertEqual(b['resolved_voice']['settings']['speed'],1.06)
        self.assertEqual(b['resolved_voice']['selection'],'override')

    def test_explicit_id_wins_over_conflicting_name(self):
        r=v.resolve_voice({'voice':{'voice_id':'CustomVoice123','name':'George','settings':{'speed':.9}}},'feature-reveal')
        self.assertEqual(r['voice_id'],'CustomVoice123')
        self.assertEqual(r['settings']['speed'],.9)

    def test_unknown_name_never_falls_back(self):
        r=v.resolve_voice({'voice':'My saved narrator'},'feature-reveal')
        self.assertIsNone(r['voice_id'])
        self.assertEqual(r['resolution'],'needs-name-resolution')
        self.assertEqual(r['name'],'My saved narrator')

    def test_changing_style_refreshes_only_default_selection(self):
        b=v.normalize({'video_type':'cinematic-hero-launch'})
        b['video_type']='feature-reveal'
        self.assertEqual(v.normalize(b)['resolved_voice']['name'],'Jessica')
        b['voice']='Alice';b=v.normalize(b);b['video_type']='short-product-launch'
        self.assertEqual(v.normalize(b)['resolved_voice']['name'],'Alice')

    def test_rejects_invalid_overrides(self):
        for voice in ({'voice_id':'bad/id'},{'settings':{'speed':False}},{'settings':{'stability':2}},{'settings':{'temperature':1}},{'name':''}):
            with self.subTest(voice=voice), self.assertRaises(v.Invalid):v.resolve_voice({'voice':voice},'feature-reveal')

    def test_prepared_narration_handoff_tracks_actual_beats_and_rebuilds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'film';b,p=fixture(root,'short-product-launch')
            b.update(voiceover=True,voice='Alice')
            for beat in p['beats']:beat['narration']='This is a compiler test.'
            v.write(root/'brief.json',b);v.write(root/'plan.json',p);v.prepare(root)
            speech=v.read(root/'voiceover.json')
            self.assertTrue(speech['enabled']);self.assertEqual(speech['name'],'Alice')
            self.assertEqual(len(speech['cues']),len(p['beats']))
            self.assertEqual(speech['cues'][-1]['end'],20)
            b['voice']={'voice_id':'UserVoice456'};v.write(root/'brief.json',b);v.prepare(root)
            self.assertEqual(v.read(root/'voiceover.json')['voice_id'],'UserVoice456')

if __name__=='__main__':unittest.main()
