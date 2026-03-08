---
description: >
  Run all 8 review agents on every chapter that lacks a revision brief.
  Produces a revision brief for each chapter. Designed to run in Sonnet
  after /book-completion has generated all chapter drafts in Opus.
---

# 📝 Book Review (Sonnet)

Run review agents on all chapters that haven't been reviewed yet. **Run this in Sonnet.**

// turbo-all

## Prerequisites

You need:
- The book directory (e.g., `book-one/`)
- Chapter files already written (via `/book-completion` or manually)

## Steps

### 1. Detect Unreviewed Chapters

List all `[book]/chapter-[NN].md` files.

Check which already have a corresponding `[book]/drafts/chapter-[NN]-revision-brief.md`.

Build a list of **unreviewed chapters** — those with a chapter file but no revision brief.

Present the list:
```
Chapters with reviews: 1, 2, 3, 4, 5, 6, 7
Chapters needing review: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
Starting from: Chapter 8
```

Then begin.

### 2. For Each Unreviewed Chapter

Loop through the unreviewed chapters in order. For each chapter:

#### 2a. Run All 8 Review Agents

Run these agents on the chapter, each reading the draft and relevant source files:

1. **🧭 Arc Guardian** — Character arc consistency
2. **✍️ Voice Editor** — Style guide compliance
3. **🌍 World Keeper** — Worldbuilding and magic accuracy
4. **🏗️ Story Architect** — Structure and pacing
5. **⏳ Pace Keeper** — Growth realism and show-vs-tell
6. **💡 Thematic Compass** — Thematic resonance
7. **🔗 Continuity Tracker** — Facts and cross-chapter consistency
8. **🌀 Convergence Tracker** — Thread management and avalanche pacing

#### 2b. Compile Revision Brief

Combine all review feedback into a single revision brief:

```markdown
# Revision Brief — Chapter [N]

## Critical Issues (must fix)
[Contradictions, POV violations, factual errors]

## Important Suggestions (should address)
[Pacing issues, character drift, missed thematic connections]

## Polish Notes (nice to have)
[Minor style refinements, missed opportunities, dialogue tweaks]

## Strengths (what's working well)
[What each reviewer praised — important to know what to preserve]
```

Save to `[book]/drafts/chapter-[NN]-revision-brief.md`.

#### 2c. Move to Next Chapter

Proceed to the next unreviewed chapter. No pause needed.

### 3. Completion

When all chapters have been reviewed:
- Summarize total issues found across all chapters (critical / important / polish)
- Flag any cross-chapter patterns (e.g., recurring voice issues, continuity threads)
- Suggest next steps (revision pass, or specific chapters needing attention)
