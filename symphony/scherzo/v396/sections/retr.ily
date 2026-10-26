% c268: 247-248 Cl 1 pp < p > pp on the held E (was pp > pp: a diminuendo to the level it started from), the swell into the suspension and the softer resolution c098 asks for; 252 Vln I ends its crescendo on p with Cl, timpani and basses (was closed by \! on the rest with no level). MOLA PDF 10, Ex. 3: each hairpin leads to a printed level.
% RETRANSITION, bars 241-252 (c023: 12 bars, was 16), poco a poco accelerando to Tempo I.
% The introduction again, compressed: Hn 1's G sharp (held 237-240 at the end of the trio) falls to G natural at 241: E major turns to E minor
% on the retransition's first bar, with the E-minor key signature; timpani motive x on B (241); the head of theme A in the violas (241),
% Cl 1 (245; c161, was Vln II) and Vln I (249), pp, over the pizzicato B; bass A (iv7, 243; c013), French sixth (244; c062), V (245), V7 (251-252). (c193: header brought up to date.)
% c023: the old 241-244 (Hn 1 G sharp over E, timpani x on B) are cut: they prolonged the trio's E-major tonic for a further 4 bars after the
%   16-bar codetta 225-240 (A&S PDF 584-586: a modulation by chromatic inflection draws attention to itself and needs no padding).
% c053: 244 iv6 (Vc C3+A3, Cb C2 pizz.): the bass A-C-B expands iv by its 6/3 and reaches V by the Phrygian half step C-B, one bar per chord into 245
%   (Aldwell-Schachter Unit 18, PDF 297-298 Ex. 18-12, PDF 301 Ex. 18-19e); bar 244 was a bare viola E4. No G sounds at 244 (Hn 1 stops at 243 beat 3): no C-E-G.
% c013: bass A (iv) at 243 before the B pedal (245), so the returning V is approached from the subdominant (Aldwell-Schachter Unit 26 sec. 15, PDF 456).

% c037: no empty bars at 244 and 248: the outgoing voice holds the head's last E as a 4-3 suspension and resolves it to D sharp under the next
%   entry (Vla e' 243-245, d sharp' 246; Vln II e'' 247-248, d sharp'' 249 as Vln I enters). Adler II PDF 217 and 224 (Ravel, Petit Poucet: the
%   background dovetails or overlaps with each new entrance); PDF 209 (Dvorak: sustained harmonic counterpoint that completes the harmony without weight).
% c062: 244 French sixth C-E-F sharp-A sharp (Vc C3+A sharp 3, Cb C2, Vla E4, Hn 1 F sharp 4) instead of iv6: the cellos' A of 243 becomes the upper
%   A sharp while the bass rises A-C (chromaticized voice exchange from iv, A-S PDF 508-509 sec. 8, Ex. 29-14; 516-517 Ex. 29-28a), Hn 1's G (7th of iv7 at 243)
%   falls to F sharp, 2 of the key, held into the V at 245 as the common tone (PDF 507: the French sixth as neighbour of V, no parallels). The scherzo's return
%   is the movement's one augmented sixth, the chord A-S reserves for the approach to structural dominants (PDF 513, 526). No German sixth: C-E-G-A sharp holds C-E-G.
% c098: 245-246 (Vla) and 248-249 (Vln II) the outgoing voice's held E (4th over the B pedal) diminishes into its D sharp resolution, under the next head entry (A-S PDF 348: resolutions softer; PDF 352: contrast in dynamics clarifies a resolution sounding with another line).
% c106: 244 the cellos' pizz. C3 + A sharp 3 is divided (one note per desk partner), unis. again at 245. In first position the two notes lie on the
%   G and A strings with the open D string between them (a strummed chord would sound D3 inside the French sixth); on adjacent strings the
%   minor seventh is beyond the hand's compass in the low register (Adler I PDF 97: anything larger than sixth double-stops is difficult in the
%   low register; PDF 76, 88: what is difficult for one player is simple played divisi). Pitches, rhythm and dynamics unchanged.
% c152: 243-245 Bsn 1 A3-A sharp 3-B3 and Bsn 2 A2-C3-B2, pp, sustain the French sixth of 244 and its resolution. The pizzicato cellos' A sharp 3
%   decayed within the beat and leapt to B2, so the augmented sixth C-A sharp was never heard opening out to the octave on B (A-S PDF 503, Ex. 29-2;
%   PDF 504, Ex. 29-3a: 4-sharp 4-5 in an upper voice over iv6-V). The bassoons give C3-A sharp 3 -> B2-B3 in one register; A-A sharp-B is the motto tail turned upward.
retrBsnOne = { R2.*2 | a2.\pp( | ais2. | b2.) | R2.*7 | }
retrBsnTwo = { R2.*2 | a,2.\pp( | c2. | b,2.) | R2.*7 | }
% c161: 245-249 the second head entry of the retransition goes to Cl 1 (Vln II rests until its pizz. at 253): the entries pass viola -> clarinet -> violins,
%   as the first retransition passes viola -> oboe -> violins since c077. Adler II PDF 30 (Berlioz, Roman Carnival, Ex. XI-14: the effect of a canon comes from
%   the colour contrast between its voices more than from any other parameter); PDF 20 (Hindemith: later presentations take new colours). The clarinet,
%   the trio tune's first voice (153), carries the scherzo's head back out of the trio. c037's dovetail (E5 held 247-248, D sharp 5 at 249 under Vln I) and
%   c098's diminuendo into the resolution are kept; Cl 1 reaches pp at 249 with Cl 2 (shared staff) and then holds B4 from 250 as before. "1." printed at 245 (the combiner prints no label after the shared rest; c035, c135).
% c184: 251-252 Cl 1 takes the seventh A4 and Cl 2 keeps F sharp 4 (were Cl 1 B4 over Cl 2 A4, a major second in one colour for five beats): the pair now reads D sharp 5/F sharp 4, B4/F sharp 4, A4/F sharp 4,
%   Cl 1 falling through the V7 against Vln I's rising arpeggio (Rimsky-Korsakov PDF 90 rule 4: concords to instruments of one colour; PDF 91b: stationary and moving parts).
retrClOne = { R2.*4 | e''4-.\pp^\markup \bold "1." b'8-. b'-. e''4-. | g''2->( fis''8 f''8 | e''2.)~\< | e''2.(\p\> | dis''2.)\pp | b'2.\< | a'2. | a'4\p r4 r4 | }
retrClTwo = { R2.*8 | fis'2.~\pp | fis'2.~\< | fis'2. | fis'4\p r4 r4 | }  % c388: F sharp 4 tied 249-251 under the crescendo; 252 stays the marked arrival (Adler PDF 321; c288 kept 252)
% c227: Hn 1 sounds the G (the trio's G sharp turned to E minor) at 241, rests at 242 and takes G again at 243 as the seventh of iv7, held into F sharp at 244 (was G held 241-243):
%   the violas' head rose to its accented G4 minim at 242 in unison with the held horn G4 and its tail F sharp 4-F4 rubbed a step under it, so the head's peak was not heard as a new note.
%   Adler II PDF 274 (accompaniment registrally distant from the line), PDF 273 (horn and viola blend in this register), PDF 267 (the accompaniment thinned while the solo line plays).
%   242 is now the head alone, as 90 is in the first retransition. G sharp 4 (240) - G4 (241, 243) - F sharp 4 (244-245) unchanged in Hn 1 (c170).
retrHnOne = { g'2.\pp | R2. | g'2.( | fis'2.~ | fis'4) r4 r4 | R2.*7 | }
retrTimp = { b,4\pp b,8 b,8 b,4 | R2. | R2.*2 | b,4 b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | R2. | b,4\< b,8 b,8 b,4 | b,4 b,8 b,8 b,4 | b,4 b,8 b,8 b,4 | b,4\p r4 r4 | }
retrVlnOne = { R2.*8 | b'4-.\pp b'8-. b'-. b'4-. | dis''4-.\< fis''-. a''-. | b''4-. a''-. fis''-. | dis''4-.\p b'-. r4 | }
retrVlnTwo = { R2.*12 | }
retrVla = { e'4-.\pp b8-. b-. e'4-. | g'2->( fis'8 f'8 | e'2.)~ | e'2.~ | e'2.(\> | dis'2)\! r4 | R2.*6 | }
retrVc = { e4\pp^\markup \italic "pizz." r4 r4 | R2. | a,4 r4 r4 | <c ais>4^\markup \italic "div." r4 r4 | b,4^\markup \italic "unis." r4 r4 | R2. | b,4 r4 r4 | R2. | b,4\< r4 r4 | b,4 r4 r4 | b,4\p r4 r4 | R2. | }  % c037: 252 to the basses alone, so the cellos have a bar and two beats to take the bow for the arco line at 253
retrCb = { e,4\pp r4 r4 | R2. | a,,4 r4 r4 | c,4 r4 r4 | b,,4 r4 r4 | R2. | b,,4 r4 r4 | R2. | b,,4\< r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4\p r4 r4 | }% c116: 241 étouffez: the harp's rolled E-major chord of 237 (G sharp 3 in the middle register, which rings on: Rimsky-Korsakov PDF 46, Adler part 1 PDF 113-114)
%   is damped where Hn 1 turns G sharp to G natural, so no G sharp is left sounding under the turn to E minor.
retrHarpR = { R2.*12 | }  % c165: étouffez moved to the end of 240 (tC.ily)
