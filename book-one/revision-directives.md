# Book One — Revision Directives

This document is the single source of truth for the Book One revision pass. Each directive describes a change to the book's thesis, cast, voice, or structure. The Plan Editor agent propagates these directives into planning documents and per-chapter revision briefs. Downstream writer and reviewer agents act on the briefs.

**Status values:**
- `pending` — directive accepted, no propagation yet
- `propagated` — planning docs updated to reflect the directive
- `briefed` — per-chapter revision briefs written
- `done` — chapters revised, directive fully realized

---

## D1 — Strip Maren's Superlatives

**Rule:** Maren is not the most precise diagnostician under thirty, not exceptional in any professional ranking. She is competent because she works hard and has carried weight no one else in her cohort has carried. Her exceptionalism is moral and circumstantial, not professional.

**Why:** Right now every named character is exceptional in their field, which leaves the cast with no calibration point for "normal." Maren is the most natural normal-anchor in the book — her grind, her caretaker burden, her quiet endurance are already on the page. The superlative framing fights with what she actually is. Strip it and she becomes the ordinariness the book needs without losing anything that makes her matter.

**Affected files:**
- `characters/sister.md`
- `book-one/outline.md` (any chapter summary that frames her as exceptional)
- `book-one/plan.md`
- `book-two/outline.md` (forward consistency)
- `.claude/agents/voice-maren.md` (if her voice spec leans on the superlative)

**Status:** propagated

---

## D2 — Ash Has a Persistent Weakness

**Rule:** Ash has two persistent weaknesses he carries across the trilogy:

1. **Public speaking.** Addressing groups terrifies him. He is bad at it. He does not grind this into competence. Council appearances, crew briefings, any moment where he has to speak in front of more than a handful of people, his body betrays him. Other characters notice. The narration does not soften it.
2. **Administrative writing.** Reports, memos, formal correspondence. He has no experience and no instinct for it. His writing is awkward, over-explains, misses the conventions. Dorenne or someone like her has to fix his drafts more than once.

Neither is overcome. Both stay bad. He works around them by leaning on people who *are* good at them, which is itself characterization.

**Counterweight — Ash's real superpower:** He is willing to keep trying, and he is able to swallow his pride. A lifetime of being the constrained one, the family burden, the apologetic presence, has made pride-swallowing his deepest competence. This is his true gift, earned long before he was ever powerful. The book should make this visible: he asks for help when other people would not, he accepts correction without flinching, he tries the thing he is bad at again because he has nothing left to protect. This is the engine that produces his competence. Not talent. Not gift. The capacity to be bad at something in front of people and try anyway.

Also: emphasize Ash's pre-Wellspring incompetence. He was not secretly always capable. His success at the Wellspring is the product of grinding hours and visible failure, not latent gift. Show two or three specific past failures, on the page or in dialogue, that establish this.

**Why:** The book currently reads as if Ash was always exceptional and merely constrained. This is the wunderkind problem. Two persistent weaknesses give the reader a calibration point and give Ash a permanent humility the prose cannot reframe away. The pride-swallowing framing also reframes his eventual competence as *earned through tolerance for humiliation*, which is a far more interesting and human engine than latent talent. Pre-Wellspring failure scenes earn his current competence rather than asserting it.

**Affected files:**
- `characters/protagonist.md` (add "Pre-Wellspring incompetence" and "Persistent weakness" sections)
- `book-one/outline.md` (insert specific failure beats; identify chapters where the persistent weakness should appear)
- `book-one/plan.md`
- `book-two/outline.md`, `book-three/` planning if it exists
- `series-outline.md`

**Status:** propagated

---

## D3 — Parents Get Offstage Normal-Life Beats

**Rule:** The mother and father each get one or two short scenes per book where Ash is not present and is not the subject. The father at his job doing something dull. The mother with a neighbor. A small marital moment between them. These scenes do not advance plot. They establish that the world contains regular humans living regular lives, not just the chosen ensemble.

**Why:** The cast currently routes all emotional weight through Ash. The parents appear as anchors for his scenes and disappear when he leaves the room. Giving them small, plot-irrelevant beats of their own builds the texture of ordinariness the book needs and makes the family feel like a family, not a support structure.

**Affected files:**
- `characters/mother.md` (add: "What she does when Ash is not present")
- `characters/father.md` (same)
- `book-one/outline.md` (identify two or three chapters where a 200 to 400-word offstage parent beat slots in naturally)
- `book-one/plan.md`

**Status:** propagated

---

## D4 — Narrator Does Not Grade Outcomes

**Rule:** The third-person narration does not soften failures with reframe, does not warm successes with metaphor, does not place small wisdoms at the ends of scenes. Warmth and meaning come from characters in dialogue and action, not from the narrator's tone. The trailing-reframe sentence pattern (literal action, then metaphor, then small wisdom) is cut on at least a 50% schedule across the book and entirely after failure beats.

Specifically banned in revision passes:
- Trailing similes that reframe a literal action as elegiac ("like watching someone breathe").
- Sentences that gloss a character's behavior with a small generalization ("the way no one in Solathis did anymore").
- Narrator-side moral framing that grades the protagonist's progress ("It took him twenty minutes instead of four").
- Any softening sentence that follows a death, loss, or failure beat. Failure beats end flat.

**Why:** The current prose voice is doing aesthetic and moral labor that should be done by character. When the narration grades every outcome, the reader is asked to feel the world is profound because the sentences are profound, and the protagonist is excused from genuine ugliness because the prose carries him gently. Cutting the trailing reframe on a schedule, and entirely after failure, forces the book to make its meaning through people rather than through tone.

**Affected files:**
- `CLAUDE.md` (add as a project rule, parallel to the No Em Dash Rule)
- `.claude/agents/the-carver.md`, `.claude/agents/the-hearthkeeper.md`, `.claude/agents/the-lyricist.md` (writer agents must respect this on revision)
- `.claude/agents/structure-reviewer.md`, `.claude/agents/thematic-compass.md` (reviewers should flag, not praise, trailing reframes)
- `.claude/agents/voice-editor.md`

**Status:** propagated

---

## Working Notes

- D4 touches the writer and reviewer agents themselves, not just planning docs. Propagation here means editing those agent specs, which is a higher-impact change than editing a character profile. Confirm with user before applying.
- After all four directives reach `propagated`, the next step is to generate per-chapter revision briefs. The user will direct which chapters to brief and in what order.
- 2026-04-26: All four directives (D1, D2, D3, D4) propagated in a single Plan Editor pass. Files touched: `characters/sister.md`, `characters/mother.md`, `characters/father.md`, `characters/protagonist.md`, `book-one/outline.md`, `book-one/plan.md`, `book-two/outline.md`, `series-outline.md`, `CLAUDE.md`, `.claude/agents/voice-maren.md`, `.claude/agents/the-carver.md`, `.claude/agents/the-hearthkeeper.md`, `.claude/agents/the-lyricist.md`, `.claude/agents/structure-reviewer.md`, `.claude/agents/thematic-compass.md`, `.claude/agents/voice-editor.md`. **Next step: per-chapter revision briefs.** The user will direct which chapters to brief and in what order; Ch1, Ch2, Ch6, Ch7, Ch11, Ch13, Ch17, Ch18 are the highest-priority candidates given the new beats inserted by D2 and D3.
