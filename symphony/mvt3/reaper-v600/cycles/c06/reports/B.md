# Cycle 6, critic B (balance and levels): what the EastWest section EQ will do to the c05 balance

Under review: the c05 render (`cycles/c05/render/`), read as the starting point for c06's EastWest template mix (BRIEF "EastWest template mix", `mockup-kit/EW-TEMPLATE-PLAN.md` sections 1-4 and 8). The EQ states come from `symphony/mockup-research/ew-template-2026-11-08/ho-mix-fx.json` (decoded ReaEQ bands of STRINGS, BRASS, WOODWINDS, Harp KS Master, Timpani Flt KS, ORCHESTRAL PERC, MASTER) and the template's mic table from `opus-mics.txt`.

Method (measured, by simulation): per-bar power spectra of all 31 c05 stems (8192-point FFT, 50 % overlap, bars from the parts.json tempo map). Each family EQ and the master EQ were applied as their magnitude responses (RBJ biquads with ReaEQ's bandwidth in octaves, the form ReaEQ uses). Levels are A-weighted, which is a better proxy for loudness than plain RMS when a filter cuts the 400-1300 Hz body. "Old EQ kept" means the mix.json `eq` bands stay where they are. EQ is linear, so every number below holds for the dry stems that c06 will render. Two things this simulation does not cover: the Opus hall that the c05 stems still contain (c06 turns it off and adds the returns), and the new mic layout. Both change level as well, so the c06 render must re-measure every balance below.

## Manual notes (row c6 B: PDF pages 114-115, 154-155, 158-159; MANUAL-GAPS.md read)

| Manual (May 2021 HO, PDF page) | Where it applies here | Followed? |
|---|---|---|
| p.114-115: in the Perc Basics kits, CC11 and velocity set the overall level and velocity sets the dynamic layer (up to 16 or 12 layers). | Crash cymbals (22in Zildjian K Crash) and Bass drum (36in Ludwig) are single-instrument patches, not the kits. They are driven by velocity, with one CC11 value each. | Yes. Their levels sit in velocity and the volume envelope, so the EQ question does not touch their layers. The template's percussion-bus EQ is only a 58 Hz high-pass (finding 6). |
| p.154: the Humanizer randomizes note timing, velocity, tuning, volume (0-100 %) and pan. | None of our tracks. | Yes, it is off. A random volume would undo the per-note level tables. |
| p.154-155: the MIDI Compressor rescales velocity or CC values above a threshold. | Not used. | Yes. It would conflict with the CC11 dynamic curves (dyn_curve) and the velocity maps. |
| p.158: a Macro Parameter drives several automation targets from one knob, each with its own depth and scaling curve. | This is the mechanism behind the template's "Mod + Expression Combo" CC1 macro (FINDINGS section 6). Plan section 5 moves it to c07. | Not used in c06, which is correct: c06 changes only the mix. When c07 tests the macro, its per-target curve can be bent to cross the woodwinds' 55-76 Non Vib/Vib zone quickly. |
| p.159: MIDI CC remapping. Avoid CCs that are already in use. | Timpani uses CC7 (242 points) and CC1 (416). The strings use CC1, CC11, CC15 and CC70. | No conflict found. Do not map any new controller onto CC7 on the timpani. |
| MANUAL-GAPS #4 (p.138-139: Mid against Close on the winds) | The template's woodwind mic layout (Close 1.0 with Main 3-21 dB under it, plan section 1) is the opposite of Mid. | c06 adopts the template layout. #4 stays open as a later test. |

## Findings, ranked by what a listener will hear

### 1. The brass loses 7-9.5 dB (A-weighted) and the strings 3.4 dB. The plan leaves out the template's bus gains, and even those restore only part of the gap (measured)

Where: the whole piece, worst in the brass-led passages. What: the BRASS EQ's two wide bells (-5.4 dB at 475 Hz and -7.8 dB at 821 Hz, both 1.92 octaves wide) overlap. Together they cut -9.8 dB at 456 Hz, -11.2 at 600, -11.0 at 821 and -9.5 at 1 kHz. That is not the "2-8 dB" stated in plan section 3. Horns put 90-93 % of their A-weighted energy in 250-1300 Hz, so they lose the most. Whole-piece change by family, family EQ plus master EQ:

| family | EQ only | with the template bus gains (brass +2.93, winds +3.36) |
|---|---|---|
| strings | -3.4 | -3.4 |
| winds | -5.9 | -2.5 |
| horns | -9.4 | -6.5 |
| trumpets | -7.1 | -4.1 |
| trombones + tuba | -7.6 | -4.6 |
| harp | -5.8 | (template -10.7: do not copy, finding 3) |
| timpani | -6.8 | (template +6.62: do not copy, finding 2) |

The bus gains come from `ho-mix-fx.json`: the BRASS bus fader is +2.93 dB and the WOODWINDS bus fader +3.36 dB. The plan does not list them. The template also runs its solo horn (1FH KS Master) at Opus master +8.0 dB against -0.3 dB for 2FH and 6FH (`opus-mics.txt`), so EastWest itself lifted the solo horn under this EQ.

Lead minus accompaniment, dB A (c05, then EQ, then EQ plus template bus gains):
- Trumpet 1 solo, bars 51-66, against everything else: +4.2, +1.4, +1.3. The soft solo loses most of its margin over the winds, which are cut only 5.5 dB.
- Bass theme, bars 27-34 (celli, basses, bassoons, contrabassoon, bass clarinet, low brass, Horn 3) against Violins I+II: +4.0, +1.0, +3.6.
- Chorale bars 223-234, brass against string tremolo: +6.2, +1.3, +4.2. Bars 255-264: +5.9, +1.5, +4.4.
- Horns against trumpets + trombones + tuba in the chorale: -5.1 to -7.0 (223-234) and -5.6 to -7.5 (255-264). Bus gains cannot fix this because both are brass. Rimsky-Korsakov (Principles, reference-books/text/rimsky-principles.txt line 1516: "two horns are needed to one trumpet or one trombone" in forte) supports c05's -5 dB for four horns against seven heavy brass. -7 dB goes beyond that.
- Trumpets, theme B bars 211-218, against the tutti: -0.9, -1.8, -1.0.
- Muted Trumpet 1 against the cor anglais it doubles, bars 171-186: -3.2, -5.4, -5.8.

The loss also depends on dynamic for trumpets and trombones (measured: softest against loudest quarter of each track's bars). Their soft layers are darker, so they lose more. Trumpet 1 loses 8.2 dB soft and 6.7 loud, Trumpet 2 7.7 and 6.7, Trombone 1 9.3 and 7.4, Trombone 2 9.6 and 7.1, Bass trombone 8.8 and 6.8. Winds, strings, horns and tuba vary by under 1 dB. So a p trumpet or trombone line ends up about 2 dB further under its ff level than in c05.

Fix (build/mix.json): add per-family make-up gains that put each family back at c05's A-weighted level against the strings. The make-up is the family's loss minus the strings' 3.4 dB: winds +2.5, horns +6.0, trumpets +3.7, trombones and tuba +4.2, harp +2.4. Apply them to the track `gain_db` values, or as one group gain if apply_mix gets one. This keeps five cycles of balance work valid and keeps the timbre change. Do not copy the template's +2.93 and +3.36 instead: they leave horns 3 dB short and do not account for our mic levels. Then raise `soft_trim_db` pp/p/mp by +1.5 on Trumpets 1-3 and by +2.0 on Trombone 1, Trombone 2 and Bass trombone, to undo the dynamic-dependent loss. Check on the render: Trumpet 1 at bars 51-66 at least +4 dB A over the rest, horns against the heavy brass at -5 ± 1 dB in both chorales, brass against strings at +5 to +6 dB at 223-234.

### 2. The timpani EQ adds boom: the 30-150 Hz band rises while the body and stroke fall. Copying the template's +6.62 dB timpani fader would make the timpani the main bass instrument at the arrival and the ending (measured)

Where: Timpani, especially the long rolls (bars 5, 35, 39, 93-94, 147-151, 167, 209-210, 219-223, 231, 243, 261-263, 273, 278). What: the Timpani Flt KS EQ boosts +8.58 dB at 84 Hz, cuts -11.5 dB at 385 Hz (2.54 octaves wide) and adds a +9.1 dB shelf at 7 kHz. Our timpani's lowest note is F2 (87 Hz), so the boost sits right on the drums' fundamentals. On the c05 timpani stem: A-weighted -6.8 dB, 30-150 Hz +1.4 dB, 150-600 Hz -7.2 dB. The low band rises 8.6 dB against the body, so the drum gets boomier and its stroke less defined. Share of all 30-150 Hz energy held by the timpani:
- ending, bars 271-279: 18 % in c05, 26 % with the EQ, 62 % with the EQ and the template's +6.62 dB fader;
- arrival, bars 223-226: 7 %, 11 %, 36 %.

Dan's rule is that long timpani rolls must not drown other parts (BRIEF priorities). The template's EQ comes with its own mic mix: Surround 0 dB, Close -8.4, Main -6.9 (`opus-mics.txt`). Our timpani uses Close 0.2 and Main 0.5 with no Surround. That is probably why EastWest needed the low boost and we do not (inferred).

Fix (mix.json Timpani): keep `gain_db` -7 and do not copy the +6.62 fader. Use a reduced form of the template EQ: HPF 44 Hz, no 84 Hz bell, -6 dB at 385 Hz (2.54 octaves), shelf +4.5 dB at 6.96 kHz. Simulated: A-weighted -4.9, 30-150 Hz -2.6, 150-600 Hz -5.4, 2-6 kHz -1.3. That keeps the clearer top and the lighter boxiness without raising the boom. A milder option, the 84 Hz bell at +3 instead of +8.6, gives A -7.6 and 30-150 Hz -2.5, but cuts the body further. Remove the timpani `loud_eq` bell (140 Hz +3, finding 5). Keep the switched 1.5 kHz -6 dB shelf for the soft and medium sticks (qn 707-712, 871-985); it emulates a specific stick. Check on the render: timpani share of 30-150 Hz energy at bars 271-279 no higher than c05's 18 %, and the roll at 223 settling under the brass after its attack, as in c05.

### 3. The harp's 183 Hz high-pass removes the fundamentals of its bass notes, and the template's -10.7 dB harp fader would bury it (measured)

Where: Harp, all its passages. Its bass notes go down to D1. 90 of its 317 notes are at or below F#3, which is the high-pass corner, spread over 34 bars, including the accompaniment to the violins' F2 at bars 67-82. What: the Harp KS Master EQ is HPF 183 Hz, -8.3 dB at 304 Hz, -8.6 dB at 1.27 kHz and +8 dB shelf at 7.68 kHz. In the bars with bass notes: 25-60 Hz -27.1 dB, 60-120 Hz -12.8 dB, 120-250 Hz -9.4 dB, A-weighted -6.0 dB. Harp against Violins I at bars 123-134 goes from +0.9 to -0.9 dB A. Against the violins at bars 67-82 the harp falls from 9.6 to 12.0 dB under. The template's harp track fader is -10.7 dB, and its Opus mix (Close 0, Mid 0, Main -9) is not ours (Close 0.6, Main 1.0). Copied, it would put the harp 16.5 dB under its c05 level.

Fix (mix.json Harp): replace `eq` [highpass 30] with the template bells and shelf but a high-pass at 80 Hz (simulated: 60-120 Hz -4.2, 25-60 Hz -13.8, A-weighted -5.7). Raise `gain_db` from -4 to -1.6 (+2.4, the make-up in finding 1). Do not copy the -10.7 fader. Keep the side-only 300 Hz -8 dB `side_shelf`. Check: harp against Violins I at bars 123-134 back to about +1 dB A, and the bass notes of the bars 67-82 accompaniment audible in 60-120 Hz.

### 4. The family high shelves make the mix much brighter than the references, and some old shelves pull against them (measured, one point inferred)

What: the shelves (strings +4 dB at 4.73 kHz, brass +4 at 7.49 kHz, winds +5.1 at 7.59 kHz, master +0.8 at 8 kHz) combine with the body cuts. Sum-of-stems band shares, dB of total energy (20-100, 100-250, 250-500, 500-2k, 2-6k, 6-20k Hz):
- c05: -15.4, -8.5, -6.5, -2.6, -12.3, -29.0
- EQ plus the template bus gains: -13.4, -6.7, -6.5, -4.0, -9.5, -21.0
- references: Dvořák 9/i -21.7, -6.6, -6.3, -3.5, -10.5, -28.8; Brahms 1/ii -8.5, -8.8, -6.0, -3.8, -12.4, -32.2; Brahms 4/ii -7.9, -7.6, -6.3, -4.4, -11.8, -32.3.

c05's top band matched the Dvořák reference. With the EQ it sits 8 dB above Dvořák and 11 dB above the Brahms recordings. The 2-6 kHz band also comes out 1-3 dB above the references. Violins I would carry 23 % of the 6-20 kHz energy, up from 12.5 %. The trumpets carry 34 %.

There is also a question about the strings shelf. It is stored at a bandwidth of 0.33 octaves. In the RBJ form ReaEQ uses, that is a resonant shelf: -5.5 dB at 4 kHz and +5.9 dB at 5 kHz, which would scoop the violins' 3-4 kHz presence and spike just above it. With a gentle bandwidth (1.9 octaves) it would be +1.3 dB at 4 kHz. This is inferred: verify by rendering noise through the chunk-loaded STRINGS ReaEQ once. Removing every shelf still leaves the top band at -23.8, because of the bus gains and the body cut. The shelves add about 3 dB of that rise.

Fix: load the family EQs from the chunks, then judge the top on the c06 master. Caveat: the c05 stems include the Opus hall, which is cut at 5.5 kHz, and the new returns are low-passed at 5.6/8.5 kHz. The dry-plus-returns master will therefore come out somewhat darker than this sum. If the 6-20 kHz share is still more than 3 dB above the Brahms references, halve the shelves (strings +2, brass +2, winds +2.5) in a pass-2 copy. Keep these old shelves, which pull against the family shelves on purpose: Violins I highshelf 5 kHz -4 dB (it cancels the strings shelf on the brightest track), Trombones 1-2 and Bass trombone highshelf 4 kHz -4, and the violins' loud_eq 2.5 kHz -2.5 at ff. Remove the Trumpets 1-3 highshelf 4 kHz +2.5: it adds to the brass shelf on the tracks that already carry a third of the top band.

### 5. The loud-tutti low bells now do what the family EQ already does (measured)

What: the `loud_eq` low bells are switched on in 74 ff/fff bars (Bassoon 2 +3 dB at 140 Hz; Contrabassoon, Bass trombone and Tuba +4 at 140; Timpani +3 at 140; Violoncellos +6 at 150; Double basses +6 at 160 with -4 at 98). Movement I added them to raise the low body against the mids in tuttis. The family EQ already does that: the 100-250 Hz share rises from -8.5 dB (c05) to -6.7 with EQ and bus gains, above all three references (-6.6, -8.8, -7.6). In the loud bars it is -6.4 with the bells kept and -8.9 with them all removed. Halving them and removing the timpani bell gives -7.7, which equals Brahms 4/ii and sits between the other two references.

Fix (mix.json `loud_eq`): Timpani, remove the 140 Hz bell. Violoncellos 150 Hz +6 to +3. Double basses 160 Hz +6 to +3 (keep the 98 Hz -4 notch). Contrabassoon, Bass trombone and Tuba 140 Hz +4 to +2. Bassoon 2 +3 to +1.5. Keep the violins' loud_eq high shelf (finding 4). Check: master 100-250 Hz share in the loud_eq bars between -7 and -8.5 dB.

### 6. Which old EQs duplicate the family EQ, and which to keep (measured unless marked)

Remove, because the family EQ now does the same job:
- HPF 40 Hz on Violins I, Violins II and Violas: the strings HPF at 53 Hz replaces it.
- HPF 40 Hz on Horns 1-4, Trumpets 1-3, Trombones 1-2 and Bass trombone: the brass HPF at 41 Hz replaces it.
- Timpani HPF 45 Hz: the timpani HPF at 44 Hz replaces it.
- Harp HPF 30 Hz: replace it with 80 Hz (finding 3).
- Trumpets 1-3 highshelf 4 kHz +2.5 dB (finding 4).
- Bass clarinet highshelf 2.5 kHz -4 dB. It stacks with the woodwind bell at 2.2 kHz (-4.7 dB, 1.7 octaves), which would put about -8.5 dB on the bass clarinet's 2-4 kHz. The family bell alone matches what the other winds get.
- The timpani loud_eq bell (finding 5).

Superseded with a choice (measured): the strings HPF at 53 Hz replaces the 30 Hz HPF on the celli and the 25 Hz HPF on the basses. 601 of the basses' 690 notes are at or below E2. On the 100 bars with bass notes at or below A1, the 53 Hz HPF costs -6.4 dB in 25-60 Hz and -2.3 dB A. A 35 Hz HPF on the basses alone would cost -3.8 and -2.2. Take 53 Hz as EastWest does unless the c06 low end sounds thin; it also serves the BRIEF's "bass solid but not boomy". The tuba's 25 Hz HPF becomes 41 Hz: -4.1 dB in 25-60 Hz on the 42 bars with notes at or below A1. That is acceptable.

Keep, because each fixes a specific sample problem or a choice the family EQ does not make:
- Double basses: bell 87.3 Hz -12 (F2) and the B1/D2 `mute_eq`.
- Tuba: 84 Hz -5 bell (E2/F2).
- Contrabassoon: low shelf 70 Hz -4.
- Violoncellos: bells at 125 and 170 Hz +3. The celli already lose 4.5 dB A against the violins' 3.0, and removing the bells would cost another 1.4 dB.
- Double basses: 180 Hz +4 bell.
- Violins I 5 kHz -4 shelf and the trombones' 4 kHz -4 shelves (finding 4).
- Trumpet 1's Mute Sus band-pass, 250 Hz-8 kHz.
- The timpani's switched stick shelf.
- Every `side_shelf`.
- The woodwind HPFs at 30/40 Hz: the woodwind EQ has no high-pass, and these are harmless.
- Bass drum: do not add the template's percussion-bus HPF at 58 Hz. The plan does not ask for it, and it would cost the bass drum 3.7 dB in 30-150 Hz at the arrival and the ending.

The trims do not duplicate the EQ. `dyn_trim_db` and `soft_trim_db` correct the level of each dynamic layer, and a linear EQ shifts every layer by the same amount. The exception is the trumpets and trombones, whose soft layers lose 1.5-2.5 dB more (finding 1). Of the track gains, only the family offsets need the make-up in finding 1.

Implementation note (read in tools/build_reaper.py, `set_eq`/`config_eq`): `set_eq` deletes every ReaEQ on the track before it adds its own. Its single ReaEQ holds only a high-pass, a low shelf, two bells and a high shelf, and the celli and basses already use three of those bands. Load each family EQ as a separate ReaEQ from its chunk (STRINGS.txt, BRASS.txt, WOODWINDS.txt, and the harp and timpani chunks with the changes above), after `set_eq`. Then make `set_eq`'s delete loop skip it, for example by renaming the FX and matching on the name. Otherwise the next `--mix-only` run deletes the family EQ silently. Expect the master to fall about 6 dB before make-up (sum of stems -5.4 to -6.8 dB A per passage), so refit deliver_master.py as the plan says.

Do not touch: the per-dynamic `dyn_trim_db` and `soft_trim_db` tables (except the trumpet and trombone soft-trim lift above); the sample-specific notches (basses 87.3 Hz and mute_eq, tuba 84 Hz); the cello and bass body bells; the Violins I and trombone high-shelf cuts; the timpani stick shelf and the 237 ms horn and dynamic-layer string release caps; c05's balance targets (Trumpet 1 at least +4 dB A over the bars 51-66 accompaniment, chorale brass +6 dB over the tremolo, timpani at most 18 % of the ending's low band). Measure them again on c06.
