# Entropy — Agent Registry

Cursor and Claude Code share this registry. Agent definitions live in `.claude/agents/`. Workflows live in `.claude/workflows/`. Prose rules live in `CLAUDE.md`.

**Before acting as any agent:** read its file in `.claude/agents/`. Cursor Task subagents with matching names should follow the same definitions.

---

## Writing Agents

Draft chapter prose from a prepared brief.

| Agent | File | When to use |
|-------|------|-------------|
| 📜 The Carver | `.claude/agents/the-carver.md` | High-stakes, grief, restraint, tension, Dorenne confrontations |
| 🔥 The Hearthkeeper | `.claude/agents/the-hearthkeeper.md` | Family, workshop, relationships, warmth (default when unsure) |
| 🌊 The Lyricist | `.claude/agents/the-lyricist.md` | Action, momentum, deployment, pacing-critical scenes |
| ⚖️ The Editor's Table | `.claude/agents/editors-table.md` | Compare 3 drafts; recommend direction; no new prose |
| 📐 Plan Editor | `.claude/agents/plan-editor.md` | Update outline, plan, briefs; no prose |

---

## Review Agents — Full Pipeline

Run on a chosen draft. Each reads the draft and relevant source files.

| Agent | File |
|-------|------|
| 🧭 Arc Guardian | `.claude/agents/arc-guardian.md` |
| ✍️ Voice Editor | `.claude/agents/voice-editor.md` |
| 🌍 World Keeper | `.claude/agents/world-keeper.md` |
| 🏗️ Story Architect | `.claude/agents/story-architect.md` |
| ⏳ Pace Keeper | `.claude/agents/pace-keeper.md` |
| 💡 Thematic Compass | `.claude/agents/thematic-compass.md` |
| 🔗 Continuity Tracker | `.claude/agents/continuity-tracker.md` |
| 🌀 Convergence Tracker | `.claude/agents/convergence-tracker.md` |

---

## Review Agents — Lean Pipeline (consolidated)

Preferred for Book Two+ routine work.

| Agent | File | Consolidates |
|-------|------|--------------|
| 🔍 Unified Reviewer | `.claude/agents/unified-reviewer.md` | Continuity + Arc + World + Convergence |
| 🏛️ Structure Reviewer | `.claude/agents/structure-reviewer.md` | Architect + Pace + Thematic |
| ✍️ Voice Editor | `.claude/agents/voice-editor.md` | Style mechanics (same as full pipeline) |

---

## Per-Character Voice Agents

Run **in parallel** for every speaking character with a dedicated agent. Skip if the character does not speak in the chapter.

| Agent | File | Voice spec |
|-------|------|------------|
| 🗣️ Voice — Ash | `.claude/agents/voice-ash.md` | `characters/protagonist.md` |
| 🗣️ Voice — Maren | `.claude/agents/voice-maren.md` | `characters/sister.md` |
| 🗣️ Voice — Haran | `.claude/agents/voice-haran.md` | `characters/mentor.md` |
| 🗣️ Voice — Ryn | `.claude/agents/voice-ryn.md` | `characters/childhood-friend.md` |
| 🗣️ Voice — Dorenne | `.claude/agents/voice-dorenne.md` | `characters/patron.md` |
| 🗣️ Voice — Leska | `.claude/agents/voice-leska.md` | `characters/mother.md` |
| 🗣️ Voice — Father | `.claude/agents/voice-father.md` | `characters/father.md` |

Template: `.claude/agents/voice-agent-template.md` (documentation only, not invocable)

---

## Skills

| Skill | File | When to use |
|-------|------|-------------|
| Voice Asymmetry Fix | `.claude/skills/voice-asymmetry-fix/SKILL.md` | Two contrasting voices collapsed toward each other in shared scenes |

---

## Workflows

| Workflow | File | Purpose |
|----------|------|---------|
| Lean Pipeline | `.claude/workflows/lean-pipeline.md` | **Default** — single draft + 3 reviewers |
| Chapter Pipeline | `.claude/workflows/chapter-pipeline.md` | Full — Writers' Room + 8 reviewers |
| Writers' Room | `.claude/workflows/writers-room.md` | 3 drafts + evaluation only |
| Chapter Revision | `.claude/workflows/chapter-revision.md` | Apply revision brief + re-review |
| Lean Review | `.claude/workflows/lean-review.md` | Book-level lean review |
| Book Review (Sonnet) | `.claude/workflows/book-review-sonnet.md` | Book-level full 8-agent review |
| Lean Completion | `.claude/workflows/lean-completion.md` | End-of-book lean pass |
| Book Completion (Opus) | `.claude/workflows/book-completion-opus.md` | End-of-book full pass |

---

## Lane Boundaries (do not duplicate)

- **Voice Editor** → POV, tense, tags, style mechanics. Not per-character voice.
- **Per-character voice agents** → One character's dialogue spec + collapse check. Not plot or pacing.
- **Arc Guardian / Unified Reviewer (character section)** → Action, motivation, arc. Not dialogue voice spec.
- **Voice Asymmetry Fix** → Pair repair when registers collapsed. Not general style or single-character audit.

---

## Output Conventions

```
[book]/drafts/chapter-[NN]-carver.md          # Writers' Room draft 1
[book]/drafts/chapter-[NN]-hearthkeeper.md    # Writers' Room draft 2
[book]/drafts/chapter-[NN]-lyricist.md        # Writers' Room draft 3
[book]/drafts/chapter-[NN]-draft.md           # Lean pipeline draft
[book]/drafts/chapter-[NN]-evaluation.md      # Editor's Table output
[book]/drafts/chapter-[NN]-revision-brief.md  # Compiled review feedback
[book]/chapter-[NN].md                        # Canonical chapter
```

---

## Cursor ↔ Claude Sync Rules

1. `CLAUDE.md` is authoritative for all prose rules.
2. Agent files in `.claude/agents/` are authoritative for agent behavior.
3. When agent files conflict with `CLAUDE.md`, `CLAUDE.md` wins.
4. Plot changes require same-pass updates to `outline.md`, `plan.md`, and affected planning docs.
5. New named characters require same-pass outline updates (Character Name Rule).
6. Proposed replacement lines must comply with the No Em Dash Rule.
