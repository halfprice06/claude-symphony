# Cycle 19: changes (actor)

This cycle changed note timing (new lead rules), one articulation test, two tempo-map steps and levels. REAPER: fresh start, project opened (33 tracks), `build_reaper.py build/parts.json jobs --midi-only --tempo` (all tracks; Violas fully rebuilt for the Stac On Bow row; tempo markers 532, mismatches none), save, quit, fresh start, open, render. After the render, one level-only stem fix (`stem_fix.py 19 cycles/c19/rendered_build build --apply`, 18 stems; originals in `cycles/c19/render_first/`), then `render_cycle.py 19 --measure-only` and `build_reaper.py --mix-only` on the same 18 tracks. Saved and quit. The quit job timed out at 60 s both times, and REAPER had exited both times.

Files: `cycles/c19/before/` (c18 tools and data), `cycles/c19/rendered_build/` (the data and code the render was made from). Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c19-actor/` (`lib.py`, `post.py`, `lag.py`, `xover.py`, `holes.py`, `vtrip.py`, `bchk.py`, `clim.py`, `cmp.py`, `chk.py`, `gaps.py`).

## Accepted

### C #1: GENTLE_ACCENT wind and brass accents get leads (new generic rule)
- `score_to_parts.py`: new `ACC_ART_LEAD = True`. Only `acc_art` notes whose row name contains "Accent" keep the score onset. Other accents fall through to RETONGUE_LEAD_S or the entry branch. Swells and CC11 stay on score time.
- Result: wind and brass re-tongue leads went from 835 to 1004 (plus entry leads), for example at 124/125, 284-286, 328, 548, 568 and 676.
- Measured: the audio moved by the planned lead. Each note's c19 level envelope was aligned to c18 around the onset. Median shift: brass -0.050 s (n 110), winds -0.030 s (n 92).
- Applied to C's c18 sample-only arrivals (brass +0.107, winds +0.095), this gives about +0.057 / +0.065 s. The target was 0.065 or less.
- Per-onset brass medians (`post.py`, C's measure): 100 0.104 -> 0.049, 124 0.117 -> 0.072, 284-286 0.10-0.11 -> 0.05, 548 0.112 -> 0.037. A few single notes read later on this measure (Trumpet 1 at 124/125). Their envelopes show the whole attack 0.035-0.05 s earlier. The measure picks a later peak on a rising note.
- Accents refit after the render (brass, wind; `--keep-long-qn 1.4 --pickup-over 2.5`, skip Trombone 1 521/529 and Contrabassoon 536):
  - brass in 2-4 dB: 23 -> 30 of 37 predicted;
  - winds: 91 -> 113 of 142;
  - 2-5 kHz front minus body over 3 dB: brass 0, winds 2.

### C #2: re-tongue lead for strings (generic rule, upper strings and celli)
- `retongue_ok()` now accepts string notes on plain "Sus MAX". It excludes:
  - REP_SPLIT / MEAS_TREM strokes and STR_SHORT_AFTER_SUS stroke runs;
  - short_sus notes and DOWNBOW strokes;
  - notes with written chords (new `poly0`: polyphony on written lengths; `polyphonic()` at that point sees the legato overlaps and called every Violins I note polyphonic);
  - re-bowed notes and the notes after them;
  - the Leg -> Sus entry path.
- `build/score_config.py`: RETONGUE_LEAD_S Violins II / Violins I / Violas / Violoncellos 0.10 s.
- The basses were left out. A family-wide value gave 151 basses notes a lead, and the basses' eighths are on time with ABUT_LEAD (c07). DETACH_LEAD_KEEP_QN now skips notes with a re-tongue lead, because the previous stroke moves with them.
- Result: 12 notes. Violins I 125/128/285/286/566, Violins II 125/284/285/286/566, celli 125/285.
- Audio shift -0.09..-0.105 s, except Violins II 125 (-0.015).
- Bar 72: Violins I 285 +0.233 -> about +0.13 s, Violins II 285/286 +0.173/+0.192 -> about +0.08/+0.09.
- Open:
  - the violas at 285/286 (dyads, poly0) and their 100/115.5/279.5/675.5;
  - the Violins I notes C listed after a slurred Leg target (59.5, 77.5, 159.5, 571.5: merged short_sus notes);
  - Violins I 127.25/127.75.
- Partial pass.

### C #3: slur heads start with their target (new generic rule)
- `SLUR_HEAD_LEAD = {"string": True}`: a string slur head on Sus MAX, 0.5 qn or shorter, whose next note is a led legato target, starts as early as that target. The note before it ends at the head's moved onset (Sus) or 0.04 qn before it (other rows). CC11 is held from the moved onset. parts.json `slur_head_leads`.
- 21 Violins I heads (C listed 23; 259.5 and 455.5 do not qualify).
- Measured, pitch crossover (head pitch harmonics 1-4 over the previous pitch, `xover.py`): median +0.088 -> -0.062 s. The heads now sound their full eighth, but 0.06 s early (worst -0.147).
- Open for c20: a lead of about 0.10 s instead of the target's 0.17 s should land them near +0.01 s with 0.75 of their written length. Proposed as a `SLUR_HEAD_LEAD` "lead_s" option.

### C #4: Oboe leads
- ENTRY_LEAD_S Oboe 2 (0.0, 0.14, 0.0); RETONGUE_LEAD_S Oboe 2 0.12; new generic `RETONGUE_LEAD_ART_S` with Oboe 1 {"Leg Slur MAX": +0.08}.
- C's Leg Slur entry extra for Oboe 2 (0.16, and 0.10 tried) was not used. On top of the 0.14 s loud lead it filled the eighth rest before 416.5 to 0.02 qn. Oboe 2 keeps the wind 0.055.
- Measured shifts on Oboe 2: -0.08..-0.18 s at the tutti onsets.

### C #5: recapitulation poco rit.
- PHRASE_ARCS (568, 576, "open"), RAMP_SPANS (576, 584, 126).
- Bars 145-146 now play 126 -> 125.8 ... 112, identical to bars 45-46. Bar 144 no longer slows (568-575 at 122-128).
- Re-bow rows unchanged (frozen). The render is 0.1 s shorter.

### A #1 (test FAILED on 7 of 9 notes): accented Leg BC notes as fresh Sus MAX strokes
- DOWNBOW_STROKE_AT: celli 91/317/321/539, Violins I 100/142/154/533/548. Their accent_fits rows and the Violins I 142/533 accent_bodies rows were removed.
- Front (score onset..+0.15 s) minus body (+0.45..+0.75), c18 -> c19, stem:

  | Note | c18 | c19 |
  |---|---|---|
  | Vc 91 | -4.9 | -7.9 |
  | Vc 317 | -2.8 | -4.8 |
  | Vc 321 | -6.0 | -0.8 |
  | Vc 539 | -3.2 | -5.6 |
  | Vln I 100 | -2.0 | -2.2 |
  | Vln I 142 | -0.4 | -1.8 |
  | Vln I 154 | -3.0 | -4.3 |
  | Vln I 533 | -2.3 | -0.7 |
  | Vln I 548 | -2.4 | -4.8 |

- The Leg -> Sus path cuts the legato note at the keyswitch, and the Sus attack blooms over 0.3-0.8 s. Celli 539 has a 7 dB hole before the beat.
- The stem fix set back the bodies that rose on the two crescendo arrivals: celli 91 -4.5, 539 -2.0 dB (they had risen +4.9/+2.3).
- Revert in c20, except celli 321 and Violins I 533. Then refit the string accents on those notes.

### A #2 / A #4: string and a2 horn join holes
- Early fills on celli 365/369 (with SLUR_PAIR_RELEASE_DB_AT -1), violas 72/180/517, Violins II 236/296/405, Horns a2 311/312.5.
- The critic's times were from the moved onset; the rule keys fills to the score onset. As first written they landed 0.05-0.24 s late: no change on the violas, and a +5.2 dB spike on the a2 horns.
- Fixed in the stem fix: pre_s = lead + pre, hold_s = hold - lead. Four fills were lowered for 30 ms peaks: celli 369 4.5, Violins II 296 2.5, 405 2.0, Horns a2 311 2.0.
- Holes (lower body minus the 30 ms minimum), c18 -> c19:

  | Join | c18 | c19 |
  |---|---|---|
  | Vc 365 | 12.1 | 5.7 |
  | Vc 369 | 9.3 | 3.3 |
  | Vla 72 | 8.9 | 3.9 |
  | Vla 180 | 7.9 | 3.0 |
  | Vla 517 | 7.4 | 4.9 |
  | Vln II 296 | 6.5 | 4.4 |
  | Vln II 405 | 6.6 | 4.7 |
  | Vln II 236 | 6.8 | 3.6 |
  | Hn a2 312.5 | 8.9 | 3.8 |
  | Hn a2 311 | 4.9 | 2.9 |

- 30 ms peak over the louder body: +1.6..+2.4, except celli 365 +3.3 (c18 +3.0) and Horns a2 311 +3.5 (c18 +3.1).

### A #3: bar-135 mf accents
- accent_fits: Violas 536 [3.0, -4.0] (3.0 alone measured +7.3), Contrabassoon 536 3.0 (skipped in the refit), celli 536 2.0 (2.5 measured +4.2).
- 536 minus 537 (+0.15..+0.40 s): Violas +0.5 -> +3.3, Contrabassoon -3.4 -> +3.7, celli +6.1 -> +3.7. Violins II, basses and Bassoon 1 unchanged.

### A #5 (test FAILED): letter-G viola triplets on Stac On Bow RRx9
- ART_SPANS Violas 464-484, full length, stroke velocity.
- Onset separation median 4.5 -> 2.6 dB (pass >= 6). The row played 3.1 dB louder re master.
- The level was set back by an exact -3 dB shape: -17.9 -> -17.8 dB re master.
- Revert in c20 (a full Violas rebuild).

### B #1-#4 (level only; measured plain power re master, c18 -> c19)

**B #1, letter G 468-480:**
- Bass trombone LEVEL_SHAPES = crescendo part only; Violins I, Flute 1 and Oboe 1 +2.5 dB over 464.2-483.5.
- Bass trombone -9.3 -> -13.1; Violins I -10.8 -> -8.4; Flute 1 -19.0 -> -16.7; Oboe 1 -20.7 -> -18.7. Trombone 1 and Horns a2 unchanged.

**B #2, fugato:** celli roles [336, 358, 3] / [336, 352, 2] now end at 348. Over 348.5-358: celli -3.5 -> -5.8, violas -6.0 -> -5.1, Bassoon 1 -6.7 -> -5.7.

**B #3, Lento:** roles Bassoon 1/2 [36, 48, -3, 1]. Over 40-47.8: Violins I -10.9 -> -10.3, Bassoon 1/2 -11.5/-9.9 -> -14.0/-12.4.

**B #4, bar 122:** Trombone 2 and Bass trombone 484-492.5 roles deleted. Trombone 2 -11.6 -> -13.9, Bass trombone -11.6 -> -13.4, Trombone 1 -12.7. The tam-tam stays on top.

## Rejected or deferred
- C #4: the Oboe 2 Leg Slur extra (above).
- B #5 small items (Horn 3/4 soft anchors, harp f trim, tam-tam pp): no change, as B proposed.
- The string accent refit: deferred until the A #1 revert.

## Before / after (c18 -> c19, after stem fixes)

| Measure | c18 | c19 |
|---|---|---|
| Master integrated (float stem sum) | -16.3 LUFS | -16.3 LUFS |
| Master LRA | 22.5 LU | 22.5 LU |
| Master sample peak | 1.509 | 1.523 |
| Master true peak | +3.6 dBFS | +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 19.0 dB | 19.0 dB |
| Delivery limiter | 1.9 dB | 1.8 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion (mp3) | 8.59 / 4.50 dB | 8.57 / 4.50 dB |

- Climax order (delivered S max): 160 -10.10 > 122 -11.60 > 167-170 -13.20 (c18 -10.10 > -11.30 > -13.10).
- Attack probe: 0 flagged.
- REAPER memory: 25 GiB with 0 compressed at the render start; 45 GiB with 30 compressed after it.
- Delivered mp3: `cycles/c19/mvt1-mockup-c19.mp3`.
