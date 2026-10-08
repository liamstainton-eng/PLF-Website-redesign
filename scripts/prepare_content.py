"""Prepare source-backed content and responsive images; never modify the audit."""
import csv, hashlib, json, re, shutil
from pathlib import Path
from urllib.parse import urlparse
from PIL import Image, ImageOps

root = Path(__file__).resolve().parents[2]
project = root / 'plf-website-redesign'
hand = root / 'PLF Website Redesign Handover'
pages = json.loads((hand/'site-extraction.json').read_text(encoding='utf-8-sig'))
manifest = json.loads((hand/'image-manifest.json').read_text(encoding='utf-8-sig'))
for folder in ['src/data','public/images','public/documents','docs','scripts']:
    (project/folder).mkdir(parents=True,exist_ok=True)
lookup = {m['url']:m for m in manifest if m.get('status')=='downloaded'}
selected = {}
def add_image(local, key=None):
    entry=next((m for m in manifest if m.get('localPath')==local),None)
    if not entry:return None
    key=key or Path(local).stem
    if key in selected:return key
    source=hand/local
    try:
        im=ImageOps.exif_transpose(Image.open(source)).convert('RGBA' if source.suffix=='.png' else 'RGB')
    except Exception:return None
    w,h=im.size
    variants=[]
    for size in [480,800,1280,1600]:
        width=min(w,size)
        if any(v['width']==width for v in variants):continue
        copy=im.copy();copy.thumbnail((width,round(h*width/w)),Image.Resampling.LANCZOS)
        filename=f'{key}-{width}.webp';copy.save(project/'public/images'/filename,'WEBP',quality=86,method=6)
        variants.append({'width':width,'src':'/images/'+filename})
    selected[key]={'key':key,'width':w,'height':h,'src':variants[-1]['src'],'srcset':', '.join(f"{v['src']} {v['width']}w" for v in variants),'sourceUrl':entry['url'],'sourcePath':local,'sha256':entry['sha256']}
    return key

for key,filename in {'logo':'PLF-Logomark--49ec81ccdcc2.png','hero':'The-PLF-LEJOG-Team-at-Claire-House-Wirral--8473da8ed4e7.jpg','cycling':'Cycling-club-pic--cef9904ea1b5.jpg','swimming':'Open-swimming-pic--9f315812cb77.jpg','running':'running-club--096716d3688b.jpg','paul':'PLF-Home_0009_IMG10--1339a5595b3f.jpg','liverpool':'liv-img-3--48ef6219ebb7.jpg','walking':'snowdon-2--4713032d7f08.jpg'}.items():
    add_image('images/'+filename,key)

records=[]
shared_footer=''
for page in pages:
    url=page['url'];route=urlparse(url).path or '/'
    if urlparse(url).netloc not in ['paullavellefoundation.co.uk','www.paullavellefoundation.co.uk']:continue
    original=page.get('text','').replace('\xa0',' ')
    body=original.split('Quick Exit',1)[-1].strip()
    footer=re.search(r'\nTelephone Numbers\s*\n',body)
    if footer:
        if not shared_footer:shared_footer=body[footer.start():].split('Copyright',1)[0].strip()
        body=body[:footer.start()].strip()
    body=re.sub(r'[\ue000-\uf8ff]','',body)
    body=re.sub(r'\n[ \t]+\n','\n\n',body)
    body=re.sub(r'\n{3,}','\n\n',body).strip()
    title=re.sub(r'\s*[-–]\s*Paul Lavelle Foundation\s*$','',page.get('title','')).strip()
    if route=='/':title='Home'
    if route=='/agency-referral/':title='Professional referrals'
    category='event' if route.startswith('/event/') else 'archive' if route.startswith(('/events/','/news')) or re.match(r'^/\d{4}/\d{2}/$',route) else 'article' if re.match(r'^/\d{4}/\d{2}/\d{2}/',route) else 'referral' if 'referral' in route else 'policy' if 'policy' in route else 'service'
    links=[]
    for l in page.get('links',[]):
        href=l.get('href','');label=' '.join(l.get('label','').split())
        if not href or not label or href.startswith(('javascript:','#')):continue
        parsed=urlparse(href)
        if parsed.netloc in ['paullavellefoundation.co.uk','www.paullavellefoundation.co.uk'] and not parsed.path.startswith('/wp-content/'):
            href=(parsed.path or '/')+('#'+parsed.fragment if parsed.fragment else '')
        pair={'href':href,'label':label}
        if pair not in links:links.append(pair)
    pics=[]
    for entry in page.get('details',{}).get('images',[]):
        image=lookup.get(entry.get('src',''))
        if not image or 'Logomark' in image['localPath'] or Path(image['localPath']).suffix.lower() not in ['.jpg','.jpeg','.png']:continue
        try:
            w,h=Image.open(hand/image['localPath']).size
            if w<500 or h<220:continue
        except Exception:continue
        key=add_image(image['localPath'])
        if key and key not in pics:pics.append(key)
        if len(pics)>=2:break
    chunks=[c.strip() for c in re.split(r'\n\s*\n',body) if c.strip()]
    when=next((line.strip() for line in body.splitlines() if re.match(r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d',line.strip())), '')
    if category=='event':
        when=when or 'Archived event'
        # First date line sometimes belongs to an event heading; retained source metadata remains authoritative.
    record={'route':route,'url':url,'title':title,'kind':category,'body':body,'paragraphs':chunks,'links':links,'images':pics,'when':when,'status':'past' if 'This event has passed.' in body else 'archived','sourceBodySha256':hashlib.sha256(body.encode()).hexdigest()}
    records.append(record)

(project/'src/data/content.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
(project/'src/data/images.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf-8')
(project/'docs/asset-provenance.json').write_text(json.dumps(list(selected.values()),ensure_ascii=False,indent=2),encoding='utf-8')
(project/'docs/shared-contact-source.txt').write_text(shared_footer,encoding='utf-8')
with (project/'docs/route-coverage.csv').open('w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f);writer.writerow(['source_url','source_title','demo_route','disposition','content_sha256'])
    for item in records:writer.writerow([item['url'],item['title'],item['route'],'Local route; curated layout with retained source details' if item['kind']!='referral' else 'Local entry with external handoff; no sensitive form',item['sourceBodySha256']])
    for item in pages:
        if 'justgiving.com' in urlparse(item['url']).netloc:writer.writerow([item['url'],item['title'],'/donate/','External provider; checkout is not simulated',''])
shutil.copy2(root/'PLF-Fundraising-Pack.pdf',project/'public/documents/PLF-Fundraising-Pack.pdf')
shutil.copy2(root/'PLF-Safeguarding-Adults-Policy.pdf',project/'public/documents/PLF-Safeguarding-Adults-Policy.pdf')
shutil.copy2(root/'PLF-DEMO-PLAN.md',project/'docs/IMPLEMENTATION-PLAN.md')
shutil.copy2(root/'research/repositories/astrowind/LICENSE.md',project/'docs/AstroWind-LICENSE.md')
print(f'{len(records)} routes; {len(selected)} source images; all route bodies hashed')
