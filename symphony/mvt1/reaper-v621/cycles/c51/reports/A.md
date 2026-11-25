# Cycle 51, critic A: articulation and phrasing

Under review: the c50 render (`cycles/c50/render`, dry stems 01-40 for articulation, `00_Master.wav` for audibility; return stems 91-94 skipped) and the data that made it (`cycles/c50/rendered_build/parts.json`, `rendered_build_pass2/`, `build/score_config.py`, `build/mix.json`). c51 applies the MIDI rules of EW-TEMPLATE-PLAN sections 5-8 and 10 and is the last cycle of this round. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c51-A/` (deleted at the end).

## Manual notes

Second round, cycles 48-51: pages chosen for this lens's top open problems (string repeats and the celli measured tremolo, the coda pedal, the CC1-only macro test, wind legato velocity). Patch facts come from the installed `.oib` files, read with `opus_state.load_oib`.

| Source (PDF page) | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| 2021 p.97-98 | Tremolo comes in two kinds, unmeasured and Measured Tremolo TS. The measured one pulses in time with the host tempo, has no velocity response, and CC11 sets dynamics and timbre. "All 5 orchestral sections include both." | Celli bars 117-121 (qn 464-484), the only measured tremolo in v621 (G2 whole notes, two slashes, f with a crescendo to fff). | No. The tremolo is expanded into Stac / Stac On Bow strokes (MEAS_TREM), which run together (finding 2). |
| Patch, Celli KS Master "Meas Trem TS" | Samples are tagged 145 bpm with tempo sync on (elastique). CC11 crossfades pp / mp / f / ff. AHDSR release is 524 ms, and there are release-trail groups. | Same. | Never tried. The stretch is 126/145 = 0.87, beyond the 2025 manual's advice to stay within about 10 bpm (2025 p.52). |
| 2021 p.53-54, p.64, p.150-151 | Velocity is for short articulations, CCs for sustains. In the HO strings and woodwinds, CC11 sets dynamics and CC1 sets vibrato. The LITE string patches put dynamics and vibrato together on CC1. | Short rows (finding 2) and the CC1 macro test (finding 6). | Partly. Short rows take their dynamics from velocity and CC11 together, so they are attenuated twice. Sustains follow. |
| Patch, Celli KS Master Sus MAX (mf groups) | CC1 crossfades three vibrato layers. Non Vib: 1.0 at CC1 0, 0.54 at 40, 0.09 at 64, 0 at 72. Vib: 0.35 at 20, 0.94 at 40, 1.0 from 50 to 90, 0.7 at 100, 0.45 at 110. Molto Vib: 0.05 at 64, 0.26 at 72, 0.72 at 90, 1.0 from 110. CC11 crossfades pp / p / mf / f / ff and also drives the Global Group volume. | Finding 6. | Read only. Two vibrato layers sound at any CC1 between about 20 and 110; our string CC1 is 38-105. |
| Opus manual p.79-83; 2025 HO manual p.98 | A macro drives one or more target parameters from one CC. Each target has a minimum, a maximum and a map (table, curve segments or curve fit). The 2025 manual shows a "Modulation / Expression" macro as an example. | Finding 6. | The installed KS Masters have no macro (`macros.lastId` 0 in the Celli KS Master). The "Mod + Expression Combo" is EastWest's template setting, not a factory one. |
| 2021 p.143-144 | True legato: velocity 50-60 gives a longer transition and 110-127 a shorter one, with no change in loudness. The emulated legato needs "no significant silence" between notes. | Wind legato velocity and legato overlap (table below). | Yes. |
| Patch, wind KS Masters' LegatoSpeed | Velocity 30-127 maps to a sample start offset (44.1 kHz samples). FL 400-4800, OB and EH 0-4800, CL / BS / CB 0-2200, BC 759-1754. | Wind legato velocity. | Read. Moving from v60 to v90 skips 31 / 34 / 15 / 7 ms more of the slide (FL / OB-EH / CL-BS / BC). |
| 2021 p.91-92 (from c50) and patch | Sustain bow direction is a round-robin pair (Dn / Up). Marc Sus LITE puts a Marc Shrt attack, chosen by velocity (1-60 mp, 61-102 f, 103-127 ff), over pp / ff sustains that fade in over 368 ms. The Marc Shrt groups have a 34 ms AHDSR attack and no velocity-to-volume. | Coda pedal (finding 5). | The c50 test used the mp zone (v45). |
| 2021 p.145 | Opus continues each round-robin cycle where it stopped; a reset makes playback consistent. | Coda pedal. | CC16 reset in the pre-roll. c49 showed the coda pedal's phase does not follow a per-note count. |

MANUAL-GAPS items still open: #5 (expressive wind rows), #7 (half-section divisi), #9 (horn portato rows), #12 (Felt Cresc), #13 (bass trombone). I rank them below the six findings here for the last cycle.

## Plan sections this lens touches that are not yet applied (c50 render)

- **Section 5.**
  - Legato overlap: 19-21 ms against the plan's 45-80 / 33-58 ms. Not applied.
  - String repeated-note gaps: 10-19 ms. Not applied.
  - Wind legato velocity: v60-100 set by note length. Not applied.
  - CC1-only control: not applied; finding 6 stages the test.
- **Section 6.**
  - Shorts with the CC parked high and dynamics by velocity: not applied (finding 2).
  - Two tracks per string section: not applied, and not recommended for the last cycle.
- **Section 7.**
  - Phrase swell and taper: critic C's c50 finding #2.
  - Per-note lean-off inside slurs: not applied. I agree with C not to apply it. -2 CC at mf is about 0.5 dB, and it would deepen the 2-5 dB legato sags that the fitted fills now close.
- **Section 8.**
  - Repeated-note gaps of 60-100 ms: met on winds and brass (60-140 ms), not on strings (finding 1).
  - Legato velocity following the dynamic: not met on winds.
- **Section 10.**
  - Beat-position short velocity: not applied. In this movement it has few targets. Only 37 fugato staccatos and 116 celli strokes play short rows. The basses' and violas' eighth figures are Sus MAX strokes, which ignore velocity, so their metric weight stays in the volume envelope (METRIC_BOWED).
  - Spiccato at 50-62 % of the slot: met on violins and violas (50 %), not on celli (92 %).
  - Doublings share one curve: met (c50 report).

If critic C's PHRASE_SHAPE rule goes in together with the CC11 park in finding 2, the park must win on short rows. A phrase offset there would only change level, so route it to velocity or the volume envelope (inferred).

## c50 values re-checked against the c50 render (coordinator's list)

| c50 value | Verdict | Evidence (c50 render unless noted) |
|---|---|---|
| REP_SPLIT gap 0.08 s, frac 0.35, minimum 0.06 s | **Confirm**, applied at mp and louder. Also raise STR_REP_NEW_BOW `gap_s` 0.06 -> 0.08. | Fall after note-off at loud dynamics, re the note body: basses Sus MAX -2.0 / -4.0 / -6.6 / -7.1 dB at +40 / 60 / 80 / 100 ms; Violins I -3.2 / -5.5 / -6.3 / -9.1. Repeats that already have a 50-60 ms gap dip 5.4 dB (basses, n=14), 7.7 (violas, n=14) and 3.6 (Violins I, n=5). Today's 14-19 ms gaps dip 1.4-5.2 dB on the stems and 1.4-4.5 dB in the master. Measured, with the prediction inferred (finding 1). |
| String shorts: CC11 held at 120 plus the lower stac velocity table | **Revise:** keep it, but expect an audible effect only on the celli Stac RRx9 strokes. | Patch: short rows take CC11 only through the Global Group volume (CC 58 / 72 / 88 / 114 = -6.9 / -5.5 / -3.5 / -1.0 dB re 127). Velocity picks the layer. Celli Stac RRx9 zones are 1-36, 37-68, 69-89, 90-104, 105-117 and 118-127, so f v96 -> v76 changes the layer. Stac On Bow zones are 1-62, 63-110 and 111-127, and violas Stac 1-60, 61-94 and 95-115, so 96->76 and 80->62 stay in the same layer and change level only. Read. |
| Beat offsets 0 / -22 / -12 / -22 | **Revise.** None on the measured tremolo, which is bowed evenly. Use 0 / -10 / -5 / -10 (±4 seeded) on the written 16ths at celli 516-520, and -10 on off-beat eighths in the fugato staccatos. | At f the new base velocity is 76, so -22 drops the "e" and "a" strokes into the mp layer (37-68). Section 10's values come from ostinato spiccato, which v621 strings do not have. Read, with the musical judgement inferred. |
| Celli shorts at 55 % of the slot, 120 ms release cap | **Confirm**, with two corrections. The cap spec must name the group words (`"dyn": ["Stac", "Hrd"]`). The pass threshold is 4 dB, not 5. | Simulated from the measured single-stroke shape: the dip rises from 110 ms / 372 ms (now) to 65 / 120 by +3.3 dB, and to 70 / 150 by +2.1 dB (finding 2). |
| Wind legato velocity 90-114 by dynamic | **Confirm as low priority.** Keep the lead the long notes lose when LEG_VEL_EXTRA_S stops firing. | Join transition window (both pitches within 6 dB) by velocity, on 6 wind tracks: v<75 32-76 ms, v95+ 46-76 ms, pcX medians -14..+49 ms. There is no sign that velocity changes the audible transition (measured). From the LegatoSpeed arithmetic, v60->v90 makes transitions 7-34 ms faster. Losing LEG_VEL_EXTRA_S (0.04-0.09 s) would then move the long-note targets later by: Bass clarinet +83 ms, CL/BS +25, OB +16, FL +9. Add `LEG_VEL_EXTRA_S`-style leads for targets of 0.9 s or longer (Bass clarinet 0.08, Clarinet / Bassoon 0.025, Oboe 0.015), or refit `leg_leads` from pcX after the render (`cycles/c48/actor_scripts/realised48.py`). |
| Legato overlap in seconds (strings 0.06, winds and brass 0.045) | **Confirm as harmless, with no expected gain;** drop it first if time runs short. | 0 chord notes on legato rows (1775 legato notes), 0 keyswitch clashes, no keyswitch within 0.005 qn of its note (main and pass 2). Each script's `EWSO.CONNECTED` is 30 (FL, BS and Celli patches read). I infer, without testing, that this is the connection tolerance, so any overlap of 0 ms or more already joins. Accept the change if unchanged joins move less than 10 ms / 1 dB. |

## Findings, ranked by what a listener would hear

### 1. String repeats in the Allegro still run together: S1, the largest articulation fault left (c51 main track; measured, with the effect of the fix inferred)

**Where.**
- Double basses: 104-124, 520-536, 556-568 and 664-676 (f-ff eighth pedals).
- Violas: 86-100, 440-468, 552-568.
- Violins II: 86-100, 536-548.
- Celli: 504-520 (the accelerating G2 of bars 127-130).

**Measured** (c50, `cycles/c50/actor_scripts/dips50.py`, stem dip / master-band dip, median):

| Run | Gap | Stem / master dip |
|---|---|---|
| Basses 104-124 | 14 ms | 2.6 / 2.7 dB |
| Basses 520-536 | 14 ms | 5.2 / 4.5 dB |
| Basses 554-568 | 14 ms | 4.7 / 2.8 dB |
| Basses 664-676 | 14 ms | 3.4 / 2.6 dB |
| Violas 86-100 | 19 ms | 4.7 / 2.5 dB |
| Violas 440-468 | 18 ms | 3.9 / 1.5 dB |
| Violas 552-568 | 19 ms | 3.4 / 1.6 dB |
| Violins II 86-100 | 19 ms | 4.5 / 2.2 dB |
| Violins II 536-548 | 19 ms | 3.6 / 1.5 dB |
| Celli 504-520 | 10 ms | 3.1 / 1.4 dB |

For comparison:
- The winds' re-tongued repeats, with 60-140 ms gaps, dip 6.8-13 dB.
- The template returns took a further 0-1.4 dB off the master dips (c50 CHANGES).
- The release fall curves and the 60 ms-gap repeats are in the table above.

**Inferred.** At an 80 ms gap the dip is set by the fall at about +95 ms (the next attack needs about 15 ms to rise over the tail). That predicts about 7 dB on the basses and 7-8 dB on the upper strings at mf-ff, and 4-6 dB in the master.

Soft repeats are different. The celli's soft Sus MAX falls only -1.3 dB by +80 ms (no pp cap since c47), so at pp-mp a gap alone cannot open them. Keep the existing STR_REP_DETACH dips there (celli 504-512: -6 dB, 0.10 s).

**Fix** (`tools/score_to_parts.py`, the REP_SPLIT run detection near line 2112, `build/score_config.py`):

```python
REP_SPLIT = dict(REP_SPLIT, gap_s=0.08, frac=0.35, gap_min_s=0.06, gap_min_cc=DYN["mp"])
STR_REP_NEW_BOW = dict(STR_REP_NEW_BOW, gap_s=0.08)
```

- **Rule.** A stroke followed by a same-pitch stroke ends `max(gap_min_s, min(gap_s, frac × slot))` before the next moved onset.
  - "Stroke" covers REP_SPLIT strokes, STR_SHORT_AFTER_SUS `short_strokes` and STR_REP_AFTER_STAC strokes, at 100 bpm or faster.
  - The rule applies only where CC11 at the next onset is `gap_min_cc` or more.
  - MEAS_TREM notes take finding 2's rule instead.
- **Resulting lengths at 126 bpm.** Eighths 158 ms of 238 (66 %, détaché rather than staccato). Quarters keep a 0.08 s gap.
- **Basses spans.** On 104-124, 520-536 and 556-568, change STR_REP_DETACH `dip_db` -5 -> -3. Its 0.08 s dip now falls inside the gap and would otherwise push the stem dip past 11 dB. Keep the +1.5 dB LEVEL_SHAPES spans, and add 1 dB if the bar level falls more than 1.5 dB.
- **Interaction.** The coda pedal aliases in finding 5 inherit these gaps.

**Pass.**
- Stem dip median 6-12 dB on every listed loud run. Below 6 fails S1; above 12 sounds like staccato on unmarked notes.
- Master-band dip median 3.5 dB or more.
- Per-bar stem level within 1.5 dB of c50.
- Attack probe 0 late.

Where a run passes on the stem but stays under 3.5 dB in the master, give that span `gap_s` 0.10 (expert string median 90 ms).

### 2. The celli measured tremolo, bars 117-121, plays as a held note (c51 main track, plus one pass-2 patch test; measured and simulated)

**Where.** Violoncellos, qn 464-484: G2 whole notes with two slashes, f, crescendo 480 -> fff 484. The figure under the build to the first fff.

**Measured.**
- 79 strokes on Stac RRx9 / Stac On Bow RRx9 (seeded alternation), each 110 ms in a 119 ms slot (92 %), v96, CC11 88.
- Stem dip median 1.4 dB, 66 of 79 under 3 dB; master band 1.4 dB. The weakest repeat figure in the piece.
- Patch: Stac RRx9 release 372 ms, Stac On Bow 489 ms; the next stroke starts before the release begins.
- Isolated celli Stac strokes (qn 345-347, 240 ms notes) peak 90-120 ms after note-on, and are -1.3..-2.9 dB at +90..+150 ms and -5.7 dB at +200 ms. So in a 119 ms slot each stroke is still at its peak when the next one starts.

**Simulated** (incoherent sum of that measured stroke shape every 119 ms, with linear release ramps):

| Length / release | Change in dip vs now (110 ms / 372 ms) |
|---|---|
| 80 ms / 120 ms | +2.4 dB |
| 70 ms / 150 ms | +2.1 dB |
| 65 ms / 120 ms | +3.3 dB |

The simulation reads the present case 2.6 dB higher than the render, so use it as a difference only. Predicted after 65 / 120: about 4-5 dB. That suits a measured tremolo, which is bow changes rather than staccato.

**Fix A (main track; `build/score_config.py`, `build/mix.json`, `tools/score_to_parts.py`).**
- MEAS_TREM notes end at 55 % of their slot (`MEAS_TREM["len_frac"] = 0.55`).
- Add to the Violoncellos `sus_release_cap_ms` list: `{"ms": 120, "dyn": ["Stac", "Hrd"], "rows": ["Stac RRx9", "Stac On Bow RRx9"]}`.
  - `cap_release()` matches the last word of the group name before " rr": "Vc Stac rrx1" -> "Stac", "Vc Stac Hrd rrx1" -> "Hrd". The default mf / f / ff matches nothing.
  - Check that the build log lists "Vc Stac" and "Vc Stac Hrd".
- Then the short-row velocity change: `SHORT_CC11_PARK = {"rows": ("Stac", "Staccatissimo", "Stac On Bow", "Spiccato"), "cc": 120}`.
  - CC11 holds 120 from the run's keyswitch to the next non-short note.
  - REP_SPLIT `stac_vel` becomes `[(22, 26), (34, 30), (46, 40), (58, 50), (72, 62), (88, 76), (114, 92), (124, 104)]`.
  - At f this moves the celli Stac strokes from the 90-104 layer to 69-89.
- Velocity offsets:
  - No beat offsets on MEAS_TREM notes.
  - 0 / -10 / -5 / -10 (±4 seeded) on the written 16ths at 516-520.
  - -10 on off-beat eighths of the fugato staccatos.
- Match levels per bar in the volume envelope after the render. The park adds +3.0 dB at CC11 88, and the softer layer takes some of it back.
- **Pass:** dip median 4 dB or more on 464-480 and 516-520; per-bar level within 1 dB after the trim; the 480-484 crescendo still grows.

**Fix B (pass-2 test alias, the patch the library has for this figure).**
- **Build:** "Vc meas trem", a TEST_TRACKS alias of Violoncellos.
  - Window (463.9, 484.0).
  - `"globals": {"MEAS_TREM": {}}`, so the five G2 whole notes stay whole notes.
  - `"tables": {"ART_SPANS": {"Violoncellos": [{"from": 463.9, "to": 484.0, "art": "Meas Trem TS"}]}}`.
  - CC11 from the printed curve as on the main track. Velocity is ignored.
  - The five notes must stay five notes, each restarting at its bar line. If the same-pitch merge joins them into one 20 qn note, end each 0.02 qn early with NOTE_END_AT. The row is not Sus MAX, so AUTO_REBOW leaves it alone.
- **Measure against the main stem:**
  - The pulse period from the autocorrelation of the 1-4 kHz envelope at lags 0.08-0.3 s. Expect 0.119 s, i.e. sixteenths at 126 bpm, then slower through the 480-484 allargando.
  - The dip at each 16th grid point (dips50.py method).
  - Per-bar level, and growth over 480-484.
  - 2-5 kHz share.
- **Pass:** pulse within ±10 ms of the 16th grid, dips 3-6 dB, crescendo growth at least the main track's.
- **If it passes,** put the ART_SPANS row in the main Violoncellos track with MEAS_TREM off for 464-480. Fix A then remains for 483.5-484 and 516-520.

### 3. Re-bow holes that reach the master, and two long wind / brass notes that are not loop pulsing (level only, stem fix; measured)

**Re-bows.** On the c50 stems (`rebows44.py` method, plus the same harmonic band measured on the master):

| Re-bow | Stem dip | Master same-band dip | Stem re master band |
|---|---|---|---|
| Violoncellos 180.0 (pp before the dolce tune) | 7.9 dB | 6.1 dB | -6.1 dB |
| Violins I 44.0 | 6.0 dB | 4.9 dB | -2.1 dB |
| Violas 700.0 | 5.4 dB | 4.4 dB | |
| Violoncellos 41.38 | 8.9 dB | 2.9 dB | |
| Violoncellos 37.377 | 6.5 dB | 2.3 dB | |
| Violoncellos 26.516 | 7.0 dB | 0.8 dB | |

The basses' 9 steps of 3 dB or more are mostly inaudible:
- 470.813, 500.512, 506.408 (+9.7) and 512.159 sit 10-22 dB under the master in their band.
- 166.01 (-4.5) and 495.114 (-4.0) fall inside printed decrescendos, so they go the printed way.
- Only 38.003 (step -5.8 inside the 32-44 crescendo, master -1.1 dB) and 47.0 (dip 9.8) are worth a refit.

**Fix.** `tools/fit_rebows.py` on the c51 render with `--tracks Violoncellos,Violins I,Violas,Double basses`. Merge only these rows into `build/rebow_fills.json`, as c22 did: Violoncellos 180.0, 41.38, 37.377, 26.516; Violins I 44.0; Violas 700.0, 725.52; Double basses 38.003, 47.0, 506.408. Apply with `stem_fix.py`.

**Pass:** master same-band dip under 3 dB at 180.0, 44.0 and 700.0; stem dips under 5 dB; steps under 3 dB except where a hairpin prints them.

**Long wind / brass notes.** The c50 "0.56 at 3.95 s" on Bass clarinet 480 and Trombone 1 716 does not show a loop pulse.
- Both notes last 6.0-6.1 s. A 5.3 s analysis window holds the 3.95 s lag only once, so that autocorrelation means little.
- The folded level peak-to-peak at 3.95 s is the same as in c49: Bass clarinet 2.7 -> 2.8 dB, Trombone 1 4.0 -> 4.3 dB.
- What the scan caught is a single step on each note:
  - **Bass clarinet 480.** The level falls 3.5-4.3 dB at the fff arrival (484, +2.08 s) and stays down (c49 -4.4). The fall is written in the volume envelope: `vol_db` +6.1 dB at 483.5, +1.0 at 483.95, +2-3 after, while CC11 rises 122 -> 124. The crescendo's dB gain is released on a note held across its arrival. Hold it to the next onset (491.94), or add `LEVEL_SHAPES["Bass clarinet"]` [(483.7, 0), (483.75, +4), (491.85, +4), (491.94, 0)]. It sits 14.8 dB under the master, so this is low priority; the same release may affect other notes held across an arrival (critic C's lens).
  - **Trombone 1 716.** The level falls 2 dB at +1.8 s against a nearly flat written envelope (-5.8..-6.0 dB; CC1 falls only 27 -> 24), so I infer a sample seam. A `loop_fills.json` lift of +1.5 dB from +1.7 s to the note end. pp final bars, 9.4 dB under the master.

### 4. The bass clarinet's bite came back when its 2.5 kHz shelf was dropped (c51 EQ, on the stem; measured)

**Measured** (Bass clarinet stem, every note of 0.4 s or more, body 0.15-1.5 s, bands relative to 0.5-2 kHz, c49 -> c50):

| | 2-5 kHz | 5-10 kHz |
|---|---|---|
| Loud notes | -11.4 -> -7.4 dB | -33.0 -> -20.4 dB |
| Soft notes | -13.5 -> -8.6 dB | -39.8 -> -26.3 dB |

- 2-5 kHz attack (first 80 ms) minus body on loud notes: median -3.1 -> -1.3 dB, maximum +3.0 -> +4.8 dB.
- Control, Clarinet 1 through the same family EQ: 2-5 kHz -8.4 -> -8.8 dB, 5-10 kHz -38.0 -> -32.4 dB.
- So the bass clarinet is now brighter relative to its body than the soprano clarinet: +4 dB in 2-5 kHz, the size of the dropped shelf, and +12.6 dB in 5-10 kHz.

**Why the stacking argument does not hold.** The worry was that the shelf would stack to about -8.5 dB at 2-4 kHz with the woodwind family EQ. But the family EQ also cuts the body (-5.1 dB at 447 Hz, -3.1 at 1 kHz), so measured against the body, the shelf only restores the c49 balance.

**Where it is heard.** The bass clarinet's exposed solos, bars 77 (qn 304.5) and 107 (424.5).

**Fix.**
- Restore the Bass clarinet's 2.5 kHz high shelf at -4 dB in `build/mix.json`, after the family EQ (the c21 anti-bite fix, on the do-not-touch list until c50).
- Apply it to the rendered dry stem with `cycles/c50/actor_scripts/eqfix50.py`. R Winds is low-passed at 2.3 kHz, so the return hardly changes.
- If 5-10 kHz is still above -28 dB re body, add a -3 dB shelf at 6 kHz.
- **Pass:** 2-5 kHz re body within 1 dB of c49 (-11.4 loud); attack minus body median -2 dB or lower.

### 5. Coda bass pedal: retry Marc Sus LITE in the f attack layer, with a lead (two pass-2 test aliases; measured, effect inferred)

**Where.** Double basses, f C2 eighths 664-675.5 (bars 167-169).

**Measured.**
- c50 main track: downbeat minus off-beat front (40-300 Hz, first 80 ms) -5.5 dB median. Downbeat peak at +136 ms, off-beat at +24 ms. This happens despite the c48 shapes.
- The other basses pedals do not show it: 104-124 +1.9 dB, 520-536 +2.6, 556-568 -0.5, with identical MIDI on and off the beat. So the coda's weak downbeat stroke is the sample's bow-direction round robin, as c48 found.
- c50 "Cb pedal M" at v45 (mp attack layer): front -3.5..-9.4 dB, pcX +58 ms; failed.

**Inferred.** The Marc Shrt attack in the 61-102 layer is the f recording, with a 34 ms AHDSR attack and no velocity-to-volume (patch). It should speak earlier and louder than v45 did. A 0.04 s lead covers most of the +58 ms.

**Build** (copy the c50 block, `rendered_build_pass2/score_config.py` near line 3470):

```python
_CBF = lambda vel: [{"from": float(q_), "to": float(q_) + 0.01, "art": "Marc Sus LITE", "vel_by_cc": [(88, vel), (114, vel + 10)]} for q_ in range(664, 676)]
ALIAS_TRACKS["Cb pedal F1"] = {"source": "Double basses", "windows": [(613.5, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP},
                               "tables": {"ART_SPANS": _CBF(75), "RETONGUE_LEADS": {"Double basses": {float(q_): 0.04 for q_ in range(665, 676)}}}}
ALIAS_TRACKS["Cb pedal F2"] = {"source": "Double basses", "windows": [(613.5, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP},
                               "tables": {"ART_SPANS": _CBF(92), "RETONGUE_LEADS": {"Double basses": {float(q_): 0.03 for q_ in range(665, 676)}}}}
```

- 664, the run's first note, needs the same +0.04 / +0.03 s through whichever table its path reads. Check with `cycles/c48/actor_scripts/realised48.py` that all 12 leads are realised.
- `alias_check.py` must say OK apart from the keys under test.

**Pass** (as c50, measured with `cycles/c49/actor_scripts/pedal49.py`):
- Downbeat front minus off-beat at least +0.5 dB on 9 of 12.
- Downbeat pcX within ±30 ms.
- 2-5 kHz front at most 2 dB over the off-beats'.
- Adjacent off-beats within 1.5 dB.

If one passes, move its ART_SPANS rows and leads to the main track, refit the pedal's level shapes, and do the same on no other pedal (the others already lean the right way).

### 6. The CC1-only "Mod + Expression Combo" test, staged as asked (pass-2 test aliases; patch read, predictions inferred)

**What the patches do now** (read):
- **Strings KS Masters.** CC11 crossfades five dynamic layers and drives the Global Group volume. CC1 crossfades Non Vib / Vib / Molto Vib (tables in the manual notes). Our string CC1 runs 38 (ppp) to 100 (fff); espr. / dolce boosts set 95-105.
- **FL, OB, EH, BS and CB KS Masters.** CC1 crossfades Non Vib and Vib between 55 and 76 (LEARNINGS 3). Melodic winds hold CC1 100.
- **Brass and Clarinet KS Masters.** CC1 already carries the dynamic layers (CC1_DYN_MAP, 2-6 units under CC11). The macro would change almost nothing there, so test strings and a double-reed solo only.
- **No installed patch has a macro,** so emulate it in MIDI. Opus's macro drives controller_1 and controller_11 from one lane, linearly (FINDINGS section 6). Sending a CC1 lane identical to the CC11 lane gives the same result with no Opus-state work. A non-linear target map becomes a table applied to that copy.

**Tool** (new generic option in `tools/score_to_parts.py`, applied after the CC lanes are sampled):

```python
CC1_FROM_CC11 = {}   # {track: None | [(cc11, cc1), ...]}: the CC1 lane becomes the CC11 lane (same breakpoints,
                     # pre-roll included), passed through the table; None = identity (EW's linear macro)
```

**Aliases** (TEST_TRACKS, pass 2; three instances, about 2-3 GB on a pass-2 project that settled at 19 GB):
- **"Vc macro":** source Violoncellos, window (135.0, 219.3), rest to rest (128.5-135.49 and 218.91-219.8).
  - `"globals": {"CC1_FROM_CC11": {"Violoncellos": None}}`.
  - Covers p 136, the crescendo to f 156, sf 160, pp 168 and the mf dolce tune 183-216.
  - Through the tune, CC1 goes from 95-105 to 72-84, so Molto Vib drops from about 1.0 to 0.26-0.5.
- **"CA macro L":** source Cor anglais, window from 18.0 to the first rest after 35.0 (the espr. solo of bars 5-9).
  - `{"Cor anglais": None}`.
  - CC11 here is 42-73, so 4 of 6 long notes sit in the 55-76 zone where both layers sound.
- **"CA macro S":** the same window with the plan's remedy, a map that crosses 55-76 in four CC11 units.
  - `{"Cor anglais": [(0, 0), (54, 54), (58, 77), (127, 127)]}`.
  - p notes (CC11 42-54) then play Non Vib only. mp-mf notes (59-73) play Vib only at CC1 78-88.
- `alias_check.py` must say OK apart from cc1.

**Measure** (test stem against the main stem of the same c51 render, every note of 0.9 s or more in the windows):
- **Vibrato / amplitude modulation:**
  - Band envelope (CA 1.5-4 kHz, celli 0.5-2.5 kHz; 5 ms hop, 30 ms window) over onset + 0.3 s .. end - 0.15 s, detrended with a 2nd-order fit.
  - Report its p95-p5 in dB, and the 4-7.5 Hz share of the 1-15 Hz modulation spectrum.
  - c50 baselines: CA 6 notes, median 6.0 dB, share 0.47; celli 136-219, 18 notes, median 4.5 dB, share 0.32.
- **Per-note level** (whole band, same span), test minus main.
- **Spectral centroid** per note.
- **Legato joins:** both-pitches-within-6-dB window, dips and pcX (`cycles/c41/actor_scripts/legtest.py`).

**Pass ("no worse", plan section 5):**
- Amplitude-modulation median within +1.5 dB of main, and no note over +3 dB (the doubling check, section 6). c17 measured +6.4 dB on a ff flute held at CC1 67.
- 4-7.5 Hz share on espr. / dolce notes at least 0.6 × main (vibrato kept where the score asks for expression).
- Per-note level within ±1.5 dB after removing the median offset.
- No new join dip of 5 dB or more; pcX within ±20 ms.

**Predictions (inferred).**
- CA L fails the doubling check.
- CA S fails the vibrato check on the p espr. notes (27, 31.3).
- Vc macro gives a thinner vibrato on the dolce tune. It passes or fails on the vibrato share.
- Whatever the result, record it in loop/LEARNINGS.md. Adopting the macro on every track belongs to the next round, not to c51.

**Do not touch:**
- GENTLE_ACCENT and the accent fits. c50 accent 2-5 kHz front minus body: strings -2.4 / winds -2.4 dB median against c49 -2.2 / -3.5; brass -16.3.
- Keyswitch placement: 0 clashes, none within 0.005 qn.
- No chords on legato rows.
- The violins' and violas' 50 % staccato lengths and STAC_LEAD_S.
- The celli Sus Marc LITE strokes 84 / 448 / 456.
- The wind and brass re-tongue gaps and REP_ROW rows.
- `LEG_MIN_GAP_S`, the leg / entry / retongue lead tables and JOIN_NOTCH.
- The trombone 4 kHz shelves.
- The 150 ms mf-ff / 350 ms p release caps and the basses' 600 ms pp cap.
- The c48 coda pedal shapes on the main track, until an alias passes.
