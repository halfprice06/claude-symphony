% RETRANSITION, bars 241-252 (c023: 12 bars, was 16), poco a poco accelerando to Tempo I.
% The introduction again, compressed: Hn 1's G sharp (held 237-240 at the end of the trio) falls to G natural at 241: E major turns to E minor
% on the retransition's first bar, with the E-minor key signature; timpani motive x on B (241); the head of theme A in the violas (241),
% Vln II (245) and Vln I (249), pp, over the pizzicato B.
% c023: the old 241-244 (Hn 1 G sharp over E, timpani x on B) are cut: they prolonged the trio's E-major tonic for a further 4 bars after the
%   16-bar codetta 225-240 (A&S PDF 584-586: a modulation by chromatic inflection draws attention to itself and needs no padding).
% c053: 244 iv6 (Vc C3+A3, Cb C2 pizz.): the bass A-C-B expands iv by its 6/3 and reaches V by the Phrygian half step C-B, one bar per chord into 245
%   (Aldwell-Schachter Unit 18, PDF 297-298 Ex. 18-12, PDF 301 Ex. 18-19e); bar 244 was a bare viola E4. No G sounds at 244 (Hn 1 stops at 243 beat 3): no C-E-G.
% c013: bass A (iv) at 243 before the B pedal (245), so the returning V is approached from the subdominant (Aldwell-Schachter Unit 26 sec. 15, PDF 456).

% c037: no empty bars at 244 and 248: the outgoing voice holds the head's last E as a 4-3 suspension and resolves it to D sharp under the next
%   entry (Vla e' 243-245, d sharp' 246; Vln II e'' 247-248, d sharp'' 249 as Vln I enters). Adler II PDF 217 and 224 (Ravel, Petit Poucet: the
%   background dovetails or overlaps with each new entrance); PDF 209 (Dvorak: sustained harmonic counterpoint that completes the harmony without weight).
retrClOne = { R2.*8 | b'2.\pp | b'2. | b'2. | b'4 r4 r4 | }
retrClTwo = { R2.*8 | fis'2.\pp | fis'2. | a'2. | a'4 r4 r4 | }
retrHnOne = { g'2.~ | g'2.~ | g'2 r4 | R2.*9 | }
retrTimp = { b,4\pp b,8 b,8 b,4 | R2.^\markup \small \italic "hard sticks" | R2.*2 | b,4 b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | R2. | b,4\< b,8 b,8 b,4 | b,4 b,8 b,8 b,4 | b,4 b,8 b,8 b,4 | b,4\p r4 r4 | }
retrVlnOne = { R2.*8 | b'4-.\pp b'8-. b'-. b'4-. | dis''4-. fis''-. a''-. | b''4-. a''-. fis''-. | dis''4-. b'-. r4 | }
retrVlnTwo = { R2.*4 | e''4-.\pp b'8-. b'-. e''4-. | g''2->( fis''8 f''8 | e''2.)~ | e''2.( | dis''2.) | R2.*3 | }
retrVla = { e'4-.\pp b8-. b-. e'4-. | g'2->( fis'8 f'8 | e'2.)~ | e'2.~ | e'2.( | dis'2) r4 | R2.*6 | }
retrVc = { e4\pp r4 r4 | R2. | a,4 r4 r4 | <c a>4 r4 r4 | b,4 r4 r4 | R2. | b,4 r4 r4 | R2. | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | R2. | }  % c037: 252 to the basses alone, so the cellos have a bar and two beats to take the bow for the arco line at 253
retrCb = { e,4\pp r4 r4 | R2. | a,,4 r4 r4 | c,4 r4 r4 | b,,4 r4 r4 | R2. | b,,4 r4 r4 | R2. | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | }