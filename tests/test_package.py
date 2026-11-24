import hashlib,json,re,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION='0.3.6'
MAIN={'agent-memory','agent-workspace-collaboration','api-integration-planner','convert-render','project-artifacts','research-projects','structured-analysis'}
PUBLIC={'public-conversion-help','public-markdown-conversion'}
class PackageTests(unittest.TestCase):
 def test_authenticated_catalogue_retains_five_and_adds_distinct_memory(self):
  self.assertEqual({p.parent.name for p in (ROOT/'openai-main/skills').glob('*/SKILL.md')},MAIN)
  content=(ROOT/'openai-main/skills/agent-memory/SKILL.md').read_text()
  self.assertIn('references/agent-memory.md',content)
  memory=(ROOT/'openai-main/skills/project-artifacts/references/agent-memory.md').read_text()
  for term in ['diff_document_versions','append_document','tail_document','metadataOnly']:
   self.assertIn(term,memory)
 def test_public_projection_is_separate(self):
  self.assertEqual({p.parent.name for p in (ROOT/'openai-public/skills').glob('*/SKILL.md')},PUBLIC)
  self.assertNotIn('agent-memory',' '.join(p.name for p in (ROOT/'openai-public/skills').iterdir()))
 def test_versions_auth_and_review_contract(self):
  for profile in ['main','public']:
   root=ROOT/('openai-'+profile);manifest=json.loads((root/'.codex-plugin/plugin.json').read_text());portable=json.loads((root/'examples/portable/plugin.json').read_text())
   self.assertEqual(manifest['version'],VERSION);self.assertEqual(portable['version'],VERSION)
   self.assertEqual(manifest['skills'],'./skills/');self.assertEqual(manifest['mcpServers'],'./.mcp.json')
   cases=manifest['extensions']['com.openai']['review']['test_cases'];self.assertEqual(len(cases['positive']),5);self.assertEqual(len(cases['negative']),3)
   server=next(iter(json.loads((root/'.mcp.json').read_text())['mcpServers'].values()))
   self.assertEqual(server['url'],'https://mcp.markdownlogic.com' if profile=='main' else 'https://markdownlogic.com/mcp')
   self.assertEqual(server['extensions']['com.openai']['auth']['type'],'oauth' if profile=='main' else 'none')
 def test_all_skill_markdown_links_resolve_and_remain_inside_profile(self):
  for profile in ['main','public']:
   base=ROOT/('openai-'+profile)
   for p in (base/'skills').rglob('*.md'):
    text=p.read_text();self.assertNotIn('skill://markdown-logic/',text,str(p))
    for target in re.findall(r'\]\(([^)\s]+)(?:\s+[^)]*)?\)',text):
     if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
     candidate=(p.parent/target.split('#')[0]).resolve();self.assertTrue(candidate.is_relative_to(base.resolve()),(p,target));self.assertTrue(candidate.is_file(),(p,target))
 def test_archive_bytes_match_source_and_safe_root(self):
  for profile in ['main','public']:
   folder=ROOT/('openai-'+profile);archive=ROOT/'dist'/f'openai-{profile}-{VERSION}.zip'
   with zipfile.ZipFile(archive) as z:
    expected={p.relative_to(folder).as_posix():p.read_bytes() for p in folder.rglob('*') if p.is_file()}
    self.assertEqual(set(z.namelist()),set(expected));self.assertIsNone(z.testzip());self.assertIn('.codex-plugin/plugin.json',z.namelist())
    for name,data in expected.items():self.assertEqual(z.read(name),data,name)
 def test_exported_provenance_has_no_private_source_or_secrets(self):
  receipt=json.loads((ROOT/'SOURCE-MANIFEST-0.3.6.json').read_text())
  self.assertEqual(receipt['canonicalRelease'],'rc.8.12');self.assertEqual(receipt['version'],VERSION)
  for rel,row in receipt['files'].items():self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),row['packagedSha256'])
  for profile in ['main','public']:
   for p in (ROOT/('openai-'+profile)).rglob('*'):
    if p.is_file():
     data=p.read_bytes();self.assertNotIn(b'/Users/pauld/',data,str(p));self.assertNotIn(b'gitlab.com/lemuridae-labs/markdownlogic',data,str(p));self.assertNotIn(b'source-revision:',data,str(p))
if __name__=='__main__':unittest.main()
