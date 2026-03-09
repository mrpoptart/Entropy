# LM Studio Setup Guide — Audiobook Production

Step-by-step instructions for using LM Studio with Orpheus TTS to generate audiobook audio.

---

## How It Actually Works

Orpheus TTS runs as an **LLM** inside LM Studio, not as a dedicated TTS endpoint. Here's what happens under the hood:

1. You send text to LM Studio's **completions API** (`/v1/completions`)
2. The Orpheus model generates a stream of special **audio tokens** (e.g., `<custom_token_10542>`)
3. A **SNAC decoder** (a separate Python library) converts those tokens into a 24kHz WAV audio file

This means you can't just call a simple "text → audio" API. You need a Python script that handles the token generation *and* the SNAC decoding. The good news: there's an open-source tool that does exactly this.

---

## Your Current Setup ✓

Based on your screenshot, you already have:

- ✅ LM Studio installed and running
- ✅ Server active at `http://127.0.0.1:1234`
- ✅ Model loaded: `vt-orpheus-3b-tts-ceylia-q4kmf` (READY)
- ✅ API endpoints available (completions, chat, models)

The model is loaded and the server is running. You're ready for the Python pipeline.

---

## Step 1: Install the Orpheus TTS Local Client

The easiest path is using the `orpheus-tts-local` tool, which wraps LM Studio's API and handles all the token-to-audio conversion for you.

Open Terminal and run:

```bash
# Navigate to the audiobook tools directory
mkdir -p ~/Desktop/work/Entropy/book-one/audiobook/tools
cd ~/Desktop/work/Entropy/book-one/audiobook/tools

# Clone the Orpheus TTS local client
git clone https://github.com/isaiahbjork/orpheus-tts-local.git
cd orpheus-tts-local

# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> [!IMPORTANT]
> The `requirements.txt` will install PyTorch (for the SNAC decoder), numpy, sounddevice, and other dependencies. This may take a few minutes and use ~2GB of disk space.

---

## Step 2: Generate Your First Audio Clip

With LM Studio still running and the Orpheus model loaded, test it:

```bash
cd ~/Desktop/work/Entropy/book-one/audiobook/tools/orpheus-tts-local
source venv/bin/activate

# Generate a test clip using a line from Chapter 1
python gguf_orpheus.py \
  --text "He crossed the bridge and paused at the far side, one hand resting on the stone where the old channeling had started to crack." \
  --voice leo \
  --output "../../output/test_narrator.wav"
```

If everything is working, you'll see token generation progress in the terminal and a WAV file will appear at `book-one/audiobook/output/test_narrator.wav`. Play it to hear the result.

> [!TIP]
> If you get a connection error, verify LM Studio shows **Status: Running** and the model shows **READY**. The API server must be active at `http://127.0.0.1:1234`.

---

## Step 3: Voice Casting

Orpheus has **8 built-in voices**. Before producing any chapters, test each voice with sample dialogue from the book:

| Voice | Gender | Quality |
|-------|--------|---------|
| `tara` | Female | Best overall quality (default); warm, clear |
| `leah` | Female | Measured, mature |
| `jess` | Female | Bright, natural |
| `mia` | Female | Soft, expressive |
| `zoe` | Female | Even, direct |
| `leo` | Male | Mid-range, warm |
| `dan` | Male | Deeper, steady |
| `zac` | Male | Younger, energetic |

### Voice casting script

Run this to generate all 8 voices for a narrator sample and a dialogue sample:

```bash
cd ~/Desktop/work/Entropy/book-one/audiobook/tools/orpheus-tts-local
source venv/bin/activate

mkdir -p ../../output/casting

# Test narrator line with all voices
for voice in tara leah jess mia zoe leo dan zac; do
  python gguf_orpheus.py \
    --text "The inspection had taken most of the morning. Ash worked his way along the Thornwall aqueduct, checking each joint where the old channeling had started to fracture." \
    --voice "$voice" \
    --output "../../output/casting/narrator_${voice}.wav"
done
```

Then test character-specific lines:

```bash
# Dorenne
python gguf_orpheus.py \
  --text "Your power is significant, but the city's needs are enormous. If we allocate wisely, we can stabilize the most critical systems first." \
  --voice leah \
  --output "../../output/casting/dorenne_leah.wav"

# Haran
python gguf_orpheus.py \
  --text "Your hands still work. The power doesn't replace them. It's another tool. You don't use a hammer on glass." \
  --voice dan \
  --output "../../output/casting/haran_dan.wav"

# Ash (dialogue)
python gguf_orpheus.py \
  --text "Sorry, I can't channel. At all. The stairs are that way if you'd like company on the walk." \
  --voice zac \
  --output "../../output/casting/ash_zac.wav"

# Maren
python gguf_orpheus.py \
  --text "Twenty-three years, and there were none. I'm used to being the Torren who channels. Now I'm the Torren who's related to the Torren who channels." \
  --voice tara \
  --output "../../output/casting/maren_tara.wav"
```

Listen to each result and decide which voice best fits each character.

---

## Step 4: Emotional Tags

You can embed emotional expressions directly in the text. Orpheus will produce natural-sounding speech with these:

| Tag | Effect | Example |
|-----|--------|---------|
| `<laugh>` | Laughter | Ash and Ryn at the plateau |
| `<chuckle>` | Soft laugh | Haran's dry humor |
| `<giggle>` | Giggle | Lighter moments |
| `<sigh>` | Sigh | Weariness, resignation |
| `<gasp>` | Sharp intake | Activation, earthquake |
| `<cough>` | Cough | Background realism |
| `<sniffle>` | Sniffle | Emotional scenes |
| `<groan>` | Groan | Physical strain |
| `<yawn>` | Yawn | Scene transitions |

**Example with emotion:**
```bash
python gguf_orpheus.py \
  --text "<sigh> You could have reinforced the eastern retaining wall with what that cost. That wall protects four thousand people." \
  --voice leah \
  --output "../../output/dorenne_sigh.wav"
```

You can also add filler sounds like `uhm` to make dialogue more natural.

---

## Step 5: Tuning Parameters

The script accepts parameters that affect audio quality:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `--temperature` | 0.6 | Higher = more expressive/varied; lower = more consistent/flat |
| `--top_p` | 0.9 | Controls diversity of token selection |
| `--repetition_penalty` | 1.1 | Prevents audio artifacts from repeated tokens. **Keep ≥ 1.1** |

**For narration:** Use default settings (0.6 temp) for consistent, clean narration.  
**For emotional peaks:** Try `--temperature 0.7` or `0.8` for more expressive delivery.  
**For Haran's dry calm:** Try `--temperature 0.5` for steadier, more controlled speech.

---

## Step 6: Batch Production (for full chapters)

For producing full chapters, you'll want to split the text into segments and generate each one. Here's the basic pattern:

```bash
# Generate a segment
python gguf_orpheus.py \
  --text "Your text segment here" \
  --voice leo \
  --output "../../output/segments/ch01_seg01.wav"

# Join segments with FFmpeg
# First install FFmpeg if you don't have it:
# brew install ffmpeg

# Create a list file for FFmpeg
echo "file 'ch01_seg01.wav'" > segments.txt
echo "file 'ch01_seg02.wav'" >> segments.txt
# ... etc

# Join them
ffmpeg -f concat -safe 0 -i segments.txt -c copy ch01_complete.wav
```

> [!NOTE]
> The production plan at [production-plan.md](production-plan.md) has the full chapter-by-chapter pipeline, including script preparation, pronunciation processing, and quality assurance checklists.

---

## Model-Specific Notes

Your model (`vt-orpheus-3b-tts-ceylia-q4kmf`) may have slightly different behavior from the baseline `orpheus-3b-0.1-ft`. The "ceylia" variant appears to be a community fine-tune. If the `orpheus-tts-local` script has issues with model name matching, you can edit `gguf_orpheus.py` line where `"model"` is set in the payload — LM Studio ignores this field and uses whatever model is currently loaded, so the value doesn't need to match.

---

## Quick Reference

| What | Value |
|------|-------|
| LM Studio API | `http://127.0.0.1:1234` |
| API Endpoint | `/v1/completions` (NOT `/v1/audio/speech`) |
| Your model | `vt-orpheus-3b-tts-ceylia-q4kmf` |
| Voices | `tara`, `leo`, `mia`, `zac`, `jess`, `dan`, `leah`, `zoe` |
| Emotions | `<laugh>`, `<chuckle>`, `<giggle>`, `<sigh>`, `<gasp>`, `<cough>`, `<sniffle>`, `<groan>`, `<yawn>` |
| Audio format | 24kHz WAV (mono, 16-bit PCM) |
| Tool location | `book-one/audiobook/tools/orpheus-tts-local/` |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Connection refused" | Make sure LM Studio is open, model shows READY, Status shows Running |
| No audio output / empty file | Check terminal for token generation — you should see streaming tokens. If not, the prompt format may need adjustment |
| Audio sounds garbled | Try lowering `--temperature` to 0.5. Ensure `--repetition_penalty` is ≥ 1.1 |
| SNAC decoder errors | Make sure PyTorch installed correctly: `pip install torch` |
| Very slow generation | Normal — Orpheus generates tokens sequentially. Each 10-second clip may take 30–60+ seconds depending on your Mac's specs |
| Model name mismatch warning | Edit `gguf_orpheus.py` — change the `"model"` field in the payload to anything; LM Studio ignores it |
| Pronunciation wrong | Add phonetic respelling in the text (see pronunciation guide in `production-plan.md`) |
