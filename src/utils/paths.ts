const base=import.meta.env.BASE_URL.replace(/\/$/,'');

/** Keep local links and public assets inside the deployment's project directory. */
export function sitePath(href:string):string{
  if(!base||!href.startsWith('/')||href.startsWith('//')||href===base||href.startsWith(base+'/'))return href;
  return base+href;
}

export function pagePath(pathname:string):string{
  return base&&pathname.startsWith(base+'/')?pathname.slice(base.length):pathname;
}

export function siteSrcset(srcset:string):string{
  return srcset.split(',').map(candidate=>{
    const [url,...descriptor]=candidate.trim().split(/\s+/);
    return [sitePath(url),...descriptor].join(' ');
  }).join(', ');
}
