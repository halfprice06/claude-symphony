# Cycle 21, critic C: blend and space (lens C1), on the c20 render and its delivered mp3

Measured on `cycles/c20/render/` (31 stems, returns 91-94, master), the delivered `cycles/c20/scherzo-mockup-c20.mp3` (decoded at 48 kHz and aligned to the master: +239 samples), `cycles/c20/build_render/parts.json` and `mix.json`, and earlier stems (c17, c18) where named. Delivery variants were simulated by running a scratch copy of `tools/deliver_master.py` on the c20 master. The copy differs only in an environment switch for the limiter release. The unmodified run reproduced the c20 mp3 exactly: -14.1 LUFS, LRA 12.3, limiter 5.5 / 3.8 / 2.7 dB. Levels are mean-square dB of both channels. "L-R" is left minus right level (positive = left). "Correlation" is L/R correlation at 300 Hz-8 kHz. "Side/mid" is the side level against the mid level. Positions are score qn; bar b starts at qn 3(b-1). Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c21-C/` (deleted).

## Manual notes

There is no MANUAL-READING row for cycle 21. I chose group L2 (May 2021 HO manual PDF pp. 219-223, read in full; pp. 220-221 also as images) because this cycle's question is whether the -14 LUFS delivery changes the hall. MANUAL-GAPS.md was read.

| manual (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.219: Algoverb, an algorithmic stereo insert (pre-delay, size, decay, density, early/late, stereo, mix) | Nothing. The hall is four EW Spaces II returns. | Yes. Not needed. |
| p.220: the convolution Reverb insert: Send Mono, IR choice, IR envelope, Bandpass low/high cut, Width 0-200 %, Wet / Dry | `mix.json` `reverb` (Opus hall, inert because `opus_reverb_off` is true) and the Spaces II returns (`returns`: 180 Hz high-pass, 2.67 kHz -6.7 dB, IR envelope) | Yes. The returns' filters do the Bandpass job. Width is not needed: the wind problem in finding 3 is a dry stage, not a narrow tail. |
| p.221: IR envelope, Simple (one Decay slider) or Full (start, end, fade-in, fade-out and curves) | `irSetup` envelopeMode 2, endPos / decayLength 0.5 on every return | On the master, yes: G.P. after the fff falls 18.3 dB at +0.3 s, 20 dB in 0.33 s, RT60 1.38 s. On the delivered mp3 the limiter's release lifts that tail by 6 dB (finding 1), which gives back part of what the envelope took out. |
| p.222: the mic mix sets "small and dry" against "large and wet". The room is "heard as long as the samples are playing (including the release trail samples)". Main is the usual single mic for its versatility, and Close or Mid can be right in some cases. | How much room each family carries on its own notes: woodwinds Close-led (Main 3.4-20.6 dB under), horns 2-4 Main-led, Horn 1 Close-led since c17, Horn 3 Main-led but "Mono From Left" since c18, DIV tracks Close only | Partly. The woodwinds, Horn 1, Horn 3 and Violas div carry less room or width than the families around them (findings 2-4). |
| pp.222-223: render each mic position in its own pass (or to separate outputs) and mix the mic tracks afterwards, "to create a wetter or drier mix" | Choosing the woodwind Main level without a series of full renders | Not used. Proposed as the test method in finding 2. |

MANUAL-GAPS #13 (Mid instead of Close or Main on woodwinds and horns) is still untested. It is the test in finding 4.

## Hall, tone and low end on c20 (measured; no change wanted except finding 1)

- **Hall, master.** G.P. after the fff (cut-off 242.75 s, qn 1015.3): drop 18.3 / 30.5 / 46.5 dB at +0.3 / +0.6 / +1.0 s, 20 dB fall 0.33 s. This is the same as c19 and inside Dan's c05 limit.
- **Detache and Sus MAX substitutions sit in the same space.**
  - Violins I's Detache pair notes against their staccato neighbours (first 100 ms, notes pooled per passage):
    - bars 101-120: L-R +4.6 against +6.2 (Stac RRx14) and +7.4 (Staccatissimo); correlation 0.41 against 0.29-0.33; 2-5 kHz over 250 Hz-1 kHz -1.3 against -1.8 / -3.0 dB;
    - bars 301-339: +4.8 against +6.2 / +7.1; 0.41 against 0.26-0.33; tilt -2.8 against -2.9 / +0.7.
  - The rows of this one instance already spread over that range: Sus Marc LITE sits at +6.5, Spiccato at +6.6. A 1.4-1.6 dB smaller L-R is a seat shift of about 0.05, so a listener does not hear the pairs move.
- **The louder delivery does not change the tone.** Band shares, master against mp3:
  - tutti 101-120: 2-6 kHz -11.3 -> -10.6, 6-20 kHz -31.5 -> -30.1, 250-500 Hz -5.3 -> -4.9, 100-250 Hz -8.8 -> -9.0 dB;
  - coda 329-339: 2-6 kHz -9.2 -> -8.7, 100-250 Hz -10.3 -> -10.2 dB.
  - These moves come from `master_eq` (167 Hz -1.6, 1.18 kHz -1.9, 8 kHz +0.8), not from the limiter, so the mp3 is not harsher than the master.
- **Low end.**
  - First tutti, 250-500 Hz share -5.3 dB (master) against -5.95 to -6.5 in the references. That is 0.7-1.2 dB more, carried by Horn 3 (17.5 % of the band), violas 12.8 %, celli 11.5 %, Violins II 10.9 %, Clarinet 2 8.3 %.
  - 100-250 Hz: -8.8 / -8.8 / -10.3 dB in 101-120 / 301-320 / 329-339, against Dvořák's loudest tenth -6.6 and Brahms -7.6 / -8.8. The summit is the lightest at 100-250 Hz.
  - Basses' div. pizz. octaves (253-268): 100-250 -9.6, 250-500 -9.0 dB. No build-up.
  - Leave the low end as it is unless Dan calls the summit thin.
- **Standing checks that pass:**
  - con sordino: Violins II 504-552 2-5 kHz over 250 Hz-1 kHz -12.2 dB, open -3.5 / -5.0;
  - link handover: borrowed harmonic -49.2 dB, L-R +5.1; harp harmonics -47.5 dB, L-R +4.0;
  - last G sharp: Violins I -50.8 dB, L-R +5.8; copy -51.4, +5.2;
  - loop pulsing on the last G sharp, Violins I plus copy at 1092-1124: autocorrelation at 3.95 s of 700-1000 Hz -0.06, 1.5-5 kHz +0.13, centroid -0.03 (no pulse);
  - trumpets and trombones in the tutti: correlation 0.87 / 0.80, L-R -3.6 / -4.0;
  - S3: the returns fall smoothly through qn 360 and 828 (largest 10 ms steps 2-6 dB, inside the returns' own frame scatter).

## Findings, ranked by what a listener would hear

### 1. On the delivered mp3 the G.P. after the fff rings 6 dB louder than on the master: the limiter releases into the silence (bar 339-340, qn 1015.3-1020) (measured, simulated)

Where: the cut-off of the summit chord at qn 1015.3 (242.75 s) and the G.P. of bar 340. The delivered file only, not the mix.

What is wrong: the delivery limiter (`alimiter` attack 5 ms, release 80 ms) takes 5.5 dB at the summit. When the chord stops, it releases within about 0.1 s, so the hall tail plays 6 dB nearer the chord's level than it does on the master. The movement's one printed silence after its loudest moment therefore sounds wetter on the file Dan hears than on the file the loop measures. Every hall reading since c18 (18.4 dB, 0.33 s) was taken on the master.

Evidence:
- Delivery gain (mp3 against master, 10 ms frames), relative to its value 0.2 s before the cut-off: +3.1 dB at the cut-off, +5.0 at +0.05 s, +6.0 at +0.1 s, +6.4 at +0.3 s, +7.0 at +0.8 s.
- G.P. drop at +0.3 / +0.6 / +1.0 s: master 18.3 / 30.5 / 46.5 dB; mp3 12.0-12.2 / 23.8 / 45.4 dB. The 20 dB fall takes 0.33 s on the master and 0.47 s on the mp3. Dan's limits are a drop of at least 13 dB at +0.3 s (the mp3 now misses it by about 1 dB) and a 20 dB fall within 0.50 s (the mp3 is 0.03 s inside it). The master meets both by a wide margin.
- The same mechanism, smaller, at the other loud cut-offs (drop at +0.3 s, master -> mp3):
  - bar 72 chord into the F major pp: 11.5 -> 8.1 dB;
  - sub. p at bar 121: 10.3 -> 7.8 dB;
  - 320 into 321: 8.9 -> 6.9 dB.
- Inside the tuttis the 80 ms release also refills the gaps between strokes. The in-bar range (p95 - p10 of 10 ms frames) falls from 5.7 to 3.9-4.0 dB in 105-120 and from 5.6 to 4.1 in 329-339. Bar 105 goes from 8.1 to 3.1. The soft theme (13-28: 9.9 / 9.9) and the trio (5.1 / 5.2) are untouched.

Fix: one delivery-only ride row (no track envelope) in `build/score_config.py` `RIDE_TRIMS`:
`[(1015.3, 0.0), (1015.8, -6.0), (1019.4, -6.0), (1019.8, 0.0)]`.
It follows the limiter's release down at the cut-off and is back at 0 before the bar 341 entries and their leads.

Simulated with `deliver_master.py` on the c20 master:
- G.P. drop at +0.3 s 18.1 dB (master 18.3), 20 dB fall 0.35 s;
- I -14.1, LRA 12.3, limiter 5.5 / 3.8 / 2.7, p10 -21.7, span 13.9: all unchanged;
- bar 341's first 0.3 s and bars 341-344 identical to c20 (-26.79 / -24.51 dB).

A generic form for other movements would be a `deliver_master.py` option that holds the limiter's gain over listed G.P. and fermata rests. The row is enough here.

Not proposed:
- A slower release (limiter 300 ms, peak compressor 250 ms) made everything worse in simulation: G.P. drop 10.8 dB, sub. p 6.2, LRA 11.3, span 12.7.
- Deeper tutti ride rows (-2 dB on 312-360 and 912-960) gave back only 0.6 dB of in-bar range (3.9 -> 4.5) and cost 0.6 LU of LRA (11.7).
- No row for the sub. p or bar 73. There the tail sits under a new soft entry, and a hold would put a rise into the p.

### 2. The woodwinds still have almost no stage sound of their own: the counterstatement's picture narrows every time the winds call (bars 29-44; Oboe 1's trio solo 185-196; cor anglais, flutes, clarinets throughout) (measured; fix to range-test; c17 #3, never tried)

What is wrong: the mic mix and the returns are unchanged since c13, and so are the numbers c17 found:
- counterstatement on the c20 master: winds' call (qn 84-90, 96-102) correlation 0.88, side/mid -11.3 dB; strings' answer (90.4-96, 102.4-108) 0.42, -4.3 dB; levels equal (-40.0 / -40.4);
- stems: Flute 1 0.94, Oboe 1 1.00, Clarinet 1 0.86, Violins I 0.42;
- Oboe 1's solo (qn 552-588): stem 0.99, side/mid -17.3 dB;
- note ends on the dry stems (drop at +0.15 / +0.25 s after isolated note ends): Flute 1 -26.7 / -36.8, Oboe 1 -25.2 / -34.9, against Violins I -18.4 / -23.9, violas -17.3 / -21.4, Horns 3-4 -14.5..-15.6 / -24.1..-28.5.

The winds are Close-led (Main under Close: Flute 1 -4.7, Flute 2 / Clarinets -3.4, cor anglais -11.6, Oboes -20.6, Bassoons -8.6). They get their room only from R Winds, which the "too wet" cuts lowered. The strings and brass carry a recorded stage on every note, and the winds do not. With the c20 inner-line work (Oboe 1's layer +6 dB), the oboe is now louder but still a dry point in the centre.

Fix: the manual's own method for choosing a mic balance (p.222, "Recording Each Microphone Individually").
- Range pass on Flute 1, Oboe 1, cor anglais, Clarinet 1 and Bassoon 1 over qn 81-110 and 549-590. Render once with `mic_db` Close 0 / Main -150 and once with Close -150 / Main 0, at the same start (begin before every track's last keyswitch before the range; c20's Clarinet 1 test was void for that reason).
- Mix the two stems offline at Main -12, -9, -6 and -3 dB under Close.
- Take the lowest Main level that gives:
  - Oboe 1 stem correlation 0.90 or less in qn 552-588;
  - note-end drop at +0.15 s between -18 and -24 dB;
  - 250-500 Hz share up by less than 1.5 dB;
  - master correlation in the winds' call 0.75 or less (stems summed with the c20 returns; send changes are linear: c07 LEARNINGS).
- Then set `build/mix.json` `mic_db` Main on those tracks, Flute 2 / Oboe 2 / Clarinet 2 / Bassoon 2 like their firsts, and re-fit `gain_db` to each track's c20 K-weighted level.
- Do not raise the wind send or the R Winds fader.
- If the oboe turns thick at every level, try Mid in place of Main (MANUAL-GAPS #13) the same way, or stop.

Pass on the render: G.P. figures unchanged within 1 dB on the master; winds' 20 dB fall at the G.P. 0.30 s or less.

### 3. The violas' upper div. voice is a mono point in the centre, next to a full section with stereo width (bars 209-224, qn 624-672; bars 349-356, qn 1044-1068) (measured; fix as tested on the solo in c13; c17 #4, never tried)

What is wrong: Violas div reads correlation 1.00, side/mid -120 to -126 dB (exactly mono), L-R 0.0, in both passages. The violas beside it read 0.42-0.48 and -4.9 / -5.0 dB. Since c20 deleted the trio role rows, the voice is 2.3 dB under the section (-43.6 / -41.3 dB in 624-672). Dan asked for the inner lines (2026-11-17), and this is one of them: the violas' tenuto thirds under the ff return. Inferred: a mono centre point inside a wide section is easier to mask than a voice with its own spread. The `width` 0.45 and the side shelf on this track do nothing, because the Close-only DIV B signal is identical in both channels.

Fix: `build/mix.json` track "Violas div": `"stereo_double": {"spread": 0.6}` (the key `build_reaper.py` already reads; manual p.141). Raise `gain_db` by the measured loss (the solo lost 2.5 dB at 0.4).

One-track range test on qn 620-672 first. Keep 0.6 if:
- correlation is 0.55-0.90;
- L-R is within 1 dB of 0;
- band levels are within 1 dB of c20 after the gain;
- the mono sum's third-octave spectrum has no notch deeper than 6 dB.

Otherwise use 0.4.

### 4. Horns 1 and 3, the two exposed horns, play as near-point sources since their phase fixes; Horns 2 and 4 keep their stage width (measured; fix to range-test)

Where:
- Horn 1: the call of bars 3-6, the motto tail 357-360, the last G sharp;
- Horn 3: the trio drone 153-168, the tutti countermelody 105-120 / 305-320, and the trio tune recalled in bars 341-344, where Horn 3 is the loudest stem by 1-10 dB.

What is wrong: both fixes for the G sharp 4 anti-phase of the Main pair (c17 Horn 1 Close-led; c18 Horn 3 `channel_map` 2 "Mono From Left") apply to every note, not only to the G sharp.

Horn 3, stem correlation:
- c17: 0.76 / 0.76 / 0.83 in the tutti / drone / recall;
- c18-c20: 0.99-1.00, side/mid -12.2 to -12.5 dB in every passage;
- in the drone it sits beside Horn 4 at 0.82.

Horn 1:
- the call is at 0.98 on the stem (c16 0.82) and 0.92 on the master (c16 0.78; Dvořák's frames 0.47-0.77);
- its note ends fall faster than the other horns': -21.2 / -35.8 dB at +0.15 / +0.25 s, against Horns 3-4 -14.5..-15.6 / -24.1..-28.5;
- so the movement's first solo is the narrowest and driest brass sound in it.

The anti-phase was measured only on G sharp 4 (fundamental -0.72..-0.78) and, weaker, F sharp 4 (-0.35). Every other horn pitch read +0.88..+0.98 (c17). Horn 3 plays G sharp 4 only at qn 1092.

Fix: one-track range passes on Horn 3, qn 450-504, 1017-1035 and 1086-1100 (start before its last keyswitch), with `channel_map` 0:
- (a) Close -6.3 dB and Mid 0 in place of Main (MANUAL-GAPS #13, manual p.138: Mid "at the edge of the stage", a different spacing from the Main tree's outriggers, so the G sharp may not cancel);
- (b) Horn 1's mix (Close -1.4 / Main -5.2).

Keep the first that gives:
- at qn 1092 a 400-430 Hz band correlation of +0.3 or more and a mono loss of 3 dB or less;
- stem correlation 0.70-0.88 and L-R +3..+5 dB in the drone and the recall;
- K-weighted level re-fitted with `gain_db` (Mono From Left had added up to +3.7 dB on some pitches).

If (a) passes, test it on Horn 1 the same way:
- the call (qn 6-18) at stem correlation 0.88 or less;
- the G sharps at qn 0, 432, 708 and 1101-1127 still +0.3 or more at the fundamental;
- the call within 1 dB of its c20 level.

If neither passes, keep the c20 settings and report the fault.

## Do not touch

- The returns, their faders, pans, filters and IR envelopes, and every send. The hall on the master is inside Dan's limits; only the delivery lifts it (finding 1).
- `deliver_master.py`'s limiter and peak-compressor timing: a slower release was worse in every reading.
- The c20 summit ride row and the other ride rows (the G.P. row is added, nothing replaced).
- Violins I's Detache pairs: they sit in the section's space (position within 1.6 dB, tilt within 1.7 dB of the staccato rows).
- The low end: no cut or boost at 100-500 Hz without Dan's word.
- Violins II con sordino lane, the borrowed harmonic and the harp harmonics at the handover, the last G sharp's doubled copy, the Violin I solo's Stereo Double 0.4, the trumpets' mics and seats.
