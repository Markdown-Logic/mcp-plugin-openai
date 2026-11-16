"""Build root-layout deterministic OpenAI upload ZIPs from this repository."""
import argparse,hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build(destination):
 destination.mkdir(parents=True,exist_ok=True);archives=[]
 for profile in ['main','public']:
  root=ROOT/('openai-'+profile);manifest=json.loads((root/'.codex-plugin/plugin.json').read_text());version=manifest['version'];dest=destination/f'openai-{profile}-{version}.zip'
  with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_STORED) as z:
   for p in sorted(root.rglob('*')):
    if p.is_symlink():raise ValueError('Symlink is not distributable: '+str(p))
    if not p.is_file():continue
    rel=p.relative_to(root).as_posix()
    if any(x in ['.DS_Store','__MACOSX'] or x.startswith('._') for x in p.parts):raise ValueError('OS metadata is not distributable')
    info=zipfile.ZipInfo(rel,(2026,11,16,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;z.writestr(info,p.read_bytes())
  archives.append({'name':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'bytes':dest.stat().st_size})
 sums=destination/'SHA256SUMS';sums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(destination.glob('*.zip'))))
 return archives
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=ROOT/'dist');a=ap.parse_args();print(json.dumps(build(a.out),indent=2))
