# Cycle 4, critic C: holistic comparison (on the cycle 3 render)

Compared: c03 master and stems, c00 master, and the Dvorak 9/i Columbia reference. There is no render five cycles back (c-2), so c00 is the only earlier point. Scripts and outputs: `/private/tmp/claude-501/mockup-loop/c04-C/` (`bright.py`, `low.py`, `aw.py`, `width.py`, `vib.py`, `shape.py`, `b65.py`).

What c00 -> c03 fixed (measured): LRA 20.0 -> 24.0 LU (reference 21.8); 63 Hz band +14.1 -> +5.4 dB re 1 kHz; brightness now rises with level like a real orchestra (slope of 2-6 kHz / 0.2-1 kHz energy against frame level: c00 -0.01 dB/dB, c03 +0.31, reference +0.27); the stereo field went from almost uncorrelated (median L/R correlation 0.10) to coherent (0.76). The soft music (bars 1-52, 65-92) now sits 15-25 dB under the climaxes, as the score asks.

What still sounds made by a machine, in order of how much a listener would notice it:

## 1. At both ff summits the tune is carried by single woodwinds; the string sections sit under them (measured; agrees with B #1)

Where: bars 61-62 (Largamente, ff, "molto sostenuto") and 79-80 (second ff). Vln I, Vln II, Oboe 1, Clarinet 1, Flute 1.

Evidence (A-weighted stem levels, so the bass instruments are not over-counted; `aw.py`):
- bar 61: Oboe 1 -33.8, Vln I -34.6, Vln II -38.0
- bar 62: Oboe 1 -35.1, Clarinet 1 -35.8, Oboe 2 -36.7, Vln I -36.9
- bar 79: Flute 1 -33.5, Oboe 2 -34.4, Clarinet 1 -37.0, Vln I -37.2
- bar 80: Clarinet 1 -33.9, Oboe 2 -34.6, Oboe 1 -36.2, Vln I -37.0

Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt`, lines 1980-1991): in forte, "Violins I = 2 Flutes = 1 Oboe + 1 Clarinet", so the first violins should be about 3 dB above any single woodwind. They are 1-4 dB below. The cause is in `build/mix.json`: the strings have negative ff trims (Vln I -1.5, Vln II -3) while Oboe 1/2 and Cor anglais have +3 at ff. A conductor hears a wind band on top of a thin string section at the two moments the movement builds toward.

Fix (`build/mix.json`, `dyn_trim_db.ff`): Violins I -1.5 -> +1.5, Violins II -3 -> 0, Oboe 1 and Oboe 2 +3 -> 0, Clarinet 1 and 2 -1 -> -3. Leave `f` as it is. Target: A-weighted Vln I at least 3 dB above the loudest single woodwind in bars 61, 62, 79, 80, with the master level within 1 dB of c03 there. Check with `aw.py`.

## 2. Woodwind, brass and harp stems are almost mono, reverb included, so every solo sounds like a dry point source pasted into the hall (measured; effect inferred)

Where: all wind, horn, low brass, timpani and harp tracks, and so every solo: Horn 1 (bars 7-14, 67-70), Oboe 1 (15-20), bass clarinet (31-36), Flute 1 (37-44), cor anglais (41-52).

Evidence (`width.py`, `bright.py`; median L/R correlation of 0.4 s frames within 30 dB of each stem's peak):
- winds 0.87-0.95, horns 0.92-0.94, low brass 0.90-0.93, harp 0.95; strings 0.69-0.80
- master: correlation 0.76 and side/mid -8.2 dB; reference: 0.61 and -5.8 dB

The hall reverb lives inside each Opus instance (fx:0), so the REAPER stereo width of the track (`groups.*.width`: wind 0.3, horn 0.3, lowbrass 0.3, harp 0.3, timp 0.4) narrows the reverb tail along with the dry sound. In a hall the tail of an oboe solo reaches the listener from every side; here it comes from the same spot as the oboe. This works against Dan's blend rule ("one ensemble in one room"). HO's Main mic is recorded with the players in their seats, so a wider width keeps the seat while it opens the room.

Fix (`build/mix.json`, `groups`; apply with `build_reaper.py --mix-only`): wind width 0.3 -> 0.7, horn 0.3 -> 0.8, lowbrass 0.3 -> 0.7, harp 0.3 -> 0.7 (also "Harp harmonics"), timp 0.4 -> 0.7, Double basses track width 0.4 -> 0.6. Keep every `seat`. Target: wind and brass stems at correlation 0.65-0.80, master correlation 0.60-0.68 and side/mid about -6 dB. Each stem's R/L balance (now within about ±6.5 dB) should change by less than 1 dB. If that is not enough, the next step is to pan the Opus Close and Main channels to the seat and leave the fx:0 return at the centre and full width, with the REAPER track at pan 0 and width 1.

## 3. The woodwind solos are played almost without vibrato, and vibrato never changes within a phrase (measured from data and audio; effect inferred)

Where: Oboe 1 (bars 15-20, 45-50, 59-62), cor anglais (41-52), Flute 1 (37-44, 57-62, 75-81); also the string espressivo lines.

Evidence:
- `score_to_parts.py` line 769 sets `cc1 = 64 + (cc11 - 46) * 0.3`, clamped 40-100. In practice CC1 sits at 63-77 through every solo (`shape.py`: Horn 1 66-72, Oboe 1 65-69, Vln I 63-77, Flute 1 64-67, cor anglais 66-70).
- The Leg Slur MAX and Sus MAX patches crossfade a "[[[Non Vib]]]" layer and a "[[[Sus Vib]]]" layer by CC1 (read from `OB Leg Slur MAX.oib` and `OB KS Master.oib`; HO manual, user manual text lines 1674-1687 and 1707). At CC1 ~66 the mix sits near the middle of the two layers.
- Measured pitch modulation (peak-to-peak cents) after the first 0.5 s of notes of 1.4 s or longer (`vib.py`, f0 tracked on the stems): Oboe 1 1-16 cents (median about 7), cor anglais 3-45 (median about 12), Flute 1 9-31, clarinets 1-8 (correct: clarinets play without vibrato). An orchestral oboe or cor anglais in an espressivo adagio solo uses clearly audible vibrato of roughly 20-40 cents peak-to-peak (inferred, standard practice), which grows into long notes and peaks at the top of the phrase.

This is the main reason the solos sound like samples: the same mid-vibrato colour on every note, at every point in the phrase.

Fix (`tools/score_to_parts.py`, replace the CC1 line after `cc11 = sample(...)`):
- Melody lines (the same spans as the solo/cantabile/espr. CC11 boost, `boost_spans`) in Flute, Oboe, Cor anglais, Bassoon and the strings: target CC1 = 100 (strings 95). On notes of 0.8 s or longer, start at target - 35 at the onset and reach the target at 40% of the note (the delayed-vibrato onset players use); add +10 (cap 120) on the highest note of each slur.
- Accompaniment at pp or softer: CC1 35-45. Flautando and sul tasto (Vln II bars 37-40): CC1 20 or lower. Tutti at f and louder: CC1 90-100.
- Horns, trombones, tuba and clarinets: keep the present formula. Horn vibrato is not idiomatic here, and the clarinets already use Non Vib.
- Target: after re-render, `vib.py` shows 20-40 cents peak-to-peak on Oboe 1 / cor anglais / Flute 1 long notes after 0.5 s, and less than half of that in the first 0.2 s.

## 4. Low end: too much 40-90 Hz, too little 90-180 Hz, so the bass booms but has little body (measured; agrees with B #2; EQ effect inferred)

Evidence (`low.py`, `bright.py`; band energy relative to the 200-1000 Hz band):
- 40-90 Hz: master -7.7 dB in bars 61-62, -9.2 in 79-80, -10.6 in 23-28; reference loudest passages -24.7. Across all loud frames: c03 -13 to -23, reference -22 to -28.
- 90-180 Hz: master -11.4 (bars 61-62); reference -5.1. Long-term 125 Hz band: mix +3.3, reference +7.0.
- Source: in every passage tested, the double basses alone make the 40-90 Hz band (within 0.1 dB of the master band level), and their own 40-90 Hz energy is 8.7-9.7 dB above their 200-1000 Hz. Contrabassoon and tuba add about 1 dB at the climaxes.

The old Columbia recording may be a little bass-light, but a 15 dB gap at 40-90 Hz together with a 4-6 dB shortfall at 90-180 Hz is a tone problem, not a level problem. Turning the basses down would lose the bass line, so the fix is EQ.

Fix: add an `eq` key to `build/mix.json` tracks and have `tools/build_reaper.py` insert ReaEQ after the Opus instance (`TrackFX_AddByName(tr, "ReaEQ", false, -1)`). Set bands with `TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPEn", ...)`, and set frequency and gain with `TrackFX_SetParamNormalized`, reading them back with `TrackFX_GetFormattedParamValue` to confirm.
- Double basses: low shelf 75 Hz -6 dB; bell 140 Hz +3 dB, Q 1.0.
- Contrabassoon and Tuba: low shelf 70 Hz -4 dB.
- Target: long-term 63 Hz band at or below 0 dB re 1 kHz (now +5.4); 125 Hz at +5 or above; 40-90 / 200-1000 Hz in bars 61-62 at -15 dB or lower.
- Optional, after that: high shelf +2 dB above 4 kHz on the string tracks. The 4 and 8 kHz bands are 2.8 and 3.2 dB under the reference, and at the loudest level the 2-6 kHz ratio is 2.6 dB under it.

## 5. Bar 65 (Tempo I, the return): Vln II swells 14 dB through a held pp note, then the printed decrescendo sounds like a hole (measured)

Where: qn 220-226. Vln II, Vla and Vc in unison, pp, slur, then a decrescendo from qn 223 (`mockup-events.tsv`). Score page 5, bars 65-66. Bar 66 is at -50.7 dB, the quietest bar in the piece outside the first and last bars and the bar-35/36 and bar-84 lows, at the moment the opening music comes back.

Evidence (`b65.py`, stem dB per 0.5 qn): Vln II goes -59.3 (220.0), -49.9, -48.6, -47.0, -46.0, -45.3 (222.5), -49.9 (223.0), -52.5 (224.0), while its CC11 is flat at 34 from 220 to 223. The 220 note re-attacks after a 0.05 qn gap (separate slurs) on Leg Slur MAX's sustain layer, and the soft sample keeps rising for about 2.5 qn. The merged same-pitch note at 223 then takes a 14-CC notch (20 at its lowest), so the master falls -44.5 -> -48.7 -> -51.2 dB from qn 222.5 to 224. The printed shape (flat pp, then down) is heard as rise, drop, fade. Violas and celli in the same unison sit 10-12 dB under Vln II (-57 to -62 against -46 to -49), so the line sounds like one desk of second violins instead of three sections.

Fix (`tools/score_to_parts.py`):
- Widen the c02 "bloom" contour (the `contour()` branch for `Sus MAX`) to string notes on Leg Slur MAX / Leg BC MAX that re-attack after a gap at p or softer and last 2 qn or more. Put the compensation in `vol_db` (level only, no timbre change): 0 dB at the onset, falling linearly to -4.5 dB at 2 qn, then held.
- Same-pitch bow-change notch at CC11 40 or below: 14 -> 8.
- `build/roles.json`: Violins II `[220, 226, -4]`. Also `note_trims.json` Violas `{220: +3}`.
- Target: Vln II varies by at most 2 dB from 220.5 to 223; the master moves by at most 2 dB across qn 222.5-223.5; Vla and Vc within 5 dB of Vln II.

## 6. The two tutti breath marks take no time, so the arrivals of the climaxes are on the grid (data measured; effect inferred)

Where: qn 204 (bar 61 downbeat, Largamente; breath printed in Fl1, Ob1, Cl1, Cl2, BCl, Bn1, Bn2) and qn 268 (bar 80, beat 4; Fl1, Ob1, Cl1, Cl2, BCl, Bn2). Also Hn1/Hn2/Bn1 at 265.

Evidence: the breath rule in `score_to_parts.py` (around line 497) only shortens the note before the breath. The tempo map (`parts.json` "tempo", 303 points) has no extra time at either point; the time between the last note before and the first note after equals the printed tempo exactly. An orchestra takes a short breath before a Largamente downbeat after an allargando. The BRIEF names "breath before a breath mark" as an allowed liberty, and c03 deferred this (C4 caesuras).

Fix (`tools/score_to_parts.py`, after the RAMP_SPANS tempo build): add `CAESURA = {204.0: 0.22, 268.0: 0.15}` (seconds). For each one, replace the tempo of the 0.25 qn before the breath with `bpm' = 15 / (15 / bpm + extra_s)`. Write that as one tempo point at q - 0.25 and restore the ramp value at q. Notes held through the breath (strings, brass in 203-204) simply last longer. The winds already stop for the breath. Print the new span lengths, as the C4 code does. Target: +0.22 s and +0.15 s exactly, with no other tempo change.

Do not touch: CC11 dynamic-layer mapping and the ff/fff values (brightness now rises with level like the reference); the hairpin parser and level holds; the legato and entry lead tables; the same-pitch merge (only the soft notch depth above); the tempo ramps; the timpani soft-roll -6 dB and settle; the one-hall reverb scheme (only the widths above change); the 1x render.
