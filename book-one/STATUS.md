# Book One — Draft Status

All 22 chapters of Book One ("The Brightest Fire") were canonically locked on 2026-05-30 at commit `03ed856` ("Execute D1/D2/D3/D4 revision directives across Book One"), built atop commit `6b693fa` ("Add Dialogue Attribution Rule and apply attribution pass across Book One").

These commits represent the locked state of:
- Attribution pass across all 22 chapters (Dialogue Attribution Rule, including the four local checks).
- D1 (Maren superlatives) execution.
- D2 (Ash's persistent weaknesses) execution across ch02/06/11/17.
- D3 (parents' offstage normal-life beats, folded to Ash-perceived per project POV rule) across ch07/11/18.
- D4 (No Trailing-Reframe Rule) execution across ch07/11/15/16/17/19/20/21/22.
- 3c review remediation (ch06 post-failure cut, Leska evidence catalogue, Dorenne register fixes, Ash chatter-armor restored, ch07 in-text meta stripped, ch17 reservoir-edges pacing beat restored, etc.).

## Lock manifest

| Chapter | File | Locked-at commit | Lock date |
|---------|------|------------------|-----------|
| 01 | chapter-01.md | 03ed856 | 2026-05-30 |
| 02 | chapter-02.md | 03ed856 | 2026-05-30 |
| 03 | chapter-03.md | 6b693fa | 2026-05-30 |
| 04 | chapter-04.md | 6b693fa | 2026-05-30 |
| 05 | chapter-05.md | 6b693fa | 2026-05-30 |
| 06 | chapter-06.md | 03ed856 | 2026-05-30 |
| 07 | chapter-07.md | 03ed856 | 2026-05-30 |
| 08 | chapter-08.md | 6b693fa | 2026-05-30 |
| 09 | chapter-09.md | 6b693fa | 2026-05-30 |
| 10 | chapter-10.md | 6b693fa | 2026-05-30 |
| 11 | chapter-11.md | 03ed856 | 2026-05-30 |
| 12 | chapter-12.md | 6b693fa | 2026-05-30 |
| 13 | chapter-13.md | 6b693fa | 2026-05-30 |
| 14 | chapter-14.md | 6b693fa | 2026-05-30 |
| 15 | chapter-15.md | 03ed856 | 2026-05-30 |
| 16 | chapter-16.md | 03ed856 | 2026-05-30 |
| 17 | chapter-17.md | 03ed856 | 2026-05-30 |
| 18 | chapter-18.md | 03ed856 | 2026-05-30 |
| 19 | chapter-19.md | 03ed856 | 2026-05-30 |
| 20 | chapter-20.md | 03ed856 | 2026-05-30 |
| 21 | chapter-21.md | 03ed856 | 2026-05-30 |
| 22 | chapter-22.md | 03ed856 | 2026-05-30 |

## What "locked" means

A locked chapter is the canonical source for downstream production (EPUB, audiobook, print). Future edits to a locked chapter file should be made deliberately, as post-lock revisions, and should be recorded here with a new "locked-at commit" and lock date. The Voice Editor, Continuity Tracker, and Plan Editor should treat the locked state as the baseline against which subsequent changes are reviewed.

Drift can be detected mechanically by `git log -- book-one/chapter-XX.md` showing commits after the locked-at commit.

## Production status

- **EPUB**: `book-one/The Brightest Fire.epub` was rebuilt on 2026-05-30 from the locked state. The cover asset was replaced with `Brightest_Fire_cover.jpg` (1600x2400, ~850KB) after the prior 2.7MB PNG caused display failures on multiple e-reader platforms. The original `Brightest_Fire_cover.png` is retained as the high-resolution master.
- **Audiobook**: not started. Production plan exists at `book-one/audiobook/production-plan.md`. Kharren/Kharren Fault homophone decision still pending before voice work begins.
- **Print / paperback**: not started.
