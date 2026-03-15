---
description: >
  Run 3 consolidated review agents on all chapters that lack a revision brief.
  Replaces /book-review-sonnet with fewer agents and less token overhead.
---

# ⚡ Lean Book Review

Run consolidated review agents on all unreviewed chapters. Replaces `/book-review-sonnet`.

// turbo-all

## Prerequisites

- The book directory (e.g., `book-one/`)
- Chapter files already written

## Steps

### 1. Detect Unreviewed Chapters

List all `[book]/chapter-[NN].md` files.
Check which have a corresponding `[book]/drafts/chapter-[NN]-revision-brief.md`.
List unreviewed chapters.

### 2. For Each Unreviewed Chapter

Run 3 review agents in parallel:

1. **🔍 Unified Reviewer** — Continuity, character, world, threads
2. **🏛️ Structure Reviewer** — Architecture, pacing, theme, growth realism
3. **✍️ Voice Editor** — Style guide compliance

Compile into a revision brief (same format as lean-pipeline step 5).
Save to `[book]/drafts/chapter-[NN]-revision-brief.md`.

### 3. Completion

Summarize:
- Total issues by severity across all chapters
- Cross-chapter patterns (recurring voice issues, continuity threads, SDT hotspots)
- Chapters needing most attention (ranked by critical issue count)
