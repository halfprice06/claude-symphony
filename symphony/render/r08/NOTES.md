# r08 (actor 8): work in progress

Built from r07 and critic 7's plan (critics/c07.md section 9). Test inputs mvt1/v203, mvt2/v82.
Progress log (updated as the work goes; final notes replace this):
- copied r07 code, config, sfz, lib, meas/scripts (paths r07 -> r08 in the .sh scripts).
- plan 1: articulate.py: every drum of a roll chain keeps the chain's printed-dynamic trim (timp_roll_chain_keep_trim).
- plan 2: brass printed_trim_dB refit (config _doc_trim_r08); velocity crossfades not used (build_iowa: crossfading two takes beats, 3.3 dB ripple).
- plan 3: tone + air shelves on brass stems (config _doc_distance_r08).
- plan 4: balance.py spot lift for soft solos up to 6 stems (spot_soft_*).
- plan 5: accent bumps for bass clarinet, basses, tuba, flutes, oboes.
- plan 6: release 0.08/0.09 s for wind/brass notes < 0.5 s.
- plan 8: trombones width 0.4.
- next: full render m1 with --keep-synth into /tmp/render-08-m1, measure.
