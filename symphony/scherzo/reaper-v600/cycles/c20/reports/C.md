# Cycle 20, critic C (holistic): the c19 render and its delivered mp3

## Manual notes (May 2021 HO manual, row 20 slot C: H2, PDF pages 44-45 and 134-136; MANUAL-GAPS.md read)

| Page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.44 | MIDI channel modes: Multi (CC1, CC11 and pitch bend apply only to the voices on the controller's channel), MPE, Omni, 1-16 | every track (one Opus instance per track, one channel) | Yes. Per-voice CC (Multi) is an option the mockup does not need: no track carries two lines that need different CC11, except the violas' "non div." double stops (bars 105-120), which play as one section anyway |
| p.45 | CC1 is "commonly used" to crossfade dynamic layers and/or vibrato layers or to set volume. CC11 sets volume, or sets dynamics when CC1 controls vibrato | strings and woodwinds: CC11 = dynamics, CC1 = vibrato. Brass and clarinets: CC1 = dynamics (`CC1_DYN_TRACKS`) | Yes. The c19 Clarinet 1 CC1 f-fff map uses exactly this, but it moved the stem only 0.9 dB (CHANGES c19), so the level fault went back to `dyn_trim_db` (below) |
| p.134-135 | Play page: purge control (samples load only as needed), Mood, Performance, Sensitivity and MIDI control, Envelope (volume envelope stages), Stereo Double, Reverb, Channels (mics, master channel) | memory (`UNLOAD_UNUSED_ROWS`), release caps (Envelope), mic mix | Yes. Rows are unloaded (43-44 GB settled). Opus reverb is off (`opus_reverb_off` true; EW Spaces II returns instead) |
| p.136 | Moods. Classic: Main mics (Decca tree and outriggers), a 3.4 s Southern California hall. Soft: "lighter touch" for slow, emotional passages, Mid + Surround mics through Abravanel Hall. Epic: Close + Main + Surround, a 2.8 s cathedral | the trio's dolce passages (bars 153-240), the Meno mosso (341-376) | Partly, and correctly so. The mix is Close + Main per family (mix.json `groups`) through one shared hall (RT60 1.38 s, G.P. drop 18.4 dB on c19), so it sits near Classic but drier. Switching the trio to Soft would change mics and hall in mid-movement, which breaks the one-room rule (BRIEF item 3) and Dan's wetness limit (the 3.4 s / 2.8 s halls are far over c05's RT60 1.5 s). Do not adopt it. The trio's lighter touch has to come from CC11 and velocity, see #3 |

MANUAL-GAPS items that bear on the findings below: #2 (repetition rows, not used), #8 (expressive rows for the cantabile lines, not used). The 2021 manual also lists "Detache" (p.90: longer than staccato, with a defined end, a fast bowed attack) and "Legato Slur Staccato" (p.99: the first note of a slur gets a firmer attack). The 1st Violins KS Master has both rows ("Detache", "StacSl Leg BC + Slur + Port MAX"). Neither is in MANUAL-GAPS, and #2 below uses them.

## How the movement sounds as a whole on the delivered mp3 (measured, ebur128 momentary/short-term per section)

Per-section mean momentary loudness on the c19 mp3 (LUFS): intro -18.4, theme A -17.7, counterstatement -14.6, second idea (f/ff) -10.4, fugato -13.9, F-major episode -18.4, retransition -19.3, first tutti -9.6, sub. p second idea -15.0, harmonic link -20.4, trio: clarinet tune -17.2, celli tune -15.5, middle part -17.5, f -14.1, ff -13.8, codetta -18.9; reprise -14.9, second tutti -10.9, coda build -11.2, summit (336-339) -7.9, Meno mosso -20.0, Violin solo -16.9, last G sharp -20.5.

- Quiet passages (Dan's AirPods case): the quietest sections are 6.4-6.5 LU under the -14.0 integrated level, with short-term p10 at -21.6. That meets the shared target (p10 -23 or higher), and the quiet-level complaint is answered by level. c19 differs from c18 by 0.6 LU or less in every section, so a listener will hear c19 much as c18: the trio's celli section +0.6 and the second tutti +0.5 are the only moves.
- Shape: soft opening, fugato growth (-13.9 with a p10 of -22.7), trio, reprise and close all keep their order. The sub. p of bar 121 drops 9.7 LU on the mp3 (bar 120 M max -9.0 to bar 121 -18.7; master 13.0 dB). Bar 277 drops 8.2 LU (master 8.5). Both are clear.
- Wet or dry: not too wet (c19 CHANGES: G.P. drop 18.4 dB, 20 dB fall in 0.33 s, RT60 1.38 s, all inside the c05 limit). The long-term spectrum is not dull or thin: the 2-6 kHz share is -10.7 dB against -10.5 to -12.4 in the three references, and 250-500 Hz is -5.5 against -5.95 to -6.3, so there is no low-mid build-up (metrics.md).
- Where the movement is weakest: the coda (the fff is not an arrival, #1), the machine-like holes inside the Allegro's staccato lines (#2), and the trio tune's uneven note levels (#3).

## Ranked findings

### 1. The summit is not an arrival on the mp3: bars 333-339 are one flat plateau (measured, simulated)

Where: coda, bars 331-339 (qn 990-1017), the delivered file.

What is wrong: the score builds from ff at bar 333 (qn 996) to fff at bar 336 (qn 1005). On the master the build steps up: bar means (momentary) are 332 -17.7, 333 -15.2, 334 -15.3, 335 -13.8, 336 -11.8. On the mp3 the same bars read -8.8, -8.0, -7.8, -7.4, -7.4, so the fff adds 0.0 LU and bars 333-338 lie within 0.8 LU. The limiter takes 5.6 dB there. The master's peak-to-loudness ratio in those bars is 7.6-8.4 dB, the same as in the tuttis, so no single stem's peak causes it: the -14 target simply needs that much gain reduction at the top. c19's ride of -1.5 / -3 dB on bars 334-335 did nothing, because it was smaller than the limiter's own reduction there (about 4 dB): the limiter gave the cut back.

Across movements: the summit's lead over the 95th percentile of short-term loudness is 1.9 LU on c19, 2.3 on Movement I c60 and 1.1 on Movement II c57, against 5.0 on c17 at -19.5 LUFS. The five recordings in mockup-kit LEARNINGS run 4.8-7.6 dB from p75 to max. The summit's lead over the first tutti's mean fell from +5.3 LU (c17) to +1.7 (c19).

Fix (delivery only, the finale's technique 94; no track envelope involved): add one row to `RIDE_TRIMS` in `build/score_config.py`:
`[(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1004.6, -4.5), (1005.1, 0.0)]`.
It has to be deeper than the limiter's reduction on 333-335, which is why it reaches -4.5. I ran `tools/deliver_master.py` on the c19 master with the c19 build_fix ride rows plus this row, in my scratch folder:
- bar means: 331 -12.6, 332 -10.5, 333 -9.4, 334 -9.5, 335 -8.7, 336 -7.4, 337 -7.6, 338 -7.2;
- the fff now steps +1.3 LU over bar 335 and +2.0 over bar 333, where it stepped 0.0 / +0.6;
- LRA 12.2 (unchanged), limiter 5.6 (unchanged), tuttis unchanged;
- I -14.1 after one pass (the loudness loop's second pass brings it to -14.0).
A row starting at 987 instead put a 0.5 LU dip between bars 329 and 330, so start it at 990. With the row, bars 329-331 read -12.7 / -12.9 / -12.6: the master's +1.6 dB at 331 becomes +0.3. Check that on the delivered file.

Optional second step, only if Dan accepts a lower LRA: deepen the two tuttis with `[(311.0, 0.0), (312.4, -2.0), (360.0, -2.0), (363.0, 0.0)]` and `[(911.0, 0.0), (912.4, -1.5), (959.0, -1.5), (961.0, 0.0)]`. Simulated together with the coda row:
- summit over the first tutti +2.7 LU (was +1.7), over the second +3.8 (was +3.0);
- LRA 11.4 (under "about 12"), p10 -21.2;
- the sub. p drop at bar 121 9.1 LU (was 9.7).

### 2. Slurred eighth pairs inside the Allegro's staccato lines fall into holes, 6-22 dB under their neighbours (measured)

Where: Violins I qn 66-68 (bar 23) and 786-788 (bar 263), the theme's crescendo into the accented C6; also 112-113.5, 125, 343, 353.5, 821.5, 893.5, 1001.5. Violins II 197.5, 343-343.5, 347.5, 353-353.5, 943.5, 947.5, 983.5. Clarinet 2 329.5 / 929.5 ("Leg Slur Rep"); Flute 1 893.5.

What is wrong: two slurred eighths among staccato notes play as two separate "Sus MAX" notes 0.52-0.55 qn (0.12 s) long. A string Sus MAX does not reach its body in 0.12 s, so the pair sounds as a gap in the line. I measured the 10 ms peak inside each note on the Violins I stem: 66 -41.6, 67 -52.0, 67.5 -47.7, 68 -30.0, under a printed crescendo from 66 to 69. In bar 263: -37.8, -45.8, -36.5, -29.6. Over the whole Allegro, 17 of 57 Violins I slurred short notes (median -1.9 dB) and 10 of 33 Violins II (median -4.7 dB) sit more than 6 dB under their detached neighbours within 1.6 qn. The data are unchanged since c15 (identical levels on the c15 stems), so this is old and has not been treated. It is the most "machine" moment in the theme: a leggiero line that drops out for an eighth and then jumps 18-22 dB to the next staccato.

Fix (instrument side; one row on two tracks; range-test first): in `build/score_config.py` `ART_SPANS`, give the slurred short notes (string notes of 0.6 qn or less inside a printed slur, Allegro only, the list above) a row with a fast attack instead of Sus MAX. Test both on qn 64-70 and 784-790 (Violins I) and 340-356 (Violins II):
- (a) "StacSl Leg BC + Slur + Port MAX" (manual p.99, Legato Slur Staccato: the slur's first note gets a firmer attack and the second is connected), at the line's staccato velocity;
- (b) "Detache" (p.90) on both notes, at the staccato velocity +5.
Target: each note of the pair within -3..+1 dB of the detached neighbours' 10 ms peak, and the crescendo rising note by note from 66 to 69. Keep the version that meets it. Kit LEARNINGS line 130 found that neither row separated 0.16 s slurred viola notes better than Sus MAX by pitch share. That test measured pitch clarity, not level; here the fault is the level hole. For Clarinet 2 329.5 / 929.5, check whether "Stac DblTng RRx9" (the track's other loaded row) at the printed length removes the 10.6 dB hole.

### 3. The trio tune does not sing evenly: note-to-note level jumps against small printed hairpins (measured; cause partly inferred)

Where: celli bars 169-184 (qn 504-552, "arco, espress."); Clarinet 1 bars 153-168 (qn 456-504, dolce).

What is wrong: across the phrase, a singer or player keeps the line even and shapes it with the hairpins. Here the hairpins move CC11 by only 5-6 units (Clarinet 1 49 -> 55 -> 49 over each < >), while the note bodies jump:
- Celli: note bodies (0.1 s after the note-on to 0.05 s before its end) span 17.6 dB, std 3.2. qn 514 (G sharp 3 after A3, a half-step slur) reads -29.0 against -36.2..-40.1 for its neighbours: the legato transition swell. 511.5 and 524 read -44.5 and -46.6: holes. 524 is a "Sus MAX" re-attack at velocity 112 that is 9 dB under its neighbours.
- Clarinet 1 ("Leg Slur Rep" for all 263 notes): range 11.8 dB, std 2.9, with 4-7 dB note-to-note steps that the hairpins do not explain (461 -41.4 after 459 -38.0; 466 -41.0 after 464 -34.6; 476 -44.4 then -35.3).
Critic A has the string join swell (median +3.2 dB, 96 of 429 joins over 6 dB). From the holistic view it matters most here, in the movement's one long cantabile tune.

Fix: spend this cycle's legato range test on the celli tune with the finale's untried alternative (technique 98: "Sus MAX" on held arrival notes took the bloom from +4.5..+7.6 to +0.7..+3.9 dB). Set `ART_AT` "Sus MAX" on the long arrivals after a slur (qn 514, 520, 533, 546; then 507, 526, 528 if the first four pass), with `REATTACK_LEAD_AT` 0.085 s (the c19 Violins I 597 recipe). Target: note-body std under 2.5 dB and no join over +4 dB. For Clarinet 1, A/B the dolce tune 456-504 on "Leg Slur MAX" against "Leg Slur Rep". The Rep row is the REP_ROW choice for the clarinet's repeated notes, but this tune (qn 456-504) has no same-pitch repeats, so the plain legato row may be steadier. Keep the row with the lower note-body std. If the steps stay, widen the hairpin CC11 swing to about ±10 units on the trio tunes (`HP_GAIN_TO_CC11` or the hairpin depth for Clarinet 1 and the celli): that shapes the phrase through the instrument, not the envelope (inferred).

### 4. Hot and cold single notes in the staccato theme (measured)

Where: staccato and spiccato notes of 0.55 qn or less in the Allegro, compared with the median of their three neighbours on each side.

What is wrong: the median deviation is 1.1-1.8 dB (good), but the p90 is 3.8-5.2 dB, and 5-8 % of notes are more than 5 dB off:
- Violins I 17 of 230. 60 (A5, bar 21 downbeat, p) is +7.2 at the same velocity 57 and CC11 50-51 as its neighbours, so it is a hot round-robin sample. Also 120 +6.4 and 126 +7.4.
- Violins II 16 of 149: 957 +9.8, 984 +10.6, 988.5 -9.0.
- Oboe 1: 120 +11.0, 279 -10.1.
- Violas: 270 -9.8.
A real section varies about ±2-3 dB in a p leggiero line. A single note 7-11 dB out sounds like a sample.

Fix: velocity only (no envelope). `VEL_SET` on the listed onsets: hot notes -8 to -12 velocity, cold notes +8. Where a velocity change does not move the level (a round-robin sample's own level), put an `RR_RESET_AT` (CC16) one note earlier so that a different take plays. Accept the change only where the note lands within 3 dB of its neighbours; leave notes that sit at printed accents, downbeat swells of a printed crescendo or a new dynamic (Violins I 68, 816 f) as they are.

### 5. The unrendered Clarinet 1 ff trim (build/ only): right, keep it (inferred from c19's numbers)

c19's CC1 map lowered the Clarinet 1 stem by 0.9 dB only, so it is still +3.0 / +3.6 / +3.1 dB over Violins I in bars 334 / 214 / 302. The `dyn_trim_db` ff step from +1.2 to -1.0 (-2.2 dB) should take it to about +0.8..+1.4. That is a slow per-dynamic balance (allowed), and it does not touch f (bar 41 is 0.0 dB, f). Check bars 72 and 300 on the c20 stems: Clarinet 1 should stay audible there at 0-1.5 dB over Violins I, not fall under them.

## Do not touch

- The delivery chain: -14 LUFS with the loudness loop, the 2:1 top ride, the c19 ride rows (add the coda row of #1, do not replace them).
- Hall and returns: RT60 1.38 s, G.P. drop 18.4 dB, inside Dan's limit; no more and no less hall.
- Horn 1's "Sus MAX" G sharps; the Violins II trio +9; the clarinets off the wind overlap; the woodwind overlap at 0.6 s; `REP_GAP_FLOOR_LONG_S`.
- The sub. p drops at bars 121 and 277 (9.7 / 8.2 LU on the mp3).
- The section order and the quiet passages' level (p10 -21.6).
