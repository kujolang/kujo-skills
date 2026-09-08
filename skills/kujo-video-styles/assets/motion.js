/* Kujo shared motion. All functions append to the caller's paused GSAP timeline.
 * No clocks, callbacks, randomness, media playback or unregistered timelines.
 * t/d are seconds; target is an element or scoped selector. */
(function (scope) {
  function create(tl, profile) {
    const axis = profile.transition_axis || 'x';
    const ease = `${profile.easing_family || 'power3'}.out`;
    const speed = profile.primary_speed || 0.5;
    const move = (target, from, to, t, d = speed) => tl.fromTo(target, from, { ...to, duration: d, ease, immediateRender: false }, t);
    const api = {
      enter: (el,t,d) => move(el,{[axis]:60,opacity:0},{[axis]:0,opacity:1},t,d),
      exit: (el,t,d) => move(el,{[axis]:0,opacity:1},{[axis]:-60,opacity:0},t,d),
      maskReveal: (el,t,d) => move(el,{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)'},t,d),
      scaleThrough: (el,t,d) => move(el,{scale:0.88,opacity:0},{scale:1,opacity:1},t,d),
      push: (el,t,d) => move(el,{[axis]:100,opacity:0},{[axis]:0,opacity:1},t,d),
      pull: (el,t,d) => move(el,{[axis]:-100,opacity:0},{[axis]:0,opacity:1},t,d),
      // Equal distance/time and linear velocity at a seam; overlap clips in a native
      // composition for a continuous handoff instead of pretending a cut is matched.
      velocityHandoff: (outgoing,incoming,t,d=speed,distance=100) => {
        tl.fromTo(outgoing,{[axis]:0},{[axis]:-distance,duration:d,ease:'none',immediateRender:false},t);
        tl.fromTo(incoming,{[axis]:distance},{[axis]:0,duration:d,ease:'none',immediateRender:false},t);
      },
      cursor: (el,t,d) => move(el,{x:110,y:100,opacity:0},{x:0,y:0,opacity:1},t,d),
      tap: (el,t,d=0.3) => move(el,{scale:0.4,opacity:1},{scale:1.5,opacity:0},t,d),
      codeReveal: (els,t,d=1) => {
        const list=Array.from(els);
        list.forEach((el,i)=>move(el,{opacity:0,x:12},{opacity:1,x:0},t+i*d/Math.max(1,list.length),Math.min(0.2,d/Math.max(1,list.length))));
      },
      kineticType: (el,t,d) => move(el,{y:45,scale:1.08,opacity:0},{y:0,scale:1,opacity:1},t,d),
      logoSting: (el,t,d) => move(el,{scale:0.8,opacity:0},{scale:1,opacity:1},t,d),
      captionRail: (el,t,d) => move(el,{y:16,opacity:0},{y:0,opacity:1},t,d),
      spotlight: (el,t,d) => move(el,{filter:'brightness(0.65)'},{filter:'brightness(1)'},t,d),
      zoomToDetail: (el,t,d=1) => move(el,{scale:0.97},{scale:1},t,d),
      artifactFan: (els,t,d=speed) => Array.from(els).forEach((el,i)=>move(el,{y:90,rotation:-4*(i+1),opacity:0},{y:0,rotation:0,opacity:1},t+i*0.1,d)),
      // Number content remains the exact measured value; reveal its magnitude with
      // a width/scale emphasis. countUp is for pre-authored digit strips (no callbacks).
      metricEmphasis: (el,t,d) => move(el,{scale:0.7,opacity:0},{scale:1,opacity:1},t,d),
      countUp: (digitStrip,t,d=1,steps=10) => move(digitStrip,{yPercent:0},{yPercent:-100*(steps-1)/steps},t,d),
      connector: (els,t,d=0.7) => move(els,{scaleX:0,transformOrigin:'left center'},{scaleX:1},t,d),
      texture: (el,t,d) => move(el,{opacity:0},{opacity:0.035},t,d),
      lineFocus: (el,t,d) => move(el,{backgroundColor:'transparent'},{backgroundColor:'rgba(128,128,128,.16)'},t,d),
      panelExpand: (el,t,d) => move(el,{clipPath:'inset(40% 15% 40% 15%)'},{clipPath:'inset(0% 0% 0% 0%)'},t,d),
      loopResolve: (el,t,d) => move(el,{scale:1.08},{scale:1},t,d),
      audioCue: (name,t) => tl.addLabel(`audio:${name}:${t}`,t),
    };
    // Vocabulary used by the supplied style specifications.
    api.heroReveal=api.maskReveal;api.pushThrough=api.scaleThrough;
    api.macroZoom=api.zoomToDetail;api.artifactCascade=api.artifactFan;
    api.thesisType=api.kineticType;api.logoResolve=api.logoSting;
    return api;
  }
  scope.KujoMotion={create};
})(typeof window==='undefined' ? globalThis : window);
