# Markdown Logic plugins for OpenAI

OpenAI plugin packages for [Markdown Logic](https://markdownlogic.com/), version 0.2.0.

| Plugin | Source | Package ZIP |
| --- | --- | --- |
| Markdown Logic Public | [openai-public](openai-public/) | [openai-public-0.2.0.zip](dist/openai-public-0.2.0.zip) |
| Markdown Logic | [openai-main](openai-main/) | [openai-main-0.2.0.zip](dist/openai-main-0.2.0.zip) |

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

The authenticated 0.2.0 ZIP contains the intake's five positive and three negative manifest test cases. Its supplemental `review-cases.json` retains all seven positive and five negative scenarios. This correction also documents both authenticated preview and rendering tools; the public package is unchanged.

These packages are locally validated. Publication of this repository does not establish directory approval, live-client compatibility, or completion of connector qualification.

## License and support

The integration files in this repository are licensed under the [MIT License](LICENSE), with the exclusions in [License scope and notices](LICENSE-SCOPE.md).

Support: support@markdownlogic.com · [Privacy](https://markdownlogic.com/privacy) · [Documentation](https://markdownlogic.com/help/en/connect-an-ai-assistant.html)
