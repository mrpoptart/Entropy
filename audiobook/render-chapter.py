#!/usr/bin/env python3
"""
Render a chapter-length annotated file by splitting on '* * *' scene breaks,
calling tts.py for each scene, then concatenating with ffmpeg.

Usage:
    python render-chapter.py chapters/chapter-01.annotated.txt
    python render-chapter.py chapters/chapter-01.annotated.txt --skip-existing

Outputs:
    out/chapter-01/scene-1.wav, scene-2.wav, ...   (intermediates)
    out/chapter-01.wav                              (concatenated final)
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TTS = HERE / "tts.py"


def split_scenes(text: str) -> tuple[str, list[str]]:
    """Split out the frontmatter and the per-scene bodies."""
    if not text.startswith("---"):
        sys.exit("Annotated chapter must start with a --- frontmatter block.")
    end = text.find("\n---", 3)
    if end == -1:
        sys.exit("Unterminated frontmatter.")
    frontmatter = text[: end + 4]
    body = text[end + 4 :].lstrip("\n")

    scenes = [s.strip() for s in body.split("\n* * *\n") if s.strip()]
    return frontmatter, scenes


def chunk_scene(scene: str, max_chars: int) -> list[str]:
    """Group paragraphs into chunks <= max_chars, never splitting a paragraph."""
    paragraphs = [p.strip() for p in scene.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for p in paragraphs:
        if current and len(current) + len(p) + 2 > max_chars:
            chunks.append(current)
            current = p
        else:
            current = f"{current}\n\n{p}" if current else p
    if current:
        chunks.append(current)
    return chunks


def render_scene(frontmatter: str, scene_body: str, out_wav: Path,
                 work_dir: Path) -> None:
    scene_file = work_dir / out_wav.with_suffix(".txt").name
    scene_file.write_text(f"{frontmatter}\n{scene_body}\n")
    subprocess.run(
        [sys.executable, str(TTS), str(scene_file), "-o", str(out_wav)],
        check=True,
    )


def concat_wavs(wavs: list[Path], out_path: Path) -> None:
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is required for concatenation.")
    listfile = out_path.with_suffix(".list")
    listfile.write_text("".join(f"file '{w.resolve()}'\n" for w in wavs))
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(listfile), "-c", "copy", str(out_path)],
        check=True,
    )
    listfile.unlink()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Annotated chapter .txt with '* * *' scene breaks")
    ap.add_argument("--skip-existing", action="store_true",
                    help="Skip chunks whose .wav already exists (for cheap reruns)")
    ap.add_argument("--max-chars", type=int, default=1500,
                    help="Max chars per TTS call. Smaller = more stable pacing, "
                         "more API calls. Default 1500.")
    args = ap.parse_args()

    in_path = Path(args.input)
    text = in_path.read_text()
    frontmatter, scenes = split_scenes(text)
    print(f"Found {len(scenes)} scenes.")

    stem = in_path.stem.replace(".annotated", "")
    chap_out = HERE / "out" / stem
    chap_out.mkdir(parents=True, exist_ok=True)

    wavs: list[Path] = []
    for si, scene in enumerate(scenes, 1):
        chunks = chunk_scene(scene, args.max_chars)
        print(f"  scene {si}: {len(chunks)} chunks ({len(scene)} chars)")
        for ci, chunk in enumerate(chunks, 1):
            wav = chap_out / f"scene-{si}-chunk-{ci:02d}.wav"
            if args.skip_existing and wav.exists():
                print(f"    chunk {ci}: skip (exists)")
            else:
                print(f"    chunk {ci}: rendering ({len(chunk)} chars)")
                render_scene(frontmatter, chunk, wav, chap_out)
            wavs.append(wav)

    final = HERE / "out" / f"{stem}.wav"
    concat_wavs(wavs, final)
    print(f"Wrote {final}")


if __name__ == "__main__":
    main()
