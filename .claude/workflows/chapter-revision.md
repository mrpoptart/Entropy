---
description: >
  Revise an existing chapter from a revision plan. Builds a revision brief,
  generates revised drafts that preserve what works, runs all 7 review agents,
  and produces a final revised chapter.
---

# ✂️ Chapter Revision

Revise an existing chapter using a revision plan. Unlike the Writers' Room (which drafts from scratch), this workflow starts from a chapter that exists and a set of specific changes to make.

// turbo-all

## Prerequisites

You need:
- The existing chapter file (e.g., `book-one/chapter-02.md`)
- A revision plan — either a formal document or author instructions describing what to change

## Steps

### 1. Build the Revision Brief

Read these files and assemble a revision brief:

**The chapter being revised:**
- The existing chapter file — read it completely

**The revision plan:**
- The author's revision instructions or a revision plan document
- If a revision brief already exists from a prior pipeline run (`[book]/drafts/chapter-[NN]-revision-brief.md`), read that too

**Context files (same as Writers' Room):**
- The chapter's entry in `[book]/outline.md`
- `[book]/plan.md`
- `characters/*.md` — profiles for characters in this chapter
- `worldbuilding.md` and `magic-system.md`
- `reference/style-guide.md`
- `series-outline.md`
- Adjacent chapters (before and after) — for continuity
- `timeline.md`

Compile the brief into a clear prompt that includes:
- The full existing chapter text
- A **scene-by-scene revision map** — for each scene in the current chapter:
  - **KEEP** — this scene works as-is (minor polish only)
  - **REVISE** — this scene stays but needs specific changes (describe them)
  - **REPLACE** — this scene should be rewritten (describe what the new version should accomplish)
  - **CUT** — remove this scene entirely
  - **NEW** — add a new scene here (describe its purpose, beats, and placement)
- The emotional arc the revised chapter should hit
- Any timeline changes (e.g., "expand from one day to two weeks")
- Specific passages or lines to preserve verbatim

**Present the revision map to the author for approval before proceeding.**

### 2. Create Drafts Directory

```bash
mkdir -p [book]/drafts
```

### 3. Generate Revised Drafts

Send the revision brief to **two** writing agents (not three — revision benefits from focused comparison, not sprawl). Choose the two most appropriate voices based on the chapter's needs:

- If the chapter needs **emotional deepening or relationship work** → 🔥 Hearthkeeper
- If the chapter needs **tighter structure or tension** → 📜 Carver
- If the chapter needs **better pacing or momentum** → 🌊 Lyricist

The revision brief sent to each agent must include:
1. The full existing chapter
2. The scene-by-scene revision map
3. Clear instructions: "You are revising, not rewriting from scratch. Preserve the voice and material marked KEEP. Rewrite material marked REPLACE. Apply the specific changes described for material marked REVISE. Add new scenes where marked NEW."
4. A reminder of Rule #9 (Growth Realism) and the specific pacing concerns that motivated this revision

Save outputs to:
```
[book]/drafts/chapter-[NN]-revision-[agent].md
```

### 4. Compare Revised Drafts

Send both revised drafts to ⚖️ **The Editor's Table** for comparison. The evaluation prompt should note:
- This is a **revision**, not a fresh draft — evaluate how well each version addresses the revision plan while preserving what was working
- Pay special attention to the **Growth Realism** criterion, since pacing concerns often motivate revision
- Note any places where a revision introduced new problems (broke continuity, lost a strong passage, etc.)

Save to:
```
[book]/drafts/chapter-[NN]-revision-evaluation.md
```

### 5. Present to Author

Show the author:
1. The evaluation comparison
2. Best passages from each revision
3. What each revision preserved vs. changed
4. Ask: "Which direction, or hybrid?"

**Pause for author decision.**

### 6. Assemble the Revised Chapter

Based on the author's choice:
- If single draft: copy to `[book]/chapter-[NN].md`
- If hybrid: merge per instructions
- If further changes needed: apply and iterate

### 7. Run Review Agents

Run all 7 review agents on the revised chapter:

1. **🧭 Arc Guardian** — Character arc consistency
2. **✍️ Voice Editor** — Style guide compliance
3. **🌍 World Keeper** — Worldbuilding and magic accuracy
4. **🏗️ Story Architect** — Structure and pacing
5. **⏳ Pace Keeper** — Growth realism and show-vs-tell
6. **💡 Thematic Compass** — Thematic resonance
7. **🔗 Continuity Tracker** — Facts and cross-chapter consistency

> **Note:** Pay special attention to the Pace Keeper and Continuity Tracker results. Revisions that change timeline or add/remove scenes often introduce pacing regressions or continuity breaks with adjacent chapters.

### 8. Compile Feedback

Combine all review feedback into a **Revision Review**:

```markdown
# Revision Review — Chapter [N]

## Revision Goals Met?
[For each goal in the revision plan: was it addressed? How well?]

## New Issues Introduced
[Problems that didn't exist in the original but appeared in the revision]

## Remaining Issues
[Problems from the original that the revision didn't fix]

## Continuity Check
[Any breaks with adjacent chapters caused by the revision]

## Strengths
[What the revision improved — important for the author to see what's working]
```

Save to `[book]/drafts/chapter-[NN]-revision-review.md`.

### 9. Present to Author

Show the author:
1. The revision review
2. Whether the revision goals were met
3. Any new issues to address
4. Ask: "Accept, revise further, or adjust approach?"

## Output Files

```
[book]/
├── drafts/
│   ├── chapter-[NN]-revision-[agent1].md     ← Revised draft 1
│   ├── chapter-[NN]-revision-[agent2].md     ← Revised draft 2
│   ├── chapter-[NN]-revision-evaluation.md   ← Comparison
│   └── chapter-[NN]-revision-review.md       ← Review feedback
└── chapter-[NN].md                            ← Final revised chapter
```
