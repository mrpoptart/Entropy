#!/usr/bin/env python3
"""
Render a graphic-novel illustration for one audio chunk of the audiobook.

Usage:
    # Render one chunk (chunk file matches an existing audio chunk .txt):
    python visualize.py out/chapter-01/scene-1-chunk-03.txt --chars ash father

    # Render a custom moment with explicit prompt fragment:
    python visualize.py --moment "Ash strikes flint and steel at the kitchen stove, three strikes, the spark caught" --chars ash --out images/chapter-01/test.png

    # Generate a character portrait sheet (no scene context):
    python visualize.py --portrait ash

API key resolution: --api-key, OPENAI_API_KEY env, then audiobook/.openai-key.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError

ENDPOINT = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
SIZE = "1536x1024"  # gpt-image-1's widescreen size (closest to 16:9)

HERE = Path(__file__).resolve().parent
CHAR_DIR = HERE / "characters"
STYLE_FILE = CHAR_DIR / "_style.md"


def load_key(cli_key: str | None) -> str:
    if cli_key:
        return cli_key
    env = os.environ.get("OPENAI_API_KEY")
    if env:
        return env
    keyfile = HERE / ".openai-key"
    if keyfile.exists():
        return keyfile.read_text().strip()
    sys.exit("No OpenAI key. Set OPENAI_API_KEY, write audiobook/.openai-key, or pass --api-key.")


def extract_section(md: str, header: str) -> str:
    """Pull the body of a '## Anchor line ...' block out of a character sheet."""
    lines = md.splitlines()
    out: list[str] = []
    inside = False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = header.lower() in line.lower()
            continue
        if inside:
            out.append(line)
    text = "\n".join(out).strip()
    text = text.replace("> ", "").replace(">", "").strip()
    return text


def load_character(name: str) -> dict:
    f = CHAR_DIR / f"{name}.md"
    if not f.exists():
        sys.exit(f"No character sheet at {f}")
    md = f.read_text()
    return {
        "name": name,
        "anchor": extract_section(md, "Anchor line"),
        "negative": extract_section(md, "Negative prompt"),
        "art_direction": extract_section(md, "Art direction"),
    }


def load_style() -> str:
    if not STYLE_FILE.exists():
        return ""
    md = STYLE_FILE.read_text()
    return extract_section(md, "Style anchor")


def build_prompt(moment: str, character_names: list[str],
                 composition: str | None) -> tuple[str, str]:
    style = load_style()
    chars = [load_character(n) for n in character_names]

    parts: list[str] = []
    parts.append(f"STYLE: {style}")
    if chars:
        parts.append("CHARACTERS PRESENT (render with these exact features):")
        for c in chars:
            parts.append(f"- {c['anchor']}")
    parts.append(f"SCENE: {moment.strip()}")
    if composition:
        parts.append(f"COMPOSITION: {composition.strip()}")

    art_directions = [c["art_direction"] for c in chars if c.get("art_direction")]
    if art_directions:
        parts.append("ART DIRECTION: " + " ".join(art_directions))

    negatives: list[str] = []
    for c in chars:
        if c["negative"]:
            negatives.append(c["negative"])
    if negatives:
        parts.append("AVOID: " + " ".join(negatives))

    prompt = "\n\n".join(parts)
    return prompt, style


def extract_moment_from_chunk(chunk_text: str, max_chars: int = 600) -> str:
    """Heuristic: take the first 600 chars of narrative content as the moment.
    Strip TTS frontmatter and bracketed cues so the image prompt is clean."""
    body = chunk_text
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end != -1:
            body = body[end + 4 :].lstrip("\n")
    import re
    body = re.sub(r"\[[^\]]+\]\s*", "", body)
    body = body.strip()
    return body[:max_chars]


def call_image_api(prompt: str, api_key: str, quality: str) -> bytes:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "size": SIZE,
        "quality": quality,
        "n": 1,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urlrequest.Request(
        ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urlrequest.urlopen(req, timeout=300) as resp:
            obj = json.loads(resp.read())
    except HTTPError as e:
        sys.stderr.write(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')}\n")
        sys.exit(1)
    try:
        b64 = obj["data"][0]["b64_json"]
    except (KeyError, IndexError):
        sys.exit(f"Unexpected response: {json.dumps(obj)[:600]}")
    return base64.b64decode(b64)


def main() -> None:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("chunk", nargs="?", help="Path to an audio chunk .txt to illustrate")
    src.add_argument("--moment", help="Free-text scene moment to illustrate")
    src.add_argument("--portrait", help="Character name for a standalone portrait")
    ap.add_argument("--chars", nargs="*", default=[], help="Characters in the scene")
    ap.add_argument("--composition", help="Optional composition hint")
    ap.add_argument("--out", help="Output PNG path (default: alongside chunk)")
    ap.add_argument("--quality", default="medium",
                    choices=["low", "medium", "high"],
                    help="gpt-image-1 quality (default medium ~$0.04, high ~$0.17)")
    ap.add_argument("--api-key", help="Override OpenAI key")
    ap.add_argument("--raw-prompt-file", help="Send the contents of this file as the entire prompt, verbatim, with no STYLE/CHARACTERS/AVOID wrapping")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print the prompt and exit without calling the API")
    args = ap.parse_args()

    if args.portrait:
        char = load_character(args.portrait)
        moment = (f"Single-character portrait of {args.portrait}, three-quarter view, "
                  f"neutral background, illustrative reference sheet pose.")
        chars = [args.portrait]
        default_out = HERE / "characters" / f"{args.portrait}-portrait.png"
    elif args.chunk:
        chunk_path = Path(args.chunk)
        moment = extract_moment_from_chunk(chunk_path.read_text())
        chars = args.chars
        default_out = chunk_path.with_suffix(".png")
    else:
        moment = args.moment
        chars = args.chars
        default_out = HERE / "images" / "ad-hoc.png"

    if args.raw_prompt_file:
        prompt = Path(args.raw_prompt_file).read_text().strip()
    else:
        prompt, _ = build_prompt(moment, chars, args.composition)

    if args.dry_run:
        print(prompt)
        return

    api_key = load_key(args.api_key)
    print(f"Generating ({len(prompt)} char prompt, quality={args.quality})...")
    png = call_image_api(prompt, api_key, args.quality)

    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(png)
    print(f"Wrote {out_path} ({len(png):,} bytes)")


if __name__ == "__main__":
    main()
