# Cycle 1 changes (actor)

Input: critic reports A (articulation), B (balance), C (blend/space) on the cycle 0 render. Snapshot of the tools and parts.json before any change: `before/`. Final render: `render/`, `metrics/metrics.md`, `mvt2-mockup-c01.mp3`. A first render made before the render-speed and gain fixes is kept in `pass1/` for comparison.

## What changed

### tools/score_to_parts.py
- **Hairpins (B1).** `hairpins_and_marks()` replaces the old pairing. It makes one pass per staff in time order. A hairpin closes at its own stop of either kind, at a later dynamic mark, at a new hairpin start, or at the next rest of 2 qn or more. Every printed mark sets the level. Between marks the level holds; c00 drew linear ramps between all breakpoints, so dynamics drifted across whole sections. A hairpin with no target moves 14 CC. A check prints any printed mark the curve misses by more than 2 CC; it prints nothing. The longest hairpin is now 9 qn; c00 had 15 spans of up to 268 qn.
- **Slurs (A2).** The last note of a slur is now slurred (`a <= q <= b`). The legato overlap applies only when both notes are in the same slur. Where the next note starts a new slur, the note is shortened by 0.05 qn so the patch plays a new attack.
- **Repeated pitches (A3).** No legato overlap into the same pitch. The first note ends 0.06 qn early (legato) or 0.03 qn early (other notes), so the repeat is not cut off.
- **Legato speed (A4).** For legato target notes, velocity comes from the note's length in seconds (tempo map): under 0.45 s → 100, under 0.9 s → 80, otherwise 60. Loudness stays on CC11. Velocities of first notes are unchanged.
- **Breaths, tenuto, accents (A6).**
  - Breaths: at a `breathe` the note before ends `min(0.25 qn, 20%)` early (29 marks).
  - Tenuto: the note is shortened by 0.06 qn before the next note, with a CC11 bump of +5 decaying over 0.5 qn.
  - Accents: `Sus Accent` only at f or louder. Every accent gets a CC11 bump of +8 decaying over 0.3 qn and velocity +10.
- **Controller timing (A5).**
  - Keyswitches and CC15 (mute) changes go into the preceding rest when there is one: rest start + min(0.5, 25% of the rest). For example, the con sord. at 42 is now sent at 9.5 and the senza at 108 at 90.5.
  - The first keyswitch is no longer sent, because the patch state already selects it (B6, the bar 1 celli).
- **Solo boost (B6).** +8 CC11 after a text containing "solo", "cantabile" or "espr." (not "tutti"). It lasts until the next text on that staff or a rest of 3 qn or more.
- **Timpani (B2).**
  - CC7 is computed per articulation as `127*10^(dB/40)`.
    - Rolls: ppp -36, pp -31, p -26, mp -23, mf -21, f -20, ff -18 dB.
    - Strokes: the roll value + 16 dB. The first render showed pp strokes at -54 with +12.
  - A roll, or a chain of one-bar rolls, settles 4 dB over 2 qn unless a crescendo is printed.
  - Stroke velocity is at least 56 (pp) to 110 (ff).
- **Harp (A1, B5).**
  - Patch is now `Harp Sus RR.oib`, which has samples from 24 to 103. Harp Maestro had none below 48, so 79 notes were silent.
  - CC11 is constant at 110, and velocity comes from the printed dynamic: pp 52, p 64, mp 76, mf 90.
- **Harp harmonics (A1).** A new 27th track, "Harp harmonics", plays `Harp Harmonics.oib`. It takes the five flageolet notes at qn 273-277 and keeps only the sounding (upper) pitch; the written lower octave is dropped. The track is appended last so the other stem numbers do not change. Measured pitches are 311 Hz and 622 Hz at qn 273 and 276, as expected, so the patch takes sounding pitch.

### build/mix.json (new) and tools/build_reaper.py
- **Track gain (B3, B4, C1)** goes to `D_VOL`. Gains were set from the first render's per-dynamic medians, so that at p every solo wind and string section measures about -49 to -51 dB RMS. Final values in dB:

  | Track | Gain (dB) |
  |---|---|
  | Flutes | -1 |
  | Oboes | -5 |
  | Cor anglais | -1 |
  | Clarinets | -1 |
  | Bass clarinet | +1 |
  | Bassoons | -2 |
  | Contrabassoon | +2 |
  | Horns | -4 |
  | Trombones, tuba | 0 |
  | Timpani | -6 |
  | Harp | -4 |
  | Harp harmonics | -2 |
  | Violins I | +5 |
  | Violins II | +6 |
  | Violas | +2 |
  | Celli | 0 |
  | Double basses | -9 |

- **Mics (C2).** These go into the Opus state.
  - Woodwinds: Close 0.5, Main 0.8.
  - Horns: Close 0.5, Main 1.0.
  - Harp: Main is now loaded; Close 0.6, Main 1.0.
  - Timpani: Surround is unloaded; Close 0.43, Main 0.24.
  - Trombones, tuba and strings keep the patch's own mics.
- **One reverb (C3).** Every patch's `fx:0` ConvolutionReverb is replaced by the Violins I patch's (S. Cal. Hall strings LR Rear), at fx volume 0.151 and wet 2.0. Depth is set by the per-mic Reverb Send:

  | Group | Send |
  |---|---|
  | Strings | 0.25 |
  | Harp | 0.3 |
  | Woodwinds | 0.35 |
  | Trombones, tuba, timpani | 0.45 |
  | Horns | 0.5 |

- **Panning (C4).** Opus sub-channel pans are set to 0. Each track uses REAPER stereo-pan mode (`I_PANMODE` 5) with C's seat and width table (`D_PAN`, `D_WIDTH`).
- The `.b64` states are always regenerated, so mix.json changes take effect. Before, an existing file was reused.
- New `--mix-only` flag: sets volume and pan on the existing tracks without reloading patches.

### Render speed (tools/render_cycle.py, mvt2-v77-mockup.rpp)
- The first render showed the late entries from A5: about 0.5 s of digital silence and then a full attack. They happened at the same moments in several tracks at once, for example qn 204 in Cbn, Hn2 and Hn3, all at 510-515 ms. That points to sample streaming from the USB/exFAT sample drive falling behind the full-speed offline render.
- The project now renders at 1x offline. The setting is `RENDER_1X 1` in the .rpp; `GetSetProjectInfo` cannot set it, so the .rpp was edited and the project reopened. `render_cycle.py` warns if the setting is missing.
- Result:
  - Woodwind late entries (over 120 ms to reach -70 dBFS) went from 20 to 3.
  - Strings at 42 went from 545-575 ms to 135-350 ms.
  - Brass at 204 went from about 515 ms to 170 ms.
- Some delays of about 0.5 s remain: Hn1 at 17 and 261, Hn3/Hn4 at 84, Vln II and Vla at 108, Vln I at 237, Cbn at 87, Timpani at 277.

## Measured, c00 → c01

| | c00 | c01 |
|---|---|---|
| Integrated loudness | -24.2 LUFS | -27.4 LUFS |
| LRA | 20.0 LU | 23.5 LU |
| True peak | -2.7 dBFS | -9.2 dBFS |
| 63 Hz band re 1 kHz (ref -6.2) | +14.1 | +4.7 |
| 125 Hz band (ref 7.0) | 11.7 | 6.9 |
| 4 kHz band (ref -14.1) | -18.9 | -14.9 |
| Loudest stem in most bars | Double basses 41, Timpani 15 | Celli 26, Horn 1 10, Vln II 8, Vln I 7, Double basses 7 |

- **Medians at p (RMS):**
  - c00: winds -40.7 to -50.7, strings -46.2 to -51.8, basses -35.2, harp -62.1.
  - c01: winds -49.0 to -51.3 (Cl2 -54), strings -49.1 to -50.0, basses -49.3, harp -51.8.
- **Timpani:**
  - ppp rolls: -48.2, against -27 to -29 in c00.
  - f rolls: -37.2, against -23.9 in c00.
  - ff: -36.0, 5 dB under the celli.
- **Harp:** the low chords at 18, 21 and 24 now sound at -57 to -61 dB; in c00 they were digital silence.
- **Celli, bar 1:** -66.9 dB; in c00 it was silent.

## Rejected or deferred

- **Leg BC (bow-change legato) for unslurred connected string lines; celli divisi DIV A/B for the slurred upper-cello answers at 18 and 22 (A2):** deferred to keep this cycle's changes measurable.
- **Moving legato target notes earlier for strings (A4, second part):** deferred until the new velocities are measured with f0.
- **Moving entry notes earlier to hide the remaining start delays (A5(3)):** rejected. The delays are not deterministic: they changed between the two renders, so a fixed shift would make some entries early. The likely remaining fix is Opus's streaming preference, `PreloadSize` (now 1) in `/Library/Application Support/East West/Opus/Preferences.json`, set to the HDD preset. That is a global Opus setting outside this project, so it is left for Dan to decide.
- **Accent handling for strings:** none are printed.
- **Solo violin for bars 17-22:** there is no solo violin library on the drive.
- **Horn 3 con sord.:** no muted-horn patch on the drive. Stopped horn is a different sound, so it was not substituted (A agrees).
- **Spaces II on a REAPER bus (C3, stronger option), master EQ (C6):** not this cycle.

## Open (measured, for the next critics)
- Celli are the loudest stem in 26 bars, including the climax at 57-63 (4-8 dB over the violins) and the counter-melody at 80 (5 dB over the theme in Vln II). At mf/f the celli patch is 8 dB hotter than the violins, and the espr./cantabile boost adds to that.
- Double basses at f are 8 dB under the celli (-41.9 vs -33.8), while at p they are level.
- Timpani pp strokes at 84-85 still measure about -58 dB, under the -48 to -52 target.
- The Harp harmonics stem is about -50 dB.
