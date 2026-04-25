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

#### 2a. Run Consolidated Review Agents (parallel)

Run 3 consolidated review agents in parallel:

1. **🔍 Unified Reviewer** — Continuity, character, world, threads
2. **🏛️ Structure Reviewer** — Architecture, pacing, theme, growth realism
3. **✍️ Voice Editor** — Style guide compliance (POV, tense, prose mechanics; per-character voice handled by the dedicated voice agents below)

#### 2b. Run Per-Character Voice Agents (parallel)

Identify every speaking character in the chapter draft. For each speaking character with a dedicated voice agent, invoke that agent **in parallel** (single message, multiple tool calls). Skip voice agents for characters who don't speak in this chapter.

Available per-character voice agents:

- **🗣️ Voice — Ash** (`voice-ash`) — invoke whenever Ash speaks (almost always)
- **🗣️ Voice — Maren** (`voice-maren`) — invoke when Maren speaks
- **🗣️ Voice — Haran** (`voice-haran`) — invoke when Haran speaks
- **🗣️ Voice — Ryn** (`voice-ryn`) — invoke when Ryn speaks
- **🗣️ Voice — Dorenne** (`voice-dorenne`) — invoke when Dorenne speaks
- **🗣️ Voice — Leska** (`voice-leska`) — invoke when Leska speaks
- **🗣️ Voice — Father** (`voice-father`) — invoke when Father speaks

Each per-character agent audits its character's dialogue against the voice spec in the corresponding `characters/*.md` profile and flags any lines that could be confused with another speaker (the **cross-character collapse check**).

For maximum efficiency, all agents in 2a *and* 2b can be invoked in a single message with multiple tool calls.

**No Em Dash Rule:** All agents (consolidated and per-character) must comply with the No Em Dash Rule in `CLAUDE.md`. Any REPLACEMENT lines proposed must not contain em dashes (U+2014); use commas, periods, semicolons, parentheses, ellipsis, or comma-plus-restart instead.

#### 2c. Compile Revision Brief

Combine all review feedback (consolidated + per-character voice) into a revision brief (same format as lean-pipeline step 5), with an added **Voice Review** section:

```markdown
## Voice Review (per-character)
For each per-character voice agent that ran:
- **[Character Name]:** one-paragraph summary of voice health, with line-level drift items folded into Critical/Important/Polish above.

### Confirmed Cross-Character Collapse
List every pair (A, B) where **both** A's voice agent flagged A's line as reading-like-B *and* B's voice agent independently flagged B's line as reading-like-A in the same scene. Two-sided flags are confirmed collapse and should be treated as critical.

### Suspected Cross-Character Collapse
One-sided flags. Warrant a human eye but are not confirmed.
```

Save to `[book]/drafts/chapter-[NN]-revision-brief.md`.

### 3. Completion

Summarize:
- Total issues by severity across all chapters
- Cross-chapter patterns (recurring voice issues, continuity threads, SDT hotspots)
- Chapters needing most attention (ranked by critical issue count)
