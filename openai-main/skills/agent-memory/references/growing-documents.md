# Working efficiently with large or growing documents

Use these patterns when repeated reads or small writes are making an authorized
workflow unnecessarily expensive. They are agent workflow guidance, not a new
storage model, permission grant, automatic background job or size policy. Use
the connected server's advertised tools and limits; do not assume every client
or deployment supports every option.

## Organize for the question

Keep a concise index of purpose, stable document IDs, task or time coverage,
status and useful source references. For an ongoing log, use separate documents
by meaningful task or time period when that improves retrieval. Point the index
to the active shard and retained history. Choose boundaries from the workflow,
not an arbitrary byte or line cutoff. A small coherent document may be simpler
than an index and many fragments.

Create or reorganize documents only within the user's authorized scope. Do not
silently split, rewrite, archive or delete existing material. Preserve evidence
links and exact version references; a summary or index is a navigation aid, not
a replacement for source evidence. Update the index when its pointers or meaning
change, not after every appended line.

## Read only what the task needs, with a valid identity

- Start from the relevant index or task shard, rather than reading all project
  history. List/search results are discovery leads; retrieve the authorized
  source needed to support the answer.
- Keep the exact document/version identity with cached content. When qualified
  metadata is available, `read_document` with `metadataOnly: true` can establish
  whether the head changed. Do not combine it with `versionId`. Avoid rereading
  an unchanged, verified cached revision merely to repeat the same analysis.
  Identity is not authority: do not use cached content to bypass current access
  restrictions or assume independent properties are unchanged.
- For changed retained versions, follow the canonical memory workflow's complete
  delta and hash/length validation. An unavailable delta is not proof of no
  change. Prefer an authorized exact-version whole-source read when the task
  needs full context, the cache cannot be verified, or reconstruction is unsafe.
  Do not silently retrieve a large body the task does not need.
- Use `tail_document` only when recent lines of an append-oriented log answer
  the question. A tail is partial evidence, not a document summary or a general
  change detector. Its bounded returned window reduces material sent to the
  agent; **it does not promise less server-side source reading or processing**.
  The current tool describes bounded full-source work. Follow its receipt,
  `hasMore` and cursor behavior. Continue with the same document ID and cursor,
  without new line/byte options; if source/access changes or the cursor expires,
  request an explicit fresh read only if still authorized and needed. Empty
  output with `line-too-large` is not an empty document.

## Write in deliberate small batches

Combine small related log entries into one authorized `append_document` call
when they belong to the same target and logical operation. Preserve entry
boundaries, source references and timestamps. Do not delay urgent records or
combine unrelated operations just to reduce calls. Stay within advertised UTF-8
payload and final-document limits; characters are not necessarily bytes. Append
is still a normal versioned write, not a promise of cheap in-place storage.

Read the required revision and append epoch first. Preserve the exact document,
expected revision, epoch, idempotency key, content and separator when recovering
an uncertain append. Do not create a fresh key or silently refresh guards to
force a retry; reconcile the receipt or conflict first. Confirm the committed
result before updating an index that depends on it.

Avoid redundant metadata/property writes, heartbeat edits and unchanged index
rewrites. Record actual semantic changes, not that the agent looked at a file.
Use the existing guarded update workflow for intentional replacements. None of
these efficiency choices weaken access checks, provenance or conflict handling.
