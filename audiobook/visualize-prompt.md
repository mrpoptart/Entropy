# Scene Visualization Workflow

This is the project-asset version of the "visualize a scene" skill. (User's
global rule disallows manually installing into `.claude/skills/`, so the
skill lives here as reusable scripts + this doc.)

## Layout

```
audiobook/
  characters/
    _style.md           # global visual style spec (graphic novel, 16:9, ...)
    ash.md              # one sheet per major character
    father.md
    mother.md
    maren.md
    haran.md
    dorenne.md
  visualize.py          # script that builds prompt and calls OpenAI gpt-image-1
  .openai-key           # API key (gitignored)
  images/               # generated images (gitignored)
```

## Three modes

### 1. Generate a character reference portrait

```bash
python visualize.py --portrait ash
python visualize.py --portrait father
```

Writes `characters/<name>-portrait.png`. Do this once per character to
sanity-check the anchor line produces a consistent person.

### 2. Visualize one audio chunk

The renderer (`render-chapter.py`) drops a `.txt` per audio chunk next to
the `.wav`. To illustrate that chunk:

```bash
python visualize.py out/chapter-01/scene-1-chunk-03.txt --chars ash father
```

This reads the chunk text, strips TTS cues, builds a scene moment from the
first ~600 chars, and writes a PNG alongside the WAV (same stem).

### 3. Ad-hoc moment

```bash
python visualize.py --moment "Ash strikes flint at the iron stove before dawn, kitchen dark except for the spark" --chars ash --out images/scratch.png
```

## How prompts are built

`visualize.py` composes a prompt like:

```
STYLE: <_style.md "Style anchor" block>

CHARACTERS PRESENT (render with these exact features):
- <ash.md "Anchor line" block>
- <father.md "Anchor line" block>

SCENE: <first 600 chars of chunk text with [cues] stripped>

AVOID: <concatenated "Negative prompt" blocks>
```

Character anchors are verbatim sentences from each sheet — repeating them
across every render is the consistency mechanism.

## Cost (gpt-image-1, 1536x1024)

- low: ~$0.011 / image
- medium: ~$0.042 / image (default)
- high: ~$0.167 / image

Chapter 1 chunked at 1500 chars produced ~30 chunks. At medium that's
~$1.20 per chapter, ~$25 for the whole 22-chapter book. At high it's ~$5
per chapter, ~$110 for the book.

## Suggested workflow per chapter

1. Confirm character anchors render consistently — generate portraits of
   every character that will appear, eyeball them, edit the anchor lines
   in `characters/*.md` until they look right.
2. Render audio chunks for the chapter with `render-chapter.py`.
3. For each chunk, decide which characters are present (or auto-detect by
   greping the chunk text for character names — possible future helper).
4. Run `visualize.py` for each chunk. Spot-check, regenerate any that
   miss.
5. When ready, run an ffmpeg ken-burns assembly to produce an MP4 with
   the chunk audio aligned to the chunk image (separate tooling, later).
