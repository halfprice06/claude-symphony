# Cycle 07, critic B (balance and levels), on the c06 render

Material: `cycles/c06/render/` (dry stems 01-31, return stems 91-94, `00_Master.wav`), `cycles/c05/render/00_Master.wav` (the only c05 audio left), `cycles/c06/build_render/parts.json` and `mix.json` (what was rendered), `build/roles.json`, `build/mix.json`, `build/score_config.py`, `build/mockup-events.tsv`, `cycles/c06/CHANGES.md`, `loop/ONE_TIME.md`, `loop/ONE_TIME_c07.md`, `loop/RESEARCH-FINDINGS.md` (Parts 2, 5), Rimsky-Korsakov *Principles* PDF p.51.

Method:
- Levels are K-weighted power (BS.1770 K filter on 2048-point spectra every 10 ms, both channels summed), averaged over bars or phrases on the parts.json tempo map. They are not the plain RMS of metrics.md. "X over Y" means X's level minus Y's in the same window.
- I checked that `00_Master.wav` equals the sum of the 31 dry stems and the 4 returns exactly (residual -173 dB). So trial masters (dry sum plus the returns at other gains, or filtered) are exact for any change to the return faders, return EQ or a uniform send change. Per-track send changes can only be estimated per return.
- Cut-off drops: I found 9 places where the dry sum falls at least 12 dB within 0.25 s and stays down (qn 166, 216, 273, 358.5, 394, 755, 862, 1016 (the G.P.), 1128). For each I give the master's fall from the 0.2 s before the cut to +0.1 / +0.3 / +0.6 s after it, as a median over the cuts. The data is the same in c05 and c06 at all of them.
- Each judgement is marked **measured**, **read** (score, data, manual) or **inferred**.

## Manual notes (cycle 7, slot B: group B1, May 2021 HO manual PDF pages 137, 140, 150-151, read in full; MANUAL-GAPS.md read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 137 | Articulations view: each KS Master row has a load button and its own **volume knob** to adjust the loudness of each articulation. | Row-level differences at one CC11: Violins II "Spiccato RRx9" against Violins I "Stac RRx14" (c05/c06 B #1-#2), the clarinets' "Leg Slur Rep", the 1FH "Port Lng" row on Horn 1 (624-664). | **Partly (read).** The pipeline unloads unused rows (`UNLOAD_UNUSED_ROWS`, follows) and balances rows with envelope trims (`ROW_TRIM_DB`, roles) rather than the per-row knob. That works, but only inside the trim's own rules (needs a Leg neighbour). A per-row knob in the Opus state would carry a row offset everywhere the row plays. Not needed for any finding below. |
| 140 | Master channel: **GAIN** sets the instrument's output "without affecting the relative mix of the microphone sub-mixer channels"; PAN keeps the mics' relative panning. | `mix.json` gain_db per track, after the c06 template mic layout (`mic_db`). | **Yes (read).** Gains and the family-EQ make-up are applied after the mic mix, so the template mic ratios stay as built. |
| 150 | Velocity sensitivity curve (default linear, 0). Note velocity selects the dynamic layer as well as loudness: samples are mapped to velocity ranges ("p 1-25, mp 26-45 ..."); velocity "is most often used in short instruments". | Harp (velocity is its only dynamic; CC11 held at 110), timpani, string shorts and pizz. The scherzo's harp plays its pp chords at v40-61 (median 52). DIGEST §10 (M1 c33): Pluck p 1-57, **Thumb p 1-42 / mp 43-70**, and Sus RR alternates the two by round robin. | **No (read + measured).** At v52 every Thumb-pick round robin of a pp chord plays the **mp** layer. The trio's and the Meno mosso's pp chords reach the solo tune's level (finding 2). The curve is linear (follows). |
| 151 | Send CC1/CC11 before the first notes. **CC7 sets a track's ceiling against the others, CC11 shapes the line.** In the Strings and Woodwinds KS Masters CC11 is dynamics and CC1 is vibrato; in the **LITE** string patches CC1 is dynamics plus vibrato and CC11 is loudness. | The pre-roll (CC values and the first keyswitch at score qn -3). Violins I "Sus Marc LITE" (20 notes: theme accents 39-795, hemiola 300-311 and 902-911). | **Yes (read).** The pre-roll sends CC1/CC11/CC70. On the LITE notes CC1 follows CC11 (v84-88 / CC1 90-98 / CC11 88-114 at the hemiola; CC1 55 / CC11 46 at the p accents), so the LITE layer follows the printed dynamic. Balance is set in the volume envelope and roles, not in CC7. That matches the page's split, because CC7 here is kept for the timpani damp. |

## Standing checks (Dan's ears), measured on c06

- **Loop pulsing (item 8): none.** Autocorrelation at 3.95 s of the detrended level / 100-300 Hz band / spectral centroid: Violins I 0-23 +0.01 / -0.02 / +0.03; 1089-1128 -0.13 / -0.17 / -0.08; 420-445 -0.06 / +0.34 / +0.06; celli 605-624 -0.41 / -0.37 / +0.39; celli 1070-1091 -0.23 / -0.49 / -0.22; Horn 1 1110-1128 +0.04 / -0.30 / +0.14; Horn 4 drone 456-504 -0.10 / +0.08 / -0.05; master 1089-1128 -0.32 / +0.18 / -0.02. Nothing reaches +0.5.
- **S1 against the hall (measured).** Master dips at 239 same-pitch eighth pairs whose notes are the same in c05 and c06 (strings, Fl 1, Ob 1, CA, Cl 2, Tpt 1) have a median of 0.6 dB in c05 and 0.7 dB in c06. On trial masters: returns -6 dB 0.9, no returns at all 1.2. On the stems the median is 2.3 dB. **The hall is not what fills the repeated-note gaps on the master; the other sections are.** Cutting the returns will not fix S1, and S1 is no argument against cutting them.
- **S3 (measured, master 50 ms K frames from 0.2 s before).** qn 360: c05 falls 4.2 dB to its trough, c06 3.9 dB. qn 828: c05 7.5 dB, c06 4.7 dB. From 0.4 s after the subito c06 sits 2-5 dB over c05 at both. That comes partly from the wetter returns (finding 1) and partly from the inner voices (finding 3). No step to silence at either.
- **Timpani rolls (priority 5, measured).** Within 1.5 qn of the coda's first ff (qn 996-998.5) the timpani's motive x (f) is -24.4 / -25.5 dB against Violins I -23.8 / -22.2. That is level with the tune, though it is a stroke figure, not a long roll. The bar-339 accented octave (1014) is the loudest stem by 1.1 dB. That is printed (an accented ff stroke into the G.P.), so I leave it.

## Findings, ranked by what a listener would hear

### 1. The template returns are much wetter than c05's hall: the master's tails are 5 dB fuller at +0.1-0.3 s, and the reverb is as loud as the direct sound below 300 Hz (measured; Dan's standing "too wet, mushy")

**Measured: cut-off drops** (median over the 9 cuts; G.P. bar 340 at qn 1016 separately):

| master | +0.1 s | +0.3 s | +0.6 s | G.P. +0.1 / +0.3 / +0.6 |
|---|---|---|---|---|
| c05 (Opus hall, fx 0.095, 160 Hz low cut) | 15.3 | 19.6 | 20.4 | 14.7 / 24.6 / 35.5 |
| **c06 as rendered** | **9.6** | **14.6** | **17.8** | 9.6 / 15.6 / 22.4 |
| c06 dry stems only | 15.4 | 21.6 | 20.5 | 16.2 / 29.9 / 52.6 |
| returns -3 dB | 11.1 | 17.0 | 18.3 | |
| returns -4.5 dB | 11.9 | 17.9 | 18.6 | 11.9 / 18.8 / 25.8 |
| returns -6 dB | 12.2 | 18.9 | 18.8 | 12.6 / 20.0 / 27.1 |
| returns -9 dB | 13.5 | 20.6 | 19.3 | |
| return HPF 180 Hz, 0 dB | 9.8 | 14.7 | 18.3 | 10.1 / 16.2 / 22.7 |
| return HPF 180 Hz, -4.5 dB | 12.2 | 18.3 | 19.1 | 12.3 / 19.6 / 26.2 |
| **return HPF 180 Hz, -6 dB** | **12.6** | **19.5** | **19.4** | **13.0 / 20.7 / 27.6** |
| return HPF 180 + LPF 2 kHz, -3 dB (batch 5's dark A/B) | 11.8 | 17.3 | 18.9 | 11.8 / 19.0 / 25.5 |
| ONE_TIME_c07 batch 5 item 1 as written, per return (R Strings -4.4, R Winds -1.6, R Brass about -3, R Perc 0) | 10.5 | 17.1 | 18.3 | |

- The c06 master falls only 9.6 dB in the first 0.1 s after a cut. The c05 master, hall included, fell 15.3 dB, as much as c06's dry stems alone. **Everything the c06 master keeps in the first 0.3 s beyond c05 comes from the four returns.**
- Return energy against the dry stems that feed it, per band, whole piece: 100-300 Hz **-0.7 dB**, 200-500 Hz -1.7, 500-2000 Hz -4.4, 2-5 kHz -8.9. In the low mids the hall is as loud as the instruments. Band shares of the master (relative to K-weighted total): 100-300 Hz c05 -8.6, c06 **-6.8**; 200-500 Hz c05 -7.1, c06 **-5.9**. That is 1.8 and 1.2 dB more low-mid weight than c05, which is the measurable side of "mushy". The template's return EQs high-pass at 87 Hz (strings) and 100 Hz (others). c05's hall had S4's 160 Hz low cut. **c06 lost that rule.**
- Which return: R Strings carries 55% of the return energy (-2.6 dB of the return sum) and R Winds 34% (-4.7). R Brass (-13.9) and R Perc (-11.7) are small. At +0.1 s after the cuts, R Winds is as loud as R Strings: -15.7 against -15.0 dB under the master's pre-cut level (R Brass -26.7, R Perc -23.4). Both returns run 3.1-4.4 dB under their senders' dry sum in every section (A, B, tuttis, trio, coda).
- **Judgement (inferred).** Dan's last word on the hall was c01's cut, and c05 measured 19.6 dB at +0.3 s. c06 is back to 14.6, near where c00-c01 sat (10-12 dB) before his complaint, and it is heavier in the low mids. A listener hears the scherzo's rests and staccato fill in again and the bass end bloom.

**Fix** (`build/mix.json` "returns", read by `tools/template_mix.py` / `build_reaper.py`; a mix-only change, no MIDI rebuild):
- All four return faders 6 dB down: R Strings, R Brass and R Winds `fader_db` 1.03 -> **-4.97**; R Perc 0.66 -> **-5.34**. This is the same as every send 6 dB lower (strings -11.6, celli/basses long rows -13.2 and short rows -18.6 with Duc's offsets, horns/trumpets/low brass -14.8, winds -14.4, timpani -12.4, harp -14.8).
- Each return's high-pass from 87 / 100 Hz to **180 Hz, 12 dB/oct**. Either edit the HPF band in the ReaEQ chunk copied from the template, or add a second ReaEQ before Spaces in each return's `fx` list. Simulated: +0.1 / +0.3 / +0.6 s 12.6 / 19.5 / 19.4 dB (c05 15.3 / 19.6 / 20.4), G.P. 20.7 at +0.3 s, master 100-300 Hz share -7.8 and 200-500 Hz -6.5 (c05 -8.6 / -7.1). The master's K loudness falls 1.2 dB, which `deliver_master.py` normalises away. If the HPF cannot be built this cycle, -6 dB alone gives 12.2 / 18.9 / 18.8 and a 100-300 Hz share of -7.5.
- **How to tune the scheduled batch 5 item 1** (`loop/ONE_TIME_c07.md`). As written ("about -10 dB on everything else"), it lowers R Strings 4.4 dB but R Winds only 1.6 dB. It simulates at 10.5 / 17.1 dB, still wetter than c05, because the winds' return carries as much early tail as the strings'. Use **strings -11.5, winds -14.5, horns / trumpets / harp -14.8, timpani -12.4**, and batch 5's **-16 dB or no send** on trombones, bass trombone, tuba, bassoons, contrabassoon and basses. That equals the uniform -6 dB plus batch 5's register cuts. Then keep the return faders at the template's +1.03 / +0.66, so the change happens in one place. The 1.8-2.3 kHz return low-pass (batch 5 item 2) does little on its own: 0 dB with it gives 10.0 / 14.9. Judge it by colour, not as a wetness fix.
- Target for the c07 render: a median cut-off drop of at least 18 dB at +0.3 s and at least 12 dB at +0.1 s, and a 100-300 Hz share of -7.5 dB or lower.

### 2. The harp's pp chords reach the solo tune's level in the trio (bars 153-168, Clarinet 1) and the Meno mosso (bars 341-348, Horn 3, then the woodwinds), because v52 plays the Thumb pick's mp layer (measured; manual p.150)

**Score (read).** Bar 153 (qn 456): Clarinet 1 p dolce, the trio tune; harp pp, "non arpegg." off-beat chords; Horns 3-4 pp drone. Bar 341 (qn 1020): Horn 3 p dolce with the tune, harp pp, basses pp pizz.; 345 (qn 1032) Oboe 1, Clarinet 1, Bassoon 1 p dolce.

**Measured.** For each harp chord I compared its 100 ms peak after the onset with the tune's mean level in the same 100 ms:

| passage | chords | harp peak over tune, median | max | chords within 3 dB of the tune or over it |
|---|---|---|---|---|
| 456-504, Clarinet 1 | 38 | -4.1 | **+2.9** | **14** (462-470 nearly all, 476, 479, 493-501) |
| 552-567, Oboe 1 | 12 | -4.5 | -1.2 | 4 (role -3 already in place) |
| 1020-1032, Horn 3 | 12 | **-1.0** | **+7.2** | **7** |
| 1032-1044, Ob 1 + Cl 1 + Bn 1 | 12 | -3.9 | +2.4 | 4 |

- Per bar, the Clarinet 1 tune sits only 1.1-3.5 dB over the harp's mean in bars 155-157. In 341-344 Horn 3 is 1.8-4.7 dB over the harp's mean (-37.7..-40.1 against -41.1..-42.2).
- The harp's pp chords play v40-61, median 52 (parts.json). Sus RR alternates Pluck (p 1-57) and Thumb (p 1-42 / mp 43-70) by round robin (DIGEST §10, M1 c33). So every Thumb chord above v42 is an mp sample. c06's family EQ (+8 dB shelf at 7.68 kHz, cuts at 304 Hz and 1.27 kHz) with its +6-7 dB make-up gain also tilts the harp toward its attack.
- **Judgement (inferred).** The accompaniment ticks at the level of the dolce tune in the two passages where the score sets one soft solo over a pp harp. This is the "harp that ticks" the C4 lens lists.

**Fix** (`build/score_config.py`, the existing harp cap): `VEL_CAP_SPANS["Harp"] += [(456.0, 504.0, 42), (552.0, 576.0, 42), (672.0, 711.0, 42), (1020.0, 1044.0, 42)]`. This keeps both round-robin cycles on their p layer (manual p.150: velocity selects the layer). At the measured 0.3-0.6 dB per velocity step the cap takes 3-6 dB off. If the actor prefers a level-only change, use `build/roles.json` "Harp" `[456, 504, -4]`, `[1020, 1044, -4]`. Simulated at -3 dB: 456-504 median -7.1, max -0.1, 8 chords within 3 dB; at -5 dB: -9.1 / -2.1 / 2. At 1020-1032 -5 dB leaves 4 chords within 3 dB (max +2.2). There, also check whether Horn 3's rests line up with those chords before cutting more.

### 3. After both sub. p's the inner voices sit level with the espress. tune: clarinets against Violins I at bars 121-128, Oboe 1's lower octave over Flute 1's top line at bars 277-280 (measured)

**Score (read, mockup-events).** Bar 121 (qn 360): Violins I sub. p espress. with the tune (B5...), Violins II the octave below, both espress.; Clarinets 1-2, violas, celli, Horn 2 sub. p with the harmony. Bar 277 (qn 828): Flute 1 sub. p espress. with the tune (B5), Oboe 1 sub. p espress. an octave below (B4); Clarinets 1-2 pp with the harmony.

**Measured (phrase means):**
- 360-372: Violins I -35.4, **Clarinet 1 -36.9, Clarinet 2 -38.2**, Violins II -41.6, violas -42.5, celli -40.7, Horn 2 -40.6. Per bar 121-127, Clarinet 1 is 1.3-2.8 dB under Violins I at 121-123 and 0.3 dB over at 124. **Clarinet 2 is 3.1 dB over Violins I at 125** and level at 126. The two clarinets together are over the tune in 5 of 7 bars.
- 372-384: Violins I -32.7, Clarinet 2 -35.2, Clarinet 1 -36.4, Flute 1 -36.5, celli -36.4.
- For comparison, the same idea at bars 45-48 (132-144) has Violins I 5.8 dB over Clarinet 1 and 8.8 over Clarinet 2.
- 828-840: **Oboe 1 -33.5 over Flute 1 -37.5** (per bar +5.9 / +6.8 / -1.5 / +3.7 at 277-280). Clarinet 2 at pp is -40.6 in bar 277, level with Flute 1's p (-40.3).
- At the c06 S3 frames above, both subitos refill 2-5 dB over c05 from 0.4 s on.

**Judgement (inferred).** At the first sub. p the listener hears a clarinet duet with the violins behind it. At the second the oboe's lower octave is the tune and the flute's B5 is a halo. In every other octave doubling of this idea (45-56, 129-131, 285-287) the top line leads.

**Fix** (`build/roles.json`, adding rows):
- "Clarinet 1": `[360, 384, -3]`; "Clarinet 2": `[360, 384, -4]`. Target: Violins I 4-6 dB over each clarinet at 360-384, as at 132-144.
- "Oboe 1": `[828, 840, -4]`; "Clarinet 2": `[828, 840, -3]`. Keep Flute 1's c06 `[828, 840, -3.5]`, so critic C's subito depth is not given back. Target: Flute 1 0-2 dB over Oboe 1. Simulated by power on the dry share only (the post-fader sends lower each track's reverb as well), the master over 828-840 falls 1.1 dB, which deepens the subito; over 360-384 the clarinet cuts take 0.4 dB off it.

### 4. Trio: two horns sit level with the tune they accompany: Horn 1 (mp) over Clarinet 1 (mf espress.) at bars 209-216, Horn 3 (p dolce) against the celli's tune (mp espress.) at bars 169-176 (measured)

**Score (read).** Bar 209 (qn 624): Violins I and II f espress. and Clarinet 1 mf espress. with the tune T, Horn 1 mp, violas div. mf, celli mf. Bar 169 (qn 504): celli arco mp espress. with T; Horn 3 p dolce; Violins II pp con sord. arpeggios.

**Measured.**
- 624-648: Violins I -31.5, **Horn 1 -34.6**, celli -35.8, Clarinet 1 -36.4, Violins II -37.1, violas -42.7, Violas div -44.0. Per bar 210-214 Horn 1 holds -33.3..-33.5: 3.6-5.8 dB over Clarinet 1, 2.1-5.6 over Violins II (both carrying T at higher printed dynamics). 648-672 (ff from 653): Horn 1 -35.3, Clarinet 1 and Violins II -34.1. The horn is now under them, as printed.
- The dynamic map (median K level of notes of 0.9 qn or longer, by printed dynamic) shows the same thing across the movement. Horn 1 at mp -34.1 sits level with its own mf (-34.2) and 3.3 dB over Violins II at f (-36.9). Horn 1 at p (-36.0) is 4-8 dB over Violins II / violas / celli at p.
- 504-528: celli -38.1, **Horn 3 -40.8**. Per bar 170-175 Horn 3 is within 0.3-2.9 dB of the celli, and over them at 174 (-39.6 against -39.0). Horn 3 carries `roles.json` `[501, 528, +2]`.

**Judgement (inferred).** In the trio's two string statements of T the horn line, printed one level softer, is as loud as the tune, so T loses its singer.

**Fix** (`build/roles.json`):
- "Horn 1": add `[624, 653, -4]`. Target: Horn 1 about -38.5 at 624-648, 2 dB under Clarinet 1 and Violins II, 7 under Violins I.
- "Horn 3": change `[501, 528, 2]` to `[501, 528, -1]`. Target: Horn 3 about -43.8, 5-6 dB under the celli. If that `+2` row was meant for the bar-168 drone handover, keep `[501, 504, 2]` and set `[504, 528, -1]`.

### 5. Counterstatement (bars 31-32, 35-36): the celli's octave doubling under the violins' answer is as loud as the tune or louder (measured)

**Score (read, sA.ily c459).** The strings' answers at 31-32 and 35-36 are Violins I p leggiero, doubled an octave lower by the celli, arco spiccato, p, over the basses' held pp root.

**Measured.** Bars 31 / 32 / 35 / 36: Violins I -40.6 / -41.8 / -39.9 / -41.3, **celli -39.7 / -37.9 / -43.5 / -39.7**. The celli are over Violins I in three of four bars, by up to 3.9 dB. Phrase means: 90-96 celli 2.5 dB over Violins I, 102-108 0.6 dB under. The celli's `[36, 84, -2]` role ends at 84. Rimsky-Korsakov (PDF p.51): at p one string section balances one wind instrument, and sections at equal p are equal. The doubling here is the same printed p, but its job is colour under the tune (the score's own note cites Adler on the doubling as reinforcement).

**Judgement (inferred).** The answer is heard in the cello register, a tenor tune with a violin octave on top, against the calls of Flute 1 and Oboe 1 at the violins' pitch.

**Fix.** `build/roles.json` "Violoncellos": add `[90, 96, -4]`, `[102, 108, -3]`. Target: celli 1.5-3 dB under Violins I in both answers.

### 6. The bassoons sit 3-12 dB under the other woodwinds at the same printed dynamic: Bassoon 1's dolce codetta solo (bars 233-236) is the weakest of the three wind solos (measured)

**Score (read).** Codetta: Oboe 1 p dolce (225-228, qn 672), Clarinet 1 p dolce (229-232, qn 684), Bassoon 1 p dolce (233-236, qn 696), the same figure passed down, over the harp, the basses' pizz. and the E pedal.

**Measured.**
- Phrase means: Oboe 1 -35.5 (672-684), Clarinet 1 -35.8 (684-696), **Bassoon 1 -39.1** (696-708). That is with Bassoon 1's `[696, 708, +1.5]` role in place.
- Dynamic map, bassoons against the median of Flute 1 / Oboe 1 / Clarinets 1-2 at the same printed dynamic: p -43.7 / -44.9 against about -36.4 (7-8 dB under); f -38.2 / -40.4 against -34.3 (4-6 under); ff -37.8 / -37.5 against -26.4 (11 under).
- Rimsky-Korsakov PDF p.51: "in piano passages, all wind-instruments, wood or brass are of fairly equal balance"; in forte Horn = 2 Bassoons = 2 Oboes, so the woodwinds are equal to each other.
- Some of this is the bassoon's low register reading lower on the K curve, but not 7-11 dB of it.

**Judgement (inferred).** In the tuttis the bassoons double bass lines and are covered anyway (the c04 "-5" gains are on the do-not-touch list for that reason). In the codetta the third solo fades instead of passing the phrase on.

**Fix** (`build/roles.json`, not the gains): "Bassoon 1" `[696, 708, +1.5]` -> `[696, 708, +4.5]`. Target: about -36.1, level with the oboe's and clarinet's phrases. Check the harp chords there after finding 2's cap (they ran 7 dB over the bassoon at their peaks).

## Do not touch

- Theme A, 13-28: Violins I 6-10 dB over the pizz. basses, violas and celli. Timpani answers at 20 / 28 under the tune.
- The tutti 101-120: Violins I -23.3 against horns -29.0, trumpets -32.3 (repeated quarters 8-10 dB under the tune: present, not on top), trombones + tuba -30.6, timpani -29.5.
- The summit 1005-1014: horns 7-10 dB under Violins I and 3-6 under Violins II; trumpets and trombones f 10-14 under Violins I; strings and woodwinds on top. The c05/c06 coda roles (Violins II -3/-7, violas +3, Violins I +2/+3) are included.
- The solo violin, 349-356: Flute 1 "col Vl. solo" 3-7 dB under, Violins II "la metà" 8-12 under, violas div. 15-20 under.
- Hn 1's motto tail, 357-360: 8-10 dB over the strings.
- The celli's T at 169-184: 10-13 dB over Violins II con sord.; Violins I 177-184 0-4 dB over the celli an octave below.
- Violas div against violas in 209-224 (within 1.3 dB); the codetta's Ob 1 / Cl 1 10 dB over the harp; Oboe 1 185-188 6-9 dB over the harp.
- The template mix's mic layout, family EQs and their gain make-up. Change only the return level and the return HPF, as above.
