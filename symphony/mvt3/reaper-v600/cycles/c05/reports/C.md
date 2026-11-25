# Cycle 5, critic C (blend and space) on the c04 render

Render under review: `cycles/c04/render` (the master is the float sum of the 31 stems) and `cycles/c04/rendered_build/parts.json`. For comparison I used c02 (no release caps; its parts are `cycles/c03/before/parts.json`), c03, Movement I c45, the Dvořák 9/i MP3 (decoded) and the stored Brahms 1/i, 4/i, 1/ii, 4/ii metrics (`symphony/render/critics/c00|c04/ref_*/metrics.json`). Scripts were numpy and soundfile only, at 48 kHz. Stereo used STFT 4096 / hop 2048; levels used 30 ms frames with a 10 ms hop. My band correlations reproduce Movement I c45's published numbers (0.564 below 250 Hz and -6.3 dB side/mid, against the reported 0.57 and -6.3), so the two sets can be compared. Each judgement is marked measured, simulated (applied to the c04 stems in the STFT domain) or inferred.

## Manual notes (cycle 5, slot C: May 2021 HO manual pp. 68-74, Hollywood Harp)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| The harp's mic set is designed for a solo instrument, with vintage close and mid positions in place of the surround mics (p.68) | Harp track: mix.json harp group Close 0.6 / Main 1.0, width 0.3, seat -0.72 | Yes. Harp stem 250 Hz-4 kHz correlation 0.59, R-L -4.4 dB: placed left and wider than the woodwinds. No problem found. |
| Sustain RR alternates Pluck Long and Thumb Pick by round robin at v1-123 (5 dynamic layers each) and plays Nail Pick at v124-127 (p.69) | Harp Sus RR is the harp's patch. Velocities in parts.json: 46-116 for 311 notes, and v126/127 on the six-note chord at qn 524 (bar 132, ff, accent, "non arpegg.") | Yes. The qn 524 chord plays nail picks, which p.70 calls "a stronger note than conventional harp plucks", the right colour for an accented ff chord. **MANUAL-GAPS.md line 200 ("no nail picks") is carried over from Movement I and is out of date for the Finale.** |
| Harmonics: hollow and transparent, fundamental missing, upper partials only (p.70). Available as `Harp Harmonics.oib`, as the Harmonics row of the Harp KS Master, or in Angels Harmonics at v123-127 (p.69) | Bars 43-47 (qn 168, 176, 184), p, "harm. (sound 8va)" | **No.** HARM_ON_TRACK plays the three notes as ordinary Sus RR plucks at sounding pitch (B flat 4, v46). Pitch is right, colour is wrong (finding 4). |
| Gliss performances are mapped to white keys by scale (pp.71-74); Gliss Technique gives separate notes so the timing can be controlled (p.70) | Bar 277 glissando (qn 1106-1108, f to ff) | Written out on Sus RR by GLISS_SPANS (C-D-E-G-A, G3 to E6). That is a valid route. None of the pre-mapped glissandi starts on the bar's pentatonic set, so the written-out version is the better choice. Follows the manual. |
| Repetition Rep lets earlier notes ring through fast repeats (p.71) | No fast same-pitch harp repeats in the Finale | Not needed. |
| Keyswitch (KS) Master (p.74) | Not used | The KS Master would put Harmonics on the same track, but it reaches down only to MIDI 36 and its keyswitches 21-35 overlap the harp's low notes (kit LEARNINGS, c00). The Finale's harp needs D1 (MIDI 26, "low D string"), so the KS Master is not an option. |
| Étouffez (not a manual item; HARP_RING_S and env_release_ms 200) | qn 326, 520, 968, 1113 | Works (measured): the harp stem falls 17-21 dB in 0.15 s and 26-32 dB in 0.3 s after each mark. |

From MANUAL-GAPS.md, nothing else falls under my lens this cycle. The Mid mic row stays unused, and was rejected in c01 (C #3b).

## Verdict on the hall: not too dry. Keep fx_volume 0.095 and the c03 envelope (measured)

Tutti stops were measured with the references' own detector (rtk `cutoff_decays`: 30 ms frames, a 0.4 s hold, then at least 15 dB of fall within 0.4 s; 12 dB for the Dvořák):

| | Stops | Time to -10 dB | Time to -20 dB | RT60 from the -5..-20 dB slope |
|---|---|---|---|---|
| c04 | 5 (1.7, 7.3, 36.2, 244.3, 421.6 s) | 0.24-0.34 s (median 0.31) | 0.42-0.54 s (median 0.49) | 1.01-1.39 s (median 1.28) |
| c02 (wetter: no IR envelope, no caps) | 4 | median 0.23 | median 0.45 | median 1.43 |
| Brahms 1/i (stored, from Movement I c45 C) | 12 | | 0.43-0.55 (median 0.485) | 1.13-1.62 (median 1.33) |
| Dvořák 9/i | 1 | 0.31 | 0.55 | 1.32 |

- The Finale's tutti stops fall exactly as fast as Brahms 1/i does (median 0.49 against 0.485 s), and the decay slope is inside the recorded range.
- The final chord (421.6 s) has the shortest slope, 1.01 s. Measured from the note-off, its master tail still takes 0.73 s to fall 20 dB, so it does not stop short.
- **What does sound dry is the soft string phrase ends** (finding 1), and the hall does not cause that. At qn 198.88 (bar 50, the strings' pp chord into the rest before the Poco meno mosso), the master's fall of 10 dB took 0.32 s in c02 and takes 0.08 s in c04. The hall return was 0.095 in both renders. What changed in between was the release cap (c03, extended in c04).
- Raising fx_volume to 0.12 would move the tutti stops to the wet end of the range (inferred: about +0.03 s to -20 dB). It would add perhaps 0.5 dB of side/mid (inferred by scaling Movement I's 1.7 dB per 6 dB of hall return). It would not fix the abrupt soft ends, because the samples' releases stop them before the hall can take over. Do not raise it.

## Findings, ranked by what a listener would gain

### 1. Soft string phrase ends stop abruptly: the 150 ms release cap is right at f-ff but too short at pp/p (measured; cap values inferred)

**Where.** Every pp/p bowed phrase end in the five string sections. Clearest are qn 198.88 (bar 50: Violins I Sus MAX pp, Violins II and Violas Leg Slur pp/ppp, the end of the poco rit. before the second theme), 454.86-455.86 (bar 114, the pp chord before the bassoon solo), 477 and 489 (bars 120 and 123, the 4 soli), 551.86 (bar 138, ppp) and 679.86 (bar 170, p, before the recapitulated second theme).

**Evidence (coordinator's check). Time to fall 10 dB and 20 dB after the note-off, per stem.** L0 is the power mean over the last 0.25-0.04 s of the note. Phrase ends are the last sounding note followed by at least 0.7 s of rest; pizzicato is excluded.

| Stem, pp/p ends | c02 (no cap): -10 dB / -20 dB | c04 (cap 150 ms incl. legato rows): -10 dB / -20 dB |
|---|---|---|
| Violins I (6) | 0.29 s / 0.42 s | **0.07 / 0.12** |
| Violins II (5) | 0.32 / 0.51 | **0.08 / 0.17** |
| Violas (2) | 0.11 / 0.31 | **0.06 / 0.15** |
| Reference | soft ends 0.20-0.40 s to -10 dB | phrase ends 0.43-0.58 s to -20 dB |

| Stem, f-ff ends | c02 | c04 |
|---|---|---|
| Violins I (11) | 0.15 / 0.30 | 0.09 / 0.22 |
| Violins II (9) | 0.21 / 0.32 | 0.14 / 0.22 |
| Violoncellos (5-7) | 0.29 / 0.53 | 0.26 / 0.58 |

- Without the cap, the soft ends sat inside the reference ranges. With it, they fall 10 dB in 60-140 ms, three to four times faster than the references. On the master at qn 198.88 the whole orchestra drops 10 dB in 0.08 s, which a listener hears as the strings being switched off.
- Two ends prove the cause. The one uncapped row in the table, Violins II Flautando at qn 390.86 (p), still falls 10 dB in 0.32 s and 20 dB in 0.48 s, inside the references. The f-ff ends are tutti cut-offs, and on the master they already sit in the reference range (verdict above), so the cap is right there.
- The cello legato ends (0.58 s to -20 dB) are still the slowest. That is the open item from c04, not the cap.

**Fix.** Use a cap per dynamic layer. `tools/build_reaper.py cap_release`: accept `"ms"` either as a number or as a dict keyed by the group's dynamic word (the `words[-1]` it already reads). For example: `ms_ = spec["ms"].get(words[-1], ...) if isinstance(spec["ms"], dict) else float(spec["ms"])`. Keep the stderr print showing each value. This rule is generic, so it goes in `tools/` with the number as the default.

In `build/mix.json`, on Violins I, Violins II, Violas, Violoncellos and Double basses, set `sus_release_cap_ms` to `{"ms": {"pp": 500, "p": 500, "mf": 300, "f": 150, "ff": 150}, "dyn": ["pp","p","mf","f","ff"], "rows": [unchanged six rows]}`.

The 500 ms at pp/p is inferred from two data points. The c04 cap of 150 ms gives a soft time to -10 dB of about 0.47 x the release and a time to -20 dB of about 1.0 x. The shipped soft releases (up to 931 ms) gave 0.29-0.32 s. So 400 ms (Movement II) would land near 0.19 / 0.40 s, just under both reference floors, while 450-500 ms lands at about 0.21-0.24 / 0.45-0.50 s. The mf value of 300 ms matches Movement II. The cap never lengthens a release, so groups shipped under 500 ms are unchanged.

This is an Opus state change, so the five string tracks must be fully rebuilt.

**Check.** The pp/p ends listed above should fall 10 dB in 0.20-0.40 s and 20 dB in 0.43-0.58 s on the stems. The master at qn 198.88 should take at least 0.2 s to fall 10 dB. The tutti stops (detector) should stay at 0.43-0.55 s to -20 dB. S1 repeated-note dips should stay as in c04 (the soft-layer caps sit under the repeat notches only at pp/p).

### 2. The image is still narrower than every reference in 250 Hz-4 kHz and above 4 kHz, because of the brass. The c04 width change barely reached them (measured; fix simulated)

**Evidence (master).**

| | Correlation < 250 Hz | 120-250 Hz | 250 Hz-4 kHz | > 4 kHz | All | Side/mid |
|---|---|---|---|---|---|---|
| c03 | 0.784 | 0.750 | 0.689 | 0.655 | 0.689 | -7.3 dB |
| c04 | **0.551** | 0.470 | **0.663** | **0.645** | 0.634 | **-6.5 dB** |
| Movement I c45 | 0.564 | 0.513 | 0.638 | 0.531 | 0.618 | -6.3 dB |
| Dvořák | 0.554 | 0.546 | 0.561 | 0.412 | 0.546 | -5.3 dB |
| Brahms ×4 (stored) | 0.54-0.62 | | 0.47-0.54 | 0.38-0.48 | 0.49-0.55 | -4.7..-5.4 dB |

- c04 fixed the bass: correlation below 250 Hz went from 0.78 to 0.55, inside the references. The low band is now if anything slightly wide: side/mid below 250 Hz is -4.5 dB against the Dvořák's -5.0. **Do not widen the celli, basses, tuba or contrabassoon further.**
- Above 250 Hz almost nothing moved (0.689 -> 0.663, 0.655 -> 0.645), and side/mid is 0.5 dB short of the -6 dB target and 1.1-1.8 dB short of the recordings.
- **Cause (measured per stem).** The brass carry about 38% of the 250 Hz-4 kHz energy and 34% of the energy above 4 kHz, and they are the most correlated loud stems. At 250 Hz-4 kHz: Horns 2-4 0.79-0.80, Trumpets 2/3 0.83/0.78, Trombones 1/2 0.81/0.70, Bass trombone 0.74. Above 4 kHz they read 0.86-0.91, against Violins I 0.43 and Violins II 0.67.
- c04's Main 0.35 widened them only a little (Horns 2-4 at 250 Hz-4 kHz went from 0.88-0.89 to 0.79-0.80, trombones by 0.03-0.05). The reason is that `width_by_mic` never narrows and the horn, trumpet and trombone widths were already 0.3 (loop/LEARNINGS c04). The Finale carries more brass than Movement I, so the same values leave it narrower.

**Simulation (c04 stems, side raised on Horns 2-4, Trumpets 2-3, Trombones 1-2 and Bass trombone; Horn 1, Trumpet 1 and Tuba unchanged).**

| Side gain | < 250 Hz | 250 Hz-4 kHz | > 4 kHz | Side/mid |
|---|---|---|---|---|
| c04 | 0.557 | 0.667 | 0.642 | -6.51 dB |
| +2 dB (x1.25) | 0.553 | **0.600** | 0.614 | **-5.75 dB** |
| +3 dB (x1.41) | 0.551 | 0.552 | 0.594 | -5.25 dB |

- Raising the side of Violins II and Violas by 3 dB instead gave only -6.17 dB. The crash cymbals, +3 dB, gave -6.49.
- A plain side gain pushes off-centre seats outward (Horn 1 at +3 dB: R-L at 1.25-4 kHz -8.6 -> -11.9 dB). The Opus Main-pair spread does not do this: Movement I c45 moved its outermost seat 1.7 dB toward the centre. So use the spread, not a side EQ.

**Fix.** `build/mix.json`: groups horn, trumpet, lowbrass `width_by_mic` {"Main": 0.35} -> {"Main": 0.5}. Keep the track entries Horn 1 and Trumpet 1 at {"Main": 0.2}. Add Tuba {"Main": 0.35} as a track entry so its low band does not widen. That makes 8 tracks change Opus state (Horns 2-4, Trumpets 2-3, Trombones 1-2, Bass trombone), all fully rebuilt, with no new instances and no memory cost.

Inferred: Main 0.5 corresponds to about +2 dB of side on these stems, giving side/mid about -5.8 dB and 250 Hz-4 kHz correlation about 0.60.

**Check.** Master side/mid -6.0 to -5.3 dB, 250 Hz-4 kHz correlation at or below 0.62, below 250 Hz still 0.54-0.62. Per-stem stereo-power levels within 0.2 dB. Brass seats at 1.25-4 kHz within 1.5 dB of c04 (Horn 2 -7.6, Horn 3 -6.3, Horn 4 -5.3, Trombone 1 +5.2, Bass trombone +6.0 dB R-L).

### 3. The "4 soli" of Violins I (bars 119-128) is the widest string sound in the piece; four players should sound narrower than sixteen (measured; fix simulated)

**Where.** qn 473-511, Violins I, "4 soli", played by the full 1st Violins section at the half-section cut (`SOLI_AS_META`).

**Evidence.** Violins I stem correlation 0.39 and side/mid -2.3 dB in the soli. The same section reads 0.46 / -2.9 dB in the tutti (600-664) and 0.46 / -2.7 dB in F2 (264-328). Movement I c40's DIV A half-section read 0.85.

**Fix (no pass 2).** Use `side_shelf_switched`, which is still supported in `tools/build_reaper.py side_lua` (Movement I c35). Violins I: `"side_shelf_switched": {"points": [[472.5, 0], [473, 1], [511, 1], [511.5, 0]], "bands": [{"band": "lowshelf", "hz": 20000, "db": -3}]}`, a broadband -3 dB on the side only.

Simulated on the stem: correlation 0.39 -> 0.72, seat R-L -8.5 -> -6.8 dB, level -0.9 dB. A -6 dB cut gives 0.87 but moves the seat 3.5 dB, so do not use it. Return the level with a roles.json Violins I [473, 511, +1].

The switch acts after the hall, so it narrows the hall share of this stem too. That is acceptable for a soft, short passage (inferred). The closer patch is still a DIV A half-section in a pass 2 (MANUAL-GAPS #7, A #6), when one is built.

### 4. Harp harmonics at bars 43-47 sound as ordinary plucks (measured in parts.json; colour inferred from the manual)

**Where.** qn 168, 176, 184, harp, p, "harm. (sound 8va)", over the B flat pedal of the transition, with motive x in the winds.

**What is wrong.** HARM_ON_TRACK plays the three notes on Harp Sus RR at their sounding pitch (70, v46, 6.6 qn). Manual p.70 describes the harmonics as hollow and transparent, with no fundamental, and says they blend with pizzicato and soft strings. A plain pluck at B flat 4 is a full, rounder note that stands out more from the soft winds.

**Fix.** Small and optional. It needs a separate instance on `Harp Harmonics.oib` (range 48-96, sounding pitch, about 0.55 dB per velocity step; kit LEARNINGS c01/c08). That means either a pass-2 track or a temporary main-pass swap if any instance is ever freed. The Harp KS Master and Angels Harmonics cannot replace Sus RR on the main track (KS range, and gliss technique at v1-122). Rank it after anything that needs no new instance.

### 5. No low-end build-up; leave the bass instruments alone (measured)

- **Band shares, whole master, c04.**

  | Band | c04 | Brahms ×4 | Dvořák |
  |---|---|---|---|
  | 20-100 Hz | -15.2 dB | -7.9..-8.9 | -21.6 |
  | 100-250 Hz | -9.2 | -7.1..-8.8 | -6.8 |
  | 250-500 Hz | -6.5 | -6.0..-7.1 | -6.3 |
  | 500-2000 Hz | -2.5 | -3.7..-4.4 | -3.4 |

  There is no 200-500 Hz build-up. 100-250 Hz is if anything 0.4-2.4 dB lighter than the references. The mockup's extra weight is at 500-2000 Hz, and that is lens B's balance question, not a mud problem.
- **Loud frames (top 10%).** 20-40 Hz is -35 dB of the total (Movement I c45 -46). The bass drum carries 98% of it (ff at 223 and 278-279, as printed). At 40-60 Hz the basses carry 78% and the contrabassoon 8%. At 100-250 Hz the timpani (15%), tuba (17% at 100-160) and basses (27-36%) share it.
- Loud frames carry less 40-60 Hz than soft ones (-28.0 against -23.8 dB), as recordings do (kit LEARNINGS c20).
- The references disagree with each other by 13 dB at 20-100 Hz (the Dvořák is a lossy MP3), so nothing here justifies a cut. Inferred: the bass drum's sub-bass is the printed ff, and a real drum has it.

### 6. Muted trumpet against cor anglais (bars 171-186): matched, keep (measured)

In the qn 680-744 unison:

| | Trumpet 1 (Mute Sus + 250-8000 Hz band-pass) | Cor anglais |
|---|---|---|
| Level | 22.6 dB | 23.7 dB |
| Centroid | 1089 Hz | 919 Hz |
| 2-5 kHz share | -15.8 dB | -15.2 dB |
| Above 5 kHz | -46.4 dB | -41.5 dB |
| R-L | +1.3 dB | +3.5 dB |
| Stem correlation | 0.89 | 0.75 |

- The two are within 1 dB in level and 2-5 kHz colour and sit 2 dB apart in the image: one blended line.
- The muted tone is not darker than Trumpet 1's own open p solo (200-264: 2-5 kHz -14.2, above 5 kHz -45.1 dB), so the mute band-pass does not dull it.
- On the envelope at the note level, the two attacks agree on 18 of 24 shared onsets (6 differ by more than 60 ms; that is lens A/S2's question).

## Measured and working

- The final fermata tail: 0.73 s to -20 dB on the master.
- Étouffez damping: 17-21 dB in 0.15 s.
- The harp's place and width, and the nail picks at qn 524.
- One hall: every tutti stop's slope is within 1.01-1.39 s.

**Do not touch:** fx_volume 0.095, low_cut_hz 160 and ir_setup {2, 0.5, 0.5} (tutti stops at 0.42-0.54 s to -20 dB, Brahms 0.43-0.55); the 150 ms string cap at f/ff (only add the pp/p and mf values); the c04 bass width (Vc/Cb Main 0.45, side-only low cuts at 0; below 250 Hz 0.551 is in range); Horn 1 and Trumpet 1 at Main 0.2; the muted-trumpet band-pass and its seat; the harp's env_sustain 1.0 / env_release_ms 200 / HARP_RING_S 2.0 and the written-out bar 277 glissando; the loud-span low EQ (no low-end build-up against the references).
