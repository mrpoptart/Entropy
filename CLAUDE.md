# Entropy - Project Instructions

## Plot Sync Rule

When drafting, revising, or rewriting chapters produces plot changes (new scenes, altered character decisions, shifted timelines, added or removed story beats, or shifts in the book's arc, themes, or thread state), the corresponding outline (`[book]/outline.md`), the book's plan (`[book]/plan.md`), and any affected planning documents (e.g., `convergence-map.md`, character profiles) **must be updated in the same pass**. Do not treat outline or plan as static references; they are living documents that track the actual story as written. Writers and revision agents should surface plot changes explicitly so they can be propagated.

This applies to every chapter draft, revision, and rewrite, not just major plot pivots. Each chapter that ships should leave outline, plan, and any affected planning docs aligned with what was actually written. Drift caught one chapter at a time is cheap; drift caught at end-of-book is expensive.

## Character Name Rule

The outline must refer to all characters **by name**, including minor and recurring characters (office staff, engineers, crew leads, etc.). When a chapter draft introduces or names a character who is not yet named in the outline, the outline entry for that chapter must be updated in the same pass to include the character's name and a brief role description (e.g., "Tessaly, Dorenne's senior scheduler"). Subsequent outline entries should use the established name, not generic descriptions like "a scheduler" or "the engineer." This ensures writer agents produce consistent names across drafts and revisions.

## Voice Variety Rule

Characters should not all sound alike. The default writerly impulse, *short sentences, withholding, the meaning is in what's missing,* is a single voice; if every character does it, none of them has a voice. When introducing or revising any speaking character (voiced or not), give them a deliberately different *relationship to talking itself* than the characters around them. Vary along axes such as:

- **Sentence length and rhythm** (do they expand, or compress?)
- **Relationship to silence** (do they fill it, use it, or break it?)
- **Emotional surface** (open, closed, performative, dry, warm, awkward)
- **Register switching** (one voice for all audiences, or two distinct registers?)
- **Body in dialogue** (verbal-only, or does the body do half the work?)
- **Comic timing** (none, deadpan, warm, sharp, awkward)

For every named character who speaks more than a line or two, hold a small piece of **backstory** that justifies their relationship to talking, even if the backstory never appears on the page. ("She was a birth attendant for thirty years and learned to narrate continuously through a crisis." "He was the funny one in the workshop because being the funny one was better than being the broken one.") The backstory is a writer-side tool, not a reader-side reveal; it ensures the character speaks like a person rather than a function.

Voiced characters carry this in their `characters/*.md` `## Voice` section. Unvoiced but recurring characters (schedulers, engineers, crew leads, neighbors) should at minimum have a one-line voice note attached when they're first named in the outline (e.g., "Tessaly, Dorenne's senior scheduler, brisk and dry"). Do not let unnamed-functional characters drift into the same flat institutional register; vary them by the same logic.

Embrace dialogue. People talking to each other is one of the strongest tools available for moving information, character, and theme together; the rule is to use it well, not to use it sparingly. The discipline is *variety,* not minimalism.

## Location Name Rule

The outline contains a **Named Locations** gazetteer listing all established district names, building names, infrastructure, and geographic features. Writer agents must check this list before drafting and use established names. Do not invent new location names when an existing one fits. When a chapter draft introduces a genuinely new location, add it to the gazetteer in the same pass with its type and the chapter that established it.

## Voice Asymmetry Rule

When two characters with contrasting voice specs share significant scene time, the **asymmetry between them must be legible on the page**. It is not enough for each character to be individually spec-compliant; the relationship between the two voices must do work. If both characters end up in the same register -- both terse, both warm, both declarative -- the contrast has collapsed and one of them has lost their voice.

The Ash/Haran pairing is the canonical example. Haran is defined by economy: short, sideways, mechanism-first. Ash is defined by elaboration: chatter-as-armor, looping hedges, apology-tucked-into-mid-sentence. When they share a scene, the asymmetry should be audible -- Haran's five-word question answered by Ash's fifteen-word non-answer. If Ash matches Haran's register beat for beat, Ash has drifted.

**The recovery rule:** Certain environments trigger partial recovery of a character's baseline register even when drift is otherwise established. For Ash, the workshop with Haran is an explicit recovery environment. Post-Wellspring drift compresses him toward declarative efficiency, but physical grounding at Haran's bench partially restores the chatter-armor. Any chapter set entirely in that environment where Ash never recovers is a voice failure regardless of how spec-compliant individual lines appear in isolation.

**The audit process for voice asymmetry failures:**

1. Run the per-character voice agent for the character whose voice has collapsed toward the other's.
2. The agent produces line-level flags with proposed revisions.
3. Apply all flagged fixes in a single pass using a writer agent, preserving all prose not listed in the fix set.
4. Do not partial-apply: the asymmetry either exists or it doesn't, and spot-fixing two lines while leaving ten more collapsed achieves nothing.

This rule applies to all paired characters with contrasting specs, not only Ash/Haran. Reviewers should flag any scene where two characters with documented spec contrast are indistinguishable in register.

## No Em Dash Rule

Em dashes (`—`, U+2014) are **prohibited** in all prose, dialogue, planning documents, voice specs, agent outputs, and revision notes for this project. Em dashes have become an AI tell, and our texts overuse them to the point of caricature. Replace every em dash with one of the following, chosen by what the dash was actually doing:

- **In dialogue (any spoken words), default to an ellipsis (`...`).** This is the preferred replacement for em dashes inside quoted speech, whether the dash was marking a trailing-off, an interruption, a stammer, a self-correction, a hesitation, a hard break, or a mid-sentence aside. When in doubt inside quotes, use an ellipsis.
- **Mid-sentence aside or elaboration in narration** → use a comma, a pair of commas, or parentheses.
- **Hard break / change of direction in narration** → use a period and start a new sentence, or use a semicolon.
- **Stammer in dialogue** (when an ellipsis would read wrong) → a comma plus restart is acceptable (e.g., `"I, I don't know."`), but the ellipsis is still the default.
- **Range or span** (rare) → use "to" or an en dash (`–`, U+2013) if a numeric range is genuinely needed. En dashes are allowed only for numeric ranges.

This rule applies to:
- All chapter drafts (`book-one/chapter-*.md`) and the EPUB build pipeline.
- All `drafts/` and revision briefs.
- All planning documents (`outline.md`, `convergence-map.md`, character profiles, voice specs).
- All review-agent reports and writer-agent outputs. Voice agents proposing line edits **must not** introduce em dashes in their replacements; if a voice rendering needs a beat, use ellipsis or comma-plus-restart.
- This `CLAUDE.md` itself and any future project instructions.

When revising or generating any text, do a final pass to confirm zero em dashes are present. Existing em dashes encountered during normal editing should be converted in the same pass.

## No Trailing-Reframe Rule

The third-person narration of this trilogy does not grade outcomes. It does not soften failures with reframe, does not warm successes with metaphor, and does not place small wisdoms at the ends of scenes. Warmth and meaning come from characters in dialogue and action, not from the narrator's tone. The trailing-reframe sentence pattern (literal action, then metaphor, then small wisdom) is **prohibited at a 50% cut by default and 100% cut after failure beats. Failure beats end flat.**

Specifically banned in revision passes and in generated drafts:

- **Trailing similes** that reframe a literal action as elegiac (e.g. "She set the cup down. Like watching someone breathe."). Cut the simile, keep the action.
- **Sentences that gloss a character's behavior with a small generalization** (e.g. "He apologized, the way no one in Solathis did anymore."). Cut the generalization, keep the apology.
- **Narrator-side moral framing that grades the protagonist's progress** (e.g. "It took him twenty minutes instead of four."). The reader can do the math; the narration must not do it for them.
- **Any softening sentence that follows a death, loss, or failure beat.** After a failure, the prose ends on the literal action. No metaphor, no aphorism, no small consolation, no narrator-side reframe of any kind. The failure stands.

When revising, scan every scene-ending paragraph and every paragraph that follows a failure beat. If the final sentence is doing aesthetic or moral labor that a character could be doing in dialogue or action, cut it. The 50% schedule applies project-wide; the 100% schedule applies after every failure. There is no negotiation on the post-failure rule.

This rule applies to:
- All chapter drafts (`book-one/chapter-*.md`, `book-two/chapter-*.md`, and the EPUB build pipeline.
- All `drafts/` and revision briefs.
- All planning documents (`outline.md`, `plan.md`, `convergence-map.md`, character profiles, voice specs).
- All review-agent reports and writer-agent outputs. Voice agents proposing line edits **must not** introduce trailing reframes; if a moment seems to need a closer, find one in character action or dialogue, not in the narrator's voice.
- This `CLAUDE.md` itself and any future project instructions.

When revising or generating any text, do a final pass to confirm zero post-failure trailing reframes are present, and that the 50% cut has been applied to non-failure scene-end reframes. Existing trailing reframes encountered during normal editing should be cut in the same pass.

## Tertiary Voice Rule

Characters without a defined voice spec (unnamed vendors, passersby, clerks, neighbors, crowd members) must speak in a **neutral, mid-register voice**. They should sound like ordinary people conducting ordinary business. Not terse, not loquacious, not distinctive. The default for a person without a voice spec is *unremarkable*: polite, transactional, conversational, forgettable.

Specifically prohibited for unvoiced tertiary characters:

- **Single-word utterances used as complete dialogue beats** (e.g., "Payment?" or "Name?" as standalone lines). One-word dialogue is a strong stylistic choice that implies compression, withholding, or authority. Real people in service roles use full sentences.
- **Hyper-compressed register** (three-word sentences, clipped fragments, zero pleasantries). This is a *voiced* register (Haran, Dorenne) and must not bleed into background characters.
- **Dramatic silence or weighted pauses.** Tertiary characters do not have interior lives on the page. They say their line and the scene moves on.
- **Distinctive verbal tics, unusual phrasing, or memorable cadence.** If a reader would remember how the character talked, the character has too much voice for their role.

The principle: **voiced characters earn their distinctiveness by contrast with the ordinary.** If every character in the scene talks like a protagonist, no one does. Tertiary characters are the baseline that makes the voiced characters legible. Keep them in the middle of the road.

When drafting or revising, check any unnamed character's dialogue against this rule. If the line would sound natural coming from a shop clerk or a transit worker on a normal morning, it passes. If it sounds like a line from a character with a backstory, it's over-voiced for its role.

## Dialogue Attribution Rule

A reader must always be able to tell who is speaking without inferring it from voice alone. Voice distinctiveness is a craft goal, not an attribution mechanism: the prose should read correctly even for a reader who has not internalized each character's register, and even mid-scene when an unattributed line could plausibly belong to more than one person present.

Every line of dialogue must carry a clear speaker. Attribution may be explicit (a `said`/action tag) or unambiguous from the immediately surrounding action beat, but it must be present whenever any of the following is true:

- **A stretch of unattributed back-and-forth has run long.** After roughly three consecutive unattributed exchanges, or any time the alternation could have slipped, re-anchor with a tag or action beat, even in a clean two-person scene.
- **The line follows a narrative paragraph, a scene break, a time skip, or any interruption to the dialogue rhythm.** The first line of speech after non-dialogue prose must be attributed. (Chapter 5, line 157 is the canonical failure: a paragraph of narration about breaking stones, then an unattributed line that is recognizable as Ash only if you already know his voice.)
- **More than two characters are present,** or anyone could plausibly be the speaker.
- **The emotional or informational weight of the line is high.** Key reveals, decisions, and turns never float unattributed.

Do not lean on a character's verbal signature (Ash's looping hedge, Haran's compression, Dorenne's institutional precision) to carry attribution. The signature is there to make the *right* speaker sound right once identified, not to identify them. If the only thing telling the reader who spoke is the voice spec, the line is under-attributed and must get a tag or an action beat.

When attributing, prefer `said` and grounded action beats. Avoid the inverse failure of straining for variety with "muttered," "offered," "ventured" on every line; an invisible `said` plus an occasional physical beat is the default. The goal is certainty, not ornament.

**The inserted tag or beat must not damage its neighbors.** A fix that resolves an attribution defect but introduces a prose defect is not a fix. Every tag or beat added for attribution must pass these four local checks against the sentences immediately before and after it:

1. **No echo.** The tag or beat must not reuse a distinctive noun or verb that already appears in the adjacent sentence. If the prior sentence is "She looked at the working stove," the attribution is `Ryn asked.`, not `Ryn asked, looking at the working stove.` The gaze is already established; repeating it is the defect.
2. **No duplicated sentence.** Never host a tag by reintroducing a sentence (or a near-identical clause) that already exists in the surrounding paragraph. If the paragraph already says "She moved toward the door," the next line is `"Maren," Ash said.` — not `She moved toward the door. "Maren," Ash said.`
3. **Detail-preserving relocation.** When a tag is created by splitting or moving an existing action sentence, every concrete noun in the original must survive. Reducing "He climbed down to the first failing section" to "He climbed down toward the lining" to make room for a tag is a detail loss, not an attribution fix. Keep the specificity; use a plain `said` tag instead.
4. **No stacked tags, preserved choreography.** Two consecutive speech lines by the same speaker must not each carry `X said`; merge the lines or drop the redundant second tag. And relocating a beat must not reorder physical action relative to speech (a character who confirms, then acts, must not be rewritten to act, then confirm).

The default when any of these four would be violated is the bare `said` tag with no beat. A correct, plain tag always beats a grounded beat that repeats, duplicates, loses detail, or reorders.

This rule applies to all chapter drafts, `drafts/`, revision briefs, and all writer- and reviewer-agent outputs. Voice agents and the Voice Editor must flag any line whose speaker is recoverable only through voice recognition, treating it as an attribution defect regardless of how spec-accurate the line is. The Voice Editor additionally owns the four local checks above: on any chapter that has had an attribution pass, it must audit each *inserted* tag and beat against its neighbors, not only the originally ambiguous lines. The Continuity Tracker is the backstop for check 3 (detail-preserving relocation), since dropped concrete detail is a continuity loss. Any writer agent applying attribution must self-run these four checks before returning and must report any case where it fell back to a bare `said` tag because a beat would have violated them. When revising a chapter, scan every first-line-after-narration and every long unattributed run, and add attribution wherever a non-expert reader could lose the thread.
