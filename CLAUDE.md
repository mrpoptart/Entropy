# Entropy - Project Instructions

## Plot Sync Rule

When drafting, revising, or rewriting chapters produces plot changes (new scenes, altered character decisions, shifted timelines, added or removed story beats), the corresponding outline (`book-one/outline.md`) and any affected planning documents (e.g., `convergence-map.md`, character profiles) **must be updated in the same pass**. Do not treat the outline as a static reference; it is a living document that tracks the actual story as written. Writers and revision agents should surface plot changes explicitly so they can be propagated.

## Character Name Rule

The outline must refer to all characters **by name**, including minor and recurring characters (office staff, engineers, crew leads, etc.). When a chapter draft introduces or names a character who is not yet named in the outline, the outline entry for that chapter must be updated in the same pass to include the character's name and a brief role description (e.g., "Tessaly, Dorenne's senior scheduler"). Subsequent outline entries should use the established name, not generic descriptions like "a scheduler" or "the engineer." This ensures writer agents produce consistent names across drafts and revisions.

## Location Name Rule

The outline contains a **Named Locations** gazetteer listing all established district names, building names, infrastructure, and geographic features. Writer agents must check this list before drafting and use established names. Do not invent new location names when an existing one fits. When a chapter draft introduces a genuinely new location, add it to the gazetteer in the same pass with its type and the chapter that established it.

## No Em Dash Rule

Em dashes (`—`, U+2014) are **prohibited** in all prose, dialogue, planning documents, voice specs, agent outputs, and revision notes for this project. Em dashes have become an AI tell, and our texts overuse them to the point of caricature. Replace every em dash with one of the following, chosen by what the dash was actually doing:

- **Mid-sentence aside or elaboration** → use a comma, a pair of commas, or parentheses.
- **Hard break / change of direction** → use a period and start a new sentence, or use a semicolon.
- **Trailing-off, interruption, or stammer in dialogue** → use an ellipsis (`...`) for trailing-off, or a comma plus restart for stammers (e.g., `"I, I don't know."`).
- **Self-correction or hesitation in dialogue** → use a comma or a period plus restart, not a dash.
- **Range or span** (rare) → use "to" or an en dash (`–`, U+2013) if a numeric range is genuinely needed. En dashes are allowed only for numeric ranges.

This rule applies to:
- All chapter drafts (`book-one/chapter-*.md`) and the EPUB build pipeline.
- All `drafts/` and revision briefs.
- All planning documents (`outline.md`, `convergence-map.md`, character profiles, voice specs).
- All review-agent reports and writer-agent outputs. Voice agents proposing line edits **must not** introduce em dashes in their replacements; if a voice rendering needs a beat, use ellipsis or comma-plus-restart.
- This `CLAUDE.md` itself and any future project instructions.

When revising or generating any text, do a final pass to confirm zero em dashes are present. Existing em dashes encountered during normal editing should be converted in the same pass.
