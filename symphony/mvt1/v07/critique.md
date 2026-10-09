# Critique of v7

Method: page 4 (bars 41–53) read at 65 dpi, build log, `analysis.txt`. Length 7:27. An independent reviewer (a separate agent reading the source and PDF) was also asked for the eight most important weaknesses. Its findings feed the v8 plan.

## Changes from v6
- **Transition rewritten (bars 37–44).** Two full motto-head units (B♭, C) are followed by four half-bar fragments rising through a B♭7 chord (d''–b♭'', f''–d''', a♭''–f''') and a scale into the E♭7 arrival. The arrival is now on g''' in the first violins and first flute, with oboe, clarinet and second violins an octave lower, so the climax has octave-doubled melody instead of a single line. The bass holds B♭ for two bars before E♭, so the arrival on E♭7 is prepared as a goal rather than reached by step.
- **Harp in the second theme's A section** moved up an octave, out of the register of the violas and second violins.
- **Mute markings removed.** Second violins and violas had two beats to put mutes on at bar 47 and none at bar 69. The pp marking does the job.
- **Hairpins.** A new tool (`tools/closehairpins.py`) closes crescendos and diminuendos that ran into rests; 26 were drawn across empty bars on page 4 and elsewhere. Four partCombine cases were fixed by hand with target dynamics.
- Flute marked mf, not p, where it doubles the oboe at bar 60.

## Remaining problems I can see
1. g''' in flute and violins is written with five or six ledger lines; it needs an 8va sign for legibility.
2. Bars 45–46 after the E♭7 climax drop straight to pp in two bars, so the dissolve is abrupt. One more bar of decrescendo, or a solo woodwind link, would let the second theme arrive in a quiet that has been prepared. The global bar count is fixed at 176, so this means reworking bars 43–46 rather than adding bars.
3. The independent review is pending. Its points will be weighed in v8 against the plan from v6 (D1 dialogue rigidity, first-theme accompaniment).
