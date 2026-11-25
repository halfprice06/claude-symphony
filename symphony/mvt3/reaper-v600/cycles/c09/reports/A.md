# Cycle 9, critic A: articulation and phrasing (render c08, score v600)

Method. All numbers come from the c08 render after its stem fix (`cycles/c08/render`: dry stems 01-31, returns 32-35, `00_Master.wav`) and the data that produced it (`cycles/c08/rendered_build/parts.json`; `build/parts.json` differs only by the basses' stem-fix refit). Times use the parts.json tempo map. Scripts: `/private/tmp/claude-501/mockup-loop/mvt3-c09-A/` (deleted after the report). "Measured" means a number from the render, parts.json, the events file or a patch file. "Inferred" means reasoned but not tested. Measures:
- **Repeat dip (S1):** broadband 10 ms RMS on the dry stem. min(peak in -0.15..-0.03 s, peak in +0.03..+0.25 s) minus the minimum in -0.06..+0.06 s around the score onset.
- **Accent:** level over neighbours is the first 0.27 s against unaccented onsets of the same track within 4 qn. Front minus body is 2-5 kHz over -0.02..+0.08 s against +0.12..+0.40 s. The tilt subtracts the same front minus body at 0.25-1.5 kHz.
- **Attack time (S2):** `tools/pcx.py attack_pcx`, plus a broadband check (time from the pre-onset minimum to within 3 dB of the local peak).

## Manual notes (cycle 9, slot A: second reading of 2021 manual PDF pages 100, 103-107, brass, read in full)

The first reading is `cycles/c03/reports/A.md`. Each of its notes is checked against c08 below. MANUAL-GAPS items open in this lens come first.

| Manual (PDF page) | Where it applies | c03 status | c08 status |
|---|---|---|---|
| MANUAL-GAPS #2: Leg Slur Rep / LegRep rows (p.106) | slurred brass repeats | not used | **Still not used, and not needed (measured).** No brass repeat dips under 3 dB except Trombone 1 992.5 (2.0 dB, Leg Slur MAX). The 1TB KS Master has no Leg Slur Rep row (ks_maps), so the fix stays on the re-tongue gap (finding 2 covers the string cases). |
| MANUAL-GAPS #1 / p.106 Legato Slur Accent (velocity = accent strength) | the 14 brass accents on Leg Slur MAX (Tbn 1 985-1009, 1081-1084; Hn 3 1076/1084) | not used; fronts "weight, not bite" | **Not used (measured).** Brass accent fronts are now darker than unaccented notes. See finding 3, where this row is the A/B option. |
| MANUAL-GAPS #13 / p.100: no solo bass trombone; 1TB samples root at E2 | 11 bass trombone notes below MIDI 40 (qn 360-372, 414-416, 611, 643, 660) | transposed samples | Unchanged (patch). Low audible gain. Not ranked. |
| p.103: Repetitions 170 / 145 / 120 bpm, tempo-synced | none: the brass have no fast same-pitch runs. Trumpet 3's Più allegro figures are single eighth-quarter pairs. | n/a | n/a. Trumpet 3's repeats dip a median 10.9 dB (40 repeats, p10 6.7). |
| p.103: Triple Performance (3 Trumpets); double tonguing | the trumpet staccatos are on "Stac DblTng RRx9" | follows | Follows. |
| p.103: **Sforzando Crescendo** (Solo Horn, Solo Tuba): accented attack, then a strong crescendo; velocity sets both | **bar 149, qn 592: "sfp <" in Horns 1-4, Trombones, bass trombone and tuba** (sfp, crescendo to ff at 596). c03 called this n/a. | n/a | **New note: it applies.** The 1FH, 1TB and 1TU KS Masters all hold a "Sfz Cres" row (ks_maps). The render's sfp has no sf (finding 1). The row is the A/B for the brass. |
| p.104-105: crescendo patches (Fast / Med / Slow; MOD SPEED on CC1 in 3 zones), no release trails | brass hairpins | not used | Not used. Not ranked: the CC1 crossfade follows the printed hairpins. |
| p.105: legato only with no gap and within an octave; mono unless CC22 0-63; slide legato | every brass legato row | follows | **Follows (measured, all 31 tracks).** 0 chords on a legato row. 0 legato overlaps over 0.2 s. No CC22. |
| p.106: Legato Slur, CC1 = volume with an overblow filter near 127; velocity = transition speed | all brass legato | CC1 max 120; Tpt 1 solo v124 | **Follows.** CC1 still stops at 120. Trumpet 1's dolce solo (qn 200-264) is on v96, and its slur joins sit at -36..+70 ms (median -12 ms), dips 2-6 dB. |
| p.106: Slur Runs | none printed | n/a | n/a |
| p.106-107: mutes; "stop" for horns | Tpt 1 con sordino 680-792; stopped horn 192-199, 548, 668-675 | mute re-tongued; stop not used | **Mute: same.** The Solo Trumpet "05 Mutes" folder holds only Mute Sus, Mute Sus Accent and StacSs DblTng Mute (listed on disk); there is no muted legato patch. c08 A measured the joins at a 2.1 dB dip, against 2.2 on the cor anglais. Keep. **Stop: on "Stop Sus" since c03.** |
| p.107: keyswitch masters | every row change | ks_clash empty; shortest 10.2 ms | **Follows, but tight (measured).** 2204 keyswitches; median lead 12.5 ms, minimum 7.1 ms. The research default is 40-800 ms (finding 5). |

## Standing checks on c08

- **Coordinator: wetness (measured).**
  - Tutti cut-offs fall 20 dB in 0.37 / 0.36 / 0.55 / 0.42 s (qn 5 / 21 / 661 / final 1113, fixed time). Median 0.40 s, so c08's 0.39 holds. qn 661 is over the 0.50 s ceiling.
  - Final chord RT60 from the -10..-30 dB slope: 1.29 s (claimed 1.26).
  - Width is not in my lens.
- **Item 4, accents (measured).** Accent level over neighbours (medians):
  - Brass +3.1 dB in the Più allegro and +3.5 in 1088-1116.
  - Strings +2.7 / +2.9 dB.
  - Winds +3.1 / +3.4 dB.

  Brass tilt median -3.8 dB, p90 +0.5..+1.3. No accent bites; the opposite risk is finding 3.
- **S1 (measured).** Medians by family:
  - Basses 10.9 dB (341 repeats), tuba 14.4, trumpets 10.2-10.9, horns 7.0-8.6, winds 6.8-11.3, upper strings and celli 5.8, violas 7.8.

  The weak spots are finding 2.
- **Legato and breaths (measured).** No mono-rule breaks. All 152 breath marks have a gap of 74 ms or more (median 135 ms).
- **Item 7 and the re-bows.** c08 changed no re-bow or held-note data (no space_rebows run). c08 A's loop autocorrelations (all under 0.25 from 880 on) stand.

## 1. The sfp at bar 149 and the fp at bar 209 start on the soft layer: no sforzando, then a swell (S3; measured)

**Where.**
- qn 592 (bar 149, "sfp <" to ff at 596): 24 tracks, all strings, winds and brass.
- qn 832 (bar 209, "fp <"): 18 tracks.

**What is wrong.** At the moved note-on, the controller that sets the dynamic layer (CC11; CC1 on the brass and clarinets) already sits at the p value. The sf value arrives only at the score onset + 0.02 qn.
- At 592, on 23 of 24 tracks the note-on is at CC 46 (Violins I to basses: CC11 52) and the attack value is 114-120. The gap after the note-on is 0.10-0.50 qn:
  - Violins I/II and basses lead 0.168 qn (61 ms);
  - violas and celli lead 0.504 qn (183 ms);
  - Horn 1 leads 0.252 qn, Oboe 2 0.336 qn.
- At 832, 17 of 18 tracks show the same: note-on at CC 46, attack 88-114.

The attack sample is therefore chosen and sounded at p, and the "sf" is a CC11 swell after the attack. That is the reverse of an sfp.

**Evidence.** Stems around 592 (50 ms RMS):

| stem | ff before | sf peak | time after 592 | p (0.7-1.4 s) |
|---|---|---|---|---|
| Violins I | -30.0 | -34.9 | +245 ms | -33.8 |
| Violins II | -30.5 | -34.3 | +215 ms | -31.5 |
| Violas | -29.4 | -34.8 | +245 ms | -35.3 |
| Violoncellos | -29.0 | -29.4 | +275 ms | -29.9 |
| Trumpet 1 | -26.0 | -31.7 | +255 ms | -30.6 |
| Master | -17.5 | -18.6 | +295 ms | -20.2 |

- The string "sf" peaks sit 4-5 dB under the ff before. The p after them is only -1.0..+0.5 dB from that peak.
- On the master the sf is 1.1 dB under the ff, its peak is 0.30 s late, and the p is 1.6 dB under it.
- At 832, Horn 1 does make f-then-p (13.4 dB), but Trombone 1 (2.8), Flute 1 (1.6), the violas (1.2) and the tuba (1.1, peak +440 ms) do not.
- The code: `tools/score_to_parts.py` fp/sfp branch (about line 1832) writes `(q, level), (q + 0.02, spike), (q + hold, spike), (q + fall, DYN[sfp])` in score qn. The note-on copy at the moved onset takes `DYN["sfp"]` (46), the level after the spike (measured in parts.json, every track listed).

**Fix (`tools/score_to_parts.py`, generic):**
- At an fp / sfp onset, write the spike value (max(DYN[SFP_SPIKE_HI], level), or FP_SPIKE's hi) at the moved note-on minus 0.005 qn on every lane that carries the dynamic (cc11, and cc1 on `CC1_DYN_TRACKS`).
- Measure `SFP_SPIKE_S` (0.15, 0.35) from the moved note-on, not from the score onset.
- Keep `FP_CHECK_AT` after the fall.
- Pull the c08 string sfp leads back (entry_leads.json violas / celli 592: +0.06 s removed; the `ROW_LEAD_S` 591.9-592.1 span 0.06 -> 0). With the attack on the loud layer, the long leads only make the sf earlier.
- Brass A/B for 592 (manual p.103): put Horns 1-4, Trombones 1-2, the bass trombone and the tuba on the "Sfz Cres" row for that one onset (`ART_SPANS` 591.5-592.5). Velocity 100-110 (velocity sets the attack and the crescendo). Each track gets one more row: about 0.1-0.3 GB each (inferred), 8 tracks.

**Targets.** On the master and on each string stem:
- sf peak within 80 ms of 592 and within 1 dB of the ff before;
- the p at 0.4-0.9 s 8-10 dB under the sf (Movement I c50 / C's 10 dB);
- the same check at 832 on every fp track.

## 2. Unslurred same-pitch string repeats still abut: dips of 2.1-2.6 dB (S1; measured)

**Where.**
- **Violas, coda bars 205-208 (qn 820-832).** Div. chords in the hammered layout's "quarter, eighth rest, eighth, quarter" figure, f then mf. The eighth runs straight into the next downbeat chord: written eighth 0.5, played 0.494 qn from a 0.36 qn lead, so the gap is 2 ms. Downbeat dips:
  - 820 4.7, 822 4.2, 826 6.5, **828 2.1**, 830 6.2, 832 6.2 dB.
  - The round robins decide which ones merge. In the same span, the dotted-quarter-to-eighth joins (gap 47 ms) dip 4.5-7.0.
- **Violins I 880 -> 884** (div. chord F5/B5 -> "unis." B5, the head of the slurred run into the 888 arrival): gap 10 ms, dip **2.5 dB** (c08: 0.3 by its measure; open item).
- **Violoncellos 828 -> 832** (held G♯2 into the same-pitch head of the run): **4.3 dB** (c08 4.1).
- Others under 3 dB with a gap of 15 ms or less:
  - Violins II 362 (7 ms, 2.5);
  - Violas 426 (11 ms, 2.5) and 556 (11 ms, 3.3);
  - Violas 868 (2 ms, 2.6).

  Basses 836-839 (2.1-2.6) sit at the accelerando's fastest tempo, on the detach dip.

**Why.** `STR_REP_NEW_BOW` acts only on repeats that the legato merge joins. Its "chord" option is limited to non-legato next rows (c08). Separate unslurred Sus MAX notes whose lead and length close the gap get neither a gap nor a dip.

**Fix (`tools/score_to_parts.py` + `build/score_config.py`):**
- New option `STR_REP_NEW_BOW["plain"] = {"gap_s": 0.09, "frac": 0.3}`. Any unslurred same-pitch string repeat on a sustained row (Sus MAX, Leg rows), not covered by `STR_REP_DETACH` and not inside a "change bow at will" skip span, ends the earlier note min(0.09 s, 30 % of it) before the next note's moved onset. That is EW research batch 4's string median of 90 ms.
- For a same-pitch slur head after a held note or a div. chord (Vln I 884, Vc 832): start the head on Sus MAX as a `SLUR_START_SUS` stroke with the same gap, and join the run from it.

**Targets.** Every listed repeat 5 dB or more (dry stem); violas 820-832 within 2 dB of each other. The pp/p re-bow points (876/880 chord re-bows under "change bow at will") stay as they are.

## 3. Brass accents now have duller fronts than unaccented notes: the swell lands after the attack (item 4; measured, fix inferred)

**Where.** All brass accents, most clearly the horns. The Più allegro and T: Horn 1 1056, 1064, 1088, 1092; Horn 3 1036, 1073, 1081; Horns 1-2 1104-1108; Trumpet 1 1056, 1088, 1096.

**Evidence.** 2-5 kHz front minus body:

| instrument | accented median | unaccented f-ff notes (same instrument, 1 qn or longer) |
|---|---|---|
| Horns | -16.1 dB (123 accents; 984 on: -18.7, p10 -28.9) | Horn 1 -7.7, Horn 3 -10.6 |
| Trumpets | -12.9 dB | Trumpet 1 -9.6 |
| Trombones | -8.1 dB | Trombone 1 -6.6 |
| Tuba | -15.0 dB | |

- Movement I c12 measured -4.2 dB on a real orchestra (comment in its config, cited in MANUAL-GAPS #1).
- Horn 1 at 1056 (ff, entry): the stem rises from -38 dB at the beat to -27 at +100 ms. That is 11 dB of rise after the beat, on top of a 90 ms lead.
- The volume envelope adds +3.2 dB at q+0.02 qn and another +1.8 to q+0.205 qn (`GENTLE_ACCENT` brass `swell_s` (0.07, 0.25, 0.6) s, db 2.5).
- Horn 3 at 1073 / 1081 measures -0.4 / -0.2 dB over its neighbours with a front of -29.7 dB: neither weight nor front.
- The master's tilt p90 is 0.5-1.3 dB in the brass passages (target under +3). There is room for a clearer front without bite.

**Fix (`build/score_config.py`):**
- `GENTLE_ACCENT["brass"]["swell_s"] = (0.02, 0.18, 0.45)`, db 2.5 unchanged. The weight peaks on the attack, not 70 ms after it. A broadband volume change leaves the tilt unchanged (inferred: the tilt subtracts the 0.25-1.5 kHz jump).
- Start the swell at the moved note-on, so it does not begin after a led note's attack.
- Horns only: an extra 0.03 s lead on accented f-ff entries after a rest (`ROW_LEAD_S` span list for Horns 1-4), for the slow 1FH bloom.
- A/B (manual p.106): put the 14 accents inside brass slurs (Trombone 1 985 / 993 / 1001 / 1009 / 1081 / 1084, Trombone 2 1081 / 1084, Horn 3 1076 / 1084) on "Leg Slur Accent MAX" at velocity 50-70, CC1 unchanged. It is present in 1FH, 1TB and 1TU.

**Targets.**
- Accented minus unaccented front within ±3 dB per instrument.
- Level over neighbours 2-4 dB.
- The master's tilt jump p90 under +3.
- Accent pcX within ±40 ms.

## 4. The basses' hammered eighths lilt long-short in two of five spans (S2; measured, cause inferred)

**Where.** Double basses, 816-840 (bars 205-210, accelerando to 184 qpm) and 1088-1108 (bars 273-277).

**Evidence.** Time from the pre-onset minimum to within 3 dB of the local peak (broadband, 5 ms window), on-beat against off-beat eighths:

| span | on-beat | off-beat | swing |
|---|---|---|---|
| 816-840 | +13 ms | +41 ms | 28 ms |
| 1088-1108 | +13 ms | +37 ms | 24 ms |
| 792-816 | | | 8 ms |
| 984-1056 | | | 9 ms |
| 1056-1088 (after c08's CC16 reset at 1056) | | | -11 ms |

- The detach dips before the off-beats bottom out at -14..+7 ms. Before the beats they bottom out at -41..-62 ms.
- pcX reads larger swings (36-54 ms) everywhere except 1056-1088 (-4 ms), but its 8192-point window is coarse at C1-G1.
- So the eighth on the beat sounds about 25 ms long and the off-beat 25 ms short: a slight dotted lilt in the hammered ostinato.
- The only span without it is the one where the round-robin cycle was reset. That the bow-direction samples differ in attack speed is inferred.

**Fix.**
- `build/score_config.py` `RR_RESET_AT["Double basses"]`: add 792, 816, 984 and 1088 (CC16 = 127 just before each span's first eighth), as at 1056.
- Refit the basses' `METRIC_BOWED_DB_SPANS` tables after the render, as c08 did. The reset flips the level cycle too.
- If a span still swings more than 15 ms, use a per-position lead instead: off-beat eighths +0.02 s (`ROW_LEAD_S` span form for Double basses, off-beat onsets only).

**Target.** On-beat minus off-beat attack time within ±12 ms in every span, and down minus off-beat level +2..+4 dB (c08's metric target).

## 5. Keyswitches arrive 7-12 ms before their notes; the research default is 40-800 ms (research default not adopted; inferred gain)

**Where.** All tracks: 2204 keyswitches, median lead 12.5 ms, minimum 7.1 ms (Violas 181.27, 425.98, 555.98, 559.27; Violins I 178.93; Violins II 174.41, 181.23).

**Evidence.**
- FINDINGS Part 2 section 9: EW's template places keyswitches 40-800 ms early (typically 100-600 ms), "almost never on the same tick". BRIEF batch 2 lists this as a default.
- The render shows no wrong-row note in my scans: every row's measured lengths and fronts match its row.
- But a keyswitch 7 ms before a note leaves Opus one 512-sample block or less (10.7 ms at 48 kHz) to switch. If REAPER's block boundary splits them, the note can take the old row (inferred). Nothing measured shows that it does.

**Fix.**
- `tools/score_to_parts.py` keyswitch placement: lead = min(0.10 s, 80 % of the time since the previous note-on on the track, or the previous note's end if later), never earlier than the previous note-on + 10 ms. Keep `ks_clash` empty.
- No level change is expected. Check by diffing per-row note counts and the attack probe against c08.

## 6. "div. a 3" at the final chord is not read as divisi (inferred level effect; patch option for divisi)

**Where.** Violins I, Violins II and violas at qn 1108 (bar 278, fff, tremolo): three-note tremolo chords on the section patches.

**Evidence.**
- `div_entries` in parts.json lists nothing at 1108 for these three tracks. Violins I's last is 968; the violas' last is 1085. The celli's "div." at 1106 is read.
- So the "div. a 3" chord takes no -10·log10(3) = -4.8 dB per voice. Each section sounds three full-section tremolos.
- LEARNINGS kit section 7: a 2-note section tremolo measured +8.2 dB over its single-note fit.
- The final chord's family balance was set by roles and FINAL_RING (critic B's lens), so the level may already be compensated. The texture is three full sections per staff instead of thirds.

**Fix.**
- Make the div parser in `tools/score_to_parts.py` accept "div. a N" (N from the text) and take -10·log10(N).
- Then re-check the final chord's string-to-brass balance against c08 (B) and move the difference into roles, so the climax order (278, 223) is unchanged.
- For "4 soli" (Violins I 472-512) and other soft div. passages, the half-section DIV A/B patches (manual p.89-90, MANUAL-GAPS #7) stay the better library choice. They are only possible in a second-pass session, for memory.

Do not touch:
- The legato data: mono rule, overlap floors 45 / 35 ms, velocity by dynamic with floor 100, and their lead compensation.
- All 152 breath gaps.
- Trumpet 1's open solo: v96, joins -12 ms median.
- The muted Trumpet 1 on Mute Sus, and stopped horns on Stop Sus.
- Trumpet 3 and basses repeat separation (medians 10.9 dB).
- c08's metric basses table and CC16 reset at 1056: no lilt in that span.
- The brass accent levels (+3.1..+3.5 dB, no bite).
- Short rows at 0.50 of the slot.
- The tremolo rows from 888.
- FINAL_RING.
- Percussion on the grid.
- The returns and envelope: tutti -20 dB median 0.40 s.
