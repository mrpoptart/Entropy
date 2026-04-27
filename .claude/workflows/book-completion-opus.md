---
description: >
  Write all remaining chapters of a book. Detects which chapters are missing
  by comparing the outline against existing chapter files, then iterates through
  each unwritten chapter using the Writers' Room. Auto-selects the Editor's Table
  top pick. Run this in Opus for best creative output.
  Follow up with /book-review in Sonnet to run review agents.
---

# 📖 Book Completion (Opus)

Write all remaining chapters for a book, one at a time. **Run this in Opus.**

// turbo-all

## Prerequisites

You need:
- The book directory (e.g., `book-one/`)

## Steps

### 1. Detect Remaining Chapters

Read `[book]/outline.md` and extract all chapter numbers and titles (lines matching `### Chapter N — Title`).

Check which chapter files already exist as `[book]/chapter-[NN].md` (zero-padded, e.g., `chapter-08.md`).

Build a list of **missing chapters** — those in the outline but without a finalized file.

Present the list to the author:
```
Chapters complete: 1, 2, 3, 4, 5, 6, 7
Chapters remaining: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
Starting from: Chapter 8
```

Then begin.

### 2. For Each Missing Chapter

Loop through the remaining chapters in order. For each chapter:

#### 2a. Run the Writers' Room

Follow the `/writers-room` workflow for this chapter:

1. **Prepare the brief** — outline, plan, characters, worldbuilding, magic system, style guide, series outline, convergence map, previously written chapters, timeline
2. **Generate 3 drafts in parallel** — Carver, Hearthkeeper, Lyricist
3. **Run The Editor's Table** — comparative evaluation

#### 2b. Auto-Select and Save

Use The Editor's Table's top recommendation as the chapter draft. Save to `[book]/chapter-[NN].md`.

All intermediary files are preserved:
```
[book]/drafts/chapter-[NN]-carver.md
[book]/drafts/chapter-[NN]-hearthkeeper.md
[book]/drafts/chapter-[NN]-lyricist.md
[book]/drafts/chapter-[NN]-evaluation.md
```

#### 2c. Update Outline and Plan (always)

After every chapter is saved, reconcile planning docs with what was actually written. This is not conditional on "did anything change" — run the check every chapter, because drift compounds:

1. **`[book]/outline.md`** — update the chapter entry to reflect the scenes, decisions, beats, named characters, named locations, and reservoir delta as written. If the chapter diverged from the outline brief, rewrite the entry to match the chapter, not the original plan.
2. **`[book]/plan.md`** — if the chapter shifted the book's arc, theme emphasis, thread state, or pacing assumptions, update the relevant sections.
3. **`convergence-map.md`** — update thread plant/progress/converge state for any thread this chapter touched.
4. **`characters/*.md`** — if a character's voice, relationships, or arc state evolved in this chapter, update the profile.
5. **Named Locations gazetteer** in `[book]/outline.md` — add any new location introduced.

Per the Plot Sync Rule and Character/Location Name Rules in CLAUDE.md. Surface the diffs you made before moving to the next chapter.

#### 2d. Move to Next Chapter

Proceed to the next missing chapter. No pause needed.

### 3. Completion

When all chapters have been written:
- List all chapter files
- Note any outline updates made during the process
- Remind the author to run `/book-review` in Sonnet for the review pass
