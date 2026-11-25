# Cycle 01, critic C: blend and space (Lens C1), on the c00 render

Scripts ran on `cycles/c00/render/` (stems and master, 48 kHz float), `build/parts.json`, `build/mix.json` and the generated Opus states in `jobs/*.b64` (read with `opus_state.split`, nothing written). The time map came from parts.json `tempo`. The only reference audio on disk is the Dvořák 9/i MP3. The Brahms band shares are the stored ones in `measure.py`. Levels are plain RMS dB unless I say otherwise.

## Manual notes (L1: PDF pp. 138-139, 141-142 of the May 2021 HO Opus manual; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.138: the Close mics stand in front of each section. Mid mics are at the stage edge ("definition without the sound of close proximity"). Main is a Decca tree plus outriggers in the fifth row, mostly room reflections ("big, unified sound"). Surround mics are high at the back. | Every track: winds Close 0.5 / Main 0.8; horns and trumpets 0.5 / 1.0; strings at the patch default 0.66 / 1.0; timpani 0.2 / 0.5; harp 0.6 / 1.0 (read in `jobs/*.b64`). | Yes for the full sections. The Mid position is used nowhere (MANUAL-GAPS #13). |
| p.139: Main = three M50s as a Decca tree plus outriggers. That is where a patch's stereo spread and room come from. | The Close-only DIV patches: Violin I solo (DIV A) and Violas div (DIV B) load only Close (read: no Main channel in states 29 and 30). | Partly. These tracks have no tree, so they are narrower and drier than the section they belong to (finding 3). The pipeline makes up for it with send (0.53 and 0.33 against the sections' 0.17 + 0.25) but not with width. |
| p.141: Stereo Double widens a stereo source, and it works only with the Stereo channel source. | It could widen the Close-only DIV tracks. | Not used. The violas div track uses a side high shelf +3 dB instead. |
| p.141-142: the reverb is a convolution IR with preset, pre-delay and volume. The Master button shares one reverb across the instruments in one instance. | One instance per track. The pipeline puts the same true-stereo IR into every instance ("S. Cal Hall Perc TS FR 3.3s", fx 0.19, wet 2.0, high cut 5.5 kHz). | Yes. All 31 states read back with the same IR, fx volume, wet and true-stereo flag. |
| p.142: the envelope (attack, hold, decay, sustain, release in ms); "be careful when changing them". | Harp and harp harmonics env_sustain 1.0 and release 200 ms; sus_release_cap 250 ms on violas, celli and basses. | Yes, as configured. The harmonics ring with a 17 dB drop at +1 s. |

## Findings, ranked by what a listener would hear

### 1. Flute 1 "col Vl. solo" covers the solo violin by 7-11 dB (bars 349-356, qn 1044-1068; Flute 1, Violin I solo, Violins II)

What is wrong: the score marks Flute 1 "dolce, sempre pp, col Vl. solo". The flute should colour the solo, not replace it. In the render the passage sounds like a flute solo with a faint violin under it. The violin solo also barely clears the Violins II "la metà" an octave below.

Evidence (measured, per bar, stem RMS): solo -47.3/-45.5/-46.1/-50.3/-51.0/-49.6/-52.5/-52.5 dB; Flute 1 -40.2/-37.6/-37.1/-40.1/-40.2/-40.4/-41.9/-49.8. Flute minus solo is +7.0, +7.9, +9.0, +10.3, +10.9, +9.2, +10.6 and +2.7 dB. Over the whole span the flute is -39.9 dB, the solo -48.6 and Violins II -49.5 (solo over Violins II: +2.2, +0.6, -1.6, +2.4, +4.2, +3.3, +3.6, +3.7 dB per bar). The flute plays the same pitches (mean MIDI 87, about 1.2 kHz), so loudness weighting does not change the order. Both tracks start from CC11 42. The gap comes from the flute's pp soft trim (+7 dB in mix.json) and the half-section DIV A patch with no Main mic.

Fix: in `build/roles.json`, Flute 1 -9 dB from qn 1043.5 to 1068 (ramp in over the solo's pickup at 1043.5, ramp out by 1068), aiming 3-5 dB under the solo. Violin I solo +2 dB over the same span, so it sits 4-6 dB over Violins II "la metà". Check bar 351, where Violins II is now louder than the solo. Re-measure per bar: flute minus solo between -3 and -5, solo minus Violins II between +4 and +6.

### 2. The tuttis lose their low-mid body while the soft passages carry too much (bars 101-120, 301-320, 329-339; Violoncellos, Double basses, bass-octave winds and brass)

What is wrong: in a real orchestra the 100-250 Hz share rises in the tuttis. Here it falls. The tutti sounds thin and mid-heavy, with the felt timpani supplying much of the low-mid body that the celli and basses should supply.

Evidence (measured, master, 0.4 s frames, energy shares of 20 Hz-20 kHz):
- Loudest 10% of frames: 100-250 Hz -9.0 dB, 500-2000 Hz -2.2. Dvořák loudest 10%: -6.1 and -3.5.
- Softest 30%: 100-250 Hz -6.1 dB, against Dvořák's -8.2.
- So the mix runs backwards from the recording, about 3 dB thin when loud and 2 dB heavy when soft. The loud share is also under both Brahms whole-piece shares (-8.75, -7.55).
- The timpani give 41% of the 120-250 Hz energy in bars 105-120 and 40% in 305-320, as much as the celli (42-43%). The basses give 8-9%. Brass are not among the top five contributors in any band in these tuttis.
- Cause (read): the port dropped Movement I's qn-keyed `loud_eq` points (mix.json `_doc`), which were Movement I's fix for the same problem (mockup-kit LEARNINGS section 14, c16).

Fix: add `loud_eq` entries in `build/mix.json` with Movement I's bands. Use scherzo points that ramp the wet over 2 qn: [[298,0],[300,1],[358,1],[360,0],[898,0],[900,1],[958,1],[960,0],[982,0],[984,1],[1015,1],[1017,0]]. The bands:
- Violoncellos: bell 150 Hz +6 dB, 1 oct.
- Double basses: bell 160 Hz +6, 1 oct, plus bell2 98 Hz -4, 0.5 oct.
- Bassoon 2, Contrabassoon, Bass trombone, Tuba: bell 140 Hz +3/+4/+4/+4.
- Timpani: none. Do not add the timpani's +3: they already carry 40%.

Target: loudest-10% 100-250 Hz share -7 to -6 dB, with the soft frames unchanged within 0.5 dB and the summit (bar 337) still the loudest bar. Inferred, for the actor's next look: the printed hard sticks (MANUAL-GAPS #6, `Timpani Hrd KS.oib`, same keys 24-28) would move the timpani's weight from boom to attack and leave the body to the strings.

### 3. The violas' div. upper voice is louder and narrower than the section it splits from (bars 209-224, qn 624-672; Violas div on DIV B, Violas)

What is wrong: in the div. bars one viola section plays two voices. The upper half (DIV B, Close only) is 3-7 dB louder than the full section on the lower voice, with a narrower, drier image, so the violas sound like a soloist group in front of a distant section. A half section should match or sit just under the other half.

Evidence (measured, stem RMS per two bars): Violas div minus Violas is +2.9, +4.6, +7.2, +3.5, +3.9, +4.6, +5.4, +4.7 dB; over the span -39.5 against -44.0 dB. L/R correlation is 0.79 against 0.56, and 0.85 against 0.68 at 2-8 kHz. Both share the same seat (R-L +2.7 and +2.5 dB), which is right. Read: Violas div gain_db +6 against the section's +2, only the Close channel loaded (manual p.139: the spread comes from the Main tree), width 0.3. In bars 349-356 the two are already close (-53.5 against -52.0 dB).

Fix: in `build/mix.json`, set Violas div `gain_db` 6 to 2 and `width` 0.3 to 0.45. The width change needs a full rebuild of that track. Target: the div track within -2..0 dB of the Violas stem in every two-bar window of 209-224, and correlation 0.65-0.70. If the gain cut leaves 349-356 too low, give it back there with a role (`build/roles.json`, Violas div, +2 dB at 1044-1068).

### 4. The bass is nearly mono, so the hall loses its width at the bottom (whole movement; Double basses, Timpani, Bass clarinet side shelves)

What is wrong: below 120 Hz the master is almost mono, while a hall recording is decorrelated there. On headphones the basses and the hall's low end sit as one point in the middle of the head, and the true-stereo hall's envelopment stops at the cello register.

Evidence (measured, master L/R correlation, frames within 50 dB of the loudest):
- Mix: 0.91 at 25-60 Hz, 0.88 at 60-120 Hz, 0.61 at 120-250 Hz. Side/mid -12.9 and -10.8 dB in the two lowest bands.
- Dvořák: 0.45 and 0.56; side/mid -4.2 and -5.0 dB.
- The kit's lossless Brahms references: about 0.60 under 120 Hz (mockup-kit LEARNINGS section 12, c19).
- Cause (read): the side-only low shelves taken from Movement II c33, Double basses 100 Hz -15 dB and Timpani 150 Hz -9 dB. In Movement I, -6 dB gave 0.88/0.71 ("more mono than the references") and -2 dB gave 0.71/0.75/0.56 (kit section 12, c20-c21).

Fix: in `build/mix.json`, set the Double basses `side_shelf` lowshelf 100 Hz from -15 to -4 dB and the Timpani side shelf 150 Hz from -9 to -4. Leave the 170 Hz side bells. These are post-Opus ReaEQs, so a `--mix-only` write is enough if it covers side_shelf; otherwise rebuild the track. Target: master 0.65-0.75 at 25-60 and 60-120 Hz, with the basses' seat within 1 dB (R-L +7.5 dB at 1-4 kHz now). Inferred: Movement II's -15 dB was set for its own sustained low pedal. This score's bass is mostly pizzicato and short.

### 5. Staccato winds and trumpets fill their own gaps, so the repeated notes run together in the hall (S1; bars 29-44, 101-120, 301-320; Flute 1, Oboe 1, Trumpets 1-2)

What is wrong: the strings' Stac rows stop and let the hall ring between the theme head's repeated eighths. The winds and trumpets play printed staccatos as sustain samples cut at 50-79% of the value, so each release runs into the next attack. A listener hears one long note with a wobble, not two strokes, and the hall sounds blurred in the tuttis.

Evidence (measured, dip between same-pitch repeats, 10 ms frames, median):
- Violins I theme 13-28: 7.0 dB on the stem, 3.8 on the master.
- Flute 1 counterstatement 29-44: 2.3 dB stem, 1.2 master. Oboe 1: 4.2 stem, 1.2 master.
- Trumpet 1 at 101-120: 3.5 dB stem (p10 1.9), 2.4 master. Horn 1 in the same bars: 8.3 dB.
- The trumpets' printed staccato quarters and eighths (qn 312, 313, 313.5, 314 ...) are Sus Non Vib MAX notes of 0.72, 0.395, 0.25 and 0.575 qn (parts.json).
- The wind and trumpet hall tails are not wetter than the horns' (drop at +0.3 s: trumpets 15.0/11.7 dB, horns 10.8-13.3, woodwinds 11.5-14.9), so the problem is the note shape, not the send.

Fix (shared with lens A): give the printed staccatos the staccato rows (MANUAL-GAPS #1). Use `ART_SPANS` with `"mark": "staccato"` on Flute 1-2, Oboe 1-2, Cor anglais and Clarinets in bars 13-56, 253-288 and 305-336, row "Stac DblTng RRx9". For Trumpets 1-2, use the same row (present in the 1TP KS Master, read in `jobs/15_1TP_KS_Master.b64`) at 300-360 and 900-960. Set `STAC_LEAD_S` 0.03 for these tracks, as Movement I c39 did. Target: 4-7 dB stem dips and at least 3 dB master dips at the repeats, with no level change over the phrase of more than 1 dB.

### 6. Paired players have different widths, so a unison or a pair in thirds shows as two images (Clarinet 2, Trumpet 2, Contrabassoon)

What is wrong: the solo winds were narrowed to width 0.05 (Movement I c25). Clarinet 2 and Contrabassoon have no width key, so they take the wind group's 0.5. Trumpet 2 takes the trumpet group's 0.3. In the trumpets' unison repeated quarters and the clarinets' thirds, the second player smears across the stage beside a point-source partner.

Evidence (measured):
- Stem L/R correlation: Clarinet 1 0.67, Clarinet 2 0.52; Trumpet 1 0.78, Trumpet 2 0.58; Contrabassoon 0.32, the lowest of any wind.
- Trumpet image at 1-4 kHz: Trumpet 1 +2.8 dB R-L, Trumpet 2 0.0 dB, with seats 0.07 and 0.12. The pair lands about 3 dB apart.
- Opus channel pans (read): Clarinet 2 [-0.70, +0.30], Trumpet 2 [-0.18, +0.42], Contrabassoon [-0.25, +0.75].

Fix: in `build/mix.json`, set `"width": 0.05` on Clarinet 2 and Trumpet 2, and 0.15 on Contrabassoon (it has side-shelf bass control already). This needs a full rebuild of those three tracks. Target: Clarinet 2 and Trumpet 2 correlation within 0.1 of their partner, and R-L images 1-4 kHz within 1.5 dB of the partner at their seats.

## Also measured, no action needed

- The G.P. at bar 340 (qn 1017) rings into the silence. The final chord's body is about -12 dB. After the brass release (243.38 s) the master falls 17.5 dB by +0.3 s, 23 dB by +0.6 s, about 30 dB by +1.0 s and 45 dB by the downbeat of bar 341. That is within the kit's recorded 13-17 dB at 300 ms. The hall decays smoothly into the silence with no cut.
- Sub. p at bar 121 (qn 360): the master eases from -21 dB (qn 357-358) to -29..-30 dB through 358-360, with no dip below the p level. There is no glitch from the hall being cut (S3); whether the contrast is big enough is for the dynamics lens.
- Violins II con sord (bars 168-196, CC15 on 393.85-552.5): 2-6 kHz re 250-2000 Hz is -12.7..-15.5 dB, against -4.6..-6.0 dB open at the same register (bars 121-128, 197-224). The mute is audible as colour.
- Loop pulsing on the held notes long enough to test (Violins I 1089-1125, horn drone 456-504, Hn 1 1110-1128): autocorrelation at 3.95 s was -0.26..+0.12 for the stem band and centroid, and at most 0.30 on the master. The other held notes are under 6 s at these tempos.
- Harp harmonics (445, 451): left of centre at R-L -3.1 to -3.5 dB, against the E6 of Violins I at -7.8. The harmonics enter 0.2 s after the violin's release (-64.6 dB at qn 445) at -42.8 dB. The harmonics sound at E4-B4, as written with `\transposition c''`.
- Stage layout at 1-4 kHz (R-L dB), coherent left to right: Vln I -8.3, harp -8.7, horns -5 to -7, Vln II -3.6, flutes -4, clarinets -2.5, timpani +0.5, violas +1.5, oboes +3.9, trombones +4.4, celli +5.9, tuba +6.8, basses +7.5.

Do not touch: the shared true-stereo hall (one IR, fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends scaled by mic volume), the seats above, the string sends (0.25), the woodwind send 0.6 group setting, the harp env_sustain 1.0 / release 200 ms, Violins II's CC15 window, and the tail holds that let the G.P. and the rests ring.
