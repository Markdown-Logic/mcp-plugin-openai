## Convert supplied Markdown without an account

Send the complete Markdown, up to **128 KiB** (131,072 UTF-8 bytes). The result is an embedded base64 file, up to **2 MiB** (2,097,152 bytes); your client must save or attach those bytes. Its URI is not a hosted download or permanent link. Public conversion reads no private files or projects and never fetches remote URLs or images.

Current conversion budgets are **3 per minute per network address**, **20 per UTC day per address**, and **80 per UTC day shared across public users**. A separate limit of 20 MCP POST requests per 60 seconds also covers discovery. These are maximum sizes and capacity budgets: conversion can fail below them. On a capacity refusal, wait; do not automatically retry a refusal or uncertain result, shorten the source, or claim a file was created.
