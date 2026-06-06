#!/usr/bin/env python3
"""
End-to-end audiobook video builder for Chapter One.

Subcommands:
  sheets    Generate multi-view character sheets for non-Ash characters
            (text-to-image via gpt-image-1 generations endpoint).
            Ash's sheet already exists at characters/ash-sheet.png.
  shotlist  Print the per-chunk shotlist (debug).
  chunks    Generate one image per audiobook chunk using gpt-image-1
            edits endpoint (conditioned on the primary character's sheet)
            or generations endpoint for environment-only chunks.
            Idempotent: skips chunks whose .png already exists.
  video     ffmpeg-assemble the chapter video with Ken Burns motion.

Run order:
    python build_video.py sheets
    python build_video.py chunks
    python build_video.py video

API key resolution: OPENAI_API_KEY env, then audiobook/.openai-key.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError

HERE = Path(__file__).resolve().parent
CHAR_DIR = HERE / "characters"
CHUNK_DIR = HERE / "out" / "chapter-01"
IMG_DIR = CHUNK_DIR / "images"
VIDEO_DIR = CHUNK_DIR / "video"
FINAL = CHUNK_DIR / "chapter-01.mp4"

GEN_ENDPOINT = "https://api.openai.com/v1/images/generations"
EDIT_ENDPOINT = "https://api.openai.com/v1/images/edits"
MODEL = "gpt-image-1"
SIZE = "1536x1024"
QUALITY_SHEET = "high"
QUALITY_CHUNK = "medium"

# ---------------------------------------------------------------------------
# Character anchors
# ---------------------------------------------------------------------------

def load_key() -> str:
    env = os.environ.get("OPENAI_API_KEY")
    if env:
        return env
    keyfile = HERE / ".openai-key"
    if keyfile.exists():
        return keyfile.read_text().strip()
    sys.exit("No OpenAI key.")


def extract_section(md: str, header: str) -> str:
    out, inside = [], False
    for line in md.splitlines():
        if line.startswith("## "):
            if inside:
                break
            inside = header.lower() in line.lower()
            continue
        if inside:
            out.append(line)
    return "\n".join(out).strip().replace("> ", "").replace(">", "").strip()


def load_anchor(name: str) -> str:
    return extract_section((CHAR_DIR / f"{name}.md").read_text(), "Anchor line")


# ---------------------------------------------------------------------------
# Style + locations
# ---------------------------------------------------------------------------

STYLE = (
    "Naturalistic painterly illustration in the style of a grounded fantasy "
    "graphic novel: warm earth-tone palette, muted color, soft directional "
    "lighting, visible brushwork, no text or captions, no logos or watermarks, "
    "no glowing magical effects unless explicitly described, restrained "
    "composition. Cinematic 16:9 widescreen framing. The world is Solathis, "
    "a vertical stone city on a high plateau, architecture of carved pale "
    "stone and dark timber, with subtle channeled-magic infrastructure "
    "(small pale stone interface ovals set into walls and stoves)."
)

LOCATIONS = {
    "home_bedroom": "Ash's small spare bedroom in a working-class Solathis "
        "apartment: bare pale-stone walls, a narrow rope-strung bed, a small "
        "square window, a wooden floor with a worn rug, predawn gray light.",
    "home_washroom": "A cramped washroom with a stone basin, a small heating-"
        "lattice oval set into the wall, a polished brass tap, a rough towel "
        "on a hook, cold morning light through a single small window.",
    "home_kitchen": "A small warm kitchen in a Solathis apartment: a black "
        "iron stove with a pale stone channeling interface disc on its side, "
        "a wooden table with two chairs, copper kettle, wooden shelves with "
        "earthenware crockery, a single window letting in grayblue dawn.",
    "home_street": "A narrow lower-middle-district street in Solathis at "
        "early dawn: pale carved stone buildings stepping down a plateau, "
        "fine cracks visible in the facades, autumn leaves on the cobbles, "
        "cold air, the gleaming elder districts visible far above on the heights.",
    "stairs": "A long flight of pale stone public stairs climbing along the "
        "side of a vertical city, terraced railings, autumn light, occasional "
        "transit lift platforms visible in their shafts.",
    "stairs_alcove": "A small alcove cut into a stone stairwell, a stone "
        "bench set into the wall, dim grayblue light, completely empty of "
        "other people.",
    "market": "The Solathis market terrace at mid-morning: open wooden "
        "stalls, jars of spice and sacks of grain, channeled display stones "
        "glowing faintly, a small crowd of shoppers in autumn cloaks moving "
        "between stalls, banners overhead, ozone-tinted air.",
    "spice_stall": "A spice vendor's wooden stall with glass-fronted display "
        "cases sealed with pale stone channeling locks, jars of saffron and "
        "dried herbs, paper envelopes for measured spice, the middle-aged "
        "woman vendor behind the stall in a brown apron.",
    "annex_hall": "A high-ceilinged hall of pale carved stone in the Council "
        "annex of Solathis: tall arched windows, polished stone floor, "
        "subtle channeled lattices humming faintly in the walls, a wooden "
        "posting board on one wall covered in printed notices.",
    "annex_lift": "A round stone transit lift platform set into a tall shaft "
        "in the Council annex, a pale stone interface stone on a low pedestal "
        "beside it.",
    "annex_ramp": "A long gently curving ramp inside the Council annex with "
        "tall arched windows along the outer wall looking out over the city "
        "of Solathis, morning light pouring in.",
    "infra_office": "The doorway of the Infrastructure office at the top of "
        "the ramp, double doors open, the sound and sight of a busy office "
        "behind: desks, maps, surveys, staff moving.",
    "home_window": "The view from a window inside the Solathis apartment "
        "looking out at the dark vertical city at night: terraced districts "
        "stepping down the plateau, the elder heights still glowing faintly "
        "with channeled warmth, lower districts already dark.",
}

# ---------------------------------------------------------------------------
# Shotlist for Chapter 1 (36 chunks)
# Each entry: id, chars (list, [] for env-only), location key, moment text.
# ---------------------------------------------------------------------------

SHOTS = [
    # Scene 1: home before dawn
    {"id": "scene-1-chunk-01", "chars": ["ash"], "loc": "home_bedroom",
     "moment": "Young man Ash sitting on the edge of a narrow bed in a small cold predawn bedroom, blankets pushed back, bare feet on a wooden floor, head slightly turned listening to the silent house, expression tired but composed, no light source but a pale gray window."},
    {"id": "scene-1-chunk-02", "chars": ["ash"], "loc": "home_washroom",
     "moment": "Ash standing at a stone washbasin washing his face with cold water from a brass tap, sleeves pushed up, shirt half open at the collar, a small pale stone heating-lattice oval visible beside the tap but unused. Cold morning light from a small window. His expression is matter-of-fact, not flinching."},
    {"id": "scene-1-chunk-03", "chars": ["ash"], "loc": "home_kitchen",
     "moment": "Ash crouched in front of an open black iron stove striking flint and steel, a small bright spark caught in the kindling, his hands clearly calloused and capable, the kitchen still dim around him, copper kettle on the counter."},
    {"id": "scene-1-chunk-04", "chars": ["ash", "father"], "loc": "home_kitchen",
     "moment": "Ash and his father Rendell sitting at a small wooden kitchen table at dawn, two clay cups of tea between them, a pot of porridge on the stove behind, the father broad-shouldered with iron-gray hair and a short trimmed gray beard wrapping both thick calloused hands around the cup, Ash across from him in his worn layers. Warm low light. Both quiet, comfortable."},
    {"id": "scene-1-chunk-05", "chars": ["ash", "father"], "loc": "home_kitchen",
     "moment": "Close two-shot at the same kitchen table: the father's eyes lifted from the cup, looking at Ash with quiet attention, Ash in mid-sentence, hand half-raised in a small gesture, his face open and slightly hopeful. The pot of porridge gently steaming. Warm dawn light."},
    {"id": "scene-1-chunk-06", "chars": ["ash", "father"], "loc": "home_kitchen",
     "moment": "Father and Ash eating porridge in companionable silence at the wooden kitchen table, bowls steaming, the father holding his cup of tea, the smallest possible upward tug at one corner of his mouth, Ash mid-bite. The kitchen now full of warm morning light."},

    # Scene 2: market run
    {"id": "scene-2-chunk-01", "chars": ["ash"], "loc": "home_street",
     "moment": "Ash stepping out the front door of a stone apartment building onto a narrow lower-middle-district street, collar pulled up against the cold, breath visible in the air, looking up toward the gleaming polished elder districts above on the heights. His expression composed, eyes catching the height of the city."},
    {"id": "scene-2-chunk-02", "chars": ["ash"], "loc": "home_street",
     "moment": "Ash walking past a transit lift station at the end of a stone street, the lift platform visible in its shaft, an older woman pressing her palm to the interface stone to ride up. Ash walking past it without slowing, hands in his coat pockets, his eyes on the next street. A blanket hangs over a window across the way where a sealing lattice has failed; fine cracks crawl up a nearby wall."},
    {"id": "scene-2-chunk-03", "chars": ["ash"], "loc": "stairs",
     "moment": "Ash mid-climb on a long flight of pale stone public stairs that climb the side of a vertical city, autumn light catching his face, his breathing controlled, his face carefully composed. Other channelers visible on the parallel transit lift in the distance, riding up effortlessly. Ash takes the stairs."},
    {"id": "scene-2-chunk-04", "chars": ["ash"], "loc": "market",
     "moment": "Ash walking through the Solathis market terrace at mid-morning, ozone-tinted air, vendors activating display stones with casual palm-touches as he passes. A woman crosses a narrow bridge toward him, her palm trailing along the railing leaving a faint warmth in the stone. Ash steps aside to let her pass. His expression neutral, eyes lowered slightly."},
    {"id": "scene-2-chunk-05", "chars": ["ash"], "loc": "spice_stall",
     "moment": "Ash at a spice vendor's stall, a middle-aged woman in a brown apron sliding a small paper envelope of saffron threads across the counter to him. Glass-fronted display cases sealed with channeled locks behind her. Ash counting coins onto the wooden counter, his calloused hand visible. Naturalistic morning light."},
    {"id": "scene-2-chunk-06", "chars": ["ash"], "loc": "market",
     "moment": "Ash pocketing the saffron envelope and walking on through the market, a small loose bundle of other purchases (flour sack, salt twist, wicking cord) under his arm. The vendor already serving the next customer behind him. Ash's expression unreadable, the city pressing on around him."},

    # Scene 3: the alcove
    {"id": "scene-3-chunk-01", "chars": ["ash"], "loc": "stairs_alcove",
     "moment": "Ash sitting alone on a stone bench in a small alcove cut into a stone stairwell, leaning back against the cold wall with his eyes closed, his face for the first time without the public smile, slacker and older, the carefully maintained performance entirely released. Dim grayblue light. Empty otherwise."},
    {"id": "scene-3-chunk-02", "chars": ["ash"], "loc": "stairs_alcove",
     "moment": "Same alcove. Ash sitting forward now, elbows on knees, looking down at his own broad calloused open hands, examining them with quiet interest. His expression tired but clear-eyed. A single beat of stillness before he stands."},

    # Scene 4: the annex and Dorenne
    {"id": "scene-4-chunk-01", "chars": ["ash"], "loc": "annex_hall",
     "moment": "Ash standing in front of a wooden posting board in the high-ceilinged stone hall of the Council annex, reading a notice, a small notebook open in his hand, a worn pencil tucked behind his ear. The notice headed POOL ASSESSMENT REQUIRED visible at the top. Pale light from tall arched windows. Other passersby moving in soft focus."},
    {"id": "scene-4-chunk-02", "chars": ["ash", "dorenne"], "loc": "annex_lift",
     "moment": "Ash turning from the posting board to face Dorenne Kharren, a sharp-faced woman of about sixty in a dark charcoal Council half-cloak with the Infrastructure seal at the collar, iron-gray hair pulled back severely. She is half a step toward a round stone lift platform, her hand on its interface stone, two younger staff a respectful distance behind her. Her sharp gray eyes already on Ash."},
    {"id": "scene-4-chunk-03", "chars": ["ash", "dorenne"], "loc": "annex_lift",
     "moment": "Dorenne standing on the lift platform with her hand on the interface stone, paused, looking down at Ash who stands at the platform's edge, his face caught mid-confession, openly embarrassed but light. Her expression neither pitying nor cold, just calibrating. Her two staff behind her exchanging a quick involuntary glance."},
    {"id": "scene-4-chunk-04", "chars": ["ash", "dorenne"], "loc": "annex_lift",
     "moment": "Dorenne stepped down from the lift platform, now standing face-to-face with Ash in the hall, her sharp gray eyes locked on him with the focused attention of a problem-solver. Ash on the receiving end, half-smiling apologetically, hand at the back of his neck. Her two staff behind her, recalculating."},
    {"id": "scene-4-chunk-05", "chars": ["ash", "dorenne"], "loc": "annex_ramp",
     "moment": "Dorenne and Ash now walking together along a long curving stone ramp inside the Council annex, tall arched windows on their left letting in morning light, the city of Solathis visible far below. Her two staff trailing a few paces behind. Dorenne's stride measured, Ash falling into step beside her, his expression careful."},
    {"id": "scene-4-chunk-06", "chars": ["ash", "dorenne"], "loc": "annex_ramp",
     "moment": "Same ramp, mid-walk. Ash mid-sentence, gesturing with one open hand, looking sideways at Dorenne. Her face turned partly toward him, listening hard, the small dry tug at one corner of her mouth that is the closest she comes to amusement."},
    {"id": "scene-4-chunk-07", "chars": ["ash", "dorenne"], "loc": "annex_ramp",
     "moment": "Same ramp, both Ash and Dorenne stopped at one of the tall windows, the morning light pouring in, the city spread below them in autumn light: grand districts above gleaming, lower districts fraying, the channeled infrastructure thinning. Dorenne looking out at it, Ash beside her, both quiet."},
    {"id": "scene-4-chunk-08", "chars": ["ash", "dorenne"], "loc": "annex_ramp",
     "moment": "Dorenne stopped and turned to face Ash directly at the top of the ramp, the open doors of the Infrastructure office visible behind her at the end of the hall. Her expression direct, even severe. Ash listening, his easy posture stilled, attention focused."},
    {"id": "scene-4-chunk-09", "chars": ["ash", "dorenne"], "loc": "infra_office",
     "moment": "Dorenne and Ash at the threshold of the Infrastructure office, her hand extended palm-up in the Solathis gesture of an offered agreement. Ash's hand meeting hers, palm to palm, just the pressure of skin on skin. No channeling glow. Her staff watching, restrained. The office bustles behind."},

    # Scene 5: rushing home with the news
    {"id": "scene-5-chunk-01", "chars": ["ash"], "loc": "stairs",
     "moment": "Ash hurrying down the long flight of pale stone public stairs, almost jogging, face bright with controlled excitement, the city of Solathis at midday around him. Other people passing in the other direction, paying him no attention."},
    {"id": "scene-5-chunk-02", "chars": ["ash", "mother"], "loc": "home_kitchen",
     "moment": "Ash through the apartment doorway with too much momentum, the door handle banging the wall. His mother Leska in the kitchen mid-task, a small wiry woman in her early fifties with dark-brown hair streaked with gray pulled back in a knot, a stained kitchen apron over a dark-blue work dress, looking up startled, a wooden spoon in one hand. Ash in mid-blurt, face open and raw."},
    {"id": "scene-5-chunk-03", "chars": ["ash", "mother"], "loc": "home_kitchen",
     "moment": "Leska standing at a small wooden shelf in the kitchen, her palm pressed to a small pale resonance stone the size of her palm, a faint warm light at her fingertips, her face composed but eyes wet. Ash a step behind her, watching her channel, his expression tender."},
    {"id": "scene-5-chunk-04", "chars": ["ash", "mother"], "loc": "home_kitchen",
     "moment": "Ash and Leska now sitting across from each other at the kitchen table, Ash flushed and slightly winded, his hands wrapped around a steaming clay cup, Leska across from him with a paper envelope of saffron in her hand. The kitchen warm and bright with mid-morning light. Both quiet, both smiling."},

    # Scene 6: family celebration
    {"id": "scene-6-chunk-01", "chars": ["ash", "father"], "loc": "home_kitchen",
     "moment": "The father Rendell at the kitchen doorway with sawdust still in his iron-gray hair, his coat already hung on a hook behind him, his hand gripping Ash's shoulder firmly, his other hand still wet from washing at the basin. Ash facing him, looking up slightly. The kitchen behind set with the good plates and the smell of saffron rice."},
    {"id": "scene-6-chunk-02", "chars": ["ash", "father", "mother"], "loc": "home_kitchen",
     "moment": "Family dinner at the small wooden kitchen table, the three of them: Leska in her dark-blue dress and apron lifting her clay cup of plum wine in a toast, Rendell with his cup raised slightly, Ash across with his own cup, the saffron rice and flatbread on the good plates between them. The stove behind them radiating excess warmth, a small celebration."},
    {"id": "scene-6-chunk-03", "chars": ["maren"], "loc": "home_kitchen",
     "moment": "The doorway of the apartment open, a gust of cold air visible, Maren just stepped through: twenty-one, slim and composed, light brown wavy hair cut jaw-length, fair freckled skin, sharp gray-green eyes, a fitted dark-charcoal surveyor's coat over a high-collared cream tunic, leather satchel slung across one shoulder, cheeks bright from the cold. She kissing her mother on the cheek in the kitchen behind."},
    {"id": "scene-6-chunk-04", "chars": ["ash", "maren"], "loc": "home_kitchen",
     "moment": "Maren turned to face Ash across the kitchen, her face breaking into a real warm smile that reaches her eyes, her satchel still on her shoulder. Ash facing her, his own smile open. Mother and father visible behind in soft focus at the table."},
    {"id": "scene-6-chunk-05", "chars": ["ash", "maren"], "loc": "home_kitchen",
     "moment": "Maren leaning forward at the kitchen table, her left palm flat on a chipped teacup with a faint warm pulse at her fingertip sealing the hairline crack, her right hand gesturing as she asks Ash a sharp question. Ash across from her mid-answer. Plum wine cups, half-empty plates."},
    {"id": "scene-6-chunk-06", "chars": ["ash", "father", "mother", "maren"], "loc": "home_kitchen",
     "moment": "All four at the kitchen table looking at Maren as she speaks lightly, deliberately downplaying her news, her cup half-raised in a small toast. Her face composed, smiling, the smile careful. Mother's hand on hers across the table. Father quiet, listening. Ash watching."},
    {"id": "scene-6-chunk-07", "chars": ["maren"], "loc": "home_kitchen",
     "moment": "Maren alone in the kitchen frame, her palm flat against the pale stone heating-lattice on the wall, a faint warm pulse of channeling visible at her fingertips, her face composed and very still. The rest of the family blurred and small at the table behind her, in mid-conversation about Ash. Maren's expression giving nothing away."},
    {"id": "scene-6-chunk-08", "chars": ["ash"], "loc": "home_window",
     "moment": "Ash standing alone at a window inside the dim apartment at night, his forehead nearly to the cold glass, looking out at the dark vertical city of Solathis, its districts visible as bands of fading warmth in the stone: bright at the elder heights, dimmer in the middle, dark below. His reflection faint in the glass."},
    {"id": "scene-6-chunk-09", "chars": ["ash"], "loc": "home_bedroom",
     "moment": "Ash now lying in his narrow bed in his small bedroom in the dark, on his back, eyes open, faint moonlight through the small window. His expression open and unguarded, tired but quiet. Not asleep yet. Just lying there in the dark."},
]

assert len(SHOTS) == 36, f"expected 36 shots, got {len(SHOTS)}"

# Which character to use as the conditioning image for the edits endpoint.
# When multiple characters present, the primary is the one whose sheet most
# defines the framing. Ash by default whenever present.
def primary_char(chars: list[str]) -> str | None:
    if not chars:
        return None
    if "ash" in chars:
        return "ash"
    return chars[0]

# ---------------------------------------------------------------------------
# OpenAI API helpers
# ---------------------------------------------------------------------------

def http_post(url: str, body: bytes, headers: dict, timeout: int = 600) -> dict:
    req = urlrequest.Request(url, data=body, headers=headers, method="POST")
    for attempt in range(3):
        try:
            with urlrequest.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read())
        except HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            sys.stderr.write(f"HTTP {e.code} (attempt {attempt+1}): {msg[:300]}\n")
            if e.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def call_generations(prompt: str, key: str, quality: str) -> bytes:
    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "size": SIZE,
        "quality": quality,
        "n": 1,
    }).encode()
    obj = http_post(
        GEN_ENDPOINT, payload,
        {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    return base64.b64decode(obj["data"][0]["b64_json"])


def call_edits(prompt: str, source: Path, key: str, quality: str) -> bytes:
    boundary = "----EntropyBoundary7zX"
    parts: list[bytes] = []
    def add_field(name: str, value: str) -> None:
        parts.extend([
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
            value.encode("utf-8"),
            b"\r\n",
        ])
    def add_file(name: str, path: Path) -> None:
        parts.extend([
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{name}"; filename="{path.name}"\r\n'.encode(),
            b"Content-Type: image/png\r\n\r\n",
            path.read_bytes(),
            b"\r\n",
        ])
    add_field("model", MODEL)
    add_field("prompt", prompt)
    add_field("size", SIZE)
    add_field("quality", quality)
    add_field("n", "1")
    add_file("image", source)
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)
    obj = http_post(
        EDIT_ENDPOINT, body,
        {"Content-Type": f"multipart/form-data; boundary={boundary}",
         "Authorization": f"Bearer {key}"},
    )
    return base64.b64decode(obj["data"][0]["b64_json"])


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_sheets(args) -> None:
    key = load_key()
    targets = ["father", "mother", "maren", "dorenne"]
    for name in targets:
        out = CHAR_DIR / f"{name}-sheet.png"
        if out.exists() and not args.force:
            print(f"[skip] {name}-sheet.png exists")
            continue
        anchor = load_anchor(name)
        prompt = (
            f"Character model sheet for {name}. Five full-body panels arranged "
            f"horizontally on a clean off-white studio background separated by "
            f"thin vertical lines: (1) front view, neutral stance, arms at "
            f"sides; (2) three-quarter view turned to the camera's right; "
            f"(3) side profile facing right; (4) back view; (5) a head and "
            f"shoulders close-up at the right. All five panels show the same "
            f"person, same face, same hair, same clothing, same age, same "
            f"proportions. Flat even studio lighting. No text labels, no "
            f"captions, no logos, no watermarks. Naturalistic painterly "
            f"illustration, muted earth-tone palette.\n\n"
            f"Locked character descriptors (apply to every panel):\n{anchor}"
        )
        print(f"[gen] {name}-sheet.png ({QUALITY_SHEET})")
        png = call_generations(prompt, key, QUALITY_SHEET)
        out.write_bytes(png)
        print(f"      wrote {out} ({len(png):,} bytes)")


def build_chunk_prompt(shot: dict) -> str:
    chars_part = ""
    if shot["chars"]:
        anchors = [f"- {load_anchor(c)}" for c in shot["chars"]]
        chars_part = "\nCHARACTERS PRESENT (render with these exact features):\n" + "\n".join(anchors) + "\n"
    loc = LOCATIONS[shot["loc"]]
    return (
        f"STYLE: {STYLE}\n"
        f"LOCATION: {loc}\n"
        f"{chars_part}"
        f"SCENE: {shot['moment']}\n"
        f"COMPOSITION: Single still illustration, cinematic 16:9 widescreen, "
        f"medium-wide shot framing characters within their environment when "
        f"characters are present, otherwise an establishing environment shot. "
        f"No text, no captions, no labels, no logos, no watermarks. Same "
        f"painterly style across every image in this series."
    )


def cmd_chunks(args) -> None:
    key = load_key()
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    shots = SHOTS
    if args.only:
        wanted = set(args.only.split(","))
        shots = [s for s in SHOTS if s["id"] in wanted]
    for shot in shots:
        out = IMG_DIR / f"{shot['id']}.png"
        if out.exists() and not args.force:
            print(f"[skip] {shot['id']}.png exists")
            continue
        prompt = build_chunk_prompt(shot)
        prim = primary_char(shot["chars"])
        try:
            if prim:
                sheet = CHAR_DIR / f"{prim}-sheet.png"
                if not sheet.exists():
                    print(f"[err]  {prim}-sheet.png missing; falling back to text-to-image for {shot['id']}")
                    png = call_generations(prompt, key, QUALITY_CHUNK)
                else:
                    print(f"[gen] {shot['id']}.png (edit, primary={prim})")
                    png = call_edits(prompt, sheet, key, QUALITY_CHUNK)
            else:
                print(f"[gen] {shot['id']}.png (text-to-image, env-only)")
                png = call_generations(prompt, key, QUALITY_CHUNK)
            out.write_bytes(png)
            print(f"      wrote {out} ({len(png):,} bytes)")
        except Exception as e:
            sys.stderr.write(f"[fail] {shot['id']}: {e}\n")


def ffprobe_duration(wav: Path) -> float:
    res = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(wav)],
        check=True, capture_output=True, text=True,
    )
    return float(res.stdout.strip())


def render_segment(image: Path, wav: Path, dur: float, out: Path) -> None:
    fps = 30
    frames = max(1, int(round(dur * fps)))
    # Slow Ken Burns: zoom 1.0 -> 1.10 over the chunk, drifting toward center.
    vf = (
        f"scale=3072:2048:flags=lanczos,"
        f"zoompan=z='min(1.0+on*({0.10}/{frames}),1.10)':"
        f"d={frames}:"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"s=1920x1080:fps={fps},"
        f"format=yuv420p"
    )
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(fps), "-t", f"{dur:.3f}", "-i", str(image),
        "-i", str(wav),
        "-filter_complex", f"[0:v]{vf}[v]",
        "-map", "[v]", "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def cmd_video(args) -> None:
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    seg_paths: list[Path] = []
    for shot in SHOTS:
        wav = CHUNK_DIR / f"{shot['id']}.wav"
        img = IMG_DIR / f"{shot['id']}.png"
        seg = VIDEO_DIR / f"{shot['id']}.mp4"
        if not wav.exists():
            sys.exit(f"missing audio: {wav}")
        if not img.exists():
            sys.exit(f"missing image: {img}")
        if seg.exists() and not args.force:
            print(f"[skip] {seg.name} exists")
        else:
            dur = ffprobe_duration(wav)
            print(f"[seg]  {shot['id']} ({dur:.1f}s)")
            render_segment(img, wav, dur, seg)
        seg_paths.append(seg)

    concat_list = VIDEO_DIR / "concat.txt"
    concat_list.write_text("".join(f"file '{p}'\n" for p in seg_paths))
    print(f"[mux]  {FINAL}")
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c", "copy", str(FINAL),
    ], check=True)
    print(f"done: {FINAL}")


def cmd_shotlist(args) -> None:
    for s in SHOTS:
        print(f"{s['id']:24}  chars={','.join(s['chars']) or '-':25}  loc={s['loc']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sheets"); s.add_argument("--force", action="store_true"); s.set_defaults(func=cmd_sheets)
    s = sub.add_parser("chunks"); s.add_argument("--force", action="store_true"); s.add_argument("--only", help="comma-separated chunk ids"); s.set_defaults(func=cmd_chunks)
    s = sub.add_parser("video"); s.add_argument("--force", action="store_true"); s.set_defaults(func=cmd_video)
    s = sub.add_parser("shotlist"); s.set_defaults(func=cmd_shotlist)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
