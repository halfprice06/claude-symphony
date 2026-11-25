# Cycle 26, critic B (balance and levels), on the c25 render

All levels come from the c25 stems and master (`cycles/c25/render/`), timed on `cycles/c25/parts_rendered.json`. The mp3 numbers come from `mvt3-mockup-c25.mp3`, decoded at 48 kHz, with its 0.30 s head allowed for. "K" means K-like weighting: a 60 Hz high-pass and +4 dB above 1.5 kHz, mono sum. "Active" means only the 10 ms frames where the track has a note sounding. c24 comparisons use `cycles/c24/render/` with `cycles/c24/parts_rendered.json`. The scripts were in the scratch folder, which has been deleted.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 26: its table stops at cycle 20, and the third round sets no fixed pages. So I skipped the full reading. I read `loop/MANUAL-GAPS.md` and, in full, the pages behind my findings.

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Volume (CC7) sets a track's level against the other instruments; Expression (CC11) shapes each instrument's line (p.64; repeated at p.151: CC7 is "best used to set the overall upper limit on the volume of each track"). | Every passage-level balance correction. Under Dan's standing rule these must now be made on the instrument side (findings 1, 2, 4). | Partly. Only the timpani have a CC7 lane (531 points). Passage levels are still REAPER envelope roles, which need their edges in rests, and several inner-line fixes stalled on that. CC7 is the manual's own instrument-side tool for this job. |
| Divisi instruments: "the loudness of a divisi part is not much less than if the whole section were playing the part"; the DIV A/B patches have Close mics only (p.89-90). | Violins I div. in octaves at 632-660 (two notes 81% of the time), the violas' div. chord at 840-846 (100%), the violins / violas held chords at 864-872, the div. a 3 final chord. `CHORD_CUTS` has been False since c16, so each divisi note plays a full-section sample. | The manual says the excess of two full-section samples over a real divisi is small: between about 1 dB (its claim) and 3 dB (half the players). So I do not ask for the old -10 log10(k) chord cut back. Where a divisi chord covers a line, the fix below is a passage level in CC7. |
| Brass sustains: CC1 crossfades 4 dynamic layers, and near 127 opens a low-pass filter for an overblown sound (p.101, p.106; DIGEST section 3). | Trumpets 1-2 at the theme B head (840: CC1 104), the brass arrival at 263 and the final chord (CC1 120). | Partly. The ff head of theme B starts at CC1 104, under the trumpets' own ff median of 108 and the DYN ff of 114 (finding 1). I do not propose CC1 127 at the final chord, because of the overblown filter. |
| Timpani rolls: the CC1 layers set the roll dynamic; the roll should start at its printed level (p.123-126; BRIEF item 5). | The fff rolls at 223 (qn 888) and 278 (qn 1108). | Not at 278. The 1108 roll starts at CC7 36 (-11.0 dB). The 888 roll starts at CC7 97 (-2.3 dB). Same printed fff, 8.7 dB apart (finding 4). |
| MANUAL-GAPS #7: half-section divisi patches (p.89-90). | Same spans as the divisi row above. | Still unused because of memory. Not needed for the levels in this report. |

## 1. Theme B head (bar 211, qn 840): the violas' div. ff chord blooms over Trumpet 1, and the trumpets start under their own ff layer (measured)

**Where:** qn 839.7-846.
- Trumpets 1-2 play the cantabile ff melody (doubled by Flute 1, Oboe 1 and Clarinet 1).
- Violas play a div. half-note chord (61 + 65), ff with a decrescendo to f at 844.

**Evidence (K, 0.5 qn windows):**

| qn | 840.0 | 840.5 | 841.0 | 841.5 | 842.0 |
|---|---|---|---|---|---|
| Violas | -30.9 | -27.7 | -28.0 | -28.5 | -34.6 |
| Trumpet 1 | -32.5 | -31.5 | -34.7 | -30.5 | -27.7 |
| Trumpet 2 | -29.6 | -28.9 | -30.4 | -30.8 | -27.6 |
| Violas minus Trumpet 1 | +1.6 | +3.8 | +6.7 | +2.0 | -6.9 |

- The violas' CC11 falls from 110 to 93 over 840-841.9 for the printed decrescendo. Their level still rises 3 dB after the attack: the Sus MAX body arrives 0.3-0.5 s late.
- Two full-section samples sound for the two divisi notes (manual p.89: about 1-3 dB more than a real divisi).
- Trumpet 1's head note has CC1 104 and CC11 114 falling to 108, and it sags 3 dB at 841.0. The second note (842) carries CC11 91.
- The trumpets' median CC1 on printed ff notes over the movement is 108 (85 notes; DYN ff is 114). So the melody's first bar sits one layer step under ff, while the accompaniment plays its ff on the slope of the layers.
- The c25 result: the melody minus the rest was -3.8 dB at 840 and the violas were 5.2 dB over Trumpet 1. The target was +2 and -3.

**Fix (instrument side only):**
- Trumpets 1-2: CC1 `note_cc` +10 over sq 839.7-846.9, ceiling 116. The head then sits at 114, as printed. CC1 is the brass layer control (p.101). Trumpet 1's CC11 on the 842 note: hold it at the head's level, 108, instead of 91 (`cc_shape` on sq 842; k 20, so +1.5 dB).
- Violas: a CC7 passage level of 90 (-3.0 dB, 20 log10(90/127)) over 839.7-848, back to 127 in the rest after the 846 note. Also make the printed decrescendo reach f by 841.5: CC11 from 107 at the note-on to 88 at 841.5, instead of 93 at 841.9. Below the Sus MAX knee (100-103) that is about 0.7 dB per unit, so the bloom drops by about 3.5 dB.
- Targets: violas minus Trumpet 1 at -1 dB or lower in every 0.5 qn window of 840-842; melody minus rest at 840 +1 dB or more.

## 2. Violins II countersubject (bars 159-165): the gap to Violins I is Violins I's div. ff octaves; a CC1 floor cannot help, because Violins II's CC1 is already at 95-105 (measured)

**Where:** qn 632-660.
- Violins II play the f espress. countersubject in eighths, doubled by Clarinet 1 (mf espress.).
- Violins I play the ff theme, "div." in octaves: two notes 81% of the time, up to 4.
- The theme is also in the flutes, oboes, Horns 1-2 and violas.

**Evidence (K, active, per bar 159-165):**
- Violins I -29.7 / -31.2 / -32.9 / -32.0 / -30.1 / -31.6 / -33.5.
- Violins II -42.4 / -41.8 / -41.8 / -42.3 / -40.5 / -42.7 / -41.9.
- Violins II minus Violins I: -12.7 / -10.6 / -8.9 / -10.3 / -10.4 / -11.1 / -8.4 dB (target -5..-7).

**Lanes in parts.json:**
- Violins II: CC11 88-94 (f, under the 94 layer step), CC1 95-105, velocity 100.
- Violins I: CC11 105-117 (ff, above the Sus MAX knee) and two notes per onset.

So the gap is made of two parts:
- The f-to-ff layer difference: about 8 dB for 88 -> 100 at 0.7 dB per unit, flat above the knee.
- The octave double stops on one section patch: 1-3 dB (p.89).

The scherzo's CC1 floor worked where CC1 sat low on soft legato notes. Here Violins II's CC1 is already 95-105, near the top of the vibrato crossfade, so a floor has nothing to add. I reject it for this passage on these lane values. More CC11 on Violins II would cross into the bright ff layer, against the printed f.

**Fix:**
- Violins I: CC7 80 (-4.0 dB) over 631.8-659.8, back to 127 at the 659.8 edge that Violins II's role already uses (`ROLE_EDGE_XF`). This is a passage level inside the patch (p.64), not a per-note move.
- Leave Violins II's CC11 under 94 and their role at 0.
- Expected: Violins II minus Violins I -4.9..-8.7 dB. Violins I at -33.7..-37.5 then sits level with Horn 1 on the theme (-32.5..-37.2), with flutes, oboes and violas on top of it, so the tune stays on top.
- Clarinet 1 is at the CC11 ceiling (127) on its first notes: leave it.

## 3. The celli's p bass line under the molto cantabile theme (bars 235-238) plays at pp and sits 11 dB under the basses and violas (measured)

**Where:** Violoncellos qn 935.6-948, printed p ("change bow at will"), half and whole notes C3 C3 D3 F2 G2, under the violins' molto cantabile tune. The basses double them an octave lower at the same printed p.

**Evidence (K, active, per bar):**

| bar | 235 | 236 | 237 | 238 |
|---|---|---|---|---|
| Violoncellos | -59.4 | -59.5 | -55.2 | -47.5 |
| Double basses | -48.3 | -46.7 | -46.2 | -48.8 |
| Violas | -49.4 | -46.7 | -46.4 | -48.2 |

- The celli's lanes: CC11 34-36 at 935.6-944, 32-34 after. That is DYN pp (34), not p (46).
- The basses play CC11 46-50 and CC1 55-57.
- Across the movement, the celli's long notes at printed p have a median of -54.4 dB K (29 notes). The violas are at -47.8 and the basses at -47.0. So "p" is 7 dB softer on the celli than on the other low strings. Most of that comes from this passage and from bars 123-124.
- Adler and Rimsky-Korsakov both treat the celli as the pitch of a bass line the basses double. Here the octave below is 11 dB over its own upper octave.

**Fix:** Violoncellos `note_cc` CC11 +12 over sq 935.6-947.5 (lane 34-36 -> 46-48). Start it at the moved note-on 935.63, after the previous note's release (the scherzo's lesson about CC11 raising the previous tail). Expected about +8 dB. Target: the celli within 2 dB of the basses (K) in bars 235-237.

## 4. The climaxes: the final chord's fff timpani roll plays 9 dB under the same roll at 223, and the fff arrival at 263 steps only 0.5 dB over the crescendo (measured)

**Timpani, final chord (qn 1108, bar 278):**
- Printed: fff roll, with crash fff and bass drum ff.
- Timpani CC7 is 36 from 1107.98 (-11.0 dB). At 888 (bar 223, also an fff roll) `TIMP_ARRIVAL_RAMP` starts it at 97 (-2.3 dB), falling to 75.
- First 0.5 qn:
  - at 888 the timpani are -24.0, 7th of 31 stems, 13.1 dB under the master;
  - at 1108 they are -33.1, 22nd of 31, 21.8 dB under the master.
- The crash (-23.5) and bass drum (-27.8) at 1108 match 888. Only the timpani drop.
- BRIEF item 5: a roll starts at its printed dynamic.

**263 arrival (qn 1048, fff after the ff crescendo of 259-262):**
- Master per quarter (K): 1045 -14.5, 1046 -14.2, 1047 -15.3, 1048 -13.7, 1049 -13.3. The fff stands only 0.5 dB over the crescendo's top.
- Per stem, 1048 minus 1046: Violoncellos -4.5, Violins I -1.7, Trumpet 3 -1.1, Trombone 1 -0.8, Trumpet 1 -0.3.
- The brass sum peaks one quarter late (-16.7 at 1048, -14.7 at 1049).
- The brass reach CC1 116 and CC11 106-107 by 1047.5 and step only to CC1 120 and CC11 112-120 at the arrival. With k 20, CC11 106 -> 112 is +0.5 dB.
- On the mp3, 263 over 262 is +0.3 dB.

**The render's hierarchy:**
- Master, first half-bar (K): 223 -10.7, 278 -11.3, 263 -13.5. So in the render, bar 223 is 0.6 dB louder than the final chord.
- The final leads on the mp3 only because the ride rows cut 223 by 8.4 dB against 5.5 at the final.
- After delivery the mp3 reads 223 -11.8, 263 -11.8, 278 -11.3. That is the c25 tie between 223 and 263.

**Fix:**
- (a) `TIMP_ARRIVAL_RAMP` (`build/score_config.py`): add (1108, 1113) with the 888 law, CC7 97 at the note-on, held to the end of the fermata at about 85 rather than falling to 75 (the roll has no printed decrescendo). Expected timpani about +9 dB at 1108, about 13 dB under the master, still under the crash. Check the timpani's 30-150 Hz share of the final chord (Movement I c50 rule).
- (b) The 263 crescendo: a `cc_cap` with `acc_free` on the brass CC11 (Horns 1-4, Trumpets 1-3, Trombones 1-2, Bass trombone, Tuba) over 1043.9-1047.85 at 98. That is about -1.5 to -2.5 dB at the end of the crescendo, because brass CC11 is linear volume. CC1 keeps rising, so the timbre still builds. The arrival lane (112-120) is unchanged.
- (c) The celli's fff whole notes at 1048: the same front shape as the 584 fix (`onset_lead` 0.04 s plus `cc_shape` [(-0.06, +18), (0.035, +18), (0.04, 0)] with `no_pre_cap`), so the new note reaches its body on the downbeat.
- Targets: master 1048-1050 at least 2 dB over 1045-1047; mp3 263 over 262 at +1.5 dB or more; the final chord at least 0.3 dB over 223 on the master before the rides.
- Then refit the delivery ride rows with a smaller cut at 223 (aim -6 dB or less). The final should keep its 0.5 LU lead with less work from the ride.

## 5. The stops after bars 94 and 113 lost their drop in the render, not in delivery: the celli's tail, lifted by the c25 loud_eq bell, rings over a lower Violins I chord body (measured)

**Evidence (master and mp3, drop at +0.3 s after the stop, `stops24.py` method):**

| stop | c24 master | c25 master | c25 mp3 |
|---|---|---|---|
| after bar 94 | 15.8 dB | 13.8 dB | 13.1 dB |
| after bar 113 | 14.9 dB | 14.1 dB | 13.5 dB |

- Delivery takes only another 0.6-0.7 dB. Most of the loss is in the stems.
- At +0.3 s after the bar-94 stop (qn 374.06), the loudest stem is the celli. Relative to the master's level in the 0.15 s before the stop:
  - celli tail -17.8 dB (c24 -20.4); their pre-stop level -10.6 (c24 -13.0);
  - Violins I's pre-stop level -14.1 (c24 -9.9: the c25 LITE region-gain removal, intended).
- So the reference fell by about 1 dB and the celli rose by 2.4-2.6 dB.
- The celli's last note (372, "Leg BC MAX") sits inside the c25 `loud_eq` span 358-378, with a +3 dB, 1.5-octave bell at 160 Hz. The same applies after bar 113: celli tail -25.8 (c24 -27.5), loud_eq span 434-454.
- Loud-frame spectrum (loudest 10% of 0.4 s frames, master against the Dvořák reference):

| band | c24 | c25 | Dvořák |
|---|---|---|---|
| 100-250 Hz | -11.25 | -10.04 | -6.12 |
| above 6 kHz | -24.04 | -25.08 | -28.09 |

  The loud_eq moved both bands by about 1 dB in the right direction. It is worth keeping elsewhere.

**Fix:**
- `build/mix.json` Violoncellos `loud_eq` points: end the two spans before the stops, [..., [372, 1], [373.9, 0], ...] and [..., [448, 1], [449.9, 0], ...] (now 376 -> 378 and 452 -> 454). Alternatively, keep the bell off in those two spans.
- Expected: master stops near c24 (15.8 / 14.9), mp3 at 14.5 or more.
- Keep the other loud_eq spans as they are.

## 6. Fader steps inside notes (standing rule): 30, none at a printed fp or sfp, and 4 of them are per-note moves (measured)

I ran `stepcheck.py` on `parts_rendered.json` (moves of 2 dB or more within 60 ms inside a note): 30 inside, 91 at note-ons, 51 in rests. Each classified against `mockup-events.tsv`:

- **22 are printed dynamics or hairpin ends** that land 0.01 qn after the score onset while the note was led 0.06-0.15 qn earlier. Each step therefore falls inside the attack, by 2.5 to 3.0 dB:
  - Oboe 1 909.9 / 931.9; Oboe 2 913.9 / 931.9;
  - Violins I 295.88 / 775.85 / 909.91 / 913.9 / 949.88;
  - Violins II 295.88 / 531.85 / 775.86 / 909.9 / 913.9 / 949.88;
  - Violas 775.86 / 931.9;
  - Violoncellos 383.85 / 551.85 / 931.9 / 967.9;
  - Double basses 931.9. The basses' step is inside a held note (928-935.2) at the printed mf: it should be a ramp, not a 0.01 qn step.
- **4 are printed player-count marks at the note-on:** Violins II, Violas and Violoncellos at 375.9 ("sul tasto, last 2 desks", -4 dB), and Violins I at 484.9 ("4 soli", -3 dB).
- **4 are not printed and break the rule:**
  - Harp 511.99, +10 dB: the role [488, 512, -10] ends while 4 plucks still ring (506.5-512.6, 507-513.1, 510-516, 510.5-512.5).
  - Violoncellos 15.5-15.9, -6 dB: the role [8.8, 15.9, +6, 0.4] ramps inside the note 15.0-16.0.
  - Violoncellos 1032.0-1032.25, -3 dB: the [1016, 1032, +6] role's end falls inside the led 1032 note.
  - Trombone 2 152.0-152.25, -3.5 dB, at the start of the 8 qn decrescendo note (a hairpin row; no fp printed).

**Fix:**
- For the 22: `vol_guard` with `hairpin_ok` False, or `dyn_step_on` extended to the hairpin-gain resets, so these points move to just before the moved note-on (`pre_s` 0.02). The double basses at 932 get a 0.25 qn ramp instead.
- Harp: replace the role with a CC11 `cc_scale` of -10 dB over 488-512. Harp CC11 sets loudness (p.69). Or end the role after 516, when the plucks have died.
- Celli 8.8-15.9: put the role's end into the 16 chord's moved note-on (`ROLE_EDGE_XF` 15.9: (15.93, 15.96)).
- Celli 1032: end the role at the moved note-on of 1032.
- Trombone 2 152: drop the point, or move it before the note-on.
- Target: 0 unprinted steps inside notes.

## Coordinator's checks (measured unless marked)

- Horns 2 / 4 after "Mono From Left": per pitch, c25 minus c24 is -1.0..+2.2 dB on Horn 2 (E flat 4 +2.2, 13 notes) and -1.0..+1.8 on Horn 4. Medians 0.0 / +0.2. Horns 1 and 3 rendered identical to c24 (0.0 dB on every pitch). Horn 3 minus Horn 4 is unchanged: 888-936 -0.2 (c24 -1.0), 936-948 -3.5 (-3.4), 1016-1048 +2.7 (+2.9). No new imbalance.
- Timpani at 223: -11.5 dB under the master at 888 (target met). At 891 it is -19.9 (2 dB short of -15..-18; leave it). The real timpani fault is at 278 (finding 4).
- The chorale against the string tremolo: 224-225 brass lead the strings by 2.8 / 3.8 dB, and the winds and violins lead in 226-228, as printed. 255-262 brass lead by 0.5-7 dB (Trumpet 2 silent by design).
- Crash at 223 / 263 / 278: -22.3 / -23.7 / -23.5 against the master's -10.9 / -14.6 / -11.3 (first 0.5 qn). Heard, never the top stem.
- f -> ff consistency (long notes, K): brass step 8-11 dB, woodwinds 2.4-4.4, strings 3.4-6.4. That follows the orchestration norm: brass dominate ff.
- Violins I chord fronts, celli repeats, the basses' re-bows, the muted joins and the 888 dips are A and C lens items. I did not re-measure them beyond the actor's `logs/render/meas25.log`.
- Scherzo items:
  - The -9 dB 3:1 peak compressor is not needed if finding 4's in-render fixes land. If the final's lead falls under 0.5 LU after the ride refit, use it (scherzo c22: 0.39 -> 0.61 LU).
  - Crescendo lookahead and CC11 lift after the preceding release apply to findings 3 and 4 (written into the fixes).
  - The CC1 floor does not apply to Violins II here (finding 2).
  - Doubling tracks counted: theme B (trumpets plus winds) and the countersubject (Violins II plus Clarinet 1).
  - Sus Marc LITE on Violins II: not proposed.

**Do not touch:**
- Trumpet 1's open-solo role [200, 264, +3.2];
- the cor anglais / muted trumpet roles 680-744 (cor anglais +6..+13 over the accompaniment);
- the Horn 1 counter-line role 263.72-295.75;
- the harp at 524 (v96) and its velocity path;
- Oboe 1's role at 568-576;
- `TIMP_ARRIVAL_RAMP` 888 / 1048;
- the 40in bass drum at -4.4 dB;
- Horns 2 / 4 Mono From Left;
- the celli Detache spans with their -6.3 / -4.5 levels;
- the chorale brass / string balance 224-234;
- k 20 on brass / clarinet `cc_scale`;
- Horn 3 CC1 +12;
- the loud_eq bells outside the two stop spans;
- the -14 LUFS delivery chain and the mp3 head.
