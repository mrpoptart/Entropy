---
description: >
  Efficient chapter pipeline. Single-draft with voice selection, 3 consolidated
  reviewers instead of 8, and SDT prevention baked into the drafting stage.
  ~3-5x fewer tokens than the full pipeline. Use for Book Two onwards and
  any remaining Book One revision work.
---

# ⚡ Lean Pipeline

Efficient end-to-end chapter writing and review. Replaces `/chapter-pipeline` for routine use.

// turbo-all

## Prerequisites

- A chapter number (e.g., "Chapter 2")
- The relevant book directory (e.g., `book-one/`)

## Steps

### 1. Select a Voice

Choose ONE writing agent based on the chapter's primary emotional need:

- **📜 The Carver** — High-stakes scenes, grief, tension, restraint, the math scene, Dorenne confrontations
- **🔥 The Hearthkeeper** — Family scenes, Haran workshop, Ryn conversations, relationship depth, warmth
- **🌊 The Lyricist** — Action sequences, the earthquake, deployments, momentum-driven scenes, pacing-critical chapters

If unsure, default to **The Hearthkeeper** — it's been the most consistent voice across the existing 22 chapters.

### 2. Prepare the Brief

Read and compile from:
- The chapter's entry in `[book]/outline.md` — beats, emotional arc, characters, reservoir level
- `[book]/plan.md` — book arc
- `characters/*.md` — profiles for characters in this chapter
- `worldbuilding.md` and `magic-system.md` — relevant world details
- `reference/style-guide.md` — prose rules
- `convergence-map.md` — thread targets for this chapter
- Adjacent chapters — for continuity and voice calibration

**Add this to the end of every brief:**

> **SDT CHECKPOINT:** Before writing any scene, ask: am I about to summarize a development that should be dramatized? If a character learns something, earns trust, demonstrates competence, or shifts a relationship — show it in scene with dialogue, action, and physical detail. Never compress a key development into narration. When in doubt, write the scene.

### 3. Draft

Invoke the selected writing agent. Save to:
```
[book]/drafts/chapter-[NN]-draft.md
```

### 4. Review (3 agents in parallel)

Run all 3 reviewers simultaneously on the draft:

1. **🔍 Unified Reviewer** — Continuity, character, world, threads (replaces Continuity Tracker + Arc Guardian + World Keeper + Convergence Tracker)
2. **🏛️ Structure Reviewer** — Architecture, pacing, theme, growth realism (replaces Story Architect + Pace Keeper + Thematic Compass)
3. **✍️ Voice Editor** — Style guide compliance, POV, tense, dialogue, narrative distance

### 5. Compile Feedback

Combine all review feedback into a single revision brief:

```markdown
# Revision Brief — Chapter [N]

## Critical Issues (must fix)
[From any reviewer — contradictions, POV violations, factual errors, SDT violations]

## Important Suggestions (should address)
[Pacing issues, character drift, missed threads, thematic gaps]

## Polish Notes (nice to have)
[Minor style refinements, dialogue tweaks]

## Strengths (preserve these)
[What each reviewer praised]
```

Save to `[book]/drafts/chapter-[NN]-revision-brief.md`.

### 6. Revise (if needed)

If critical issues exist:
- Apply fixes directly to the draft (same agent voice, or author edits)
- Re-run ONLY the reviewer(s) that flagged critical issues — not all 3
- Save revised version to `[book]/chapter-[NN].md`

If no critical issues:
- Copy draft to `[book]/chapter-[NN].md`
- Apply important/polish suggestions at author's discretion

### 7. Update Planning Docs

Per the Plot Sync Rule: if the chapter introduced any plot changes vs. the outline, update `[book]/outline.md` and any affected planning documents.

Per the Character Name Rule: if the chapter introduced or named any characters not yet named in the outline, update the outline entry to include each character's name and brief role (e.g., "Tessaly, Dorenne's senior scheduler"). Future outline references to this character should use the established name.

Per the Location Name Rule: if the chapter introduced any new location names not in the outline's Named Locations gazetteer, add them with type and chapter number.

## Output Files

```
[book]/
├── drafts/
│   ├── chapter-[NN]-draft.md           ← Single draft
│   └── chapter-[NN]-revision-brief.md  ← Compiled feedback
└── chapter-[NN].md                     ← Final chapter
```

## When to Use the Full Pipeline Instead

Use the original `/chapter-pipeline` (3 drafts + 8 reviewers) for:
- Climactic chapters (the math scene, the earthquake, the Dorenne break)
- Chapters where you're unsure which voice fits
- First chapters of a new book (voice calibration)

For everything else, this lean pipeline is sufficient.
