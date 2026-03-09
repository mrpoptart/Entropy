# Audiobook Production Plan — "The Brightest Fire"

Book One of the Entropy Trilogy. 22 chapters, ~700,000 characters of prose.

---

## Overview

This plan covers the end-to-end process for producing an audiobook of Book One using **LM Studio** with locally-run TTS models. The goals are:

1. **Distinct character voices** — each speaking character has a unique, consistent vocal identity
2. **Realistic, human-quality speech** — leveraging the best available open-source TTS models
3. **Consistent pronunciation** — especially for invented names, places, and terminology
4. **Production-quality output** — properly paced narration with chapter structure, scene breaks, and emotional range

---

## Phase 1: Text Preparation

### 1.1 Create Audiobook-Ready Scripts

The raw chapter markdown files need to be converted into TTS-ready scripts. Each chapter file should be processed into a structured script format.

**Tasks:**
- [ ] Strip markdown formatting (headers, bold, italics markers) while preserving meaning
- [ ] Convert scene breaks (`* * *`) into pause markers (e.g., `[PAUSE:3s]`)
- [ ] Tag all dialogue with speaker identification: `[SPEAKER:Dorenne]` / `[SPEAKER:Narrator]`
- [ ] Mark italic interior monologue passages with emphasis tags for the TTS model
- [ ] Annotate emotional register shifts (medium → deep close) as voice direction cues
- [ ] Split chapters into segments of ~2,000–3,000 characters for manageable TTS generation runs

**Output:** One script file per chapter in `book-one/audiobook/scripts/`, e.g., `chapter-01-script.md`

### 1.2 Speaker Identification Pass

Go through every chapter and tag every line of dialogue with the correct speaker. Also identify:

- **Narration** — the bulk of the text (third-person limited, Ash's POV)
- **Dialogue** — spoken lines in double quotes
- **Interior monologue** — italicized direct thoughts (Ash only)
- **Document text** — broadsheets, postings, reports read aloud

**Character Dialogue Inventory (Book One):**

| Character | Chapters Appearing | Speaking Role |
|-----------|-------------------|--------------|
| Ash | 1–22 | Major — speaks in every chapter |
| Dorenne Kharren | 1, 4–7, 10, 12–13, 16–18, 21 | Major — significant dialogue |
| Haran | 3, 8, 13, 20, 22 | Major — sparse but weighted |
| Maren | 1, 4, 6–7, 11, 14 | Supporting — key emotional beats |
| The Mother | 1, 4, 6–7, 11, 18 | Supporting |
| The Father | 1, 4, 6–7, 11, 18 | Supporting |
| Ryn | 2, 6, 9, 14, 21 | Supporting — honest, grounding |
| Halsten | 16 | Minor — earthquake coordination |
| Sorren | 4, 7, 12–13, 16 | Minor — structural assessments |
| Verant | 12–13 | Minor — junction readings |
| Petra | 8, 13, 20 | Minor — workshop tinkerer |
| Davel | 8, 13 | Minor — workshop tinkerer |
| Tavin | 13 | Minor — teenage apprentice |
| Vasra | 5–6 | Minor — scholar who names the Wellspring |
| Jelen Voss | 16 | Minor — young channeler at the dam |
| Misc. vendors, officials, neighbors | Various | Incidental — a line or two each |

---

## Phase 2: Voice Design & Casting

### 2.1 Recommended TTS Models in LM Studio

Based on current LM Studio model availability, here is the recommended model strategy:

| Model | Role | Why |
|-------|------|-----|
| **Orpheus TTS 3B** | Primary narrator + ALL character dialogue | Best emotional range and human-like quality. The model's 8 built-in distinct voices (`tara`, `leo`, `leah`, `dan`, `jess`, `mia`, `zac`, `zoe`) will be used to cast every speaking character. Runs well on M-series Mac. |
| **Kokoro** | Quick iterations | Extremely lightweight (82M params), fast inference. Good for test passes and rapid iteration during script debugging. |

**Recommended approach:** Use **Orpheus TTS 3B** exclusively. Assign a distinct Orpheus voice ID to each major character (e.g., `tara` for Narrator, `leo` for Ash, `leah` for Dorenne) for true multi-voice production. The single-narrator approach was tested and rejected due to insufficient character separation. Use Kokoro only for fast script timing passes.

### 2.2 Voice Profiles

Each character needs a defined vocal identity. These profiles guide model selection, voice parameter tuning, and reference sample creation.

#### The Narrator
- **Quality:** Warm, grounded, conversational. Modern literary fiction register — not declamatory, not theatrical.
- **Range:** Must shift between medium narrative distance (clean, composed, observational) and deep close (fragmented, physical, Ash's raw interiority).
- **Pacing:** Unhurried baseline with controlled acceleration during action sequences (earthquake chapters) and deceleration during emotional beats.
- **Voice type:** Mid-range male, 30s–40s. Think: someone telling you a story they care about.
- **Emotional tags (Orpheus):** Use `<neutral>` for baseline, `<sad>` for grief beats, `<excited>` for power euphoria, `<whisper>` for intimate moments.

#### Ash (dialogue only — distinct from narrator)
- **Quality:** Warm, self-deprecating, quick. The cheerful performance has a specific cadence — light, easy, deflecting. When it drops (stairwell scenes, math scene), the voice goes flatter and slower.
- **Voice type:** Young male, early 20s. Slightly lighter/brighter than the narrator.
- **Key register shifts:** Pre-Wellspring cheerful performance → power euphoria (faster, looser) → post-math sobriety (slower, heavier).

#### Dorenne Kharren
- **Quality:** Precise, authoritative, controlled. Speaks in complete sentences. Every word chosen. Not cold — focused. Her warmth emerges in small cracks between the institutional language.
- **Voice type:** Female, late 50s–early 60s. Lower register, measured cadence. Think: a brilliant administrator who runs a tight ship but cares more than she shows.
- **Pacing:** Deliberately even. Her moments of emotional leakage are marked by pauses, not vocal breaks.

#### Haran
- **Quality:** Dry, patient, unhurried. Speaks in short sentences. Long silences between thoughts. Wry humor that arrives without announcement. His voice carries the weight of decades of understanding, delivered lightly.
- **Voice type:** Male, late 60s–70s. Warm baritone, slightly rough. The voice of someone who's spent most of his life in a workshop.
- **Pacing:** Slow. Comfortable with silence. His pauses aren't dramatic — they're how he talks.

#### Maren
- **Quality:** Competent, precise, controlled — mirrors Dorenne in some ways but younger and warmer. Her speech is efficient and often slightly clipped. She hides vulnerability under briskness.
- **Voice type:** Female, early 20s. Clear, bright, quick. An edge of intensity underneath the composure.
- **Key moments:** When the performance cracks (Ch6: "Twenty-three years, and there were none"), the voice should slow and thin.

#### The Mother
- **Quality:** Fierce, emotional, physical. Speaks from the body — her voice carries her feelings before she can organize them into words. Oscillates between protectiveness and tenderness.
- **Voice type:** Female, late 40s–50s. Warm, slightly rough. Strong emotional range.
- **Pacing:** Variable. Quick when worried, slow when tender. Uses Ash's full name ("Ashlyn") as an emotional register shift.

#### The Father
- **Quality:** Quiet, deliberate, understated. Expresses love through action references and short affirmations. "Good. That's good, son." A man of grip-the-shoulder, not make-a-speech.
- **Voice type:** Male, late 40s–50s. Deep, steady, warm. Few words, each one landing.
- **Pacing:** Unhurried. Never rushed.

#### Ryn
- **Quality:** Direct, honest, unperforming. Says what she means without decoration. Warm but not effusive. Asks practical questions. Her sincerity is her defining vocal quality — she doesn't hedge or soften.
- **Voice type:** Female, early 20s. Mid-range, clear, grounded. 
- **Pacing:** Even, comfortable. She doesn't rush to fill silences.

#### Minor Characters
- **Halsten:** Functional, exhausted, clipboard-voice. Male, 40s.
- **Sorren:** Professional, precise, slightly clipped. Assessment-report cadence. Female.
- **Verant:** Casual, observational. Mentions things "in passing." Female.
- **Petra:** Few words, practical. Workshop colleague energy. Female.
- **Davel:** Dry, brief. "Much better" with unclear sincerity. Male.
- **Vasra:** Academic, measured, awed despite herself. The scholarly surprise voice. Female, older.

### 2.3 Voice Reference Samples

For XTTS v2 voice cloning, you'll need 6–15 second reference audio clips for each character voice:

**Options for sourcing reference audio:**
1. **Record yourself** performing a few lines as each character — XTTS v2 will generalize the vocal identity
2. **Use audiobook samples** from narrators whose vocal quality matches — search for public-domain or Creative Commons readings
3. **Use voice sample databases** — sites like LibriVox (public domain audiobooks) offer a wide range of narrator styles
4. **AI-generated reference voices** — use Orpheus TTS with extreme parameter tweaking to generate a reference sample, then feed that to XTTS v2 for consistency

**Recommended:** Start with option 1. Record yourself reading 2–3 short lines as each character. Even rough performances work — XTTS v2 extracts vocal identity (pitch, timbre, cadence) rather than acting quality.

Store reference samples in: `book-one/audiobook/voice-references/`

---

## Phase 3: Pronunciation Guide

### 3.1 Custom Pronunciation Lexicon

This is the **critical** consistency document. Every invented word needs an authoritative pronunciation specified in IPA (International Phonetic Alphabet) and a phonetic respelling for human reference. This lexicon should be embedded in TTS prompts or used to pre-process text with phonetic hints.

#### Character Names

| Word | IPA | Phonetic Guide | Notes |
|------|-----|----------------|-------|
| Ash | /æʃ/ | ASH | Short, single syllable |
| Ashlyn | /ˈæʃ.lɪn/ | ASH-lin | Full name; used rarely, by parents only |
| Torren | /ˈtɒr.ən/ | TOR-en | Family surname |
| Maren | /ˈmɛər.ən/ | MAIR-en | Rhymes with "Karen" ✓ |
| Haran | /ˈhɑː.rən/ | HAR-an | Soft 'a', unstressed second syllable |
| Dorenne | /dɔːˈrɛn/ | dor-EN | Stress on second syllable; the French feel matches her bearing |
| Kharren | /ˈkɑːr.ən/ | KAR-en | Her surname; the 'kh' is a hard K, not guttural |
| Ryn | /rɪn/ | RIN | Single syllable, short |
| Davan | /ˈdɑː.vən/ | DAH-van | Not "DAY-van" |
| Halsten | /ˈhɔːl.stən/ | HALL-sten | |
| Sorren | /ˈsɒr.ən/ | SOR-en | |
| Verant | /ˈvɛr.ənt/ | VEHR-ant | |
| Petra | /ˈpɛt.rə/ | PET-ra | Standard |
| Davel | /ˈdæv.əl/ | DAV-el | |
| Tavin | /ˈtæv.ɪn/ | TAV-in | |
| Vasra | /ˈvæz.rə/ | VAZ-ra | |
| Jelen Voss | /ˈdʒɛl.ən vɒs/ | JEL-en VOSS | |
| Comyn | /ˈkɒm.ɪn/ | KOM-in | |
| Edrin Solath | /ˈɛd.rɪn ˈsɒl.əθ/ | ED-rin SOL-ath | Historical figure; mentioned in exposition |

#### Place Names

| Word | IPA | Phonetic Guide | Notes |
|------|-----|----------------|-------|
| Solathis | /sɒˈlɑː.θɪs/ | sol-AH-this | Stress on second syllable. The city. |
| Verenthi Range | /vɛˈrɛn.θi/ | veh-REN-thee | Mountain range |
| Verandhi Coast | /vɛˈrɑːn.di/ | veh-RAHN-dee | Southern seaboard |
| Ashward Ridge | /ˈæʃ.wərd/ | ASH-ward | Highland country |
| Hearthlands | /ˈhɑːrθ.lændz/ | HARTH-lands | Agricultural belt |
| Kharren Fault | /ˈkɑːr.ən/ | KAR-en | Same as Dorenne's surname — **unintentional collision**; consider renaming the fault to avoid confusion in audio (e.g., "Tharen Fault," "Gorren Fault") |
| Thornwall | /ˈθɔːrn.wɔːl/ | THORN-wall | District / aqueduct name |
| Verengate | /ˈvɛr.ən.ɡeɪt/ | VEHR-en-gate | District |
| Threadneedle | /ˈθrɛd.niː.dl̩/ | THRED-needle | District |
| Saddler's Row | Standard | SADD-ler's ROW | |
| Harrier Street | Standard | HAIR-ee-er | |
| Coppersmiths' Terrace | Standard | | |
| Weaver's Terrace | Standard | | |
| Colter Street | /ˈkoʊl.tər/ | KOHL-ter | |
| The Splits | Standard | | Workshop district on the Fifth Terrace |
| Kelleren aqueduct | /ˈkɛl.ər.ən/ | KEL-er-en | |
| Velden building | /ˈvɛl.dən/ | VEL-den | Location of the pump project |
| Grayspire | Standard | GRAY-spire | Mentioned in ch12 |

#### Magic & World Terminology

| Word | IPA | Phonetic Guide | Notes |
|------|-----|----------------|-------|
| Channeling | Standard | CHAN-el-ing | The act of using magic |
| Channeler | Standard | CHAN-el-er | A person who channels |
| Pool | Standard | POOL | Daily magical budget |
| Wellspring | Standard | WELL-spring | Ash's massive reservoir |
| Reservoir | Standard | REZ-er-vwar | Total stored energy |
| Resonance disc | Standard | REZ-oh-nance DISK | Communication device |
| Dead weight | Standard | DEAD WEIGHT | Slur for non-channelers |
| Running hot | Standard | | Channeling inefficiently |
| Clean channeling | Standard | | Efficient technique |
| Flooding | Standard | | Brute-force channeling |
| The hum | Standard | | Full-pool sensation |
| Dry | Standard | | Out of magic for the day |
| The Levelers | Standard | | Political movement (mentioned in broadsheets) |
| Elder-days | Standard | | Unit of measurement for reservoir |

> [!IMPORTANT]
> **Pronunciation decisions needed:** Several names have ambiguous pronunciations. Before production begins, record yourself saying each invented word and confirm the pronunciation feels right for the character/place. The guide above represents best-guess defaults. Update this table as the authoritative source.

### 3.2 TTS Pronunciation Enforcement

Most TTS models handle pronunciation through one of these methods:

1. **Phonetic respelling in the script** — Replace `Solathis` with `Sol-AH-this` on first use, or use SSML-like markup: `<phoneme alphabet="ipa" ph="sɒˈlɑː.θɪs">Solathis</phoneme>`
2. **Custom lexicon file** — Some TTS systems accept a pronunciation dictionary that maps words to phonemes. Create one at `book-one/audiobook/lexicon.json`.
3. **Post-processing consistency check** — After generating audio, listen specifically for pronunciation of every invented word. If a model mispronounces a word, add phonetic respelling directly into the script for that segment.

**Recommended approach:** Create a preprocessing script that replaces all invented words with phonetic hints before sending to the TTS model. This is more reliable than hoping the model infers correctly.

---

## Phase 4: Production Pipeline

### 4.1 Workflow Per Chapter

```
┌─────────────────────────────────────────────────┐
│  1. PREPARE SCRIPT                              │
│     chapter-XX.md → chapter-XX-script.md        │
│     Strip markdown, tag speakers, add cues      │
├─────────────────────────────────────────────────┤
│  2. PREPROCESS                                  │
│     Apply pronunciation lexicon                 │
│     Split into segments (~2,000 chars each)      │
│     Assign voice/model per segment              │
├─────────────────────────────────────────────────┤
│  3. GENERATE AUDIO                              │
│     Run each segment through LM Studio          │
│     Orpheus for narration + major characters    │
│     XTTS v2 for character-specific voices       │
├─────────────────────────────────────────────────┤
│  4. REVIEW & ITERATE                            │
│     Listen for pronunciation errors             │
│     Check emotional register matches            │
│     Re-generate problem segments                │
├─────────────────────────────────────────────────┤
│  5. ASSEMBLE                                    │
│     Join segments per chapter                   │
│     Insert scene-break pauses (3s silence)      │
│     Add chapter markers                         │
├─────────────────────────────────────────────────┤
│  6. MASTER                                      │
│     Normalize volume across segments            │
│     Apply light compression for consistency     │
│     Export as chapter-level audio files          │
└─────────────────────────────────────────────────┘
```

### 4.2 LM Studio Configuration

**Model loading:**
1. Open LM Studio → Discover tab
2. Download **Orpheus TTS 3B** (requires ~6–8GB VRAM; M-series Mac handles this)
3. Download **XTTS v2** for voice cloning
4. Download **Kokoro** for fast draft passes

**API usage for batch processing:**
- LM Studio exposes a local API server (typically `http://localhost:1234`)
- Create a Python script to send text segments to the API and save audio output
- Store script at: `book-one/audiobook/scripts/generate_audio.py`

**Orpheus TTS emotional tags:**
```
[narrator, neutral] He crossed the bridge and paused at the far side.
[narrator, sad] The old kettle sat in the cabinet where she'd placed it.
[narrator, excited] The stone beneath his palm was glowing.
```

### 4.3 Audio Assembly Tools

You'll need basic audio tools for post-processing:

- **FFmpeg** — For joining segments, inserting silences, normalizing volume
- **Audacity** — For manual review, fine edits, and QA listening passes
- **Sox** — For batch audio processing (normalize, trim silence)

**Chapter assembly command pattern (FFmpeg):**
```bash
# Join segments with scene-break pauses
ffmpeg -f concat -i chapter-XX-segments.txt -c copy chapter-XX-raw.wav

# Normalize volume
ffmpeg -i chapter-XX-raw.wav -af loudnorm=I=-16:LRA=11:TP=-1.5 chapter-XX.mp3
```

---

## Phase 5: Production Order

### 5.1 Pilot Chapter

Start with **Chapter 1** as the pilot production. This chapter is ideal because:

- It contains **all narrative modes** — medium distance narration, scene-setting, dialogue, interior monologue
- It features **5 speaking characters** — Ash, Father, Mother, Maren, Dorenne
- It has **emotional range** — quiet morning, the private stairwell moment, the Dorenne encounter, the celebration
- It's the **first impression** — if the voice, pacing, and pronunciation work here, the foundation is set

**Pilot chapter milestones:**
1. [ ] Complete Chapter 1 script with speaker tags
2. [ ] Record/source voice reference samples for narrator + 5 characters
3. [ ] Generate draft audio using Kokoro (fast pass for script debugging)
4. [ ] Generate production audio using Orpheus TTS
5. [ ] Apply character voices using XTTS v2
6. [ ] Assemble chapter, review, iterate
7. [ ] Lock pronunciation guide based on pilot results

### 5.2 Full Production Sequence

After the pilot, produce chapters in narrative order (1–22). However, prioritize generating voice profiles early for characters with the most dialogue:

**Priority voice profile creation:**
1. Narrator (used throughout)
2. Ash (dialogue — every chapter)
3. Dorenne (major dialogue in 11+ chapters)
4. Haran (key chapters — sparse but emotionally crucial)
5. Maren (emotional beats)
6. Mother / Father (supporting)
7. Ryn (supporting)
8. All minor characters

### 5.3 Estimated Production Timeline

| Phase | Duration Estimate | Notes |
|-------|------------------|-------|
| Text preparation (all 22 chapters) | 2–3 days | Script conversion, speaker tagging |
| Voice design & reference recording | 1–2 days | Record samples, test with XTTS v2 |
| Pronunciation guide finalization | 1 day | Listen, decide, document |
| Pilot chapter (Ch1) | 2–3 days | Full pipeline test, iteration |
| Pipeline automation (scripting) | 1–2 days | Batch processing scripts |
| Chapters 2–22 production | 3–5 weeks | ~1–2 chapters per day, with QA |
| Final assembly & mastering | 2–3 days | Normalize, export, chapter markers |
| **Total** | **~5–7 weeks** | Assumes part-time effort |

---

## Phase 6: Quality Assurance

### 6.1 Per-Chapter QA Checklist

- [ ] **Pronunciation:** All invented words match the lexicon
- [ ] **Voice consistency:** Each character sounds like themselves across segments  
- [ ] **Emotional register:** Narrator shifts between medium and deep close appropriately
- [ ] **Pacing:** Scene breaks have proper pauses; no rushed transitions
- [ ] **Volume:** Consistent levels across segments; no jarring jumps
- [ ] **Artifacts:** No digital glitches, repeated words, or unnatural prosody
- [ ] **Dialogue flow:** Conversations sound natural; proper pause between speakers

### 6.2 Known Challenges & Mitigations

| Challenge | Mitigation |
|-----------|------------|
| TTS models mispronouncing invented words | Phonetic respelling in scripts + lexicon preprocessing |
| Maintaining character voice consistency across 22 chapters | XTTS v2 voice cloning from locked reference samples; re-use same reference for all segments of a character |
| Emotional range — the book demands grief, euphoria, devastation | Orpheus TTS emotional tags; split highly emotional passages into smaller segments for more control |
| Scene breaks and pacing | Explicit pause markers in scripts; post-processing silence insertion |
| Long narration passages losing listener engagement | Vary pacing subtly; use the style guide's "controlled lyrical peaks" as moments to adjust vocal energy |
| Em-dash interruptions in dialogue | Test how models handle these; may need to split into separate segments at interruption points |
| Interior monologue (italicized thoughts) | Generate with different vocal quality — slightly more intimate, possibly lower volume — to distinguish from narration |

---

## File Structure

```
book-one/audiobook/
├── production-plan.md          ← This document
├── pronunciation-guide.md      ← Expanded lexicon (extracted from this doc)
├── voice-profiles.md           ← Detailed character voice specifications
├── voice-references/           ← Audio reference samples per character
│   ├── narrator.wav
│   ├── ash.wav
│   ├── dorenne.wav
│   ├── haran.wav
│   └── ...
├── scripts/                    ← TTS-ready chapter scripts
│   ├── chapter-01-script.md
│   ├── chapter-02-script.md
│   └── ...
├── tools/                      ← Automation scripts
│   ├── generate_audio.py       ← LM Studio API batch processor
│   ├── preprocess_script.py    ← Lexicon substitution / script prep
│   └── assemble_chapter.sh     ← FFmpeg assembly pipeline
├── output/                     ← Generated audio
│   ├── segments/               ← Individual TTS-generated segments
│   ├── chapters/               ← Assembled chapter audio files
│   └── master/                 ← Final mastered output
└── qa/                         ← QA notes and issue tracking
    └── qa-log.md
```

---

## Resolved Decisions

- **Maren pronunciation:** MAIR-en (rhymes with "Karen") ✓
- **Kharren Fault / Kharren surname:** Unintentional name collision. Consider renaming the fault for the audiobook to avoid listener confusion, since identical pronunciation for a geological feature and a character surname could be disorienting in audio format. ✓
- **Narration approach:** True multi-voice casting. The single-narrator approach (using one voice and relying on text cues for differentiation) proved insufficient for character distinction. Instead, the final audiobook will assign entirely different Orpheus voice models to specific characters for their dialogue lines (e.g., `tara` for Narrator, `leo` for Ash, `leah` for Dorenne, `dan` for Haran), stitched together in post-production. ✓
- **Interior monologue:** Ash's dialogue voice at a slightly lower, more intimate register. ✓
- **Chapter length and format:** 22 chapters, ~35–45 minutes each, ~13–16 hours total. Export as both WAV (archival/editing quality) and MP3 (listening/distribution). ✓
- **Mother and Father:** Unnamed in text. Narrator carries their vocal identity through modulated delivery — deeper/steadier for the Father, warmer/fiercer for the Mother. ✓
