# Cycle 24, critic A: articulation and phrasing (on the c23 render)

Sources: the c23 stems and master (`cycles/c23/render/`), `build/parts.json` (the c23 data), `build/score_config.py`, `build/mix.json`, `build/mockup-events.tsv`, the score (`v600/score.pdf` p.3), the keyswitch maps (`~/.rpr-bridge/libs/ew_ho/ks_maps.json`, `build/ks_maps_extra.json`), and the May 2021 HO manual. I also re-ran the actor's legato-hole measure (`cycles/c23/actor_scripts/holes23.py`) read-only. For the 200 ms variant I used a scratch copy that adds Bassoon 1, Clarinet 1 and the celli to its 200 ms list.

"Measured" means a number taken from these files. "Inferred" means a conclusion that a render has to confirm. Every fix acts on the instrument side: rows, note lengths and gaps, velocity, CC11 / CC1. None moves the track volume envelope per note.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 24, so I skipped the fixed reading. Instead I read the pages behind my findings in full, plus `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.90 (Strings, Long) | Détaché notes "do not have a legato connection to the following note", have a clear attack and a defined end. Sustain cycles up and down bows by round robin. | The celli's unslurred half-note bass line, bars 11-26 and 151-167 (finding 1) | No. These detached notes play on "Leg BC MAX". The basses double the same line on "Sus MAX". |
| p.90-91 (Marcato Sustain) | A marcato sample on top of the sustain gives "extra power at the start of the note". | The same line, as an alternative row | Not used. "Sus Marc LITE" is key 25 in the Celli KS Master. |
| p.97-98 (Strings, Legato) | Legato needs "no significant time gap". The bow-change legato is for bow changes "during a legato passage". | Finding 1 (the line is not slurred) and finding 2 (the slurred cello melody) | Leg BC is applied to unslurred notes. Inside the slurs the rows are right, but 4 joins sag 6-10 dB. |
| p.100 (Brass, Long) | Sustain volume comes from the Mod Wheel. On Sustain Accent, velocity sets the attack. | Trombone 1's accents, bars 247-253 (finding 4) | The tongued accents (Sus MAX, v103) follow it. |
| p.105 (Brass, Legato) | Velocity sets the speed of the slur ("the harder ... the faster the slur"). Near CC1 127 a filter opens for the overblown sound. Leg Slur Accent takes its accent strength from velocity. | Trombone 1's slurred accents at v118 (finding 4) | Fast transitions at v118 bring a 2-5 kHz burst. |
| p.144 (via c23 A) | Legato velocity is timing, not loudness. | Finding 4's fallback (a lower legato velocity) | — |
| MANUAL-GAPS #2 / c23 entry (re-tongue rows) | Chorale repeats fixed by gaps. | Verified (below) | Yes. 2 of 35 chorale repeats are under 4 dB. |

## Findings, ranked by what a listener would gain

### 1. The celli's unslurred half-note bass line (bars 11-26, 151-167) swells on every other note and sags across the beat, because it plays on the bow-change legato row (measured; fix inferred)

**Where.** Violoncellos, qn 40-100 and 609-656. The score prints f / ff and no slurs (`mockup-events.tsv`; slurs only at 36-37 and 668-676). In parts.json these notes are "Leg BC MAX" with overlaps, at velocity 118 / 124, with a flat CC11 of 94-110. The Double basses play the same line an octave lower on "Sus MAX".

**Evidence.**
- *Shape inside each half note.* Level in 0.6-0.9 of the slot minus 0.1-0.4, on score time:
  - celli: +6.7, +8.6, +3.4, +6.8 in 52-66, and +6.9, +4.1, +7.8, +4.3, +9.2 in 614-624;
  - basses on the same notes: -4.0..+5.5, median about 0.
  - Over the whole movement, celli "Leg BC MAX" half notes measure a median of +3.1 dB, with 24 of 69 over +4 dB. Violins I / II / violas on the same row measure -0.1..+2.6, and the basses on "Sus MAX" +0.6.
- *Where the sag sits.* In 40 ms steps from the moved note-on, the new note sags -7..-10 dB from about +0.1 to +0.45 s. At 620: +3 +5 +6 +7 +4 -0 -3 -8 -9 -9 -7 -4 -3 dB. The leads are 0.15-0.27 s, so the sag lands on the printed beat, and the body arrives in the back half of a 0.71 s note.
- *Holes, 200 ms window.* Five of the celli's nine holes of 6 dB or more are in this line: 60 (6.1), 62 (8.1), 620 (6.3), 622 (7.3), 624 (6.6). The same notes repeat in both statements, so this is deterministic.
- *Heard in the master.* The master's 100-400 Hz band swells too: back-front +8.4, +7.0, +5.1, +4.5 dB on four of the eight half notes in 612-628, and +4.9 / +4.0 in 52-66. A listener hears the bass pump "wah" on each second note under the first theme.

**Fix** (`build/score_config.py`, c15 block near line 1015):
- Add the celli to the steady-line treatment the upper strings and basses already have. `_C15_SPANS["Violoncellos"]` becomes `[(40.0, 72.0), (72.0, 104.0), (104.0, 136.0), (600.0, 632.0), (632.0, 664.0)]`. Stop at 664 so the slurs of 668-676 stay on the legato rows.
- Values: "Sus MAX", `gap_s` 0.03, `rep_gap_s` 0.05, base lead 0.04 (`_C15_BASE`). Add no accented-half fronts for the celli outside 104-136.
- If the c14 cello G2 trims or leads in these spans were fitted on Leg BC, refit them on the range render.
- A/B in one range render (qn 36-104 and 596-668, control from the same start): (a) "Sus MAX"; (b) "Detache" (key 30, p.90; one more loaded row, so check memory).
- Expected (inferred from the basses on the same notes): back-front about 0..+2 dB.
- Pass:
  - celli back-front median +2 dB or less;
  - no 200 ms hole of 6 dB or more in 40-104 / 600-664;
  - master 100-400 Hz back-front +3 dB or less on every half note of 612-628;
  - the -3 dB point of each note within ±30 ms of the basses'.
- Watch the open item: celli G2 (MIDI 43) also blooms late on "Sus MAX" (600 / 604 / 658: back +6..+10 dB). If G2 still swells after the row change, add a CC11 dip on G2 only (`INSTR_POST note_cc` or `cc_shape` `from_note`): -12 units from +0.30 s to the next note-on. It has to go below the "Sus MAX" knee near CC11 100 (c18), because values above the knee do nothing.

### 2. Four sags of 6-10 dB in the celli's slurred lines: the counter-melody (bars 72, 89), bar 216 and bar 220 (measured; fix inferred from c22 / c23)

**Where** (200 ms window, depth at time after the moved note-on):

| qn | join | row | depth | context |
|---|---|---|---|---|
| 286 | A flat 3 -> D3, tritone down | Leg Slur, v106 | 8.3 dB at +0.29 s | mp espress. counter-melody under the violins' tune |
| 352 | D3 -> C3 | Leg BC, v118 | 6.0 dB at +0.35 s | |
| 860 | F3 -> F2, octave down | Leg BC, v118 | 10.2 dB at +0.26 s | |
| 876 | A flat 2 -> G2 | Leg Slur, v100, CC11 31-37 | 8.1 dB at +0.44 s | |

**Evidence.**
- At 286, in 50 ms steps relative to the next body: -5 -7 -7 -9 -11 -14 -16 -18 -14 -14 -15 -14 -13 -7 -2 dB. The new note is missing for half a second.
- On the 30 ms measure the celli have 28 holes of 6 dB or more out of 112 legato targets. Violins I has 8 of 52 and the violas 11 of 66. Most of the celli's extra holes are bow-change and vibrato movement, and the 200 ms list above keeps only the real ones.

**Fix** (`ART_SPANS` / `INSTR_POST onset_lead` in `build/score_config.py`, the c22 / c23 method that took Horn 1's and the woodwinds' 8 / 8 early holes under 6 dB):
- Play the targets at 286, 352 and 876 on "Sus MAX", 0.06 s earlier than now.
- Give the previous note a 0.03 s overlap rather than a gap: "Sus MAX" is polyphonic, so the overlap crossfades with no legato script.
- Play 860 (an octave leap down onto a 4-qn note) as a new entry on "Sus MAX" with the entry lead (kit LEARNINGS section 5: the scripts join only within an octave).
- Range test with a control from the same start.
- Pass:
  - all four under 5 dB;
  - the old pitch at least 10 dB under the new body at +0.15 s (no smear);
  - pcx join time within ±30 ms of c23.

### 3. Bars 222-223 (qn 888): no breath is printed, but the brass and winds barely re-attack the fff chord. Give them the same lift they have at 1048 (measured; values from the measured 1048 relation)

**The coordinator's question, read from the score.**
- No breath or caesura is printed before 888 or before 1048. The `breathe` events at 880 / 884 / 892 / 1032 / 1040 / 1044 are elsewhere, and there is no fermata.
- At 884-888 every wind and brass part holds a crescendo whole note into the fff downbeat, untied. The timpani roll runs through into its 888 stroke. Flute 1 and Violins I run eighths into the bar line.
- So a real breath (a hole in the master) is not wanted, and the "master dip 6 dB" target should be dropped. What the score asks for is a fresh tongued attack on the fff chord in every wind and brass part: the players lift the whole notes at the bar line.

**Evidence (stems).** Each part's dip in the 150 ms before its new note, against the body in the 0.4-0.2 s before.

| | at 888 | at 1048 |
|---|---|---|
| note gaps | 45-80 ms | 88-122 ms |
| brass and wind dips (dB) | Horn 1 4.9, Horn 2 2.8, Horn 4 6.2; Trumpet 1 -0.9, Trumpet 2 3.8, Trumpet 3 4.2; Trombone 1 4.2, Trombone 2 2.8; Tuba 7.4; Bassoon 1 5.6, Bassoon 2 3.7; Contrabassoon 4.2; Oboe 1 5.8 | 5.1-11.2 on every brass and wind track |
| master in the 150 ms before | min -20.8, body -17.4 dB | — |

The master's 888 attack is still +6.3 dB over the body before, so the arrival step is not the problem. The weak part is the brass re-articulation, which a listener hears as the crescendo swelling straight into the fff rather than a new attack.

**Fix** (`INSTR_POST["note_end"]`, the c23 key `gap_next_s`):
- Rows `{"end": 888.0, "tol": 0.3, "gap_next_s": 0.10}` on Horns 1-4, Trombones 1-2, Bass trombone, Tuba, Trumpets 2-3.
- 0.08 s on Trumpet 1, Oboes 1-2, Clarinets 1-2, Bassoons 1-2 and Contrabassoon. Trumpet 1's B -> C is the leading-tone arrival and should stay audibly connected but tongued.
- No CC11 fall.
- Leave Flute 1, the strings (the tremolo starts at 888) and the timpani alone.
- Keep the c23 0.06 s caesura and the 1048 values.
- Expected (inferred from the 1048 relation): brass dips 5-9 dB.
- Pass:
  - every brass track dips 5 dB or more before 888;
  - the master's in-bar step at 223 on the mp3 stays at +3 dB or more (c23 +3.4).

### 4. Trombone 1's slurred accents in the Più allegro heads (bars 247, 249, 251) bite: a 2-5 kHz burst of 5-11 dB from the fast legato transition (measured; fix inferred)

**Where.** Trombone 1 (Trombone 2 has no notes here in parts.json: the unison is played by Trombone 1), qn 985 / 993 / 1001. In each, an eighth pickup on G2 is slurred up a major sixth to the accented dotted quarter (E3 / F3 / E3). parts.json plays them as "Leg Slur MAX" targets at velocity 118 (CC1 91-94, CC11 97).

**Evidence.**
- 2-5 kHz in the first 80 ms after the moved note-on, minus the body (0.15-0.4 s): **+10.9 / +5.4 / +7.9 dB**. That is Dan's "harsh trombone accent" profile (7-13 dB).
- The same track's tongued accents in the same phrase (990 / 998 / 1006, "Sus MAX" v103) read **-4 / -3 / -7 dB**.
- Every other accented part at these onsets (Violins I / II, celli, Bassoon 1, Flutes) reads -6..+3.
- On the master, the 2-5 kHz jump at the onset is +1.6 / **+2.8** / +1.9 dB. That is over the brief's +2 dB limit at 993. Trombone 1's own 2-5 kHz sits 10.6-15.9 dB under the master there, so the bite is an edge in the brass rather than a crack. It is still the one place in the movement where an accent fails Dan's "weight, not bite".
- p.105: legato velocity is slur speed, so v118 is a fast, hard transition.

**Fix** (`build/score_config.py`):
- (a) Put the three accented notes on "Sus MAX" at velocity 103, as their tongued neighbours are. That means `ART_SPANS` rows (984.9-985.1, 992.9-993.1, 1000.9-1001.1) on Trombone 1.
- End each pickup 0.02 s before the note-on (`INSTR_POST note_end` `early_s` 0.02 at 985 / 993 / 1001). A trombone tongues an accent inside a slur anyway.
- (b) Fallback: keep "Leg Slur MAX" with `vel_cap` `{"row": "Leg Slur MAX", "max": 92, "from": 984.9, "to": 1001.1}` on Trombone 1, and re-measure the join time (pcx).
- Pass:
  - Trombone 1 accent 2-5 kHz minus body at 0 dB or less;
  - master 2-5 kHz jump at 993 of +2 dB or less;
  - accent body still +2 to +3 dB over the plain notes.

### 5. Two dynamic steps arrive 0.22-0.27 s after their led notes start, so those notes enter soft and swell (measured)

**Where and evidence.** A scan of every note led by 0.12 qn or more whose CC11 / CC1 rises 15 units or more between the moved note-on and the score onset finds two notes that are not short-row parks or the sf chord at 548:

| | led by | CC11 | what the stem shows | the neighbour |
|---|---|---|---|---|
| Violins II at 511 (bar 128, "arco, unis." mf, the entry with Violins I) | 0.27 s | 32 until 511.0, then 72 | the note sits at -14 dB for 0.40 s, then jumps to 0 | Violins I's lane steps up with its moved note-on (CC11 72 from 510.43), so the two violin sections reach mf 0.2 s apart |
| Violoncellos at 952 (bar 239, f) | 0.217 s | 43 -> 88 at 952.0 | the note rises over 0.3-0.7 s (-18 dB at +0.1 s, -6 dB at +0.4 s) | — |

This is Movement I c61's lesson: move the CC rise with the moved note-on.

**Fix** (`INSTR_POST cc_shape` with `"from_note": True`, CC11):
- Violins II at 511: pts `[(0.0, 39), (0.27, 39), (0.28, 0)]`.
- Violoncellos at 952: pts `[(0.0, 45), (0.217, 45), (0.23, 0)]`.
- Or, if `dyn_step_on` can be extended to the lane itself rather than only the dynamic-trim curve, do it generically for every led note with a printed dynamic jump.
- Pass: each note within 3 dB of its body by +0.15 s after the moved note-on.

## The coordinator's c23 list, through this lens

- **Breath at 223 / 263.** Finding 3: none is printed. Drop the 6 dB master-dip target and measure the per-stem brass re-attack instead. 1048 already meets it (dips 5.1-11.2 dB).
- **Chorale repeats.** Verified on the stems (150-6000 Hz, peak of the new note in its first 0.15 s minus the floor before it). 35 wind and brass repeats in 894-936 have a median of 8.3 dB, with 2 under 4 dB: Horn 1 at 900 (2.0) and Oboe 1 at 928 (3.7). Met.
- **Wind legato holes.** On the 200 ms window, Bassoon 1 has **0** holes of 6 dB or more of 16 (median 3.2), and Clarinet 1 has 0 of 20. Bassoon 1's "6 -> 10" was its vibrato on the 30 ms measure, not render variance: add Bassoon 1 and Clarinet 1 to `holes23.py`'s 200 ms list. The other counts are Flute 1 2, Oboe 1 1, cor anglais 1.
- **Trumpet 1's solos.** The open solo (51-66) and the muted solo (171-198) have no hole of 6 dB or more. Trumpet 1's four holes are at 844-978.
- **Pizzicato (51-66, 115-121, 171-185).** Onsets reach -10 dB of the peak within -6..+12 ms of the beat on all four sections. The violas sit 12 ms (median) behind Violins II on their shared onsets. Fine.
- **Basses' hammered eighths.** Same-pitch separation is a median of 17 dB (n 297). Velocity follows the beat pattern (strong beats 97-102, off-beats 81-87). Fine.
- **Opening chord spread, Horn 3 / 4 levels, Oboe 1 568-576, sample peak, Trumpet 3 accents.** These are balance or timing items for B and C.
- **Other movements.**
  - Scherzo c20, slurred staccato pairs on Detache: does not apply. The Finale's slur-end staccatos are quarters on the staccato rows, with dips of 12-15 dB.
  - Scherzo c21, phrase-shape swells on long held bass notes: checked. No basses or celli note of 2 s or more gets 10 or more CC11 units without a printed hairpin, apart from 952 (finding 5, a printed f).
  - Scherzo c21, string staccato releases: the separations above are already 12-17 dB.

**Do not touch:**
- the chorale's 0.12 / 0.08 s same-pitch gaps with `no_fall`;
- the 1048 lifts;
- the Sus-row wind targets (Oboe 1, cor anglais, Clarinet 1);
- Horn 1's "Sus MAX" targets;
- the basses' "Stac On Bow" eighths with their 0.06 s lead and velocity pattern;
- the pizzicato rows and trims;
- the Tremolo rows from 888;
- Trombone 1's tongued "Sus MAX" accents (990 / 998 / 1006);
- the upper strings' and basses' steady-line spans;
- the trumpet 240 ms release with its re-tongue gaps;
- the harp's Harmonics / Gliss Technique rows.
