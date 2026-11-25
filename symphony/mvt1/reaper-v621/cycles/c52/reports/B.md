# Critic B, cycle 52 (render c51): balance and levels, and the level side of finale items 5, 6, 11 and 15

Under review: `cycles/c51/render` (dry stems 01-40, returns 91-94, master), the delivered `mvt1-mockup-c51.mp3`, and
`build/` (identical to `cycles/c51/rendered_build_pass2/`). Balance is measured on the dry stems, K-weighted (8192 Hann
FFT, hop 4096, stereo power, per 1 qn), with the c50 actor's `bal50.py`. Blend figures come from the master. Re-run on
the c51 render, my check table matches the actor's `bal51_final.txt` exactly (measured). For the finale items I applied
each EQ change to every stem's per-frame spectrum (RBJ bells, ReaEQ octave bandwidths). The returns are scaled per band
by their family's dry change (post-fader sends). I then re-ran the check table on the result. The simulator reproduces
bal50 on the baseline to 0.0 dB, and its stem sum is within 0.3 dB of the master in every third octave from 125 Hz to
4 kHz. Labels: "measured" = read off the c51 or c50 files; "simulated" = this model; "inferred" = reasoning.

## Manual notes (third round: pages chosen for this lens's top problems)

| Source (PDF page) | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| 2021 p.64, p.151 | CC7 / the fader sets a track's level against the others; CC11 shapes the line. Opus strings and woodwinds crossfade dynamics on CC11 | Every make-up in this report (items 5 and 6, bar 122) | Yes. All the make-ups below are fader or volume-envelope changes, so CC11 keeps each dynamic's timbre |
| 2021 p.109; DIGEST 7.2 (patch) | Woodwind sustains play their dynamic layers together, with one or two audible at a time. The Clarinet KS Master crossfades its dynamic layers on CC1 | Clarinet 1's coda join at qn 700 (finding 3) | No. PHRASE_SHAPE (`both_lanes`) moves CC1 28→37 and CC11 42→49 across that join, so it lands on a louder layer. The c47 hole-fill fitted on the old layer now makes a +4.5 dB bump |
| 2021 p.151 | "Volume can be adjusted mid-note … a crescendo or diminuendo for a held note"; CC11 makes "swells … over the course of a phrase" | HP_CURVE's diminuendo rule (finding 1); bar 122's held fff note (finding 3) | Partly. Long diminuendi now hold at f until their last inner onset. The bar-122 note lost the held-note swell that c50 gave it |
| 2021 p.138-139 | The Main pair is a Decca tree (3 M50s) plus outriggers in the fifth row, giving "a big, unified sound". The Close mics stand in front of each section | Item 5: REAPER's track width acts on the summed signal after Opus, Main included | Not applied yet (plan §9) |
| 2021 p.53, p.150 | Velocity sets the level of shorts; each recorded dynamic has its own velocity range | Nothing new this cycle; c51's string-short velocities stay in their zones | Yes |
| MANUAL-GAPS #4, #13 | Mid mics on winds; the bass trombone's lowest notes | Still open; low priority for this lens | — |

## EW-TEMPLATE-PLAN sections this lens touches

- Applied: §1 (Close at the seat, Main at seat ±0.8 by measured choice), §2, §3 (with c51's brass bells), §6 (shorts
  level-safe), §8 (basses EQ, register sends), §10 (one curve for doublings; level lane follows timbre lane).
- Not yet applied: §9 "brass as narrow sources" (finale item 5, finding 4), §8's tutti entry spread, and §5's CC1 macro
  on the main tracks.
- §9's hairpin shapes are applied. They are the cause of finding 1.

## Findings, ranked by what a listener would hear

### 1. HP_CURVE holds every long diminuendo at f until its last inner onset. Bars 123-125 are 4-9 dB louder than c50, and the Horn 1 "mp espr." entry at bar 125 sits 6.7 dB under Violins I (measured; fix simulated)

**Where:** Violins I/II, violas, celli, Clarinets 1-2, Oboe 1, Bass clarinet, Bassoon 1, Tuba and Horns 3-4 over qn
488-500. Smaller cases: bars 66-67 (qn 260-268) and bars 162-165 (qn 644-660).

**Evidence (measured):**
- Violins I's printed fff→p diminuendo runs 488-500. Its last inner onset is 498. `decresc_last` 0.35 puts only 35 % of
  the fall at 498, so the curve reads CC 99 at 497 and 94 at 498. A linear hairpin would read about 65.
- The celli read 83 at 497 against 65.
- Per qn, c50 → c51 over 492-499:
  - Violins I +4.0 / +5.1 / +4.1 / +4.6 / **+9.2** / +5.9 / +4.8 / +3.1 dB;
  - celli +2.9..+9.7;
  - Violins II +2.1..+6.5;
  - tuba +3.3..+6.4;
  - clarinets +1.6..+5.6.
- Horn 1's bar-125 entry (497, printed mp espr.) over the loudest other stem: median +1.6, minimum **-6.7** (Violins I).
  c50 had +2.9 / -0.2.
- The same rule lifts Violins I +3.1..+3.4 and Horn 2 +3.6..+4.8 at 262-266, and the upper strings +2.7..+4.9 at
  648-652.
- To a listener (inferred): the sostenuto's three-bar diminuendo now holds and then collapses on the last beat, and the
  horn's solo enters under the strings.

**Fix:**
- In `tools/score_to_parts.py`, in the HP_CURVE diminuendo branch (`elif hk == "decresc" and tgt < st_:`, about line
  1931), require `stop - q <= HP_CURVE.get("decresc_max_qn", 1e9) + EPS`.
- In `build/score_config.py`, add `"decresc_max_qn": 4.0` to HP_CURVE.
- This leaves the six printed diminuendi longer than 4 qn linear, as c50 had them: bars 3, 21, 66-67, 74, 123-125 and
  162-165. Shorter ones keep C's curve.

**Simulated** (c50 levels on those 15 tracks over 488-500.5, with the brass gain and EQ change):
- Horn 1 at 497 / 498 / 499 / 500: -0.7 / +8.0 / +5.3 / +1.2 over the loudest other.
- Brass minus strings at 123-126: +1.0 → about +2.4 (c50 +1.6).
- Horns minus heavy brass: -4.7 → -5.2.
- Every other row is unchanged.

### 2. Finale item 6 (315 Hz). The excess is real, but the horns make only about a quarter of it here. The finale's +1.0 / +0.8 make-up would leave Horn 2 2.2 dB low and the soft horns 1.6-2.7 dB low. Use a per-track make-up (measured excess; fix simulated)

**The excess (measured; master mono, whole length, third-octave share of the total):**
- 315 Hz: c51 **-9.5 dB**. Brahms 1/i, 4/i, 1/ii, 4/ii: -13.8..-14.8. Dvořák: -12.5. That is 4.3-5.3 dB over the
  lossless Brahms recordings and 3.0 dB over Dvořák.
- The "hump" (315 minus the mean of 250 and 400): c51 +2.9 (loudest 25 % of frames +3.0). References: -0.7..-2.5.
- 200 and 250 Hz are also 1.6-4.2 dB over the Brahms recordings.
- 400 and 500 Hz are 1.4-2.4 and 0.8-3.2 dB *under* them. Part of that is the template bells at 447-475 Hz.
- Dan's "mushy" note fits a 200-315 Hz excess (inferred).

**Who makes the 315 band (share of the stem + return sum):**
- celli 16 %, violas 14 %, tuba 8 %;
- Horn 2 7 %, Horn 3 6 %, Horns a2 5 %, Horn 1 3.5 % (the horns together 22-25 %);
- bass clarinet 5 %, Clarinet 1 5 %, Bassoon 2 4 %.
- In the finale the horns made 52 %.
- Horn 2's own 315 band stands 12 dB over its 250 and 400 Hz bands; the bass clarinet's 10.5 dB.

**What item 6 does here (simulated):**
- As written, it cuts the master's 315 share by 0.8 dB (hump +2.5).
- With a level-keeping make-up the cut is 0.6 dB (hump +2.6).
- Per-section hump c51 → item 6: Lento +1.0 → +0.3, theme +3.5 → +3.2, development +2.6 → +2.2, 131-146
  +2.9 → +2.5. Unchanged at 115-126 (+3.6) and 171-182 (+4.2).

**Level cost (simulated, exact per-frame K).** The horn 315 bell costs more K level than the finale assumed, and more at
soft dynamics:

| Track | K, all frames | K at ≤p | K at mp-mf | K at ≥f | A, all frames |
|---|---|---|---|---|---|
| Horn 1 | -2.0 | -3.4 | -2.7 | -1.7 | -1.3 |
| Horn 2 | -3.2 | -3.8 | -2.9 | -3.2 | -2.2 |
| Horn 3 | -2.0 | -2.9 | -2.8 | -2.0 | -1.3 |
| Horn 4 | -1.3 | -2.6 | -2.0 | -1.3 | -1.0 |
| Horns a2 | -1.6 | — | -2.4 | -1.6 | -1.0 |
| Violas (-3 dB) | -1.4 | -1.3 | -1.3 | -1.5 | -0.9 |

**Why the finale's make-up does not hold here (simulated check table, c51 → item 6 with +1.0 / +0.8):**
- Horn 1 solo 13-14: +9.4 → +8.1.
- Same-dynamic pp horns: -2.1 → -3.7; f horns: -3.4 → -4.4.
- Trumpets a2 minus Horns a2, 167-170: +1.8 → +2.3.
- Cor anglais minus Horn 1, 147-152: -5.1 → -3.2 (outside -4..-6).
- Horn 3 minus Horn 4 at ppp: -1.0.

**Fix (`build/mix.json`):**
- Add `{"band": "bell", "hz": 315.0, "db": -5.0, "bw_oct": 1.0}`. The brass family EQ is shared, so put it in each
  horn track's `eq`, or give the horn group its own family EQ: Horns 1-4 and Horns a2 only, not trumpets, trombones or
  tuba.
- Add `{"band": "bell", "hz": 315, "db": -3, "bw_oct": 1.0}` to `tracks.Violas.eq`.
- Make-up (K-weighted, so the check table holds; gain_db carries the f cost, soft trims the rest):

| Track | gain_db | soft_trim_db ppp / pp / p | soft_trim_db mp / mf |
|---|---|---|---|
| Horn 1 | -2.2 → -0.4 | 13.5/12.5/9.6 → 15.1/14.1/11.2 | 7.2/-1.4 → 8.1/-0.5 |
| Horn 2 | -3.1 → +0.2 | 13.5/12.5/8.7 → 13.9/12.9/9.1 | 9.6/2.4 → 9.2/2.0 |
| Horn 3 | -2.6 → -0.6 | 13.5/12.5/11.0 → **12.8**/13.3/11.8 (ppp includes finding 3c's -1.5) | 6.7/1.7 → 7.5/2.5 |
| Horn 4 | -2.5 → -1.3 | 12.7/12.7/11.0 → 14.1/14.1/12.4 | 5.3/3.3 → 6.0/4.0 |
| Horns a2 | 3.1 → 4.7 | unchanged | 7.2/2.0 → 7.9/2.7 |
| Violas | 2 → 3.4 | unchanged | unchanged |

- Simulated check table with this make-up: every row within ±0.5 dB of c51. The largest moves: Horns a2 41-42 +0.5,
  celli tune 47-55 -0.5, horns minus heavy brass +0.4, f horns -0.4. Bar 122 and the tam-tam are unchanged.
- Optional, same cycle: the celli are the largest single source. A 315 Hz -3 dB bell (bw 1) with +1.1 dB gain_db on
  Violoncellos and Cello solo takes the master's 315 band to -0.9 dB and the hump to +2.5.
- For c53 (blend): moving the strings' 456 Hz and the winds' 447 Hz template bells down to 315 Hz, together with item 6,
  takes the hump to +1.7, the 315 band -1.8 dB, and 500 Hz +1.0 dB toward the references (simulated). But soft notes
  near 300 Hz lose 1-2 dB (Clarinet 1's coda pickup, horns at p -1.8), so it needs its own per-dynamic make-up.

### 3. Open items from c51: bar 122, the coda clarinet, Horn 3 at ppp (measured causes; fixes simulated)

**3a. Bar 122 sits 0.5 dB under c50.**
- **Cause (measured):** c51 drops the per-note swell on notes inside shaped phrases. Bar 122's held fff arrival lost
  c50's SWELL_DB rise.
  - Over 485-486.5 the volume envelope reads 0.7-1.3 dB under c50 on every brass, string and wind track. For example
    Trombone 1 at 485.5: +2.5 against +3.8; Violins I: -3.0 against -1.7.
  - CC11 stays at 124 where c50 rose to 126-127.
  - Per family at qn 485 / 486: brass -1.8 / -1.3 dB, strings -1.3 / -0.9, winds -1.1 / -0.6. The arrival at 484 itself
    is unchanged (dry sum 60.4 against 60.6).
- **Fix:** add a `LEVEL_SHAPES` row of +1.0 dB on every brass, string and wind track:
  `[(484.25, 0.0), (485.0, 1.0), (487.25, 1.0), (488.0, 0.0)]`. The tam-tam and timpani are excluded.
- **Simulated:** I applied it to the c51 master and ran `deliver_master.py` on a scratch copy.
  - Delivered S max at bar 122: -12.4 → **-12.0** (c50 -11.9).
  - Order: 160 -11.4 > 122 -12.0 > 167-170 -13.4 > 26 -14.3, so 160 stays 0.6 dB over 122.
  - LRA 14.5 LU, span 18.8 dB, limiter 0.0 dB.
  - Tam-tam minus all others: -6.3 → -6.8 (window -6..-7.5).

**3b. Clarinet 1 in the coda (qn 699-706).** The minimum over the other stems is +0.6 (c50 +3.1). Two causes (measured):
- **The pickup at 699.** It is 1.7 dB under c50 (per 0.1 qn: 0.9-5.6 against 3.9-4.9). The phrase starts at CC11 33
  where c50 had 42. Trombone 1's chorale chord is the loudest other stem there.
- **The arrival at 700.25.** It peaks **+6.4 dB** over its own body (c50 +1.3).
  - It is the c47 hole-fill `[(700.14, 0), (700.20, 5.0), (700.40, 5.0), (700.50, 0)]` (score_config.py line 3168),
    fitted when both lanes were flat.
  - Now PHRASE_SHAPE raises CC1 28→37 and CC11 42→49 through the join, the layer entry the patch has there (see
    Manual notes). The join no longer has a hole, so the fill makes a bump.
- **Fix:**
  - Delete that fill row. Keep c49's two cuts.
  - Add a pickup lift: `LEVEL_SHAPES["Clarinet 1"]` `[(698.88, 0.0), (698.93, 2.0), (699.4, 2.0), (699.8, 0.0)]`.
- **Simulated on the stem:** arrival over body +6.4 → +2.2 dB; pickup back to c50's level; coda minimum about +2.5.
  Check on the render: a 2.2 dB dip at 700.1 that the old cut leaves without the fill after it.

**3c. Horn 3 at ppp is +1.2-1.5 dB over c50.** The four C4s of 720-726.6 come from the softfix raising ppp together with
pp (Horn 3 ppp 12.0 → 13.5, measured on the stems: +1.49 dB after gain and EQ). Horn 3 now sits 4.4 dB over Horn 4's
ppp G3 in the final chord (c50 3.3). Fix: Horn 3 `soft_trim_db.ppp` 13.5 → 12.0, before finding 2's +0.8.

### 4. Finale item 5 (track width). The seats are predictable, but REAPER's level change under width is not: -2.4 or +0.9 dB depending on how REAPER implements it. Measure it and make it up, because either way the c51 brass balance breaks (simulated)

**Current seats (measured, dry stems, 250 Hz-5 kHz):**
- The trumpets sit near the centre and diffuse: R-L +1.3..+2.0 dB, correlation 0.24-0.40.
- The trombones already sit right of them: +4.1..+5.2 dB, correlation 0.28-0.45.
- For comparison: tuba +6.2 (0.68), horns -4.3 (0.63), Violins I -7.0.

**With the finale's values** (trumpets and Trumpets a2 width 0.5 at pans +0.30 / +0.33 / +0.36 / +0.315; trombones 0.6
at +0.26 / +0.30 / +0.34):
- Trumpet 1 R-L +3.8..+4.7, Trumpets 2-3 +3.7..+5.1, trombones +4.4..+6.8.
- Correlation 0.69-0.81: narrow sources, horns left, trumpets centre-right, trombones and tuba right.
- Master proxy: correlation 250 Hz-5 kHz 0.478 → 0.529; side/mid -4.51 → -5.10 dB. Both stay inside the references
  (0.47-0.56; -4.7..-5.4).

**Level.** The REAPER docs on this machine do not give the stereo-pan formula, so I simulated two models:

| Model | Trumpets 1 / 2 / 3 / a2 | Trombone 1 / 2 / Bass trombone |
|---|---|---|
| A: mid/side width, then a 0 dB-law balance pan (the project has `PANLAW 1`) | -2.2 / -2.4 / -2.1 / -2.1 dB K | -1.3 / -1.5 / -1.4 |
| B: each channel panned by constant power | +0.7 / +0.6 / +0.7 / +0.9 | +0.5 / +0.4 / +0.7 |

The c51 brass sits on the orchestration norm: at f and ff, trumpets ≈ trombones ≈ horns + 2.7 dB (Rimsky-Korsakov:
trumpet = trombone = two horns). Without make-up:
- Model A: same-dynamic f / ff trumpets -0.7 → -2.9 / -2.8; Trumpet 1 minus Violins I, bars 82-83: -1.6 → -3.8;
  Trumpets a2 minus Violins I at 167-170: +0.5 → -1.6.
- Model B: Trumpets a2 minus Horns a2 at 167-170: +1.8 → +2.7 (limit 2.5).

**Fix:**
- `tools/build_reaper.py`: port mvt3's `track_width()` and write it where D_WIDTH is set to 1 now (line 1099, and the
  `--mix-only` job).
- `build/mix.json`: `reaper_pan` and `track_width` on the seven tracks, with the values above.
- Then hold every K level at c51's:
  - **Either** run a short range render of 82-84 and 167-170 with and without the width (mix-only, no Opus state), and
    set `gain_db` by the measured difference: model A's make-up would be +2.2 / +2.4 / +2.1 / +2.1 and +1.3 / +1.5 /
    +1.4; model B's -0.7 / -0.6 / -0.7 / -0.9 and -0.5 / -0.4 / -0.7.
  - **Or** render, measure the same per-note change as finding 5's method, and correct with `stem_fix.py`.
- The renders repeat to ±0.07 dB on unchanged notes, so the measurement is exact. The returns follow the post-fader
  signal, so nothing to do there.

### 5. The "11 brass state-flip runs" of c51 are the c51 brass EQ, not state flips. The only real flip is Trumpet 1's Leg Slur note at 643. `state_check.py` will flag every horn and viola note in c52 unless it learns the EQ (measured)

**Evidence (measured; `flips.py` on all 73 flagged brass notes):**
- I applied each note's c50 spectrum through the c51 `gain_db` and family-EQ difference. The bells moved from -5.4 / -7.8
  to -2.7 / -3.9 and the 3.2 kHz -3 dB bell was added.
- That predicts the c51 stems to a median **-0.03 dB** (range -0.07..+0.07). The renders are reproducible to that
  precision.
- The state check removes the envelope and gain changes but not the EQ, so it read the bells' +3..+4.8 dB of unweighted
  body as level jumps. The 11 "runs" are just consecutive notes from that same shift.
- Residuals over 0.1 dB:
  - Horn 3 720-726.6 +1.49 (the ppp soft trim, finding 3c);
  - Horn 4 720 +0.69 (ppp +0.7);
  - Horns a2 670-673 +0.6 (c51's roles row);
  - **Trumpet 1 at 643** (Leg Slur MAX, bar 161): +4.0 dB K beyond the EQ, pcX -86 ms. That matches the scherzo's
    stale-legato signature (loud joins about 85 ms early after a `--midi-only` build).

**Fix:**
- Fully rebuild Trumpet 1 in c52, not `--midi-only`.
- Check every legato join on the other `--midi-only` brass tracks on pcX.
- In `tools/state_check.py`, before flagging, subtract each note's predicted change. That is gain_db difference plus
  10·log10(Σ P_old(f)·|H_new(f)/H_old(f)|² / Σ P_old(f)), with H from family_eq + eq for each build.
- Flag on the K-weighted residual. Without this, c52's 315 Hz bells flag every horn and viola note.

### 6. Finale items 11 and 15

**Item 11 (strings 1 kHz -5 → -2.5, winds -3.1 → -1.55): drop it for Movement I.**
- **Evidence (measured):** the finale adopted it because its 500 Hz-1 kHz sat under the references. Movement I is
  already level with or over them:
  - 500 Hz-1 kHz share: c51 -6.2 dB, references -5.6..-7.0.
  - 1-2 kHz share: -5.8, references -6.1..-7.4 (over all five).
  - Third octaves: 794 Hz -11.8 (Brahms -14.1..-15.5) and 1 kHz -12.2 (Brahms -13.3..-14.7).
- **Simulated effect:**
  - +0.9 dB at 1 kHz; the 1-2 kHz share +0.3 dB further over.
  - Centroids +8 Hz (loudest 10 %), +6 at 121-126, +11 at 167-170, against C's c51 aim of darker climaxes.
  - Level: strings +0.1..+0.7 dB K, winds +0.3..+0.9 dB.
- **If it is adopted anyway**, this make-up holds the check table within ±0.3 dB:
  - Violins I / II -0.7, violas -0.5, celli -0.3, basses -0.1, Cello solo -0.5;
  - flutes and cor anglais -0.9, oboes and Clarinet 1 -0.5, Clarinet 2 -0.4, Bassoon 1 -0.4, bass clarinet, Bassoon 2
    and contrabassoon -0.3.

**Item 15 (delivery ride rules).**
- **One measured violation.** The `RIDE_TRIMS` row 656-664 ends with its -0.5 dB step at 663.5-664.0. That is inside
  the tutti crescendo 662-664.5 into the coda: Horns 1-4, Horns a2, violas, Violins I, basses, timpani (p< f) and
  Clarinet 1. Fix in `build/score_config.py`: end that row at `(661.5, 0.5), (662.0, 0.0)`.
- **The final row.** It ends with a step at 727.5-728 inside the final chord's last 0.6 s. Hold it to the end of the
  file: `(727.5, 0.5), (730.0, 0.5)`.
- **No `--fit-flat` rows are needed (measured).** After the four true loud→soft steps (qn 134.8, 293.2, 336.7, 501.5)
  the ride rises only 0.3-0.8 dB in the first 4 s, under the finale's 1.5 dB.
- The two larger rises (+1.6 at 169.6, +1.7 at 574.8) sit inside printed diminuendi (160-168, 566-578). There the ride
  follows the printed fall, at 3:1 below the knee: master -18 / -20 dB against delivered -13 / -16 dB. A flat row would
  flatten them further.
- The existing +0.5 rows stay.

## Check table for the c52 render (dry stems with `bal50.py` plus the rows below; master and mp3 where named)

| Check | c50 | c51 (baseline) | Target for c52 |
|---|---|---|---|
| Brass minus strings 25-32 / 115-122 / 123-126 / 158-161 | -0.4 / +0.9 / +1.6 / -0.1 | -0.8 / +0.2 / +1.0 / -0.8 | each within ±0.5 of c51; 123-126 up to +2.5 with finding 1 |
| Horns minus trumpets + trombones + tuba, 123-126 | -5.0 | -4.7 | -5.5..-4.0 |
| Horns a2 over loudest other, 41-42 | +0.3 | +0.3 | ≥ 0 |
| Trumpets a2 minus Violins I / minus Horns a2, 167-170 | +1.5 / +2.8 | +0.5 / +1.8 | -0.5..+1.5 / ≤ +2.5 |
| Trumpet 1 minus Violins I, 82-83 | -1.6 | -1.6 | -2.1..-1.1 (item 5 make-up) |
| Horn 1 solo over loudest other, 13-14 / Violins I theme 15-22 / celli tune 47-55 | +11.3 / +3.5 / +4.5 | +9.4 / +4.3 / +5.1 | ≥ +8 / ≥ +3.5 / ≥ +4 |
| **Horn 1 bar-125 solo over loudest other, 497-501, median / min** (new) | +2.9 / -0.2 | +1.6 / -6.7 | ≥ +2.5 / ≥ -1 |
| Winds minus strings 25-32 / 158-161 | -1.5 / -1.9 | -1.5 / -2.2 | ±0.5 of c51 |
| Cor anglais minus Horn 1, 147-152 | -4.5 | -5.1 | -6..-4 |
| Tam-tam fff minus all others, 484-491 | -7.6 | -6.3 | -6..-7.5 |
| Sus. cymbal + crash minus all others, 636-640 | -16.8 | -16.6 | ±0.5 |
| pp chorale minus strings, 175-178 | -1.8 | -2.2 | -1.5..-3.5 |
| Clarinet 1 over loudest other, 699-706, min / median | +3.1 / +3.7 | +0.6 / +6.6 | ≥ +2.0 / ≥ +4 |
| **Clarinet 1 arrival at 700 over its body** (new; 0.1 qn K frames) | +1.3 | +6.4 | ≤ +2.5 |
| **Horn 3 minus Horn 4, 720-728 (ppp)** (new) | +3.3 | +4.4 | ≤ +3.3 |
| Cello solo over loudest other, 680-696 / timpani ppp minus violas 181-182 | +7.5 / -9.3 | +7.5 / -10.1 | ≥ +6 / -8..-11 |
| Same-dynamic scan, each family | c50 file | horns pp/p/f/ff -2.1/-3.2/-3.4/-2.8; trumpets f/ff -0.7/-0.7; trombones+tuba f/ff 0.0/0.0, pp -4.0; winds pp/p/f/ff -0.9/-1.6/-5.3/-4.4 | each within ±0.5 of c51 |
| Horns and violas K change per printed dynamic, c51 → c52 (kres51 method) | | | within ±0.5 dB (item 6 make-up) |
| Trumpets / trombones K change on notes with unchanged data, gain and EQ removed (flips.py method) | | | 0 ± 0.3 dB (item 5 make-up) |
| Trumpet 1 R-L / trombones R-L / brass correlation (250 Hz-5 kHz, dry) | | +2.0 / +4.1..+5.2 / 0.24-0.45 | +3.5..+5 / +4.4..+7 / 0.65-0.85 |
| Master 315 Hz third-octave share / hump (mono, whole length) | | -9.5 / +2.9 | ≤ -10.1 / ≤ +2.6 (≤ +2.5 with celli) |
| Master correlation 250 Hz-5 kHz / side/mid | 0.483 / -4.71 | 0.483 / -4.66 | 0.47-0.56 / -4.7..-5.4 |
| Delivered S max 160 > 122 > 167-170 > 26 (mp3) | -11.2 / -11.9 / -13.4 / -14.1 | -11.4 / -12.4 / -13.4 / -14.2 | 122 within 0.3 of c50; 160 over 122 ≥ 0.5 |
| Ride rows ending with a step inside a printed crescendo; ride rise over 4 s after a loud→soft step | | 1 (656-664); 0.3-0.8 dB | 0; ≤ 1.0 dB |
| Delivered LRA / span / limiter | 14.7 / 19.1 / 0.2 | 14.6 / 18.8 / 0.0 | 14-16 LU / 16-19 dB / ≤ 3 dB |
| State check on unchanged brass notes, after the EQ correction | | 1 real flip (Trumpet 1 643) | 0 |
| Timpani rolls, median / max re loudest other; low-band share | | see below | no roll the loudest stem for more than its arrival beat |

## Dan's standing checks through this lens (c51, measured)

- **Timpani rolls.** Medians run -6.6..-11.4 dB under the loudest other stem. The timpani is the loudest stem for one qn
  only: qn 664, the f arrival of the printed p< f into the coda, +0.1 dB over the celli, 57 % of the dry 30-150 Hz. From
  665 it settles 5-11 dB under through 676. The bar-158 ff entry (628) sits -1.6 under. Rule 5 holds; no change.
- **Same dynamic across families.** Against c50 the upper strings rose about +0.8 dB at f (phrase shapes; kres51
  Violins I/II f +0.9 / +1.0). The same-dynamic offsets fell by that much for every other family: f horns -1.8 → -3.4,
  f trumpets +0.1 → -0.7, f trombones +0.8 → 0.0, f winds -4.2 → -5.3. The families still keep their mutual ratios
  (trumpet ≈ trombone ≈ horn + 2.7 dB), and every melody row passes. I do not propose a global change. Watch the trend.
- **S3.** The bar-62 subito falls 12.7 dB by +0.3 s (c50 13.0), with at most 9.4 dB in any 0.2 s: unchanged.
- **Not re-measured by this lens:** loops, accent fronts, S1 and S2.

Scripts and tables are in `/private/tmp/claude-501/mockup-loop/mvt1-c52-B/`: `flips.py`, `eqsim.py` + `eqrep.py`
(item 6 / 11 spectra), `eqvar.py` (315 Hz variants), `width.py` (item 5), `baltab.py` + `scen.py` (check table under
each change), `hpfix.py`, `ride.py`, `leads.py`. The 37 MB frame file was deleted; re-run `eqsim.py` (about 3 min) before
`baltab.py`.

Do not touch: c51's K-level balance (every check row passes except the ones named above); the c51 brass bells and
3.2 kHz bell; the timpani soft-roll shelf and HP_CURVE's timpani skip; the 600 ms basses pp cap; REP_SPLIT gaps and their
level returns; the celli 464-484 +4.2 dB; the Trumpets a2 coda bell; the Horn 3 [163.75, 168, -4] and cor anglais
[584, 608, +1.5] rows (put them into REAPER as ONE_TIME.md says); the existing +0.5 ride rows; deliver_master.py's
ratio, knee and top ride.
