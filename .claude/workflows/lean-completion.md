---
description: >
  Write all remaining chapters using the lean pipeline. Single draft per chapter
  with voice selection, 3 consolidated reviewers. Use for bulk chapter generation
  where the full 3-draft pipeline is overkill.
---

# ⚡ Lean Book Completion

Write all remaining chapters using the lean pipeline. Replaces `/book-completion-opus` for efficient bulk drafting.

// turbo-all

## Prerequisites

- The book directory (e.g., `book-one/`)

## Steps

### 1. Detect Remaining Chapters

Read `[book]/outline.md` and extract all chapter numbers.
Check which `[book]/chapter-[NN].md` files exist.
List missing chapters.

### 2. For Each Missing Chapter

#### 2a. Select Voice

Based on the chapter's emotional center (from the outline):

| Chapter Type | Voice |
|---|---|
| Family, relationships, warmth, workshop | 🔥 Hearthkeeper |
| Tension, confrontation, restraint, grief | 📜 Carver |
| Action, momentum, deployment, earthquake | 🌊 Lyricist |
| Mixed / unsure | 🔥 Hearthkeeper (default) |

#### 2b. Run Lean Pipeline

Follow `/lean-pipeline` steps 2-7 for this chapter.

#### 2c. Move to Next

No pause needed between chapters.

### 3. Completion

When done:
- List all chapter files created
- Note any outline updates made
- Summarize total critical/important/polish issues across all revision briefs
- Suggest which chapters warrant a second look
