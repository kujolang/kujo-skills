/* Optional integration gate. Usage: node test_browser.mjs <fixture-parent>
 * <absolute-puppeteer-core-module> <Chrome executable>. Fixtures are prepared by
 * test_video_styles.fixture; this script never captures a real product/account. */
import { createRequire } from 'node:module';
import { readdir, mkdir, writeFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
const [dir,modulePath,executablePath]=process.argv.slice(2);
if(!dir||!modulePath||!executablePath)throw new Error('fixture parent, puppeteer module and Chrome executable required');
const require=createRequire(import.meta.url);
const puppeteer=require(resolve(modulePath));
const browser=await puppeteer.launch({executablePath,headless:true,args:['--allow-file-access-from-files']});
const results=[];
try {
 for(const entry of await readdir(dir,{withFileTypes:true})){
  if(!entry.isDirectory()||entry.name==='snapshots')continue;
  const page=await browser.newPage();const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('requestfailed',r=>errors.push(r.url()+': '+r.failure()?.errorText));
  await page.goto(pathToFileURL(join(resolve(dir),entry.name,'composition/index.html')).href);
  await page.evaluate(()=>document.fonts.ready);
  const data=await page.evaluate(()=>({width:Number(document.getElementById('film').dataset.width),height:Number(document.getElementById('film').dataset.height),beats:KUJO.plan.beats}));
  await page.setViewport({width:data.width,height:data.height,deviceScaleFactor:1});
  const samples=data.beats.map(b=>b.start+b.duration/2);
  // Inspect every settled beat, then compare pixels after reverse/random seeks.
  for(let i=0;i<samples.length;i++){
   await page.evaluate(t=>{window.__timelines['kujo-styles'].seek(t,false);},samples[i]);
   const bad=await page.evaluate(index=>{
    const scene=document.getElementById(`scene-${index}`); const rect=scene.getBoundingClientRect();
    const issues=[];
    if(Number(getComputedStyle(scene).opacity)<0.99)issues.push('active scene invisible');
    for(const el of scene.querySelectorAll('h1,.support,.eyebrow,.caption,.code-line,.node')){
     if(!el.textContent.trim())continue;
     const r=el.getBoundingClientRect();
     if(r.width<=0||r.height<=0)issues.push('collapsed '+el.className);
     if(r.left<rect.left-1||r.right>rect.right+1||r.top<rect.top-1||r.bottom>rect.bottom+1)issues.push('outside canvas '+el.className);
     if(el.scrollWidth>el.clientWidth+2)issues.push('horizontal overflow '+el.className);
    }
    return issues;
   },i);
   assert.deepEqual(bad,[],`${entry.name} beat ${i}: ${bad}`);
  }
  const at=samples[1];
  await page.evaluate(t=>{window.__timelines['kujo-styles'].seek(t,false);},at);
  const first=await page.screenshot();
  for(const t of [samples.at(-1),0,samples[2],at])await page.evaluate(t=>{window.__timelines['kujo-styles'].seek(t,false);},t);
  const again=await page.screenshot();
  assert.equal(createHash('sha256').update(first).digest('hex'),createHash('sha256').update(again).digest('hex'),`${entry.name}: reverse seek pixel mismatch`);
  assert.deepEqual(errors,[],entry.name);
  await mkdir(join(resolve(dir),'snapshots'),{recursive:true});
  await writeFile(join(resolve(dir),'snapshots',entry.name+'.png'),again);
  results.push({fixture:entry.name,beats:samples.length,randomSeekPixels:'identical',runtimeErrors:0});
  await page.close();
 }
} finally { await browser.close(); }
await writeFile(join(resolve(dir),'browser-results.json'),JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify({ok:true,fixtures:results.length,results}));
