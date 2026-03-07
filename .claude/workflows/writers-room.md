---
description: >
  Run the multi-draft writing cycle for a chapter. Invokes all 3 writing agents
  (The Carver, The Hearthkeeper, The Lyricist) on the same chapter brief, then
  invokes The Editor's Table to compare drafts and recommend the best path.
---

# 🎭 Writers' Room

Run the multi-draft writing cycle for a single chapter.

// turbo-all

## Prerequisites

You need:
- A chapter number (e.g., "Chapter 2")
- The relevant book directory (e.g., `book-one/`)

## Steps

### 1. Prepare the Brief

Read these files and assemble a writing brief:

- The chapter's entry in `[book]/outline.md` — scene beats, emotional arc, characters present, reservoir level
- `[book]/plan.md` — the book's overall arc and themes
- `characters/*.md` — profiles for every character appearing in this chapter
- `worldbuilding.md` and `magic-system.md` — world details relevant to this chapter
- `reference/style-guide.md` — prose rules
- `series-outline.md` — trilogy context
- Any previously written chapters — for continuity

Compile the brief into a clear prompt that includes:
- Chapter number and title (from outline)
- Scene-by-scene beats (from outline)
- Emotional arc (from outline)
- Characters present and their current state
- Reservoir level at chapter start and end
- Worldbuilding to introduce or maintain
- Seeds to plant (from outline)
- Any specific moments or lines highlighted in the outline

### 2. Create Drafts Directory

```bash
mkdir -p [book]/drafts
```

### 3. Invoke The Carver

Send the brief to the 📜 **The Carver** agent. Save the output to:
```
[book]/drafts/chapter-[NN]-carver.md
```

### 4. Invoke The Hearthkeeper

Send the identical brief to the 🔥 **The Hearthkeeper** agent. Save the output to:
```
[book]/drafts/chapter-[NN]-hearthkeeper.md
```

### 5. Invoke The Lyricist

Send the identical brief to the 🌊 **The Lyricist** agent. Save the output to:
```
[book]/drafts/chapter-[NN]-lyricist.md
```

### 6. Invoke The Editor's Table

Send all 3 drafts to the ⚖️ **The Editor's Table** agent for comparative analysis. Save the evaluation to:
```
[book]/drafts/chapter-[NN]-evaluation.md
```

### 7. Present Results

Show the user:
1. The evaluation scorecard
2. The recommended path (which draft to build from)
3. Best passages from each draft
4. Ask: "Which direction would you like to go?"

The user may choose:
- A single draft as the foundation
- A hybrid approach (elements from multiple drafts)
- Revisions to a specific draft
- A complete rewrite with adjusted instructions

Save the chosen/revised version as `[book]/chapter-[NN].md`.
