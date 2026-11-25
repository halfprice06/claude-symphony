# Cycle 37, critic A: articulation and phrasing (on the c36 render)

Inputs: `cycles/c36/render/` (stems and master), `build/parts.json`, `build/score_config.py`, `build/rebow_fills.json`, `build/mockup-events.tsv`, score v600 page 5. c34 and c35 stems were used for comparisons. All levels are plain RMS dB on the stem unless the text says master. Times are on the parts.json tempo map.

## Manual notes (A4, May 2021 HO manual, PDF pp. 108-113: Hollywood Orchestral Woodwinds)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| "Flute 2" is a different player with its own samples, so it does not collapse with "Flute" in unison (p.108) | Flute 2 track | Yes. Flute 2 plays `FL2 KS Master.oib`. No wind pair plays a unison onset anyway: 0 unisons in Ob, Bn, Cl, Fl, Hn 1-2 (measured, parts.json). Oboe 2 shares the OB KS Master with Oboe 1, but they never play the same pitch at the same time. |
| Sustain dynamics on the Mod Wheel, all three layers sounding at once (p.109; Play-era text, see 2025 p.52) | every wind Sus/Leg note | The mockup keeps CC11 for dynamics on flutes, oboes, cor anglais, bassoons and bass clarinet (CC1 = vibrato crossfade, 38-110), and CC1 dynamics on the clarinets (c30). This matches the 2025 manual and the patch files. |
| Sus Expressive: slower attack, vibrato that grows (p.109) | the espr./dolce wind solos (MANUAL-GAPS #5) | Not used. See finding 3. |
| Legato Repetitions RRx4: a re-tongued attack for repeated notes inside a sustained phrase (p.109-110) | wind same-pitch repeats (13 re-tongued, 2 merged) | Not used. Re-tongued repeats dip 4-10 dB on the stem (measured). The merged Flute 1 repeat is not audible (finding 1). |
| Short articulations have no release trails; hold the last note so the room can ring (p.110) | none | v600 prints no wind staccato. |
| Runs, trills, flutter, repetition patches (p.111) | none | Nothing printed that needs them. |
| Legato joins only with no gap and at most an octave (p.112) | every wind Leg Slur line | Yes. No transition on any legato row is wider than 12 semitones (measured, all 32 tracks). |
| Legato patches are monophonic; CC22 below 64 makes them polyphonic (p.112) | every Leg row | Yes. No two different pitches overlap by more than 0.08 qn on any legato row (measured, all tracks). CC22 is not sent, which is correct. |
| Legato Slur Repetitions: same-pitch notes inside a slur, played with no space between them, get a re-tongued sample (p.112) | Flute 1 qn 135-136; Cor anglais qn 270-271 | Not used. This is the fix for finding 1. The row exists in the FL and EH KS Masters ("Leg Slur Rep", key 36; `ks_maps.json`). |
| Slur Runs: portamento slurs for fast runs in seconds (p.112-113) | Flute 1 run at qn 261.5-262 (three 0.2 qn notes) | Not needed. The run is 3 notes on Leg Slur MAX, and Flute 1 is under Violins I there. |
| KS Masters switch between articulations by keyswitch (p.113) | every wind track | Yes. No keyswitch arrives after the note it serves (c36 report A; unchanged in c36). |

## Extra check: unchanged tracks that differ from c35 (render started at 32 GB)

**Measured.** I compared the c35 and c36 stems in 0.5 s windows. Oboe 1 and Horn 2 are sample-exact (max difference 1e-7). Violins I has 5 windows that differ by more than 1 dB, Violins II 8, Bassoon 1 1, Violas div 1 and Horn 3 none. Violas div was sample-exact between c34 and c35, so this non-exactness is new in c36.
- No window drops to silence. No window has a click: the 2 ms high-band (>6 kHz) peak-to-median ratio is the same within 2 dB, c35 against c36. Band levels (60-250 Hz, 250 Hz-1 kHz, 1-3 kHz, 3-8 kHz) differ by at most 2 dB, and the window totals by at most 0.8 dB.
- Every difference starts at a note onset or a legato join and is gone 1-3 s later. The two renders are then identical again (Violins II 216.5-220.5: correlation 0.95, identical except for 217.8-219.3). At the joins I measured, the pitch crossover moved by 0.06-0.16 s at 6 of 17 joins (Violins I 196: -0.05 -> +0.05 s; 262: +0.10 -> +0.01 s; Violins II 70: -0.03 -> -0.09 s; 73.5: +0.04 -> -0.07 s; 218: +0.06 -> +0.22 s). The other 11 are identical to 0.01 s.

**Judgement (inferred).** None of these windows looks like a missing sample. A dropped layer or a stream that never arrived would leave a hole or a band loss, and none appears. The pattern fits the legato script or the round robin choosing a different take, or a stream that arrived a few hundred ms late on one note. The case closest to a late sample is Violins II's B3 at 218 (bar 64, sul G, p). It reaches its pitch 0.16 s later than in c35 and sits 4-8 dB lower for about 0.5 s, then is followed by a 219 D4 3-5 dB louder. But it is at -55 dB, about 30 dB under the master (Trombone 1's ff quotation), so nobody will hear it. The Violins I windows (196-197, 261-263, ±1-2 dB at -28 to -42 dB) are inside the theme's own variation from note to note. None of them is audible in the master as a fault. Render-health suggestion for the actor: let REAPER settle (as in c31-c35, 44 GB) before `render_cycle.py`, and keep the c36 habit of checking unchanged stems for sample-exactness.

## Findings, ranked by what a listener hears

### 1. Flute 1, bars 43-44 (qn 135-136): the slurred repeat of E flat 5 is still not heard. Deepening the notch in c36 did nothing, so move it to the Leg Slur Rep row (measured; S1)

**Where.** Flute 1, the E flat 5 crotchet at 135 slurred to the E flat 5 at 136, in the duet with the cor anglais (bars 41-44).

**Evidence (measured).** `WIND_SLUR_REP_MERGE` plays the two notes as one, with CC11 34 -> 20 -> 27 -> 34 at 135.875-136.25 (`MERGE_NOTCH_AT["Flute 1"] = {136.0: 14}`). The repeat's 100 ms minimum (-53.7 dB at 135.94-136.0) is only 0.2 dB under the troughs of the flute's own vibrato in the 0.7 s before it (-53.2 dB at 135.50). The master dip is 1.9 dB. Measured the same way, every other wind repeat re-articulates 3-11 dB under its own troughs: Cor anglais 271 (merged, notch 20) -7.8, Clarinet 1 289 -7.8, Bassoon 1 235 -10.8, Horn 4 265 -7.6. A listener hears one long note where the score has two. Side note for critic B: over 135.3-136.8 the flute stem is -48..-54 dB against the cor anglais at -42..-46, so the flute does not lead here, despite c35's +5 dB.

**Manual.** p.112, Legato Slur Repetitions: when same-pitch notes are played with no space between them, the second and later ones use a re-tongued sample. The FL KS Master has the row "Leg Slur Rep" (key 36) next to "Leg Slur MAX" (`~/.rpr-bridge/libs/ew_ho/ks_maps.json`).

**Fix.** In `tools/score_to_parts.py` add a per-onset skip of the wind merge with an empty default, for example `WIND_SLUR_REP_MERGE_SKIP = {}`, checked where `wind_rep_merge` is set (line ~2185). In `build/score_config.py`:
- `WIND_SLUR_REP_MERGE_SKIP = {"Flute 1": [136.0]}`
- remove `MERGE_NOTCH_AT["Flute 1"]`
- `ART_SPANS["Flute 1"] = [{"from": 133.9, "to": 139.0, "art": "Leg Slur Rep"}]`

The 135 note must end exactly at 136's onset. Do not let it overlap into the same pitch: LEARNINGS §5 measured -18..-33 dB dips when it does. Adding the row means a full rebuild of Flute 1, about 0.1-0.3 GB. Fall back to "LegRep RRx4" (key 31, p.109-110) if Leg Slur Rep plays the 136 attack too hard.

**Target.** A re-articulation 4-6 dB under the vibrato troughs on a 100 ms window, a master dip of 2-4 dB, and no hole longer than 0.15 s.

### 2. Double basses, bars 82-84 (qn 273.2-276.1): the coda pedal swings about 6 dB down and 7 dB up in 3 s, the same in every render (measured)

**Where.** Double basses, the A flat 1 pedal at ppp, re-bowed at 273.229 and 276.05. The celli 4 soli enter at 274, over the harp harmonics.

**Evidence (measured, 150 ms windows).** The 273.229 piece falls from -51 (bar 82) to -60.8 at 273.56 and -60..-60.6 at 274.0-274.12. Its body after the c34 shape (-5 dB at 274.24-274.67) is -54..-55. It dips again to -59.3/-59.6 at 274.78 and 275.19, then rises to -48.2/-46.9 at 275.44-275.56, 6-8 dB over that body, in the pre-part of the 276.05 fill (+6.64/+5.14/+2.31 dB at -0.12/-0.08/-0.04 s in `rebow_fills.json`). From 276.1 it is level again at -53. c34, c35 and c36 give the same values to the dB in all 22 windows, so a fitted fill will hold. The re-bow table shows the 273.229 piece as the deepest of the 19 basses re-bows (200 ms dip -9.2, step -4.2; the others -0.3..-5.8). HISTORY has listed it as open since c34 ("Cb 273.229 still swings 10 dB").

**Fix.** In `build/rebow_fills.json` "Double basses":
- add "273.229": +4 dB over +0.55..+0.95 s and +1.35..+1.70 s, plus +3 dB over +2.2..+2.6 s (0.08 s ramps; the c29 "no fill" decision predates the c34 shape)
- lower "276.05" at -0.12/-0.08/-0.04 s to +2.0/+1.5/+1.0

Or let `tools/fit_rebows.py --window "Double basses:2.6"` fit 273.229 on c36 and re-level it to the piece mean, as c34 did. Keep the 274.24-274.67 shape.

**Target.** The 150 ms level within ±3 dB of -54 over 273.6-276.2, and no window above -50.

### 3. Cor anglais "solo, espr." (bars 47-50, qn 151-168): try the Leg Slur Exp row (inferred; manual p.109)

**Where.** The cor anglais quotation of movement I's second theme, the most exposed espressivo wind line in the movement. The same applies to "solo, dolce cantabile" at 124-140.

**Evidence.** The line plays Leg Slur MAX at v53-90, with Sus MAX at 156.94-158.94 for the tenuto at 157 (parts.json). Its legato joins and timing pass (c35/c36 reports). What the plain sustain row cannot give is the slower, singing onset and the vibrato that grows into long notes, such as the 3.5 qn A4 at 152 and the 157 tenuto.

**Manual.** p.109: Sus Expressive adds "a slower attack and a gently increasing vibrato". The EH KS Master has "Leg Slur Exp" (key 35) and "Sus Exp Vib" (key 30) (`ks_maps.json`). This is MANUAL-GAPS #5, never tried.

**Fix.** A/B in one render: `ART_SPANS["Cor anglais"] = [{"from": 150.9, "to": 168.5, "art": "Leg Slur Exp"}]`, keeping the 157 tenuto on its current Sus row. Full rebuild of the cor anglais (one more row). Then re-measure the entry at 151 and the crossovers. The slower attack may need about 0.05 s more lead (`entry_leads.json` / `leg_leads.json`). Keep the row only if the -6 dB arrival of the long notes stays within 0.15 s of the beat (S2) and the 152 and 160 notes still meet their printed p.

### 4. Basses "4 soli" (bars 65-70 and 87-92): the remaining patch change with an audible gain (inferred; MANUAL-GAPS #8, deferred in c35 and c36)

**Where.** Cb 220-238 (sul A, change bow at will, under Horn 1's solo) and 286-304 (under the final chord).

**Evidence.** The full Basses KS Master plays both passages at -3 dB (`SOLI_AS_META`). The level is on target (critic B, c35), but four players have a narrower, more focused sound than a section played quietly. The celli's 4 soli moved to DIV A in c33 (Violoncellos div), and the basses are now the only "4 soli" still on a full section. The patch `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is installed (c35 critic A checked).

**Manual.** p.89-90 (DIV A/B half sections, Close mics only).

**Fix.** A "Double basses soli" track on that patch, filled through `TRACK_WINDOWS` (220-238, 286-304) with `META_SKIP_TRACKS` as for Violoncellos div. If memory allows a 33rd instance (Close only, about 0.7 GiB against 44-45 GB settled), use one. Otherwise render it in a second pass. Refit the basses re-bow fills in those windows with `fit_rebows.py --window`. Do this only in a cycle that does not also refit finding 2's fills, or combine the two: the 273.229 piece is outside these windows, so they do not interact.

### 5. Violas' sotto voce portato, bars 48-51 (qn 152.5-167.5): every other note arrives about 0.1 s late (measured; S2, small)

**Evidence.** On Detache the notes alternate between two round-robin takes. The -6 dB arrival is +0.08..+0.09 s at 152.5, 154.5, 157.5 and 161.5, and -0.02..-0.06 s at 153.5, 156.5, 158.5, 160.5, 162.5, 163.5, 164.5 and 166.5. The peaks of the late takes are 3 dB higher (-46.6 against -49.7..-50.0). Separation is good: the rests drop 12-22 dB, and the notes sit 6-10 dB under the cor anglais. c36 critic A's energy-centroid range (-0.045..+0.093 s) shows the same spread.

**Fix.** `ENTRY_LEAD_AT["Violas"]` (or the Detache entry-lead table used since c29) +0.07 s on 152.5, 154.5, 157.5 and 161.5 only. Keep the per-note CC7. Re-measure, because the round-robin order may move if note timing changes the reset.

**Target.** All 15 arrivals within ±0.05 s.

## Checked and fine (measured unless stated)

- **Legato.** No chords on any legato row, and no legato transition wider than an octave (all tracks). Viola slurred triplets in bars 37-40 (Leg Slur MAX, 0.33 s notes): own-pitch share 30-200 ms median 0.92 (2 of 45 under 0.5). Viola pizzicato bars 41-44: 0.96.
- **Pizzicato (bars 37-44).** Violas: -6 dB arrival median +0.02 s, peak +0.06 s, 13 dB over the ringing before. Basses: +0.015 s, 23 dB rise.
- **Violins II div. sul tasto (bars 37-40, Flautando).** No trough inside the passage deeper than about 3 dB from the 1.5 s mean, apart from the edges.
- **Portato and tenuto.** Violins II portato pairs (bars 15-17): merged repeats dip 4.5-6 dB on the stem and 2.7-3.7 dB on the master at 44 and 50. Bars 61-62 molto sostenuto: string join dips 1.5-5.5 dB on a 30 ms window, all on body level. The deep wind values there (Flute 2 -10/-14) are flute vibrato on a 30 ms window (LEARNINGS §6).
- **Accents.** Trombone 1 213 and 218: 2-5 kHz over the first 80 ms is 9.4 and 13.8 dB under the body, the master 2-5 kHz jump is -1.4 and -3.8 dB, and the level is +5.3 dB over 212.5 and +2.2 over 217.5. Weight without bite. The other quotation notes are -0.5..-15 dB attack against body.
- **Tremolo (bars 61-64).** No hole at the violas' Tremolo entry (203.94) or at the 212 entries. The sf at 212 rises 4-6 dB on every string stem, and the CC7 fall follows it. 216 enters at p with no gap.
- **Re-bows.** On 200 ms windows, most string re-bows dip 1-4 dB with a step within ±3 dB. Larger steps follow printed diminuendos (bar 66 niente at 223: -5..-6; violas 86.861 into the p of bar 30). Loop pulse (100-300 Hz and centroid autocorrelation at 3.95 s) is 0.18 or less on the final-chord stems and master, the basses 4-soli pedals and the 13 s timpani roll at 226-237.5.
- **Wind repeats and breaths.** All 44 printed wind and brass breaths dip 7-29 dB on the stem, except Trombone 2 and Bass trombone at 204 (4-5 dB, 0.04-0.07 qn gaps under the strings' unbroken ff). Horn 3's con sord. 289 repeat dips about 5 dB for 0.25 s.
- **Mutes.** CC15 matches every printed con sord. / mettere sord. / senza sord., and never changes under a sounding note.
- **Timpani.** Rolls are smooth (sd of 100 ms steps 0.8-1.6 dB). Strokes sound 0.045-0.06 s after the beat by design (`TIMP_DELAY_S`). At 172 the stroke falls inside the harp's 40 ms roll, so there is no flam to fix.

**Do not touch:** Trombone 1's accents and quotation shapes; the violas' Detache portato and its CC7; the Violins II portato merges and notches (44, 50); the bar 61-64 tremolo rows, the sf CC7 lanes and the 216 p entries; the final-chord, opening and bar 66 re-bows and fits; the c34 basses shape at 274.24-274.67; the wind breath gaps; CC15 placement; the pizzicato rows and their velocity floor.
