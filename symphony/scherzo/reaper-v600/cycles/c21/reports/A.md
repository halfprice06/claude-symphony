# Cycle 21, critic A: articulation and phrasing (on the c20 render)

Material: `cycles/c20/render` stems and master, `cycles/c20/build_render/parts.json` (the data as rendered), c18 stems for comparison, the patch files read with `opus_state.load_oib` (read only). All levels are the mean of the two channels' powers on 5 ms frames. My scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c21-A/` (deleted after this report). "Measured" means a number from the render, parts.json or a patch file; "inferred" means reasoned from those and the manual.

## Manual notes

`MANUAL-READING.md` has no row for c21 ("cycles after c20 pick their own pages"). I read A2 (PDF p.95-99), T1 (p.143-146) and the velocity-trigger pages of A7 (p.161-162, 189-190) in full, because the open items for this lens are string legato, repeated short notes and accents.

| manual (PDF page) | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| p.97 | Repetitions exist only in Violas and Basses: about a dozen tempo-synced pulses in a little over a second, CC11 crossfades 3 layers, velocity ignored | the theme head's repeated eighths are two notes, not a run of repeats | yes, not used; it does not fit two eighths (inferred) |
| p.98 | a legato transition needs no significant gap between the notes; the first note of a phrase has no transition | every string legato join | yes: all 257 string joins overlap by 0.060 s (measured, parts.json) |
| p.99 | legato patches are monophonic by default; CC22 64-127 makes them polyphonic, with a risk of glides between voices | chords on Leg rows | yes: no two notes start together on any Leg row of any track (measured, parts.json) |
| p.99 | Legato Slur Staccato puts a stronger attack on notes with no legato connection | Violins I's slurred eighth pairs | tried in c20 and rejected on measured levels; no change |
| p.99 | Bow Change legato plays the sound of the bow changing direction | slurred lines | Leg BC MAX unloaded since c14 (memory, one row per line); no change proposed |
| p.144 | true-legato velocity sets transition speed: about 50-60 longer and more relaxed, 110-127 tighter; velocity does not change loudness | the dolce trio tune: celli 169-184 play at velocity 80 (27 of 31 notes), Violins I doubling it an octave higher in 177-184 play at 106-112 | partly (finding 6) |
| p.145 | the Repetition script detunes or borrows a neighbouring sample at random; Round Robin Reset (CC36) gives a repeatable order | every round-robin row | yes: CC36/CC16 resets are in use; no Repetition script |
| p.143 | CC5 sets legato/portamento time for the script-emulated legato only, not for true-legato rows | none | not applicable |
| p.162, p.189-190 | an accent can be made by layering a short articulation restricted to velocity 110-127 over a sustain | the 321 printed accents | not used. A KS Master track plays one row at a time, so the single-row equivalent is the "Sus Accent MAX" row of the woodwind KS Masters (finding 2) |

From `MANUAL-GAPS.md`: #2 (repetition rows) stays unusable for two eighths; #3 (spiccato) is in use on Violins I (22 notes) and Violins II (82 notes, in the tuttis); #11 (portamento at bar 214) is in use.

## Findings, ranked by what a listener would hear

### 1. The string staccato rows' shipped releases join the theme's repeated eighths (S1); the 150 ms cap that worked on Violins II's "Stac RRx9" is missing on every other string short row

Where: every statement of the theme head's B-B / E-E eighths (bars 13-28, 29-44, 105-120, 253-276, 305-320, 325-340) in Violins I, Violins II (tuttis), violas, celli and basses.

What is wrong (measured): the AHDSR release of each short row, read from the patch files, is long compared with the 0.114 s between the two eighths:

| track | row | notes on it | shipped release |
|---|---|---|---|
| Violins I | "Staccatissimo RRx9" (V1 Stac) | 164 | 524 ms (8 groups), 1000 ms (1) |
| Violins I | "Stac RRx14" | 94 | 333 ms |
| Violins I | "Spiccato RRx9" | 22 | 318 ms |
| Violins II | "Spiccato RRx9" (tuttis 105-120, 305-320, coda) | 82 | 1718 ms |
| Violas | "Stac RRx9" | 116 | 489 ms |
| Violas | "Staccatissimo RRx16" (tuttis, coda) | 136 | 1000 ms |
| Violoncellos | "Stac RRx9" | 113 | 372 ms |
| Double basses | "Staccato RRx9" | 26 | 1330 ms |
| Violins II | "Stac RRx9", capped in c20 | 112 | 749 -> 150 ms |

Separation of same-pitch eighths 0.5 qn apart, measured as the lower of the two notes' peaks (within 0.11 s of each moved note-on) minus the lowest frame between the peaks. This peak-to-trough form is needed because the string stacs peak 0.07-0.10 s after the note-on; the rt20 "dips" window reads too early for them.

| | c18 | c20 |
|---|---|---|
| Violins II "Stac RRx9" (capped in c20), 19 pairs | 3.9 dB | **6.6 dB** (p10 1.4 -> 4.3) |
| Violins I "Staccatissimo RRx9", 35 pairs | 4.0 | 4.0 (p10 0.7). By passage: bars 13-28 4.7, counterstatement 29-44 **0.7**, tuttis **1.6**, reprise 4.8, coda 4.0 |
| Violins I "Stac RRx14", 10 | 4.8 | 3.9 (p10 0.0) |
| Violins II "Spiccato RRx9", 9 (tutti) | 3.1 | 3.1 |
| Violas "Stac RRx9" 11 / "Staccatissimo RRx16" 6 | 3.5 / 3.1 | 3.5 (p10 -0.6) / 2.9 |
| Violoncellos "Stac RRx9", 19 | 3.6 | 3.6 (p10 0.5) |
| woodwinds "Stac DblTng RRx9" (Fl 1, Ob 1, CA, Cl 2) | | 6.2-8.2 |

The cap was the only change to the Violins II row, and it gained 2.7 dB of separation on the full render. Violins I, which leads the theme, still runs its repeated eighths together in the counterstatement and the tuttis. Violins I is the stem in the theme that a listener follows.

Fix (`build/mix.json`, `sus_release_cap_ms` of each track, the c20 form): add `{"ms": 150, "rows": [...], "any_dyn": true}` for
- Violins I ["Staccatissimo RRx9", "Stac RRx14", "Spiccato RRx9"],
- Violins II ["Spiccato RRx9"],
- Violas ["Stac RRx9", "Staccatissimo RRx16"],
- Violoncellos ["Stac RRx9"] and Double basses ["Staccato RRx9"] at 200 ms (their eighths are less exposed and carry the bass).

The rows have no release-trail groups, so the cap does not touch the hall. Check on the render:
- the same separation measure (target 5.5 dB or more on every string row, as Violins II reached);
- 60 ms peaks (Violins II lost 1.4 dB in c20);
- the master's 20 dB fall at the G.P. (bar 340, c20 0.33 s) and after bar 120 into the sub. p. These two keep the "not too dry" side in view.

Measured: the releases, the dips, the c18-to-c20 gain. Inferred: that the other rows respond as Violins II did.

### 2. Accents add neither level nor shape: accented notes peak 0.3 s after the beat, the same as unaccented ones, and they follow staccatos whose attacks are stronger

Where: the 144 isolated accents that the c20 actor's `acc20.py` reads. 113 of them are a sustained or legato note directly after a note on a short row: the theme head's accented half note after the staccato quarter, at 315, 327, 345, 351, 915, 927, 945, 951 and every statement.

Evidence (measured, c20):
- By the c20 measure (first 100 ms against the two neighbours), the 113 "sustain after short" accents read a median of -1.3 dB. Against the note before them they read -2.1 dB, and against the note after them -0.3. The other 29 accents read +0.3. So the overall median of -0.8 comes from the step from a short row to a sustain row. The CC11 bump is not undersized.
- The accent does not change the note relative to the same context unaccented. Unaccented sustained notes that follow a short note read -1.1 dB on the same measure, and accented ones also read -1.1.
- Shape. Front (30-180 ms) minus body (250-400 ms) on notes of 2 qn or more in the Allegro is -0.9 dB for the 232 accented notes and -1.0 for the 862 unaccented ones. The accented notes reach their peak:
  - +0.29-0.35 s after the beat on Flute 1, Flute 2, Oboe 1, cor anglais, Clarinet 2, Violins II and violas (more than a quarter note at quarter 264);
  - +0.19 s on Violins I, the only track whose accents are front-loaded (+3.6 dB front over body): its theme heads play "Sus Marc LITE".
- Brightness. The 2-5 kHz share in the first 80 ms minus the body's share is -2.2..+0.5 dB on accented notes and -1.1..+0.8 on unaccented ones. There is no bite anywhere, so a firmer front has room under Dan's "weight, not bite".
- Cause (inferred from these numbers and the c15/c16 history): the post-fader swell that once carried the accent (+3.5 dB, full at +0.07 s) is gone under Dan's rule. Its replacement is a CC11 bump of 0.08 s plus 0.20 s, and Opus smooths CC11 over about 120 ms. On a sustain row that bump lands in the sample's own slow rise, which peaks at 0.3 s.

Fix, generic, in order:
- a. `build/score_config.py`, `ROW_CHANGE_ACC_ADD_S`: extend the c20 0.04 s from Flute 1, Oboe 1 and cor anglais to Flute 2, Clarinet 2, Violins I, Violins II, Violas and Violoncellos, with the same `ROW_CHANGE_ACC_SKIP`. In c20, together with +6 CC11, this raised the first-100 ms reading 1.8-2.4 dB. It costs no memory and moves only note-ons. Expected on the medians:
  - Violins I's 23 accents after short notes are at -1.9, Clarinet 2's 8 at -1.8, Flute 2's 6 at -1.1;
  - Violins II's +3.2 group after "Stac RRx9" is already high, so skip Violins II accents whose previous note is on "Stac RRx9".
- b. Range test, woodwinds: the accented sustain notes of Oboe 1 (18 after staccatos, -2.3) and cor anglais (12, -2.4) on the KS Masters' own "Sus Accent MAX" row (OB / EH KS Master key 25, C#0; 6,495 and 4,195 regions, about 0.5 GB together at c02's 4 GB per 92 thousand). Settings:
  - the CC11 bump off on those notes (`_ACC_BY` 0 for them);
  - velocity about 70 at p-mf and 90 at f. The manual (p.101, DIGEST) gives Sustain Accent velocity as the attack's loudness. Movement I c01 measured +4..+7.6 dB front over body with +8 CC11 and +10 velocity, so start well under that.
  - Targets: first 100 ms against the neighbours +1..+2 dB, front-minus-body +1..+3 dB, peak within 0.12 s of the beat, 2-5 kHz first-80 ms share no more than 3 dB over the body's.
  - If it passes, Flute 1 and Clarinet 2 ("Sus Accent", 7,140 / 8,605 regions) next, within the 45 GB cap.
- Do not raise the CC11 bumps again. At the strings' ff rest the bump gives 0.8 dB (c16), and the measured peak shows that it comes late.

### 3. Violins I's slurred eighth pairs on "Detache": the slur now sounds as two separate strokes, with a 9 dB trough between the slurred notes

Where: Violins I's 18 pairs, the `_c20_pairs` list (67, 113, 125, 209, 317, 329, 343, 347, 353, 787, 821, 893, 917, 929, 943, 947, 953, 1001), all inside a printed slur.

Evidence (measured; peak-to-trough between the pair's notes, peaks within 0.11 s of each moved note-on):
- inside the slur: c20 (Detache) median **9.1 dB**, 13 of 16 pairs 7-11 dB; c18 (Sus MAX) 4.5 dB;
- from the pair's second note into the next staccato: c20 1.75 dB, c18 4.8;
- so the gap now falls inside the slur and the join falls across the articulation break, the reverse of what the score asks.
- Example, bar 106 (qn 317), as 10 ms frames: the first note peaks at -24 dB 0.05 s after its note-on and has fallen to -35 by the second note-on. The second note reaches only -28, 0.08 s later.
- Over all 18 pairs the second note's peak comes a median 0.115 s after its note-on (IQR 0.070-0.129), against 0.038 s for the first note. With the same 0.045 s lead on both, the second note's weight lands about 0.07 s late, almost on the next eighth.
- c20's gain is real: holes of 10 dB or more fell from 4 of 12 to 1, and bar 23 went from -13 to -3..-8 dB. It should be kept, with the join fixed.

Fix (`build/score_config.py`, c20 item 2): keep Detache. Change the `LEAD_SET_AT` loop, which now gives 0.045 s to both `q_` and `q_ + 0.5`, so that the second note `q_ + 0.5` gets 0.09 s and the first keeps 0.045. Keep the existing overlap of the first note; Detache is polyphonic, so the first note keeps sounding. Prediction:
- the trough inside the pair falls to about 4 dB or less;
- the second note's peak lands within about 0.03 s of its beat (S2);
- the pair-to-next join stays as it is.

Check the same 12-pair hole count as the c20 range test (no more than 1 of 12). This is a timing change on 18 notes, not a level change. Inferred: the trough size after the change.

### 4. String legato swell: it is a crest followed by a sag, which points to the connected sustain's slow fade-in. The fourth approach is the sustain groups' attack, not the transition or the CC11

Where: string legato joins in all sections; worst at soft dynamics. Violas 726 (+14.0 dB), celli 516 (+11.8), solo 1065 (+9.5), Violas div 1047 (+9.0), Violas 363 / 387 (+9.0 / +8.2).

Evidence (measured):
- Join excess by the critics' measure on the full render: Violins I +2.9 (53 joins), Violins II +2.4 (42), violas +1.5 (44; 6 over 6 dB), celli +1.8 (112; 3 over 6), solo +6.1, Violas div +6.6.
- Across the 257 joins the excess does not correlate with |interval| (-0.35 to -0.01 on the large sections), velocity, overlap (constant 0.060 s), lead or CC11 band. By CC11 band the median is +1.8 to +2.8 dB, with no band clean. This is why per-join velocity, lead and CC11 changes found nothing.
- Median level after the moved note-on of joins into notes of 1.3 s or more, against the old note. Celli (4 joins) and Violins II (2) show:
  - +2.3..+2.5 dB at 0.00-0.10 s;
  - -2..-3 dB at 0.20-0.45 s;
  - back to 0..+1 dB only by 0.7-0.9 s.

  The critics' "body" window (0.15-0.6 s after the beat) sits in that sag. About half of the reported "swell" is the sag, not the crest. Small n; inferred beyond these notes.
- Patch files ("Leg Slur MAX" row):
  - the transition groups ("TLeg") have attack 116 ms, decay 10 s and sustain 1.0, so they play their recorded shape through;
  - the connected sustain groups ("V1s ..." on violas, celli and Violins I; "V2s ..." on Violins II) fade in with AHDSR attacks of 841-1501 ms (violas 1054-1501, celli 1054-1380, Violins II 957-1380).
  - So for most of the first second the join is the transition sample's tail plus a sustain still at a fraction of its level. That explains the crest and sag. It also explains c20's result: "TLeg" -6 dB dug a 10.8 dB hole, because the sustain was not yet there to fill it.
- "Legato3" also crossfades the old note out over 180 ms (FADE_OUT 180, FADE_OUT_VOL 95) and starts the new note at OFFSET 200.

Fix (a range test, the same ranges and starts as c20's R3 violas 714-746 and R4 celli 501-555, control and variant in one pass):
- a generic option in `tools/build_reaper.py`, next to `cap_release`: mix.json `"leg_sus_attack_ms": {"ms": 400, "rows": ["Leg Slur MAX"], "prefix": ["V1s", "V2s"]}`. It sets the AHDSR `attack` of the groups whose regions are all on the row and whose name starts with a prefix. The "TLeg" groups and the detached "1V ..." / "V2 ..." groups stay as shipped.
- Variants: 400 ms and 250 ms.
- Measures:
  - the sag (lowest 50 ms between 0.15 and 0.5 s after the moved note-on, against the old note);
  - the excess against the body at 0.7-1.0 s as well as at 0.15-0.6 s;
  - holes, and the crest at 0-0.1 s, which must not grow.
- Caution: the finale found a 200 ms attack cap on woodwind legato sustains made post-transition holes worse (SHARED-TECHNIQUES 101). The woodwind transition groups fade to 0 (finale c23 report), while these string ones hold at 1.0, so the result may differ; that is why it is a range test. The finale's c23 SSOFFSET test (the connected sustain starting later in its sample) is the related option. If it lands first, try `"legato_speed": {"SSOFFSET": ...}` on the strings with the same measures.

Inferred: the cause. Measured: the shape and the patch values.

### 5. Clarinet 1 "Leg Slur" against "Leg Slur Rep": a valid test design

Where: the trio tune, Clarinet 1 bars 153-168 (qn 456-504).

Evidence (measured, parts.json):
- Clarinet 1's last note before the tune is the 405 B4, sounding 404.85-408.0. The tune starts at 455.79 (moved).
- With `C20_CL1ROW=leg` the "Leg Slur" keyswitch falls in the rest after the 405 note (408.5, c20 CHANGES), 47 qn before R5's start at 453. The range render does not chase it, so both passes played "Leg Slur Rep".
- CC1 and CC11 both have a point at 455.7827, just before the first note, so their state at the range start does not matter.

Fix (actor scripts, no data change):
- start R5 at qn 408.0 for the control and the variant (one pass, the same start);
- render to 505 (about 23 s at the trio and rit. tempi);
- measure only 456-504: body std and range (c20 control: std 2.6 dB, range 11.6), the joins' excess and holes, and S2 against the harp's off-beat chords.
- Add a guard to the range-render writer (`rr20.py`'s successor): for every track in the range, read each variant's parts.json and refuse a start later than that track's last keyswitch before the first measured note. This repeats c17's and c20's lesson; two tests have now been lost to it.

### 6. The trio tune's doubled legato lines play at different transition speeds (manual p.144)

Where: bars 177-184 (qn 528-552). Violins I play the celli's tune an octave higher, "dolce espress.", sul A.

Evidence (measured, parts.json):
- legato target velocities: celli 80 (27 of 31 notes), Violins I 106 (9) and 112 (5);
- the solo of bars 349-356 plays at 82;
- the manual (p.144) gives velocity as transition time (50-60 relaxed, 110-127 tight), with no effect on level.

Fix: `LEG_VEL_SPANS["Violins I"]` (528, 552) at 80, the celli's value, so the doubled joins use the same transition length. Low priority. mockup-kit LEARNINGS section 5 found that velocity did not move crossovers on the 1st Violins KS Master (108 against 124). Measure the joins' timing (pcx) against the celli's on the render and revert if nothing moves. Inferred.

## Not reported

Checked and correct (measured):
- con sordino CC15 on at 445.3, before Violins II's first con sord. note at 501.3, and off at 552.5, where the part prints "via sord." at 552;
- no chords on monophonic legato rows;
- every string legato join overlaps.

Not measured this cycle: pizzicato edges, timpani rolls and harp; no claims made.

Do not touch:
- Violins II "Stac RRx9" 150 ms cap;
- Detache on Violins I's pairs (fix the second note's lead, not the row);
- Violins I theme heads on "Sus Marc LITE" (the only front-loaded accents in the render);
- woodwind "Stac DblTng RRx9" rows (6-8 dB repeat separation);
- the 0.060 s legato overlap;
- con sordino and sul A lanes;
- the c20 ROW_CHANGE_ACC_ADD_S on Flute 1, Oboe 1 and cor anglais.
