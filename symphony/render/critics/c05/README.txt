Critic 5 measurements (review of r05; report critics/c05.md). My renders are bit-identical to r05/out-m*.mp3 (MIDIs to r05-m*.midi), so no MP3 copies are kept.
m1/, m2/            r05 on mvt1/v156 and mvt2/v30 (scripts/meas.sh = r05/meas/scripts/meas.sh unchanged; no WAVs)
mixtable.md         mix table r04/r05/refs (scripts/mixtable.py; third-octave vs mean of four Brahms refs)
mixonsets.md        onset sharpness of whole mixes, renders and refs (scripts/mixonsets.py)
accents-m*.txt      accent boost / rise / onset crest / front edge per stem (scripts/accents.py)
pitch-m*.txt        tuning of isolated notes per stem (scripts/pitchcheck.py)
onset_tuning.txt    time to pitch per stem (scripts/onset_tuning.py)
iowa_onset.txt      previous-note lead-ins in assets/iowa samples (scripts/iowa_onset_pitch.py)
rollfront.txt       roll start front edges (scripts/rollfront.py)
blendstem-m*.txt    per-stem HF share / centroid / L/R (critics/c03/scripts/blendstem.py)
generality.txt      r05 score stages on mvt1/v191 and mvt2/v69 (r05/meas/scripts/generality.sh)
scripts/competitor.py, inv_by_stem.py   melody competitors per bar; inversions by too-loud stem
