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

**Status:** propagated; final-prose execution EXECUTED 2026-05-18, reviewed and remediated 2026-05-24 under 3c, for ch01. Not marked review-verified beyond 3c (no D1-specific verification pass logged this round; D1 was outside the 3c scope of ch02/06/07/11/17/18). Prior audit note retained: 2026-05-18 full-book audit found one residual violation: `book-one/chapter-01.md:273` still ranks Maren ("I scored highest in the cohort. My supervisor said the survey was the cleanest diagnostic work the team had produced all quarter."). Outline Ch1 dinner entry must be checked for the same superlative and aligned to effort/diligence framing. Briefed in `book-one/drafts/revision-briefs/chapter-01-brief.md`.

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

**Status:** EXECUTED 2026-05-18, reviewed and remediated 2026-05-24 under 3c, for ch02/ch06/ch11/ch17. All four load-bearing D2 beats now present in final prose: Ch2 marked-up deployment-summary memo restored (with the junction-nine scheduling beat demoted from competence showcase to flagged-and-corrected exchange, and the Osten "Good." validation removed in concert); Ch6 press-event panic restored with the corridor "You're not going to a podium without me." line; Ch11 failure-anchor "worst letter" beat (subject: Devrin) restored, pointing-tool competence-anchor substitution removed; Ch17 council on-feet failure restored with Dorenne taking the floor. Pending formal review-verification only. Prior audit note retained for the historical trail: 2026-05-18 full-book audit found all four beats ABSENT from final prose, three replaced with competence/charm renderings; 3c remediation pass closed the gap.

---

## D3 — Parents Get Offstage Normal-Life Beats

**Rule:** The mother and father each get one or two short scenes per book where Ash is not present and is not the subject. The father at his job doing something dull. The mother with a neighbor. A small marital moment between them. These scenes do not advance plot. They establish that the world contains regular humans living regular lives, not just the chosen ensemble.

**Why:** The cast currently routes all emotional weight through Ash. The parents appear as anchors for his scenes and disappear when he leaves the room. Giving them small, plot-irrelevant beats of their own builds the texture of ordinariness the book needs and makes the family feel like a family, not a support structure.

**Affected files:**
- `characters/mother.md` (add: "What she does when Ash is not present")
- `characters/father.md` (same)
- `book-one/outline.md` (identify two or three chapters where a 200 to 400-word offstage parent beat slots in naturally)
- `book-one/plan.md`

**Status:** EXECUTED 2026-05-18, reviewed and remediated 2026-05-24 under 3c, for ch07/ch11/ch18. All three parent beats now present in final prose. **POV reconciliation applied in 3c (project style guide overrides D3's offstage framing):** the Ch7 Leska+Saren beat has been folded from a true offstage scene to Ash overhearing from the back bedroom of the new flat; the Ch11 Leska+Rendell marital beat has been folded from offstage to Ash glimpsing from the corridor; the Ch18 Rendell+Tomek beat remains Ash-adjacent / glimpsed-from-the-doorway as already noted. The intent of D3 (parents have life that does not orbit Ash, world goes on at regular pace in rooms Ash does not control) is preserved; the reader-never-sees-a-scene-Ash-isn't-present-for rule is honored by folding rather than by license-amending. Outline Ch7 and Ch11 entries updated to reflect the realized POV choice; outline Ch18 entry already reflected the doorway frame. Incidental sourdough-starter vehicle in Ch7 carries no plot weight. New offstage-reference characters added to the outline Named Characters list 2026-05-18: Devrin, Vask, Mira. Pending formal review-verification only. Prior audit note retained for the historical trail: 2026-05-18 full-book audit found all three beats ABSENT from final prose; 3c remediation closed the gap.

**Tomek-location reconciliation (DECIDED 2026-05-18):** One task framing placed the Rendell+Tomek joinery beat in Ch11. This is rejected. The canonical placement is the one already consistent across `book-one/outline.md` and `book-one/plan.md`: Ch7 = Leska+Saren bread/cold-weather beat (outline ~line 288); Ch11 = Leska+Rendell post-dishes marital beat (outline ~line 386) AND the D2 Rendell "worst letter" beat (outline ~line 384); Ch18 = Rendell+Tomek joinery in retired river-trader Tomek's house (outline ~line 546). Rationale: outline and plan.md already agree on this distribution; Ch11 is the family-detonation chapter where the marital beat and the "worst letter" beat reinforce each other; Ch18 is an Act Three reckoning chapter where Rendell's offstage warm-journeyman register lands against Ash's drift. No planning-doc edits to placement were required; the discrepancy was in the task framing only. Decision recorded here as the audit trail.

Net beats to write: Ch7 Leska+Saren (bread, cold weather, ~200-400w, Ash absent); Ch11 Leska+Rendell (marital, post-dishes, ~200-400w, Ash not the subject); Ch18 Rendell+Tomek (joinery in Tomek's house, ~200-400w, Ash absent or glimpsing from the doorway). Saren and Tomek are new named characters added to the outline Named Characters list with role + one-line voice notes (2026-05-18). Briefed in chapter-07/11/18 briefs.

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

**Status:** VERIFIED 2026-05-24. Final-prose line-level cuts EXECUTED 2026-05-18 across the audit cut list; 3c thematic verification pass (2026-05-24) confirmed zero still-present trailing-reframe violations from the original cut list and zero new-reframe regressions introduced by the D2/D3 restoration work in ch02/06/07/11/17/18. D4 is the only directive carrying a thematic-verification stamp this round. Prior audit note retained for the historical trail: 2026-05-18 full-book audit produced a per-chapter flag list (critical/post-failure 100% cuts and high/non-failure cuts). Folded into per-chapter briefs for ch07, ch11, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22. Each flagged line: cut the reframe, end on the literal action, no replacement reframe, no em dashes.

---

## Working Notes

- D4 touches the writer and reviewer agents themselves, not just planning docs. Propagation here means editing those agent specs, which is a higher-impact change than editing a character profile. Confirm with user before applying.
- After all four directives reach `propagated`, the next step is to generate per-chapter revision briefs. The user will direct which chapters to brief and in what order.
- 2026-05-24: 3c remediation pass landed across ch02, ch06, ch07, ch11, ch17, ch18. Planning-doc propagation (Plan Editor): D2/D3 marked EXECUTED with 3c remediation incorporated; D4 marked VERIFIED (thematic verification: zero still-present and zero new-reframe regressions); D1 status note refreshed (D1 was outside 3c scope). Outline updates: Ch2 entry — junction-nine scheduling beat demoted from competence showcase to flagged-and-corrected exchange (Tessaly verifies the depressurization read, corrects the wrong part, routes the corrected version herself); Osten recurring-gag punchline note added ("he kept trying, and one stuck without anyone noticing", replacing Tessaly's "Good." validation); D2 audit notes refreshed to "reviewed and remediated under 3c". Ch7 entry — D3 parent beat reframed as Ash-perceived overhearing from the back bedroom (POV reconciliation per project style guide). Ch11 entry — D3 marital beat reframed as Ash-glimpsed from the corridor (POV reconciliation); D2 audit note refreshed; new "Cut framing note" added documenting that the Leska "A tool. A solution." dialogue beat has been cut (replaced with evidence catalogue plus silence-observation in final prose) and that the Ash-as-tool framing now lives entirely in the Ch13 Council-look beat (chapter-13.md:27) and the Ch20 memory-of-touch beat (chapter-20.md:155). Ch18 entry — no change (Rendell+Tomek doorway-glimpse frame already in place). No new directives invented. `reference/style-guide.md` left untouched (the reader-never-sees-a-scene-Ash-isn't-present-for rule was honored by folding D3 beats to Ash-perceived form, no exception or license amendment needed).
- 2026-05-18: Full-book audit reconciliation pass (Plan Editor). D1/D2/D3 statuses changed to "propagated; final-prose execution PENDING"; D4 to "propagated; final-prose line-level cuts PENDING". Tomek-location reconciliation DECIDED and recorded under D3 (Ch7 Saren / Ch11 marital + worst-letter / Ch18 Tomek; no placement edits required, outline and plan.md already agreed). Planning docs updated: `book-one/revision-directives.md`, `book-one/outline.md` (Ch1 dinner D1 framing note; D2 audit notes on Ch2/6/11/17 weakness beats; new Named Characters quick-reference section with Saren + Tomek), `book-one/plan.md` (D2/D3 audit + reconciliation note). Consolidated per-chapter revision briefs written to `book-one/drafts/revision-briefs/`: chapter-01-brief.md (D1), chapter-02-brief.md (D2), chapter-06-brief.md (D2), chapter-07-brief.md (D3+D4, single pass), chapter-11-brief.md (D2+D3+D4, single pass), chapter-15-brief.md (D4), chapter-16-brief.md (D4), chapter-17-brief.md (D2+D4, single pass), chapter-18-brief.md (D3+D4, single pass), chapter-19-brief.md (D4), chapter-20-brief.md (D4), chapter-21-brief.md (D4), chapter-22-brief.md (D4). Directive statuses for the briefed chapters now reflect `briefed`; final-prose execution by writer agents is the next step. No reference D2 beat renderings were found in `book-one/drafts/`; writers build the D2 beats from the outline specs cited in each brief.
- 2026-04-26: All four directives (D1, D2, D3, D4) propagated in a single Plan Editor pass. Files touched: `characters/sister.md`, `characters/mother.md`, `characters/father.md`, `characters/protagonist.md`, `book-one/outline.md`, `book-one/plan.md`, `book-two/outline.md`, `series-outline.md`, `CLAUDE.md`, `.claude/agents/voice-maren.md`, `.claude/agents/the-carver.md`, `.claude/agents/the-hearthkeeper.md`, `.claude/agents/the-lyricist.md`, `.claude/agents/structure-reviewer.md`, `.claude/agents/thematic-compass.md`, `.claude/agents/voice-editor.md`. **Next step: per-chapter revision briefs.** The user will direct which chapters to brief and in what order; Ch1, Ch2, Ch6, Ch7, Ch11, Ch13, Ch17, Ch18 are the highest-priority candidates given the new beats inserted by D2 and D3.
