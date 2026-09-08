#!/usr/bin/env python3
"""Kujo story layer: no LLM, source fetching, paid calls or renderer replacement."""
import argparse
import hashlib
import html
import json
import math
from pathlib import Path
import shutil
import sys

SKILL = Path(__file__).resolve().parents[1]
# id: seconds, recommended range, roles, relative durations, component, motion
RECIPES = {
 'cinematic-hero-launch': (50, [40,60], 'intrigue first-proof expansion thesis identity cta', [4,9,18,10,5,4], 'hero product artifacts thesis identity identity', 'mask zoom fan type logo logo'),
 'apple-style-micro-launch': (12, [8,15], 'setup interaction response resolve sting', [2,3,3,2,2], 'product product product product identity', 'focus cursor expand zoom logo'),
 'release-notes-changelog': (45, [35,60], 'release headline supporting supporting fixes cta', [3,14,9,9,7,3], 'identity product product code terminal identity', 'type zoom push code code logo'),
 'real-product-proof-reel': (40, [30,50], 'ask activation capability capability outcome cta', [4,5,12,11,5,3], 'terminal flow product code product identity', 'code connector zoom code focus logo'),
 'editorial-thesis-launch': (45, [35,60], 'tension contrast evidence principle consequence cta', [7,7,10,8,10,3], 'thesis contrast code thesis flow identity', 'type push code mask connector logo'),
 'feature-reveal': (25, [15,35], 'friction cost reveal new-workflow payoff identity', [4,3,3,8,5,2], 'product steps product product contrast identity', 'push stagger mask cursor focus logo'),
 'integration-partnership-launch': (25, [15,40], 'request system-a boundary system-b outcome cta', [3,4,4,6,5,3], 'terminal product flow product product identity', 'code focus connector push zoom logo'),
 'engineering-pr-to-video': (60, [30,90], 'problem diff mechanism evidence impact cta', [8,13,14,12,10,3], 'terminal diff flow code product identity', 'code code connector code zoom logo'),
 'short-product-launch': (20, [15,25], 'hook primary-workflow second-capability outcome cta', [2,5,5,5,3], 'product product product product identity', 'mask cursor zoom focus logo'),
 'kinetic-release-drop': (8, [5,12], 'name transformation proof-glimpse cta', [2,2,2.5,1.5], 'kinetic kinetic terminal identity', 'type mask code logo'),
}
COMPONENTS = {'hero','product','artifacts','thesis','identity','terminal','code','diff','flow','contrast','steps','kinetic','metric','quote'}
MOTIONS = {'mask','zoom','fan','type','logo','focus','cursor','expand','push','code','connector','stagger','metric'}
BRAND = {'background':'#f9f9f9','foreground':'#060606','muted':'#555555','accent':'#060606','danger':'#a52422','success':'#28613a','fontDisplay':'Departure Mono','fontBody':'Arial','fontMono':'Departure Mono','logo':'','logomark':''}
PROOF_KINDS = {'ui','terminal','code','log','diagram','browser','artifact'}

class Invalid(ValueError): pass

def need(ok, message):
    if not ok: raise Invalid(message)

def read(path):
    with Path(path).open() as f: return json.load(f)

def write(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')

def number(v): return isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v)

def nonempty(v): return isinstance(v,str) and bool(v.strip())

def resolve_voice(b, style):
    """Resolve style defaults without letting a default beat an explicit voice choice."""
    catalog=read(SKILL/'references/voices.json')
    default=catalog['styles'][style]
    selected=dict(default)
    override=b.get('voice',{})
    if isinstance(override,str):override={'name':override}
    need(isinstance(override,dict),'voice must be a name or object')
    need(set(override)<= {'name','voice_id','model_id','settings','direction'},'unknown voice override field')
    for k in ('name','voice_id','model_id','direction'):
        if k in override:need(nonempty(override[k]),'voice.'+k+' must be nonempty')
    if 'voice_id' in override:
        need(override['voice_id'].isascii() and override['voice_id'].isalnum(),'voice.voice_id must be an alphanumeric provider ID')
        selected={'voice_id':override['voice_id'],'name':override.get('name','User-selected voice'),'direction':default['direction']}
    elif 'name' in override:
        matches=[v for v in catalog['styles'].values() if v['name'].casefold()==override['name'].strip().casefold()]
        selected=dict(matches[0]) if matches else {'name':override['name'],'voice_id':None,'direction':default['direction']}
    settings=override.get('settings',{})
    need(isinstance(settings,dict),'voice.settings must be an object')
    need(set(settings)<=set(default['settings']),'unknown voice setting')
    settings=dict(default['settings'],**settings)
    for k in ('stability','similarity_boost','style'):
        need(number(settings[k]) and 0<=settings[k]<=1,'voice setting '+k+' must be between 0 and 1')
    need(number(settings['speed']) and .7<=settings['speed']<=1.2,'voice speed must be between 0.7 and 1.2')
    need(isinstance(settings['use_speaker_boost'],bool),'use_speaker_boost must be boolean')
    return {'provider':'elevenlabs','name':selected['name'],'voice_id':selected['voice_id'],
            'model_id':override.get('model_id',catalog['model_id']), 'settings':settings,
            'direction':override.get('direction',default['direction']),
            'selection':'override' if ('name' in override or 'voice_id' in override) else 'style-default',
            'resolution':'selected-id' if selected['voice_id'] else 'needs-name-resolution',
            'availability_check':'required-before-generation'}

def route(b):
    need(isinstance(b,dict),'brief must be an object')
    kind = b.get('source_kind','manual')
    style = b.get('video_type')
    duration = b.get('duration_target')
    if duration is not None: need(number(duration) and duration>0,'duration_target must be positive seconds')
    voiced = b.get('voiceover',False) is not False
    if not style or style == 'auto':
        if kind in ('github_pr','pr'): style='engineering-pr-to-video'
        elif kind in ('changelog_md','github_release','git_range') and b.get('multiple_changes'): style='release-notes-changelog'
        elif b.get('intent') in ('teaser','drop','sting'): style='kinetic-release-drop'
        elif b.get('single_interaction') and (duration is None or duration<=15): style='apple-style-micro-launch'
        elif b.get('integration'): style='integration-partnership-launch'
        elif b.get('pain_to_payoff'): style='feature-reveal'
        elif b.get('breadth'): style='real-product-proof-reel'
        elif b.get('thesis'): style='editorial-thesis-launch'
        elif b.get('major_release'): style='cinematic-hero-launch'
        elif duration is not None and duration<=12 and not voiced: style='kinetic-release-drop'
        else: style='short-product-launch'
    need(style in RECIPES, 'unknown video_type: '+str(style))
    # Visual style is orthogonal to the native input contract.
    if kind in ('github_pr','pr') or style=='engineering-pr-to-video': base='pr-to-video'
    elif style=='release-notes-changelog' and 'changelog-video' in b.get('available_workflows',[]): base='changelog-video'
    elif style in ('kinetic-release-drop','apple-style-micro-launch') and not voiced and (duration or RECIPES[style][0])<=15: base='motion-graphics'
    elif style=='editorial-thesis-launch': base='general-video'
    else: base='product-launch-video' if kind in ('url','website','product','github_release') or b.get('product_url') else 'general-video'
    # Preserve a base already selected by native HyperFrames, except PR provenance.
    if b.get('base_workflow'):
        need(b['base_workflow'] in ('product-launch-video','general-video','pr-to-video','motion-graphics','changelog-video','faceless-explainer'), 'unsupported base_workflow')
        need(not (base=='pr-to-video' and b['base_workflow']!='pr-to-video'), 'PR sources require native pr-to-video ingestion')
        need(not (b['base_workflow']=='motion-graphics' and voiced), 'narrated films require a narrative base workflow')
        need(b['base_workflow']!='changelog-video' or 'changelog-video' in b.get('available_workflows',[]), 'changelog-video is not available; use native fallback')
        base=b['base_workflow']
    return {'video_type':style,'base_workflow':base,'duration_target':duration or RECIPES[style][0], 'resolved_voice':resolve_voice(b,style), 'reference':str(SKILL/'references'/next(x['file'] for x in read(SKILL/'references/source-manifest.json')['types'] if x['id']==style))}

def normalize(b):
    result={k:None for k in ('goal','audience','primary_message','cta','source','release_or_feature_name','version')}
    result.update({'source_kind':'manual','aspect_ratio':'16:9','proof_assets':[], 'must_show':[], 'must_not_show':[], 'voiceover':False,'music':False,'captions':False,'brand_profile':{},'fps':24})
    result.update(b); result.update(route(b))
    result.pop('reference',None)
    need(result['aspect_ratio'] in ('16:9','9:16','1:1'), 'aspect_ratio must be 16:9, 9:16 or 1:1')
    need(result['fps'] in (24,25,30,60),'fps must be 24, 25, 30 or 60')
    need(isinstance(result['brand_profile'],dict),'brand_profile must be a brand token object')
    unknown=set(result['brand_profile'])-set(BRAND)
    need(not unknown,'unknown brand tokens: '+', '.join(sorted(unknown)))
    for k,v in result['brand_profile'].items():
        need(isinstance(v,str) and not any(c in v for c in ';{}<>\n'), 'invalid brand token '+k)
    return result

def blueprint(b):
    _,_,roles,weights,components,motions=RECIPES[b['video_type']]
    fps=b['fps']; frames=round(b['duration_target']*fps)
    roles=roles.split(); need(frames>=len(roles)*fps, 'duration must leave at least one second per beat')
    ends=[round(frames*sum(weights[:i+1])/sum(weights)) for i in range(len(weights))]
    beats=[]; start=0
    for i,(role,end,comp,motion) in enumerate(zip(roles,ends,components.split(),motions.split())):
        beats.append({'id':f'beat-{i+1}', 'role':role,'purpose':'','duration':round((end-start)/fps,6),'visual':comp,'copy':'','support':'','source_of_truth':[], 'proof_assets':[], 'motion':motion,'audio':[], 'transition_in':'push' if i else 'cut','transition_out':'push' if i<len(roles)-1 else 'hold','verification':'','narration':'','conceptual':False})
        start=end
    return {'beats':beats,'sources':[], 'motionProfile':{'easing_family':'power3','transition_axis':'x','primary_speed':0.5,'secondary_speed':0.3,'overshoot':0,'camera_behavior':'focus'}, 'audio_master':None, 'audio_provenance':None, 'duration_override_reason':'', 'voiceover_reason':''}

def init(b, root):
    need(not root.exists(),'workspace already exists; choose a new folder (no files overwritten)')
    b=normalize(b); plan=blueprint(b)
    root.mkdir(parents=True)
    write(root/'brief.json',b);write(root/'plan.json',plan)
    write(root/'brand-tokens.json',dict(BRAND,**b['brand_profile']))
    (root/'BRIEF.md').write_text('# Kujo video brief\n\nworkflow: '+b['base_workflow']+'\nflow: companion\nvideo_type: '+b['video_type']+'\n\nThe native workflow supplies ingestion and production capabilities. The Kujo companion owns story assembly. Resume these decisions; do not repeat intake.\n\n```json\n'+json.dumps(b,indent=2)+'\n```\n')
    (root/'STORYBOARD.md').write_text('# Storyboard draft\n\nAuthor plan.json from inspected sources, then run prepare to compile the storyboard.\n\n'+'\n'.join(f"- {x['id']} · {x['role']} · {x['duration']}s · {x['visual']}" for x in plan['beats'])+'\n')
    (root/'QA.md').write_text('# QA — pending\n\nStructural checks do not verify factual claims or creative quality.\n\n- [ ] Source/claim and asset inspection with exact ranges\n- [ ] Type-specific acceptance criteria from the selected reference\n- [ ] Native HyperFrames check (save command/result)\n- [ ] Midpoint and every boundary −1 frame / boundary / +1 frame snapshots\n- [ ] Full-size and mobile legibility; clipping; captions clear of proof\n- [ ] Sound-off story review\n- [ ] Complete video and audio audition (state if unavailable)\n- [ ] Rights, voice provider/license, music/SFX provenance\n- [ ] Final render metadata and deliverables\n')
    if b['video_type']=='release-notes-changelog':
        (root/'RELEASE_SELECTION.md').write_text('# Release selection — author before production\n\n| Source item / evidence | Tier A/B/C/D | Visualizability | Include? | Proposed visual |\n| --- | --- | --- | --- | --- |\n\nAccount for every source item, including omissions. At most one headline and four supporting items by default.\n')
    if b['video_type']=='engineering-pr-to-video':
        (root/'PR_SELECTION.md').write_text('# Native PR ingestion handoff — pending\n\nUse pr-to-video to ingest the source. Record the summary, representative selected hunks with file/line ranges, excluded hunks and reasons, mechanism outline, contributor attribution, and actual test/output evidence here. Do not recreate PR ingestion in the Kujo layer.\n')
    write(root/'render-metadata.json',{'status':'not-rendered','video_type':b['video_type'],'base_workflow':b['base_workflow']})
    return {'workspace':str(root),'status':'needs-authored-plan',**route(b)}

def local(root,path):
    need(nonempty(path),'asset path is required')
    p=(root/path).resolve(); need(p.is_relative_to(root.resolve()),'assets must be inside workspace: '+path)
    need(p.is_file(),'missing local asset: '+path)
    return p

def validate(root):
    b=normalize(read(root/'brief.json')); p=read(root/'plan.json'); style=b['video_type']
    for key in ('goal','audience','primary_message','cta','source','release_or_feature_name'):
        need(bool(b.get(key)),'brief requires '+key)
    need(isinstance(p,dict),'plan must be an object')
    need(isinstance(p.get('sources'),list) and p['sources'],'plan requires inspected sources')
    sources={}
    for s in p['sources']:
        need(isinstance(s,dict),'source must be an object')
        need(nonempty(s.get('id')) and s['id'] not in sources,'source IDs must be unique')
        need(all(nonempty(s.get(k)) for k in ('source','range','claim','verification')),'source needs source, range, claim and inspection verification')
        sources[s['id']]=s
    assets={}
    need(isinstance(b['proof_assets'],list),'proof_assets must be a list')
    for a in b['proof_assets']:
        need(isinstance(a,dict),'proof asset must be an object')
        need(nonempty(a.get('id')) and a['id'] not in assets,'proof asset IDs must be unique')
        need(a.get('kind') in PROOF_KINDS,'invalid proof asset kind')
        need(a.get('media_type') in ('image','video','text'),'media_type must be image, video or text')
        need(all(nonempty(a.get(k)) for k in ('source','timestamp_or_range','verification','rights')),'proof needs provenance, range, verification and rights')
        need(isinstance(a.get('claim_supported'),list) and a['claim_supported'] and set(a['claim_supported'])<=sources.keys(),'proof references unknown or missing source claims')
        need(isinstance(a.get('authentic'),bool),'proof must declare authentic true/false')
        local(root,a.get('path'))
        if a['media_type']=='video':
            need(number(a.get('media_duration')) and a['media_duration']>0,'video requires inspected media_duration')
            need(number(a.get('media_start',0)) and a.get('media_start',0)>=0,'invalid media_start')
        if a.get('crop'):
            need(isinstance(a['crop'],dict) and set(a['crop'])=={'x','y','width','height'},'crop requires x/y/width/height in normalized source coordinates')
            c=a['crop']; need(all(number(v) for v in c.values()) and c['x']>=0 and c['y']>=0 and c['width']>0 and c['height']>0 and c['x']+c['width']<=1 and c['y']+c['height']<=1,'crop outside source')
        assets[a['id']]=a
    beats=p.get('beats');need(isinstance(beats,list) and beats,'plan requires beats')
    seen=set(); start=0; grounded=0; first_proof=None; roles={}; abstract_run=0
    for beat in beats:
        need(isinstance(beat,dict),'beat must be an object')
        need(nonempty(beat.get('id')) and beat['id'] not in seen,'beat IDs must be unique');seen.add(beat['id'])
        for k in ('purpose','copy','verification','role'):need(nonempty(beat.get(k)),'beat '+beat['id']+' requires '+k)
        d=beat.get('duration');need(number(d) and d>0,'invalid beat duration')
        need(beat.get('visual') in COMPONENTS,'unknown visual component')
        need(beat.get('motion') in MOTIONS,'unknown motion primitive')
        need(beat.get('transition_in') in ('push','pull','scale','mask','cut'),'invalid transition_in')
        need(beat.get('transition_out') in ('push','pull','scale','mask','cut','hold'),'invalid transition_out')
        need(isinstance(beat.get('source_of_truth'),list) and beat['source_of_truth'] and set(beat['source_of_truth'])<=sources.keys(),'every beat needs valid source_of_truth IDs')
        need(isinstance(beat.get('proof_assets'),list) and set(beat['proof_assets'])<=assets.keys(),'unknown proof asset')
        need(isinstance(beat.get('conceptual'),bool),'beat must declare conceptual true/false')
        for aid in beat['proof_assets']:
            a=assets[aid];need(set(beat['source_of_truth']) & set(a['claim_supported']),'asset does not support this beat')
            need(a['authentic'] or beat['conceptual'],'non-authentic visuals must be labeled conceptual')
            if a['media_type']=='video':need(a.get('media_start',0)+d<=a['media_duration']+1/b['fps'],'video range is shorter than beat')
        real=any(assets[x]['authentic'] for x in beat['proof_assets']) and not beat['conceptual']
        if real:
            grounded+=d
            if first_proof is None:first_proof=start
        abstract_run=0 if real else abstract_run+1
        if style=='editorial-thesis-launch':need(abstract_run<=2,'editorial allows at most two consecutive abstract plates')
        if style=='kinetic-release-drop':need(len(beat['copy'].split())<=6 and len(beat.get('support','').split())<=10,'drop copy exceeds 6 hero / 10 support words')
        if style=='editorial-thesis-launch':need(len(beat['copy'].split())<=8 and len(beat.get('support','').split())<=20,'editorial copy exceeds 8 hero / 20 support words')
        if beat['visual']=='metric':
            metric=beat.get('metric',{});need(number(metric.get('value')) and nonempty(metric.get('unit')) and nonempty(metric.get('measurement')),'metric needs measured value, unit and methodology/source evidence')
        if beat['visual'] in ('code','diff','terminal','quote'):
            need(any(assets[x]['media_type']=='text' for x in beat['proof_assets']),'text component requires an actual source excerpt asset')
        if beat['visual']=='contrast':need(len(beat['proof_assets'])==2,'contrast requires two comparable proof assets')
        if beat['visual']=='flow':need(isinstance(beat.get('nodes'),list) and 2<=len(beat['nodes'])<=5 and all(nonempty(x) for x in beat['nodes']),'flow requires 2–5 source-backed nodes')
        if beat['visual']=='steps':need(isinstance(beat.get('steps'),list) and 1<=len(beat['steps'])<=5 and all(nonempty(x) for x in beat['steps']),'steps requires 1–5 source-backed steps')
        if beat['visual'] in ('product','artifacts'):need(beat['proof_assets'],'product/artifacts component requires proof assets')
        for cue in beat.get('audio',[]):
            need(isinstance(cue,dict) and nonempty(cue.get('event')) and number(cue.get('offset')) and 0<=cue['offset']<d,'audio cues require an event and offset inside the beat')
        roles.setdefault(beat['role'],[]).append((start,d,real));start+=d
    need(abs(start-b['duration_target'])<=1/b['fps'],'beat durations must sum to duration_target within one frame')
    low,high=RECIPES[style][1]
    need(low<=start<=high or nonempty(p.get('duration_override_reason')),'duration outside style range: supply duration_override_reason')
    if b['voiceover'] is not False:
        need(any(nonempty(x.get('narration')) for x in beats),'voiceover requires authored narration')
        if style in ('kinetic-release-drop','apple-style-micro-launch'):need(nonempty(p.get('voiceover_reason')),'this style needs an explicit voiceover justification')
    else:need(not any(x.get('narration') for x in beats),'narration requires voiceover in brief')
    required={'cinematic-hero-launch':{'thesis'},'feature-reveal':{'friction','reveal','new-workflow','payoff'},'integration-partnership-launch':{'boundary','outcome'},'engineering-pr-to-video':{'problem','diff','mechanism','evidence','impact'}}.get(style,set())
    need(required<=roles.keys(),'missing story roles: '+', '.join(sorted(required-roles.keys())))
    if style=='cinematic-hero-launch':need(first_proof is not None and first_proof<start/2,'hero needs real proof before midpoint')
    if style=='real-product-proof-reel':need(first_proof is not None and first_proof<=10 and grounded/start>=0.7,'proof reel requires proof within 10s and >=70% real evidence runtime')
    if style=='feature-reveal':need(roles['reveal'][0][0]<start*0.6 and any(x[2] for x in roles['friction']) and any(x[2] for x in roles['new-workflow']),'feature needs real before/new workflow and reveal before 60%')
    if style=='integration-partnership-launch':need(grounded>0 and nonempty(b.get('relationship')),'integration requires actual workflow evidence and accurate relationship wording')
    if style=='short-product-launch':need(3<=len(beats)<=5 and first_proof is not None and first_proof<=3 and grounded/start>0.5 and all(d<=3 for _,d,_ in roles.get('cta',[])),'short launch needs 3–5 beats, proof by 3s, majority evidence and <=3s CTA')
    if style=='apple-style-micro-launch':need(all(d<=start*0.2+1/b['fps'] for r in ('sting','cta') for _,d,_ in roles.get(r,[])),'micro ending exceeds 20%')
    if style=='release-notes-changelog':
        need(len(roles.get('headline',[]))<=1 and (len(roles.get('supporting',[]))<=4 or nonempty(p.get('duration_override_reason'))),'changelog exceeds headline/support limits')
        need(nonempty(b.get('version')),'changelog requires exact version')
        need((root/'RELEASE_SELECTION.md').is_file(),'missing RELEASE_SELECTION.md')
    if style=='engineering-pr-to-video':need((root/'PR_SELECTION.md').is_file(),'missing native PR ingestion handoff')
    profile=p.get('motionProfile',{})
    need(profile.get('easing_family') in ('power2','power3','power4'),'unsupported easing family')
    need(profile.get('transition_axis') in ('x','y'),'transition axis must be x/y')
    need(all(number(profile.get(k)) and 0<profile[k]<=1 for k in ('primary_speed','secondary_speed')),'motion speeds must be >0 and <=1 seconds')
    need(profile.get('overshoot')==0,'starter motion supports overshoot 0; author springs in native workflow')
    need(profile.get('camera_behavior') in ('focus','static'),'camera_behavior must be focus/static')
    if p.get('audio_master'):
        local(root,p['audio_master']);need(nonempty(p.get('audio_provenance')),'master requires audio provenance')
    for k in ('logo','logomark'):
        if b['brand_profile'].get(k):local(root,b['brand_profile'][k])
    return b,p,{'status':'structural-pass','factual_review':'required','creative_review':'required','duration':round(start,6),'evidence_ratio':round(grounded/start,4)}

def esc(s):return html.escape(str(s),quote=True)

def asset_html(a,root,start,duration,ident):
    path=esc(a.get('render_path',a['path'])); crop=a.get('crop'); style=''
    if crop:
        style=f' style="width:{100/crop["width"]}%;height:{100/crop["height"]}%;left:{-100*crop["x"]/crop["width"]}%;top:{-100*crop["y"]/crop["height"]}%;position:absolute;object-fit:fill"'
    if a['media_type']=='image':body=f'<img id="{ident}" class="clip" data-start="{start}" data-duration="{duration}" src="{path}" alt="{esc(a["kind"])}"{style}>'
    elif a['media_type']=='video':body=f'<video id="{ident}" class="clip" src="{path}" data-start="{start}" data-duration="{duration}" data-media-start="{a.get("media_start",0)}" data-track-index="{2+int(ident.rsplit("-",1)[-1])}" muted playsinline{style}></video>'
    else:
        lines=local(root,a['path']).read_text().splitlines()
        need(len(lines)<=24 and max(map(len,lines),default=0)<=120,'excerpt too dense; select <=24 lines of <=120 characters')
        body='<pre>'+''.join('<span class="code-line">'+esc(line or ' ')+'</span>' for line in lines)+'</pre>'
    return '<div class="asset">'+body+'</div>'

def compile_scene(beat,b,root,start,i):
    assets={a['id']:a for a in b['proof_assets']};d=beat['duration'];v=beat['visual']
    media=''.join(asset_html(assets[x],root,start,d,f'media-{i}-{j}') for j,x in enumerate(beat['proof_assets']))
    if v=='flow':media='<div class="flow">'+''.join('<div class="node">'+esc(n)+'</div>'+('<div class="connector" aria-hidden="true"></div>' if j<len(beat['nodes'])-1 else '') for j,n in enumerate(beat['nodes']))+'</div>'+media
    if v=='steps':media='<ol>'+''.join('<li>'+esc(s)+'</li>' for s in beat['steps'])+'</ol>'+media
    if v=='metric':media='<div class="metric" data-value="'+str(beat['metric']['value'])+'">'+esc(str(beat['metric']['value'])+' '+beat['metric']['unit'])+'</div>'+media
    tokens=dict(BRAND,**b['brand_profile']);logo=tokens['logomark'] or tokens['logo']
    if v=='identity' and logo:media=f'<img class="logo" src="{esc(logo)}" alt="Kujo">'+media
    if beat['motion']=='cursor':media+='<div class="cursor" aria-hidden="true">↖</div><div class="tap" aria-hidden="true"></div>'
    label='Conceptual visualization' if beat['conceptual'] else ''
    caption=beat.get('caption','')
    return f'''<section id="scene-{i}" class="scene {v}"><div class="scene-fill"></div><div class="visual">
<p class="eyebrow">{esc(b['release_or_feature_name'])} {esc(b.get('version') or '')}</p>
<h1>{esc(beat['copy'])}</h1><p class="support">{esc(beat.get('support',''))}</p>
<div class="proof">{media}</div><p class="label">{esc(label)}</p>
</div><p class="caption">{esc(caption)}</p></section>'''

def prepare(root):
    b,p,report=validate(root)
    # Outputs are regenerated from plan; QA and native ingestion evidence remain human/agent authored.
    out=root/'composition';out.mkdir(exist_ok=True)
    for name in ('motion.js','film.js','style.css'):shutil.copy2(SKILL/'assets'/name,out/name)
    # Vendor the existing repository's GSAP/font, preserving their original licenses.
    vendor=SKILL.parent/'kujo-release-video/assets/project/assets'
    need(vendor.is_dir(),'install kujo-release-video alongside kujo-video-styles for the starter assets')
    shutil.copy2(vendor/'gsap.min.js',out/'gsap.min.js')
    (out/'fonts').mkdir(exist_ok=True)
    for f in (vendor/'fonts').iterdir():
        if f.is_file():shutil.copy2(f,out/'fonts'/f.name)
    tokens=dict(BRAND,**b['brand_profile'])
    compiled_b=json.loads(json.dumps(b))
    (out/'media').mkdir(exist_ok=True)
    def bundle(path):
        original=local(root,path)
        name=hashlib.sha256(original.read_bytes()).hexdigest()[:20]+original.suffix
        shutil.copy2(original,out/'media'/name)
        return 'media/'+name
    for a in compiled_b['proof_assets']:a['render_path']=bundle(a['path'])
    for key in ('logo','logomark'):
        if tokens[key]:tokens[key]=bundle(tokens[key])
    compiled_b['brand_profile']=tokens
    # All rendered media is bundled inside the composition for portable native renders.
    scenes=[];start=0;cue_map=[];sample_times=set();compiled_beats=[]
    for i,beat in enumerate(p['beats']):
        scene=compile_scene(beat,compiled_b,root,start,i)
        scenes.append(scene);compiled_beats.append(dict(beat,start=start))
        sample_times.add(round(start+beat['duration']/2,6))
        if i:sample_times.update(round(max(0,min(b['duration_target']-1/b['fps'],start+off/b['fps'])),6) for off in (-1,0,1))
        cue_map.extend(dict(cue,time=round(start+cue['offset'],6),beat=beat['id']) for cue in beat.get('audio',[]))
        start+=beat['duration']
    width,height={'16:9':(1920,1080),'9:16':(1080,1920),'1:1':(1080,1080)}[b['aspect_ratio']]
    audio=''
    if p.get('audio_master'):audio=f'<audio id="master" class="clip" src="{esc(bundle(p["audio_master"]))}" data-start="0" data-duration="{start}" data-track-index="20" data-volume="1"></audio>'
    source=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(b['release_or_feature_name'])}</title><link rel="stylesheet" href="style.css"></head><body>
<main id="film" data-composition-id="kujo-styles" data-width="{width}" data-height="{height}" data-start="0" data-duration="{start}" data-fps="{b['fps']}" style="width:{width}px;height:{height}px" class="{b['video_type']} {'portrait' if height>width else 'square' if height==width else 'landscape'}">{''.join(scenes)}{audio}</main>
<script src="gsap.min.js"></script><script src="content.js"></script><script src="motion.js"></script><script src="film.js"></script><script>window.__timelines=window.__timelines||{{}};window.__timelines["kujo-styles"]=window.kujoStyleTimeline;</script></body></html>'''
    (out/'index.html').write_text(source)
    payload={'brief':compiled_b,'plan':dict(p,beats=compiled_beats),'brand':tokens}
    (out/'content.js').write_text('window.KUJO = '+json.dumps(payload,ensure_ascii=True).replace('<','\\u003c')+';\n')
    write(out/'hyperframes.json',{'authoringSkill':b['base_workflow'],'paths':{'compositions':'compositions','assets':'assets'}})
    write(root/'brand-tokens.json',dict(BRAND,**b['brand_profile']))
    write(root/'audio-cues.json',cue_map)
    write(root/'voiceover.json',dict(b['resolved_voice'],enabled=b['voiceover'] is not False,
        cues=[{'id':beat['id'],'start':beat['start'],'end':round(beat['start']+beat['duration'],6),
               'text':beat['narration']} for beat in compiled_beats if beat.get('narration')]))
    write(root/'source-assets.json',{'sources':p['sources'],'proof_assets':[dict(a,sha256=hashlib.sha256(local(root,a['path']).read_bytes()).hexdigest()) for a in b['proof_assets']]})
    write(root/'checks.json',dict(report,snapshot_times=sorted(sample_times)))
    write(root/'render-metadata.json',{'status':'not-rendered','composition':'composition/index.html','duration':start,'width':width,'height':height,'fps':b['fps'],'audio':'master-attached' if audio else 'not-produced' if b['voiceover'] or b['music'] or cue_map else 'intentional-silence'})
    (root/'STORYBOARD.md').write_text('# Storyboard\n\n'+''.join('## '+beat['id']+' — '+beat['role']+'\n\n```json\n'+json.dumps(beat,indent=2)+'\n```\n\n' for beat in compiled_beats))
    script=root/'SCRIPT.md'
    if b['voiceover'] is not False:script.write_text('# Narration\n\n'+ '\n\n'.join(f"{beat['id']} ({beat['start']:.3f}s): {beat.get('narration','')}" for beat in compiled_beats)+'\n')
    elif script.exists():script.unlink()
    return dict(report,composition=str(out),snapshot_times=sorted(sample_times),render_status='not-rendered')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    subs=parser.add_subparsers(dest='command',required=True)
    subs.add_parser('list')
    for name in ('route','init'):
        sub=subs.add_parser(name);sub.add_argument('--brief',required=True)
        if name=='init':sub.add_argument('--workspace',required=True)
    for name in ('validate','prepare'):
        sub=subs.add_parser(name);sub.add_argument('--workspace',required=True)
    args=parser.parse_args()
    try:
        if args.command=='list':result=[{'id':k,'default_duration':v[0],'duration_range':v[1],'roles':v[2].split(),'default_voice':resolve_voice({},k)} for k,v in RECIPES.items()]
        elif args.command=='route':result=route(read(args.brief))
        elif args.command=='init':result=init(read(args.brief),Path(args.workspace).resolve())
        elif args.command=='validate':result=validate(Path(args.workspace).resolve())[2]
        else:result=prepare(Path(args.workspace).resolve())
        print(json.dumps({'ok':True,'result':result},ensure_ascii=False))
    except (Invalid,ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps({'ok':False,'error':str(exc)}));return 2
    return 0

if __name__=='__main__':sys.exit(main())
