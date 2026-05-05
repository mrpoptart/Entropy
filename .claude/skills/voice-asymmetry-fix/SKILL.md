---
name: voice-asymmetry-fix
description: "Use when two characters with contrasting voice specs are sharing scene time and one has collapsed toward the other's register. Trigger phrases: 'they sound the same', 'too terse', 'both sound like Haran', 'voice has collapsed', 'fix Ash's voice', 'restore the asymmetry'. NOT for general style-guide compliance (use Voice Editor) or single-character drift in isolation (use the per-character voice agent alone)."
license: MIT
metadata:
  version: 1.0.0
  author: Morgan
  category: entropy-fiction
  updated: 2026-05-02
---

# Voice Asymmetry Fix

You are a voice repair specialist for the Entropy trilogy. Your goal is to restore audible contrast between two characters whose voices have collapsed toward the same register in a chapter.

## Before Starting

Read these files before doing anything else:
- `CLAUDE.md` -- the Voice Asymmetry Rule and Voice Variety Rule
- `characters/protagonist.md` -- Ash's full voice spec
- `characters/mentor.md` -- Haran's full voice spec
- The chapter file being audited

Only ask for information not available in those files.

## How This Skill Works

### Mode 1: Diagnose and Fix (full pass)

When you have a chapter where two characters sound alike and you need to find and fix all collapse points.

**Step 1: Identify the collapsed pair.**
Name the two characters. State which one has drifted toward the other's register (usually the more expansive voice has compressed toward the more economical one).

**Step 2: Run the per-character voice agent for the collapsed character.**
The agent produces:
- Line-level spec drift flags with proposed revisions
- Cross-character collapse flags (lines that could be assigned to the other speaker)
- Missed opportunities (places the character should have spoken distinctively and didn't)
- Working lines to preserve

**Step 3: Compile the full fix list.**
Every flagged line becomes a numbered fix. Format:
```
Fix N -- Line ~[number]: [one-line description]
Find: [exact quoted text]
Replace with: [spec-compliant revision]
```

**Step 4: Apply all fixes in a single pass.**
Use a writer agent. Pass the complete fix list. Instruction: apply every fix exactly as listed, preserve all prose not listed, no partial application.

**Step 5: Verify the asymmetry is restored.**
After applying fixes, read the dialogue exchanges aloud (or scan them) and check: is the contrast between the two voices now audible? Can you tell who is speaking from register alone, without dialogue tags?

### Mode 2: Quick Asymmetry Check (diagnostic only)

When you want to know whether the asymmetry has collapsed before committing to a full fix pass.

Pick three dialogue exchanges between the two characters. For each exchange:
- Count the words in each character's contribution
- Check whether the shorter speaker is the one whose spec calls for economy
- Check whether the longer speaker's extra words are doing spec-compliant work (hedging, looping, deflecting) or are just filler

If the ratios are reversed or matched, the asymmetry has collapsed. Proceed to Mode 1.

### Mode 3: Recovery Environment Check (Ash/Haran specific)

When the chapter is set in Haran's workshop and Ash still sounds post-drift compressed throughout.

The spec states: "warmth recovers whenever he is physically grounded with Haran." Check:
- Is any scene set at Haran's bench, at Haran's workshop, or in a working session with Haran?
- In those scenes, does Ash's sentence length increase?
- Does any of the following appear: apology-as-greeting, self-deprecating loop, quoted-Haran-back-at-Haran, flagged joke, trailing off rather than escalating?

If none of these appear in a workshop-set scene, flag it as a recovery environment failure. Apply Mode 1 fixes with specific attention to those scenes.

## The Ash/Haran Asymmetry Reference

This is the canonical collapsed pair in the Entropy trilogy. Use as the reference model for all other pairs.

**What Haran sounds like:**
- Flat two-word openers: "So." / "Hm." / "That's interesting."
- Medium sentences when unpacking a thought; short ones before and after
- Mechanism analogies: whatever is in his hands becomes the metaphor
- Patient pauses -- he does not fill silence
- Dry asides delivered half under his breath
- One more question instead of an answer
- Almost no abstract emotional vocabulary

**What Ash sounds like (workshop recovery mode):**
- Multi-clause loops with three side-paths
- Apology tucked into mid-sentence: "which, I should have tested that earlier, but, well"
- Self-deprecating flags: "which is a terrible reason, but here we are"
- Quotes other people back at them: "Haran says you don't use a hammer on glass, which, fair"
- Trails off rather than escalating: "it's not... it's not even close"
- Returns to concrete physical detail when emotion goes heavy
- "Yeah, I, I noticed that, sorry" not "I know"

**The ratio test:**
Haran asks: "How much is left?"
Ash answers: "Enough, I think, probably, hard to say, you know how it is."
Five words vs. fifteen. That ratio is the target. If Ash answers in five words, the asymmetry has collapsed.

**Collapse signatures to flag immediately:**
- Ash answers a Haran question in under eight words with no hedge
- Ash opens a line with "I know" (Haran's flat acknowledgment register)
- Ash completes Haran's thought confidently and without hesitation
- Ash delivers a moral verdict in two sentences ("It buys time. Not enough.")
- Any Ash line that could be spoken by Haran without the reader noticing

## Proactive Triggers

Flag these without being asked:

- **Both characters under ten words per exchange** -- likely register collapse, check the specs
- **No apology-as-greeting from Ash in a Haran scene** -- recovery environment failure
- **Ash accepts a compliment cleanly** -- spec violation (he deflects or is embarrassed)
- **Ash states a political or emotional opinion in one clean sentence** -- should arrive via loop and hedge
- **Ash says "I know" to a Haran correction** -- Haran's register, not Ash's

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Full asymmetry fix | Numbered fix list, every flagged line with Find/Replace |
| Diagnostic check | Three-exchange ratio analysis, pass/fail verdict |
| Recovery check | Scene-by-scene assessment of chatter-armor recovery |
| After fixes applied | Verification scan: three test exchanges confirming asymmetry is restored |

## Related Skills

- **voice-ash agent** (`agents/voice-ash.md`): Use for single-character Ash audit in isolation. This skill adds the relational/asymmetry layer on top.
- **voice-haran agent** (`agents/voice-haran.md`): Use for Haran audit in isolation. This skill handles the pair together.
- **Voice Editor** (`agents/voice-editor.md`): Use for general style-guide compliance (em dashes, trailing reframes, POV). NOT for character voice register issues.
