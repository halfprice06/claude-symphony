# Cycle 4, critic A: articulation and phrasing (on the cycle 3 render)

My scripts are in `/private/tmp/claude-501/mockup-loop/c04-A/`, run with `CYCLE=03`:
- `leg.py`: the c03 actor's legato crossover script, measured against `sq`;
- `legbd.py`: crossover broken down by articulation and interval;
- `harpch.py`: harp chords in parts.json;
- `unis.py` and `corr.py`: same-patch unisons, and the correlation between two stems;
- `fine.py`: stem levels in 20 ms windows on a qn grid;
- `ten2.py`: joins in bars 61-62;
- `around.py`: notes, keyswitches, CC11 and levels for a span.

Bars: 1-36 = qn/3+1, 37-64 = (qn-108)/4+37, 65-92 = (qn-220)/3+65. `build/parts.json` (00:54) is the data the c03 render (01:01) was made from.

## 1. Every printed harp arpeggio plays as a block chord: 34 chords in bars 7-14 and 71-83

**Measured in the data.** The harp parts carry 36 `\arpeggio` marks: 17 in `sections/aOne.ily` and 19 in `aTwo.ily`. Almost every harp chord under the horn solo (bars 7-14) and under the cor anglais and horn in bars 71-83 has one. In the score image, bar 12 has the roll drawn across both staves.

- `mockup.ly`'s event engraver has no listener for `arpeggio-event`. Its `articulation-event` listener does not catch it, so `mockup-events.tsv` has no arpeggio rows.
- In parts.json, all 34 multi-note harp onsets in those bars have every note on the same tick and the same velocity (`harpch.py`). Examples: qn 33 [37,44,56,61] all v52; qn 253 [37,44,56,61,65] all v64; qn 261 [27,36,56,60,63] all v64.
- The 17 octave pairs in bars 37-44 have no arpeggio sign, and they are correct as block plucks.

**Inferred.** A rolled chord is the most audible thing a harp does. Played as one simultaneous pluck at one velocity, these chords sound like a keyboard harp. The harp is exposed in exactly these bars: c03 measured it 3-6 dB under the cor anglais.

**Fix.**
- **`build/mockup.ly`, `mock-engraver` listeners.** Add `((arpeggio-event eng e) (mock-line ctx "arpeggio" 1))`, then re-run LilyPond. The events land on staves HarpR and HarpL.
- **`tools/score_to_parts.py`, `build_track()`, family "harp".** Collect `arp_q = {q for s in staves for q,k,v in ev[s] if k == "arpeggio"}`. At each onset in `arp_q`:
  - Sort the harp notes at that onset by pitch, across both staves. A roll marked on both staves is one roll from the lowest note up.
  - Delay note k (k = 0 for the lowest) by `k * step`, where `step = (0.040 if base(q) <= DYN["mp"] else 0.030) * bpm_at(q) / 60` qn. The lowest note sits on the beat.
  - Keep each note's end.
  - Put the delay into the `shift` dict as a negative lead (`shift[id(n)] = -k*step`), so that `sq` stays the score onset.
  - Give the top note +4 velocity (it carries the line). Leave the others at the table value.
  - A 4-note chord then spans about 120 ms at ♩=52.
- **Check.** In the Harp stem, the onsets inside each chord should be 30-40 ms apart, lowest first.

## 2. Unisons on the same patch play the identical sample twice: Horns 1+2 at the climax (bars 79-82) are one horn doubled, and Clarinets 1+2 partly cancel at bar 78

**Measured (`unis.py`, `corr.py`).** Four tracks share a patch file with another track: Horn 1-4 (1FH KS Master), Ob1/Ob2, Cl1/Cl2 and Bn1/Bn2. Where two of them play the same pitch at the same onset, with the same velocity and CC, Opus renders the same samples:

| Where | Notes | Stem correlation | Effect |
|---|---|---|---|
| Hn1 + Hn2, qn 261-270 (bars 79-82, the ff climax) | 8 notes, 11.6 qn | 0.999 in both channels; 1.00 in every 0.5 s window | Sum -32.3 dB against -38.8 / -37.8 alone: +6.5 dB, a coherent sum |
| Hn1 + Hn2 + Hn4, qn 265 | 1 note | | Three copies |
| Cl1 + Cl2, qn 250 (bar 75) | 1 note | 1.00 for the first 1.5 s (the slur's first note on Leg Slur uses the same sustain sample as Sus Non Vib) | |
| Cl1 + Cl2, qn 259 (bar 78) | 1 note | -0.86 | Sum -47.7 dB is quieter than Cl2 alone (-46.8). Adding clarinet 1 removes level |
| Ob1 + Ob2, qn 210 (bar 62) | 1 note | 0.98 | |

**Inferred.** Two real horns a2 add about 3 dB, with a wider, chorused sound. A sample-identical pair is a single horn turned up 6 dB with a phantom image between the two seats, so the climax horn line is too loud and thin. Partial cancellation, as at bar 78, removes the line.

**Fix (`tools/score_to_parts.py`, after `parts = [...]`).** Add a pass over track pairs that share `patch`. Two notes count as a unison when they have the same pitch, onsets within 0.01 qn, and overlap by more than 0.25 qn.
- **Horns.**
  - Add a track "Horns 1-2 a2" on `B + "2 French Horns/06 Keyswitch/2FH KS Master.oib"`. That is a recorded pair. ks_maps.json already has 2FH, with Leg Slur MAX on 26.
  - Append the new track last, so the stem numbers stay, as was done for Harp harmonics.
  - Move Horn 1's notes in the unison spans (qn 260.5-270) to it, with Horn 1's CC11 and keyswitches, and drop Horn 2's (and Horn 4's at 265) duplicates.
  - mix.json: seat between Horn 1 and Horn 2, Horn 1's mics and sends. Set the gain so its level is 3 dB under c03's Hn1+Hn2 sum, about -35 dB over qn 261-270.
- **Simpler alternative.** Drop Horn 2's duplicate notes and add a `note_trims.json` +3 dB on Horn 1 at those onsets.
- **Winds (Cl 250/259, Ob 210).** Keep the longer of the two notes, drop the other, and give the kept note +3 dB in `note_trims.json`: Clarinet 1 {250: 3}, Clarinet 2 {259: 3} (Cl2 holds longer), Oboe 1 {210: 3}.
- **Check with `corr.py`.** No same-patch pair should be above 0.9 anywhere. Hn a2 should sit about -35 dB.

## 3. Bar 63 sf tremolo: a 9-13 dB hole in Violins I on the downbeat; the sf arrives late and differs by up to 15 dB between sections

**Measured (`fine.py 211.5 213.5 0.0625`, 69 ms steps; `around.py`).** Bar 63 is the arrival of the Largamente: sf> tremolo in all upper strings, the basses sf, and Trombone 1's marcato entry.

**Cause in the data.** The last notes of bar 62 are tenuto (`fes''2--`). In Vln I, Vln II and Vc the tenuto rule cuts them 0.06 qn (end 211.94), and the keyswitch to Tremolo sits at 211.94. The tremolo starts at 212.0 with no lead. Its sf CC11 spike lasts only 0.1 qn: 114 → 124 at 212.02 → 113 at 212.125 → 99 at 212.25 → 72 at 212.5.

| Stem | Level before 212.0 | At 212.0 | sf peak (delay) | Bars 63-64 after the peak |
|---|---|---|---|---|
| Vln I | about -41 dB | -50 (a 9-13 dB hole on the downbeat) | -35 (+6 dB), at +0.14 s | |
| Vln II | -43 dB | | -26 (+17 dB), at +0.21 s | sits at -34 for a beat, 9 dB above its ff bar 62, inside the printed sf> p |
| Vla (tremolo since bar 61, no cut) | | | +6 dB, at +0.07 s | |
| Vc | | | about +2 dB: no sf | |
| Cb (Sus MAX) | | | +3 dB | |

**Inferred.**
- The downbeat of the climax arrives as a gap in the first violins, followed by a late, uneven swell. Vln II pops out.
- A real section plays the sf with the bow on the beat and drops at once. One shape for the whole string section, about 4-6 dB over the ff and on the beat, is what the score asks for. Dan's accent rule (2-4 dB, no spike) is the guide for the upper end.

**Fix (`tools/score_to_parts.py`).**
- **Note-length loop.** A string tenuto note whose next note on the track starts within 0.02 qn on a different articulation (Tremolo, Sus) should end at the next onset + 0.02 instead of being cut. The patches are polyphonic there, so this is a crossfade. In practice: skip the tenuto cut when `o0.get("art") != n.get("art")` and `base(q) >= DYN["f"]`.
- **Lead.** Give tremolo notes that follow a sounding note an entry lead of 0.05 s. Add `"Tremolo"` to the lead branch for `pe is None` too, with `L = 0.05*bpm/60`, CC on score time.
- **`base_points()`, sf branch.**
  - For sf followed by a decrescendo, use `(q, level), (q+0.02, spike), (q+0.25, spike-6), (q+0.75, post)`, so the spike outlasts the tremolo's attack.
  - Set `spike = min(124, level + 8)` when `level >= DYN["f"]`. From ff (114) that gives 122, not a fresh +12.
- **`build/note_trims.json`.** Violins II {212: -6} (balance; this one is for critic B to confirm).
- **Check with `fine.py`.**
  - No string stem should drop more than 3 dB between 211.9 and 212.0.
  - sf peaks within 80 ms of 212.0, each 3-6 dB over the stem's bar-62 level.

## 4. Tenuto notes inside a wind slur (portato, bars 61-62) re-start on Leg Slur MAX: Flute 2 blooms 0.6 s late and Oboe 1 drops 5-9 dB for a whole half note at ff

**Measured (`ten2.py`, `around.py 203.9 212`).** In bars 61-62 the flutes and oboes have tenuto half notes under one slur (ff, "molto sostenuto"). The c03 tenuto rule ends each note 0.03 qn early (mf and louder). The next note, still on Leg Slur MAX, then starts without a legato transition, on the patch's slow non-legato layer.

| Stem | Join at qn 206 / 208 / 210 | After the join |
|---|---|---|
| Flute 2 | -3 / -15 / -12 dB | At 206 the new note stays at -47 to -52 dB until 206.65, then jumps to -35: a bloom 0.6 s after the beat. At 208: -42 to -47 against -37 to -41 before |
| Oboe 1 | 208: -12, 210: -8 | After 208 it sits at -41 to -37 dB against -32 before, for the whole half note (about 2.2 s) |

The same moment on Sus MAX:

| Stem | Join at qn 208 / 210 | After the join |
|---|---|---|
| Oboe 2 | -4 / -7 dB | holds its level at once |
| Cl 1 and Cl 2 (Sus Non Vib) | -1 to -8 dB | |
| Horns, trombones, tuba (Sus MAX) | -1 to -6 dB | |

**Inferred.** A wind portato is tongued, so a Sus attack is the right sample. Leg Slur's first-note layer is not: it is the same slow-attack problem c03 found for string repeats.

**Fix (`tools/score_to_parts.py`, `build_track()`, wind/brass articulation branch).** A note that carries a tenuto and is inside a slur gets the Sus articulation, `ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib")`. So does the note after it, when that note is also tenuto. Keep the c03 gap `min(0.03, 0.1*dur)` at mf and louder, and the +5 CC tenuto bump. That is 4 Fl2 notes and 3 Ob1 notes. Fl1's tied whole note is not affected.

Check with `ten2.py`: Fl2 and Ob1 joins within -8 dB, and the level 0.1-0.8 s after each join within 3 dB of the level before.

## 5. Woodwind legato targets on long notes (velocity 60) still cross over 100-150 ms late; the cor anglais solo is the worst (median 160 ms)

**Measured (`leg.py`, crossover against `sq`).** Woodwind legato-target velocity is 100 (< 0.45 s), 80 (< 0.9 s) or 60 (longer). Woodwinds other than oboe and bassoon have no lead.

| Track | Median (ms) | By velocity (n, median ms) |
|---|---|---|
| Cor anglais | 160 | v60 19, 150; v80 6, 185 |
| Flute 1 | 90 | v60 29, 110; v80 23, 85; v100 3, 70; v127 3, 35 |
| Clarinet 1 | 90 | v60 14, 112; v80 11, 85 |
| Oboe 1 | 90 | v60 19, 100; v80 16, 62 |
| Bass clarinet | 90 | |
| Bassoon 1 | 105 | |

The strings sit at 50-80 ms and the horns at 85-108 ms.

**Inferred.**
- The cor anglais solos (bars 31-34 "solo, espr.", 41-44 "solo, dolce cantabile") place every slurred note about 0.15 s behind the harp and the strings.
- The HO manual (2.1, True Legato, p. 91) says velocity 50-60 gives the slower transition "allowing the melody to breathe". Keep that character and move the onset instead, as c03 did for the strings.

**Fix (`tools/score_to_parts.py`).**
- **`LEG_LEAD_S`.** Add `"Cor anglais": 0.08, "Flute": 0.03, "Clarinet": 0.03`. Name keys are matched before family. "Clarinet" does not match "Bass clarinet", whose key already exists.
- **Wind velocity table.** Raise the cor anglais's legato velocities to 100/90/80, since its v60 and v80 both measure late. Leave the other woodwinds' velocities.
- **Check with `leg.py`.** Every woodwind median should be 60-100 ms, and the cor anglais under 110 ms.

## 6. Divisi and solo lines still use full-section patches (third report; narrowed to the two places where it changes the articulation)

**Measured in parts.json.**
- **Vc div., qn 51-54 and 63-66 (bars 18, 22).** The slurred upper answer and the held lower note sound together, so both are on Sus MAX (11 Vc Sus notes). The printed slur is not legato.
- **Vln I "solo, senza sord." (bars 17-22).** The whole section plays it, with +8 CC.

**Fix.** A minimal version of c03 A5. Use `Celli Divisi/06 Keyswitch/Celli KS Master DIV B.oib` as a new track (appended last) carrying only the upper notes at qn 51-54 and 63-66, on Leg Slur MAX with the normal slur logic. The main Vc track then sees a single line there, and its Sus notes return to Leg. For the Vln I solo, `1st Violins Divisi/06 Keyswitch/1st Violins KS Master DIV A.oib` (a half section) is the closest thing on the drive to a solo player. Use it as a separate track for qn 48-66, with Vln I's mix entry at -3 dB. Lower priority than findings 1-5.

## Do not touch

- **String legato leads and velocity 124** (measured crossover: Vln I 50, Vln II 75, Vla 80, Vc 60 ms; Leg Slur and Leg BC within 15 ms of each other).
- The same-pitch merge with CC11 notches. qn 223's level drop follows the printed decrescendo (CC 34 → 12) and is not a hole.
- Leg BC joins in bars 61-62 (Vln I -5/-4, Vc -4 dB).
- Pizz velocity scheme (v53 at p, following the hairpins in Vla bars 41-44).
- Harp Sus RR velocity table, harp ring and the Harp harmonics track.
- Tbn1's three accents (c03: +4 to +6 dB attack brightness).
- Brass and lower-wind Sus MAX tenuto gaps in bars 61-62 (dips -1 to -6 dB).
- The grace run at bar 78; breath shortening; the timpani roll/stroke articulation scheme.
