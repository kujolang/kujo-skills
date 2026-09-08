/* One root timeline. Untimed scene shells permit timed video children; HyperFrames
 * alone owns media timing/playback. Only the shell's visual state is animated. */
const { brief, plan, brand } = window.KUJO;
const root=document.getElementById('film');
for (const [key,value] of Object.entries(brand)) root.style.setProperty(`--${key}`,value);
const tl=gsap.timeline({paused:true});
const motion=KujoMotion.create(tl,plan.motionProfile);
plan.beats.forEach((beat,i)=>{
  const scene=document.getElementById(`scene-${i}`);
  const visual=scene.querySelector('.visual');
  const proof=scene.querySelector('.proof');
  const title=scene.querySelector('h1');
  const t=beat.start;
  const d=Math.min(plan.motionProfile.primary_speed,beat.duration/4);
  tl.set(scene,{autoAlpha:0},0);
  tl.set(scene,{autoAlpha:1},t);
  if(i<plan.beats.length-1)tl.set(scene,{autoAlpha:0},t+beat.duration);
  if(beat.transition_in==='push')motion.push(visual,t,d);
  if(beat.transition_in==='pull')motion.pull(visual,t,d);
  if(beat.transition_in==='scale')motion.scaleThrough(visual,t,d);
  if(beat.transition_in==='mask')motion.maskReveal(visual,t,d);
  const actions={
    mask:()=>motion.maskReveal(title,t,d),
    zoom:()=>plan.motionProfile.camera_behavior==='static' ? motion.enter(proof,t,d) : motion.zoomToDetail(proof,t,beat.duration*0.7),
    fan:()=>motion.artifactFan(proof.querySelectorAll('.asset'),t,d),
    type:()=>motion.kineticType(title,t,d),
    logo:()=>motion.logoSting(scene.querySelector('.logo')||title,t,d),
    focus:()=>motion.spotlight(proof,t,d),
    cursor:()=>{motion.cursor(scene.querySelector('.cursor'),t+d,d);motion.tap(scene.querySelector('.tap'),t+2*d);},
    expand:()=>motion.panelExpand(proof,t,d),
    push:()=>motion.push(proof,t,d),
    code:()=>motion.codeReveal(scene.querySelectorAll('.code-line'),t,Math.min(2,beat.duration*0.65)),
    connector:()=>motion.connector(scene.querySelectorAll('.connector'),t+d,Math.min(1,beat.duration*0.4)),
    stagger:()=>motion.codeReveal(scene.querySelectorAll('li'),t,Math.min(2,beat.duration*0.6)),
    metric:()=>motion.metricEmphasis(scene.querySelector('.metric'),t,d),
  };
  actions[beat.motion]();
  if(beat.visual==='diff')motion.lineFocus(scene.querySelector('.code-line'),t+d,d);
  if(beat.caption)motion.captionRail(scene.querySelector('.caption'),t+d,Math.min(d,plan.motionProfile.secondary_speed));
  for(const cue of beat.audio||[])motion.audioCue(cue.event,t+cue.offset);
  // End treatment is local to the outgoing visual. Author an overlapping native
  // velocityHandoff when a shot calls for shared-object continuity.
  const exitAt=t+beat.duration-d;
  if(i<plan.beats.length-1){
    if(beat.transition_out==='push')motion.exit(visual,exitAt,d);
    if(beat.transition_out==='pull')tl.to(visual,{[plan.motionProfile.transition_axis]:60,opacity:0,duration:d,ease:`${plan.motionProfile.easing_family}.in`},exitAt);
    if(beat.transition_out==='scale')tl.to(visual,{scale:1.08,opacity:0,duration:d},exitAt);
    if(beat.transition_out==='mask')tl.to(visual,{clipPath:'inset(0 0 0 100%)',duration:d},exitAt);
  }
});
window.kujoStyleTimeline=tl;
