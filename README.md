# Markdown Logic plugins for OpenAI

OpenAI plugin packages for [Markdown Logic](https://markdownlogic.com/), version 0.3.5.

| Plugin | Source | Package ZIP |
| --- | --- | --- |
| Markdown Logic Public | [openai-public](openai-public/) | [openai-public-0.3.5.zip](dist/openai-public-0.3.5.zip) |
| Markdown Logic | [openai-main](openai-main/) | [openai-main-0.3.5.zip](dist/openai-main-0.3.5.zip) |

The public plugin converts complete supplied Markdown to PDF, DOCX, HTML or EPUB without an account. The authenticated plugin supports team document workflows through browser OAuth. Each source folder includes its own manifest, remote MCP configuration, Skills, setup documentation, and license notices.

Package ZIPs match the corresponding source folders. Verify downloads against [SHA256SUMS](dist/SHA256SUMS):

```sh
cd dist
shasum -a 256 -c SHA256SUMS
```

## Connections

| Profile | MCP endpoint | Authentication |
| --- | --- | --- |
| Public | `https://markdownlogic.com/mcp` | None |
| Team documents | `https://mcp.markdownlogic.com` | Browser OAuth |

See each source folder's README for setup, capabilities, and limits.

## Directory submission

Upload the ZIP for the intended profile through [OpenAI's Plugins dashboard](https://platform.openai.com/plugins). Follow [OpenAI's submission instructions](https://developers.openai.com/plugins/deploy/submission), connect the matching MCP server, resolve automated findings, and complete the review materials before submitting.

The authenticated 0.3.5 ZIP contains the intake's five positive and three negative manifest test cases. Its supplemental `review-cases.json` retains all seven positive and five negative scenarios. All six authenticated workflows are included, with agent-memory as a distinct entrypoint. The public package remains limited to its two anonymous workflows.

These packages are locally validated. Publication of this repository does not establish directory approval, live-client compatibility, or completion of connector qualification.

## License and support

The integration files in this repository are licensed under the [MIT License](LICENSE), with the exclusions in [License scope and notices](LICENSE-SCOPE.md).

Support: support@markdownlogic.com · [Privacy](https://markdownlogic.com/privacy) · [Documentation](https://markdownlogic.com/help/en/connect-an-ai-assistant.html)

See [0.3.5 changes and qualification](RELEASE-0.3.5.md). Refresh or re-import the plugin after uploading; cached tools and skills in an existing chat do not establish what a new connection advertises.

## Authenticated skills

The account package includes six workflows: Agent memory, API integration planner, Convert/render, Project artifacts, Research projects and Structured analysis. Agent memory uses ordinary authorized documents, exact version identities, bounded deltas, and attributed append logs. It does not create a separate memory database or grant new permissions.

The server retains a five-entry legacy importer listing for compatibility; its modern discovery exposes all six, and exact memory lookup/resources are available. That protocol projection is distinct from the six skills bundled in this ZIP. Public conversion does not include authenticated memory or private project access.

## Build and verify

Use `python3 tools/build-packages.py --out <new-output-directory>` to reproduce the current ZIPs, then `python3 -m unittest discover -s tests -v` for package/authentication/link/digest checks. `SOURCE-MANIFEST-0.3.5.json` records canonical and packaged skill hashes and the relative-link adaptation. The sync utility accepts a separately authorized canonical checkout; no private source checkout or service credentials are distributed.
