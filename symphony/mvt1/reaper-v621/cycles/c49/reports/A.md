# Cycle 49, critic A: articulation and phrasing (render c48, score v621)

## Method

Everything is measured on the delivered c48 stems and master (`cycles/c48/render`), placed with `cycles/c48/rendered_build/parts.json`. The basses stem is the 450 ms pp-cap audio up to qn 695.8, as the coordinator noted. For before/after comparisons I used `cycles/c47/render` with `cycles/c47/rendered_build/parts.json`.

Measures:
- **pcX**: `tools/pcx.py` `attack_pcx` and `legato_joins`, on every track that has legato joins (1,397 joins matched between c47 and c48).
- **Band envelopes**: `pcx.band_env`, used for re-bow dips and steps, repeated-note dips (S1) and stroke swells.
- **Accent against its staccatos**: the accent's first 0.3 s against each staccato's first 0.14 s, both from the moved onset. This is c48 A's measure.
- **Simulations**: stem times a volume shape. The volume envelope sits after the Opus hall, so a simulation of a level-only change is exact.

Labels: **measured** (render or parts.json), **read** (code, config, CHANGES or manual), **inferred** (reasoned, not tested). The scratch scripts in `/private/tmp/claude-501/mockup-loop/mvt1-c49-A/` are deleted after the run, as the brief asks.

## Manual notes

c49 has no fixed pages (MANUAL-READING.md, second round). I read these pages in full because they sit behind this lens's top open problems:
- **PDF p.91-92** (Sustain bow direction, Marcato Sustain), behind findings 1 and 2.
- **p.143-145** (performance scripts: legato velocity, CC22, Repetition script, Round Robin Reset), behind finding 1 and the join check.

I also read MANUAL-GAPS.md (including its c48 results) and DIGEST.md sections 2 and 5. The open MANUAL-GAPS items in this lens (#3 Solo Cello, #5 expressive wind rows, #7 half-section divisi, #9 horn portato, #12 Felt Cresc, #13 bass trombone low notes) are not behind any problem measured here. Every divisi passage plays chords of whole notes or tremolos on Sus MAX or Tremolo rows, never on a legato row, so #7 is a colour question and not an articulation one. The new c48 entry, "p.91 bow direction", is finding 1.

| Manual (PDF page) | What it says | Where it applies | Does the render follow it? |
|---|---|---|---|
| p.91 Sustain, "Bow Direction" | A two-sample round-robin cycle alternates up and down bow on each note | Basses' coda C2 eighths, bars 167-169 (Sus MAX) | **No.** The strong stroke falls on every off-beat and the weak, slow one on every downbeat. Level shapes cannot separate the off-beats (finding 1). |
| p.91-92 Marcato Sustain | A marcato sample on top of the looped sustain gives "extra power at the start of the note" | Celli repeated-pitch strokes 84 / 156 / 448 / 456 on Sus Marc LITE | **Yes on 84 / 448 / 456**: pcX -25 / -2 / +2 ms. **Worse on 156**: half amplitude at +160 ms, against +84 on c47's Sus MAX (finding 2). |
| p.144 Monophonic True Legato: velocity sets transition time (50-60 slower, 110-127 tighter) and does not change loudness; CC22 64-127 = monophonic | Every legato row | All joins | **Yes.** Legato targets play at v124. No note on a legato row is overlapped by another pitch for more than 0.35 qn in any track, so no chord reaches a monophonic patch. No keyswitch lands inside the note it governs (the in-note switches all prepare the next note under a short pickup). |
| p.145 Repetition script: random detune or a neighbour's sample, so renders do not repeat | Strings | CC69 = 0 in the pre-roll | **Yes** (read): it is off, so the round-robin order is fixed. |
| p.145 Round Robin Reset: Opus remembers the next sample **per note** (a note heard three times plays A B A), and a reset "at important positions" forces a chosen order | Every round-robin row | Reset only in the pre-roll (CC16, plus CC36) | **Partly.** There is no reset inside the music, so where each bow direction falls in the coda pedal is decided by how many C2s came before it (finding 1). |

## 1. Coda bars 167-169: the basses' strong bow stroke lands on every off-beat. The off-beats are barely separated and still come 40 ms early, and level shapes cannot change this (S1, S2; measured, simulated; fix inferred, to be tested)

**Where.** Double basses, qn 664-676: f, repeated C2 eighths on Sus MAX, plus the `STR_REP_DETACH` dips and three level layers (the c22 hold, the `_cb24` alternation and the c48 +3 / -1.5 dB shapes). The basses are the third-loudest stem here (-10.5 dB re master, after Trumpets a2 and Horns a2). They are the only eighth-note pulse in the bass, under off-beat figures in the horns, trumpets and violas.

**What is wrong (measured, c48 stem / master).** Each line gives the band dip into the note against the lower of the two bodies, then pcX:
- **Into downbeats**: dip 6.8 / 2.6 dB; pcX +32 ms by my estimator (c48's own figure is +18).
- **Into off-beats**: dip **2.2 / 1.6 dB**; pcX **-41 ms**.
- **Peak level**: off-beats still 2.7 dB over the downbeats.
- **The other pedals**, which carry the same dips: bars 27-31 off-beats 3.3 / 2.0 dB; bars 131-134 7.6 / 3.6 dB; bars 140-142 4.6 / 1.4 dB.

So in the coda each off-beat runs into the downbeat before it and is heard early. The rhythm comes out short-long, a limp with the weight on the wrong eighth.

**Why (read, measured).** p.91: Sus MAX alternates two bow-direction samples. The alternation has been identical in c46, c47 and c48 because CC16 resets the order in the pre-roll.

I simulated level changes on the c48 stem (with the c48 off-beat cut taken out first):

| Variant | Dip into off-beats, stem / master (dB) | Off-beat pcX (ms) |
|---|---|---|
| c48 as rendered | 2.2 / 1.6 | -41 |
| Off-beat cut removed | 2.2 / 1.6 | -38 |
| Cut started 0.06-0.1 qn later | 2.2 / 1.6 | -38..-39 |
| Cut deepened to -2.5 dB | 2.2 / 1.6 | -38..-39 |

None of them moves the off-beat dip or its timing. Only a different sample on each beat can.

**Which sample plays where (read, p.145).** Opus keeps the next round-robin sample per note. On Sus MAX the basses play 61 C2s before qn 664 (counted in parts.json), so 664 is the 62nd: the B sample, which here is the weak one. The A sample, the strong one, falls on the off-beats.

A windowed alias builds only the notes inside its window, so after the pre-roll reset its first C2 plays A. Two windows fix the order:
- **Window starting at 664.0**: 664 is that instance's first C2, so it plays A and the strong stroke goes onto the downbeats.
- **Window starting at 662.0**: it includes the C2 at 662, so 664 plays B, as now.

Under the other possible model, one counter per row, 664 would be the 289th Sus MAX note and play A. That is why the test below renders both windows. No tool change is needed.

**Fix (pass-2 test, then a permanent alias).** In `build/score_config.py`, after the c48 block:
- `ALIAS_TRACKS["Cb pedal A"] = {"source": "Double basses", "windows": [(664.0, 676.0)], "drop": {"LEVEL_SHAPES": <the first-point onsets of the _cb24 row (663.97) and of the c48 C #2 rows (q - 0.14 and q + 0.5 for q in 664..675)>}}`.
- `ALIAS_TRACKS["Cb pedal B"]`: the same, with `"windows": [(662.0, 676.0)]`.
- Both go in `PASS2_TRACKS` and `TEST_TRACKS`. Keep the `STR_REP_DETACH` span (664, 676) and the +1.5 dB hold row [663.85..676.1]: the alias inherits them.

Render both in pass 2. Keep the one whose downbeats carry the strong stroke, by these criteria on its stem:
- off-beat dip at least 3.5 dB on the stem and 2.5 dB in the master (the other pedals' range);
- downbeat peak at least 0.5 dB over the off-beats;
- downbeat pcX within ±30 ms.

Then make the winner permanent: set the source to rest in that window (`TRACK_WINDOWS["Double basses"]`, keep inside False, as the Bassoon 1 stac windows do) and remove the alias from `TEST_TRACKS`. For this render, splice qn 663.9-676.0 of the alias stem into the delivered basses stem (as `swap48.py` did).

If the strong stroke then reads early on the downbeats, give the off-beats a lead of 0.03-0.05 s rather than taking lead off the downbeats (inferred; a lead is never negative). The main track's round-robin state after 676 is untouched, so the coda re-bows and the pp-cap checks stay valid.

**Target.** Separate eighths with the weight on each beat, at a level the master carries (the basses are -10.5 dB re master).

## 2. Celli bar 40 (qn 156): the c48 switch to Sus Marc LITE made the stroke later than c47's Sus MAX. Revert it (S2; measured)

**Where.** Violoncellos 156, a repeated A-flat2 stroke after a 4-beat note, bar 40, rel -6.2 dB.

**What is wrong (measured).** t50 and h10 are the half-amplitude and -10 dB points of the attack, in ms from the beat; "under" is the time the band stays 6 dB under its body after the beat.

| Render | Row, lead | pcX (ms) | t50 / h10 (ms) | Under after the beat (ms) |
|---|---|---|---|---|
| c47 | Sus MAX, lead 190 ms | +32 | +84 / -20 | **0** (148 ms after the note-on, all before the beat) |
| c48 | Sus Marc LITE, lead 120 ms | **+77** | **+160** / -6 | 0 |
| c48 pass 2 (CHANGES) | Sus Marc LITE, 0.055 s extra lead | +61 | | 134 ms under |

For comparison, the other LITE strokes in c48: 84 -25 ms, 448 -2, 456 +2 (456 improved from t50 +272 to +20; keep it).

c48 A counted 156's c47 "under" (222 ms) from the note-on. With a 190 ms lead, almost all of that time is the bow change before the beat, which is the separation S1 asks for. c47's attack reached body 42 ms before the beat.

A level fill does not help. Simulated on the c48 stem, +2..+4 dB held 0.10-0.15 s moved pcX only +77 → +72 ms, while overshooting the body by 2.2-3.4 dB: the late rise is in the sample.

**Fix.**
- `build/score_config.py`: in the c48 line, change `ART_SPANS["Violoncellos"] + _spans47([156.0, 456.0], _STR_B)` to `_spans47([456.0], _STR_B)`.
- `build/retongue_leads.json` Violoncellos: `"156.0": 0.02 -> 0.09` (c47's value).

This changes a row, so check `tools/state_check.py` on the celli against c47 after the render. If 156 does not come back near c47's pcX +32, splice c47's qn 154-158 (the data elsewhere is unchanged).

## 3. Fugato check: the c48 shapes work, but the violas' quarter-note staccato at 358 is now as loud as the accented subject head at 354 (measured; fix exact by simulation arithmetic)

**Where.** Bars 85-96 (qn 337-376).

**Measured (accent minus the loudest following staccato, c47 → c48).** This answers the coordinator's check: every head A #1 targeted now leads its eighths by 1.4-4.1 dB, and no 2-5 kHz front rose above -4.3 dB re body (the brief's rule 4 holds).

| Head | c47 (dB) | c48 (dB) | Note |
|---|---|---|---|
| Vc 337 | +1.6 | +4.1 | |
| Vc 342 | -3.8 | +3.5 | |
| Vla 349 | -1.4 | +1.4 | |
| Bn1 stac 349 | -3.1 | +2.4 | |
| Vln I 373 | +0.1 | +2.1 | |
| Vla 354 vs its eighths 355.5 / 356 | | +2.1 / +5.0 | |
| **Vla 354 vs the quarter staccatos** | | 357 +1.7, **358 +0.0**, 359 +2.2 | |
| Cor anglais stac 366 | | -1.3 | 367.5 is 2.1 dB louder; untouched, at rel -6..-8 |
| Flute 1 stac 373 | | -3.7 | 374.5 is 1.9 dB louder; at rel -10 |

The violas have no crescendo before their f at 360, so a player would keep 358 under the head (inferred).

**Fix.** `LEVEL_SHAPES["Violas"] += [[(357.95, 0.0), (357.98, -2.0), (358.6, -2.0), (358.7, 0.0)]]`. This puts 354 at +2.0 over 358 (a level-only change on a single note, so the result is exact). The two wind doublings are optional and lower priority, since both are covered by their string doublings: `ALIAS_TRACKS["Cor anglais stac"]` and `["Flute 1 stac"]` `LEVEL_SHAPES` -2 dB over [367.47, 367.9] and [374.47, 374.9].

## 4. The c48 lead moves did not make any legato join or re-bow worse (measured; no action)

The coordinator asked for this check against c47 (pcx.py, state_check.py).

**Legato joins.** Of 1,397 matched joins, 52 had their lead changed.

| Joins | Median change in \|pcX\| | Better by >30 ms | Worse by >30 ms |
|---|---|---|---|
| Moved (52) | -37 ms | 38 | 2 |
| Unmoved (1,345) | 0 | 44 | 40 (render noise) |

- The crossover window (the time both pitches sit within 6 dB) changed by a median of -2 ms. One window grew: celli 97, 92 → 218 ms, with the old G still about 6 dB over the new F's peak.
- The two "worse" joins (Bassoon 1 531.5, celli 182) and the large celli 387 value are measurement artefacts. In each, the new note reaches -10 dB 40-70 ms earlier than in c47, and pcX rose only because the body peak sits later (on 387 the band also picks up the next note, the D4).

**Join medians, c47 → c48.**

| Track | pcX median (ms) | Notes over 60 ms off |
|---|---|---|
| Violins I | +22 → +14 | 21 → 16% |
| Violins II | +25 → +15 | 26 → 20% |
| Violas | +20 → +19 | |
| celli | +6 → +1 | |

**All 158 moved notes (pcX on each note's own band).** The median |pcX| went 61 → 24 ms: 100 notes better and 9 worse by more than 20 ms. Seven of those nine are Horn 3 entries, which now sit +14..+60 ms after the beat (median -4 → +14 ms signed, |pcX| 17 → 15). That is the later placement C #1 (b) intended, not a fault.

**Re-bows.** 96 automatic re-bows, measured as dip and step on the stem and in the master. None got worse by more than 1.5 dB except:
- Violins II 292: dip 1.0 → 3.0 dB, 1.3 → 3.1 in the master. This is a printed, untied repeat of E-flat (290-292), so the deeper dip is what S1 asks for.
- Violins II 576: stem dip 5.9 → 7.8 dB, master unchanged.

Violins II 176 (7.2 → 4.6 dB) and celli 289 (step -3.4 → +1.2 dB) improved.

**Repeated notes (S1) next to moved notes.** No exposed repeat lost its separation. Contrabassoon 521 and 537 measure 1.3 and 0.1 dB, but their notes and gaps are unchanged apart from the 20 ms entry shift, and the instrument sits in the tutti.

**Keyswitches.** 0 keyswitches late. 3 new in-note switches (Violins I 74.5 and 106.5, Violins II 397.5) prepare the following Leg Slur target under a pickup that got shorter, as before.

## 5. Basses pp release cap: keep 600 ms throughout; no coda-only alias (read; inferred)

The delivered bars 1-174 use the 450 ms audio. A rebuild plays 600 ms, which differs only at the pp chord changes 176 / 180 / 224 / 230: -9.8..-11.7 dB re the new note, against -11.7..-15.4 at 450 (CHANGES). That is 2 to 4 dB of extra hang, on notes the basses play at rel -12..-19 dB under the celli and violas.

The final release needs 600 ms: at 450 ms its -20 dB point falls from 0.35 to 0.30 s, under the references' 0.48-0.79 s in the master. An alias with a second instance would cost memory and a state risk to fix a hang that is probably inaudible (inferred). Accept 600 ms in mix.json as written, and drop the "450 up to 695.8" splice from c49 on.

## 6. Leave as they are (measured)

- **Clarinet 1 706** (pcX +99 ms). The broadband stem has a 5 dB dip for 40 ms just before the beat, then the B4 at full level on the beat (the c48 fill), then the printed diminuendo. The late band pcX is the legato transition's timbre change at about 66 bpm (0.11 of a beat). A level or lead change would only add overshoot.
- **Violas 372** on Sus MAX: pcX +33 in c47 and +88 in c48 on identical data. That spread is render noise, so do not fit it.
- **Celli 47** (Lento bar 12, pcX +60, rel -11.4): 5% of a beat at q=50.
- **Timpani rolls.** No roll of 3 qn or longer is the loudest stem. Long rolls sit at -11..-19 dB re master, and the opening ppp roll solo falls to -6.9. Rolls grow only under printed crescendos (bar 80: -15.1 → -8.6 dB).

## Do not touch

Keep the following as they are:
- The c48 per-note lead rows and the moved fills, notches and shapes (joins and re-bows checked above).
- The swell fills.
- The A #1 fugato shapes (add only finding 3's row).
- The celli 84 / 448 / 456 Sus Marc LITE strokes with their leads.
- `STR_REP_DETACH` and the +1.5 dB pedal holds.
- `GENTLE_ACCENT` and `accent_fits.json`.
- `AUTO_REBOW` with its fills.
- `TREM_JOIN` / `TREM_SPLIT`, the pizzicato rows, `REP_ROW` with its gaps, and the pass-2 wind staccato windows.
- `TIMP_RH_ALT` and the roll roles.
- The pre-roll CC16 / CC36 resets with CC69 = 0.
- Every keyswitch rule (none late, no chord on a legato row).
- The 600 ms basses pp cap, with the other sections uncapped at pp.
