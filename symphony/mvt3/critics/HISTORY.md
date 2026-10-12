# Movement III critic history

Cycle N reviews vNN and produces v(N+1). Each entry: Accepted, Rejected (with reason), Open, Do-not-touch.

## v01 (composer's first draft, 2026-10-12)
- 262 bars, 2/2, about 6:40 (402 s MIDI); plan in movement-3-plan.md. Sections: intro 1–10, pOne 11–26, pTwo 27–42, trans 43–50, sOne 51–66, sTwo 67–82, clos 83–98, dev 99–134, retr 135–150, recP 151–170, recS 171–198, codaOne 199–210, codaTwo 211–218, arrival 219–230, sHead 231–242, finale 243–262.
- Build: 0 warnings, 0 outer-voice parallels, 16 A3 pages (the page cap). Range flag: trumpet C6 at 239 and in the finale, accepted for C trumpet.
- Do-not-touch (cyclic rules from cyclic-notes.md "Start here for movement III"; change only by answering the reason there):
  - Bars 1–2: movement II's A♭ chord as a German sixth A♭–C–E♭–F♯ resolving to V, ff. Reason: mvt II critics 120 and 130, A&S p. 593.
  - No root-position V–I or V–i cadence in C before 254–255. Reason: the last cadence is the symphony's first since movement I bar 135.
  - Trumpets tacet 1–50; soft undoubled trumpet solo at 51. Reason: owed item 1.
  - String tremolo and the violins' C7 only from 219. Reason: owed item 2.
  - Stop chord B–D–F–A♭ (138, 218) resolves only at 218→219, trumpets B→C with the timpani.
  - Violas D♯→E at 215–216 (E♭/E♮ thread). Chorale top line `g1 | e'1 | d'1 | c'2 des'2 | c'1` (219–223) and its last statement ending `c'2 b2 | c'1` (251–255).
  - No tam-tam; Hn 3·4 "senza sord." at their first entry; timpani label "retune D♭ → G during the pause".

## Cycle 1 (v01 → v02), lens 1 melody, A&S Unit 20
- Accepted: F1 head in C major ff in horns and trombones 256–259; consequent peak A♭6–G–F at 22 and 162; appoggiatura at F2's first peak (53, 69, 173, 189); new F1 bar rhythm at 17 and 157; clarinet eighths held in 12, 16, 20, 24.
- Rejected: turn in F2 at 64, 80, 184 (the solo stays plain; it already has the appoggiaturas).
- Do-not-touch (critic): both chorale statements; the D–D♭–C passing tone in movement I's head; F1's head bar.

## Cycle 2 (v02 → v03), lens 2 harmony, A&S Unit 5
- Accepted: 218 bass D (stop chord over G; no V–I in C before 254–255); 254 cadence voice leading; iv6 at 57/177; 247 bass; chorale bass A at 222–223; brass revoicing 36–37, 111–112, 165–166, 243–249; 211–212; Tbn 1 and cellos at 1–2, 5–6.
- Kept: fifths at 244, 246 (quoted themes) and in upper voices of the German sixth (A&S PDF 526).
- Tool: tools/critic-scripts/c002/par.py checks every pair of staves for parallels (analysis.txt only checks top vs bass).

## Cycle 3 (v03 → v04), lens 3 form, A&S Unit 14
- Accepted: ending 256–262 aligned (all parts 20 bars, final chord 261–262, V–I echo at 260); 237–238 V6/5 of V into the 239 cadential 6/4; G7 at 133–134; crescendo 129–131; leading-tone doubling at 131–132 removed.
- Do-not-touch (critic): 218→219 arrival; both chorale statements; exposition key plan with the B♭ pedal into 51.
- Note for critics: the build does not warn when the last section's parts are short; check last onsets in the MIDI.

## Cycle 4 (v04 → v05), lens 4 orchestration, Rimsky-Korsakov ch. I, III
- Accepted: chorale f / canon ff balance 220–227; Hn 1 and Hn 3 voicing at 220, 222; second winds doubling at 243–250, 256–260; Fl 2 and Ob 1 registers 151–166; strings below the harp 123–130; Hn 1·2 mf at 11–26; bass drum at 219 and 261.
- Do-not-touch (critic): arrival chord scoring at 219; muted trumpet with cor anglais 171–186; accompaniment of the trumpet solo 51–66.
- Open (relay from movement II, 2026-10-12 14:18): add a starting harp pedal diagram at the harp's first entry, as movement II did at its bar 1 (cycle 116). Assigned to cycle 6 (playability). Timpani first tuning G, A♭, C, E♭ matches movement II's "muta D♭ in G" note.
