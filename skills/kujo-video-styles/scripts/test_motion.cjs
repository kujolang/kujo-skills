const assert=require('node:assert/strict');
require('../assets/motion.js');
const calls=[];
const tl={fromTo(...args){calls.push(args);return this},addLabel(...args){calls.push(args);return this}};
const m=globalThis.KujoMotion.create(tl,{easing_family:'power3',transition_axis:'x'});
for(const name of ['enter','exit','maskReveal','scaleThrough','push','pull','cursor','tap','kineticType','logoSting','captionRail','spotlight','zoomToDetail','metricEmphasis','countUp','connector','texture','lineFocus','panelExpand','loopResolve'])m[name]({},2,0.5);
m.codeReveal([{},{}],3,1);m.artifactFan([{},{}],3,1);
const before=calls.length;m.velocityHandoff('out','in',4,0.5,120);
assert.equal(calls[before][2].x,-120);assert.equal(calls[before+1][1].x,120);
assert.equal(calls[before][2].ease,'none');assert.equal(calls[before+1][2].ease,'none');
for(const c of calls){assert.equal(c[2].immediateRender,false);assert.ok(Number.isFinite(c[2].duration));}
m.audioCue('click',5);assert.deepEqual(calls.at(-1),['audio:click:5',5]);
console.log('Shared motion construction and matched-velocity contract passed');
