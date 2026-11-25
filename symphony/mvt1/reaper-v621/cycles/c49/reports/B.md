# Critic B, cycle 49 (render c48): balance and levels

## Manual notes (second round, cycles 48-51: pages picked for this lens's open problems; MANUAL-GAPS.md and DIGEST.md sections 2, 8 and 9 read)

Pages read in full from the May 2021 HO manual: p.64, p.89-92, p.150-151.

| Source | What it says | Where it applies here | Followed in c48? |
|---|---|---|---|
| p.64, p.151 | CC7 (or the fader) sets a track's level against the others. CC11 shapes the line and crossfades the dynamic layers. Velocity sets loudness only on shorts. | Every fix below. | Yes. Every balance correction is in the volume envelope (roles, LEVEL_SHAPES, note trims), and CC11 follows the printed dynamic (read in parts.json). All fixes below are level changes only. |
| p.64, p.151 | In the LITE string instruments, CC1 controls dynamics and vibrato together. In the MAX instruments CC1 is vibrato only. | Celli strokes on "Sus Marc LITE" (84, 156, 284, 448, 456). | CC1 tracks CC11 at the strokes (156: CC1 90, CC11 88; 448: 70 / 69; 456: 79-80 / 79; read), so the LITE row plays the printed layer. Its body is still quieter than Sus MAX at the same values (finding 2). |
| p.91-92 | The Marcato Sustain plays a marcato sample that "ends relatively quickly" over looped sustain samples, for "extra power at the start of the note". | Celli bar 40 (qn 156), Sus MAX in c47 and Sus Marc LITE in c48. | Followed as an attack. The level after the marcato part is 1.3-4.4 dB under c47's Sus MAX body, so the c47 body cut written for the Sus MAX bloom now cuts too deep (finding 2). |
| p.89-90 | Divisi patches are Close only, and "the loudness of a divisi part is not much less than if the whole section were playing the part". | Cello solo (DIV A) and the f62 aliases. | No balance issue measured: the Cello solo is +8.4 dB (median) over the loudest other stem at 680-696 with the cor anglais answering under it. |
| p.150 | Velocity maps samples by range (p 1-25, mp 26-45 and so on) and suits shorts. | Percussion and timpani strokes. | Tam-tam fff is the loudest stem at 484-491, as printed. The suspended cymbal's pp roll stays under -30 dB re master until 633, then peaks at the fff stroke (-19). Unchanged since c47. |
| MANUAL-GAPS #12 | Felt Cresc rolls have never been tried. | The bar-11 roll. | Not needed: the c48 role brought it to -12..-14 re master (below). |

## Method

- Render: `cycles/c48/render/` (40 stems as delivered; the basses carry the 450 ms test audio up to qn 695.8). Compared with `cycles/c47/render/`.
- Data: `build/parts.json`, `cycles/c48/before/parts.json` (the c47 data), `build/score_config.py`, `build/roles.json`, `build/note_trims.json`, `build/mockup-events.tsv`.
- Level frames: 4096-point FFT, 50 ms hop, on every stem and the master, K-weighted in the frequency domain, plus octave bands. "re M" means the stem minus the master. "Over the loudest other" means the stem minus the loudest single other stem in the same window.
- Short or staccato lines were also measured at their attacks: for each note, the peak frame in its first 0.4 qn against the competing line in the same frame. Clarinet contours use 40 ms RMS frames taken straight from the wav.
- Same-dynamic scan: per beat, the tracks whose printed dynamic is flat (no change, no hairpin) and whose notes cover at least 75% of the beat. Each track is compared with the median of the others at that dynamic, where at least five share it. Alias stems are summed into their source track.
- Simulations scale stem frames, or the stem's samples for the clarinet, by the proposed shape and add the difference to the master.
- Score pages read: 2, 4, 5, 6, 7, 8, 15, 17.

## The coordinator's c48 checks

- **Basses against celli, bars 6-7 and 13-14.**
  - Per qn 20-27: c47 -3.9 / -11.8 / -15.3 / -12.9 / -3.5 / -9.3 / -10.3 / -10.7, c48 +0.4 / -6.8 / -10.3 / -8.1 / +0.9 / -4.3 / -5.1 / -6.0. Span -9.5 -> -4.9 dB.
  - Per qn 48-55: span -6.6 -> -3.1 dB.
  - Bar-5 C2 re M -0.6, unchanged. The cor anglais solo is still 6-15 dB over the basses.
  - **Done** (measured).
- **Coda Clarinet 1.**
  - Re M per qn 699-706: -5.1 / -2.3 / -5.1 / -3.5 / -3.2 / -3.9 / -4.3 / -5.1.
  - Over the loudest other: +4.8 / +8.7 / +1.0 / +4.1 / +7.8 / +4.2 / +3.4 / +1.2. It is the top voice on every beat.
  - The +8.7 at 700 is the arrival of the held C5, not the body (finding 1).
- **Bar-11 roll.**
  - Re M per qn 40-44: -13.7 / -13.6 / -12.0 / -11.3 / -9.3. Rank among the stems 9 / 10 / 8 / 5 / 2. In c47 it was 6 / 5 / 3 / 2 / 2.
  - It now sits under Violins II and the celli (-8..-13 re M) until the f stroke.
  - **Done** (measured).
- **Bar-81 tremolo.**
  - Violins II re M per half qn 320.5-323.5: -7.5 / -8.0 / -8.8 / -5.0 / -5.4 / -7.4 / -7.7 (c47 -5.5..-3.1). It is no longer the loudest stem from 321.
  - The f entry (Violins I + Flute 1) is still level with or under single accompaniment voices on its first two beats (finding 4).
- **Lead moves and swell fills.**
  - Master per bar c48 minus c47: within ±0.7 dB in every bar except 84 (+1.6), 86 (+1.0), 87 (-3.4) and 176 (-1.0).
  - Bars 84-87 come from the A #1 fugato shapes. The cello subject's staccato quarters at 343.5-347 are 2.5-3.5 dB under c47, and the head accents are 3.6-4.5 dB over.
  - Bar 176 comes from the Clarinet 1 cut.
  - Per half beat, the stem changes of 1.5 dB or more within 15 dB of the master are almost all at moved onsets (timing, not level).
  - Two changes are on unchanged data:
    - Violins II at 162-165 (bar 41, sf > mf inner note) is 4-7 dB under c47 with identical parts.json data. This is render variance; the horns' ff a2 melody is on top there, so it does no harm.
    - The celli at 157-159.6 are lower because of the row change (finding 2).
- **Delivered** (recomputed from the mp3):
  - p10 -30.4, maximum -11.4, span 19.0 dB.
  - S max 160 -11.4 > 122 -12.1 > 167-170 -13.5 > 26 -14.3. Climax order unchanged.
- **Timpani rolls (Dan's priority).** Per 1 qn window, the roll's rank among 39 stems and the roll minus the loudest other stem:
  - 11-12 pp<f: rank 2-13, -5.3 / -1.0. The -1.0 is the f stroke at 44.
  - 13-14: rank 5-11, -17.6 / -10.0.
  - 40-43: rank 3-15, -9.8 / -1.5. The -1.5 is at 159, in the printed pp<ff.
  - 80-81: rank 3-9, -5.9 / -1.7. The -1.7 is at 323, in the printed p<ff.
  - 117-130: rank 2-23, -8.7 / -1.6.
  - 144-146: rank 2-9, -5.8 / -2.9.
  - 158-161: rank 2-17, -4.6 / -0.4. The -0.4 is at 636, the fff stroke.
  - 166-169: rank 1-18, -7.2 / 0.0. The 0.0 is at 664, the f arrival stroke.
  - 174 / 181-182: -18.4 / -9.4 (median).
  - Every beat within 3 dB of the top falls on a printed stroke or the end of a printed crescendo. No held roll covers a part. **Rule met** (measured).
- **Same-dynamic scan.** Median against the other tracks at the same dynamic:
  - Most tracks are within ±3 dB at every dynamic. Violins I runs +3.5..+6.4 as the lead.
  - **Double basses**: pp -3.1, p -5.0, mp -6.5. Their notes double the celli an octave down at -3..-6 dB (coda 696-719, bars 145, 163). K-weighting takes 6-10 dB off 40-80 Hz, so no change is proposed.
  - **Clarinet 1**: pp +6.1 / p +4.0. These beats are the coda solo and bars 145 / 126 / 168. Bar 145 was settled in c47. The coda is finding 1.
  - **Trumpet 1**: f +2.5, ff +4.2. **Trombone 1**: f +3.6. Both sit within Rimsky-Korsakov's ratio for loud passages: "Trumpet = Trombone = Tuba = 2 Horns", "Horn = 2 Clarinets = 2 Oboes" (Principles, Comparison of resonance).
  - The highest Trumpet 1 beats (bar 82, 325-330, +9..+10) double the ff motif in unison with Violins I. Violins I keeps 2.8-5.7 kHz at all of them (-3.7..-4.9 dB share against the trumpet's -8.7).
  - **Trumpets a2** in 167-170: +1.1..+4.4 dB over Horns a2 on the ff tune. That is RK's 2 horns per trumpet, and it was kept by the c48 B "Do not touch".
  - The second-chair winds sit under their firsts at f: Flute 2 -2.5, Oboe 2 -3.7, Clarinet 2 -1.9. These are inner chord notes (bars 69-72, 167-169) with no printed role. Inferred low priority.
- **Family shares at the tuttis** (wind / brass / strings re M):
  - Bars 25-32: -5.3 / -4.2 / -4.7.
  - Bar 82: -7.9 / -4.1 / -5.2.
  - Bars 115-122: -5.0 / -4.4 / -6.0.
  - Bars 158-161: -6.2 / -4.4 / -5.0.
  - Bars 167-170: -6.9 / -3.1 / -6.0.
  - No family dominates. Brass leads by 1-3 dB only at the brass-tune passages.
- **Percussion.**
  - Tam-tam fff at 484-491: the loudest stem by +1..+6.5 dB.
  - The bar-175 pp soft-stick tam-tam starts at -8 re M (rank 3, under the trombones' pp chorale) and falls to -12..-20. Its 86 Hz partial takes 1/3-1/6 of the coda's 20-180 Hz band, alongside the basses and celli. That is the intended dark shimmer, and no change is proposed (inferred).
  - The suspended-cymbal stroke and the K Crash ring together take most of the master's 5.7 kHz+ band at 635-639 (-3 / -6 dB share). Unchanged.

## Findings, ranked by what a listener would gain

### 1. Bar 176: the coda clarinet solo's held C5 swells twice in its first beat, 5-6 dB over its own body (measured)

**Where.** Clarinet 1, qn 700.0-700.7. The C5 is held for 6 qn after the D5 pickup, pp espr., over the pp trombone chorale and pp strings. This is the most exposed solo note in the coda.

**Evidence (measured, 40 ms frames of the c48 stem, body = median of 700.8-701.8 = -47.3 dB):**
- Arrival frames relative to the body:
  - 700.01-700.20: +3 / +3 / +3 / +4 / +4.
  - 700.25-700.34: +2 / 0 / 0 (dip).
  - 700.39-700.63: +3 / +5 / +4 / +6 / +5 / +3.
  - From 700.68: body.
- Maximum over the body: +5.8 dB, so the note sounds as two bulges ("wah-wah") before it settles.
- The C5's peak is 5.9 dB over the D5 pickup. The master bulges 2 dB at 700.4-700.6 (-40.1 against a -42.0 median after).
- Over the loudest other stem: +11 at 700.5, against +3..+4 on the body.
- Causes:
  - The sample has a bloom at about 0.45 s after the note change, present in c46, c47 and c48 alike (-39 / -40 against a -46 body in c46).
  - The envelope adds to it. `vol_db` is +4.5 at 700.0, then the c47 fill `LEVEL_SHAPES["Clarinet 1"] [(700.14, 0), (700.20, 5), (700.40, 5), (700.50, 0)]` (score_config c47 block), then a drop to -5 by 700.72 (read).
  - The fill filled the c46 dip at 700.3 (c46 -49/-50 there). Its falling edge (700.40 +5 -> 700.50 0) and the base envelope's ramp both lie over the bloom.

**Fix (level only; can be a stem fix).**
- Add one row to `LEVEL_SHAPES["Clarinet 1"]` in the c49 block of `build/score_config.py`: `[(700.02, 0.0), (700.06, -3.0), (700.24, -3.0), (700.28, 0.0), (700.38, 0.0), (700.44, -4.5), (700.64, -4.5), (700.72, 0.0)]`. Keep the c47 fill and the c48 -2 dB row.
- Simulated on the c48 stem (samples scaled):
  - Arrival frames relative to the body: +3 / +1 / 0 / +1 / +2 / +2 / 0 / 0 / +1 / 0 / 0 / +1 / +1 / 0 / 0 / -1.
  - Maximum over the body 5.8 -> 2.6 dB. No new dip (minimum -0.6).
  - Master bulge -40.1 -> -41.4, level with the next beat.
- Check the shape against the envelope build_reaper will actually write (`cycles/c48/actor_scripts/simenv48.py`), because shape points between grid points can read the base envelope's step value (CHANGES c48, Values 4).

### 2. Bar 40: the celli's f bass note lost 3-4 dB with the Sus Marc LITE stroke, on top of a body cut written for the Sus MAX bloom (measured)

**Where.** Violoncellos, A-flat3 at qn 156.0-160.0. It is printed f, crescendos to the bar-41 sf, and is the bass of the bar-40 crescendo under the Violins I run and the horns' f.

**Evidence (measured).**
- Celli level c48 minus c47, same span:
  - 155.75-156.25: +2.6. The stroke front is louder.
  - 156.25-157: +1.4.
  - 157-158: -1.3.
  - 158-159: -4.4.
  - 159-159.6: -2.1.
- The volume envelope is 1.0-1.5 dB higher in c48 at 156-157.5 (read). So the row change alone takes 2.5-6 dB off the body, as p.91-92 describes: the marcato sample ends quickly, leaving the LITE sustain.
- Celli over the loudest other per half qn 157-159.5:
  - c47: +0.2 / -1.6 / +3.1 / +4.0 / -4.0 / +3.3.
  - c48: -0.2 / -4.1 / -0.8 / -1.1 / -5.4 / -3.5.
  - Re M -8.0..-13.6 (c47 -5.5..-11.7).
- c47 B #4 deepened the body cut to -8 dB over 157.5-159.6 (`_c45b4`, score_config c47 block) because the Sus MAX bloom made the note the loudest stem by 6-7 dB. With the LITE row that bloom is gone, but the cut stayed. The bass now falls 4-5 dB under its c47 target.

**Fix (level only; can be a stem fix).**
- In the c49 block of `build/score_config.py`, restore the c45 body value on this note: replace `(157.5, -8.0), (159.6, -8.0), (159.75, -5.0)` in the `_c45b4` row with `(157.5, -5.0), (159.6, -5.0), (159.75, -3.0)`.
- Simulated (+3 dB over 157.5-159.6): celli over the loudest other -0.2 / -4.1 / -0.8 / -1.1 / -5.4 / -3.5 -> +0.7 / -1.1 / +2.2 / +1.9 / -2.4 / -2.9. This is about c47's planned margin, without the c46 bloom. Master change under 0.4 dB.
- The same reasoning applies to celli 456, but there the c48 body rises smoothly with the stringendo crescendo (25.9 / 30.1 / 33.6 / 40.8 / 39.3 per segment). No change there.

### 3. Fugato, bars 94 and 96: the last subject entry (Violins I + Flute 1, f) starts level with the Violins II countersubject (measured)

**Where.**
- qn 372.5-373.5: the Violins I / Flute 1 subject's pickup and accented head. Violins II starts its countersubject at 372 with a held B-flat4, f.
- qn 380.5: the subject's last staccato before the bar-96 ff stretto. Violins II is crescendoing into its own 381 ff entry.

**Score (build/mockup-events.tsv).** The fugato enters cello (mf, 336.5), violas + Bassoon 1 (mf, 348.5), Violins II + cor anglais (f, 360.5), then Violins I + Flute 1 (f, 372.5). Each earlier voice continues as a countersubject at the same printed dynamic.

**Evidence (measured).**
- Subject peak over the countersubject in the same frame:

| Entry | Head and first notes | Later notes |
|---|---|---|
| Violas + Bassoon 1 (348.5-360) | +5.1 / +9.8 / +8.1 | +3.1..+10.8 |
| Violins II + cor anglais (360.5-372) | +8.2 / +5.7 / +12.1 | +2.7..+8.2 |
| Violins I + Flute 1 (372.5-380.5) | **-0.4 / +0.3** / +9.6 | +2.7..+7.6, then **-1.5** at 380.5 |

- Only the last, most important entry fails to stand out at its head. Adler (Study of Orchestration, p.128) lists "thinning the counterpoint to let the main theme break through" as the first remedy when a subject and countertheme share a register.
- The A #1 fugato head / staccato shapes did their job: accent heads +1.4..+2.6 dB over their staccatos. The earlier entries' staccato quarters stay +2.7..+8.2 over the countersubject at their attacks.
- Per-beat means make the countersubject look louder (-1..-5 dB) between the staccato attacks. That is the gaps between the staccatos, not a balance fault.

**Fix (level only).**
- In `LEVEL_SHAPES["Violins II"]`, add `[(371.9, 0.0), (372.05, -3.0), (373.6, -3.0), (374.0, 0.0)]` and `[(380.25, 0.0), (380.4, -3.0), (380.85, -3.0), (380.95, 0.0)]`. The second ends before the 381 ff accent, so the stretto entry keeps its level.
- Simulated: subject over the countersubject at 372.5 / 373.0 / 380.5: -0.4 / +0.3 / -1.5 -> +2.6 / +3.3 / +1.5.
- The printed cresc. from 376 is untouched between the two rows. Master change under 0.5 dB.

### 4. Bar 81: the f motif entry (Violins I + Flute 1) is still under single accompaniment voices on its first beats (measured; audibility inferred)

**Where.** qn 322.5-324. Violins I / Flute 1 enter f (pickup 322.5, accented E-flat6 at 323) over the p<ff tremolo (Violins II, violas), the basses' p<ff whole note and the timpani's p<ff roll.

**Evidence (measured).**
- Motif (Violins I + Flute 1 + Flute 1 stac) minus the loudest single accompaniment voice per half qn 322.5 / 323.0 / 323.5: -1.8 (Violins II) / +1.9 (Violins II) / -3.2 (Double basses).
- In 1/8-qn frames over the accented note 323.0-324.0:
  - Violins I: 31 26 15 12 27 40 41 39.
  - Basses: 36 33 31 27 31 30 28 25.
  - Timpani: 37 40 37 33 37 42 35 32.
  - Values are dB on the analysis scale. The Violins I accent's body sits under the basses and the roll for its first half.
- The high register helps it carry (inferred). c48's Violins II cut fixed the worst of it, so this is the remainder.

**Fix (level only).**
- In `build/roles.json`, add Double basses `[320.75, 324.0, -2.0, 0.25]` and Timpani `[321.0, 324.0, -2.0, 0.25]`, and deepen the c48 Violas row from -1.5 to -3.0.
- Each crescendo still grows; it arrives at the ff downbeat 324.5 at full level through the 0.25 qn end ramp.
- Simulated (basses and violas only): motif minus loudest at 323.5 -3.2 -> -1.2.
- The timpani row is inferred and was not simulated. Check that the roll's growth over bars 80-81 stays above +3 dB (the c46 ramp rule).
- This is a smaller gain than findings 1-3. Do it only if it costs no extra render.

### 5. Bars 147-152: the cor anglais's p dolce answers sit 6-10 dB under the tune, and the first pickup is lost (measured level, inferred audibility)

**Where.** Cor anglais, qn 586.5-588 (first answer, three-eighth pickup into a half note), 594.5-596, 602.5-604. The tune is in Horn 1 (mp dolce), violas and celli (mf dolce).

**Evidence (measured).**
- Cor anglais mean minus the tune's sum per note:
  - 586.5: -14.2. 587.0: -9.1. 587.5: -6.6. 588.0: -8.3.
  - Then -6.0..-10.5.
- Peak minus the loudest single tune voice: -11.2 on the first pickup note, -1.5..-6.6 on the rest.
- Re M: -14.7 on the first note, then -7..-11.5.
- One step under mp and two under mf is about right for a p answer. But the first note of the first answer, -11 dB under the tune at its own peak, is not heard, so the answer starts on its second note (inferred).

**Fix (level only).** Add a note trim of +3 dB on Cor anglais 586.5 in `build/note_trims.json`, as a step on the attack, ramped out by 587.0. Leave the rest alone: c41 B #1 put the answers under the tune on purpose.

## Do not touch

- The c48 B #1-#4 rows: the basses' bars 6-7 / 13-14 trims and roles, the Clarinet 1 -2 dB shape with the `[699, 712, 2]` role, the bar-11 timpani role and the bar-81 Violins II / violas rows.
- The A #1 fugato head / staccato shapes. Finding 3 only thins the countersubject.
- Every timpani roll level and ramp: no held roll is within 3 dB of the top except at printed strokes.
- The tam-tam, suspended-cymbal and K Crash levels, including the bar-175 pp tam-tam.
- The Trumpets a2 / Horns a2 / violas tune in bars 167-170, and Trumpet 1 in the bar-82 unison.
- The family balance at the tuttis.
- The hall and every send.
- Delivery: span 19.0 dB and climax order 160 > 122 > 167-170 > 26.
- On the open basses cap question: the bars 1-174 pp chord changes read -11.7..-15.4 dB re the new note at 450 ms against -9.8..-11.7 at 600. From a balance view, keep the delivered 450 ms up to 695.8 (a coda-only 600 ms alias) rather than letting a rebuild play 600 throughout.
