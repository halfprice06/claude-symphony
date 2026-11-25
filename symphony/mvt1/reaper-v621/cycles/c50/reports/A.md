# Cycle 50, critic A: articulation and phrasing

Under review: the c49 render (`cycles/c49/render`, `cycles/c49/rendered_build/parts.json`) and the current `build/parts.json`, which is the c49 data. c50 adopts the EastWest template mix (`build/mix_template50.json`). c51 applies the MIDI rules. For each change below I say which cycle it belongs to.

## Manual notes

This is the second round (cycles 48-51), so there are no fixed pages. I read the pages behind my lens's top open problems: repeated-note separation, the coda bass pedal's bow alternation, short notes and legato rules. The patch reads came from the installed `.oib` files, decoded with `opus_state.load_oib`.

| Source (PDF page) | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| 2021 p.91 | Sustain: bow direction is a round-robin cycle that alternates up and down bows. | Every Sus MAX stroke and repeat. | Yes. It is the cause of the coda pedal's alternation (finding 3). |
| Patch, Basses KS Master | Sus MAX has 4 dynamic layers in two sets: RR index 0 "Dn Bow" and RR index 1 "Up Bow", start mode `RoundRobin` with `tolerance` 22. No other start condition. | Coda pedal, bars 167-170. | Read only. |
| 2021 p.91-92 | Marcato Sustain plays a marcato sample on top of the sustain samples, for "extra power at the start of the note". | Coda pedal downbeats (finding 3). | Used on the celli at 84 / 448 / 456 only. |
| Patch, Basses "Marc Sus LITE" | Marc Shrt attack samples (rrx1 / rrx2, group volume 0.67) in three velocity zones: 1-60 (mp), 61-102 (f), 103-127 (ff). They decay to 0.001. Under them are pp / ff sustain layers with a 368 ms attack and the same Dn / Up RR. | Finding 3. | Not used on the basses. |
| 2021 p.145, 2025 p.92, Opus p.29-30 | "Opus remembers which sample should be played the next time a note sounds." A reset (the Preferences CC, 16 here) forces the order. | Finding 3. | The CC16 reset is in the pre-roll. c49's four instances contradict a per-note count (finding 3). |
| 2021 p.92-94 | Short bows (staccato, staccato on bow, staccatissimo, spiccato) are RR instruments with 9-16 takes. "Unlike most instruments in the Short folder", Repetitions has release trails, so the shorts do not. | String Stac rows (finding 4). | Partly. Celli shorts fill 92% of the slot. |
| Patch, Celli KS Master | Stac RRx9 groups have 6 velocity zones (1-36, 37-68, 69-89, 90-104, 105-117, 118-127), Velocity->Volume at intensity 0.6, an AHDSR release of 372 ms (Stac On Bow 489 ms) and no CC11 in the group. CC11 acts only through the Global Group volume table: CC 58 = -6.9 dB, 72 = -5.5, 88 = -3.5, 114 = -1.0 against 127. | Finding 4. | No. Shorts are attenuated twice (finding 4). |
| 2021 p.94, p.98 | Repetitions (Violas, Basses): a dozen tempo-synced repeats with bow reversals inside one sample. No velocity response; CC11 crossfades 3 layers. | Considered for the bass pedal. | Not recommended: the internal rate is unverified (c42 deferred it), and the pedal is in eighths. |
| 2021 p.99, p.112 | A legato transition needs "no significant time gap" between notes and an interval within an octave. Legato is monophonic unless CC22 says otherwise. | All legato rows (finding 6). | Yes. Overlap is 19-21 ms everywhere, and no chord reaches a mono legato row (measured: 0 chords on legato targets). |
| 2021 p.144 | True legato: velocity sets the transition time (50-60 longer, "allowing the melody to breathe"; 110-127 shorter) and not loudness. | Legato velocity (finding 5). | Strings and brass play 124 (90 when soft). Winds play 60-100, set by note length rather than dynamic. |
| MANUAL-GAPS open items | #5 expressive wind rows, #7 half-section divisi, #9 horn portato rows, #12 Felt Cresc, #13 bass trombone. | — | Still open. I rank them below the items here for c50 and c51. |

## Plan sections this lens touches, and what is not yet applied

Measured on the current parts.json:

- **Section 5, legato overlap 45-80 / 33-58 ms:** not applied (19-21 ms).
- **Section 5 / 8, legato velocity 90+ following the dynamic:** strings and brass meet the floor. Winds do not: 42-54% of joins are under 90 on Flute 1, Oboe 1, Clarinet 1 and Bassoon 1, and 63% on Bass clarinet.
- **Section 8, repeated-note gaps 60-100 ms:** applied on winds and brass (60-140 ms). Not applied on strings (10-19 ms).
- **Section 6, shorts with CC parked at 118-127 and dynamics by velocity:** not applied.
- **Section 10, beat-position short velocity:** not applied.
- **Section 10, spiccato length 50-62%:** met on violins and violas (50%), not on celli (92%).
- **Section 10, doublings share one curve:** met in CC11.
- **Section 6, two tracks per string section:** not applied, and I do not recommend it for c50 or c51.

## Findings, ranked by what a listener would hear

### 1. Repeated string notes run together (Dan's S1). Gaps are 10-19 ms against the plan's 60-100 ms. c51, with a baseline measurement in c50

**Where.** The Allegro's repeated-note string figures, all REP_SPLIT strokes or `STR_REP_DETACH` spans on Sus MAX or the Stac rows:

- Double basses: 104-124, 324-328, 520-536, 554-568, 664-676.
- Violoncellos: 464-484 (bars 117-121, the measured-tremolo 16ths) and 504-520 (bars 127-130).
- Violas: 86-100, 440-468, 552-568.
- Violins II: 86-100 and 536-548.

**Measured.** In parts.json the gap from each note-off to the next same-pitch onset is 14 ms on the basses (eighths at 126 bpm: 0.47 qn notes, 0.03 qn gap), 10 ms on the celli, and 17-19 ms on the violas and Violins II. Across all string repeats the median is 19 ms; 554 of 838 are under 60 ms and 461 under 30 ms. These counts include re-bow pieces and held common tones as well as written repeats. Winds and brass sit at a median of 100 ms (43 of 294 wind repeats under 60 ms; 9 of 260 brass).

On the c49 stems I measured each repeat's dip: 10 ms RMS minimum within -80 / +50 ms of the next onset, against the quieter of the two note bodies. In the master I measured the same thing in the instrument's band.

| Run | Gap | Stem dip, median | Dips under 3 dB | Master-band dip |
|---|---|---|---|---|
| Basses 104-124 | 14 ms | 3.7 dB | 14 of 34 | 4.9 dB |
| Basses 520-536 | 14 ms | 6.6 dB | 9 of 28 | 6.6 dB |
| Basses 554-568 | 14 ms | 4.6 dB | 8 of 21 | 5.3 dB |
| Basses 664-676 | 14 ms | 3.4 dB | 11 of 23 | 4.6 dB |
| Celli 464-484 | 10 ms | 2.9 dB | 41 of 79 | 2.9 dB |
| Celli 504-520 | 10 ms | 5.1 dB | 8 of 39 | 2.8 dB |
| Violas 86-100 / 440-468 / 552-568 | 18-19 ms | 4.6-4.8 dB | 1-2 per run | 2.2-3.1 dB |
| Violins II 86-100 | 19 ms | 4.0 dB | 2 of 9 | 3.2 dB |
| Violins II 536-548 | 19 ms | 2.7 dB | 5 of 8 | 2.9 dB |
| Contrabassoon 104-120 / 520-532 (60 ms) | 60 ms | 7.0 / 6.8 dB | — | 7.9 / 7.5 dB |
| Horn 3 / Trombone 1 / Trumpet 2 (100-110 ms) | 100-110 ms | 7.1 / 6.9 / 13.0 dB | — | — |

The string figures are the weakest repeats in the piece, which matches Dan's S1 note. The same patches already separate well when given a gap: the c44 `STR_REP_NEW_BOW` 0.06 s gap took stem dips from 2.2-2.9 to 3.9-7.8 dB (MANUAL-GAPS Results c44). Row changes did not help: Marc Shrt, Detache and a 250 ms release cap all failed on the basses' eighths (loop/LEARNINGS c03, c13, c22).

**Inferred.** c50's returns are post-fader and use the full 3.3 s IR at a -5.6 dB send. The c44 hall was an Opus hall shortened to endPos 0.5 at fx_volume 0.095. The new returns should fill these dips more in the master, so S1 will probably get worse in c50 before c51 fixes it.

**Fix for c51.** In `tools/score_to_parts.py`, give `REP_SPLIT` (the run detection near line 2112; strokes and MEAS_TREM notes take its path) the same note-end rule `STR_REP_NEW_BOW` uses: a stroke followed by a same-pitch stroke ends min(gap_s, frac × slot) before the next moved onset. Proposed keys:

```python
REP_SPLIT["gap_s"] = 0.08
REP_SPLIT["frac"] = 0.35
REP_SPLIT["gap_min_s"] = 0.06
```

That gives 80-83 ms on eighths at 112-126 bpm (notes about 0.32 qn of 0.5) and 80 ms on quarters. 16ths and triplets on Stac rows take finding 4's length rule instead.

- Keep the `STR_REP_DETACH` spans and their +1.5 dB `LEVEL_SHAPES` for the first render. Their dip window now falls in the gap, so it shapes the release; re-balance after.
- The 150 ms mf-ff release cap leaves a real gap at f. At p the 350 ms cap and the basses' 600 ms cap will fill most of it, and that is acceptable on soft pads.
- Leave out same-pitch common tones in soft held chord changes (Violas 188-213, gap 3 ms at CC 40-72). There the hold is correct.

**Pass criteria.** Stem dip median at least 6 dB on every listed run, at most 10% of dips under 4 dB, and master-band dips at least 4 dB on the violas, Violins II and celli. Moved onsets stay where they are, so no pcX change is expected.

**For c50.** Run the same dip measurement on the c50 render as the baseline for c51. Method: 10 ms RMS on the stem; minimum within -80 / +50 ms of the moved onset, against the median body of each note; master band-passed to 40-200 Hz (basses), 100-800 Hz (celli), 150-1500 Hz (violas), 250-3000 Hz (violins).

### 2. The template's brass EQ makes brass 6.5 dB brighter relative to its body, which risks the harsh accents Dan heard. c50

**Where.** Every brass track in c50 (`family_eqs["brass"]` in `build/mix_template50.json`). The accents most at risk are bars 23-26, 32-33, 131-138, 142-143, 160 and 167-170.

**Measured** (RBJ biquad responses of the template bands, averaged over each band):

| Family | Body, 0.5-2 kHz | 2-5 kHz | Brightness change |
|---|---|---|---|
| Brass | -7.5 dB | -1.0 dB | +6.5 dB |
| Strings | -3.2 dB | -1.7 dB | +1.5 dB |
| Woodwinds | -4.6 dB | -2.7 dB | +1.9 dB |

The brass bands are -5.4 dB at 475 Hz and -7.8 dB at 821 Hz, both 1.92 octaves wide, plus +4 dB at 7.49 kHz. Balance critics will raise the brass to restore its loudness, which lives in the body band. That leaves brass 2-5 kHz about 5-6 dB higher in the master than in c49.

**c49 baseline (measured).** Over 88 brass accents of 0.5 s or longer:

- 2-5 kHz energy in the first 80 ms, minus the same band over the body (+0.15..+0.45 s): median -15.8 dB, worst -2.3 (Trombone 1, qn 521).
- The master's 2-5 kHz jump at the accent against the 140 ms before it: median -1.7 dB, p90 +0.5.
- Strings: front minus body median -9.9 dB, worst +5.8 (celli 536); master jump p90 +4.0.

So "weight not bite" holds at c49. The front-minus-body measure is within one band, so the EQ does not change it. The master jump does change.

**Fix for c50.**

1. Keep the Trombone 1 / Trombone 2 / Bass trombone 4 kHz -4 dB high shelves. They are c21 anti-bite fixes on HISTORY's do-not-touch list, not duplicates of the family EQ. Keep the Bass clarinet 2.5 kHz -4 dB shelf for the same reason.
2. Drop the Trumpet 1-3 and Trumpets a2 +2.5 dB 4 kHz shelves. They stack on the family's +4 dB shelf, and c49 already left the a2's 8-16 kHz share 1.7 dB over target.
3. After the render, measure the master 2-5 kHz jump at each brass accent of f and louder. `tools/fit_accents.py --family brass` prints the stem 2-5 kHz front.
4. If the jump p90 exceeds +2 dB (the c26 limit that fixed Dan's note), or any climax accent exceeds +4 dB, change the brass family EQ's 821 Hz bell from -7.8 to -4.0 dB. Or add a fifth band, a bell at 3.2 kHz of -3 dB with 1.5 octaves bandwidth (the c49 Trumpets a2 bell took 2-5 kHz against 0.5-2 kHz from -5.6 to -7.9 dB). Do not raise the GENTLE_ACCENT swells to compensate.

**Also for c50.** Every re-bow shape in `build/rebow_fills.json` was fitted with the Opus hall and the old mics; LEARNINGS 6 says to refit after any mic or hall change. c49 re-bow state (measured, `cycles/c44/actor_scripts/rebows44.py`): dip medians 1.3-2.8 dB, step medians 0.5-1.1 dB. The rows already outside dip 5 dB / step 3 dB:

- Violins I: 44.0 (dip 6.5), 48.0 (step -6.1).
- Violins II: 47.0, 292.0.
- Violas: 576.0.
- Violoncellos: 26.516 (dip 7.8), 180.0 (dip 8.1, step +3.8), 289.145, 721.869.
- Double basses: 26.0, 38.0 (step -6.0), 42.0, 47.0 (dip 9.1), 52.92, 166.01, 495.114, 506.408 (step +7.9).

After the c50 render, re-run that script and refit with `fit_rebows.py` only the rows over 5 dB dip or 3 dB step. Check first whether a step is a printed hairpin.

### 3. Coda bass pedal: put the twelve downbeats on "Marc Sus LITE". A CC16 reset or a silent extra note cannot move the strong stroke. c50 test alias in pass 2

**Where.** Double basses, the f C2 eighths at 664-675.5 (bars 167-169, crescendo 672-676). All 24 notes are on Sus MAX at velocity 83-90, 0.47 qn long with a 14 ms gap, with no accent printed.

c48 measured the off-beat bow 2.9 dB stronger with about 95 ms earlier perceived attack. The main track now carries c48 level shapes: downbeat pcX +14 ms, off-beat -41 ms (c49 CHANGES).

**Why not a CC16 reset at 663.9 (measured by equivalence).** c49's "Cb pedal C" was a fresh instance with the pre-roll CC16 reset and 664 as its first note. That is exactly the state a reset inside the music would create, and it rendered the same strong off-beats as the main track.

**Why not a silent extra note (measured, then inferred).** I counted C2 note-ons on any row before 664 in `cycles/c49/rendered_build_pass2/parts.json`. In the main track 664 is the 68th; in alias A the 3rd, in B the 2nd and in C the 1st. Counted on the Sus MAX row only, the positions are 62nd, 2nd, 2nd and 1st. Every instance played the same phase. So the phase at 664 does not follow a per-note count, either per key or per row, which the 2025 manual's description (p.92) would predict. Adding one note changes the count by one, and the count already varied across instances without effect, so I expect no change.

**Why Marc Sus LITE (manual p.91-92, patch read).** The row adds a decaying Marc Shrt attack sample over pp / ff sustains that fade in over 368 ms. That gives the downbeat a defined front whatever bow direction the sustain plays. The same row type passed on the celli: 84 / 448 / 456 with time under the body 64 / 124 / 364 -> 0 / 0 / 84 ms and pcX +2..+19 ms (c47-c49). It failed once, on violas 372. In the basses patch the row is called "Marc Sus LITE", not "Sus Marc LITE", and it is loaded by default.

**Test (c50, pass 2).** One test alias, "Cb pedal M", source Double basses, window 613.5-680. That is c49's rest-to-rest window "Cb pedal A"; c49 lesson 5 says to place alias windows from rest to rest. Its tables:

```python
"ART_SPANS": {"Double basses": [{"from": q, "to": q + 0.01, "art": "Marc Sus LITE",
                                 "vel_by_cc": [(88, 45), (114, 55)]}
                                for q in (664.0, 665.0, ..., 675.0)]}
```

That is 12 entries, velocity in the mp attack zone 1-60. Also:

- Leave out the c48 pedal level shapes inside the alias, as c49 did.
- Add no extra lead at first; refit per onset from pcX.
- `alias_check.py` must say OK apart from the key under test.
- Compare with the c50 main Double basses stem using `cycles/c49/actor_scripts/pedal49.py`.

**Pass.**

- Downbeat minus off-beat front level (40-300 Hz, first 80 ms) at least +0.5 dB on 9 of 12.
- Downbeat pcX within ±30 ms.
- Downbeat 2-5 kHz first 80 ms minus body no more than 2 dB above the off-beats'.
- Adjacent off-beats within 1.5 dB of each other. The Sus MAX cycle then runs only on the off-beats, and if it alternates among them, every other off-beat stays strong.

If it passes, move the entries into the main `ART_SPANS` in c51 and refit the pedal's level shapes.

### 4. String shorts: CC11 attenuates them on top of loud velocity layers; no beat weight; celli 16ths fill 92% of the slot. c51 pass-2 test

**Where.**

- Violoncellos Stac RRx9 / Stac On Bow RRx9 at 464-484 (bars 117-121, 79 notes) and 504-520 (bars 127-130, 28 Stac notes).
- The fugato staccatos: Violins I Staccatissimo RRx9 (11 notes), Violins II and Violas Stac RRx9 (13 each), bars 85-96.

**Measured.**

- **Double attenuation.** Short-row notes carry CC11 72-114 (median 88 on Violins II and celli, 72 on violas) and velocity 77-116 (celli median 96). Short rows take no layer crossfade from CC11 (patch read above). CC11 only scales the Global Group volume, by -1.0 to -5.5 dB at those values, while the recorded layer comes from velocity alone (zones 69-89 and 90-104 at f).
- **What EW does.** EastWest parks the CC1 macro, which drives CC1 and CC11 together, at 118-127 on string shorts and sets the dynamic by velocity alone, with medians 24-52 (FINDINGS section 7). Ours play louder recorded layers turned down, which is more bite per dB.
- **No beat weight.** The celli 16ths have the same mean velocity, 98, on all four 16th positions.
- **Length.** Celli shorts are 110 ms in a 119 ms slot (92%). The violins and violas are at 50%.
- **Separation.** On the celli 16ths the stem dips are 2.9 dB median, 41 of 79 under 3 dB (finding 1 table).

**Fix (c51; test as a pass-2 alias on Violoncellos 460-522 and the Violins II / Violas stac windows first).** In `tools/score_to_parts.py`, a new generic option:

```python
SHORT_CC11_PARK = {"rows": ("Stac", "Staccatissimo", "Stac On Bow", "Spiccato"), "cc": 120}
```

It holds CC11 at 120 from each run of short-row notes' keyswitch to the next non-short note. Dynamics then go to velocity through one table for every short-row note: `REP_SPLIT["stac_vel"]` near line 603, also used for printed staccatos on those rows. Proposed table:

```python
[(22, 26), (34, 30), (46, 40), (58, 50), (72, 62), (88, 76), (114, 92), (124, 104)]
```

That is 20-34 steps under today's.

Then add beat weight for running 16ths (plan section 10):

- Velocity offsets on beat / e / and / a of 0 / -22 / -12 / -22.
- ±5 seeded random, seeded by onset so renders repeat.
- On the celli at f that gives about 92 / 70 / 80 / 70, across the 69-89 and 90-104 zones.

Then set the celli shorts to 55% of the slot (65 ms at 126 bpm). For that to open a gap, cap the Stac rows' release in `build/mix.json`:

```json
"sus_release_cap_ms": {"ms": 120, "rows": ["Stac RRx9", "Stac On Bow RRx9"]}
```

on Violoncellos. The groups are named "Vc Stac rrx1"..., with no dynamic word, so check that the build prints the matched groups and set "dyn" accordingly.

Match levels with the volume envelope after the first render; the CC11 change alone lifts mp shorts by up to 6.4 dB.

**Pass.**

- Per-note level within 1 dB of the main stem after the trim.
- 2-5 kHz first 80 ms minus body at least 2 dB lower than the main stem.
- Beat minus off-16th front 1-3 dB.
- Celli 16th dips median at least 5 dB.

### 5. Wind legato velocity follows note length, not dynamic, and is under 90 on 37-63% of joins. c51

**Measured.** Wind legato targets take 100 / 80 / 60 by note length (<0.45 s / <0.9 s / longer; the else branch near line 2962 in score_to_parts.py), and the cor anglais takes 100 / 90 / 80. The correlation with CC11 is -0.19..+0.63.

Joins under 90: Flute 1 42%, Oboe 1 44%, Clarinet 1 45%, Bassoon 1 54%, Bass clarinet 63%. `LEG_VEL_EXTRA_S` (wind (70, 0.04), Oboe (70, 0.05), Bass clarinet (70, 0.09)) adds lead to the slow v60 targets.

Strings play 124, with 90 at CC11 ≤ 40 (`CODA_SOFT`, `LEG_VEL_STRONG`). Brass play 124 / 100. Both are above the floor. Manual p.144: velocity sets transition time only.

**Fix (c51).** Replace the wind length rule with a dynamic map at a floor of 90:

| Dynamic | p and softer | mp | mf | f | ff |
|---|---|---|---|---|---|
| CC11 | ≤ 46 | 58 | 72 | 88 | ≥ 114 |
| Velocity | 90 | 96 | 102 | 108 | 114 |

Interpolate on the printed CC11. Keep the cor anglais's own short-note value of 100 as a minimum.

- The `LEG_VEL_EXTRA_S` wind rows then stop firing, because no target is under 70.
- Refit the per-onset `leg_leads` from pcX after the render (`cycles/c48/actor_scripts/realised48.py`, `tools/pcx.py`).
- Inferred effect: soft wind transitions arrive about 15-25 ms sooner. The horn's LegatoSpeed range is 0-2281 samples, about 50 ms over the velocity range (DIGEST section 8).
- Strings (optional, the same cycle): grade `LEG_VEL_STRONG` by CC11 as 104 / 112 / 118 / 124 at p / mf / f / ff. That is at most 20 velocity steps, about 20 ms of extra slide. v108 against v124 measured no crossover change in c11, so the leads hold.

**Pass.** Wind join pcX median within ±30 ms, no new join dip of 5 dB or more.

### 6. Legato overlap is 0.04 qn (19-21 ms at Allegro tempos) against the plan's 45-80 / 33-58 ms. Probably inaudible, but follow the default. c51, low priority

**Measured.** Overlap medians by family: strings 20 ms (19..22, 812 joins), winds 19 ms (19..24, 417), brass 21 ms (19..24, 161). Only the Lento joins reach 47-52 ms. The exception is 77 wind and brass joins out of a slur's Sus head: Clarinet 1 has 19, Flute 1 9, Bassoon 1 8 and Oboe 1 7. They overlap 0.26-0.30 qn (about 125 ms) because the target is led by `SOST_JOIN_LEAD_S` while the head keeps its end. Leave those; c23 fitted them so the transition fires. No legato row receives a chord (0 simultaneous onsets on legato targets). `LEG_OVERLAP = 0.04` qn is fixed in score_to_parts.py line 83, and the lead stage keeps the end at the moved onset + `LEG_OVERLAP` (near line 5387).

**Inferred.** The manual asks only for "no significant gap" (p.99, p.112, p.144). In the basses patch the transition groups start on a 30 ms `VoiceTimer`, which depends on the old voice's age, not on the overlap. So a longer overlap should not change the sound.

**Fix (c51).** Make the overlap seconds per family, converted at the target's moved onset:

```python
LEG_OVERLAP_S = {"string": 0.06, "wind": 0.045, "brass": 0.045}
```

Apply it where `LEG_OVERLAP` is added: the lead application near line 5387, and the join helpers near lines 2704-2741 and 2825-2897. Leave out the `SOST_JOIN_LEAD_S` head joins, and keep `FAST_LEG_OVERLAP` for the Slur Runs spans.

Check that the keyswitch guard (`ks_cut`) and the same-pitch end guard near line 5417 still pass. Accept if join pcX and dips on unchanged joins move by less than 10 ms and 1 dB.

**Doublings share one curve (measured, no change).** I found 183 doubled spans: 8 or more shared onsets in the same pitch class, with no unshared onsets between them. Across them the CC11 shape difference is 0 at the median, after removing each pair's offset. The few larger ones follow different printed marks: Bassoon 2 has f at 316 where the basses have a crescendo, and Flute 1 has a decrescendo to mf at 492 that Violins I lacks. The volume envelopes differ by 3-5 dB (p90) because of per-note fills and fits, which correct the samples and should stay.

**Do not touch:**

- Keyswitch placement: 0 keyswitch clashes and none closer than 0.005 qn to its note.
- The GENTLE_ACCENT shapes and accent fits: brass front minus body -15.8 dB median at c49.
- The c47-c49 celli Sus Marc LITE strokes (84 / 448 / 456) and celli 156 on Sus MAX.
- The wind and brass re-tongue gaps and `REP_ROW` rows (dips 6.8-13 dB).
- `STR_REP_NEW_BOW` with its 0.06 s gap.
- The violins' and violas' staccato lengths (50% of the slot) and `STAC_LEAD_S`.
- `LEG_MIN_GAP_S`, the leg_leads / retongue_leads tables, the per-join legato rows and `JOIN_NOTCH`.
- The trombone and bass clarinet anti-bite shelves.
