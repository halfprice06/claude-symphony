# Critic A, cycle 50: articulation and phrasing

Render under review: `cycles/c49/render/` (master and stems), with `cycles/c49/rendered_build/` (parts.json and the data
tables that produced it), compared join by join with the c47 and c48 renders. Positions are score quarter notes (qn);
bar b starts at qn 3(b-1) up to bar 36, 108 + 4(b-37) for bars 37-64, 220 + 3(b-65) from bar 65. Because c50 is the
rebuild of the legato tracks and the refit of the leads, this report measures the legato joins of every track: 727 joins
on 22 tracks. Two numbers per join, both from `tools/pcx.py` (imported read-only), both relative to the score onset,
positive = late: **pcX**, the perceived attack centre of the new pitch's band, and **cross**, the time the new pitch's
band reaches the old pitch's band (the pitch change). pcX moves later when the level keeps rising after the beat; cross
does not depend on any track-level gain. Values are c49 unless three are given (c47/c48/c49). Every judgement is marked
**measured** or **inferred**. Order of work assumed: Finding 2 before the join measurements of ONE_TIME step 3 (it
changes pcX on 67 joins); Findings 1 and 3 are step 4; Finding 4 after the leads are settled; Finding 5 says what the
rebuild is likely to change. The non-legato items of the lens were not re-measured this cycle (list at the end).

All data in this report are c49's rendered data (`cycles/c49/rendered_build/`), not the live `build/` folder, which has
since received the approved score change at bars 36-37. Two consequences for the lists below, neither of them a
finding: the Cor anglais join at 108 (72>77, counted here as one of its 14 joins within +-60 ms) no longer exists, and
the new Flute 1 join at 108 (72>77) is not in the c49 audio, so it has no measurement; measure it with the others on
the first c50 range render.

## Manual notes

The reading schedule has no row for cycle 50. Pages consulted for the findings (Opus Edition User Manual 2021):

| Page | Content | Used in |
|---|---|---|
| 79 | Legato group: monophonic true legato, every interval transition recorded; Leg Bow Change; transition timing depends on note velocity | Findings 1, 3 |
| 80 | Leg Exp Vib (for slower tempos), Leg Lyr Vib, Leg Runs (connected notes up to 3 semitones play a runs articulation, wider intervals a bow change), Leg Slur | Findings 3, 6 |
| 99 | A slur needs two notes without a significant gap; legato instruments are monophonic by default (CC22 switches that off) | passed checks |
| 101 | Legato Repetitions: re-bowed or re-tongued repeated notes inside a legato phrase | Finding 6 |
| 144 | Monophonic True Legato script: velocity about 50-60 gives the longest transition, 110-127 the shortest; velocity then does not set loudness | Findings 1, 6 |

## Findings

### 1. Lead refit: 87 of 727 joins need a lead change (52 late, 35 early); 80 more read late on pcX but change pitch on time

**Where.** Every legato row. Classes (median of c47, c48, c49): **A** pcX >= +60 ms and cross >= +40 ms (lead too
short); **B** pcX >= +60, cross < +40 (pitch change on time, level builds late); **C** pcX <= -60 and cross <= -40
(lead too long); **D** pcX <= -60, cross > -40; **var** = the three renders differ by 25 ms or more; ok = pcX within
+-60 ms.

| Track | joins | ok | A | B | C | D | var | median pcX (ms) |
|---|---|---|---|---|---|---|---|---|
| Flute 1 | 52 | 42 | 5 | 2 | 3 | 0 | 0 | +7 |
| Oboe 1 | 32 | 22 | 3 | 4 | 0 | 0 | 3 | +31 |
| Cor anglais | 29 | 14 | 0 | 11 | 0 | 0 | 4 | +35 (c48: -1) |
| Clarinet 1 | 20 | 17 | 0 | 3 | 0 | 0 | 0 | +9 |
| Clarinet 2 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | +45 |
| Bass clarinet | 18 | 13 | 1 | 4 | 0 | 0 | 0 | +20 |
| Bassoon 1 | 30 | 25 | 1 | 3 | 0 | 0 | 1 | +20 |
| Bassoon 2 | 14 | 9 | 1 | 4 | 0 | 0 | 0 | +28 |
| Horn 1 | 41 | 34 | 0 | 4 | 1 | 2 | 0 | -16 |
| Horn 2 / 3 / 4 | 5 / 4 / 4 | 4 / 4 / 2 | 0 / 0 / 2 | 1 / 0 / 0 | 0 | 0 | 0 | +2 / -19 / +62 |
| Trombone 1 | 4 | 3 | 0 | 0 | 0 | 0 | 1 | -24 |
| Violins I | 86 | 52 | 14 | 5 | 3 | 3 | 9 | +17 |
| Violins II | 114 | 68 | 9 | 13 | 10 | 7 | 7 | +18 |
| Violas | 134 | 91 | 8 | 11 | 6 | 11 | 7 | +4 |
| Violoncellos | 105 | 67 | 7 | 11 | 11 | 2 | 7 | +2 |
| Double basses | 3 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| Violin I solo | 9 | 8 | 0 | 1 | 0 | 0 | 0 | +9 |
| Violoncellos div / Violas div | 7 / 6 | 4 / 2 | 0 / 1 | 0 / 2 | 0 | 0 | 3 / 1 | +1 / +80 |
| Horns 1-2 a2 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | -18 |
| **All** | **727** | **492** | **52** | **80** | **35** | **25** | **43** | |

**What is wrong (measured).** 492 joins (67.7 %) lie within +-60 ms. The errors are not a per-track offset: every track
median is within +-45 ms except Horn 4 and Violas div, while the spread inside a track (robust SD of pcX) is 62-63 ms on
Violins I, Violins II and Violas, 51 on the Violoncellos, 54 on the Bass clarinet, 47 on Oboe 1, and 14-27 ms on
Clarinet 1, Bassoon 1 and Flute 1. Each join repeats: the median difference between the three renders is 0-1 ms on every
track with more than 3 joins. A row lead therefore cannot correct these tracks; the correction is per onset or per pitch
pair. Only classes A and C can be corrected by a lead. In class B the pitch already changes within 40 ms of the beat and
pcX is late because the level rises after it (Findings 2 and 4); more lead on those 80 joins would move the pitch change
ahead of the beat. Velocity is not available as a tool: string joins are already at velocity 124 (the range the manual
gives for the shortest transition, p.144), and inside a track velocity correlates with pcX at -0.27 to +0.38 only.

**Fix.** In `build/leg_leads.json` (seconds per score onset, added to the row lead; add to an existing entry, or create
one; the total is clamped to 0.03-0.35 s), change the lead where pcX and cross agree, by the smaller of the two rounded
to 10 ms, at most 100 ms in one pass. The amounts assume 1 ms of join per ms of lead (**inferred**: no lead changed
between c47 and c49, so the response is not measured; check it on the first range render). Notation: onset (bar;
old>new MIDI pitch; pcX/cross ms) change in ms. "cap" marks joins that also need Finding 3.

Class A, add lead:

- Flute 1 (row 30 ms): 110 (b37; 77>78; +65/+82) +70; 113 (b38; 73>72; +102/+52) +50; 120 (b40; 73>72; +82/+66) +70;
  113.5 (72>73; +99/+56) and 121 (72>73; +117/+64): these are the only joins of that pair, so set
  `LEG_PAIR_EXTRA_S["Flute 1"][(72, 73)] = 0.06` in `build/score_config.py` instead. Keep (73,72) per onset: its third
  join 121.5 is class B (+75/+14).
- Oboe 1 (row 60): 57 (b20; 70>68; +93/+78) +80; 193.5 (b58; 80>78; +142/+58) +60; 269.5 (b81; 75>73; +125/+52) +50.
- Bass clarinet 31 (b11; 44>48; +60/+44) +40. Bassoon 1 143 (b45; 61>60; +175/+102) +100. Bassoon 2 261 (b78; 52>51;
  +248/+54) +50.
- Horn 4: 292 (b89; 52>51; +137/+114) +100; 268: see Finding 5.
- Violins I (row 170): 72 (b25; 73>72; +72/+108) +70; 74 (b25; 70>68; +66/+80) +70; 78 (b27; 65>68; +105/+72) +70;
  79.5 (b27; 68>72; +146/+42) +40; 174.5 (b53; 78>77; +70/+52) +50; 199 (b59; 85>82; +124/+76) +80; 244 (b73; 85>84;
  +84/+90) +80; 252 (b75; 72>77; +116/+62) +60; 254 (b76; 77>82; +122/+70) +70; cap: 182, 185.5, 186, 192, 258.5.
- Violins II (Leg Slur row 240): 162 (b50; 81>74; +168/+100) +100; 168 (b52; 75>77; +101/+68) +70; 199 (b59; 73>70;
  +102/+88) +90; 204 (b61; 72>68; +83/+46) +50; 208 (b62; 73>77; +123/+64) +60; cap: 177.5, 181.333, 182, 186.
- Violas (Leg Slur row 225): 292 (b89; 52>51; +68/+51), the pair's only join: `LEG_PAIR_EXTRA_S` (52, 51) -0.08 -> -0.03;
  cap: 193.667, 195.333, 195.667, 250, 257. No room: 111 (b37; 65>61; +84/+51) and 189 (b57; 65>61; +102/+69) already
  use 0.75 of a 0.32-0.36 s note (Finding 6).
- Violoncellos: 77 (b26; 56>55; +96/+70) +70; 156 (b49; 49>54; +118/+120) +100; 184 (b56; 36>45; +210/+60) +60;
  188 (b57; 46>53; +206/+72) +70; 261 (b78; 59>60; +105/+84) +80; cap: 68.5, 145.5.
- Violas div 286 (b87; 65>56; +93/+82) +80.

Class C, reduce lead:

- Flute 1: all four joins of the pair (77,75) are early at its extra of 0.12: 111 (b37; -61/-94), 118 (-57/-29),
  130 (-45/-114), 135 (b43; -163/-118): set `LEG_PAIR_EXTRA_S["Flute 1"][(77, 75)]` 0.12 -> 0.06 and add "135": -0.05;
  200 (b60; 82>84; -112/-184): "200" 0.2 -> 0.10.
- Horn 1 193 (b58; 65>63; lead 350 ms, at the clamp; -97/-182): "193" 0.1 -> 0.0.
- Violins I: 67.5 (b23; 68>72; -70/-64) -60; 191.5 (b57; 89>90; -77/-60) -60; 242 (b72; 87>86; -78/-66) -70.
- Violins II: 56 (b19; 68>67; -92/-80) -80; 70 (b24; 75>74; -123/-112) -100; 177 (b54; 73>72; -124/-94) -90;
  181 (b55; 78>77; -78/-108) -80; 195.5 (b58; 78>77; -124/-108) -100; 238 (b71; 65>68; -61/-82) -60; 244 (b73; 73>72;
  -133/-84) -80; 246 (b73; 70>68; -86/-92) -90; 247 (b74; 68>67; -69/-74) -70; 255 (b76; 82>80; -92/-52) -50.
- Violas: 109.333, 110 and 111.333 (b37; 61>56; -67..-70 / -85..-91) -70 each, per onset (the pair's joins at 189.333
  and 192 do not agree); 118 (b39; 61>58; -80/-47) -50; 247 (b74; 56>51; -93/-77) -80.
- Violoncellos: 60 (b21; 48>49; -64/-60) -60; 76 (b26; 58>56; -71/-64) -60; 81 (b28; 53>56; -73/-60) -60, and its
  early fill's `pre_s` 0.11 -> 0.05 with it; 145 (b46; 58>57; -66/-50) -50; 193 (b58; 53>51; -83/-84) -80; 199 (b59;
  51>52; -82/-70) -70; 200 (b60; 52>51; -98/-46) -50; 219.5 (b64; 47>46; -74/-70) -70; 240 (b71; 51>56; -77/-60):
  "240" 0.08 -> 0.02; 244 (b73; 55>56; -101/-82) -80; 292 (b89; 49>44; -71/-90) -70.
- Double basses 83 (b28; 49>46; -108/-152) -100.
- Optional, inside +-60 ms but both joins of the pair early on both numbers: Bassoon 1 (61,58) 0.12 -> 0.06 (36:
  -51/-88; 256: -58/-104); Horn 1 (58,56) -0.04 (26, 39) and (62,61) -0.05 (23, 230); Violas (68,58) -0.05 (242, 243).

Class B, do not add lead (pcX/cross):

- Flute 1 121.5 (+75/+14), 189 (+127/-44). Oboe 1 140 (+135/-24), 189 (+144/-42), 199 (+92/+22), 200 (+76/-8).
- Cor anglais 97 (+127/-22), 99 (+83/-12), 127.5 (+111/-2), 128 (+177/+6), 132 (+254/-26), 134 (+135/-4), 136
  (+213/+24), 155.5 (+136/+8), 162 (+88/-34), 171 (+111/0), 292 (+170/-8).
- Clarinet 1 194, 259 (+128/-84), 283. Bass clarinet 22, 26, 35 (+112/-6), 108. Bassoon 1 146 (+147/+4), 200
  (+172/+30), 252. Bassoon 2 31 (+208/+22), 243 (+111/+12), 244, 246. Horn 1 32 (+129/+18), 177.5, 192 (+133/+34), 199.
  Horn 2 252.
- Violins I 80, 181.667, 250, 256, 268. Violins II 60 (+101/-28), 65 (+129/-4), 67.5 (+117/-4), 79.5, 80, 82
  (+173/-18), 161, 171, 181.667, 210, 251.5, 257.5 (+179/+6), 261 (+122/+38).
- Violas 112.667, 194.667, 195, 239.5, 240, 241.5 (+127/-48), 242.5 (+108/+13), 245.5 (+170/-13), 249 (+152/+17),
  251.5, 259. Violoncellos 75, 86 (+97/-66), 132 (+125/-14), 140 (+167/-8), 142, 142.5 (+148/-28), 146, 195.5, 253,
  255 (+111/-74), 258 (+190/-58). Double basses 186. Violin I solo 61. Violas div 69, 72 (+175/+26).

Class D, leave: Horn 1 18, 38; Violins I 174, 237.5, 249.5; Violins II 62, 174, 188, 219, 220, 268, 271; Violas
108.333, 111.667, 112.333, 116.333, 117.667, 122.333, 188.333, 189.667, 190.333, 244.5, 246.5; Violoncellos 160, 259.
Cross is not usable in the returning-note figures (Violins I/II 181.667, Violas 114, 193, 194, 194.667, 195).

These lists are c49 values. After the rebuild, apply a change only where the join is still in the same class on the new
measurement.

**Pass.** Every class A and C join within +-40 ms on both pcX and cross; no join that is now within +-60 ms leaves that
range; cross of the class B joins stays within +-40 ms. Report S2 with class B counted separately from A and C. Expected
(**inferred**): 492 -> about 579 of 727 joins (79.6 %) within +-60 ms from the leads alone.

### 2. Positive pitch trims on joined notes drop out at the join: a c49 regression on the Cor anglais solo; the same shape acts on 67 joins

**Where.** Every joined note whose pitch has a positive entry in `build/pitch_trims.json`: 67 joins. Cor anglais 11
(bars 41-44 and 49-52: 127.5, 130, 131.5, 134, 156, 166, 168, 171 and others; the +3 dB entries for pitches 65 and 66
are new in c49), Flute 1 12 (bars 37-40), Violas 23, Bassoon 1 9, Bassoon 2 4, Horn 1 4, Clarinet 1 2, Clarinet 2 2.

**What is wrong (measured).** c49's two new Cor anglais trims moved four joins later with the pitch change unchanged:
130 (68>66) -22 -> +39 ms, 156 (68>66) -18 -> +48, 166 (68>66) -28 -> +35, 168 (66>65) -21 -> +82; cross changed by 0 to
2 ms at all four. Bassoon 1 253 (53>56, pitch 56 new at +5) went from +85 to +250 ms with cross at +86 in both. The Cor
anglais track median went from -1 to +35 ms and its joins with a dip of 6 dB or more from 4 to 7 (40 ms RMS; 131.5: 8.6
dB / 100 ms -> 10.1 dB / 130 ms; 134: 4.0 / 125 -> 6.7 / 225; 130: 2.6 -> 5.5; 168: 2.1 -> 4.3). Level of the new
pitch's band against the note's own body, 0-50 / 50-100 / 100-200 ms after the beat: Cor anglais 168 was -2.8 / -3.9 /
-1.6 dB in c48 and is -5.0 / -6.2 / -3.3 in c49; 130 was -2.2 / -1.3 / +1.2 and is -5.1 / -4.3 / 0.0. The older trims
show the same form: Bassoon 2 261 (+6) -11.0 / -8.6 / -7.9, Clarinet 1 259 (+6) -9.2 / -8.4 / -7.9, Cor anglais 134 (+4)
-7.6 / -8.4 / -7.5. Flute 1's 12 trimmed targets have a median pcX of +57 ms against +4 for its other joins; Bassoon 2's
four +159 against +18.

**Cause (measured in the lane, and in the code).** `trim_shape` in `tools/score_to_parts.py` (line 4221): the previous
note's trim ends over [next moved onset - 0.05, + 0.03] qn, but a joined note's pitch trim starts at 0 at its moved
onset and takes 0.25 qn to arrive (the branch `if joined_in(n) and ramp == 0.25`). The function's own docstring
describes a crossfade over [moved - 0.05, moved + 0.03]; the 0.25 qn ramp was introduced in c09 for negative trims.
In c49's `vol_db` lane at Cor anglais 168 (66>65, both +3) the level is +3.9 dB up to 0.05 qn before the moved onset,
+2.0 at the moved onset and +1.2 at +0.03 qn: a 2.7 dB drop during the transition, where c48's lane was flat (+0.9).
At 130 (untrimmed 68 > trimmed 66) the lane is -0.3 dB at the moved onset and reaches +3.6 only 0.25 qn later, about
0.2 s after the beat.

**Fix.** In that branch, start positive trims with the mirror of the previous note's release ramp:
`a0, a1 = (m - 0.05, m + 0.03) if (dbv is not None and dbv > 0) else (m, m + 0.25)`. Negative trims keep the 0.25 qn
ramp (the c09 evidence concerns them). Two notes with the same positive trim then hold a constant sum through the
join. Do this before the join measurements of ONE_TIME step 3: it changes pcX (not cross) on all 67 joins, among them
the class A targets Flute 1 110, 113, 113.5, 120, 121 and Bassoon 2 261 and nine class B joins (Cor anglais 127.5, 134,
171; Clarinet 1 259; Bassoon 1 200; Bassoon 2 31, 243; Flute 1 121.5; Violas 249). Cor anglais 127.5 and 171 were
already at +111 ms in c47 and c48, before their trims existed, so the fix is not expected to bring those two inside
+-60 ms. Risk (**inferred**): the last 40-50 ms of the previous note are raised by up to the trim.

**Pass.** Range renders of bars 37-44, 49-52 and 76-78: Cor anglais 130, 156, 166, 168 back within +-30 ms; 127.5 and
171 not later than c48's +111 ms; dips at 130, 131.5, 134, 168 at or under c48's 2.6, 8.6, 4.0, 2.1 dB; Bassoon 1 253 at
+85 ms or earlier (with cross at +86 it is then a class A join: +0.08 s of lead); the body level of the trimmed notes
(0.45-0.8 s after the beat) within 0.5 dB of c49; the previous pitch's band in the 100 ms before the pitch change not
more than 1 dB above its level 0.3-0.1 s before the moved onset.

### 3. Strings, bars 54-58: leads cut by the 0.45 cap are 50-200 ms late

**Where.** Joins whose lead is limited to 0.45 of the previous note's score length (`LEG_CAP_FRAC` default): Violins II
16, Violas 20 outside their two existing 0.75 windows, Violins I 4, Violoncellos 2.

**What is wrong (measured).** Capped against uncapped joins, median pcX: Violins II Leg Slur +49 ms (13 joins) against
+3 (67); Violins I Leg Slur +74 (3) against +12 (53); Violoncellos Leg Slur +199 (2) against -5 (66); Violas Leg Bow
Change +115 (4) against +49 (8). The error follows the previous note's length: Violins I Leg Slur joins after a note
shorter than 0.35 s are at +74 ms, after 0.35-0.60 s at +56 (cross +50; 24 joins), after 0.60-1.0 s at +12, after
1.0-1.6 s at -45, after more than 1.6 s at -22; Violins II after less than 0.35 s at +102; Violoncellos after 0.35-0.60 s
at +122 against -12 to -17 for longer notes. The sampled transition takes longer than the short notes of bars 54-58
allow at the present cap (pp.79-80: the interval transitions are recorded, and their timing follows velocity, which is
already at the fastest setting).

**Fix.** `build/score_config.py`, `LEG_CAP_FRAC`, entries with the fourth field `"listed"` so that only onsets present
in `build/leg_leads.json` get the higher cap, plus those onsets (seconds, added to existing entries):

- Violins II `[(177.0, 187.0, 0.75, "listed")]`: 177.5 (+154/+78) +0.08; 181.333 (+116/+142) +0.10; 182 (+102/+102)
  +0.10; 186 (+85/+110) +0.08.
- Violins I `[(181.0, 193.0, 0.65, "listed"), (258.0, 259.0, 0.65, "listed")]`: 182 (+74/+54) +0.05; 185.5 (+95/+68)
  +0.07; 186 (+110/+60) +0.06; 192 (+137/+74) +0.07 (0.04 -> 0.11); 258.5 (+211/+88) +0.09.
- Violas, add `(192.0, 196.0, 0.75, "listed")` and `(249.5, 257.5, 0.6, "listed")`: 193.667 (+99/+94) +0.09; 195.333
  (+64/+81) +0.06; 195.667 (+69/+156) +0.07; 250 (+65/+53) +0.05; 257 (+71/+73) +0.07.
- Violoncellos `[(145.0, 146.0, 0.7, "listed"), (68.0, 69.0, 0.5, "listed")]`: 145.5 (+302/+100) +0.10; 68.5
  (+109/+70) +0.07.

Check that `LEG_MIN_GAP_S` does not cut these leads again, and that the previous note still sounds for at least 0.10 s
before each moved onset (**inferred** lower limit for a recognisable short note).

**Pass.** The 16 listed joins within +-60 ms on pcX and +-40 ms on cross; per track, the median pcX of each
previous-note-length group within +-25 ms; the note before each listed join not more than 2 dB lower in its own band.

### 4. Level dips of 6-10 dB lasting 120-350 ms at 58 joins, 13 of them on Oboe 1; many lie outside the time their fill covers

**Where.** Oboe 1 bars 19-20, 45, 58-60, 81-82; Flute 1 bar 42; Cor anglais bars 33 and 43; Horn 1 bar 60; Violins II
bars 21-28 and 75; Violoncellos bars 73 and 76.

**What is wrong (measured).** 40 ms RMS of each stem; reference = the lower of the previous note (0.35-0.05 s before the
moved onset) and the new note's body (0.45-0.75 s after the beat); search from 0.05 s before the moved onset to 0.35 s
after the beat, limited to the note. 58 of 675 measurable joins dip 6 dB or more and stay more than 3 dB under the
reference for 120 ms or longer: Oboe 1 13 of 32, Violins II 8 of 114, Violoncellos 8 of 105, Flute 1 7 of 52, Cor
anglais 4 of 29, Violins I 4 of 86, eight other tracks 1 or 2 each. By class: 25 ok, 19 B, 6 A, 5 var, 3 C, so about a
quarter of the class B joins of Finding 1 are explained by such a dip. The minimum lies before the beat at 16 joins and
150 ms or more after it at 14. A plain-number entry in `build/early_fills.json` is full only 50 ms after the beat and a
dict entry with `hold_s` 0.1 falls from +100 ms, so both kinds miss those dips. On Flute 1, Oboe 1 and Cor anglais a
40 ms window also reads vibrato (the reason `tools/auto_fills.py` uses 200 ms and a 4 dB threshold there since c17), so
I repeated the measurement with 200 ms: Oboe 1 has 10 joins at 4 dB or more and 5 at 5 dB or more, Flute 1 7 and 2, Cor
anglais 5 and 4. The fixes below list only wind joins that both windows show; Oboe 1 44, 56, 59, 145.5 and 269 and
Flute 1 190 and 195.5 read 6-10 dB at 40 ms but 3.1-4.3 dB at 200 ms and are left alone.

**Fix.** Data only, in `build/early_fills.json`, dict entries `{"db", "pre_s", "hold_s"}`: `pre_s` places the full fill
that long before the beat, `hold_s` holds it that long after. Amounts are **inferred**; the times are measured.
Notation: onset (bar; old>new; dip at 40 ms / at 200 ms; time more than 3 dB under, relative to the beat; present
entry) new entry. Do this after the leads of Finding 1 are settled, and where a lead changes, change `pre_s` by the same
amount.

- Oboe 1 140 (b45; 68>73; 10.2 / 5.9 dB; -97..+98 ms; 4.2 plain) `{"db": 6, "pre_s": 0.10, "hold_s": 0.10}`.
- Oboe 1 199 (b59; 73>70; 10.3 / 6.6; -62..+283; none) `{"db": 6, "pre_s": 0.06, "hold_s": 0.28}`; 200 (b60; 70>72;
  6.3 / 5.2; -27..+148; `{2.9, 0, 0.28}`) db 2.9 -> 5.
- Oboe 1 55.5 (b19; 73>72; 7.3 / 4.9; -75..+85; 7 plain) `{"db": 7, "pre_s": 0.09, "hold_s": 0.09}`.
- Oboe 1 193.5 (b58; 80>78; 8.8 / 7.7; -28..+317; none), 57 (b20; 7.6 / 4.8) and 269.5 (b81; 7.3 / 4.9) are class A:
  change the lead first, measure again, then for 193.5 `{"db": 5, "pre_s": 0.03, "hold_s": 0.30}` if the dip remains.
  271 (b82; 70>68; 9.9 / 6.0; -68..+97; `{0.2, 0, 0.22}`) varies between renders: measure after the rebuild, then
  `{"db": 5, "pre_s": 0.08, "hold_s": 0.10}`.
- Flute 1 131.5 (b42; 75>77; 8.2 / 6.0; -27..+228; `{2.7, 0, 0.2}`) db 2.7 -> 5. Flute 1 129 (b42; 77>78; 6.9 / 5.7;
  -135..+275; none) has a trimmed target: Finding 2 first.
- Cor anglais 97 (b33; 60>59; 7.0 / 5.8; -7..+263; `{1.1, 0, 0.25}`) db 1.1 -> 4. Cor anglais 132 (b43; 65>63; 8.2 /
  6.8; -103..+247; `{4.4, 0, 0.21}`), 134 and 131.5 (dip entirely before the beat, -132..-7 ms, under a fill that
  starts at the beat) have trimmed neighbours: Finding 2 first, then 132 `{"db": 6, "pre_s": 0.08, "hold_s": 0.25}`
  and 131.5 `pre_s` 0 -> 0.10 if they remain.
- Horn 1 201 (b60; 63>65; lead 200 ms; 9.2 / 5.7; -250..-15; `{3.9, 0, 0.15}`): the dip is over before the fill
  starts: `{"db": 4, "pre_s": 0.17, "hold_s": 0.05}`.
- Violins II (40 ms only): 67.5 (b23; 68>72; 9.3 dB; -100..+95; none) `{"db": 5, "pre_s": 0.08, "hold_s": 0.10}`;
  80 (b27; 72>77; 8.5; -123..+182; `{5.0, 0, 0.22}`) `pre_s` 0 -> 0.10; 82 (b28; 77>82; 7.1; -245..+215; none)
  `{"db": 4, "pre_s": 0.17, "hold_s": 0.20}`; 251.5 (b75; 68>72; 7.4; -184..+151; none)
  `{"db": 4, "pre_s": 0.10, "hold_s": 0.18}`; 60 (b21; 64>65; 6.8; -83..+147; 2.4 plain)
  `{"db": 4, "pre_s": 0.06, "hold_s": 0.15}`.
- Violins I 80 (b27; 72>77; 7.7; -138..+22; `{2.0, 0, 0.2}`) `{"db": 4.5, "pre_s": 0.10, "hold_s": 0.05}`.
- Violoncellos 246 (b73; 56>60; lead 370 ms; 8.6; -184..+306; `{3.0, 0.12, 0.2}`) db 3 -> 5, `hold_s` 0.2 -> 0.30;
  255 (b76; 56>61; 7.4; -349..+126; `{1.4, 0.22, 0.35}`) db 1.4 -> 4.
- Leave: Violoncellos 140 (7.4 dB under a fill of 8 dB that already covers it), Violas 84 (the same under 4 dB), Double
  basses 186 (33>34; 10.8 dB at +245 ms; **inferred**: two pitches 3 Hz apart beating during the overlap, not a level
  dip), Violoncellos 82 (minimum before its moved onset; it belongs to the join at 81, which gets a shorter lead).

After the first full c50 render, run `tools/auto_fills.py` without `--write` and compare its plan with this list (I did
not run it); Horn 4, Bassoon 2, the Double basses and Violas div are not on its track list.

**Pass.** Each listed join under 4 dB (200 ms window on Flute 1, Oboe 1, Cor anglais; 40 ms elsewhere) or under 120 ms
below -3 dB; no peak more than 2 dB above the louder of the two notes' bodies (the tool's own overshoot rule); pcX of
the class B joins among them under +60 ms.

### 5. What the rebuild is likely to change, the 43 joins that vary between renders, and three small rows

**Where.** All legato tracks; Clarinet 2 bars 58-59 and 73-75; Horn 4 bar 81.

**What to expect (measured on c49's own rebuilds).** c49 fully rebuilt Oboe 1 and Trombone 1 with unchanged join data.
Of Oboe 1's 31 unchanged joins, 29 moved by a median of -8 ms and two moved far: 269 (75, 75, -1 ms in c47/c48/c49) and
271 (37, 37, -23). One of Trombone 1's four moved: 217.5 (-73, -73, -38). No Oboe 1 dip changed by more than 1.1 dB. A
read-only comparison of the instrument state stored in the project file with the build's job files (my own decode, not
Movement I's `state_guard.py`) found 0 of 32 tracks stale by the envelope-attack criterion; the fields that differ are
last-controller values, a pitch-bend range that differs by rounding, and runtime fields, and I could not establish
whether any of them affects playback. Expectation (**inferred**): most joins move by less than 10 ms and about one in
fifteen by 35-80 ms. If a track's median moves by more than 20 ms, its state was stale: derive that track's changes
from the new measurement and do not apply the Finding 1 list to it.

**What is wrong (measured).** 43 joins differ by 25 ms or more between c47, c48 and c49. Six are caused by data
(Cor anglais 130, 156, 166, 168 and Bassoon 1 253: Finding 2; Oboe 1 142.5: 196, 124, 145). The others have unchanged
data and take one of two values: Violins I 77, 77.5 (-59, +51, -59), 86, 177, 195.5 (-22, -22, +85), 196, 200
(-72, +32, -72), 262 (+2, +101, +101), 266; Violins II 77.5 (-39, +68, -36), 84, 85 (+5, +128, +6), 146
(-1, +85, -1), 152 (+247, +147, +128), 242, 262 (-8, -8, +93); Violas 72, 115.333, 192, 194, 243.5, 257.5, 258
(+131, +32, +128); Violoncellos 68, 74, 164 (+19, +144, +144), 201, 219 (-47, +66, -47), 240.5, 249; Violoncellos div
52 (-83, +8, +8), 63, 63.5; Violas div 283. Many deviate in c48 only, the render for which CHANGES.md reports state
drift on unchanged data. **Fix:** no per-onset lead for these until two range renders after the rebuild agree within
25 ms; then classify them as in Finding 1.

**Small rows (measured).**

- Clarinet 2: six of its seven joins sit at pcX +36..+52 and cross +28..+60 ms with the row lead of 30 ms (194, 195,
  196, 246, 248, 252), identical in three renders; 244 (lead 150 ms) is at +37/-54. Fix: `LEG_LEAD_S["Clarinet 2"]`
  0.03 -> 0.07 in `build/score_config.py` and `leg_leads.json` "244" 0.12 -> 0.08.
- Horn 4 268 (b81, the ff cadence; 56>55): lead 0 ms, +110/+170 ms, and the stem is more than 3 dB under the note's
  body from +112 to +347 ms (dip 6.7 dB). The keyswitch to Leg Slur MAX is at 267.94 and the note before it (265,
  3.04 qn long) is on another row, so 268 is the first note on the legato row and gets neither a lead nor a sampled
  transition. Fix: put the 265 note on the legato row, so that 268 becomes a join with the row lead of 0.10 s; if the
  row at 265 is deliberate, give 268 an entry of about 0.10 s in `build/entry_leads.json` (**inferred** amount). 289
  (+15/+64; 6.1 dB, +19..+349 ms): measure again afterwards.

**Pass.** Clarinet 2's seven joins within +-30 ms on pcX and cross; Horn 4 268 within +-60 ms with no dip of 6 dB;
`tools/state_check.py` against c49 and c48 after every render, as ONE_TIME requires.

### 6. Patch question (inferred; nothing here is for c50)

- Violas 111 and 189 (65>61, triplets of bars 37 and 57): the lead already uses 0.75 of a 0.32-0.36 s note and the
  joins are still +84/+51 and +102/+69 ms late (measured). A transition that does not fit the note cannot be fitted by
  a lead. Candidates: the Legato Slur Repetition / Leg Runs patches (pp.80, 101; MANUAL-GAPS #2) for the triplet
  figures of bars 37-40 and 57-58, tested on a range render against the present Leg Slur row.
- Slower legato velocity (60-75) on cantabile string lines (MANUAL-GAPS #6, p.144) lengthens every transition, so it
  can only be tried together with a full lead refit of that track; not before the c50 refit has been measured.
- A dedicated Leg Slur + Port LITE track per string section (template plan item 6) stays the c51 test. The sul tasto
  fallback for Violins II bars 37-40 (Sus MAX with CC1 at 0) is still untried (c49 open item).
- Violin I solo, bars 17-22: no patch change is indicated. 8 of 9 joins are within +-26 ms, the median dip is 1.4 dB
  and none reaches 6 dB (measured).

## Measured and passed (no finding)

- No two notes with the same onset on any legato row and never three notes sounding at once; overlap at the joins
  median 40-49 ms (minimum 33-38, maximum 48-90), as p.99 requires for a slur.
- Keyswitch before the next note: winds and brass 28-113 ms minimum (medians 67-135), strings 20-22 ms minimum
  (median 33-34); no note measured on a wrong row.
- Join velocities: winds 88-104, horns 82-96, Trombone 1 112-124, strings median 124, Violin I solo 72-80.
- Repeatability of a join across c47, c48, c49: median range 0-1 ms on every track with more than 3 joins.
- Trombone 1's quotation (bars 63-64): 213 -5/-20, 215 -35/-32, 215.5 -13/-10 ms; median dip 1.7 dB. Horn 2 within
  +-30 ms except 252 (class B); Horn 3 within +-53; Horns 1-2 a2 -15, -37, -18; Clarinet 1 17 of 20 within +-60.
- Re-bows, coarse check only: master dip at re-bow points median 2.3 dB, 90th percentile 4.4; opening chord (Violins I
  at 2.4 and 4.6) 2.7 and 2.8 dB on the master; Violoncellos div pedal re-bows 275.5-284 1.8-2.6 dB on the stem.
- Not re-measured this cycle (c49's checks in `cycles/c49/CHANGES.md` and `cycles/c49/reports/A.md` stand): tenutos of
  bars 61-62, the Violas' portato eighths, tremolo joins, pizzicato, sul tasto, mutes, harp, timpani, Trombone 1's
  accent spectrum, breath marks and ties.

**Do not touch:** the leads of class B and class D joins; per-onset leads of the 43 render-variable joins; the leads of
Violin I solo, Horn 2, Horn 3, Trombone 1, Horns 1-2 a2 and Clarinet 1; Trombone 1 217.5 (no compensation before the
rebuild is measured); the 0.25 qn ramp of negative pitch trims; legato overlaps, row choices and `KS_LEAD`; the celli
CC1 vibrato macro; the Violas' Detache levels, their reset at 152.06 and their nine entry leads; Oboe 1 Main 0.24 with
B's trims at 42-45; the tenuto gaps and breaths of bars 61-62; tremolo joins 61-64; pizzicato rows and leads 37-44;
Trombone 1's accent data; the re-bow points and fills of the opening chord, bar 66 and the final chord,
`rebow_moves.json`, the 4.1 s pedal fills; CC15 mute placement; harp rolls; timpani rows; the fp chain.
