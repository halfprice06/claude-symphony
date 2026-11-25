# Cycle 30, critic B (balance and levels), on the c29 render

Sources: the c29 and c28 stems and masters (`cycles/c29/render/`, `cycles/c28/render/`), both mp3s, `cycles/c29/parts_rendered.json` and `cycles/c28/parts_rendered.json` (tempo map, notes, CC lanes), `build/mockup-events.tsv`, `build/mix.json` (`return_rides`), `cycles/c29/CHANGES.md` and logs, `loop/MANUAL-GAPS.md`.

How I measured:
- Levels are K-weighted power from 40 ms Hann frames at a 10 ms hop. I used an approximate K curve: a 38 Hz high-pass and a +4 dB shelf above about 1.5 kHz.
- "Rel" means a stem or a group against the sum of the 31 dry stems in the same window.
- "Lead" means a line against the loudest other stem.
- mp3 loudness comes from ffmpeg `ebur128`, with the 0.30 s head removed.
- Stops were measured with the actor's `stops24.py`, run read-only on the two render masters.

All scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c30-B/`. That folder has been deleted.

## Manual notes

MANUAL-READING.md has no row for cycle 30 (third round), so I did no page reading. I used MANUAL-GAPS.md instead.

| What the manual / gap list says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| CC7 sets the track level inside Opus, before the hall send. It works as 20 log10 on these patches (p.64, p.151; GAPS Finale c26-c28). | The c29 roles under the solos at 43-50 and 95-97, the Trumpet 1 Mute Sus pitch gains, and the `ENV_MAX_DB` excess moved into CC7 | Yes. The c29 role cuts measure as written: strings -3 / -4 / -6 dB, exactly, in every bar of 43-50 and 95-97 (table in finding 6). |
| "Leg Slur Accent MAX": accent strength by velocity on a legato note (p.106; gap #1) | The accented slur heads of the trumpets / Horn 1 at 968 and Horn 1 at 818 | Not used, and still untested. The c29 sustain-row crossfades solved the join holes without it. Not for this cycle (finding 3). |
| Channel Routing "Mono From Left" (p.141; GAPS c25) | Horns 1-4, now with spread pans (c29 ruling 5) | Yes. Horn levels moved by 0.4 dB or less. The pans may have taken 0.5 dB off the brass return's tail at bar 166 (finding 2, inferred). |
| Bass trombone's three lowest notes are transposed tenor samples (gap #13) | qn 451.78-459.89 | Unchanged. They are inaudible under the bar 113-115 texture (inferred). Left as is. |

## Findings, ranked by what a listener on earbuds would hear

### 1. Trumpets 1-2 in bars 243-246 (qn 968-984): keep the c29 version. No trim. (measured)

**What the score prints.** At 968, Horns 1-2 have the tune at ff ("molto espr.", accent). Trumpet 1 doubles it an octave higher and Trumpet 2 doubles it in unison, both at f ("molto espr.", accent). Oboe 1 is at f. The strings are at mf, with a crescendo from 972 to ff at 984.5.

**Per note, c28 to c29 (stem dB, measured from 0.15 qn after each note-on):**
- Trumpet 1:
  - 970 / 973 / 978 rise by +5.3 / +3.1 / +8.7 dB.
  - Other notes move by +0.8 to +1.1 dB.
- Trumpet 2: 970 / 973 / 978 rise by +3.4 / +2.2 / +3.5 dB.
- Horn 1: changes by -0.6 to +1.7 dB.
- Master: 968-984 changes by -1.5 to +1.4 dB per note.

These rises are the legato holes being filled. In c28, Trumpet 1's 978 sat 9 dB under its neighbours (-39.9 against -30..-33). In c29 the line is level: 968 -31.0, 970 -28.5, 973 -27.0, 976 -26.8, 978 -31.2, 980 -31.8.

**Balance against the horns (trumpets minus horns, per note 968-980):**
- c28: -1.4 / -5.6 / -0.9 / +2.0 / +5.6 / -9.3 / -2.9
- c29: -1.4 / -1.3 / -0.5 / +3.5 / +5.2 / -2.5 / -2.7

The trumpets were already over the horns at 973-976 in c28 (+2.0 / +5.6). c29 did not create that.

**Balance against the whole texture.** The doubled tune (trumpets plus Horns 1-2) sits 1.7-6.2 dB under the sum of all stems (c28: 2.0-7.3). It does not stick out of the texture.

**Accent fronts.** Front minus body at 2-5 kHz:
- Trumpet 1: -6.7..+6.1 dB (c28 -4.7..+14.0).
- Trumpet 2: -3.6..+2.4 dB (c28 -1.7..+4.5).

The fronts are no brighter than in c28.

**Verdict.** The c29 change removed a dip that a listener would hear and left the passage within 1.5 dB of c28 on the master. A trumpet role cut (for example -2 dB over 967.9-983.9) would bring the trumpets level with the horns at 973-976. It would also put the trumpets 3-4 dB under the horns at 970 / 978 and bring back part of the sag. Do not do it in the last cycle.

### 2. The bar 166 stop drops 17.6 dB on the mp3, 0.6 dB over the band. Fix it with a tail-only return ride. (cause measured, fix size inferred)

**Where.** Tutti cut-off at qn 662 (bar 166 beat 3). The next note is at 663.66.

**Evidence.**
- Master stop (`stops24.py`): c27 17.4, c28 16.7, c29 17.4 dB.
- mp3: c28 16.8, c29 17.6 dB.

The note data near 662 did not change, so I looked at the stems. Over the 0.15 s before the cut:
- Flute 1 rose +1.7 dB and Flute 2 +1.0 (render variance; no ruled change there).
- The master pre-cut level rose +0.6 dB.

At +0.3 s after the cut:
- The winds return fell -0.7 dB and the brass return -0.5 dB. The brass part is possibly the horn pans (inferred).
- The master tail fell -0.3 dB.

**What the tail is made of at +0.3 s.**
- Master: -35.4 dB.
- Sum of the four returns: about -39.0 dB (R Strings -42.9, R Winds -42.2, R Brass -49.5, R Perc -54.8).
- The returns are therefore about 44% of the tail energy.

**Fix.** In `build/mix.json` `return_rides`, change `{"stop": 662.0, "db": 0.0}` to `{"stop": 662.0, "db": 2.0}`. This is the same tail-only mechanism as bars 2 / 6 (2.5 / 3.0 dB). Apply it with `--mix-only`.

**Expected.**
- The tail rises about +1.0 dB, so the mp3 stop goes to about 16.6 dB (inside 14.5-17).
- The pre-cut level does not move, because the ride starts at the stop.
- Loudness, LRA and climax order are untouched, since the ride covers only about 1 s of tail.

**Check.** On the c30 mp3, bar 166 should be 15.5-16.9 dB. If it comes out under 15.5, use 1.0 dB.

### 3. Cor anglais joins 701 / 734 (bars 176 / 184), with dips of 5-6 dB on the stem and 3.0-3.3 dB on the master: leave them. Left for later. (measured)

**Balance in the muted-trumpet passage (bars 171-186).**
- The cor anglais and muted Trumpet 1 together lead every other stem by +9.7..+13.0 dB per 2-bar window (c28 +8.0..+13.0).
- The cor anglais alone leads by +7.5..+12.4.
- The unison trumpet fills both joins on the master, so each dip measures 3.0-3.3 dB there.

**Why not fix it now.** The only fixes are row or lead changes on the cor anglais sustain row. Those carry the risk the c29 range test showed: 701 / 734 got worse while 702 / 706 / 735 / 740 improved. That is not a last-cycle change.

**For a later cycle.** Range-test a lead of 0.06 s and a velocity of 60 (the note before each join is soft on the Sus row) on those two joins only.

### 4. The small c29 leftovers need no change: Flute 1 at 168, the Trumpet 3 pickups, Trumpet 1 at 989. (measured; audibility inferred)

**Flute 1, bars 43-44.** On my 2 qn K-weighted windows, Flute 1 leads by +3.1 / +4.6 / +8.9 / +8.0 dB at 168 / 170 / 172 / 174 (c28: -0.5 / -0.1 / +3.3 / +3.5). The leads of the other two solos, per 2 qn window:
- Clarinet 1 (176-182): +4.5..+11.6 dB.
- Oboe 1 (184-190): +3.6..+11.5 dB.

Every solo window now leads. The actor's -0.3 at 168 comes from a different estimator (the full band).

**Trumpet 3 pickups at 362 / 366 (3.0 dB of separation).** This is an inner trumpet in an ff tutti, and the pickup is already separated from the downbeat. A listener on earbuds would not hear it as a separate line.

**Trumpet 1 at 989 (-1.3 dB against its neighbours).** This is inside normal phrasing.

None of these is worth a change in the last cycle.

### 5. The opening ff chords (bars 1-2, 5-6, and the 584 chord) are string-heavy. On the mp3 they sit only 1.1 LU under the final chord. Left for later. (measured; the balance judgement is inferred)

**Where.** qn 0-5, 16-21 and 584-592. These are the Sus Marc LITE chords on Violins I / II, with the +4 dB row gain from c24-c27.

**Evidence: the strings run hot.**
- At the opening, Violins I / II / celli play at -23.6 / -22.0 / -23.8 dB.
- Their medians for notes printed ff are -29.7 / -29.9 / -31.1 dB, so they are 6-8 dB over.
- Their fff level at bar 223 is -18.1 / -19.5 / -23.9 dB.

**Evidence: the brass sit at their own ff medians.** Horns are at -28.6..-33.7, trombones / bass trombone / tuba at -28.1..-31.7.

**Section balance.** Rel to the sum:
- Violins: -3.2 dB.
- Horns: -10.9.
- Low brass: -8.9.
- Woodwinds: -8.8.

**On the mp3.** Bars 5 / 255 measure -8.7 LUFS. That is 1.1 LU under the final chord (-7.6) and 0.6 under bar 223.

In a German-sixth tutti marked ff (no trumpets), the four horns and three trombones carry the weight. Rimsky-Korsakov's tutti balance (one trombone or trumpet is about two horns, which are about the woodwind) puts the brass at least level with the full strings.

**Possible fix (not for this cycle).** A -3 dB role on Violins I, Violins II and celli over the three chords, edges in the rests. It would move the opening toward the brass and widen the gap between ff and fff. It touches tuned values from c24 (marcato chords), c27 (Violins II marcato) and the bar-1 ride rows. It also changes p10, LRA and the delivery refit. That is too much to verify in one render.

The delivery spec is met now: the final leads bar 5 by 1.1 LU, which is 0.5 or more. This finding should go to the next movement's or the kit's list, with these numbers.

### 6. c29 against c28: nothing to revert. Two shifts are render variance, and one ruled change made the softest bars softer. (measured)

**Method.** I checked per-bar stem levels against c28 for every move of 1.5 dB or more in a bar where the stem is within 30 dB of the master. Every move is a ruled change except these three:
- **Bassoon 1 at 462 (bar 116), -3.4 dB.** The note data is identical. The c28 note was a 6.5 dB pop over its neighbours (-37.3 against -44..-48). It is now -40.7, closer to them. The solo still leads by +4.0..+10.9 over bars 115-121. This is an improvement, not a fault.
- **Violins II at 528 (bar 133), +4.1 dB, and Trumpet 1 at 447 / 448, -4.0 / +1.9 dB.** The notes, CC1, CC11, CC7, keyswitches and envelope are identical (diffed in parts_rendered.json). This is render variance on single notes. The Violins II note sits 6 dB under the sum, and the trumpet notes are inside an ff tutti. Not audible as a fault.
- **mp3 bars 95-98, -2.1 / -0.8 / -0.7 / -1.2 LU (bar 95 now about -28.8 LUFS momentary).** This comes from ruling 2: strings -4 dB and basses -6 dB under Oboe 1's solo. The oboe's own level is unchanged, and its lead rose to +5..+14 dB. A louder accompaniment would only bring back the masking, so keep it.

**Ruled role cuts land as written.** Strings -3.0 / -4.0 / -6.0 dB in every bar of 43-50 and 95-97. Horn 4 -1.9.

**Delivery check (ffmpeg).** c29 mp3: -14.0 LUFS, LRA 10.8 (c28 11.0). The 0.3 LU margin over 10.5 is small. Of the proposals above, only finding 2 is for this cycle, and it does not move LRA. Any other raise of soft passages in c30 must be checked against LRA 10.5.

## Checks that pass (measured; no action)

**Solos over their accompaniment** (median lead per window, c29):

| Line | Bars (qn) | Lead |
|---|---|---|
| Trumpet 1, F2 | 51-66 (200-264) | +9.8 dB (min +7.6) |
| Violins I+II, F2 | 67-82 (264-328) | +4.5 (min +1.1 against the cello counter-melody at 304: both printed mf with crescendo) |
| Bassoon solo | 115-121 (456-484) | +7.5 (min +4.0) |
| Celli espress. over the harp | 123 (488-494) | +5.5 |
| Theme B, Trumpets 1-2 | 211-216 (840-864) | +4.7..+11.3 |
| Muted pair | 171-186 (680-744) | +11.4 |

**Counterstatement, bars 27-34.** The theme group (violas, celli, basses, bassoons, Horns 3-4, tuba) sits at -0.9..-2.4 dB of the sum. The violins' countersubject is at -6.4..-8.5.

**Più allegro, 247-254.** The two theme groups are level (-4.0..-6.7 each). The bass group (basses, tuba, contrabassoon, bass trombone) is at -5.2..-9.4, solid but not covering.

**Chorale, 223-228.** The brass chorale is at -1.5..-2.9 rel. The tremolo violins at mf are at -10..-13. At 900-912 the ff winds and violins rightly lead (-4 / -4 to -6) over the f brass (-7.6..-8.3).

**Chorale in doubled values, 255-262.** The chorale brass is at -3.8..-5.6 rel. The espress. inner line (Horns 3-4, Violins II, violas, celli) is at -2.1..-11.3. The Violins I tremolo is at -8.5..-13.1.

**Percussion and timpani.**
- Timpani in every long roll ranks 7th-29th of 31 stems, at -12..-26 dB under the sum.
- At 1108 (fff) the timpani is 5th, at -12.
- Crash cymbals at the stroke are -4.9 / -8.0 / -8.1 dB of the 2-5 kHz band at 1048 / 888 / 1108, and fall under -15 within 1 s: heard, not dominant.
- The bass drum is -16 / -17 dB K-weighted at 888 / 1108.

**Dynamic mapping, median note level by printed dynamic** (notes of 0.9 qn or more outside hairpins):

| | p | ff |
|---|---|---|
| Woodwinds | -41..-47 | -33..-36 |
| Horns | -45..-47 | -29..-32 |
| Trumpets | (no p notes) | -25..-28 |
| Low brass | | -28..-30 |
| Strings | -44..-47 | -30..-31 |

p sounds like p across the families. The solo roles (Trumpet 1 at p -42.7, cor anglais p -40.9) are intended.

**Loop pulsing.** On the master, the 100-300 Hz band in the held chords (892-936, 1016-1048, 1088-1108) has a 3.95 s autocorrelation of 0.24 or less and a standard deviation of 1.5-2.6 dB. These are the same as c28.

## Findings from the other movements

- **Scherzo c28: hold a crescendo gain to the next decrescendo.** Not needed here. No arrival sag of 1.5 dB or more was found in my lens. In the one place it could matter (strings mf with crescendo against the tune at 972-984), the tune is 1.7-6.2 dB under the sum, and the accompaniment is not level with the tune.
- **Scherzo c28: tenuto quarters on Marc Lng / Portato.** Not used here. Does not apply.
- **Scherzo c28: hard-stick timpani cannot switch back to soft sticks on one instance.** Same here: Timpani Hrd KS plays the whole movement. The rolls are under the texture (above). Left for later (a second-pass soft-stick alias).
- **Scherzo c28: delivery ride rows off ff arrivals.** Our f -> ff is +3.7. Not needed.
- **Scherzo c28: build stops above +23.5 dB envelope.** Already in place (`ENV_MAX_DB` 23.5).
- **Scherzo c29: Mono From Left changes every note.** Applies to Horns 1-4 (Mono From Left since c25). c25 measured no mono losses over 2 dB. A Close-led stereo mix would be a full horn rebuild: not this cycle.
- **Scherzo c29: an mf accompaniment level with an f tune.** Checked at 243 (finding 1). It does not happen.
- **Scherzo c29: tutti tenuto quarters that ring into the next beat; woodwind harmonic gates.** Articulation lens (A). Not measured here.

Do not touch: the sustain-row crossfades at 243, Horn 3 146 / 578 and Horn 1 74 (no trumpet trim); the c29 roles under the solos at 43-50 and 95-97 and Violins I CC1 0; the Mute Sus pitch gains; the horn pans; the ride rows at 223 / 263 / 1079.5 / final and the bar-113 return ride; `ENV_MAX_DB` 23.5; the timpani arrival ramps and roll trims; the crash and bass-drum levels; the room bed.
