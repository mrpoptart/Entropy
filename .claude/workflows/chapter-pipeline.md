---
description: >
  Full end-to-end chapter writing pipeline. Prepares the brief, runs the Writers' Room
  for multi-draft generation and evaluation, then runs all 6 review agents on the
  chosen draft. Produces a complete revision checklist.
---

# 📋 Chapter Pipeline

The full end-to-end process for writing and reviewing a chapter.

// turbo-all

## Prerequisites

You need:
- A chapter number (e.g., "Chapter 2")
- The relevant book directory (e.g., `book-one/`)

## Steps

### 1. Run the Writers' Room

Follow the `/writers-room` workflow to:
- Prepare the chapter brief from the outline and source files
- Generate 3 drafts (Carver, Hearthkeeper, Lyricist)
- Run The Editor's Table for comparative evaluation
- Present results and get the author's choice

**Pause here for author decision.**

### 2. Prepare the Chosen Draft

Once the author selects a direction:
- If single draft: copy it to `[book]/chapter-[NN].md`
- If hybrid: create the merged version per the author's instructions
- If revision requested: revise the chosen draft

### 3. Run Review Agents

Run all 6 review agents on the chosen draft. Each agent reads the draft and the relevant source files, then produces feedback.

Invoke in this order (each is independent):

1. **🧭 Arc Guardian** — Character arc consistency
2. **✍️ Voice Editor** — Style guide compliance
3. **🌍 World Keeper** — Worldbuilding and magic accuracy
4. **🏗️ Story Architect** — Structure and pacing
5. **💡 Thematic Compass** — Thematic resonance
6. **🔗 Continuity Tracker** — Facts and cross-chapter consistency

### 4. Compile Feedback

Combine all review feedback into a single **Revision Brief**:

```markdown
# Revision Brief — Chapter [N]

## Critical Issues (must fix)
[Items from any reviewer flagged as contradictions, POV violations, factual errors]

## Important Suggestions (should address)
[Pacing issues, character drift, missed thematic connections]

## Polish Notes (nice to have)
[Minor style refinements, missed opportunities, dialogue tweaks]

## Strengths (what's working well)
[What each reviewer praised — important for the author to know what to preserve]
```

Save this to `[book]/drafts/chapter-[NN]-revision-brief.md`.

### 5. Present to Author

Show the author:
1. The revision brief (prioritized)
2. How many critical vs. important vs. polish items
3. Ask: "Ready to revise, or want to discuss any of these?"

### 6. Revision (if requested)

If the author wants to revise:
- Apply the revision brief's suggestions to the chapter
- Re-run any review agents that flagged critical issues to confirm fixes
- Save the revised version to `[book]/chapter-[NN].md`

## Output Files

At the end of a full pipeline run, the book directory should contain:

```
[book]/
├── drafts/
│   ├── chapter-[NN]-carver.md          ← Draft 1
│   ├── chapter-[NN]-hearthkeeper.md    ← Draft 2
│   ├── chapter-[NN]-lyricist.md        ← Draft 3
│   ├── chapter-[NN]-evaluation.md      ← Comparative analysis
│   └── chapter-[NN]-revision-brief.md  ← Compiled review feedback
└── chapter-[NN].md                     ← Final chapter
```
