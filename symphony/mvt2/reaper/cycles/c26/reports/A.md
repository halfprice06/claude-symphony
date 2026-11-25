# Cycle 26, critic A: articulation and phrasing

Render under review: c25, with c24 for comparison where Dan's notes apply, because he listened to c24. Scripts are in `/private/tmp/claude-501/mockup-loop/c26-A/`: `fin.py`, `bands.py`, `fin3b.py`, `mcent.py`, `fold.py` (final chord), `tbn.py` (trombone attacks), `jitter.py`, `tree2.py` (patch CC1 tables), `timp.py`. All times are score qn from `build/parts.json` (the moved note-on is `qn`, the score onset is `sq`). Both of Dan's 2026-10-12 notes fall under this lens, so they are findings 1 and 2.

## 1. Final chord, bars 89-92 (qn 292-304), all five string sections: the held chord swells and darkens in a regular 4-second cycle. This is Dan's "bowing effect". Measured; the fix is inferred.

**What is wrong.** Every string section holds one sample for 15-25 s. Violins I has C5 from 291.74, Violas E flat 3, Violoncellos A flat 2 and Double basses A flat 1 from about 291.8. Violins II has A flat 4, merged from 286. The Hollywood Strings sustain samples loop with a period of 3.93-4.00 s (3.40 s for Violins II), so the whole chord cycles in tone colour every 4 s. A real section changes bow at staggered times, which no listener hears as a cycle.

**Evidence (measured).**
- Master, 100-300 Hz band (cello and bass partials 2-5, viola fundamental), qn 292.6-303:
  - c24: residual swing 6.1 dB p2p, period 3.96 s, autocorrelation 0.59. Folded at 3.96 s, the periodic part alone is 7.2 dB p2p.
  - c25: 4.8 dB, period 3.94 s, autocorrelation 0.58.
  - The opening ppp chord (qn 3.5-8.5, same chord type, notes under 2 loops long) has no cycle: autocorrelation 0.18.
  - Master spectral centroid over the final chord: c24 period 3.96 s, autocorrelation 0.53, swing 847 cents. c25: autocorrelation 0.39, 655 cents.
- Per stem, the brightness cycle is strong. Centroid residual autocorrelation at the loop period: Violins I 0.63, Violoncellos 0.63, Double basses 0.59, Violins II 0.45 (3.40 s), Violas 0.39. Swings are 580-1380 cents.
- The level cycle is mostly gone. The c17 inverse loop profiles (`build/loop_profiles.json`, keys Violins I/Violas/Violoncellos/Double basses 292 and Violins II 286) took the master's 0.5-1.5 Hz level movement from 2.7 dB (c15) to 1.3 dB (c25), and the Violins I stem from 10.0 to 3.9 dB p2p.
- A volume envelope cannot fix a cycle in tone colour. What is left is the sample's change in harmonic balance inside each loop. The level and centroid residuals are anti-correlated (Violins I -0.67, Violas -0.77), so each loop sounds louder-and-darker, then quieter-and-brighter. That is the movement of a slow, synchronized bow stroke (inferred).
- Other candidates checked:
  - The volume fade (morendo rows) is smooth.
  - CC1 is constant at 42 from 292.25 (38 after 300.6).
  - The reverb tail decays steadily at about 33 dB/s.
  - Violins I's printed bowings (V at 292, down-bow at 295, V at 298, down-bow at 301) are rendered as 6 CC notches in CC11 (34 -> 28 in one step at 295 and 298, 22 -> 16 at 301, back over 0.25 qn). They do not show in 100 ms level frames, so they are not the cycle. They are still a synthetic bow change on a single looping sample.
- Patch tables (measured, read from the .oib files with `tree2.py`). In the 1st Violins, 2nd Violins, Violas and Celli KS Masters, CC1 38-42 plays two sample sets at once: Non Vib at gain 0.27-0.54 and Sus Vib at 0.84-0.89. Each set loops on its own. From CC1 55 up, only Sus Vib sounds (Non Vib 0.00). In the Basses KS Master the two layers crossfade across the whole CC1 range. The coda holds CC1 38-42, so each string track loops two layers.
- Same-pitch re-bow evidence from this render: the Double basses' D flat 2 at qn 289 is a fresh Sus MAX note after a 0.03 qn gap at v41. It dips 3-5 dB for about 0.4 s, with no hole: -55 -> -59/-60 -> -57 dB in 50 ms frames.

**Fix.** Re-bow the held chord at staggered, irregular times, so that no sample plays one segment much past 3.8 s and no two sections change together.
- In `tools/score_to_parts.py`, add `REBOW_AT = {track: [score qn, ...]}`. Apply it after the tie merge: split the merged note at each listed qn. The first part ends 0.03 qn before (the Double basses 289 shape). The new note starts at the qn with the same pitch, velocity (41) and articulation, and gets no legato lead (same pitch).
- Suggested points. Segments come out at 1.8-3.8 s and the closest two sections' changes are 0.26 s apart. Spread the last pairs a little more.
  - Violins I: 295, 298, 301 (the printed bowings), plus 302.75 inside the fermata bar. The printed segments are 3.7/4.1/4.5 s, then 2.9/3.4 s.
  - Violins II ("change bow at will", from its printed 289 note): 290.6, 293.0, 295.8, 297.6, 300.2, 302.2, 303.4.
  - Violas: 294.1, 296.9, 299.2, 301.5, 303.1.
  - Violoncellos: 293.6, 296.3, 298.6, 300.6, 302.35.
  - Double basses: 294.5, 297.2, 299.8, 302.0, 303.35.
  - Keep the intervals irregular. Equal steps would bring back a common period.
- Remove the five loop-profile entries listed above from `build/loop_profiles.json`, because they are keyed to note starts that will no longer exist. Remove the Violins I bow notches at 295/298/301 (`bow_q` loop, around line 1287): the re-bows replace them.
- Each continuation note plays Leg Slur MAX (Violins I/II, Violas, Violoncellos) or Sus MAX (Double basses) as a new note. Inferred: on the legato patches that is the soft first-note layer, which suits a pp bow change. If a re-bow dips more than 4 dB on its stem, add a `{"db", "pre_s"}` entry in `build/early_fills.json`, or put the continuations on Sus MAX for the Violas and Violoncellos (row already loaded). Violins I/II have no Sus MAX row loaded, so that would need a full rebuild of those tracks.
- Second step, only if a stem's centroid cycle still has autocorrelation over 0.35 after the re-bows: hold CC1 at 56 from 292 on Violins I, Violins II, Violas and Violoncellos. That plays Sus Vib alone instead of two looping layers. The table values are measured; the effect is inferred. Do not change the Double basses' CC1.
- Small, measured: after the note-off at 304, the post-release hold lifts the tails. Violins I and Violoncellos go -16 -> -10 dB over 0.5 qn (1.5 s at 20 bpm); Double basses go -17 -> -11.6 dB in 0.1 qn. Hold each track's value at its release instead of the fixed -10 dB, in the final-fade code in `score_to_parts.py` that writes the -10 hold after the last release.
- Checks on c26, using `fold.py`/`mcent.py`:
  - Master 100-300 Hz periodic fold under 3 dB, with autocorrelation under 0.3 (opening chord: 0.18).
  - Per-stem centroid autocorrelation under 0.3.
  - Each re-bow dip 3 dB or less on its stem and 1 dB or less on the master.
  - The morendo still falls (c25: master from about -41.5 at 292.5 to -51 by 301).

## 2. Trombone 1, bars 63-64 (qn 212.5, 213, 218): the accents are a 2-5 kHz burst, not weight. This is Dan's "too harsh" note. Measured.

**What is wrong.** The three accented notes (ff marcato, the call back to movement 1) play Sus Accent MAX at v108/105/110. On top of the sample's attack, `ACCENT_DB_AT` (+4.0/+3.0/+4.5 dB) rises in 10 ms. Both stack on the same 40-80 ms. The 218 F3 accent sits inside the printed ff > mf decrescendo, where the surrounding orchestra has already thinned, so it stands out most.

**Evidence (measured, c24 and c25 are identical here).**

Tbn1 stem, 20 ms frames, attack peak minus the note's own body at +0.2..+0.4 s:

| qn | 2-5 kHz | broadband |
|---|---|---|
| 212.5 | +8.6 dB | +3.6 dB |
| 213 | +7.4 dB | +3.8 dB |
| 218 | +13.4 dB | +2.8 dB |

The broadband emphasis already sits in Dan's 2-4 dB. The harshness is all in the upper mids.

For comparison:
- The Marc Lng eighths of the same line: 2-5 kHz -5.5..+3.5 dB.
- Trombone 2 Sus MAX at 200-210: -4.2..+1.1 dB.

On the master at 218, the 2-5 kHz band jumps +12.1 dB over the 0.2 s before and stands +14.8 dB over 0.25-0.45 s after. At that moment Tbn1 is the master's 2-5 kHz content (its peak is -0.4 dB re the master peak) and 13 dB over Violins I. At 213 the master band rises +4.8 dB, with Tbn1 level with the master. At 212.5 the strings' sf masks it (+0.6 dB).

**Fix** (Dan's own suggestion; the Sus MAX row is already loaded on Trombone 1, so this is a `--midi-only` update):
1. In `tools/score_to_parts.py`, add `ACCENT_ART_AT = {"Trombone 1": {212.5: "Sus MAX", 213.0: "Sus MAX", 218.0: "Sus MAX"}}`. Check it before the `Sus Accent MAX` branch (around line 1149). Set `VEL_SET` for these three notes to v96/v96/v92 (inferred starting values).
2. Replace the `ACCENT_DB_AT` shapes for Trombone 1 with a swell that has no front edge: 0 at onset - 0.01 qn, +3.0 dB at onset + 0.07 s, held to + 0.25 s, back to 0 by + 0.6 s. Write it as a seconds-based shape like `MARC_ATTACK_S` (`sec_qn`), not the current 10 ms rise. Use +2.5 dB at 218 (inside the decrescendo).
3. Keep CC11 for 218 at the decrescendo's own value. Today it jumps to 122 at 218.0 and falls; start it at the hairpin's current value (about 114) instead.
4. Checks:
   - Each accent's 2-5 kHz attack within +4 dB of its own body.
   - The master 2-5 kHz rise at 218 under +5 dB.
   - Each accent still 2-4 dB broadband over the body of the neighbouring Marc Lng eighths. c21 raised 218 because it measured only 1.5 dB over them. If it falls under 2 dB, raise the swell, not the velocity.
   - If Sus MAX at v92-96 still bursts more than +6 dB in 2-5 kHz, lower the velocity in steps of 8 before anything else.

## 3. Timpani, the final ppp roll (qn 292-304): a regular 3.12 s loop pulse, the most periodic stem in the last chord. Measured, minor.

The roll is one 12 qn note at a flat CC7 of 16. Its level residual has a period of 3.12 s with autocorrelation 0.74 (2.6 dB p2p broadband, 4.9 dB in 100-300 Hz, the celli's band). The roll at 226-237 is the same: 2.94 s, autocorrelation 0.72. c25's +4 dB roll lift (B #2) brought it to -5.2 dB in that band against the celli's +3.0. Once the strings stop cycling (finding 1), this is the last regular pulse under the chord (inferred).

A roll's spectrum stays the same through its loop, so a level-only inverse profile works here, unlike the strings. Fit one on the c25 Timpani stem over qn 292.4-303.5: period 3.12 s, same method as `loop_profiles.json`, corr clamped -3..+3 dB. Add it as a `"Timpani": {"292": ...}` entry, and do the same for 226 (2.94 s). Check: residual autocorrelation under 0.3.

## Also checked, no finding

- No chord reaches a monophonic legato patch on any track (all 32 checked: no two overlapping legato-articulation notes start together or overlap by more than 0.6 qn).
- Legato overlaps in every legato track have a median of 0.040-0.049 s and a minimum of 0.037 s inside slurs. The gaps I found (Ob1 143->144, Vla 252->252.5, Vc 145.5->146 and others) are slur boundaries in the score.
- Keyswitches all arrive 0.012 qn or more before their notes. The Leg Slur <-> Leg BC switches inside legato overlaps are by design.
- The Violins II con sord. portato of bars 15-21 is merged with notches. The re-articulations read 1-6 dB, which is in range.

Do not touch:
- The Marc Lng eighths of the Tbn1 marcato line (`MARCATO_SPANS`, `MARC_ATTACK_S`, `MARC_BODY_DB`). Their 2-5 kHz attacks are clean.
- The legato overlap and lead tables. No legato chords anywhere.
- The loop profiles on notes other than the five final-chord entries named in finding 1.
- The Double basses' same-pitch re-attack shape (0.03 qn gap), which finding 1 copies.
- `UNLOAD_UNUSED_ROWS` (finding 2 needs no new row).
