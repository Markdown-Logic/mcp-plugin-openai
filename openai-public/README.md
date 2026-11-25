# Markdown Logic Public

Convert your Markdown into PDF, DOCX, HTML or EPUB—no Markdown Logic account required.

## Connection

Endpoint: `https://markdownlogic.com/mcp`

Authentication: `none`

Use this package’s declared anonymous hosted connection. It requires no account, credentials, or browser sign-in.

The package includes remote-server configuration and workflow Skills. Skills provide instructions; they grant no permissions and add no server tools. Call only the tools actually advertised by the connected server.

## Files and limits

The anonymous service converts complete supplied Markdown to PDF, DOCX, HTML or EPUB. It cannot read private projects or fetch remote URLs. Current limits are 128 KiB of UTF-8 Markdown and 2 MiB of generated file bytes, with additional request and shared-capacity limits. Preserve the complete source. Stop on capacity refusals or uncertain results; do not silently shorten a document or retry in a loop.

File saving, attachments, Skills loading and interactive interfaces depend on the client. An embedded-file resource URI does not by itself provide a hosted or permanent download. Save or attach the actual returned bytes when supported, preserving their filename and media type. Report a refusal or unsupported file operation accurately.

Read [setup instructions and limits](help/en.md), browse [localized help](help/), and see the [localized descriptions](listing-translations.json) and [example test scenarios](review-cases.json).

## License and support

First-party configuration, Skills, documentation and the original geometric integration icon included in this package are licensed under the [MIT License](LICENSE), subject to the [license scope and notices](LICENSE-SCOPE.md). The private Markdown Logic platform remains under its existing terms. Product and third-party names, trademarks and logos are excluded from the copyright grant; third-party components retain their own licenses and notices. The license grants no right to imply endorsement.

Support: support@markdownlogic.com. [Markdown Logic](https://markdownlogic.com/) · [Privacy](https://markdownlogic.com/privacy) · [Terms](https://markdownlogic.com/terms).

This package contains only the two public conversion/help skills. It cannot retrieve authenticated memory, private projects or their properties. Use the separate authenticated package for team documents.
