#!/usr/bin/env python3
"""
Gemini TTS driver for the Entropy audiobook.

Uses the Gemini API (generativelanguage.googleapis.com), which accepts the
AI-Studio-style API keys (AQ.Ab8R...). The Cloud TTS REST endpoint does NOT
accept these keys (OAuth only), so we use the Gemini surface instead.

Usage:
    python tts.py examples/01-narrator-sentence.txt
    python tts.py examples/04-multi-voice-scene.txt -o out/scene.wav
    echo "Hello." | python tts.py - --voice Aoede --style "warm, calm"

Input file format (frontmatter optional):

    ---
    style: warm, calm narrator; audiobook opening
    voice: Aoede                       # single-voice
    # --- OR for multi-voice: ---
    speakers:
      Narrator: Aoede
      Ash: Puck
      Father: Charon
    ---
    Body text. For multi-voice, every line is "Speaker: text".

API key lookup: --api-key flag, GEMINI_TTS_API_KEY env, then audiobook/.key
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import wave
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError

MODEL = "gemini-2.5-flash-preview-tts"  # AI-Studio-accessible TTS preview
ENDPOINT_TMPL = (
    "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
)
DEFAULT_VOICE = "Aoede"

HERE = Path(__file__).resolve().parent


def load_key(cli_key: str | None) -> str:
    if cli_key:
        return cli_key
    env = os.environ.get("GEMINI_TTS_API_KEY")
    if env:
        return env
    keyfile = HERE / ".key"
    if keyfile.exists():
        return keyfile.read_text().strip()
    sys.exit("No API key. Set GEMINI_TTS_API_KEY, write audiobook/.key, or pass --api-key.")


def parse_input(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text.strip()
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text.strip()
    front_raw = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    current_key = None
    for line in front_raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            if current_key is None:
                continue
            k, _, v = line.strip().partition(":")
            meta.setdefault(current_key, {})[k.strip()] = v.strip()
        else:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if v == "":
                meta[k] = {}
                current_key = k
            else:
                meta[k] = v
                current_key = None
    return meta, body.strip()


def build_payload(meta: dict, body: str, style_override: str | None,
                  voice_override: str | None) -> dict:
    style = style_override or meta.get("style") or ""
    speakers = meta.get("speakers")

    if isinstance(speakers, dict) and speakers:
        speech_config = {
            "multiSpeakerVoiceConfig": {
                "speakerVoiceConfigs": [
                    {
                        "speaker": name,
                        "voiceConfig": {
                            "prebuiltVoiceConfig": {"voiceName": voice}
                        },
                    }
                    for name, voice in speakers.items()
                ]
            }
        }
        # Gemini multi-speaker prompt convention: prefix each line "Speaker: text".
        # Body already follows that shape, so pass it through verbatim.
        prompt_text = body
        if style:
            prompt_text = f"TTS the following conversation. Style: {style}\n\n{body}"
    else:
        voice = voice_override or meta.get("voice", DEFAULT_VOICE)
        speech_config = {
            "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}
        }
        prompt_text = body
        if style:
            prompt_text = f"Say the following in this style: {style}\n\n{body}"

    return {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": speech_config,
        },
    }


def synthesize(payload: dict, api_key: str, model: str = MODEL) -> tuple[bytes, str]:
    url = ENDPOINT_TMPL.format(model=model)
    data = json.dumps(payload).encode("utf-8")
    req = urlrequest.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urlrequest.urlopen(req) as resp:
            raw = resp.read()
    except HTTPError as e:
        sys.stderr.write(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')}\n")
        sys.exit(1)
    obj = json.loads(raw)
    try:
        part = obj["candidates"][0]["content"]["parts"][0]
        inline = part["inlineData"]
        return base64.b64decode(inline["data"]), inline.get("mimeType", "")
    except (KeyError, IndexError):
        sys.exit(f"Unexpected response shape: {json.dumps(obj)[:600]}")


def write_wav(audio: bytes, mime: str, out_path: Path) -> None:
    if audio[:4] == b"RIFF":
        out_path.write_bytes(audio)
        return
    # mimeType looks like "audio/L16;codec=pcm;rate=24000"
    rate = 24000
    m = re.search(r"rate=(\d+)", mime)
    if m:
        rate = int(m.group(1))
    with wave.open(str(out_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(audio)


def main() -> None:
    ap = argparse.ArgumentParser(description="Gemini TTS for Entropy audiobook")
    ap.add_argument("input", help="Input .txt path, or - for stdin")
    ap.add_argument("-o", "--out", help="Output .wav (default: out/<name>.wav)")
    ap.add_argument("--voice", help="Override single voice")
    ap.add_argument("--style", help="Override style prompt")
    ap.add_argument("--api-key", help="Override API key")
    ap.add_argument("--model", default=MODEL, help=f"Model (default {MODEL})")
    ap.add_argument("--speed", type=float, default=1.0,
                    help="Post-process tempo (1.0=as-rendered, 1.25=brisker, 1.5=fast). "
                         "Uses ffmpeg atempo, preserves pitch.")
    ap.add_argument("--dry-run", action="store_true", help="Print payload and exit")
    args = ap.parse_args()

    if args.input == "-":
        text = sys.stdin.read()
        stem = "stdin"
    else:
        p = Path(args.input)
        text = p.read_text()
        stem = p.stem

    meta, body = parse_input(text)
    if not body:
        sys.exit("Empty body.")
    payload = build_payload(meta, body, args.style, args.voice)

    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    api_key = load_key(args.api_key)
    audio, mime = synthesize(payload, api_key, args.model)

    out_path = Path(args.out) if args.out else HERE / "out" / f"{stem}.wav"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_wav(audio, mime, out_path)

    if args.speed != 1.0:
        if not shutil.which("ffmpeg"):
            sys.exit("--speed requires ffmpeg on PATH.")
        tmp = out_path.with_suffix(".raw.wav")
        out_path.rename(tmp)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp),
             "-filter:a", f"atempo={args.speed}", str(out_path)],
            check=True,
        )
        tmp.unlink()

    print(f"Wrote {out_path} (speed={args.speed})")


if __name__ == "__main__":
    main()
