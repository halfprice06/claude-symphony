
## From Movement I c51 (mockup-kit/README.md, last section; commit a6f4317f), relayed by the coordinator
1. Brass bells at 475 Hz -2.7, 821 Hz -3.9 and 3.2 kHz -3 dB lowered climax centroids by 64-114 Hz. Compare with ours (821 Hz -4, 3.2 kHz -4).
2. Phrase shapes (0.8 s rise, taper at the phrase end) work on brass. Winds need the offsets multiplied by 1.4.
3. Fit soft brass levels on the whole movement, not on a range test. Their range test said +3.7 dB at pp; the full render gave -2.0 to +3.4 dB per part and dynamic.
4. 80 ms string repeat gaps separate the notes on the stems, but in the master the hall fills them on violins and violas. Check our c09 "plain" new-bow gaps on the master, not only on the stems. The gaps did fix weak bass downbeats.
5. After changing held-note dynamics, check inner held notes under a tune: their Horn 3 was 4-6.6 dB too loud and needed -4 dB. Check this after our c09 sfp/subito changes.

## From the c09 actor (measured on the c09 render after its stem fix; cycles/c09/CHANGES.md)
1. 315 Hz hump still 4.9 / 8.5 / 5.4 dB over its 250-400 Hz neighbours in P / J / R (T 3.5; whole 4.3; target 3). The horn and viola bells took off only 1.5-2.5 dB: find the other sources (per-stem 315 Hz share in J).
2. Horns' soft passages fell 3-5 dB in plain RMS after the 315 Hz bell (Horn 1 pp 264-300 -53.6 dB, 10.9 under Vln I; stubs Hn 1 118 -53.9, Hn 2 122 -52.3). Check A- or K-weighted before lifting.
3. sfp 592: Double basses and Flute 2 have no sf (sf minus p 4.5 / 5.5 dB; peaks under the ff before). Level fixes cannot add it; try a higher sf velocity or the attack row on those tracks.
4. Basses lilt: on-beat minus off-beat attack -68 ms at 1088-1108 and -30 ms at 816-840 (target +-12) with CC16 resets at every span start. Level tables now give down - off 3.0-3.8 dB everywhere; do not refit them again without a new reset layout.
5. Brass accent fronts still 3-8 dB duller than plain notes on Horns 1-4, Trumpet 1 and the tuba (2-5 kHz front minus body); the swell from the moved note-on helped by 2.5-3.4 dB.
6. Repeat dips under 5 dB: Violas 832 3.8 (c08 9.9; the "plain" gap rule changed it), Violas 426 1.1, Violins I 884 0.0, Violoncellos 832 4.3.
7. Stem-fix roles added in c09 (roles.json "_c09_stemfix"): sfp 593-596 deepened to -12 on the flutes; if a later change gives the winds a real sf / p step in CC, shrink these rows first.
8. Brass "Sfz Cres" row A/B for 592 (manual p.103; 8 tracks, one more row each) still untried (memory).
