Critic 4 measurements (review of r04; report critics/c04.md).
m1/, m2/                  r04 on mvt1/v156 and mvt2/v30 (scripts/meas.sh = r04/meas/scripts/meas.sh unchanged)
ref_brahms1_ii_musopen/, ref_brahms4_ii_musopen/   slow-movement references (tools/measure.py), files in assets/refs
rollcurve-m*.txt          timpani rolls per 1 s window (scripts/rollcurve.py)
melody_nt-m*.txt          melody relief over whole phrase and balanced bars (scripts/melody_nt.py)
blendstem-m*.txt          per-stem HF share / centroid / L/R (critics/c03/scripts/blendstem.py)
ltas_vs_refs.txt          third-octave r03/r04 minus mean(Brahms 1, 4) (r04/meas/scripts/ltas.py)
cmp-m*.md/.png            tools/compare.py tables; generality_v181_v56.txt (scripts/generality.sh)
My renders are bit-identical to r04/out-m1.mp3 and out-m2.mp3 (and the MIDIs to r04-m*.midi), so no MP3 copies are kept.
