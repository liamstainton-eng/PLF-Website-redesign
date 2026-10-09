import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const records=JSON.parse(fs.readFileSync('src/data/content.json','utf8'));
const base=(process.env.PLF_BASE_PATH||'/').replace(/\/$/,'');
const deployedPath=href=>base+href;
const failures=[];
const files=[];
function walk(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,entry.name);if(entry.isDirectory())walk(p);else if(p.endsWith('.html'))files.push(p);}}
walk('dist');
const decode=s=>s.replace(/&#(x[\da-f]+|\d+);/gi,(_,c)=>String.fromCodePoint(c[0].toLowerCase()==='x'?parseInt(c.slice(1),16):+c)).replace(/&(amp|quot|apos|lt|gt|nbsp);/g,(_,c)=>({amp:'&',quot:'"',apos:"'",lt:'<',gt:'>',nbsp:' '})[c]);
const norm=s=>decode(s).toLowerCase().replace(/\s+/g,' ').trim();
const text=html=>norm(html.replace(/<script\b[^>]*>[\s\S]*?<\/script>/g,'').replace(/<[^>]+>/g,' '));
const routeFile=route=>route==='/'?path.join('dist','index.html'):path.join('dist',route.slice(1),'index.html');
for(const file of files){
 const html=fs.readFileSync(file,'utf8');
 if((html.match(/<h1\b/g)||[]).length!==1)failures.push(`${file}: expected one H1`);
 if(!/noindex,\s*nofollow/.test(html))failures.push(`${file}: preview index protection missing`);
 for(const tag of html.match(/<img\b[^>]*>/g)||[]){if(!/\balt(?:=|\s|>)/.test(tag)||!tag.includes('width=')||!tag.includes('height='))failures.push(`${file}: image description or dimensions missing`);}
 const references=[...html.matchAll(/\b(?:href|src|data-gallery-src)="([^"]+)"/g)].map(match=>decode(match[1]));
 for(const [,srcset] of html.matchAll(/\bsrcset="([^"]+)"/g))references.push(...decode(srcset).split(',').map(candidate=>candidate.trim().split(/\s+/)[0]));
 for(const href of new Set(references)){
  if(!href.startsWith('/')||href.startsWith('//'))continue;
  if(base&&!href.startsWith(base+'/')){failures.push(`${file}: link escapes deployment base ${href}`);continue;}
  const [raw,hash]=href.slice(base.length).split('#');const target=raw.endsWith('/')?routeFile(raw):path.join('dist',raw.slice(1));
  if(!fs.existsSync(target)){failures.push(`${file}: missing ${href}`);continue;}
  if(hash&&target.endsWith('.html')&&!fs.readFileSync(target,'utf8').includes(`id="${hash}"`))failures.push(`${file}: missing anchor ${href}`);
 }
}
let paragraphs=0;
for(const prefix of ['','/demo-2']){
for(const record of records){
 const file=routeFile(prefix+record.route);if(!fs.existsSync(file)){failures.push(`Missing original route ${prefix+record.route}`);continue;}
 if(crypto.createHash('sha256').update(record.body).digest('hex')!==record.sourceBodySha256)failures.push(`Source hash changed: ${record.route}`);
 const html=fs.readFileSync(file,'utf8');const rendered=text(html);
 // The captured agency page was a 404; its useful replacement is documented.
 if(record.route!=='/agency-referral/')for(const p of record.paragraphs){
  if(record.kind==='event'&&['« All Events','This event has passed.'].includes(p))continue;
  if(!rendered.includes(norm(p)))failures.push(`Missing source paragraph on ${record.route}: ${p.slice(0,70)}`);
  paragraphs++;
 }
 if(record.kind==='event'&&!html.includes('Booking is closed'))failures.push(`Open historic booking: ${record.route}`);
}
for(const route of ['/get-support/','/referral-forms/self-referral/','/agency-referral/'])if(/<form\b/.test(fs.readFileSync(routeFile(prefix+route),'utf8')))failures.push(`Sensitive form rendered on ${prefix+route}`);
if(!fs.readFileSync(routeFile(prefix+'/donate/'),'utf8').includes('https://www.justgiving.com/charity/paullavellefoundation'))failures.push('Donation handoff changed');
}
for(const file of files.filter(file=>file.includes('demo-2'))){for(const [,href] of fs.readFileSync(file,'utf8').matchAll(/href="(\/[^\"]*)"/g)){if(href!==deployedPath('/')&&href!==deployedPath('/compare/')&&!href.startsWith(deployedPath('/demo-2/'))&&!href.startsWith(deployedPath('/documents/'))&&!href.startsWith(deployedPath('/_astro/')))failures.push(`Second demo leaves its route space: ${file}: ${href}`);}}
for(const name of fs.readdirSync('dist/_astro').filter(name=>name.endsWith('.css'))){
 const css=fs.readFileSync(path.join('dist/_astro',name),'utf8');
 for(const [,href] of css.matchAll(/url\(["']?(\/[^\s)"']+)/g)){
  if((base&&!href.startsWith(base+'/'))||!fs.existsSync(path.join('dist',href.slice(base.length+1))))failures.push(`${name}: missing or unprefixed CSS asset ${href}`);
 }
}
if(failures.length){console.error(failures.join('\n'));process.exit(1);}
console.log(`Verified ${files.length} built pages at ${base||'/'}, ${records.length} original routes in each demo, ${paragraphs} source paragraphs across both demos, local links/assets/srcsets, archived bookings and referral boundaries.`);
