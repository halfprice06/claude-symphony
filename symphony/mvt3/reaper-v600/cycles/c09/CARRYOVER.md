
## From Movement I c51 critics (symphony/mvt1/reaper-v621/cycles/c51/reports/), relayed by the coordinator
1. Loud tutti tone: their simulated fix matches our c08 re-voicing (brass 475 Hz -2.7, 821 Hz -3.9, a 3.2 kHz -3 bell, brass gains -1.8 to -4.0 dB for loudness). Check our climax centroid against Dvořák (824 Hz).
2. HP_CURVE: keep timpani roll lanes linear. The curve lifted a fff→pp roll up to 8 dB over a mp solo.
3. Soft timpani rolls: under the template every other stem lost 2.1-2.5 dB in 30-150 Hz and the timpani did not. Fix (simulated): a 160 Hz -3 dB low shelf on the timpani during soft-roll spans only, +1 dB level there.
4. String shorts: on HO string short rows, CC11 parking is only a level change and velocity picks the layer, so one velocity table can move a note's layer by up to about 10 dB. Keep each note's current layer; compensate the CC11 park in the volume envelope and put the beat weight there (+1.5 / 0 / -1 dB). Check our c08 metric tables against this.
5. PHRASE_SHAPE (their measurement on our c07): about 0.26-0.30 dB per lane unit, about 3 dB of taper where the lane taper is 8 units or more; the "drive" type does almost nothing (0.1 dB). Consider scaling it up.
