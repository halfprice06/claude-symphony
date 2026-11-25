# Cycle 7, critic B (balance and levels): the c06 EastWest template mix

Under review: the c06 render (`cycles/c06/render/`, 31 dry stems plus the four return stems 32-35; `00_Master.wav` is their plain sum, and the delivered mp3 adds `master_eq` in `deliver_master.py`). Data: `build/parts.json` (identical to `cycles/c06/actor_scripts/parts_c06.json`), `build/mix.json`. The coordinator asked for three checks: the balance after the switch, the brightness (simulate halving the family shelves), and values for Movement I's new defaults (Duc's sends; the basses' 205-250 Hz cut).

Method. Every stem was transformed (mono mean as in `measure.py`, 8192-point Hann STFT, hop 4096) and summed back into a simulated master, so a scenario that changes an EQ or a send is exact for the dry stems. EQ changes were applied as RBJ biquad responses. A family-EQ change on a return is also exact, because every input of R Strings, R Brass and R Winds carries the same family EQ. Duc's sends change only part of the R Strings input, so they were simulated in the power domain: each string stem's power per 1/6-octave band was smoothed with a 3.3 s decay, Vc/Cb's share of the R Strings input was computed per frame and band, and that share was scaled by the new send (short-note frames from the parts.json keyswitch rows). The simulated base reproduces `metrics.md` band shares within 0.5 dB, and the 6-20 kHz figures below are shifted onto the `measure.py` scale. Balance is A-weighted, as in `bal06.py`, on the dry stems and on dry plus returns. For the second, each return is split between its family's tracks in proportion to their dry level. Reference band shares: Dvořák 9/i (lossy MP3), Brahms 1/ii and 4/ii (`metrics.md`). Scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c07-B/` (deleted).

## Manual notes (second reading of row c1 B: PDF pages 137, 140, 150-151; cycles/c01/reports/B.md re-checked; MANUAL-GAPS.md read)

| Manual (May 2021 HO, PDF page) | Where it applies now | Followed? |
|---|---|---|
| p.137: each KS Master row has a load button and a volume knob. | Row loading by `load_articulations()`; row level differences (tremolo rows, Trumpet 1 Mute Sus). | Yes. c01's tremolo and mute row offsets are handled in the envelope (`ROW_GAIN_DB`, roles). c01 and Movement I c36 avoided the row knob because it also scaled the Opus hall send. With the Opus hall off (c06) that no longer applies, but the envelope stays the right place: it survives a rebuild and can vary per note. Not re-measured this cycle. |
| p.140: the master channel gain sets the output without changing the mic mix; the pan keeps the mics' relative pans. | c06 seats: Close panned to the seat inside Opus (`pan_by_mic`), Main full width, REAPER `track_pan` after the plugin. | Yes. Opus master pan stays centred and the seat lives in the Close pans plus the small REAPER pan, which is what the manual describes. |
| p.150: velocity selects the sampled layer and is used mostly on shorts. | Pizzicato and staccato rows; c07's plan item "string shorts: CC parked high, dynamics by velocity". | Partly. c01 #5 (soft trim stacked on a pp layer that velocity already chose) was fixed by roles. When c07 moves shorts to velocity dynamics, `soft_trim_db` must not be added on top of the velocity layer again. |
| p.151: CC7 sets each track's ceiling, CC11 shapes the line; send the CCs before the first note. | Track levels in the REAPER volume envelope; the pre-roll carries the first CC values. | Yes, and the c06 routing changes one consequence. The REAPER envelope now comes before the post-fader sends, so an envelope drop no longer cuts the hall tail: the tail keeps ringing on the return track. Measured at the sfp at qn 592 (592.0-593.25 against 591.0-591.5): Violins I -3.6 / -9.2 / -5.8 / -8.1 / -13.1 dB per quarter, R Strings only -0.5 / -1.6 / -1.4 / 0.0 / -1.0 dB. BRIEF S3's "never a fast fall in the volume envelope" was written for the in-plugin hall. For the dry sound it still matters; for the tail it now matters less. |
| MANUAL-GAPS #4 (Mid mics on the winds) | The template's Close-led winds make the winds the driest family (finding 5). | Open, unchanged. |

## 1. The strings return carries more 80-320 Hz energy than the dry strings and makes up over half of the master's low mids (measured)

Where: the whole piece; worst in the low tuttis (bass theme bars 27-34, ending 271-279, chorale 223-234). Tracks: R Strings, fed from Violins I-Double basses at -5.56 dB post-fader. The template's return EQ high-passes at only 87 Hz (`STRING_VERB.txt` band 0, bw 2.64 oct).

Evidence (measured, stereo power L²+R² over the whole piece): R Strings minus the five dry string stems is +2.9 dB at 80-160 Hz and +2.4 dB at 160-320 Hz, then -1.0 dB at 320-640 and -2.5 dB at 640-1280. In the mono sum, R Strings is 56 % of the master's 120-180 Hz energy, 52 % of 180-300 Hz and 36 % of 60-120 Hz. That is more than the celli and basses together (9.3 + 3.7 % at 120-180 Hz). By passage, R Strings minus dry strings at 80-320 Hz: bars 27-34 +4.0, 223-234 +3.2, 271-279 +5.0 dB. The master's 100-250 Hz share is -5.6 dB, against -6.6, -8.8 and -7.6 in the three references. Until c05 the Opus hall had a 160 Hz low cut (BRIEF, Dan's "too wet ... mushy" note). Movement I c44 measured that cut taking 0.8 dB off the loud passages' 100-200 Hz (mvt1 LEARNINGS 2026-11-07). The template mix removed that cut. Wet against dry, A-weighted, whole piece: strings -4.2 dB, winds -8.9, brass -10.1. In the soft pizzicato bars 51-66 the strings' return is only 1.9 dB under their dry sound.

Fix (two parts, both simulated on the c06 stems; finding 2 gives the send values):
- Duc's sends (finding 2) alone: R Strings -1.6 dB below 250 Hz, master 100-250 Hz share -5.6 -> -6.2 dB.
- A 160 Hz high-pass on the R Strings return: in `tools/build_reaper.py returns_job`, after pasting the chunk, set band 0 (the ReaEQ high pass) of the return's first FX to 160 Hz with `set_by_fmt`, and read it back. Drive it from a new mix.json key on the return entry, `{"name": "R Strings", ..., "hp_hz": 160}`. R Brass and R Winds can keep the template's 100 Hz: adding the same filter there changed the master's 100-250 Hz share by less than 0.1 dB.
- Together: R Strings minus dry strings at 80-320 Hz goes +3.4 -> -0.6 dB (27-34: -0.3, 223-234: -0.2, 271-279: +1.6). The master's 100-250 Hz share goes to -7.4 dB, inside the reference range. 250-500 Hz is unchanged and the A-weighted master falls 0.6 dB.
- Side effect to check on the render (measured in the mono sum): the master's 80-100 Hz rises 2.5 dB with the high-pass, because the return's delayed low end had been partly cancelling the dry basses there. Check 60-100 Hz in the loud bars against c06. If it rises more than 2 dB in stereo, try 140 Hz.

## 2. Duc's sends: values and simulated effect (measured by simulation; the per-note route is inferred to be feasible)

Values, in this mix's send levels (Duc's levels are relative to his violin send, which here is the strings' -5.56 dB):
- Violins I, Violins II, Violas: R Strings -5.56 dB (Duc 0 dB, unchanged).
- Horns, trumpets, trombones, bass trombone, tuba: R Brass -8.77 dB (Duc 0 dB, unchanged).
- Violoncellos and Double basses, long notes: R Strings -7.16 dB (-1.6).
- Violoncellos and Double basses, short notes: R Strings -12.56 dB (-7.0). Duc applies -7 to his cello and bass short patches (LOTR: "Cello CSS shorts" and "Bass CSS shorts" -7.0, `duc-mix.txt`). Here that means the rows "Stac RRx9" and "Pizzicato RRx4" (Vc: 37 + 62 notes) and "Staccato RRx9" and "Pizz RRx4" (Cb: 13 + 60 notes).

Simulated effect: R Strings A-weighted -0.5 dB, below 250 Hz -1.6 dB. Master 100-250 Hz -0.9 dB absolute (share -5.6 -> -6.2), A-weighted -0.03 dB. The short-note send matters only in the pizzicato passages: R Strings 80-320 Hz falls 2.9 dB in bars 51-66 and 4.4 dB in bars 171-186 with the -7 dB shorts, against 0.9 and 1.3 dB with -1.6 dB on every note. Those are the soft accompaniments under the Trumpet 1 solo and the muted trumpet with cor anglais, where a wet bass pizzicato blurs the pulse. Also sending Vc/Cb Sus-row notes of 0.6 qn or less at -7 (the hammered eighths) takes bars 199-210 from -1.5 to -3.2 dB. Duc's own patches do not cover this case, so it stays optional.

Implementation (file: `build/mix.json`, `tools/score_to_parts.py`, `tools/build_reaper.py`): a track-level `"return": {"to": "R Strings", "db": -7.16, "short_db": -12.56, "short_rows": ["Stac", "Staccato", "Pizz"]}` on Violoncellos and Double basses. `score_to_parts.py` writes a `send_db` lane `[[qn, db], ...]` that steps to `short_db` 0.03 s before each short-row note and back 0.03 s before the next long note. `build_reaper.py set_sends` writes the lane as the send's volume envelope (`GetTrackSendInfo_Value(tr, 0, k, "P_ENV:<VOLENV")`, points through `ScaleToEnvelopeMode`) and reads it back. A step while no note is sounding is inaudible, because the reverb already in the return keeps ringing (Manual notes, p.151 row). If the envelope route fails, apply -1.6 dB to every Vc/Cb note first: it gives most of the low-band gain (whole piece -1.5 dB below 250 Hz).

## 3. Halving the family shelves removes only 0.9 dB of the excess brightness; the delivered mp3 is 1.4 dB brighter than the master the metrics measure (measured)

Where: the whole piece, mostly the brass tuttis. Share of the master's 6-20 kHz energy: Trumpet 1 19.7 %, Violins I 13.3, Trombone 1 11.9, Trumpet 2 10.8, crash 8.7, Trombone 2 7.6, Trumpet 3 6.2, Violins II 5.9, bass trombone 5.6. Trumpets and trombones carry 62 %. The returns carry almost nothing above 6 kHz (low-passed at 5.6 and 8.5 kHz).

Evidence (6-20 kHz share, `measure.py` scale; Dvořák -28.8, Brahms -32.2 / -32.3):
- `00_Master` as rendered: -25.1. Strings, brass and winds shelves halved: -26.0. All three shelves removed: -26.9. So the shelves account for less than half of the 3.7 dB gap to Dvořák.
- The delivered file has the master EQ (-1.9 dB at 1.18 kHz, -1.6 at 167 Hz, +0.8 shelf at 8 kHz): -23.7 now, -24.6 with halved shelves. The metrics compare `00_Master`, so they understate what Dan hears by 1.4 dB.
- Top band minus 500-2000 Hz, which does not move when the low end changes: c05 -25.4 (the same as Dvořák's -25.4), c06 master -20.7, c06 delivered -19.2. Against Dvořák in third octaves the master is +2.6..+3.8 dB from 4.6 to 14.5 kHz and -4.2 / -3.4 dB at 453 / 905 Hz. The brightness is half treble and half the scoop that the family mid cuts (strings -5 dB at 1 kHz, brass -9.8..-11.2 dB at 450-1000 Hz) and the master's 1.18 kHz cut leave in the mids.
- The Brahms references are two slow movements with little brass. For a brass-led finale the Dvořák allegro is the better target, about -28.5 to -29 delivered.
- The strings shelf is not resonant (measured, against c06 critic B's inference). Modelled as an RBJ shelf at the stored 0.33 octaves, it would put -5.4 dB at 4 kHz and +9.4 dB at 5.5 kHz. The rendered Violins I/II, Violas and Violoncellos spectra fall smoothly through 3.4-6.1 kHz, with no dip or peak. Dividing that resonant shape out of them produces a 6-7 dB cliff at 4.8-5.4 kHz, which no real string spectrum has. So ReaEQ does not build its shelf the RBJ way from that bandwidth value. Simulations that model ReaEQ shelves with `biquad_h` (as `deliver_master.py` does for `master_eq`) are approximate for shelves; the master shelf at 1.39 octaves is a gentle one either way.

Fix:
- `build/mix.json` groups `family_eq`: strings hshelf 4730 Hz +4.0 -> +2.0 (keep bw 0.33); horn, trumpet and lowbrass hshelf 7490 Hz +4.0 -> +2.0; wind hshelf 7590 Hz +5.1 -> +2.55. Leave harp (+8) and timpani (+4.5): including them changed the 6-20 kHz share by 0.01 dB.
- `build/mix.json master_eq`: remove the 1.18 kHz -1.9 dB bell (it deepens the mid scoop) and replace the 8008 Hz +0.8 dB shelf with 6000 Hz -3.0 dB (bw 1.39). Simulated delivered file with halved shelves: 6-20 kHz -27.6, 2-6 kHz -9.9 (Dvořák -10.5), 500-2000 Hz -3.9 (Dvořák -3.5), top minus mids -23.2. If the c07 delivered file still measures above -28, use 5000 Hz -4.0 (simulated -29.2, top minus mids -24.8). This needs no REAPER time: `deliver_master.py` can be run on the c06 master first.
- `tools/measure.py`: also report the band shares of the delivered file. Today the shares are computed on `00_Master`, before `master_eq`.

## 4. The basses' 205-250 Hz cut works against the basses' own +4 dB bell at 180 Hz: move the bell down and add the cut (measured)

Where: Double basses, all bars, most in 27-34 (bass theme), 199-210 and the loud_eq spans. The track's static EQ is bell 180 Hz +4 dB (1 oct), the 87.3 Hz notch, the strings HPF 53 and the 456 Hz bell. The loud_eq adds 160 Hz +3 dB in ff spans. Net now (static / with loud_eq): +2.9 / +5.8 dB at 150 Hz, +3.7 / +6.4 at 180, +3.2 / +5.2 at 205, +2.5 / +4.1 at 225, +1.7 / +2.8 at 250. Duc's cut sits on the upper half of a boost this mix already makes.

Simulated on the Cb stem (Duc's Q 1.02 = 1.39 oct):
- 243 Hz -2.4 dB (Duc's longs, Mahler): Cb A-weighted -1.5 dB; 180-250 Hz -2.0; 125-180 -1.1.
- 249 Hz -3.6 dB (LOTR longs): Cb A -2.2; 180-250 -2.9; 125-180 -1.5; 80-125 -0.8.
- Recommended, bell 180 -> 150 Hz +4 dB (1 oct) plus 240 Hz -3.0 dB (1.39 oct): 40-80 Hz -0.05, 80-125 +0.1, 125-180 -0.4, 180-250 -3.8, 250-350 -3.0, 350-500 -1.5; Cb A -2.25. Net static response: +2.2 dB at 150, +0.7 at 180, -0.8 at 205, -1.6 at 225, -2.1 at 250, -2.4 at 280. The fundamentals and the 125-180 Hz body stay where they are; the cut lands in Duc's 205-250 Hz.
- On the master the cut is small, because the basses are only 9.9 % of 180-300 Hz (R Strings 52 %): -0.2 to -0.3 dB at 180-300 Hz. It changes the basses' own colour more than the mix's low mids. Finding 1 is the bigger low-mid change.
- Role check: Cb minus Vc in bars 27-34 -2.7 -> -4.4 dB, 199-210 -6.7 -> -8.9, 223-234 +0.6 -> -1.8. The bass theme at 27-34 against Violins I+II with returns: 3.2 dB now, 3.6 with findings 1-4 together.

Fix (`build/mix.json` tracks "Double basses"): `eq` bell `hz` 180 -> 150 (keep +4 dB, bw_oct 1.0). Add the cut through a track-level `family_eq`, because `set_eq`'s ReaEQ has no free bell (bell and bell2 are taken). Copy the four string bands and add `{"type": "bell", "hz": 240, "db": -3.0, "bw": 1.39}`. `reaeq_b64` writes any number of bands; check the 5-band read-back (0 mismatches). Leave the loud_eq 160 Hz +3 dB as it is. No make-up gain: the level lost is in the 180-350 Hz band Duc means to thin. Check on the render: Cb minus Vc at 27-34 no lower than -4.5 dB, and the master's 125-180 Hz within 0.5 dB of c06 in the loud bars.

## 5. Every balance target was met on the dry stems, but the returns favour the strings, so the heard margins are 0.5-1 dB smaller (measured)

The c06 targets were checked on the dry stems (`bal06.py`). Re-measured with the returns added (A-weighted; dry, then dry plus returns):
- Trumpet 1 solo bars 51-66 against the rest: +4.3, then +3.5 (target at least +4). The pizzicato strings' return in these bars is only 1.9 dB under their dry sound.
- Brass against strings, chorales 223-234 / 255-264: +6.1 / +6.2, then +5.3 / +5.2 (target +5..+6).
- Bass theme bars 27-34 against Violins I+II: +3.8, then +3.2.
- Muted Trumpet 1 against the cor anglais, 171-186: -2.6, then -3.1.
- Trumpets, theme B 211-218, against everything else: 0.0, then -0.4.
- Bassoon 1 solo 115-122 against the rest: +4.3, then +3.9. Violins I+II F2 67-82 against the rest: +1.0, then +1.1. Harp against Violins I 123-134: +1.4, then +1.5. Horns against heavy brass 223-234: -4.6 both ways.
- Whole piece: winds minus strings +2.5, then +1.6; brass minus strings +4.6, then +3.6.

All the recommended changes together (findings 1-4) leave these within 0.3 dB, except the bass theme, which rises to +3.6, and the chorales, which rise to +5.6 / +5.5.

Fix: measure the critics' balance targets on dry plus returns from c07 on (`bal06.py`: add each return's level, split by family share). Trumpet 1, bars 51-66: a +0.7 dB role in `build/roles.json` (qn 200-264, step in at the solo's first note and out at its last). That brings the solo back to +4.2 with returns. Everything else is within its target.

Do not touch: the template return chunks, pre-delays and the brass/wind/perc send levels; the violins', violas' and brass sends (Duc 0 dB); the c06 make-up gains with their stem-fix corrections (every dry-stem target met: horns -4.6 / -4.9 under the heavy brass, harp +1.4 over Violins I, timpani 13 % of the ending's 30-150 Hz); the harp HPF 80 and the reduced timpani EQ; the basses' 87.3 Hz notch and mute_eq; the Violins I 5 kHz and trombone 4 kHz cuts; the per-dynamic string release caps; the climax order (223 and 278 loudest).
