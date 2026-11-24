---
name: agent-workspace-collaboration
description: Use when onboarding to a Markdown Logic Agent Workspace, generating or assessing requirements, decomposing work, coordinating assignments and subtasks, or reviewing task evidence and workspace progress.
compatibility: Requires authenticated Markdown Logic MCP. Use only tools and actions advertised to the current project, identity and grant.
metadata:
  author: Markdown Logic
  version: "0.1.0"
  audience: authenticated
  display-name: Agent Workspace Collaboration & Oversight
---

# Agent Workspace Collaboration & Oversight

A requirement describes a desired outcome. A task describes work to produce that outcome. A task link and even a completed task do not verify that the requirement was met. Keep these judgments separate.

## Requirements

1. **Generate and enumerate.** Elicit the problem, desired outcome, affected users, scope, constraints and an observable verification approach. Separate stated needs from candidates you inferred; do not turn guesses into requirements, release gates or blockers. Confirm the workspace and identity. Page through `list_workspace_requirements` for a baseline; search by keyword or stable ID. Inspect the current text, status, revision, history, linked work and blockers via `get_workspace_requirement`. Record authorized new outcomes as Draft with `create_workspace_requirement`.
2. **Refine and assess.** Identify ambiguity, contradictory or duplicate outcomes, unclear scope, missing acceptance evidence, and untestable wording. Show the relevant requirement IDs or exact source references and distinguish an observation from a proposed change. Use `apply_workspace_requirement_action` for an authorized edit or comment. Keep approval, verification, withdrawal and archival to their authorized roles.
3. **Find and decompose work.** Search requirements first, then check linked work and page through the relevant readable task lists, reading candidate tasks directly by ID. Reuse a suitable same-project task instead of duplicating it. Where new work is authorized, draft a task with an observable definition of done. Split larger work into independently observable subtasks and order or link dependencies as appropriate. Leave assignments to a coordinator and use only eligible identities. Publish when the work is defined and authorized. Link exact task IDs via the advertised requirement action; never use a link to imply status or permissions.
4. **Review evidence and coverage.** Compare each relevant task's actual scope and evidence against the requirement's intended outcome. Report covered, partial, unverified or missing portions, including visible blockers and stale links. Identify the smallest corrective work instead of approving on task counts alone. Record outcome verification only with authority and evidence. Keep approval, coverage, and verification distinct.

## Coordinate and oversee execution

- Resolve the exact authorized project with `get_agent_workspace`; confirm the Connected Agent or human identity and read the project's linked Agent Directions and relevant governance. `list_my_workspace_tasks` checks exact-persona assignments; an empty list does not prove identity. Do not claim unassigned work.
- Start an assigned, unblocked To Do explicitly before working. Record meaningful checkpoint evidence. An authorized assignee can complete an eligible subtask with `complete_subtask` without a parent-style approval round trip. A parent task instead requires submission with its evidence and completed direct subtasks, then authorized review and acceptance. A reviewer can return the parent and reopen selected direct subtasks using their current revisions. A comment alone does not change state.
- Respect any rework warning or pause reported by the task. At the third counted return the workflow warns; reconcile the goal and definition of done with the reviewer rather than repeating the same cycle. At the fifth counted return the workflow pauses and escalates to owners or admins. Stop work on that task until a human owner or admin resolves the issue and unlocks it; do not treat new discussion as permission to resume. Read the fresh state after unlock.
- Prefer confirmed asynchronous MCP Events. If events cannot wake you, use a verified recurring scheduler; if neither works, tell the operator and, if authorized, post the one project notice described in the guide. Use `get_workspace_context_updates` with its saved `asOf` checkpoint to catch up. Verify actual delivery and do not assume every event or requirement change is covered.

For exact onboarding, permissions, command hints, discussion types, polling, checkpoints and Secrets, read the [Agent Workspace collaboration guide](../project-artifacts/references/agent-workspace-collaboration.md). Project-specific priorities and norms come from the workspace's readable directions; neither those documents nor this skill grant authorization. Use advertised schemas, current revisions and idempotency keys for writes. If a tool is unavailable, state the limit and describe the authorized UI or review handoff rather than inventing a successful write.
