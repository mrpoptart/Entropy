#!/usr/bin/env python3
"""
Generate a multi-view character model sheet from a source portrait, using
the OpenAI gpt-image-1 edits endpoint so the source image conditions the
result. The output sheet is the canonical visual reference for the
character and is fed back into every per-chunk scene generation.

Usage:
    python make-character-sheet.py \\
        --name ash \\
        --source ../reference/visual/ash-reference.png \\
        --out characters/ash-sheet.png

Reads the character's anchor line from audiobook/characters/<name>.md so
the textual description matches the project's locked descriptors.

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

ENDPOINT = "https://api.openai.com/v1/images/edits"
MODEL = "gpt-image-1"
SIZE = "1536x1024"  # widescreen sheet

HERE = Path(__file__).resolve().parent
CHAR_DIR = HERE / "characters"


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


def load_anchor(name: str) -> str:
    f = CHAR_DIR / f"{name}.md"
    if not f.exists():
        sys.exit(f"No character sheet at {f}")
    return extract_section(f.read_text(), "Anchor line")


def build_sheet_prompt(name: str, anchor: str) -> str:
    return (
        f"Character model sheet for {name}. Five panels arranged horizontally "
        f"on a clean off-white studio background, separated by thin vertical "
        f"lines. From left to right: (1) full-body front view, neutral stance, "
        f"arms relaxed at sides; (2) full-body three-quarter view turned to "
        f"the camera's right; (3) full-body side profile facing right; "
        f"(4) full-body back view; (5) head-and-shoulders close-up, front, "
        f"neutral expression. All five panels show the same person, same "
        f"face, same age, same clothes, same proportions. The face, build, "
        f"hair, skin, and clothing must match the supplied source image "
        f"exactly. The supplied source image is the canonical reference for "
        f"this character; do not invent new features. Consistent flat even "
        f"lighting across all panels. No text labels, no captions, no logos, "
        f"no watermarks. Naturalistic painterly illustration, muted earth-tone "
        f"palette.\n\n"
        f"Locked character descriptors (apply to every panel):\n{anchor}"
    )


def call_edits_api(prompt: str, source: Path, api_key: str, quality: str,
                   size: str) -> bytes:
    boundary = "----CharSheetBoundary7zX"
    parts: list[bytes] = []

    def add_field(name: str, value: str) -> None:
        parts.append(f"--{boundary}\r\n".encode())
        parts.append(
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode()
        )
        parts.append(value.encode("utf-8"))
        parts.append(b"\r\n")

    def add_file(name: str, path: Path) -> None:
        parts.append(f"--{boundary}\r\n".encode())
        parts.append(
            f'Content-Disposition: form-data; name="{name}"; '
            f'filename="{path.name}"\r\n'.encode()
        )
        parts.append(b"Content-Type: image/png\r\n\r\n")
        parts.append(path.read_bytes())
        parts.append(b"\r\n")

    add_field("model", MODEL)
    add_field("prompt", prompt)
    add_field("size", size)
    add_field("quality", quality)
    add_field("n", "1")
    add_file("image", source)
    parts.append(f"--{boundary}--\r\n".encode())

    body = b"".join(parts)
    req = urlrequest.Request(
        ENDPOINT,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urlrequest.urlopen(req, timeout=600) as resp:
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
    ap.add_argument("--name", required=True, help="Character name (e.g. ash)")
    ap.add_argument("--source", required=True, help="Source portrait PNG")
    ap.add_argument("--out", required=True, help="Output sheet PNG path")
    ap.add_argument("--quality", default="high",
                    choices=["low", "medium", "high"])
    ap.add_argument("--size", default=SIZE)
    ap.add_argument("--api-key")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    anchor = load_anchor(args.name)
    prompt = build_sheet_prompt(args.name, anchor)

    if args.dry_run:
        print(prompt)
        return

    source = Path(args.source)
    if not source.exists():
        sys.exit(f"Source not found: {source}")

    key = load_key(args.api_key)
    print(f"Generating {args.name} sheet (quality={args.quality}, size={args.size})...")
    png = call_edits_api(prompt, source, key, args.quality, args.size)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(png)
    print(f"Wrote {out} ({len(png):,} bytes)")


if __name__ == "__main__":
    main()
