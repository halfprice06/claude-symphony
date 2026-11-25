# Critic C, cycle 49: blend and space (render c48)

Render under review: c48 as delivered (`cycles/c48/render`, 40 stems; master = float sum of the stems; `rendered_build/parts.json` and `build/mix.json`). Compared with c47 where a change needed isolating. Reference recordings: the Dvořák 9/i MP3 (decoded and measured with the same scripts) and the stored rtk metrics of Brahms 1/i, 4/i, 1/ii and 4/ii (`symphony/render/critics/c00`, `c04`). Method: STFT 4096 / hop 2048 at 48 kHz, ten bands (20-60 ... 8-16k Hz), L, R and cross power per frame, plus a 10 ms envelope per stem. "Loud" means the top 10% of active frames, "soft" the bottom 30%. rtk's `cutoff_decays` was copied without scipy. The scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c49-C/`, deleted at the end. Each judgement is marked measured, simulated (STFT-domain change to one stem, re-summed) or inferred.

## Manual notes (cycles 48-51 rule: pages chosen for this lens's open problems, read in full: 2021 manual PDF pp. 100-103, 118-120, 138-139, 141, 220-222; MANUAL-GAPS.md and DIGEST.md read)

| Page | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| p.100 | Brass is recorded with "the same variety of microphone positions" so that it blends "into a unified sound" with the other libraries | Trumpets, horns and low brass on Close + Main, like the other families | Partly. Close + Main are used everywhere, but the coda Trumpets a2 (2TP patch) is brighter and roomier than the 1TP solo trumpets it plays beside (finding 3). |
| p.101 | Brass sustains: the Mod Wheel (CC1) crossfades 4 dynamic layers | The a2 trumpets' ff in bars 167-170 | Followed. The brightness in finding 3 is in the body at the printed ff, not in an accent front (accent fronts measured -0.1..-2.2 dB re body in 2-5 kHz). |
| p.102 | Shorts have no release trails, only the room at the end of the sample; hold the last short note so the room rings | Staccato aliases and fugato | Not re-measured (lens A). |
| p.103 | Brass "Repetitions" patches do have release trails | Not used | — |
| p.118-119 | 18in Zildjian Sus Cymbal Cresc: crescendo-sustain rolls that "ring out", "very little coloration" in the upper range, 2 velocity layers. 22in K Crash: "grandiose", marching-band timbre | Suspended cymbal bar 159 into the 636 stroke; the Crash track only rings softly under it | Followed. Both cymbals sit in the shared room (stem correlation 0.68-0.71 and side/mid -6.9 / -7.6 dB, the same as the tam-tam's 0.69 / -7.4). At bar 160 they hold 18% and 12% of the master's 8-16 kHz, against Trumpet 1's 31%. Nothing sticks out (measured). |
| p.138 | Close = presence; Main = fifth row, Decca tree plus outriggers, "big, unified sound"; Surround adds "dimension and depth" | Mic mix of every section | Followed for depth. Still short on width (finding 1). The DIGEST's factory Solo Trumpet mix is Close 0.25 / Main 0.47 / Surround 1.0. The mockup's Close 0.5 / Main 1.0 keeps the factory Close-to-Main ratio and drops only the Surround mic. |
| p.139 | Each mic sub-mix has its own volume, **panning**, load and mute | Per-mic pan | Followed since c45 (`width_by_mic`, Main 0.35 on winds and brass). Read back from the built states in `jobs/*.b64`: wind Close at seat ±0.05, Main at seat ±0.35; strings Close and Main both at seat ±0.5. |
| p.141 | Stereo Double widens the image (stereo routing only) | — | Not used, correctly. Widen with the recorded Main pair and the hall's Width first (finding 1). |
| p.220 | Reverb insert: true stereo, IR envelope, Bandpass, **Width 0-200% (default 100%)**, Wet/Dry | Shared hall | Followed except Width: true stereo, envelope, low cut 160 Hz and high cut 5.5 kHz are all set. Width is still at 100%. It is the untested fallback from c45 / c46 (finding 1). |
| p.221 | IR envelope, Full mode: start, end, fade times and curves | `ir_setup` {2, 0.5, 0.5} | Followed. The hall verdict below says keep it. |
| p.222 | Mixing ranges from "small and dry" to "large and wet"; the room "is heard as long as the samples are playing (including the release trail samples)" | Per-track trail gain | **Now the cause of a seam.** Violas `rt_gain_db` -6 removed their recorded room. At every tutti stop they now fall faster than any other string section (finding 2). |

Open MANUAL-GAPS items in this lens: #4 (Mid mics on the woodwinds) stays deferred. At the common tutti stops the winds' decays are not drier than the strings' (measured: +0.3 s drops of -0.5..-10.8 dB for the winds against -2.4..-12.7 dB for the strings at the bar-26 and bar-138 stops), so there is no depth inversion for Mid to fix. #3 (Hollywood Solo Cello) is still not installed; see finding 5.

## Coordinator's checks

- **Hall: keep fx_volume 0.095. It is not too dry and not mushy (measured).** On rtk's own detector the c48 master shows 4 tutti stops (bars 14, 26, 46, 138):
  - time to -20 dB: 0.46 / 0.54 / 0.53 / 0.48 s. Brahms 1/i: 0.43-0.55 s (median 0.485). Dvořák: 0.49-0.55 s.
  - RT from the -5..-20 dB slope: 0.85 / 1.19 / 1.67 / 1.06 s. Brahms 1/i: 1.13-1.62 s (median 1.33). Dvořák: 1.32 s.
  - So the time to -20 dB sits inside the recordings' range and the early slope is at their dry edge, as in c45 and c47.
  - Final chord (actor, c48): master -20 dB at 0.53 s, inside the references' 0.48-0.79 s.
  - **Recommendation:** no change. The 0.12 fallback is for Dan's ear only, if he calls this render dry.
- **Mush in the low mids: none (measured).**
  - 250-500 Hz share of the whole file: -6.4 dB (Dvořák -6.5). Loud frames: -6.8 dB (Dvořák -6.7). Soft frames: -5.1 dB (Dvořák -5.6).
  - Relative to 250 Hz-2 kHz, 250-500 Hz is at most 1.6 dB over the Dvořák's soft frames. That happens in the A-flat second theme (bars 47-58: -3.1; bars 147-155: -2.9; Dvořák soft -4.5) and nowhere else.
  - Loud passages remain *short* of 100-250 Hz (bars 158-161: 100-160 / 160-250 Hz at -13.8 / -12.4 dB re 250 Hz-2 kHz; Dvořák loud -9.2 / -5.7). This is c45's voicing finding. Leave it.
- **Low end in the soft passages and the final chord, with the c48 basses releases (measured).** 20-100 Hz re 250 Hz-2 kHz, c47 (no pp cap) -> c48 (450 ms up to qn 695.8, 600 ms after):

  | Span | c47 | c48 |
  |---|---|---|
  | Bars 5-7 | -19.3 | -15.5 |
  | Bars 42-46 | -21.0 | -20.5 |
  | Bars 57-58 | -20.1 | -20.0 |
  | Coda bars 176-178 | -17.1 | -16.5 |
  | Final chord | -16.0 | -16.1 |

  - Dvořák soft frames: -14.3. Every span stays under it.
  - The bars 5-7 rise comes from c48's B #1 (+4.7 dB on the basses' pp octave), not from the cap.
  - The basses' tail 0.4-0.6 s after their soft pizz. and arco phrase ends sits 27-41 dB under the master.
  - The final chord's low band did not change, so the 600 ms cap adds no build-up.
  - **From this lens, accept 600 ms everywhere** (the rebuild default). It adds no low end, and it avoids a separate coda-only basses instance with its own round robins. Whether the 4-versus-7 failing chord changes matter is lens A's call.
  - Do not raise the bars 5-7 basses any further: at -15.5 they are 1.2 dB under the Dvořák's soft frames.
- **Long timpani rolls (measured).** Every roll sits under the master: 8-19 dB in bars 2-3, 11-14, 41-43, 62-63, 76, 143-145, 174 and 182. In bars 1 and 4 (the solo opening) the timpani lead. No roll drowns a part.
- **Item 7, loop pulse (measured on the master).** 100-250 Hz level and centroid autocorrelation at 3.95 s:
  - final chord +0.07 / +0.05 (controls at 2.6 / 3.3 s: -0.04..+0.04);
  - Lento bars 1-6 -0.03 / -0.03;
  - sostenuto bars 122-125 -0.17 / -0.23;
  - coda bars 175-178 -0.19 / +0.19.
  - No pulse.
- **S3, bar 62 (measured).** The master falls -5.6 / -8.2 / -13.2 / -13.9 dB at +0.1 / 0.2 / 0.3 / 0.5 s, with no step inside the first 0.1 s. The hall still rings under the p.
- **S1 / S2.** Not re-measured here. See c48 CHANGES (median |pcX - ref| 30 ms on 108 rows).

## Findings, ranked by what a listener would gain

### 1. The image is still narrower than every reference between 250 Hz and 5 kHz, and the hall's own tail is too correlated. Test the hall Width (p.220) in pass 2 (measured problem; fix inferred, to be tested)

**Where.** The whole movement, loud and soft alike.

**Evidence (measured).**

| | Correlation < 250 Hz | 250 Hz-5 kHz | > 5 kHz | Side/mid |
|---|---|---|---|---|
| c48, all frames | 0.57 | **0.64** | 0.56 | **-6.3 dB** |
| c48, loud / soft frames | 0.59 / 0.55 | 0.65 / 0.62 | 0.59 / 0.45 | -6.4 / -6.0 dB |
| Dvořák (decoded) | 0.55 | 0.56 | 0.37 | -5.3 dB |
| Brahms 1/i, 4/i, 1/ii, 4/ii (stored, 250 Hz-4 kHz) | 0.54-0.62 | 0.47-0.54 | 0.38-0.48 | -4.7..-5.4 dB |

- The low band is now right, thanks to c45's per-mic width and the zeroed side cuts. The mid band is 0.08-0.17 more correlated than every reference, and side/mid is 1-1.6 dB narrower. c45's accept line (≤ 0.62 and -6.0 dB) is still missed.
- **Per stem, 250 Hz-5 kHz, while each plays:**
  - solo winds 0.84-0.91 (Bassoon 1 0.91, side/mid -12.1 dB);
  - horns 0.79-0.83, trumpets 0.76-0.78, Trombone 1 0.75;
  - Violas 0.75 (side/mid -8.2 dB), Double basses 0.73, celli 0.67, Violins II 0.65;
  - only Violins I (0.45) is as wide as a recorded section.
- **The hall tail itself is correlated.** In the master 0.6-1.2 s after each stop, where only the hall and a few held notes remain, the 250 Hz-5 kHz correlation is 0.34-0.59 (0.54 after the final chord). A diffuse late field from a spaced pair is normally much lower than that (inferred). The shared IR, `S. Cal Hall Perc TS FR 3.3s` at Width 100%, adds less spread than a hall would.

**Fix (pass-2 test, then generic).** This is the fallback that c45 wrote and nobody ran.
- `tools/build_reaper.py apply_mix()`, where the shared ConvolutionReverb insert is written: `rv["width"] = float(MIX["reverb"].get("width", 1.0))`. The state key is `width` (p.220: 0-200%, stored 0-2).
- Run the c44 hall-test kit (`cycles/c44/halltest/make_halltest.py`, send 1.0) at width 1.0 / 1.5 / 2.0.
- **Adopt 1.5 for the shared hall in `mix.json reverb.width`** if both hold:
  - the test tail's L/R correlation (0.3-1.0 s after the stop, 250 Hz-5 kHz) falls by 0.15 or more;
  - the tail's L²+R² level changes by 1 dB or less, so the decay verdict above stands.
- If 2.0 passes the same checks and 1.5 does not reach them, use 2.0.
- It is a hall-state change, so every track and pass-2 alias needs a full rebuild. Per-note level profiles keyed to the hall do not change if the tail level is held.
- **Accept on the master:**
  - 250 Hz-5 kHz correlation ≤ 0.60;
  - side/mid -5.8 dB or wider;
  - every seat (stem R-L) within 0.5 dB of c48, because a hall widening does not move dry seats;
  - time to -20 dB still 0.43-0.58 s.
- **Second step, only if the master is still over 0.60 after the Width change** (mix only, then a full rebuild of these tracks): `width_by_mic` `{"Main": 0.7}` on Violins II, Violas and Violoncellos, Close unchanged.
  - Expected effect (inferred from c45's step 2, where Main 0.45 took the celli from 0.87 to 0.67): Violas 0.75 -> about 0.62.
  - Check that each seat moves less than 1 dB. If a seat moves more, move it 0.05 outward.
- **Generic for every movement:** after drying the hall, measure the hall tail's own correlation. If it is over about 0.4, raise the insert's Width before widening any section's mics.

### 2. The violas stop dead at every tutti stop: their tail falls 5-13 dB faster than the other strings' at the same moment (measured; fix inferred)

**Where.** Every tutti stop where the violas play: bars 14, 26, 138 and the bar-170 fermata (master stops at 65.9 / 89.6 / 311.1 / 379.2 s). It also applies to every viola phrase end that is exposed.

**Evidence (measured).** Each stem's fall from its own level just before the stop, at the same instant:

| Stop | Violas at +0.3 / +0.6 s | Median of the other four string sections |
|---|---|---|
| Bar 14 | -10.1 / -29.6 | -4.5 / -22.3 |
| Bar 26 | -12.7 / -28.7 | -7.2 / -19.3 |
| Bar 138 | -18.7 / -35.7 | -5.6 / -21.3 |
| Bar 170 fermata | -12.3 / -27.3 | -7.6 / -21.7 |

- The violas fall 4.7-13.1 dB faster at +0.3 s and 5.6-14.4 dB faster at +0.6 s.
- Every other family stays within a few dB of the strings' median at these stops: one late room for everyone except the violas.
- Over all phrase ends, the violas' tail at 0.15-0.25 s is -17.3 dB re body (Violins I -12.5, Violins II -8.5, celli -11.6). At 0.8-1.0 s it is -47.9 (others -40..-46).
- They are also the narrowest string section (corr 0.75, side/mid -8.2 dB).
- **Cause.** The violas are the only track with `rt_gain_db` -6 (c45 / c46). p.222: the recorded room "is heard ... including the release trail samples". The trail cut removed the violas' share of the room after every note-off. The section's caps (150 / 350 ms) are the same as the other strings', so they are not the difference.

**Fix (mix only, then a full rebuild of Violas).** Keep `rt_gain_db` -6, which cleared the figures' pitch overlap (old pitch -6.2 -> -8.4 dB). Give back the room through the shared hall instead:
- In `build/mix.json` set Violas `"send": 0.35` (string group 0.25; +2.9 dB into the hall).
- c44 measured that halving the whole hall moved the détaché overlap point only 31 ms, so the hall is not what carries the overlap (inferred). The send should leave c46's overlap result standing.
- **Accept:**
  - at the four stops, the violas' +0.6 s fall within 3 dB of the other strings' median (now 5.6-14.4 dB faster);
  - the violas' figures' old pitch 70 ms into the next note still ≤ -8 dB;
  - the Violas' K level within 0.5 dB of c48 per bar where they play (if not, trim `gain_db`).
- If 0.35 leaves the stops more than 3 dB fast, use `rt_gain_db` -3 with send 0.3 (a pass-2 alias, `alias_check.py` against the main track first).

### 3. Coda, bars 167-170: the Trumpets a2 alias is 4-5 dB brighter than every brass partner and holds 29% of the master's 2-5 kHz and 8-16 kHz (measured; fix simulated)

**Where.** Trumpets a2 (2TP KS Master), qn 664.5-679, the ff unison with Horn 1 / Horns a2.

**Evidence (measured).**
- Band levels re its own 0.5-2 kHz, each part's loudest 15 dB of frames in the span:

  | Part | 2-5 kHz | 5-8 kHz | 8-16 kHz |
  |---|---|---|---|
  | Trumpets a2, coda | **-4.9** | **-19.9** | -32.3 |
  | Trumpet 3, same bars, ff | -9.4 | -27.3 | -39.9 |
  | Trombone 1, same bars | -12.6 | -25.0 | -34.1 |
  | Trumpet 1 at the bar 158-161 fff | -7.6 | -23.7 | -28.5 |
  | Trumpets a2 in the recap, bars 131-132 (f) | -15.7 | -36.2 | -50.4 |

- In the master the a2 holds -5.3 dB (29%) of 2-5 kHz and -5.4 dB of 8-16 kHz. The next part is Violins I at -6.4 / -7.4. The master's own 2-5 kHz re 0.5-2 kHz (-8.7) is normal (Dvořák loud -8.1), so the problem is one part's colour, not the total.
- **Why (from `mix.json`).**
  - The a2 track carries a +2.5 dB 4 kHz shelf (like every trumpet). Its `loud_eq` 3.2 kHz -4 dB bell covers only 519.7-525.7, the recap entry, where the a2 matches Trumpet 1 within 2 dB.
  - In the coda nothing tames it, while the Horns a2 in the same span get a 1.6 kHz -8 dB shelf.
  - The 2TP patch's trails also make it roomier than the 1TP trumpets beside it: early tail -12.4 dB re body against -16..-18 for Trumpets 1-3. This is c45's seam, still there.
- The accents are not the cause: 2-5 kHz in the first 80 ms minus body is -0.1..-2.2 dB at 665 / 670 / 673 / 676.

**Fix (mix only, `--mix-only`).** In `build/mix.json` Trumpets a2 `loud_eq`, extend the existing 3.2 kHz -4 dB (1.5 oct) spec's points with the coda span: `[..., [664.4, 0], [664.5, 1], [679.6, 1], [679.7, 0]]` (to the fermata's end).
- Simulated over 664.5-679, approximating the bell's shape: the a2's 2-5 kHz re 0.5-2 kHz -4.9 -> -6.6 dB; its master 2-5 kHz share -5.3 -> -8.3 dB; master 2-5 kHz re 0.5-2 kHz -8.7 -> -9.4 (still at the Dvořák's level).
- The a2's broadband level falls about 2 dB in this simulation. Check that the trumpet/horn melody stays over the violins' tremolo (lens B). If it drops below, add +1.5 dB to the a2 in that span as a role row rather than removing the bell.
- **Accept:** the a2 within 2.5 dB of Trumpet 3 in 2-5 kHz re 0.5-2 kHz, and the a2's share of the master's 8-16 kHz at -7 dB or lower.

### 4. The second-theme soft passages carry 1.4-1.6 dB more 250-500 Hz than a recording's soft frames. Watch it; change nothing yet (measured; judgement inferred)

- Bars 47-58 and 147-155: 250-500 Hz re 250 Hz-2 kHz -3.1 / -2.9 dB, against the Dvořák's soft frames at -4.5. Every other span is within 0.5 dB of it.
- This is the dolce celli / violas / horns register of the A-flat theme. It is small, and from one reference only.
- Do not cut it now. If Dan calls these bars thick, the first lever is a 300 Hz -1.5 dB bell (1 oct) on Violoncellos and Violas over 184-232 and 584-620 as a `loud_eq`-style wet span. Check that the celli's dolce line keeps its level.

### 5. The coda cello solo (DIV A, Close only) is a dry point source next to its own section. Acceptable for a soloist; one small optional change (measured; fix inferred)

- Cello solo (qn 680-696): stem correlation 0.96 at 250 Hz-5 kHz and side/mid -10.6 dB, against the celli section's 0.67 / -5.2. Its seat (R-L +4.6 dB) is close to the section's (+6.0).
- Its tail at 0.15-0.25 s after its phrase end is -17.9 dB re body, against the celli's -11.6. At 0.4-0.6 s it is -24.8 against -23.7, so it shares the late room.
- A real solo cellist is also heard through the Main tree. The DIV A patch has no Main mic (p.89-90, DIGEST 4.1).
- **Optional (mix only):** Cello solo `"send"` 0.5 -> 0.7 (+2.9 dB into the hall), to bring its early tail within about 3 dB of the section's. Skip it if the actor is short of a full-rebuild slot. The solo is not heard as a different instrument, only as a nearer one.

### 6. Seats and the cymbals: no change (measured)

- Stem R-L, matching an American seating: Violins I -8.1, Violins II -3.5, Violas +1.7, celli +6.0, basses +6.8, horns -3.3..-8.1, trumpets +1.5..+3.3, trombones +5.4..+6.9, tuba +7.6, harp -6.9, timpani +0.2 dB.
- Master balance R-L +0.1 dB (loud +0.3, soft +0.5).
- Cymbals and tam-tam share the room (manual notes, p.118-119).
- The crash ring at bar 160 supplies the top octave without leading it (12% of 8-16 kHz). The suspended cymbal's roll at bar 159 holds 21% of 8-16 kHz, under Violins I.

Do not touch: the shared hall (fx 0.095, low cut 160 Hz, `ir_setup` envelopeMode 2 / endPos 0.5 / decayLength 0.5, the true-stereo IR, wet 2.0, high cut 5.5 kHz) except the Width test in finding 1; every send except the Violas and optional Cello solo sends; `width_by_mic` (Main 0.35 winds/brass, 0.45 celli/basses) and the zeroed side low cuts; the seats; Violas `rt_gain_db` -6 (keep it, add room via the send); the 150 / 237 ms caps and the 350 ms p caps; the basses' pp cap (600 ms is fine from this lens); the loud_eq low-mid bells on celli, basses and low brass; Trumpet 1's climax shelves to 644.5; the Horns a2 1.6 kHz shelf spans; the crash ring under the bar-160 stroke; the bars 6-7 basses lift (do not raise it further); the timpani roll shapes.
