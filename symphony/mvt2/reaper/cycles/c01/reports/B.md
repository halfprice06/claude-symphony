# Critic B, cycle 1: balance and levels (render c00)

Method. All levels below are K-weighted (BS.1770 filter, LUFS-style dB) unless marked "RMS". Per-note levels: each note of each stem measured from onset+80 ms to min(end, onset+1.5 s), grouped by the value of the track's own `dyn_curve` at the onset, so they measure what the CC mapping does at each CC11 value. Per-bar levels: each stem over each bar in which it has notes. Scripts and data: `/private/tmp/claude-501/mockup-loop/c01-B/` (`an.py`, `bars.py`, `low.py`, `notes.json`, `bars.json`).

Median per-note level at a given CC11 dynamic (measured):

| track | pp | p | mp | mf | f | ff |
|---|---|---|---|---|---|---|
| Flute 1 | | -42.7 | -39.8 | -31.2 | -29.0 | -25.1 |
| Oboe 1 | | -34.9 | -36.0 | | | |
| Cor anglais | | -42.3 | -41.5 | | | |
| Clarinet 1 | -44.1 | -39.2 | | | | |
| Bass clarinet | -48.8 | -45.1 | -40.4 | -37.4 | -34.0 | -34.3 |
| Bassoon 2 | -47.8 | -41.2 | -39.6 | -36.4 | -34.6 | -34.8 |
| Horn 1 | | -38.0 | -35.9 | -32.1 | -31.7 | |
| Horn 3 | -44.7 | | | -30.4 | -26.2 | |
| Trombone 1 | | | | -38.7 | -35.5 | -35.2 |
| Timpani (roll) | | -23.8 | | | -20.0 | -19.1 |
| Harp | -64.1 | -56.0 | -45.1 | | | |
| Violins I | -52.0 | -51.4 | -44.7 | -41.5 | -36.8 | -31.2 |
| Violins II | -57.5 | -52.6 | -45.1 | -43.1 | -36.0 | |
| Violas | -52.9 | -48.0 | -46.0 | -38.6 | | |
| Violoncellos | -50.2 | -46.4 | -46.6 | -37.4 | -33.9 | |
| Double basses | -39.4 | -34.6 | -32.2 | -28.1 | -26.3 | -23.2 |

Loudest stem per bar (measured): Double basses in 29 of 92 bars, Timpani in 17 (it plays in about 20), Horn 1 11, Violins II 11.

## 1. A third of the printed dynamics are never applied: hairpins are paired wrongly (measured)

Where: 14 tracks, mostly bars 23-92. Worst: Violins I and II, Violas, Celli from bar 27 (qn 78) to bars 75-82; Horn 1 from bar 11 (qn 32) to bar 85; Horn 4 from bar 2 to bar 84; Clarinets 1-2 and Oboe 1 from bar 59-63 to the end.

What: `spans()` in `tools/score_to_parts.py` pairs a hairpin start (`-1`) only with a later stop (`1`) of the same kind, and ignores any new start while one is open. In the event list many hairpins have no stop (they end at the next dynamic or hairpin), and some stops carry the other kind (Timpani: `decresc -1` at qn 6, `cresc 1` at qn 8). The result is 15 spans longer than 8 qn: Horn 4 cresc qn 3-271 (268 qn), Horn 1 cresc 32-273, Violins I cresc 78-244, Violins II cresc 78-226, Violas cresc 78-172, Celli cresc 78-151, Clarinet 1 cresc 176-297, Oboe 1 cresc 188-273, Timpani cresc 168 open to the end. `dynamics_curve()` then skips every printed mark inside the span (`if q < hp_end: continue`) and draws one straight ramp across it.

Evidence: I compared each track's `dyn_curve` with every printed dynamic at its position. 91 of 287 marks are off by 8 CC or more. Examples: Violins II pp at qn 108 (bar 37, sul tasto accompaniment) gets CC11 80 (f), so in bars 37-40 Violins II is the loudest stem (-30 to -32) and the p flute solo sits 10 dB under it (-41/-42). Violins I p at qn 171 gets 86, ff at 204 gets 90, p at 216 gets 91. Clarinet 1 ff at qn 204 (bar 61) gets 38 (pp), f at 259 gets 46. Horn 4 f at 204 gets 36. Oboe 1 ff at 204 gets 49. Violas ff at 204 gets 66. Celli ff at 204 gets 45 and pp at 220 gets 50. Timpani CC7 climbs from 63 to 103 across bars 67-79 although the roll is ppp.

Fix (`score_to_parts.py`): replace `spans()` for hairpins with one pass per staff over cresc/decresc/dynamic events in time order. A start opens a hairpin of its kind and closes any open one at that qn. A stop of either kind closes the open hairpin. A dynamic mark later than the start closes it at the mark's qn. A hairpin still open at the staff's next rest of 2 qn or more closes at the end of the last note before the rest. In `dynamics_curve()`, never skip a printed mark: every mark sets the level at its qn. Add a check at the end of `build_track` that prints every printed mark where the curve differs by more than 2 CC; it should print nothing. This one change fixes more balance errors in the mix than any gain setting.

## 2. Timpani rolls are the loudest stem at ppp and cover the horn solo (measured)

Where: bars 2-3, 67-70 and 89-92 (ppp rolls), bar 52 (pp cresc. to p), bars 60-62 and 79-81 (f/ff rolls), bars 84-85 (pp single strokes).

What and evidence: the ppp rolls measure -27 to -29, 8-12 dB above the next stem (bar 2: Timpani -28, Double basses -40, Celli -41; bar 89: Timpani -28, Clarinet 1 -36). In bars 67-70 Horn 1 has "1. solo" p to mp and measures -28 to -34, while the ppp roll under it measures -27. In the f/ff tuttis the timpani are again the loudest stem (bar 61: -19 against Double basses -20 and Horn 2 -27). The BRIEF rule is that a roll starts at its dynamic and settles under the texture. Three causes:
- The roll articulation ("Timpani Flt Rls") is about 14 dB louder than single strokes ("Lng") at the same CC7 and velocity (p strokes at qn 172 and 271: -38.8 and -37.6; p roll at qn 200: -23.8).
- Velocity hardly changes the roll level (ppp roll at vel 31: -29.3; p roll at vel 53: -23.8, of which about 4 dB comes from the CC7 difference 63 to 80). CC7 is the only working control, and `cc7 = 50 + 0.6*v` gives 63 (ppp) to 112 (ff), about 9 dB if Opus uses the usual 40*log10(v/127) law (inferred).
- Single strokes have the opposite problem: the pp strokes at qn 277-283 (bars 84-85, vel 41) measure -62 to -68, which is inaudible, while vel 53 strokes measure -38. So there is a steep velocity layer step between 41 and 53.

Also, the Timpani Flt KS patch loads the Surround mic as well as Close and Main (`layerMatrix.columns`). Every other track loads Close and Main only.

Fix (`score_to_parts.py`, timp block of `build_track`): compute CC7 per articulation, as 127*10^(dB/40) with dB from the corrected `dyn_curve` (finding 1). Rolls: ppp -36, pp -31, p -26, mp -22, mf -19, f -16, ff -14 (CC7 16, 21, 28, 36, 42, 50, 57). Strokes: 12 dB higher (ppp -24, pp -19, p -14, f -4). Write the CC7 value at each articulation change too, so a stroke after a roll gets its own level. Set the velocity of "Lng" strokes to at least 56 (pp 56, p 64, mf 80, f 96), and of rolls to the printed-dynamic velocity, unchanged. In `build_reaper.py` `state_for`, set the timpani's Surround column to off, matching the others. Targets for the next render: ppp roll at -48 to -52 (under the strings' pp), the f/ff rolls 3-6 dB under the loudest string or horn stem, and pp strokes at -48 to -52.

## 3. The double basses are 12 dB above the celli and lead the mix (measured)

Where: the whole movement. They are the loudest stem in 29 bars, including bars 21-30 and 45-47. In bars 21-28 they are 10-20 dB above the Celli's "unis., cantabile" p line (bar 25: Double basses -30, Celli -42; bar 26: -30 against -53).

Evidence: at the same CC11, the Double basses measure -34.6 at p against Celli -46.4, Violas -48.0, Violins I -51.4. At pp they are -39.4 against -50.2. They carry 99.7% of the mix's 40-90 Hz energy. The long-term spectrum has the 63 Hz band at +14.1 dB relative to 1 kHz, against -6.2 in the Dvorak 9 reference (metrics.md), about 20 dB too much bass. The pizz. basses in bars 37-44 (p, -34 to -45) also sit above the p flute and cor anglais solos (-41/-42). By orchestral norms the basses sit at or slightly under the celli in loudness. Adler and Rimsky-Korsakov both treat the bass line as a foundation, not a lead.

Fix: add a per-track gain (see finding 4) of -11 dB on Double basses. This brings their p to about -46, level with the celli, and should bring the 63 Hz band within a few dB of the reference. Check that the 63 Hz band comes out between -2 and +4 dB relative to 1 kHz.

## 4. The same printed dynamic gives levels 17 dB apart across families; strings sit under solo winds (measured, targets inferred from Rimsky-Korsakov)

Where: every passage where strings and winds play together, for example bars 15-20 (Oboe p -35/-38 against muted strings pp -48 to -57) and bars 45-47 (Oboe p -35 against Celli p -52).

Evidence: at p (CC11 46) the solo winds measure Oboe -34.9, Horn 1 -38.0, Clarinet 1 -39.2, Bassoon 2 -41.2, Cor anglais -42.3, Flute -42.7, Bass clarinet -45.1. The string sections measure Violins I -51.4, Violins II -52.6, Violas -48.0, Celli -46.4. Harp -56.0. Rimsky-Korsakov, Principles of Orchestration (reference-books/text/rimsky-principles/p0051.txt), gives the norm. In piano all wind instruments, wood or brass, are about equal. In piano one whole string department (all Violins I) equals one wind instrument. In forte one department equals two winds, a horn equals two woodwinds, and a trombone equals two horns. The mockup has violins 9-17 dB under a solo wind at p, and the oboe 8 dB above the flute. At f the trombones are 4-9 dB under the horns (Trombone 1 f -35.5; Horn 1 f -31.7, Horn 3 f -26.2), not above them. The CC11 slope itself is consistent: about 14-15 dB from p to f in Violins I, Flute and Celli, so per-track gain is the right tool, not a new curve.

Fix: add a `gain_db` field to each row of `TRACKS` in `score_to_parts.py`, write it into parts.json, and in `build_reaper.py` `track_job` add `reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 10^(gain_db/20))` next to D_PAN. Values in dB, chosen so that p is about -46 for every solo wind and every string section, with the Celli unchanged:
Flute 1/2 -4, Oboe 1/2 -9, Cor anglais -4, Clarinet 1/2 -6, Bass clarinet -1, Bassoon 1/2 -4, Contrabassoon 0, Horns 1-4 -7, Trombones 1-2 and Bass trombone 0, Tuba 0, Harp +6 (see finding 5), Violins I +5, Violins II +6, Violas +2, Celli 0, Double basses -11, Timpani 0 (handled by CC7, finding 2).
After the render, rerun the per-dynamic table. Medians at p should fall within ±3 dB of each other, except the basses 0-3 dB under the celli and the harp 2-4 dB under.

## 5. The harp is 10-20 dB too quiet and its dynamics are compressed twice (measured; cause partly inferred)

Where: bars 7-14 (harp under the horn solo: -56 to -67, one bar -89), bars 37-44 (p chords: -55 to -61, and bars 38, 40 and 44 at -85 to -93, which is inaudible), bars 53-56 (-41 to -46).

Evidence: the harp measures -64.1 at pp, -56.0 at p and -45.1 at mp: 19 dB from pp to mp, against about 7 dB for the strings. Harp Maestro is velocity-driven, and `build_track` also sends it the full CC11 dynamics curve. In this library CC11 "controls overall volume" (HO manual, section 2.1.3 "Instrument programming"), so a soft harp note is attenuated twice (inferred). The Harp Maestro patch loads only the Close mic (columns Close on, Main off), while every other track loads Close and Main. That makes the harp drier and lower than the rest (measured from the .oib; level effect inferred).

Fix: in `score_to_parts.py`, for family "harp" send a constant CC11 of 110 instead of `dynamics_curve`, and set velocity from the printed dynamic: pp 52, p 64, mp 76, mf 90, with ±4 per note across a chord for evenness. In `build_reaper.py` `state_for`, for the harp set the Main column's loaded/enabled flag to true, like the other patches. Use track gain +6 (finding 4). Target: p chords at about -48 to -50, audible but under sustained p winds. Rimsky-Korsakov p0051 notes that sustained groups easily overpower plucked strings, so the harp should stay a little under them.

## 6. Printed solos do not stand out; the opening chord has no celli (measured; fix inferred)

Where: Violins I "solo, senza sord." bars 17-22 (qn 48), played by the section; Horn 1 "1. solo" bars 67-70 (masked by the timpani, finding 2); Celli "cantabile" bars 23-28 and 80 onwards; bar 1.

Evidence: in bars 17-18 the Violins I solo (p) measures -49 and -44, level with the muted pp Celli accompaniment (-45 and -50). Bar 1: the Celli's first note (C3 at qn 0, ppp) renders as silence (-121 dB), while the Violas and Violins I notes at the same qn and the same CC11 22 render at -59 to -64. The Celli's Sus MAX keyswitch sits at qn 0, at the same instant as the note, because KS_LEAD is clamped to 0 (inferred cause).

Fix: in `dynamics_curve()`, add +8 CC11 (about +3 dB at the measured slope of 0.3-0.35 dB per CC step) to staves after a text containing "solo", "cantabile" or "espr.". The boost runs until the next text on that staff or the next rest of 3 qn or more. Do not apply it to tutti entries ("tutti" in the text). For bar 1, skip a keyswitch event at qn 0 when it equals `first_ks`, since the patch state already selects it. If the Celli are still silent in bar 1, start the Celli's first note 0.02 qn late. Check that Celli bar 1 measures above -60.

Do not touch: the CC11 slope (about 0.3-0.35 dB per CC step, p to f about 14-15 dB in Violins I, Flute and Celli); the Horn 1 solo balance in bars 6-14 (10-14 dB over the pp bassoons and bass clarinet); the Double basses' dynamic curve (no misplaced marks, only the gain is wrong); CC1 vibrato following CC11; CC15 con sordino; the pans; the KS Master patch choices.
