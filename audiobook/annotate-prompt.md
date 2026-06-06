# Audiobook Annotation Prompt

Use this prompt (or paste it into a fresh Claude session) to annotate any
chapter for the Gemini TTS single-narrator audiobook pipeline.

---

You are preparing a chapter of the Entropy novel for audiobook narration by
a single voice (Aoede). The narrator performs all characters via subtle
shifts; the actual rendering follows performance cues you embed in the text.

**What to do:**

1. Read the chapter end to end.
2. Before every line of spoken dialogue, insert a bracketed cue describing
   how the line should be performed. Cues are 2–5 short adjectives or short
   phrases, comma-separated, e.g. `[deep, resonant, tired-warm, low register]`.
3. Cues are character-grounded. Build a small style sheet at the top of your
   working notes so the same character sounds consistent across all their
   lines. Reference the project's character voice specs in
   `characters/*.md` when available.
4. Cues describe **affect** (emotion, register, body), not stage business
   (no "[whispering]" unless the line is canonically whispered in the prose;
   no "[pause]"). Performance, not blocking.
5. Narrative paragraphs (no quoted speech) get NO cues — they default to
   Aoede's warm narrator voice.
6. Italicized inner-monologue passages (e.g. `*Look how much I can spare.*`)
   should have the asterisks stripped and may carry a single cue if the
   tonal shift is sharp; otherwise leave them in narrator voice.
7. Preserve all original prose. Do not paraphrase, condense, or move sentences.
   You are only inserting cues and stripping italic asterisks.
8. Keep scene breaks (`* * *`) on their own line — the renderer splits there.

**Voice register references** (extend per chapter):

- **Ash** — bright, hedging, chatter-as-armor, fast, apologetic, looping;
  voice tightens to declarative when ground-truthing something he means.
- **Father (Haran-the-elder, Ash's father)** — deep, resonant, tired-warm,
  low register, careful, spare.
- **Mother (Leska)** — warm-controlled by default; cracks open into fierce
  tenderness on emotional beats; pivots to logistics-mode under strain.
- **Maren** — clean, precise, composed, slightly cool, sharp; the lightness
  is a mask that should sound *almost* natural.
- **Dorenne** — institutional-precise, dry, calibrating, direct, attentive.
- **Tertiary characters** (vendors, clerks) — neutral, transactional,
  unremarkable. No distinctive cues. Default register.

**Output format:**

```
---
style: warm conversational audiobook narrator at natural reading pace.
  Bracketed cues like [deeper, resonant] are performance directions for
  the next line of dialogue only; do not read the brackets aloud. Return
  to the warm narrator voice for all unbracketed narration.
voice: Aoede
---
[chapter title heading here, e.g. "Chapter One."]

Narrative paragraph in narrator voice...

[cue] "Dialogue line."

Narrative continues...

* * *

[next scene begins]
```

Write the annotated chapter file to `audiobook/chapters/chapter-NN.annotated.txt`.
