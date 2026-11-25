# Cycle 45, critic A: articulation and phrasing (render c44, score v621)

## Method

All measurements are on the final c44 stems and master (`cycles/c44/render`, 40 stems), compared with the final c43 render. Notes are placed with each cycle's `rendered_build/parts.json` (main) and `rendered_build_pass2/parts.json` (pass-2 tracks). The scratch scripts were deleted after the run, as the brief asks; the measures are defined below so they can be repeated.

Measures:
- **pcX** is the perceived attack from `tools/pcx.py attack_pcx`, in ms after the score onset. Same-pitch repeats are measured with no exclusion band.
- **Join dips** are broadband stereo power in 30 ms windows: the lower of the two note bodies minus the minimum in [moved onset - 0.03 s, score onset + 0.15 s]. Every monophonic legato join (`pcx.legato_joins`) was measured, 754 joins in all.
- **Repeat and re-bow dips** are on the repeated pitch's harmonic band (2048-point FFT, 20-30 ms box), as in `cycles/c44/actor_scripts/m44.py` and `rebows44.py`.
- **"rel"** is the stem minus the master over the note.

I did not touch build/, tools/, the .rpp or REAPER. Labels: **measured** means a number from the render or from parts.json; **inferred** means reasoned, not tested.

## Manual notes (second round: c39 slot A's pages, 2021 manual PDF pp. 108-113, woodwinds, read again in full; MANUAL-GAPS.md and DIGEST.md read)

**MANUAL-GAPS items still open in this lens:**
- **#1, brass accents on Marc Sus LITE.** Not needed (measured). The 32 fitted brass accents have a 2-5 kHz front minus body of median -9.3 dB, p90 -4.8. The drier hall did not brighten them (c43: -8.8 / -3.2).
- **#5, expressive wind rows.** Still untried. Oboe 1's dolce solo at bar 145 is the obvious test span: it is also where finding 3's worst new hole sits (582).
- **#7, half-section divisi.** Open. See "Deferred items" below.
- **#9, horn portato rows.** Untried.
- **#13, 3TB for the bass trombone's lowest notes.** Untried.

| Manual (PDF page) | c39 A's note | Now (c44 render) |
|---|---|---|
| p.108: Flute 2 is a different player; the other woodwinds have one player each | Flutes yes; same-patch unisons drop a copy | **Unchanged** (measured, parts.json `unison_dropped`): Clarinet 2 drops 78 notes, Bassoon 2 29 and Oboe 2 7, so those a2 passages are one player at +3 dB. "3 Clarinets" and "3 Bassoons" are installed (folder read) and could serve the a2 passages in pass 2. Low priority: most of the 78 notes are in tutti. |
| p.109: Sustain dynamics "with the Mod Wheel" | Play-era text; the render follows the patches | **Unchanged and correct.** CC11 sets dynamics on FL/OB/EH/BS/CB and CC1 on the clarinets (`CC1_DYN_TRACKS`). |
| p.109: Sus Expressive (slower attack, growing vibrato) | not used | **Still not used** (no "Exp" row in any track's `art_counts`). |
| p.109-110: Legato Repetitions (LegRep RRx4) | used, measured pass | **Followed, and it held up with the drier hall** (measured, stem dip / master dip, c43 -> c44). Bass clarinet 308: 10.6 / 5.2 -> 9.0 / 3.8; Bass clarinet 428: 9.5 -> 10.3 stem; Contrabassoon 108-120: stem dips 5.4-9.4 dB. |
| p.110: shorts have no release trails; hold notes so the room rings | not used except as finding 1 | **Partly done.** Since c39 the fugato windows of Bassoon 1, Cor anglais and Flute 1 play "Stac DblTng RRx9" in pass 2. Their decay did not change with the drier hall: the time above -10 dB after the peak is 315 ms in both renders (measured). The bar-30 staccatos (Flute 1, Oboe 1, Clarinet 1) and Clarinet 1 bar 96 are still on Sus rows. |
| p.110-111: Shorts MOD SPEED, runs, trills, flutter tongue, repetitions, FX | n/a | Still n/a. |
| p.112: legato only with no gap and within an octave; monophonic unless CC22 < 64 | followed | **Followed** (measured on c44 parts.json): no chord on any wind legato row, no same-pitch overlap, no wind legato join over 12 semitones, no CC22 lane. |
| p.112: Legato Slur Repetitions | Clarinet 1 108/508/640 yes, 310 merged | **Followed, 310 now on the row** (measured, stem dip c43 -> c44): 108 11.4 -> 13.8, 310 11.8 -> 12.0, 508 10.1 -> 8.7, 640 7.1 -> 8.7. |
| p.112-113: Slur Runs; keyswitch masters | n/a; yes | Unchanged. |
| p.110 (new on this reading): "short articulations do not include release trails ... there is some reverberation at the end of the main sample" | | The drier hall halves the shared tail, but the shorts carry their own recorded room, so their decay did not change (above). No change needed. |

## The three c44 changes, measured through this lens (c43 -> c44)

**1. Drier, shorter hall.**
- **Legato joins:**
  - strings: median dip 2.2 -> 2.3 dB; joins of 6 dB or more 7 -> 14 of 442;
  - winds: 2.0 -> 2.6; 15 -> 29 of 218 (Oboe 1 1 -> 6, Clarinet 1 3 -> 6, Cor anglais 1 -> 3);
  - brass: 1.2 -> 1.8; 3 -> 2 of 94.
- **Join bursts of 5 dB or more:** unchanged (strings 56 -> 51).
- **Legato timing:** unchanged. pcX medians are Violins I / II / violas / celli +17 / +20 / +23 / +6 ms, robust SD 49 / 42 / 52 / 50.
- **Accent fronts:** unchanged (2-5 kHz front minus body: strings -9.5, winds -10.6, brass -9.3 dB).
- **Plucked and struck notes:** harp and timpani ring 0.4-1.0 dB less at +0.3 / +0.6 s.
- **Staccatos:** decays unchanged.

The hall used to hide the wind and string legato sags. That is finding 3.

**2. Release caps.**
- **Phrase ends, stem drop at +0.15 s (median):**
  - string Sus: -6.1 -> -13.5 dB; soft string Sus ends (CC11 50 or less) -3.0 -> -17.9; loud ones -7.3 -> -11.8;
  - brass Sus: -6.7 -> -10.3.
- **No ending sounds clipped** (endings falling more than 8 dB in the first 50 ms):
  - strings: 0 -> 4 of 82, the worst -8.7 dB (Violins I 125);
  - winds, whose release did not change: 4 -> 9 of 172, the worst Bassoon 1 460 at -12.4 (c43 -11.5).
- **Final chord, master after the last note (728):** -5.5 -> -14.3 dB at 0.3 s and -12.5 -> -25.9 at 0.6 s. That is inside the 13-17 dB that recordings give at 0.3 s.
- **Side effect:** the soft-layer (pp / p) part of the string cap made the hidden re-bows and the soft pads dip. That is finding 5.

**3. `STR_REP_NEW_BOW`.**
- **The separation is there** (stem dip medians from `cycles/c44/reps44.txt`, confirmed): portato 5.0, strokes 7.8, soft re-bows 3.9, Sus gaps 6.4 dB.
- **The gaps do not sound chopped.** The holes before the strokes are 7-11 dB under the lower body, and at most 30 ms of any hole lies more than 10 dB down.
- **But the new strokes speak late** (finding 1), and the portato tenutos have a level and shape problem (finding 2).

## 1. The new string strokes and Sus-gap repeats speak about 90 ms after the beat, 70-90 ms behind the same sections' legato notes (S2, S1; measured)

**Where.**
- **15 strokes** (`rep_strokes` class "stroke"):
  - Violas 80, 372, 500;
  - Violoncellos 47, 84, 88, 152, 156, 164, 326, 374, 448, 456, 656, 668.
- **23 Sus-gap repeats** (`rep_sus_gaps`):
  - Violas 537-547 (the bars 135-137 hemiola);
  - Double basses 125, 156, 388, 404, 537-548, 570, 632, 676.

**What is wrong (measured, stem pcX).**
- **Strokes:** median +92 ms, robust SD 49; 10 of 15 more than 60 ms late. Their lead is 0.07-0.10 s.
- **Sus-gap repeats:** median +94 ms; 18 of 23 more than 60 ms late. They have **no lead at all**: lead 0.000 in parts.json for all 23, because the `sus_min_s` branch adds the gap but not the re-tongue lead.
- **The same sections' legato joins sit at +6..+23 ms.** Their entries after rests sit at -31..+44 ms. So each new stroke lands a beat-fraction behind its own line.
- **The level shape shows why.** The strokes reach -6 dB of their peak at a median of about +100 ms (celli 47 +245, 152 +135, Violas 372 +245, Violas 540 +160) and peak 250-450 ms after the beat. The fresh Sus MAX attack is slow and then swells.
- **The hole is centred on the beat, not before it.** Because the attack is late, the stem stays more than 6 dB under the lower body for 100-145 ms at celli 88 / 152 / 156 / 374, Violas 136 / 540 and Double basses 537. At 126 bpm that is half an eighth. The separation Dan asked for (S1) is present, but it falls where the attack should be (S2).

**Fix.**
1. **Per-onset re-attack leads** in `build/retongue_leads.json` (`RETONGUE_LEADS`; the note before gives way, so the played gap is kept). Extra = stem pcX − 0.015 s, rounded to 0.01 s, capped at +0.12. Values in seconds:

   | Track | Onsets |
   |---|---|
   | Violoncellos | 47: +0.12, 84: +0.06, 88: +0.04, 152: +0.10, 156: +0.10, 164: +0.02, 326: +0.03, 374: +0.10, 448: +0.06, 456: +0.12, 656: +0.08, 668: +0.08 |
   | Violas | 372: +0.12, 537: +0.08, 538: +0.07, 540: +0.12, 541: +0.12, 543: +0.12, 544: +0.07, 546: +0.10, 547: +0.11 |
   | Double basses | 156: +0.09, 404: +0.05, 537: +0.09, 538: +0.07, 540: +0.12, 541: +0.12, 543: +0.08, 544: +0.02, 546: +0.09, 548: +0.12, 570: +0.07, 632: +0.03, 676: +0.04 |

   - Leave Violas 80 (-30 ms), Violas 500 (-49 ms), basses 125 (+11) and 388 (+13) as they are.
   - After the render, check the `LEAD WARNING` lines (`LEAD_WARN_S`); every stroke must take its lead.
2. **Generic, for the next score.** In `tools/score_to_parts.py`, let `STR_REP_NEW_BOW` "sus_min_s" repeats take the string re-tongue lead, as the strokes do (`retongue_ok`). The table above then shrinks to residuals.
3. **Optional, after the leads.** If the holes still stay more than 6 dB down for over 100 ms, lower the stroke gap (`STR_REP_NEW_BOW["gap_s"]`) from 0.06 to 0.045 s for strokes at f and louder. The slow attack already supplies part of the separation.

**Targets.**
- Stem pcX of every stroke and Sus-gap repeat within ±40 ms of the section's legato median.
- Stem dip still 6 dB or more (strokes).
- No hole more than 6 dB down for over 90 ms.

Measure on pcX only (the c42 rule). Leads transferred 0.89-0.98 s per s in c42 (inferred to hold for fresh attacks).

## 2. The portato tenutos: the Violins I eighths still carry -4 / -3.5 dB trims from when they were merged, and every tenuto starts under its own body and swells late (S1, articulation; measured)

**Where.** The ten portato tenutos of the motif `d''8( des'' c'' | c''4--)`:
- Violins I 60 and 572 (bars 16 and 144, the leading voice, rel -2.3 / -3.6 dB), 108, 140;
- Violins II 108;
- Violas 108, 136, 668;
- Violoncellos 314, 524.

**What is wrong (measured).**
- **Stale trims.** `build/note_trims.json` has Violins I `59.5: -4.0` and `571.5: -3.5` (steps by `NOTE_TRIM_RAMP_S` 0.1, `build/score_config.py` line 318).
  - They were set when 59.5 / 571.5 was one merged Sus MAX note of 1.29 qn: the eighth plus the tenuto (c43 parts.json).
  - Since c44 the merged note is split. The trim now lands on the 0.117 s eighth only, and the tenuto at 60 / 572 plays untrimmed.
  - The volume envelope drops from +2.0 to -3.7 dB across the eighth and returns at the tenuto (parts.json `vol_db` 59.47-59.88).
- **The tenutos swell instead of re-attacking.** The table gives levels on the pitch band, relative to the tenuto's body (+0.15..+0.42 s):

  | Tenuto | Eighth median / peak | Tenuto front (moved onset..+0.10 s) | Body peak at | pcX |
  |---|---|---|---|---|
  | Violins I 60 | -10.1 / -8.5 | -7.8 | +169 ms | +116 |
  | Violins I 572 | -8.0 / -7.0 | -6.3 | +170 | (split front) |
  | Violins I 140 | -6.8 / -3.5 | -3.4 | +374 | |
  | Violins I 108 | -1.8 / -1.0 | -2.7 | +374 | -26 |
  | Violins II 108 | -3.2 / +0.3 | -2.5 | +274 | -14 |
  | Violas 108 | -3.0 / -0.5 | -4.8 | +274 | -5 |
  | Violas 136 (p) | -1.8 / +0.4 | -9.0 | +305 | +211 |
  | Violas 668 | -2.9 / -0.4 | -4.2 | +274 | -6 |
  | Violoncellos 524 | -2.5 / +1.7 | -3.7 | +344 | +46 |

  - At bars 16 and 144 the listener hears a weak, clipped eighth, then a tenuto that opens at the eighth's level and grows 6-8 dB through the beat.
  - **Violas 136 (p) has its hole after the beat.** Its band falls to -15..-17 dB at 136.02-136.23 qn and rises only from 136.3. The soft Sus MAX attack takes about 0.3 s, so the separation lands after the beat instead of before it. LEARNINGS §6: soft string entries reach level in 300-1010 ms.
- **The c44 CHANGES figure** ("3.5-5.3 dB over the eighth") is the same problem, read on another window.

**Fix.**
1. **Delete** `note_trims.json` Violins I `59.5` and `571.5`, and their `_steps` entries in `build/score_config.py`. This is level only and can be stem-fixed. It raises the eighths by 4 / 3.5 dB.
2. **Per-tenuto level shapes in `LEVEL_SHAPES_S`** (seconds around the score onset, so they keep their length). Targets:
   - front (moved onset to +0.10 s) at the eighth's median within 1 dB;
   - body (+0.15 s to the next moved onset) no more than 1.5 dB over the eighth's peak;
   - ramps 0.03-0.04 s.

   From the table, after step 1:

   | Tenuto | Body | Front |
   |---|---|---|
   | Violins I 60 | -3.0 | +1.7 |
   | Violins I 572 | -2.0 | +1.8 |
   | Violins I 140 | -2.0 | 0 |
   | Violas 108 | 0 | +1.8 |
   | Violas 668 | 0 | +1.3 |
   | Violoncellos 524 | 0 | +1.2 |

   Violins I 108 and Violins II 108 need nothing. Violoncellos 314 already opens at its body (front +1.3).
3. **Violas 136 needs time, not level.** Give it +0.10 s in `retongue_leads.json`; the eighth gives way and plays about 0.11 s, as Violins I's do. Add a +3 dB fill held to +0.15 s after the moved onset (`early_fills.json`, `pre_s` 0). Remove its -2.5 dB `note_trims.json` entry, which only deepens the hole.
4. **Optional patch test** (the library offers a row made for this). Render the ten tenutos on the "Detache" row in pass 2 (`ART_SPANS` per onset on a `TEST_TRACKS` alias of Violins I and of Violas). The manual describes détaché as separated, with a defined end, and allowed to be cut short (p.91). A quarter-note louré is that stroke, and it may avoid the Sus MAX swell (inferred, untested). Keep it only if its front reaches -6 dB of its peak by +0.06 s and its level matches the eighth within 2 dB.

**Targets.**
- Tenuto body within -1..+2 dB of the eighth's peak.
- pcX within ±40 ms of the Clarinet 1 / brass re-tongue in the same bar.
- Stem dip below the eighth 6 dB or more.
- Master dip 4 dB or more at bars 16 and 144. Now: 60 3.1 dB on the reps44 measure, 572 -0.4.

## 3. The drier hall uncovered legato sags in the winds and strings; two of them are exposed solo joins (measured)

**Where and how much.** These joins are now 6 dB or deeper and at least 2 dB deeper than in c43 (stem dip c43 -> c44, master dip in c44, rel):

| Join (qn, bar) | Pitches | Stem dip | Master dip | rel |
|---|---|---|---|---|
| **Oboe 1 582 (bar 146, dolce solo)** | E5 -> D5 | 5.1 -> 10.3 | 2.9 | -3.6 |
| **Clarinet 1 516 (bar 130)** | D4 -> C#4 | 1.9 -> 7.0 | 5.9 | -2.6 |
| Violoncellos 372 (bar 94) | | 5.3 -> 7.6 | 4.0 | -6.6 |
| Violins I 629 (bar 158) | | 2.6 -> 7.2 | | -10.4 |
| Cor anglais 400 | | 5.9 -> 8.0 | | |
| Flute 1 546 / 279 / 540 | | 2.5 / 5.1 / 3.4 -> 7.7 / 7.4 / 6.3 | | |
| Clarinet 1 639 | | 4.7 -> 7.3 | | |
| Violins II 527 | | 4.8 -> 7.2 | | |
| Violas 655.5 | | 4.7 -> 7.0 | | |
| Bassoon 1 129 | | 4.3 -> 6.6 | | |
| Violoncellos 413 | | 3.1 -> 6.4 | | |
| Oboe 1 498 | | 3.7 -> 6.3 | | |

The unmarked rows are buried, at rel -9 to -16 dB.

**The two exposed holes.**
- **Oboe 1 582.** The oboe falls from about -41 to -50.6 dB in the 100 ms before the beat; it was a 3 dB sag in c43.
- **Clarinet 1 516.** A 60 ms hole of 6-7 dB under the next note's body sits on the beat.

**Why (inferred).** Each stem carries its own share of the hall. Halving the return halved what filled the transition sag.
- For the nine wind joins, notes, CC11 and volume envelope are identical in the two builds within ±1.5 qn (measured).
- Round-robin state after c44's full rebuild may account for part of a single join (KIT §16: renders on identical data differ). It cannot explain the doubling across the winds.

**Fix.**
- Run `tools/auto_fills.py 44 cycles/c44/rendered_build/parts.json` on the wind and string tracks, with its overshoot rule and `--guard-existing`. LEARNINGS §6 says to refit fills after any hall change. Keep the usual exclusions (c33 list) and check each new fill against the 30 ms peak (join spikes).
- If the pass leaves Oboe 1 582 or Clarinet 1 516 over 5 dB, write their fills by hand in `build/early_fills.json`:
  - Oboe 1 582: +5 dB, `pre_s` 0.10 (the hole starts 0.105 s before the score onset), held to +0.03 s;
  - Clarinet 1 516: +4 dB from -0.02 s, held to +0.06 s.

**Targets.** Exposed joins (rel > -8 dB) under 5 dB in the stem; winds' 6 dB joins back to about 15.

## 4. Slurred eighths in Violins II and the violas are still re-attacked on Sus MAX against Violins I's legato; the octave doublings stay ragged (deferred A #3: still worth doing; measured)

**What is wrong (measured, c44).** At the slurred onsets these sections share with Violins I (joined Sus MAX notes under 0.8 qn against Violins I's Leg Slur targets):
- **Violins II** runs a median 47 ms ahead of Violins I (c43 34 ms). 15 of 21 onsets are more than 30 ms apart; the worst are 557.5 (-185 ms), 109.5 (-146), 128 (-125), 81 (-94) and 107 (-92).
- **Violas:** median -4 ms, but 25 of 36 are more than 30 ms apart (robust SD 70). The worst are 633 (-291 / -272), 282 (-204), 640 (-147), 281.5 (+105) and 279 (+99).

**Why.** With the 150 ms Sus MAX cap, each of these slurred notes is now a separate fresh stroke with a fast release (inferred). The same figure is legato in Violins I and détaché in Violins II and violas, an octave apart.

**Fix.** As c44 A #3:
- `SHORT_SUS_LEG_TRACKS` += "Violins II", "Violas" (the celli have only 7 such notes, so leave them for later);
- `LEG_CAP_FRAC` [(56.0, 728.0, 0.75)] for both;
- slur-repeat eighths before a same-pitch note stay on Sus MAX (the existing condition);
- after the render, refit the shared onsets' `leg_leads.json` on pcX against Violins I, and move any join of 6 dB or more to `SHORT_SUS_LEG_SKIP`.

Do it after finding 1's leads, in the same render. Neither changes the other's notes.

**Target.** At most 6 of the 57 shared onsets more than 30 ms from Violins I.

## 5. The soft-layer part of the string release cap deepened the hidden re-bows and the soft pad changes (measured; audibility inferred)

**Where.** The string `sus_release_cap_ms` in `build/mix.json` has "dyn" ["pp", "p", "mf", "f", "ff"] at 150 ms; the patches ship 524-931 ms at pp-p.

**What is wrong (measured, c43 -> c44).**
- **Automatic (unprinted) re-bows.** These should be inaudible ("change bow at will"). Their stem dip on the pitch band, median over 78: 2.4 -> 3.5 dB, after c44's refit.
- **Final ppp chord (qn 712-728), master pitch-band dips:**
  - Violas 718.925 0.9 -> 4.4 dB, 721.333 3.4 -> 6.3, 726.816 4.2 -> 5.7 (rel -6..-9);
  - Double basses 726.078 stem 1.6 -> 8.5.
  - At 721.333 the violas' E-flat4 band drops 6 dB at +50 ms and recovers by +250 ms. In c43 it did not move.
  - The broadband master over the chord did not get worse (residual SD 1.38 -> 1.27 dB). So this is one voice of the chord dipping, not the whole chord (inferred: heard as a bow change inside the held chord).
- **Viola divisi pads** (bars 47-59, 15 chord changes): median trough 1.9 -> 3.4 dB; 196 8.7, 184 7.2, 208 5.1.
- **Soft string phrase ends** fall -17.9 dB at +0.15 s in the stems (c43 -3.0; loud ends -11.8), so soft ends now fall faster than loud ones. In the master, the soft ends that are exposed drop only 2.5-4.8 dB at +0.15 s, because the rest of the orchestra holds the level. The final release is within the recordings' range (above). This alone would not need a change.

**Fix.**
- Cap the soft layers less: 350 ms at pp / p, keeping 150 ms at mf-ff. In `tools/build_reaper.py state_for` (the `cap_release` call, line 299), let `sus_release_cap_ms` take a list of specs (call `cap_release` once per spec): `[{"ms": 150, "dyn": ["mf", "f", "ff"], "rows": [...]}, {"ms": 350, "dyn": ["pp", "p"], "rows": [...]}]` on the five section string tracks and their aliases. This is a state change, so it needs a full rebuild of those tracks.
- Then refit the re-bow fills (`tools/fit_rebows.py 45 ... --write`, level only).
- Test it first on Violas in pass 2 if the render budget allows: a `TEST_TRACKS` alias over 184-236 and 712-728.

**Targets.**
- Automatic re-bow stem dips back to a median of 2.5 dB or less.
- Final-chord re-bow master band dips at most 3 dB.
- Viola pad troughs at most 4 dB.
- Soft phrase ends -8..-12 dB at +0.15 s in the stems.
- Keep mf-ff unchanged.

## Deferred items and coordinator questions

- **A #3 (legato for the other sections' slurred eighths):** still worth doing (finding 4).
- **A #4 (viola divisi).** The c44 troughs grew because of the pp release cap (finding 5). Fix the cap first. The DIV A / DIV B route stays a colour and blend choice for the Blend cycle, not an articulation fix: the pads sit 15 dB under the master.
- **Horn 2 bar 59 (qn 232) on LegRep RRx4: no longer needed** (measured).
  - The horn band now falls about 7 dB for 100 ms (231.73-231.84), from -1 to -8 dB re the note.
  - It is back at -0.5 dB by 231.98, i.e. -0.02 qn.
  - The master pitch band dips 3.5-4 dB, and Clarinet 1 in unison dips 16 dB.
  - The c44 horn release cap (237 ms) did the work.
- **Master dips under 6 dB.** Judge them by exposure.
  - Exposed strokes do reach the target: Violas 80 (rel -4.1) has master 6.0.
  - The only exposed failures are the Violins I portatos 60 / 572 (finding 2).
  - Buried strokes (rel -9 to -21) cannot carry a 6 dB master dip, because the other sections play through. Their stem dips (median 7.8) are what count.
  - The soft printed re-bows (master 2.2, stem 3.9) are inner pads at rel -11 to -30. A 6 dB hole in a pp pad would be wrong.

## Standing checks (measured)

- **S1:** findings 1-2. The wind repetition rows separate 5-14 dB, and Horn 1-4 repeats are 5.4-7.2 dB in the stem (c44 CHANGES).
- **S2:** findings 1, 2 and 4. Legato pcX medians are +6..+23 ms per string section.
- **Item 7:**
  - final chord master 100-300 Hz / centroid autocorrelation at 3.95 s: -0.05 / +0.15 (c43 -0.11 / +0.11);
  - Lento 0-40: -0.00 / -0.14;
  - no loop pulse. Re-bow dips: finding 5.
- **Item 8:**
  - accent 2-5 kHz front minus body medians: strings -9.5, winds -10.6, brass -9.3 dB;
  - over +3 dB only the buried Violoncellos / Violas 536 (+5.2 / +5.1, rel -17 / -13) and Clarinet 1 558 (+4.9, rel -13);
  - master 2-5 kHz jump at string accents over +3 dB: 16 -> 21 of 131 (tutti attacks).
- **S3:** bar 62 is unchanged from c43 (c44 CHANGES).

## Do not touch

- `GENTLE_ACCENT` and `accent_fits.json` (dark fronts, unchanged by the drier hall).
- The wind and brass repetition rows (`REP_ROW` LegRep / Leg Slur Rep spans with the c38 gap rules).
- The pass-2 wind staccato windows.
- `STR_REP_NEW_BOW`'s classification (portato / stroke / soft) and its gaps. Change only the leads and levels named above.
- The hall values (fx 0.095, low cut 160, `ir_setup`) and every send.
- The 150 ms cap at mf-ff and the horn 237 ms cap.
- `TIMP_RH_ALT`, the harp ring and damp settings, and the timpani roll settings (decays moved under 1 dB).
- The legato lead tables (pcX medians unchanged).
- Every c44 and earlier do-not-touch item.
