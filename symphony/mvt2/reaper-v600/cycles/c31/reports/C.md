# Cycle 31, critic C: tempo, timing and transitions (on the cycle 30 render)

Material: `cycles/c30/render` (master and 32 stems after the c30 stem fix; the fix changed levels only), `cycles/c30/metrics`, `cycles/c30/rendered_build/parts.json` (the data the render was made from; all qn->s conversions use its tempo map), `build/{early_fills,entry_leads,leg_leads}.json`, `build/score_config.py`, `tools/score_to_parts.py`, `build/global.ily`, `build/mockup-events.tsv`. I ran `score_to_parts.py` once with `STP_DEBUG_VOL` and wrote its output to my scratch folder only (to read the volume items on Vln I 171).

Methods, all measured from the score onset (`sq`) on the tempo map:
- Entry timing: 5 ms stereo-power envelopes, 20-50 ms smoothing. The body is the level over +0.4..+0.9 s. b-6 and b-3 are when the stem first reaches body - 6 dB and body - 3 dB. Entries are notes after at least 0.45 s of silence on the track and at least 0.6 s long (128 entries).
- Legato and arrival timing: 4096-point STFT with a 5 ms hop. Crossover is when the new pitch's harmonics 1-4 (±3%) overtake the old pitch's and stay ahead for 60 ms. Rise is when the new pitch reaches its own body - 6 dB. This covered 911 joins on 17 tracks.
- Fill simulation: the `early_fills.json` dict shape (0 at onset - 0.02, +db at the onset, held to + hold_s, 0 by + hold_s + 0.25 s), added to the measured envelope. I report b-6, b-3 and the 50 ms peak over the body in the first 0.6 s.

## Manual notes (T1, May 2021 HO manual PDF pp. 143-146)

| What the manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Performance scripts by CC: CC5 legato/portamento time, CC15 con sordino, CC22 mono/poly, CC36 round-robin reset, CC57 legato script, CC65 portamento script, CC69 repetitions, CC70 finger position (p.143 table) | every Opus track | Yes. The pipeline sends CC15, CC36 and CC69 (pre-roll) and CC70 (strings). CC5, CC57 and CC65 only drive the emulated legato and portamento scripts (p.143-144), and the mockup uses the true-legato rows instead, so it correctly sends none of them. |
| Monophonic True Legato: note velocity sets the transition time. About 50-60 gives a longer transition "allowing the melody to breathe", 110-127 a shorter one, and velocity does not change loudness (p.144) | every legato target | Partly. `build_reaper.py` sets `legato_speed_active = True`. Targets play at v124 (v108 at the climax 204-210, v90 in the soft coda). That gives tight transitions: string crossover medians are +0.005..+0.025 s (measured). The slower "breathing" setting is not used on the cantabile lines (MANUAL-GAPS #6). If it is tried, the leads must grow by the extra transition time, or arrivals will land later than they do now. |
| CC22 0-63 polyphonic, 64-127 monophonic; disabling mono risks unwanted transitions (p.144) | legato rows | Yes. CC22 is never sent, so the rows stay monophonic, and divisi and chords are split onto other tracks. |
| Con sordino on CC15 (p.144) | strings (bars 15-30, coda), Horns 3/4 coda | Yes (measured in parts.json). Every CC15 change sits in a rest, 0.58-0.69 s after the track's last note. The shortest time to the next muted entry is 6.2 s (Violas, 279), and no change falls under a sounding note. |
| The Repetition script detunes or borrows neighbour samples at random; RR reset is the consistent choice (p.145) | strings | Yes. CC69 is set to 0 on the strings in the pre-roll, which keeps attack timing repeatable. |
| RR reset on CC36, any value (p.145) | every track | Open. The installed Preferences use CC16, and the 2025 manual (p.92) wins (MANUAL-GAPS #10). Not a timing issue: attack times repeat from render to render. |
| Finger position on CC70: 0-38 FP1, 39-76 FP2, 77-114 FP3, 115-127 FP4; the setting is only a preference where the note allows it (p.146) | the "sul A/D/G" spans | Values 0, 20 and 127 are in range. One timing observation for the T2 reader: "sul A" is printed on the Vln I pickup at 171, but CC70 goes to 127 only at 171.817 (just before bar 53's moved onset). The pickup itself plays on CC70 20, and so does Vln II at 171.79. Whether FP4 is the A string for C5 needs the tables on pp. 147-149. |

## Where c30 stands on this lens (measured)

- **Tempo map.** It follows `global.ily` closely. Bar means:
  - Bars 35-36: 49.2 / 45.0.
  - Bars 47-48: 58.0 / 54.0. Bars 49-52 run at 52.3-52.8 against the printed 54, from the phrase arcs.
  - Animando bars 53-59: 60.0, 60.2, 60.7, 61.2, 61.7, 62.7, 64.0.
  - Bar 60: 63.75 down to 56.75, then the 0.22 s caesura.
  - Largamente bars 61-63: 53.2 / 53.2 / 54.0.
  - Bar 64 allargando: 45.0 against the printed 44.8 mean (beats 1-2 about 50, beats 3-4 about 42).
  - Tempo I: 52. Bars 78-82: 50.3, 48.7, 47.5 without the caesura, 45.9, 44.0. Bars 89-92: 48.4, 44.0, 39.9, then 36-37 and 20 on the last beat.
  - Total 348.2 s.
- **Keyswitches.** All 334 come before their notes; the smallest gap is 19.6 ms, and there are no clashes.
- **CC15.** See the table above.
- **Final fermata.** Bar 92 lasts 6.33 s. CC11 22 -> 8 over the last 1.1 s, and all seven sounding tracks release together at 348.23 s. After the release the master falls about 28 dB/s (RT about 2.1 s). The mp3 ends 1.6 s after the release, with the tail already under -100 dB, so nothing is cut audibly.
- **Entries, b-6 median.**
  - Harp: +0.005..+0.02.
  - Timpani: +0.06. That is TIMP_DELAY_S; the timpani play no exposed unison attack, so it does no harm.
  - Pizz. basses: 0.00.
  - Bassoons: -0.01.
- **Legato crossover medians.** Strings +0.005..+0.025; Horn 1 -0.003; Oboe 1 +0.060; Flute 1 +0.038; bass clarinet and Bassoon 1 +0.075 (p90 +0.16..+0.26).
- **Breaths.**
  - qn 204 (12 wind and brass staves): wind gaps 0.19-0.23 s. Stems dip 10-21 dB, but the master dips only 1.7 dB.
  - qn 268 (bar 81, 9 winds; the brief says "before bar 82", but qn 268 is bar 81's downbeat): stems dip 7-21 dB, master 2.9 dB.
  - qn 196 (BCl, Fl1, Hn1, Ob1): Fl1 and Ob1 gaps are only 0.095 s; master dip 2.7 dB.

## 1. Soft string entries and pickups still reach their level 0.25-0.47 s after the beat (S2; measured)

The leads are at or near the cap, so they now only move the quiet start of the sample earlier. Vln I 171 is audible at -14 dB from -0.15 s and still reaches body - 6 dB only at +0.35 s. LEARNINGS section 6 (c07, c23) gives the fix that works: lead plus a short fill. Most of these notes are exposed.

The worst place is **qn 139, the pickup into bar 45**, where the B flat minor head is played by Oboe 1 and the celli together. Oboe 1 reaches b-6 at **-0.080 s**, the celli at **+0.326 s** (b-3 +0.366). The two halves of one gesture are 0.4 s apart. The celli trace in dB from -0.2 s in 50 ms steps is -36, -35, -30, -25, -19, -11, -10, -12, -13, -12, -6, -3: it reaches body only at +0.4 s. The note is 1.12 s long.

**Vln I 171** is the pickup into bar 53 (a tempo, poco a poco animando; "sul A, cantabile"). It measures b-6 +0.348, b-3 +0.468, which is about the series-1 value (+0.34), and the probe has misread it as "early -0.14" since c24. Its front is also held down on purpose: a -4 dB role span (170.4-171.75) plus a -2 dB env item from 170.9 (`STP_DEBUG_VOL`).

Table (b-6 / b-3 now; then the proposed `build/early_fills.json` entry; then the simulated b-6 / b-3 and peak over the body):

| track, sq (bar) | now | proposed fill | simulated |
|---|---|---|---|
| Violins I 171 (52.75) | +0.348 / +0.468 | `"171": {"db": 5, "pre_s": 0, "hold_s": 0.15}` | +0.063 / +0.118, +0.9 |
| Violoncellos 139 (44.75) | +0.326 / +0.366 | `"139": {"db": 7, "pre_s": 0, "hold_s": 0.10}` | +0.056 / +0.101, +0.2 |
| Violoncellos 124 (41) | +0.226 / +0.421 | `"124": {"db": 6, "pre_s": 0, "hold_s": 0.20}` | +0.071 / +0.171, +0.5 |
| Violoncellos 152 (48) | +0.115 / +0.310 | `"152": {"db": 3, "pre_s": 0, "hold_s": 0.10}` | +0.065 / +0.120, -0.2 |
| Double basses 140 (45) | +0.299 / +0.369 (has 4 dB, hold 0.4) | replace with `{"db": 8, "pre_s": 0, "hold_s": 0.20}` | +0.004 / +0.174, +0.8 |
| Violins II 108 (37) | +0.142 / +0.282 (has 4 dB, hold 0.4) | replace with `{"db": 8, "pre_s": 0, "hold_s": 0.20}` | +0.092 / +0.122, +0.1 |
| Violins II 42 (15) | +0.136 / +0.306 | `"42": {"db": 4.5, "pre_s": 0, "hold_s": 0.10}` | +0.076 / +0.121, +0.8 |
| Violins II 59 (20.67) | +0.263 / +0.293 | `"59": {"db": 5.5, "pre_s": 0, "hold_s": 0.10}` | +0.043 / +0.083, +1.0 |
| Violins II 140 (45) | +0.179 / +0.274 | `"140": {"db": 3, "pre_s": 0, "hold_s": 0.20}` | +0.069 / +0.179, 0.0 |
| Violins II 286 (87) | +0.210 / +0.385 | `"286": {"db": 3.5, "pre_s": 0, "hold_s": 0.15}` | +0.070 / +0.105, -0.3 |
| Violoncellos div 62 (21.67) | +0.236 / +0.281 | `"62": {"db": 6.5, "pre_s": 0, "hold_s": 0.15}` | +0.061 / +0.141, +1.7 |
| Violas 78 (27) | +0.272 / +0.307 | `"78": {"db": 6.5, "pre_s": 0, "hold_s": 0.10}` | +0.037 / +0.107, +2.1 |

Leave the leads as they are. Violas 66, 238 and 279 are also late (+0.15..+0.19), but their body windows overlap the next note, so I could not size a fill with this window. Re-measure them with a +0.2..+0.5 s body.

After the render, check that the 50 ms peak in the first 0.6 s stays under body + 2.5 dB. Larger fills on soft first notes have overshot before (LEARNINGS section 6, c16-c17). Gain: these are the most audible timing faults in the soft half of the movement, and they are what Dan's S2 describes.

## 2. The bass of the Largamente downbeat (qn 204, bar 61) arrives 0.12-0.17 s late; Violins II lag Violins I (measured)

Arrivals at 204, b-6 / b-3 on each track's own pitch:
- On or before the beat: Flute 1 -0.005/0.000, Oboe 1 -0.015, Clarinet 1 +0.010, Bass clarinet +0.010, Bassoon 2 0.000, Contrabassoon -0.035, Horn 1 +0.040, Violins I -0.025/+0.080, Violoncellos -0.025/-0.015, Tuba +0.055.
- Late:
  - **Double basses +0.125/+0.190** (crossover +0.165)
  - **Bass trombone +0.165/+0.260**
  - **Oboe 2 +0.120/+0.175**
  - **Violins II +0.105/+0.130** (crossover +0.110, against Vln I +0.055)
  - Trombone 2 +0.080/+0.135
  - Horn 3 +0.085/+0.100

The ff chord after the caesura therefore starts with its top and middle, and the low end blooms in about 0.15 s later. That runs against the "molto sostenuto" weight the bar asks for.

Causes, read in parts.json and `score_to_parts.py`:
- **Double basses.** The 0.16 s `ABUT_LEAD` is not applied at 204, 152 or 220; their leads are 0.000. `abut_cond` drops 152 and 220 through `skip_next_same`: 156 and the 221.8 re-bow are the same pitch. It drops 204 through the AUTO_REBOW long-note test (the note is 4.49 s). The same cause shows at 152 (crossover +0.210) and at the Tempo I pedal entry 220 (+0.220), which sits under Horn 1's solo.
- **Bass trombone, Trombone 2 and Oboe 2.** They re-enter after the breath, or enter fresh, with lead 0.
- **Violins II.** 204 has no `leg_leads` entry; only 206 has one. Series 1's c27 critic C #3 proposed it and it was not applied. Vln II 208 is now +0.065.

Fix:
- `tools/score_to_parts.py` `abut_cond`: add an optional `force_at` list to an `ABUT_LEAD` entry. A listed onset skips the `skip_next_same` test and the AUTO_REBOW long-note test, and keeps the other tests. In `build/score_config.py`, set `ABUT_LEAD["Double basses"]["force_at"] = [152.0, 204.0, 220.0]`. The c20 measurement of this lead was crossover median 0.20 -> 0.03 s. After the render, check the following same-pitch notes (156, 221.8) for the c15-type hole with a 50 ms dip measure.
- `build/leg_leads.json` `"Violins II"`: add `"204": 0.06`. The total of 0.23 s is under `LEG_LEAD_CLAMP` 0.35; the previous note is 4 qn.
- `build/entry_leads.json`: `"Bass trombone": {"204": 0.10}`, `"Trombone 2": {"204": 0.05}`, `"Oboe 2": {"204": 0.08}`. 204 is in `CAESURA`, so a listed extra applies after the `CAESURA_BREATH_QN` gap (the `cb_` branch).

Expected: every arrival at 204 within -0.03..+0.06 s on b-6.

## 3. Bar 79 (qn 262, the ff B flat 6): the violins' triplet run and their arrival trail the flute by 0.05-0.15 s (measured)

Vln I and II play the 261.5-261.83 triplet sixteenths on Sus MAX with no lead. Pitch dominance, run note by note:

| | 261.5 | 261.67 | 261.83 |
|---|---|---|---|
| Vln I | +0.056 | +0.161 | +0.119 |
| Vln II | +0.028 | +0.146 | +0.057 |
| Flute 1 | +0.008 | +0.079 | +0.047 |

The run notes have the 90-120 ms Sus lag that LEARNINGS section 5 describes. The 262 target is Leg BC MAX, and its lead is **capped at 0.091 s** (0.45 × the 0.167 qn run note).

Arrivals at 262:
- Flute 1 +0.025 / +0.070
- Vln I +0.080 / **+0.205**
- Vln II **+0.175 / +0.190**

The melody's top note, the climax of A', comes in behind the flute that doubles it. A larger lead cap alone would shorten the last run note to about 0.05 s.

**Fix** (`build/score_config.py`): `GROUP_LEAD_AT = {"Violins I": [(261.5, 262.0, 0.15)], "Violins II": [(261.5, 262.0, 0.15)]}`. This is the Movement I c20 rule for "a fast run into a legato target: the run notes and the target arrive together". The run notes keep their played lengths, and the note at 261 ends at the first moved onset + 0.03 qn.

Expected: run dominance about -0.09..+0.01, and 262 b-3 about +0.12..+0.14. Check in parts.json that each run note still sounds for at least 0.12 qn and that the Leg BC keyswitch (now 261.895) moves with the group.

## 4. Late legato joins that repeat by interval, and two late wind entries (measured)

Joins late on both metrics (crossover / rise), each in a solo line:
- Flute 1 F5 -> E flat 5 at **111** (+0.185/+0.180) and **118** (+0.170/+0.250). This is the bar 37-40 solo "dolce cantabile"; the flute lead is 0.03 s. Flute 1 200 (82 -> 84) is +0.14/+0.18 with leg_leads 0.10.
- Bassoon 1 D flat 4 -> B flat 3 at **36** (+0.170/+0.210) and **256** (+0.145/+0.200), lead 0.06. Also Bassoon 1 198 (54 -> 51) +0.220/+0.250, lead 0.
- Violins II 48 (67 -> 68, the bar 17 downbeat where the solo violin enters): +0.220/+0.330.

Two wind entries reach level late:
- Cor anglais 286, the coda entry after the CAESURA breath: b-6 +0.215, b-3 +0.445. Trace -15, -11, -10, -9, -10, -9, -5 from 0 s.
- Bassoon 1 140 (bar 45): +0.204 / +0.244.

Fix:
- `build/score_config.py` `LEG_PAIR_EXTRA_S`: add `"Flute 1": {(77, 75): 0.12}` and `"Bassoon 1": {(61, 58): 0.12}`. LEARNINGS c19: the same pair late every time is fixed per pair. Check the reverse steps 75 -> 77 and 58 -> 61 are not pulled early.
- `build/leg_leads.json`: `"Violins II"` add `"48": 0.10`; `"Bassoon 1"` add `"198": 0.12`.
- `build/early_fills.json`:
  - `"Cor anglais"` add `"286": {"db": 6, "pre_s": 0, "hold_s": 0.20}` (simulated -0.005 / +0.175, peak +1.1).
  - `"Bassoon 1"` add `"140": {"db": 5.5, "pre_s": 0, "hold_s": 0.10}` (+0.074 / +0.104, peak +1.4).

Expected: crossovers +0.03..+0.08.

## 5. Wind and brass first notes on Leg Slur MAX arrive early; wind Sus MAX entries arrive late (measured; the size of the fix is inferred)

- **Wind first notes on Leg Slur MAX** (FL, OB and CA KS Masters, lead 0.11 s, n = 15): b-6 median **-0.055**, b-3 -0.030.
  - Oboe 1 at 139 and 188: -0.080 / -0.090.
  - Cor anglais at 107: -0.080.
- **Brass first notes on Leg Slur MAX** (lead 0.16-0.22 s, n = 7): b-6 median **-0.090**.
  - Horn 3 at 6: b-3 -0.110.
  - Horns 1-2 a2 at 261: -0.165 / -0.155.
  - Trombone 1 212.5, the ff quotation's head: b-6 -0.070 (trace -12.8 dB at -0.10 s, -6.0 at -0.05).
- **Wind Sus MAX entries with no lead** (Flute 2 204, Oboe 2 204 and 262): b-6 +0.05, b-3 +0.10.

The 0.11 s wind and 0.06 s brass articulation extras come from Movement I c03 (+0.150 / +0.115 there with no lead). On movement II's softer first notes they overshoot.

**Fix** (`build/score_config.py`, a movement II override):
- `ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.06, "Leg Slur": 0.11, "Sus Non Vib": 0.07, "Sus MAX": 0.05}, "brass": {}, "Bassoon": {}, "Contrabassoon": {}}`. The clarinets' "Leg Slur" at 0.11 and "Sus Non Vib" at 0.07 measure -0.020 and 0.000, so they stay.
- `build/entry_leads.json`: `"Horns 1-2 a2"` `"261": 0.08` -> remove.

Expected: wind Leg Slur MAX b-6 about 0.00, brass about -0.03..-0.04, and Trombone 1 212.5 about -0.01. Early fills on these onsets are keyed by score onset and still apply, but the auto fills were fitted on the old timing: re-run `auto_fills.py` on the c31 render.

## 6. The tutti breaths at qn 204 and 268 are heard only as lost time (inferred from measurement)

The CAESURA stretches 0.22 s (204) and 0.15 s (268), and the winds cut 0.19-0.23 s. But the strings join across both places (legato overlaps), so the master dips only **1.7 dB at 204** and **2.9 dB at 268**. The wind stems' own gaps are 10-21 dB, and the hall fills them. At 204 the printed string bowing is Vln I up-bow < then down-bow ff tenuto, with Vln II and the celli on tenutos and the basses "change bow at will". That is a new stroke. A section re-taking the bow under a full wind breath would leave a small lift; the pipeline plays it as a Leg BC transition. The listener gets a 0.22 s hesitation with continuous sound, which reads as a drag rather than a breath.

**Test, with a pass criterion set before the render** (204 only; 268 is correct as it is, because the violins' slur runs across it):
- Vln I, Vln II and Vc 204 as fresh strokes. The previous note ends 0.10 qn before 204's moved onset, and the 204 note gets the entry path: the family loud entry lead, with `entry_leads` extras of 0.06 if needed.
- `BREATH_GAP_AT` on the 12 wind and brass notes ending at 204: 0.3 qn, with `BREATH_FALL_CC` 6.
- Pass: master dip at 203.8-204.0 of 4-6 dB, every string arrival at 204 within b-6 +0.06 s, and no 2-5 kHz bump at the re-attack over the c30 level.
- If it fails, revert to the c30 legato transitions.

The audible gain is smaller than in findings 1-3.

**Do not touch:**
- The tempo map: `RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `APEX_AGOGIC`, `BEAT_STRETCH`, and the `CAESURA` values. Every printed tempo, rit., animando and allargando is within 1-3% bar by bar.
- The final bar (36-37 then 20 bpm), the CC11 tail and the release, and the mp3's tail trim.
- Keyswitch placement (gaps of 19.6 ms and more), CC15 placement in rests, and the pre-roll CC36/CC69.
- TIMP_DELAY_S. Harp and pizz. timing.
- The string legato leads that now cross at +0.005..+0.025 s median.
- Vln II 208 (now +0.065), the Vla/Vln II/Cb fills set in c23, and the breath gaps at 196 and 268.
