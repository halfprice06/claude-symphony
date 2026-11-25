# Cycle 44, critic C: holistic comparison (on the c43 render)

Compared with: the c27 port baseline, the c38 render (five cycles back), series 1's c26 render of v77 (bars 1-22 and other unchanged passages), the Dvořák 9/i recording, and the stored Brahms 1/ii and 4/ii metrics. The tempo was also compared with the expert mockups in `mockup-kit/EW-TEMPLATE-PLAN.md` sections 8-9 (Duc's Mahler Adagietto; Mulan and Howl's).

Context for the actor: c44 switches to the EastWest template mix, c45 adopts the performance defaults, and c46 targets rubato. Finding 1 is the rubato plan for c46. Findings 2-4 can go into any of c44-c46.

## Manual notes (H2: May 2021 HO manual PDF pp. 44-45, 134-136, read in full; `loop/MANUAL-GAPS.md` read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 44 | MIDI channel modes. In 1-16 mode, CC1, CC11 and pitch bend apply only to that channel. OMNI is for stacking sections. | All 32 tracks: one instance each, one channel each. | Yes. No issue. |
| 45 | Virtual keyboard. CC1 usually crossfades dynamic and/or vibrato layers, or sets volume. CC11 sets overall volume, or carries the dynamics when CC1 carries vibrato. | Strings and winds use CC11 for dynamics and CC1 for vibrato. Horns, trombones, tuba and clarinets use CC1 for dynamics (c30, `CC1_DYN_TRACKS`). | Yes. For c45's "Mod + Expression Combo" test: the manual allows both layouts, so read each patch's mapping before moving dynamics onto CC1 (plan section 5). |
| 134 | Play page. Purge control and preload; samples stream as needed. | REAPER memory: 45 GB after the c43 render. | Yes. |
| 135 | Player window: Mood, Performance, Sensitivity, Envelope, Stereo Double, Reverb, Mic channels, master channel. | `build/mix.json` (shared Opus hall, mic mix, release caps). | c44 replaces the Opus reverb with REAPER returns (plan section 2). |
| 136 | Moods. Classic: Main mics, S. Cal hall, 3.4 s. Soft: Mid + Surround mics through Abravanel Hall, "for slower, more emotional passages", giving definition and depth. Epic: Close + Main + Surround, cathedral, 2.8 s. | This is an Adagio. Strings play on Main; winds and horns on Close + Main. | Partly. The manual's mic choice for slow music (Mid) is untested here (`MANUAL-GAPS.md` #4). The EW template uses Close + Main. Use Mid only as the fallback if c44's layout measures mushy (finding 3). |

## Where c43 stands against the earlier renders (measured)

- **Tempo map.** The same as c27 except that c39 cut `CAESURA[204]` from 0.22 to 0.10 s. Length is 348.1 s (c27 348.2 s, series 1 c26 348.9 s). The per-beat statistics are identical across c27, c38 and c43 (table in finding 1).
- **Per-bar master level, c43 minus c27.**
  - Bars 4-5: -5.5 / -5.2 dB (the bass clarinet swell was fixed).
  - Bar 35: -5.5 dB.
  - Bars 79-80: -3.9 / -4.1 dB (climax order; bars 61-62, at -15.2 / -16.4 dB, are now the loudest, as printed).
  - Bars 57-62: +1.1 to +2.9 dB.
  - Coda bars 85-86: -2.4 / -3.4 dB.
  - Everything else is within ±2 dB.
- **c43 against c38.** Bars 65-66 are +2.0 / +3.2 dB (the niente fade was restored). The coda is +1 to +2 dB. Everything else is within ±1 dB.
- **c43 against series 1 c26 on bars 1-22 (unchanged notes).** Within ±2 dB, except bars 13-14 (-1.8 / -2.1 dB).
- **Release tails.** The tails are now drier than every earlier render (finding 3).
- **Dan's standing checks.**
  - Loop pulsing: no 3.95 s pulsing in the master. 100-300 Hz band and spectral-centroid autocorrelation at the loop lag is -0.29 / -0.22 on the opening C5, -0.26 / +0.03 on the bar 65-67 pedal, +0.11 / +0.01 on the coda pedal (bars 83-86), and -0.27 / -0.26 on the final chord.
  - Trombone 1 accents: 2-5 kHz in the first 80 ms is 9-14 dB under the note body at 213 and 218. The master's 2-5 kHz level at the attack is 1.0-4.6 dB lower than just before it.
  - S1 and S3 were not re-measured by this lens; critics A and B cover them. Finding 1 adds breaths before four same-pitch repeats, which helps S1.

## 1. The tempo is still nearly metronomic: beat deviation is a fifth of Duc's, and the slowest beats fall on the pickups instead of the breaths before them (measured; the plan is simulated on the real pipeline)

**Where.** The whole movement, above all the lyrical a-tempo stretches: bars 7-30 (qn 18-90), 37-52 (108-172), 65-78 (220-259) and 83-89 (274-292).

**Evidence (extra check).** Beat tempi were computed from each `parts.json` tempo map. Deviation is measured from a 17-beat moving median, as in `symphony/mockup-research/ew-template-2026-11-08/scripts/rubato.py`. Beat tempo here is 60 / (the beat's real duration), so caesuras count.

| | median abs. deviation | 90th pct | beats >15 % slower | beats >25 % slower | beats with a change |
|---|---|---|---|---|---|
| printed steps only | 0.0 % | 0.0 % | 3 | 1 | 9 % |
| series 1 c26 | 1.5 % | 7.9 % | 7 | 1 | 53 % |
| c27 / c38 / c43 | 1.5 % | 6.3-6.5 % | 7 | 1 | 52 % |
| Duc, Mahler Adagietto (403 beats) | 8.0 % | 23.4 % | 49 | 20 | 98 % |
| Mulan / Howl's (batch 5) | n/a | 8 % / 5 % | 20 / 26 | 4 / 6 | 20 % / 19 % |
| **this plan (simulated)** | **3.0 %** | **9.3 %** | **16** | **9** | 74 % |

- **Deviation from the printed tempo.** c43 departs from the printed step tempo by a median 0.7 % (90th percentile 4.0 %).
- **Of the 7 beats >15 % slower, 4 are inside printed rits.** They are qn 107, 218, 219 and 303. Only 3 are breaths: 41 (bar 14.3), 65 (22.3) and 123 (40.4).
- **Many stretches run at exactly the printed tempo:**
  - qn 15-18
  - qn 42-46 (the oboe's bars 15-16)
  - qn 54-60
  - qn 116-121
  - qn 152-156
  - qn 205-215 (Largamente, apart from the two 0.94 downbeats)
  - qn 286-291
  - The animando, qn 172-192, is a straight ramp: 60.0, 60.1, 60.2 ... 62.2 bpm.
- **Last beat of the bar.** It averages -2.4 % (bars 1-36), -2.2 % (37-64) and -4.0 % (65-92) against the local median. Duc's beat 4 is -6.9 %. Most of our figure comes from phrase ends.
- **The arcs end one beat late at the pickups.** The `PHRASE_ARCS` ends 30, 78, 140, 238 and 250 lie one beat after the phrase's real end. Each new phrase begins with a pickup on the beat before, so the arc's x0.92 last beat slows the pickup itself:

  | qn (bar.beat) | what plays | c43 tempo | deviation |
  |---|---|---|---|
  | 29 (10.3) | Horn 1 E flat-F into bar 11 | 47.8 bpm | -8 % |
  | 77 (26.3) | Violins E flat-F | 47.8 bpm | -8 % |
  | 139 (44.4) | Oboe 1 A flat into D flat at 140 | 51.4 bpm | -14 % |
  | 237 (70.3) | Violins E flat-F into A' | 45.8 bpm | -12 % |
  | 249 (74.3) | Violins E flat-F | 47.8 bpm | -9 % |

  The note that should broaden comes one beat earlier: the held G3 at 27-29, G4 at 75-77, C4 at 136-139, B flat 3 at 235-237, G5 at 247-249. A player breathes before the pickup and moves through it. `CAESURA[140]` also adds its time between the oboe's slurred pickup and its downbeat.
- **Printed breaths that take no time.** The breaths at 102 (BCl, Bn1), 188 (Cl1, Hn1), 196 (BCl, Fl1, Hn1, Ob1), 259 (Bn1) and 265 (Bn1, Hn1, Hn2) get no caesura. So do the same-pitch phrase restarts at 96 (BCl E flat 3), 148 (Ob1 D flat 5, the fp), 235 (Hn1 B flat 3) and 265 (Vln I B flat 6).

**Plan (in `build/score_config.py` terms; simulated by re-running `tools/score_to_parts.py`'s tempo functions).** The simulation reproduces c43's map exactly with the c43 settings (max beat difference 0.0 bpm, 348.11 s). The plan's map is 353.2 s long (+5.1 s). By section:

| section | qn | c43 | plan |
|---|---|---|---|
| A (horn theme) | 18-42 | 28.19 s | 28.66 s |
| B | 108-152 | 44.41 s | 45.37 s |
| A' | 238-274 | 43.39 s | 43.94 s |
| climax | 204-220 | unchanged | unchanged |

**a. Tool.** In `tools/score_to_parts.py`, make `PHRASE_PUSH`, `PHRASE_SLOW`, `PHRASE_SLOW_SUB`, `PHRASE_SLOW_MAIN`, `PHRASE_RETURN` (lines 1149-1150) and `APEX_AGOGIC` (line 1220) read from the config with `globals().get(name, default)`, as `PHRASE_RETURN_AFTER_OPEN` already does. The defaults stay as they are, so other movements do not change.

**b. Depths.** Duc's breaths are 15-30 % slower than the local tempo, so:

```
PHRASE_PUSH = 1.03; PHRASE_SLOW = (0.93, 0.84); PHRASE_SLOW_SUB = (0.97, 0.90)
PHRASE_SLOW_MAIN = (0.91, 0.80); PHRASE_RETURN = 0.98; APEX_AGOGIC = 0.93
```

**c. Arcs cut at the pickups.** Every arc now ends on the beat where the next phrase's pickup starts.
- Changed: (18,29), (66,77), (124,139), (226,237,"main"), (237,249).
- Split: (108,124) becomes (108,116,"sub") + (116,124).
- New: (139,148,"sub").
- Also add `APEX_LEAD[116] = "Flute 1"`.
- Keep c16's rule: no arcs on 42-48 or 54-60.
- Do not add an arc that ends at a ramp start (249-259 or 286-292): the ramp code would let the tempo jump back up.

```
PHRASE_ARCS = [(18, 29), (29, 42, "main"), (48, 54, "sub"), (60, 66, "main"), (66, 77), (77, 90, "main"),
               (108, 116, "sub"), (116, 124), (124, 139), (139, 148, "sub"), (152, 160, "sub"), (160, 168),
               (220, 226, "sub"), (226, 237, "main"), (237, 249), (274, 286)]
```

**d. Breaths.** Replace both `CAESURA` definitions (line 79, and the c39 override at line 880).
- Raised: 29, 42, 66, 124, 164, 237, 268, 286.
- New:
  - 54 and 60: the oboe/solo-violin hand-offs.
  - 77 and 249: before the violin pickups.
  - 96 and 148: same-pitch restarts.
  - 102: printed breath.
  - 116: the flute's sub-phrase.
  - 139: moved from 140.
  - 188, 196, 259 and 265: printed breaths.
- Kept at 0.10: 204 (c39's reason: the strings play through) and 171.

```
CAESURA = {29.0: 0.22, 42.0: 0.18, 48.0: 0.15, 54.0: 0.10, 60.0: 0.10, 66.0: 0.20, 77.0: 0.15, 96.0: 0.15,
           102.0: 0.15, 116.0: 0.10, 124.0: 0.22, 139.0: 0.15, 148.0: 0.10, 164.0: 0.20, 171.0: 0.10,
           188.0: 0.12, 196.0: 0.08, 204.0: 0.10, 237.0: 0.18, 249.0: 0.15, 259.0: 0.10, 265.0: 0.12,
           268.0: 0.22, 286.0: 0.20}
```

**e. Per-beat table (duration contrast inside the phrase).** In `BEAT_STRETCH`:
- A beat where the lead line starts a note of 1.5 qn or more on the beat gets x0.96.
- A beat with two or more lead-line onsets (moving eighths, the pickups) gets x1.04.
- Downbeat arrivals after a pickup get x0.97.
- No entry is placed on an arc's last two beats, a caesura beat or an apex beat.
- The lead lines used: Hn1 17-42, Ob1/Vln I solo 42-66, Vln I 66-90, BCl 90-102, Fl1 108-124, CA 124-139 and 152-172, Ob1 139-150, Hn1 220-237, Vln I 237-259, Cl1 280-292.
- The four existing entries stay.

A generic rule (`DURATION_CONTRAST` over the lead spans) would produce the same table. The explicit table is:

```
BEAT_STRETCH = {17: 1.04, 18: 0.97, 24: 0.96, 29: 1.04, 30: 0.97, 37: 1.04, 38: 1.04, 39: 0.96, 42: 0.96, 45: 0.96,
  48: 1.04, 51: 0.96, 55: 1.04, 57: 0.96, 60: 1.04, 63: 0.96, 66: 0.96, 72: 0.96, 77: 1.04, 78: 0.97, 85: 1.04,
  86: 1.04, 87: 0.96, 91: 1.04, 92: 1.04, 93: 0.96, 97: 0.96, 99: 0.96, 108: 0.96, 113: 1.04, 121: 1.04, 126: 0.96,
  131: 1.04, 132: 0.96, 136: 0.96, 140: 0.97, 145: 1.04, 147: 0.97, 148: 0.96, 152: 0.96, 155: 1.04, 160: 0.96,
  164: 0.96, 168: 0.96, 204: 0.94, 208: 0.94, 226: 0.96, 232: 0.96, 237: 1.04, 238: 0.97, 244: 0.96, 249: 1.04,
  250: 0.97, 257: 1.04, 280: 0.96, 283: 0.96, 286: 0.96, 289: 0.96}
```

`TEMPO_PUSH`, `RAMP_SPANS` and the climax are unchanged.

**Result (simulated).**
- **Where the breaths fall.** The beats more than 15 % under the local tempo are now the phrase-end breaths. Beats:
  - 28 (bar 10.2, -28 %)
  - 41 (14.3, -29 %)
  - 65 (22.3, -27 %)
  - 76 (26.2, -24 %)
  - 89 (30.3, -20 %)
  - 115 (38.4, -16 %)
  - 123 (40.4, -29 %)
  - 138 (44.3, -25 %)
  - 147 (46.4, -16 %)
  - 236 (70.2, -29 %)
  - 248 (74.2, -26 %)
  - 267 (80.3, -15 %)
  - 285 (86.3, -27 %)

  The printed rits at 218, 219 and 303 complete the list.
- **Pickups.** The pickups at 29, 77, 139, 237 and 249 now run at -2 % instead of -8..-14 %.
- **Last beat of the bar:** -2.7 % / -3.5 % / -3.8 %.
- **Horn theme, bars 7-10 (qn 17-30), in bpm:** 54.1, 50.4, 53.6, 49.8, 53.6, 54.4, 53.6, 49.9, 52.0, 52.0, 48.4, 37.7 (breath), 53.0, 52.0.

**Limits.**
- Median deviation reaches 3 %, not Duc's 8 %. Duc's map follows a recording at 40 bpm, beat by beat. I would not go further by rule: it would need beat-level irregularity that no score mark supports. Tune the depths by ear after c46.
- The plan follows the printed tempos. It slows no beat inside a printed animando beyond the printed breaths at 188 and 196, and it does not touch the bar 61-64 climax.

**Before c46 renders (pipeline traps; LEARNINGS c11 and Movement I c04).**
1. Tempo changes move the `AUTO_REBOW` points, which are placed in seconds, and detach the fitted `rebow_fills.json` shapes. List the current re-bow points in `REBOW_AT` before changing the map, then run `fit_rebows.py` with the relevel41 step.
2. The Sus/Leg choice reads note lengths on the arc-shaped map (`TEMPO_NC`). Diff the keyswitches in `parts.json` against c45's.
3. Any note that grows past 6 s needs the loop check (BRIEF item 8). Candidates: the held notes at 39-42, 87-90 and 122-124 at 37-43 bpm.
4. `add_caesuras` exits if a tempo point falls strictly inside a caesura's 0.25 qn. 188, 196, 265 and 268 sit on ramp step boundaries, which is allowed. The simulation ran without that error.

## 2. The theme's printed swells are flat or reversed, and long notes barely move (measured)

**Where and what.** The theme's first phrase has a printed one-beat swell on its high E flat (p, then < >). The swell is not heard in any of the three statements:
- **Horn 1, bar 8 (qn 20-21).** CC11 rises 46 -> 58, but `roles.json` Horn 1 `[20.5, 23.5, -2.5, 1.0]` drops the volume envelope 2.5 dB over the peak. Stem level per half beat from 19 to 22.5: -41, -42, -44, -41, -43, -42, -43, -44 dB. The swell measures -2.5 dB (reversed). The decrescendo 21-24 measures 0-1 dB.
- **Violins I, bar 72 (qn 240-241), A'.** CC11 rises 49 -> 61, but the 2.9 dB early fill at 240 makes the start loud. Levels: -42, -43, -42, -43 dB, so the swell is flat (-0.8 dB). Bar 24 (qn 68-69) rises only 1-2 dB on Violins I; Violins II rises 3-8 dB.
- **Flute 1, bar 37 (qn 108-111).** The flute's first crescendo falls instead of rising: -38 at 108 to -40/-42 dB at 110.5-111, although CC11 rises 54 -> 73 and the role adds +2.
- **Across all printed hairpins over 1 qn, on every track.** They do go the printed way: median +5.7 dB for crescendos, -7.3 dB for diminuendos. But 16 % of crescendos and 11 % of diminuendos measure under 1 dB or reversed. The volume envelope works against the hairpin in 33 % of crescendos (series 1 c26: 34 %).
- **Long notes.** Of all notes of 1.5 s or longer, 20 % of string notes and 19 % of wind notes have CC11 flat (range under 3) inside the note; the median movement is 5 CC. In the expert files only 0-13 % of long notes are flat, and phrase ranges are 30-60 units (plan section 8).

**Why it happened.** Series 1 c24 (C #1) added the Horn 1 role and removed the bar 24 swell gain. The aim was to keep the bar 12 mp crest 3 dB over the bar 8 swell. That margin is now 5-6 dB: Horn 1 measures -36 dB at qn 32 against -41..-42 at 19-21, after c42's +4.5 dB on bars 7-14. Removing the role keeps the crest 3 dB or more on top.

**Fix.**
- Remove the Horn 1 role `[20.5, 23.5, -2.5, 1.0]` from `build/roles.json`.
- Add `HP_SOFT_GAIN_AT["Horn 1"][20.0] = 3.0` (the dict already holds 32.0).
- Add `HP_SOFT_GAIN_AT["Violins I"] = {240.0: 4.0}`, and lower the Violins I early fill at 240 from 2.9 to 1.5 dB. Check on a stem_fix simulation that the 240 join dip stays under about 5 dB.
- Add `HP_SOFT_GAIN_AT["Flute 1"] = {108.0: 4.0}`.
- Target: each swell's peak sits +2.5 to +4 dB over its start on the stem, and the following decrescendo falls 3 dB or more.

**For c45.** When the phrase arch and hairpin shapes come in (plan sections 7-9), use this as the acceptance check:
- Long notes flat in CC11 under about 15 %.
- No printed hairpin under 1 dB on a lead line. Lead lines here: Hn1 17-42 and 220-237, Ob1, Fl1, CA, BCl, Cl1 solos, Vln I 66-90, 172-204 and 237-274.
- Every per-note trim, fill or role inside a hairpin listed with the dB it adds against the hairpin.

## 3. Dan's "too wet" and "mushy": the hall tail is no longer wet; what remains is low-mid density in the soft passages, which c44's family EQ targets. c44 must not bring the tail back (measured; mush cause inferred)

**Too wet (measured).** Stems were measured at phrase ends followed by at least 1.2 s of rest, as the drop at +0.15 / +0.3 / +0.6 s and the time to -20 dB (median):

| | strings | winds | brass |
|---|---|---|---|
| series 1 c26 | 7.7 / 12.2 / 21.1 dB; 0.52 s (n 34) | 12.9 / 18.2 / 25.9; 0.34 s (50) | 7.6 / 14.9 / 21.9; 0.52 s (21) |
| c27 | 5.3 / 10.7 / 20.2; 0.53 s | 13.0 / 18.1 / 25.9; 0.35 s | 7.0 / 13.5 / 22.7; 0.47 s |
| c38 | 5.4 / 12.3 / 23.5; 0.48 s | 13.9 / 20.3 / 28.7; 0.24 s | 10.5 / 20.9 / 28.8; 0.28 s |
| c43 | 6.0 / 14.9 / 28.7; 0.39 s | 14.5 / 22.0 / 31.5; 0.23 s | 13.7 / 23.1 / 31.3; 0.25 s |

- **The recordings** (c41 critic C's detector on the same kind of event): Brahms 1/i tutti stops take 0.43-0.55 s to -20 dB, and Dvořák 9/i takes 0.49 s.
- **c43 against the recordings.** c43's strings sit at the dry end of that range. Winds and brass fall to -20 dB in about half the recordings' time.
- **So "too wet" is solved by number since c38-c42.** If anything, the winds and brass are now dry. This matches c41 C's verdict.

**Mushy (measured spectrum; cause inferred).** The low-mid range is thick in the soft wind and horn passages. 1/3-octave levels relative to 1 kHz on the c43 master:

| span | 160 Hz | 200 Hz | 250 Hz | 315 Hz | 400 Hz | 500 Hz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|---|---|---|
| bars 7-30 | +8.6 | +5.8 | +3.0 | +7.3 | +6.0 | +5.2 | -6.2 | -16.9 |
| bars 37-52 | -0.2 | -0.3 | +1.7 | -1.1 | +0.6 | +3.3 | -10.3 | -25.3 |

- Whole movement: 250 Hz is +6.1 dB, against Dvořák 9/i's +4.4. The band shares are close to the references (250-500 Hz: -5.67 dB, against -5.95 to -6.34).
- **So the excess is local.** It sits in bars 7-36, where Horn 1, clarinets, bassoons, bass clarinet and harp all play at 150-500 Hz, and it was the same in series 1 c26.
- **What c44 does about it.** The EW family EQs cut exactly this band (plan section 3): woodwinds -5.1 dB at 447 Hz, brass -5.4 dB at 475 Hz and -7.8 dB at 821 Hz, strings -2.2 dB at 456 Hz. The template's Close mic on the strings adds note definition (plan section 1).

**Fix (guard rails for the c44 template mix).**
1. **Measure the tails again after c44.** The EW returns use the full IR (endPos 1.0) of 3.3-3.4 s halls at sends of -5.6 to -8.8 dB. That is longer than our c40 IR envelope (0.7) and could undo c38-c42. Keep:
   - strings' time to -20 dB at 0.40-0.55 s;
   - winds and brass at 0.30-0.50 s;
   - every family's drop at +0.3 s at 13 dB or more.

   If the strings exceed 0.55 s, first apply the batch 5 defaults: register sends 10 dB lower on bassoons, contrabassoon, trombones, tuba and basses, and the 2.3 kHz low-pass after each Spaces return. Then lower the string send in 2 dB steps. The last resort is Duc's 2.1-2.45 s hall (plan section 8).
2. **Measure the mush.** Use the 315-500 Hz level relative to 1 kHz over bars 7-30 on the master. c43 is +5.2 to +7.3 dB. Expect 2-4 dB less with the family EQ. Report it with the 2-4 kHz level, so the 4.7-7.6 kHz shelves do not overshoot. The finale's first template render measured too bright: 6-20 kHz share at -25 dB, against -29 to -32 dB (plan section 9).
3. **Mid mics.** If the EQ does not move the figure, try Mid on Horn 1, the clarinets and the bass clarinet in bars 7-36. This is the manual's mic choice for slow music (Soft mood, p.136) and `MANUAL-GAPS.md` #4.

## 4. The coda clarinet solo has lost 3.5 dB since c27 and now competes with the cor anglais inner line (measured; audibility inferred)

**Where.** Clarinet 1, bars 85-89 (qn 280-292): the dolce motto tail E flat 5 - D5 - D flat 5 - D flat 5. Two pp lines join it at 286: the cor anglais (F4 - E4 - E flat 4) and Horns 3-4.

**Evidence.**
- **Clarinet 1 stem by bar (85, 86, 87, 88):**

  | render | 85 | 86 | 87 | 88 |
  |---|---|---|---|---|
  | c27 | -45.3 | -42.8 | -44.6 | -46.7 |
  | c43 | -48.9 | -47.1 | -47.9 | -48.8 |

- **Cor anglais in bars 87-88:** -51.8 / -51.8 dB in c27, -48.9 / -50.2 dB in c43.
- **The gap.** The clarinet's margin over the cor anglais fell from 7.2 / 5.1 dB to 1.0 / 1.4 dB. This comes from c35 B #1 (coda clarinet -2, cor anglais +2), c38 B #3 (Clarinet 1 coda CC7) and c43's soft roles.
- **Lead over the sum of all other stems, median, qn 286-292:** series 1 c26 +0.4 dB, c27 -1.1, c38 -3.9, c43 -3.8.
- **Printed dynamics.** Clarinet 1 is pp. The strings are ppp until the pp at 286.

**Fix.**
- Raise Clarinet 1 by +2 dB over qn 279.9-292 in `roles.json`. Keep the c38 CC7 lane, which flattens the bumps at 283 and 292.
- Return the cor anglais to 0 dB over 286-292. That undoes half of c35 B #1 for this span only.
- Target: the clarinet 3-4 dB over the cor anglais in bars 87-88, and lead-over-rest of about 0 dB.
- Check bar 85's ppp-to-pp balance against the basses, which are now at -51.9 dB.

## Weakest passages now, and what still sounds like a machine (summary)

Ranked by what a listener would notice.

1. **Bars 7-14, the horn theme.** The tempo is almost straight 52 (finding 1). The printed swell is reversed (finding 2). The low-mid range is thick (finding 3).
2. **Bars 23-30 and 71-78, the violin theme.** The swell is weak or flat. The pickups at 77, 237 and 249 are slowed where the breath should come before them.
3. **Bars 37-44.** The flute crescendo falls, and the tempo is a flat 60.9 bpm over qn 109-121.
4. **Bars 85-89.** The clarinet solo is too low (finding 4).

The animando (bars 53-60) and the climax (bars 61-64) are the strongest passages: the climax order and the brass accents are right.

The machine traits, in order:
- tempo with no breathing (finding 1);
- long notes and swells that do not move (finding 2);
- attacks aligned to the beat more tightly than any expert file. This is inferred from our lead method; the plan's 36-55 ms tutti spread is a c45 default, so measure the perceived spread there.

## Changes for the next renders, in order of effect

1. c46: the rubato plan in finding 1. Steps a-c and the pickup fix can go in earlier if the actor wants them heard before c46.
2. Now: the swells in finding 2 (remove the Horn 1 role; four `HP_SOFT_GAIN_AT` entries; the Violins I 240 fill).
3. c44: the tail and low-mid guard rails in finding 3. Measure them and report them in CHANGES.md.
4. Now: Clarinet 1 +2 dB at 280-292 and the cor anglais back to 0 at 286-292 (finding 4).
5. c45: the long-note and hairpin acceptance check in finding 2.

Do not touch: the climax order (bars 61-62 loudest; the c28/c34/c39 balance at 61-62 and 79-80); Trombone 1's accent handling (2-5 kHz front 9-14 dB under the body); the re-bows and fills that keep the held notes free of loop pulsing (master autocorrelation under 0.12 on the opening, the pedals and the final chord); `CAESURA[204] = 0.10` and `BEAT_STRETCH` 204/208; the printed tempo ramps (`RAMP_SPANS`); the release caps (string tails are at the recordings' dry end); the bar 66 niente CC7 lanes.
