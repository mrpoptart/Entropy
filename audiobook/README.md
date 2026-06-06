# Entropy Audiobook — Gemini TTS

## Setup

```bash
# Save your key one of these ways:
echo 'YOUR_KEY' > audiobook/.key            # gitignored
# or
export GEMINI_TTS_API_KEY=YOUR_KEY
```

> ⚠️ The key you pasted in chat (`AQ.Ab8R…`) should be rotated in the
> Google Cloud console; treat it as exposed.

## Test the four scenarios

```bash
cd audiobook
python tts.py examples/01-narrator-sentence.txt
python tts.py examples/02-narrator-paragraph.txt
python tts.py examples/03-narrator-plus-one.txt
python tts.py examples/04-multi-voice-scene.txt
```

Outputs land in `audiobook/out/<name>.wav`. Play with `afplay out/01-narrator-sentence.wav` on macOS.

## Granularity

- **Sentence / paragraph**: write a one-off file or pipe stdin:
  `echo "One line." | python tts.py - --voice Aoede --style "warm"`
- **Chapter**: copy the chapter body into a file with a frontmatter block
  and run the script. For multi-voice chapters, prefix every spoken line
  with `Character:` and list speaker→voice mappings in `speakers:`.

## File format

```
---
style: free-text style/tone prompt (optional)
voice: Aoede                 # single-voice mode
# OR
speakers:
  Narrator: Aoede
  Ash: Puck
  Father: Charon
language: en-US              # optional, default en-US
---
Body text. For multi-voice, every line is "Speaker: text";
blank lines and continuation lines attach to the prior turn.
```

## Limits

- **Multi-speaker mode is capped at exactly 2 voices.** The Gemini TTS preview
  rejects any `speakers:` block with more or fewer than 2. For 3+ voice scenes
  (e.g. Narrator + Ash + Father), either fold the narrator into one of the
  character voices, render the narrator separately and stitch in audio, or use
  single-voice mode and let one narrator perform everyone.
- Per-request length is bounded; for chapter-scale audio you will need to
  segment and concatenate.

## Notes / gotchas

- `MODEL` in `tts.py` is set to `gemini-3.1-flash-tts-preview` to match
  your playground screenshot. If Google renames the preview, edit that
  one constant.
- The multi-speaker request shape (`multiSpeakerMarkup` + `multiSpeakerVoiceConfig`)
  is the current Cloud TTS schema for Gemini TTS preview; if the API
  errors on a multi-voice call, run with `--dry-run` to inspect the payload
  and compare against current Google docs.
- `LINEAR16 @ 22050 Hz`, speed 1.0, gain 0 dB — matches your settings.
- Voices in the playground (Aoede, Puck, Charon, Kore, Fenrir, etc.) are
  the prebuilt Gemini TTS voice names; swap freely in frontmatter.
