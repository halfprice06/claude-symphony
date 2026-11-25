# Cycle 27, critic A: articulation and phrasing (on the c26 render)

Sources: the c26 stems and master (`cycles/c26/render/`), `cycles/c26/parts_rendered.json`, `build/mix.json`, `build/mockup-events.tsv`, `cycles/c26/CHANGES.md` and `logs/`, `tools/build_reaper.py` `vol_points` (read, not run), `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, the Solo Trumpet patch folders on the sample drive, the May 2021 HO manual and `loop/MANUAL-GAPS.md`. All numbers come from my own scripts on the stems (20-100 ms frames, 200-6000 Hz unless stated). "Measured" means a number from these files. "Inferred" means a cause or a fix that a render still has to confirm. Every fix is on the instrument side (rows, leads, note ends, velocity, CC11 / CC1, release caps) or in the dynamic-trim rule. None is a per-note move in the track volume envelope.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 27, so there was no assigned reading. I read the pages behind my findings, and `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.100 (brass Sustain, Sustain Accent, Marcato) | Sustain Accent: velocity sets the attack, the Mod Wheel sets the sustain. Marcato: velocity opens a low-pass filter on the attack, so harder means harsher. | Violins I "Sus Marc LITE" chords (finding 3); brass accents | Yes. Violins I fronts are only +1.2..+3.0 dB over their body in 2-5 kHz, so they are gentle. The fault lies in the other string sections (finding 3). |
| p.104 (brass legato) | A slur needs "no significant gap" and an interval of an octave or less. Legato patches are monophonic. | Trumpets 1-2, Più allegro 984-998 (finding 5) | Yes on the joins. The f-layer targets are weak (finding 5). |
| Solo Trumpet "05 Mutes" folder (installed patches) and MANUAL-GAPS c12 | Only "Mute Sus", "Mute Sus Accent" and "StacSs DblTng Mute" exist, with no muted legato. "Mute Sus" attacks every note fresh. | Trumpet 1 con sordino, 680-728 (finding 1) | Yes, there is no better trumpet row. The legato has to come from the cor anglais, which plays the same tune in unison, and it does not (finding 1). |
| MANUAL-GAPS c22 / c23 (woodwind sustain AHDSR attack 438-738 ms; sustain-row targets 0.06 s early) | Woodwind "Sus MAX" notes start slowly. Played as a target 0.06 s early with no overlap, the sustain row fills the hole. | Cor anglais unison spans on "Sus MAX" (finding 1); Flute 1's run and Bassoon 1 at 514 (finding 6) | Partly. The cor anglais plays its "Sus MAX" notes with no lead and no overlap. Variant C was never tried on Flute 1. |
| Strings LEARNINGS sec. 16 (Sus MAX pp re-bow dips 6-15 dB; release caps) and BRIEF "Soft endings" (350-400 ms at pp/p) | A pp re-bow on Sus MAX dips, and a short pp release deepens the dip. | Basses' pp pedal re-bows, 170.9 / 181.7 / 190.5 (finding 4) | No. The release cap is 150 ms at pp, the new piece has no lead, and the dips are 7-16 dB. |

## Findings, ranked by what a listener would hear

### 1. The muted second theme (bars 171-186) is played detached: the cor anglais re-attacks every slurred note (measured; fix inferred)

**Where:** Cor anglais and Trumpet 1, qn 680-695 and 712-730, "con sord., dolce cantabile", one slur per phrase, printed p.

**What is wrong:**
- Trumpet 1 has no muted legato row, so the cor anglais is the only instrument that can make this line legato. Since c21 it plays these unison spans on "Sus MAX" (keyswitches at 679.97 and 707.77).
- Its notes start exactly on the score onset, with no lead, and each ends exactly where the next begins, with no overlap.
- Every new note therefore opens with the slow woodwind sustain attack while the old note has already gone.

**Evidence (measured):**
- **Cor anglais, alone.** After each note-on the stem falls 6-8 dB for 0.15-0.3 s and then recovers.
  - At 687: -43.3 dB, then -49.8 / -52.1 at +0.04..+0.08 s, back to -47 only by +0.4 s.
  - At 690: -44.6, then -48.8 / -49.5. At 692: -41.9, then -47.3.
- **Trumpet 1, alone.** The joins dip 3.9-7.6 dB: 687 7.6, 688 7.0, 685 4.8, 694 5.1, 717 4.7, 726 4.0.
- **Master** (200-6000 Hz, the minimum around the join against the lower neighbour): 5.1 dB at 687, 3.6 at 688, 4.2 at 690, 4.7 at 692, 5.1 at 719, and 3.4-3.9 at 724-728.
- Twelve of the 22 joins dip 3 dB or more in the master. A slurred cantabile tune is heard as a series of soft re-attacks.
- **What c26's fix did.** The c26 CC11 lifts on Trumpet 1 (685 / 688 / 717 / 726) cannot fix this, because the cor anglais makes half of the hole.

**Fix (`build/score_config.py`), range-tested on 679-731:**
- **A.** Put the cor anglais's slurred spans 679.97-695.75 and 707.77-730.74 back on "Leg Slur MAX". Use the c23 rule (target on "Sus MAX" 0.06 s early, no overlap) only on the notes of 2 qn or more, where c21 measured the legato bloom: 680, 688, 692, 712, 720, 728.
- **B.** If A brings back the bloom, keep "Sus MAX". Give every cor anglais note in those spans a lead of 0.10 s, and end each note 0.10 s after the next note-on. The row is polyphonic, so the two notes cross-fade.
  - Use the `INSTR_POST note_end` and `entry_leads` tables keyed by onset.
  - Hold CC11 flat over each join, with no fall.
- In both variants, leave Trumpet 1 as it is.

**Pass:**
- The cor anglais shows no join with a dip over 3 dB.
- The master's joins in 680-730 dip 2.5 dB or less.
- Cor anglais pcX within 40 ms of the beat.
- In variant B, the old pitch is at least 10 dB under the new one by +0.15 s.

### 2. The dynamic trims run against the printed hairpins on held notes; this is what the 73 "inside_hp" ramps are (measured)

**How the trims work:**
- `vol_points` adds `trim(dyn_at(q))`, and inside a printed hairpin that trim is read as a line.
- The trim tables are U-shaped. Examples (p / mf / f / ff, dB):
  - Horn 1: 10.6 / 2.0 / -2.0 / 2.6.
  - Horn 3: 12.0 / 1.7 / 1.5 / 2.2.
  - Trombone 1: 12.6 / 4.1 / -0.9 / 2.1.
  - Tuba: 10.3 / 4.1 / 0.6 / 1.4.
  - Basses: 8.0 / 3.7 / 3.9 / 7.4.
- Over a held note, a p -> f crescendo therefore drives the fader down by 4-12 dB while CC1 / CC11 rises. A f -> p decrescendo drives it up by the same amount.
- `SOFT_DECRESC_KEEP` 0.5 halves the rise only.

**Is the rate audible?** I rebuilt the trim lanes from parts.json and mix.json without running the tool. I then measured every held note of 1 s or more under a printed hairpin where the trim moves by 1.5 dB or more. There are 295 such notes.
- **Not a per-note move in most cases.** The ramps follow the printed curve over 1-3 s. The instrument's layer change, in the hairpin's direction, is larger, and the stem moves the printed way. Examples: Horn 1 32 +11.6 dB, Horn 4 544 +18.7, Trombone 1 928 -13.1.
- **The audible fault is direction.** On these held notes the stem goes against the print, or barely moves, and the trim's counter-move is the cause or a large part of it:
  - Horn 1 668: stopped, f > p over 2.86 s. Trim +12.6 dB, stem -0.7 dB (flat).
  - Horns 3 / 4 548: stopped sf > p. Trim +8.7 / +7.0, stem **+2.2 / +5.9 dB** (a swell where a fade is printed).
  - Horn 1 324: p < mf. Trim -6.8, stem +1.0.
  - Trombone 1 880: p < mf. Trim -8.1, stem +1.8 (`cresc_trim_hold` with KEEP 0.5 is already on this one).
  - Clarinet 1 304 / 540 / 942: p < mf. Trim -2.2..-2.4, stem +1.2 / +1.0 / -4.3.
  - Flute 1 516: trim -1.9, stem -5.2.
  - Double basses 160 / 376: p decrescendo. Trim +3.6 / +2.0, stem +3.5 / +4.8.
  - Trumpet 1 720: the muted solo's printed crescendo 719-724. Trim -2.2, stem +0.3.
- **Not caused by the trim** (trim travel under 2 dB in the hairpin's direction): Violas 160 (+7.7 dB across a decrescendo, a "Leg Slur MAX" target at v66 rising) and Oboe 1 860 / 910. These are legato blooms. I list them, but the trim fix will not help them.

**Rate limit: no** (inferred).
- A 3 dB/s limit leaves the direction of the counter-move unchanged and only spreads it.
- On crescendos it would leave the trim high at the arrival, so the arrival's next note-on would step down, which reverses the arrival.
- Moving the trims into CC11 changes nothing either. On brass CC11 is 20 log10 volume, the same law as the fader, and it adds an S3 risk at subitos.

**Fix (`tools/build_reaper.py vol_points`, generic, with the Finale value in mix.json):**
- **(a) Decrescendos.** Set `SOFT_DECRESC_KEEP` 0.5 -> **0.0** inside held notes. The trim may not rise inside a held decrescendo.
  - The hold already ends at the first note-on after the hairpin, so the trim's return lands on a note edge, where the next note takes its calibrated p level. guard26 counts that as "edge", not "inside".
  - Expected: Horn 1 668 and Horns 3 / 4 548 fall by the CC1 decrescendo (about -6..-10 dB), and the basses' 160 / 376 decrescendos fall.
- **(b) Crescendos from p or pp on the brass and clarinets** (Horn 1 324, Trombones 1-2 880, Trumpet 1 720, Clarinet 1 304 / 540 / 942): add a CC11 depth on the held note itself. Start CC11 at -4 dB (×0.63; brass and clarinet CC11 is 20 log10) at the hairpin's start and ramp it to the lane value at the hairpin's end.
  - Use `INSTR_POST["cc_shape"]` lane cc11 `from_note` True: `pts [(0, -37%), (hairpin_len_s, 0)]`.
  - That gives the printed direction 4 dB more with no fader move.
  - Do not extend `cresc_trim_hold` to them: holding the trim on a crescendo leaves the step at the arrival (the c15 simulation already found 63 of 104).
- **Pass:**
  - On the 12 notes above, the stem moves in the printed direction by 3 dB or more.
  - guard26 `inside_hp` falls (expected under 50).
  - No new inside move.
  - Arrival steps 91 / 110 / 199 within 0.3 dB of c26.

**The other gate items:**
- The 5 printed dynamic steps on legato overlaps (1.7-4.7 dB) sit inside the transitions' own 5-15 dB moves. On the stems none stands out from the join (Violas 823.5, celli 951.5, harp 951.9, Clarinet 1 135.75). Not audible.
- Celli 870.4 (+4.6 dB under `--strict`) shows no step on the stem: frames at -52.5 / -49.6 / -51.5 dB, the same ±3 dB as the bars around it. Not audible.
- One of them hides a real hole: Bassoon 1 320.1 dips **13-15 dB** at the legato join after the step (-50 -> -65 dB at +0.1..+0.4 s). See finding 6.

### 3. Bar 5 (qn 16) and the ff string chords: Violins II, violas and celli arrive 100-230 ms after Violins I. That, not a bright Violins I, is the 7-10 dB "front difference" (measured)

**Evidence** (2-5 kHz, first 80 ms minus 0.25-0.6 s body):
- **Violins I** is only +3.0 / +1.6 / +1.2 / +2.5 / +2.6 dB at qn 0 / 16 / 372 / 584 / 1104. Its "Sus Marc LITE" front is a gentle accent, within Dan's 2-4 dB.
- **Violins II** is **-6.1 / -9.0 / -1.4 / -3.6 / -5.4 dB**: its front lies under its own body. So the 7-10 dB gap is Violins II arriving late.
- **Time to -3 dB of the body:**
  - At qn 16: Violins I -30 ms, Violins II **+160**, Violas **+150**, celli **+230**, basses +100.
  - At 584 / 1104: Violins II +80 / +80 ms.
- **Data:**
  - At 16, Violins II, violas and celli have **lead 0.0 s** (Violins I 0.085, basses 0.06), on "Sus MAX" at v111.
  - The c26 note-end rule lifts the quarter at 15 for celli and Violins I only.
  - At 584 Violins II leads 0.06 s.
- **Master:** the broad 200-6000 Hz front is 2.0-3.3 dB under the body at 16 / 372 / 584. The tutti chord swells in instead of striking.
- **Why not velocity or row:**
  - v80 on Violins I made the gap no smaller (c26 range: front +7.7 / +6.2).
  - Marcato rows on the lower strings start 13-25 dB late (c24).
  - So the fix is timing on the late sections.

**Fix (`build/score_config.py` `entry_leads` / `INSTR_POST note_end`):**
- Violins II, Violas and Violoncellos at 16.0: lead **0.12 s**. End the quarter at 15 0.13 s early, a lift like Violins I's, so the onset falls in a rest and `ROLE_EDGE_XF` stays in the rest.
- Violins II at 584.0 and 1104.0: lead 0.06 -> **0.12 s** (LEARNINGS: Hollywood Strings entries need 0.12 s at the slower layers).
- Keep Violins I's "Sus Marc LITE" at v92.

**Pass:**
- Each section's -3 dB point within 40 ms of Violins I's at 16 / 584 / 1104.
- Violins II front minus body -2 dB or higher.
- The master's front within 1 dB of its body.

### 4. Double basses' pp pedal, bars 43-50: each re-bow digs a 7-16 dB hole, then swells over its old level (measured; values partly inferred)

**Where:** the B flat pedal, "Sus MAX" v45, pieces 170.859-181.646, 181.676-190.503 and 190.533-198.877. Each new piece starts 0.03 qn after the old one ends, with no lead.

**Evidence** (30-150 Hz, 0.1 s frames from 0.5 s before the re-bow):
- 170.9: -52 / -54, then **-70.1** at +0.3 s, then -52.5 at +0.9 s (1.5 dB over the level before the re-bow), then -56.
- 181.7: -60, then **-67.5** at +0.6 s, recovering by +1 s.
- 190.5: -58, then **-66.4** at +0.4 s, then -55.5 (+2.5 over the level before).
- **What c26's shape did.** The c26 CC11 shape (`rebow_cc11.json`, -14 units from +0.45 to +1.9 s) acts after the hole. It also sits on a CC11 lane already at 17-32, below the Sus MAX knee, so it cannot reach the 0.9 s peak. That is why the rises did not move.
- **Cause.** The 150 ms pp release cap (`sus_release_cap_ms` strings, dyn includes "pp") lets the old piece vanish before the new piece's slow pp attack comes in (LEARNINGS sec. 16: Sus MAX pp re-bows dip 6-15 dB for about 0.9 s).

**Fix:**
- `build/mix.json` `sus_release_cap_ms`: give Double basses its own pp / p cap of **400 ms**. The BRIEF's soft-endings rule already asks for 350-400 ms at pp / p, and this is Movement II's c41 value. Keep 150 ms at mf-ff.
- Lead each re-bow piece **0.10 s** (old piece still ending 0.03 qn before the new note-on: no same-key overlap).
- Then refit the re-bow shape on the render with `fit_rebows.py --cc11`. Shape the first 1.0 s of the new piece only, not +0.45..+1.9 s.

**Pass:**
- Each re-bow dips 4 dB or less in 30-150 Hz.
- No rise over +2 dB above the level before the re-bow.
- The pp ends of bars 50 / 66 still fall 10 dB in 0.20-0.40 s (BRIEF reference).

### 5. Più allegro, bars 247-250: the trumpets' legato targets sit 8-12 dB under the slur's head; the tenuto is not the softest note (measured)

**Evidence** (each note's p90 level, Trumpet 1 / Trumpet 2):

| qn | 984 (head, v83) | 987.5 | 988 | **989 (tenuto)** | 991 | 993.5 | 994 | 995 |
|---|---|---|---|---|---|---|---|---|
| Trumpet 1 (dB) | -31.8 | -41.9 | -44.1 | **-33.9** | -38.9 | -41.8 | -43.4 | -42.6 |
| Trumpet 2 (dB) | -37.0 | -43.2 | -42.6 | **-35.7** | -41.2 | | | |

- With its CC11 +24 the tenuto is the loudest note after the head, not the softest: +5 dB over 991, which is weight without a spike. CHANGES' "softest" reading does not hold on this measure.
- The weak notes are the "Leg Slur MAX" targets at CC1 89-91 (987.5, 988, 993.5-995), 10-12 dB under the head.
- Horn 1 and Oboe 1 play the same figure within 4.6 / 7.4 dB.
- The same row at CC1 108-115 (840, 1056) matches its head (c26 A).

**Fix (`build/score_config.py`):**
- Trumpets 1-2: CC1 `note_cc` **+12** over 984.5-999.9, ceiling 110. This is the ruling-5 mechanism used at 839.7-846.9; on these KS Masters CC1 is the dynamic layer.
- Reduce 989's CC11 bump from +24 to **+12 units**, so it stays at most +3 dB over its neighbours once they rise.

**Pass:**
- Per-note range over 984-998 6 dB or less on each trumpet.
- 989 0-3 dB over the mean of 988 / 991.
- The 2-5 kHz accent front of 984 still under +4 dB.

### 6. Soft wind solos: three holes left, with untried variants that fit them (measured; fix inferred)

**Flute 1 run, bar 43 (169-174).**
- Unchanged: 170 -4.4 dB, 173 -6.8 dB (c26 CHANGES).
- Variants A (v90 head) and B ("Leg Slur Runs") were tried and failed. **Variant C was never tried on the flute** (T2 put C on Clarinet 1 and Bassoon 1 only). C fixed the clarinet's 177.5 / 178 holes in this same passage.
- **Fix:** `C26_WIND` "Flute 1:C" with the weak targets 169.5, 170.0 and 173.0 on "Sus MAX", 0.06 s early, with 0.011 s overlap.

**Bassoon 1 at 514 (bar 129, tied into the crescendo).**
- The stem falls from -46 to **-57.7 dB** at +0.08 s around the join.
- The target is **v60** with a **0.616 qn (0.22 s) lead**. It follows a half note, so the c26 rule (targets after a quarter note) skipped it.
- **Fix:** 514 at v100 with the 0.168 qn lead of its neighbours, and the half note at 512 ending 0.098 qn after the new note-on.
- **Pass:** dip 5 dB or less.

**Bassoon 1 at 320 (bar 81).**
- 13-15 dB dip at the legato join, with the p > cresc trim step on the overlap.
- **Fix:** the same treatment as 514. List it in the bassoon's variant-C targets (sustain row 0.06 s early).

## The coordinator's list, through this lens

**Hairpin ramps, 5 legato-overlap steps, celli 870.4.** Finding 2: audible as direction faults on 12 notes, not as steps. The fix is KEEP 0 on decrescendos plus a CC11 depth on soft crescendos, not a rate limit.

**223 against 263.** Both are printed fff in every staff. 223 has a bass drum ff, and 263 is approached from the ff of 1032 with a crescendo (Fl, Hn 1040). The score gives no order between them, so a tie is correct to the print. 263 over 223 by 0.1 dB is not audible.
- The +0.8 dB step at 263 is small because 262 is already the top of a printed crescendo.
- Through this lens, 263 needs a clearer attack, not more level. The 0.05 s caesura and the 0.06 s string lift exist. The crash and the brass re-attack carry it.
- Not re-measured here.

**Violins I marcato fronts.** Finding 3: Violins II, violas and celli arrive late. Violins I itself is fine.

**Basses' pp re-bows.** Finding 4: the hole comes before the swell, and the release cap causes it.

**Muted Trumpet 1 joins.** Finding 1: the cor anglais makes half of each hole.

**Trumpet 1 989.** Finding 5: not the softest on my measure. The targets around it are the weak notes.

**Bassoon 1 514.** Finding 6.

**Flute 1 run.** Finding 6: variant C is untried there.

**Violas over Trumpet 1 at 840-842, celli under the basses at 235-237.** Balance lens; not re-measured here.

**Listening through on earbuds,** in the order a listener would notice:
1. The muted cantabile line pulsing note by note (171-186).
2. The bar-5 chord smeared by the late lower strings.
3. The held horn notes that swell where the print fades (bars 138 and 168).
4. The basses' pedal holes in the transition, which is very quiet otherwise.
5. The trumpets' f line at 247-250 dropping away after its first note.

**Other movements' findings:**
- **Violins I short-row ringing (scherzo):** does not apply. The isolated "Staccatissimo RRx9" notes fall to -19..-23 dB of their peak by +0.3 s (qn 574, 1102).
- **Pizzicato basses over celli (scherzo 7.4 dB):** smaller here. Median pluck peak in bars 51-66: basses -47.3, celli -51.1 dBFS (3.8 dB, peaks, with the basses an octave lower). Not a fault at this size.
- **Soft slurred string pair separation, CC1 floor growth (scherzo c23):** consistent with the Violas 160 bloom in finding 2 (a soft "Leg Slur MAX" target rising 8 dB). Not acted on here.
- **Celli 6+ semitone legato leaps late:** not measured.
- **Room bed:** not in this lens.

## Other checks that passed (measured)

- **Hammered and repeated eighths:**
  - Double basses 792-840: 82 repeats, median separation 9.3 dB, 1 under 3 dB.
  - 984-1080: 161 repeats, median 12.5 dB, none under 5.
  - Contrabassoon 792-840: median 8.6, none under 5.
  - Violas: median 6.3 / 9.6, none under 3.
  - Trumpet 3 984-1080: median 4.8 (1 of 9 under 3).
- **Violins I "Sus Marc LITE" fronts:** +1.2..+3.0 dB in 2-5 kHz, and the master's 2-5 kHz front -1.8..+0.2 dB at the five chords. No bite.

**Do not touch:**
- The basses' "Stac On Bow" hammered eighths with metric velocities.
- Violins I "Sus Marc LITE" at v92 (its front is right; fix the other sections' timing).
- The c26 celli Détaché resets and gaps.
- Oboe 1 "Leg Slur Runs".
- Clarinet 1 and Bassoon 1 sustain-row targets.
- The chorale's re-tongue gaps.
- The stopped-horn rows (keep the row; fix the trim).
- Trumpet 1 on "Mute Sus" (no better row exists).
- The harp's Harmonics / Gliss rows and étouffez cuts.
- The tremolo rows at 888 / 1088 / 1108.
