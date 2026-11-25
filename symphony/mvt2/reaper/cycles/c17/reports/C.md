# Cycle 17, critic C: blend and space (on the cycle 16 render)

Under review: `cycles/c16/render` (master and 29 stems), `cycles/c16/mvt2-mockup-c16.mp3`, `build/parts.json` (21:16, the data of the c16 render after the viola fix), `build/mix.json`, `tools/build_reaper.py` (`apply_mix`, `shared_reverb`, `vol_points`), the Opus states of all 21 patches (read with `opus_state.load_oib`), score pages 2 and 4.

Scripts are in `/private/tmp/claude-501/mockup-loop/c17-C/`:
- `tails.py` and `tailpan.py`: sustain and tail pan per stem, at the note ends where each stem falls silent.
- `pans16.py`: R-L and L/R correlation per stem, in three bands.
- `refcmp.py`, `dvspec.py`, `fine.py`, `contrib16.py`: spectrum against Brahms 1/ii, Brahms 4/ii and Dvorak, plus each stem's share of each band.
- `tailenv.py`, `tailchk.py`, `tailsrc.py`: volume-envelope moves inside rests, and what they do to the stems' tails.
- `mics.py`, `rvdump.py`: mic channels, sends and reverb inserts of every patch.
- `lowcorr.py`, `lowsim.py`: low-band coherence, with a simulated narrowing of the celli and basses.
- `presence.py`, `pres2.py`, `vln2.py`, `tone.py`, `tone2.py`: 2-6 kHz shares and tone per note.
- `m_c16/`, `m_mp3/`, `m_side*/`: `symphony/render/tools/measure.py` outputs.

Delivery numbers (measured; this lens does not change them):
- master: -23.0 LUFS, LRA 23.6 LU, TP -2.9 dBFS
- mp3: -19.8 LUFS, LRA 16.1 LU, TP -1.6 dBTP, span from p10 to S max 18.9 dB, limiter 3.2 dB (taken from the c16 CHANGES)

## 1. Every instrument's hall still comes back from its own seat. The library's true-stereo hall already loads in this project, in the timpani patch (measured; the fix's effect is inferred, so test it)

**Where:** all tracks. It is most audible at phrase ends and on the outer seats: Vln I, Vc, Cb, Tuba, the horns, the harp. It has been open since c05. c13 C #2 proposed this fix, and c13/c14 deferred it because it needs a full rebuild.

**What is wrong:** `shared_reverb()` copies the hall from `3BS Sus MAX.oib`: `"impulseA": "//ir/latest PLAY impulses final/New Hollywood Hall 2.0", "trueStereo": false`. A stereo IR convolves L only with L and R only with R. So a source seated left gets a tail on the left, and the hall never fills the other side. The orchestra then sounds like 29 instruments, each in its own small room at its own seat, not one ensemble in one hall.

**Evidence (measured):**
- Tail pan follows the sustain pan in every stem that matters (`tailpan.out`, median over each stem's cutoffs, sustain R-L -> tail R-L in dB):

  | Stem | Sustain | Tail |
  |---|---|---|
  | Vln I | -7.5 | -8.1 |
  | Vln II | -6.0 | -4.5 |
  | Horn 1 | -5.6 | -6.1 |
  | Horn 4 | -4.8 | -5.3 |
  | Vc | +5.9 | +5.2 |
  | Cb | +6.9 | +5.4 |
  | BTbn | +6.5 | +5.6 |
  | Bassoon 2 | +4.9 | +4.7 |
  | Cor anglais | +5.2 | +4.2 |
  | Violin I solo | -5.0 | -5.0 |

  These values are unchanged from c12. A hall tail sits near the centre whatever the seat.
- The master is more coherent in the mids than the references, and its energy sits further toward the sides (`m_c16`, against the Brahms 1/ii and 4/ii metrics):
  - corr 250 Hz-4 kHz: 0.61, against 0.48 and 0.52
  - corr above 4 kHz: 0.50, against 0.38 and 0.47
  - pan-energy histogram, centre two bins: 39%, against 50% and 50%
  - outer three bins: left 13%, right 16%, against 9-10% and 10-12%
- The fix is already proven in this rig. `Timpani Flt KS.oib` (the patch on track 20) ships `"impulseA": "//ir/HOP True Stereo/S. Cal Hall Perc TS FR 3.3s", "trueStereo": true`, and it rendered in c00, before `apply_mix` replaced every hall. The two inserts differ in only four keys (`rvdump.py`):
  - `impulseA`
  - `trueStereo`
  - `delay`: 0.0303 now, 0.0 in the timpani patch
  - `wet`: 1.99985 against 2.0

  `irSetup`, the filters, `width` and `inGain` are identical.

**Fix:**
- `build/mix.json` `reverb`: add `"impulse": "//ir/HOP True Stereo/S. Cal Hall Perc TS FR 3.3s", "true_stereo": true`.
- `tools/build_reaper.py` `apply_mix`, after `rv = shared_reverb()`: `if MIX["reverb"].get("impulse"): rv["impulseA"] = MIX["reverb"]["impulse"]; rv["trueStereo"] = bool(MIX["reverb"].get("true_stereo"))`.
- Keep `delay` 0.0303, `wet` 2.0, `high_cut_hz` 5500 and `fx_volume` 0.19 for the first pass.
- This is an Opus state change, so all 29 tracks need a full rebuild (as in c09), then a restart. Memory does not change, because no samples are added.
- Test it first on a range render of bars 15-30 and 89-92, then compare with c16 using `tailpan.py`, `rel.py` and `measure.py`.
- Level: a true-stereo IR adds the cross paths. If the tail-to-sustain level (`tails.py` d600) on Vln I, Vc and Ob1 rises more than 1.5 dB, lower `fx_volume` until it matches c16.
- Length: if the final-release drop at 1.0 s is more than 3 dB shallower than c16's 26.9 dB, set `rv["irSetup"]["simpleDecay"]` to 0.8 (Opus manual p. 134, the Simple envelope).

**Check:**
- Vln I, Vc, Cb, Horn 1 and Tuba tail R-L within ±3 dB, while each stem's sustain R-L stays within 1 dB of c16.
- Master corr 250 Hz-4 kHz at 0.55 or less. Centre two pan bins at 44% or more.
- Final-release drops at 0.3/0.6/1.0 s within 2 dB of c16's 9.8/17.3/26.9 dB.
- mp3 LRA, span and limiter each within 0.5 of c16.

## 2. Volume-envelope moves inside rests also move that instrument's hall tail: cuts of 6-8 dB and swells of 5-8 dB after the note has stopped (measured in parts.json and in the stems; how audible it is depends on exposure, inferred)

**Where:** the reverb is inside each Opus instance, and the REAPER volume envelope (`vol_points`) comes after it. Any role span, fill or trim that changes while a track rests therefore acts on the decaying hall of its last note. In parts.json, `tailenv.py` finds 37 changes of 3 dB or more within 1.5 s of a phrase end. Most come from `vol_db` role starts and ends, not from the dynamic trims (`tailsrc.py`).

**Evidence (measured).** Envelope change during the tail (stem decay in dB re the last sustain, 0.1 s steps):

- **Tails cut short:**
  - Oboe 1, bar 47 beat 4 (qn 151), the end of its solo phrase: -6.2 dB at +0.2 s, -7.9 at +1.4 s. The stem tail is -33 dB at 0.5 s and -57 at 1.2 s.
  - Ob2 bar 62.3 (qn 210): -7.3.
  - Cl1 bar 78.3 (qn 261): -8.3.
  - Cl2 bar 63.1 (qn 212): -6.2, and bar 82.3 (qn 273): -6.2.
  - Bn1 bar 36.3 (qn 107): -6.0.
  - Tuba bar 63.1 (qn 212): -4.5. Fl1 bar 40.4 (qn 123.75): -4.0.
- **Tails swelled:**
  - Cb bar 31.1 (qn 90): +8 dB. In the stem the tail rises 5 dB over the last sustain at +0.1-0.4 s, after the note has ended.
  - Vln II bar 41.1 (qn 124): +8. The decay stalls at -21 dB from 0.6 to 1.0 s.
  - Vla bar 31.1 (qn 90): +6. Vln II bar 67.1 (qn 226): +6.
  - Vln I, Vc and Cb at the end of the intro chord (qn 9): +5, where the roles [0, 9.2, -5] end.
  - Horn 1 bar 61.1 (qn 204): +4.6.
- In a hall, a tail decays at one rate whatever the player does next. A tail that drops a step, or swells after the bow has stopped, is a mixing artefact.
- Inferred: most of these are masked in tutti. The ones heard are the exposed phrase ends, for example Ob1 bar 47, Cb/Vla at the bar 30 cadence and Vln II bar 41.

**Fix:** `tools/build_reaper.py` `vol_points`, after `vals` is computed, add a tail hold:
- For each rest of the track, from a moved note end `e` (no other note of the track sounding) to the next moved onset `n`, hold the envelope at its value at `e`. Hold it for every grid point in `(e, n_hold)`, where `n_hold` is 0.35 s before `n` (on the tempo map), so that the new value arrives just before the next entry.
- Skip the final fade (q ≥ 303.5) and rests shorter than 0.5 s.
- Values on sounding notes do not change, so the stems' note bodies stay exact. Early fills with `pre_s` up to 0.3 s still start after `n_hold`.
- This is level only (`--mix-only` is enough, no MIDI change), so the c16 stems can preview it. Multiply each stem by the envelope ratio, new over old, in the tail windows.

**Check:**
- Rerun `tailenv.py` on the new envelopes: no change of 3 dB or more within 1.5 s of any phrase end except the final fade.
- `tailchk.py`: Ob1 151 and Cb 90 decay monotonically, with no 0.1 s frame more than 1 dB above the one before.
- Note-body levels (`metrics.md` per dynamic) unchanged within 0.2 dB.

## 3. The harp and the harp harmonics are not at their seat. They sit left of centre, near the horns, with an almost uncorrelated image (measured; listener effect inferred)

**Where:** Harp (bars 7-14, 37-56: the arpeggios on page 2 and page 4) and Harp harmonics (bars 83-92).

**What is wrong:** `mix.json` seats both at -0.65 with width 0.3, outside Violins I (-0.55). Measured over all active frames (`pans16.out`):

| Stem | R-L (dB) | corr (all) | corr 250 Hz-4 kHz |
|---|---|---|---|
| Harp | -4.0 | 0.51 | 0.19 |
| Harp harmonics | -3.8 | 0.21 | 0.20 |
| Violins I (seat -0.55) | -8.1 | | |
| Horn 1 (seat -0.45) | -4.7 | | |

The two harp stems have the lowest coherence in the mix. The harp patch's two channels differ a lot: inferred, its R channel is hotter, because the HO harp was recorded to the right. The 0.6-wide pan spreads it from the left wall to centre-left. A real harp is a point source. Here it sounds spread and placed nowhere in particular, under the flute and cor anglais solos of bars 37-52.

**Fix:** `build/mix.json`: Harp and Harp harmonics `"seat": -0.72, "width": 0.12` (panLeft -0.84, panRight -0.60). This is a state change, so do it in the same full rebuild as finding 1.

**Check:**
- Harp R-L -7 dB or lower, and corr 250 Hz-4 kHz 0.40 or more.
- Harp level within 0.5 dB of c16 in bars 37-52. Re-trim `gain_db` if the narrower pan changes the power.

## 4. Low end: no build-up below 100 Hz, but the bass image is too wide. The 200 Hz "excess" is the tonic, not EQ (measured)

**Where:** Vc and Cb all through. The climaxes, bars 61-62 and 79-80, for the Db2 fundamental.

**Evidence (measured):**
- There is no sub-bass build-up.
  - The 20-100 Hz share of the master is -14.5 dB. The references give Brahms 1/ii -8.5, 4/ii -7.9 and Dvorak -21.7, so the mockup sits between them.
  - Relative to 500 Hz, the 62/79 Hz bands are -8.7/-11.6, against -4.1/-6.0 (Br1), -2.3/-3.2 (Br4) and -28/-15 (Dv).
- A 1/3-octave comparison does show 198 Hz at +4.1 dB over the Brahms mean, and 315 Hz at +3.7. With 1 Hz resolution, these are notes of the key:
  - 207 Hz Ab3: Vc 65% of it
  - 175 Hz F3: Vc 83%
  - 311 Hz Eb4 and 349 Hz F4
  - the strongest low peak is 69 Hz Db2: Cb 99%

  The references are in E, so a band-by-band match across keys measures the key, not the mix. Do not EQ toward it. Keep using the broad shares (LEARNINGS c09).
- Climax: loud minus soft at 79 Hz is +2.0 dB, against +0.8/+0.7 in both Brahms. The Db2 fundamental grows 1.2 dB more than in the references (a slight boom; effect inferred).
- The bass image is too diffuse.
  - Master coherence below 250 Hz is 0.52, against 0.60/0.62.
  - The two stems that carry it are the least coherent at low frequencies: Vc 0.47 and Cb 0.52 (Tuba 0.67, Cbn 0.67, BCl 0.88).
  - Simulated (`lowsim.py`, M/S on the c16 Vc and Cb stems only), side x0.85: master low corr 0.52 -> 0.61, mid corr 0.61 -> 0.62. Side x0.7 -> 0.70, which is past the references.

**Fix, after finding 1's render, because the true-stereo hall changes the low coherence too:**
- If master corr below 250 Hz is still under 0.56, set `mix.json` Violoncellos and Double basses `"width": 0.35 -> 0.28`. This is a full rebuild of 2 tracks.
- If loud minus soft at 79 Hz is still over +1.5 dB, set the Cb `loud_eq` lowshelf from 80 Hz -3 to 80 Hz -4.5. This is `--mix-only`; the 150 Hz bell and the centroid stay.

**Check:**
- low corr 0.58-0.64
- loud minus soft at 79 Hz +0.5..+1.5
- 20-100 Hz share within 0.5 dB of c16
- centroid of the loudest 10% still 900 Hz or lower

## 5. Under the cor anglais solo (bars 48-51), the pp second violins are the brightest thing in the mix (measured; whether this is wrong is inferred)

**Where:** Violins II, bars 45-51 (qn 140-168), Leg Slur/Leg BC MAX, CC11 32-34, printed pp, senza sord.

**Evidence (measured):**
- Vln II supplies 66-91% of the master's 2-6 kHz in bars 48-52, with 9-10% of its broadband energy (`presence.py`). Its 2-6 kHz level is 6.3 dB over the solo cor anglais (`pres2.py`: -19.9 against -26.2 dB).
- Per note, at the same pitches (77-79), 2-5 kHz re the fundamental (`vln2.py`):
  - pp in bars 48-51: +0.9, -1.2, +1.1, -4.5 dB
  - f in bars 57-58: -1.4, -1.3, +1.8, +0.7 dB

  So the pp layer here is as bright as the f layer, and the soft trims then lift it by 3-3.5 dB.
- In both references, loud minus soft at 2.5 kHz is +1.4/+5.8 dB, so soft playing is darker than loud. Inferred: a pp accompaniment with a brighter edge than the solo draws the ear away from the cor anglais.

**Fix:** `build/mix.json` Violins II: add `"loud_eq": {"points": [[139,0],[140,1],[168,1],[170,0]], "bands": [{"band": "highshelf", "hz": 3000, "db": -5}]}`. The mechanism is generic, so the name does not matter. It is a wet-automated ReaEQ, so bars 53-62 keep today's sound. Apply it with `--mix-only`.

**Check:**
- Vln II 2-6 kHz in bars 48-51 at or under the cor anglais.
- Vln II share of the master's 2-6 kHz in bars 48-51 at 55% or less.
- Vln II broadband level within 1 dB of c16.

## Smaller, measured, no action proposed

- **The Violin I solo (DIV A, Close mic only) is near mono** (corr 0.93, the section 0.43-0.48).
  - Its 2-5 kHz re f0 is -1.0 dB, against -2.9 for the unmuted section at the same pitches. It is not bright for an unmuted solo: the section is con sord. in bars 15-30, which explains the larger gap against bars 1-55.
  - The Violoncellos div is also mono (0.92) and 6 dB darker than the section. It is quiet, so it is not exposed.
  - Their space can only come from the hall, so finding 1's tail check covers them.
- **Depth staging is consistent.** Every channel's send is pre-fader at `send x channel volume`, so the hall-to-dry ratio follows the group send:
  - strings 0.25
  - harp 0.3
  - winds 0.35
  - timp and low brass 0.45
  - horns and the two DIV tracks 0.5

  That puts the strings in front and the brass behind, with Close/Main 0.5-0.66 / 0.8-1.0 throughout.

## Do not touch

- The send ratios per group.
- The mic sets: Close + Main; no Surround, since it would add memory.
- The pre-delay of 0.0303 s and the 5.5 kHz hall high cut.
- The final-release decay (9.8/17.3/26.9/39.1 dB at 0.3/0.6/1.0/1.5 s, matching Brahms).
- The seats of every stem except the harp tracks.
- `loud_eq` on Vc/Cb, apart from the conditional shelf step in finding 4.
- The 20-100 Hz share.
- The broad-band spectrum (100 Hz-6 kHz shares within 1 dB of the Brahms mean).
