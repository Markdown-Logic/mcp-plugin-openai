"""Sync reviewed MDL release skill bytes; never connects, publishes or changes service auth."""
import argparse,hashlib,json,posixpath,re,shutil,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION='0.3.4'
def sha(data):return hashlib.sha256(data).hexdigest()
def export(data,profile,relative):
 text=data.decode('utf-8')
 text=re.sub(r'^  source-revision: [^\n]*\n','',text,flags=re.M)
 text=re.sub(r'^(  version: "[0-9]+\.[0-9]+\.[0-9]+)-candidate("\s*)$',r'\1\2',text,flags=re.M)
 text=text.replace('The prepared converter uses','The MCP converter uses').replace('Its source/configuration may exist before deployment; an empty tools list means conversion is unavailable there.','If `tools/list` does not advertise `convert_markdown`, conversion is unavailable through this connection.')
 prefix='skill://markdown-logic/'+profile+'/'
 # Package-local links preserve the exact workflow while avoiding dependence on
 # a host's ability to resolve server-owned resource URIs across skill packages.
 text=re.sub(re.escape(prefix)+r'([^\s)]+)',lambda m:posixpath.relpath(m[1],posixpath.dirname(relative) or '.'),text)
 return text.encode('utf-8')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--ref',default='release/mdl-production-rc.8.9');args=ap.parse_args();src=args.source_root.resolve()
 ref=subprocess.check_output(['git','rev-parse',args.ref+'^{commit}'],cwd=src,text=True).strip();receipt={'version':VERSION,'canonicalRelease':'rc.8.9','source':'Canonical Markdown Logic released skill definitions; no server implementation included.','adaptation':'Remove internal source-revision/candidate markers; resolve same-profile skill resource links as package-local relative links. Body guidance is otherwise unchanged.','files':{}}
 for profile in ['main','public']:
  prefix='packages/mcp-skills/content/'+profile+'/';paths=subprocess.check_output(['git','ls-tree','-r','--name-only',ref,'--',prefix],cwd=src,text=True).splitlines();assert paths
  dest=ROOT/('openai-'+profile)/'skills';shutil.rmtree(dest);dest.mkdir()
  for path in paths:
   rel=path.removeprefix(prefix);assert '..' not in Path(rel).parts
   mode=subprocess.check_output(['git','ls-tree',ref,'--',path],cwd=src,text=True).split()[0];assert mode=='100644',(path,mode)
   original=subprocess.check_output(['git','show',ref+':'+path],cwd=src);data=export(original,profile,rel);target=dest/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
   receipt['files'][target.relative_to(ROOT).as_posix()]={'canonicalSha256':sha(original),'packagedSha256':sha(data),'adapted':data!=original}
  manifest=ROOT/('openai-'+profile)/'.codex-plugin/plugin.json';v=json.loads(manifest.read_text());v['version']=VERSION
  if profile=='main':v['extensions']['com.openai']['publication']['release_notes']='Adds the distinct Agent memory skill, version-aware refresh with bounded document diffs, attributed append/tail workflows, project discovery metadata, and current security-summary guidance. Existing workflows remain available.'
  manifest.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
  portable=ROOT/('openai-'+profile)/'examples/portable/plugin.json';v=json.loads(portable.read_text());v['version']=VERSION;portable.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'SOURCE-MANIFEST-0.3.4.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({'version':VERSION,'canonicalFiles':len(receipt['files']),'mainSkills':sorted(p.parent.name for p in (ROOT/'openai-main/skills').glob('*/SKILL.md'))},indent=2))
if __name__=='__main__':main()
