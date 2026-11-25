# Cycle 35, critic B: balance and levels (on the c34 render)

**Method.**
- Stems and master from `cycles/c34/render/`. `build/parts.json` is identical to `cycles/c34/rendered_build/parts.json`, and c34 had no stem fix.
- **Level scale.** K-weighted: the BS.1770 response applied to 4096-point spectra, 25 ms hop, both channels summed, ungated. The stems sum to the master within 0.01 dB. On this scale the master reads about 3 dB under its gated LUFS.
- **Other bands.** Unweighted 20-100 Hz, 100-300 Hz, 300-2000 Hz and 2-5 kHz.
- **Note bodies.** From onset + 0.25 qn to 0.1 qn before the note's end. "Accompaniment" means the power sum of every other stem.
- **Printed dynamic.** From each track's `dyn_curve`. Score qn mapped to time on the parts.json tempo map.
- **Simulations.** dB arithmetic on the stem frames, with the master re-summed as stem power.
- **Labels.** "Measured" means a number from the render, parts.json, a table or an Opus state in `jobs/*.b64`. "Inferred" means a judgement about what a listener hears.

## Manual notes (B2: May 2021 HO manual pp. 194-200; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.194, p.196: the Mix page has a master channel per instrument and Sub Mixer channels, one per mic position. Each has its own volume, pan and a LOAD button. | `mix.json` `groups.*.mics` and the per-track overrides. These set the depth and presence of each family; the balance is in `gain_db` and the REAPER envelope. | Yes. Read from the 32 Opus states in `jobs/*.b64`: only the listed mics are loaded. Values: strings Close 0.60-0.66 + Main 1.0 (the patch defaults); winds Close 0.5 + Main 0.8; horns and the a2 track 0.5 + 1.0; trombones 0.49 + 1.0; tuba 0.45 + 1.0; timpani 0.2 + 0.5; harp and harmonics 0.6 + 1.0. The four DIV tracks are Close only (0.65-0.66), as p.89-90 says, and their gains of +4 to +8.5 dB make up the missing Main mic. The timpani's low mic volumes (about -14 dB Close, -6 dB Main) plus gain -7 keep the rolls under the texture (measured below: ranks 18-22 at the climaxes). |
| p.195: Store Mix / Restore Mix. | None. | Not used. The pipeline writes every state by script, which serves the same purpose and is reproducible. |
| p.196-197: an FX Bus channel holds the Reverb insert, and the Sub Mixer channels feed it through Reverb Send inserts. | The shared hall: `fx:0` in every patch. | Yes. Every state has the same `fx:0`: S. Cal Hall Perc TS 3.3 s, true stereo, high cut 5500 Hz, wet 2.0, volume 0.19. It is fed by a Reverb Send on each loaded mic channel. |
| p.198: each Effects Send has a LEVEL slider and a POST switch. For reverb, post-fader "is typically used" so that the send follows the channel fader. | `reverb.send_pre_fader` (c09). | The render departs from the manual's default, but the result is the same. Every send is pre-fader (`post: false`) with level = send x channel volume: strings 0.25 x 0.66 = 0.164, winds 0.6 x 0.5 = 0.30, and so on. The Opus channel volumes never change during the piece, so this equals a post-fader send. The balance consequence: all level automation is in REAPER's envelope after Opus, so the dry signal and the hall move together. Every fix below keeps each track's wet/dry ratio. |
| p.199-200: the EQ inserts (Bass Comp, Channel Equalizer, Equalizer). | The tone EQs in `mix.json` (`eq`, `loud_eq`, `mute_eq`, the side shelves) are ReaEQ after Opus. | Nothing is duplicated. The string states carry the patch's own Channel Equalizer (3.1 kHz -8, 15.3 kHz -4) and an SSL strip, both `active: false` (read). No Opus EQ is active, so ReaEQ is the only EQ. |

**MANUAL-GAPS items that touch this lens.**
- #8 (half-section patches for the 4 soli): the basses' 4 soli (bars 65-70 and 87-92) still play the full section through `SOLI_AS_META`. Their level is now on the c32 target (below), so this item is about timbre, not level.
- #4 (Mid instead of Close mics on the solo winds and Horn 1): would change presence, not the level relations measured here.

## 1. Clarinet 1's coda solo prints pp but plays at the level of the movement's p solos, 6-8 dB over its pp duet partner, the cor anglais (measured)

**Where.** Clarinet 1, qn 280-292 (bars 85-89: "dolce", niente < pp, then pp). Cor anglais, qn 286-292 (bars 87-89: "dolce", pp, the lower voice of the duet in parallel motion).

**Evidence (note bodies, measured).**
- Clarinet 1: 280 (ppp rising to pp) -41.2; 283 (pp) -38.8; 286 (pp) -37.8; 289 (pp) -40.5.
- Cor anglais at the same pp: 286 -45.3, 289 -46.4. Clarinet 1 leads by 7.5 and 5.9 dB in a duet where both parts print the same dynamic and the same "dolce".
- The movement's p solos: Oboe 1 p median -38.4, Horn 1 p -38.9, Flute 1 p -38.4, cor anglais p -38.8, Violin I solo p -39.9. The pp coda clarinet (median -39.3) is at their level. Mockup-kit LEARNINGS §16 measured about 4 dB per printed dynamic step on this pipeline, so a pp solo should sit about 4 dB under these.
- Clarinet 1's own table: across all its notes, pp (-41.5 median) is louder than p (-43.4), and the ppp entry at 280 is louder than its p accompaniment notes at 182-186 (-40.0..-44.1).
- Causes (read):
  - `mix.json` Clarinet 1 `soft_trim_db` pp +5.4 against p +1.4. This is c30's refit after CC1 put the clarinet on its soft layers.
  - `roles.json` Clarinet 1 stacks +3, +2.5, +2.5, +1.5 and +3 rows over 280-297, offset only by c32's -2.5 over 280-286.
  - `note_trims.json` 286 +4 and 289 +4.
  - Together the envelope is at +15 dB at 286 (vol_db +10.8, soft trim +5.4, gain -1).
- Over the pedal the clarinet is 9-12 dB over the loudest other stem (Vc div -50.3 at 282, celli -47.0 at 286).

**Why it matters (inferred).** In bars 87-89 the duet sounds like a clarinet solo with a faint cor anglais beneath it. The coda's pp sounds like p or mp, so the morendo of bars 91-92 has further to fall.

**Fix (level only; stem_fix can simulate it).** This goes the same way as c32's cut; it does not reverse it.
- `build/roles.json` Clarinet 1: add `[279.9, 291.9, -2, 0.5]`.
- `build/note_trims.json` Clarinet 1: `"286": 4` → `2.5`.
- `build/roles.json` Cor anglais: add `[285.9, 292.5, 2, 0.5]`.

**Simulated.**
- Clarinet 1: 280 -43.2, 283 -40.8, 286 -41.3, 289 -42.5. That is 2-4 dB under the p solos and still 7-9 dB over the pedal's loudest stem.
- Cor anglais: 286 -43.3, 289 -44.4.
- Clarinet 1 now leads the duet by 1.9-2.0 dB.
- Master: 280-283 -1.5, 283-286 -1.7, 286-289 -1.3, 289-292 -0.5 dB. The coda is mostly strings ppp to pp, so check the delivered 10th percentile after the render. `deliver_master`'s lift acts on soft passages and should take up most of this.

## 2. The violas are still 5-6 dB under Violins II at the ff of bars 61, 78 and 79: c34's climax hold raised the violins and celli but not the violas (measured)

**Where.**
- Violas, bar 61 (qn 204-208): ff tremolo double stop, "non div., molto sostenuto".
- Violas, bars 78-80 (qn 259-268): the f eighths into the cadence, then the ff held B flat 4 at 262/263.4. Violas div joins at 266.

**Evidence. Violas (with Violas div) minus Violins II (with Violins II div), per bar, measured:**

| Bar | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 78 | 79 | 80 | 81 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Va - Vln II (dB) | -7.4 | -6.8 | -0.8 | -3.0 | **-5.5** | -3.3 | -5.2 | **-5.4** | **-5.6** | -3.2 | +2.6 |

(Bars 57-58 print mp/mf against the violins' mf/f, so their gap is mostly printed.)

- c34 B #1 targeted -1..-3 dB at f/ff. Bars 59, 62 and 80 now meet it; bars 61, 78 and 79 do not.
- Cause in bar 61 (read, `score_config.py` "c34" block): C #1 added `LEVEL_SHAPES` +3 dB on Violins I and II and +3.5 dB on the celli over 204.2-211.6, and nothing on the violas. So the violas' +2.5 from B #1 was cancelled at bar 61 (c33 -1.9 → c34 -5.5 here; c34 CHANGES measured -3.6 for bars 61-62 together).
- Cause in bar 79 (read):
  - The violas carry `[262, 268, -1.5]`, `[262.5, 265, -2.5, 0.25]`, the c34 `_all` -1.5 and `dyn_trim` ff -1.5. Their vol_db is -3.7..-6.4 over 262.8-264.5, against -1.8..-2.6 for Violins II.
  - The violas' ff notes at 262/263.4 are -31.2/-30.3, 6-7 dB under their own ff at bar 61 (-24.3 tremolo).
- Norm (Rimsky-Korsakov, `reference-books/text/rimsky-principles.txt`, as c34 B cited): 14 second violins against 12 violas, "practically the same" weight. Each string section counts as two winds in forte.

**Why it matters (inferred).** The alto of the two ff chords that frame the second half is thin. In bar 78 the violas' eighths are the inner motion of the crescendo into the cadence.

**Fix (level only; rises only, so no tail is cut).** `build/score_config.py` (c35 block):
```
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [
    [(204.0, 0.0), (204.2, 2.5), (207.8, 2.5), (208.2, 1.0), (211.6, 1.0), (211.9, 0.0)],
    [(258.6, 0.0), (259.0, 2.5), (265.6, 2.5), (266.0, 1.0), (267.75, 1.0), (268.25, 0.0)]]
LEVEL_SHAPES["Violas div"] = LEVEL_SHAPES.get("Violas div", []) + [
    [(265.9, 0.0), (266.0, 1.0), (267.75, 1.0), (268.25, 0.0)]]
```

**Simulated.**
- Va - Vln II: bar 61 -5.5 → -3.0; bar 62 -3.3 → -2.3; bar 78 -5.4 → -2.9; bar 79 -5.6 → -3.1; bar 80 -3.2 → -2.2.
- Master: +0.0..+0.2 dB. Bars 61-62 move under 0.15 dB and bars 78-80 by 0.1-0.2 dB, so the climax order is unchanged.
- The c34 limiter was 2.6 dB and the master true peak -0.3 dBFS. If the delivery limiter goes over 3 dB, take Violins I -1 dB over 208.2-211.6, where it leads Violins II by 4-5 dB. That brings the master at 208-212 to -0.15 dB net.

## 3. Horn 3's two f notes in bars 79-80 are cut 5 dB by a pitch trim copied from Horn 1 (F4 body -5) and sit 3-4 dB under Horn 4 (measured)

**Where.** Horn 3, qn 262 and 265 (F4 sounding, MIDI 65, f, bars 79-80). These are the upper note of the Horns 3-4 chord under the Horns 1-2 a2 line.

**Evidence.**
- `build/pitch_trims.json` gives Horns 1-4 the same entry: `"65": {"early": 1, "body": -5}` with `_all_arts`. Series 1 c06 measured that bloom on Horn 1's legato F4, with CC11 dynamics. Since c30 the horns' dynamics are on CC1 layers, so the old measurement no longer describes these samples.
- Horn 3 plays F4 nowhere else in v600 (Horn 4 never plays it).
- Horn 3's envelope steps from +1.9 to -3.9 dB at 262.49, once the +1 "early" part ends. Horn 4, holding Ab3 at the same printed f, is at +4.1..+5.0.
- Bodies: Horn 3 262/265 -34.6/-34.5. Horn 4 262/265 -30.2/-31.2. Horns 1-2 a2 -25.6..-26.6.
- The control is Horn 3's own untrimmed f notes. E4 at 267 (f, rising) is -30.8, level with Horn 4. Its f notes in bar 61 (204-210) are -26.4..-28.1.
- So the -5 is the only reason for the 3-4 dB deficit.

**Fix.**
- `build/pitch_trims.json` "Horn 3": add `"_skip_onsets": [262.0, 265.0]`. The key already works this way for Horn 1.
- Expected: Horn 3 at about -29.6 on both notes, within 1 dB of Horn 4. Master under +0.1 dB.
- After the render: compare the F4 bodies with Horn 4 and check for a bloom in the first 1 s (the original reason for the trim). If F4 blooms more than 3 dB over its body at CC1 86, use `"body": -2` for Horn 3 instead of the skip.

## 4. Flute 1's printed counter-line in bars 41-44 (pp < p > pp) ends 11-13 dB under the cor anglais solo, which prints only one step louder (measured)

**Where.** Flute 1, qn 126-139 (bars 41-44; "1.", pp < p, decrescendo to pp, a high descant: A flat 5-F6). The cor anglais solo "dolce cantabile" prints p < mp > p over the same bars.

**Evidence (1 qn frames, measured).**
- Flute minus cor anglais: 127 -3.5, 128 -5.6, 129 -9.3, 130 -3.3, 131 -4.0, 132 -5.0, 133 -5.0, **134 -7.9, 135 -12.8, 136 -11.9, 137 -11.1**.
- In 134-137 the flute (-47..-50.8) is only 1-3 dB over the violas' pp accompaniment triplets (-50..-53.6).
- Cause (read): through the shared decrescendo of 131-136 the flute falls from CC11 45 to 34 plus `hpgain [131, 136, -2.5]` (11 dB in level). The cor anglais falls from 65 to 55 under its `[124, 137, 2]` solo role (2-3 dB).
- The two parts print the same hairpin, one step apart. LEARNINGS §16 measured about 4 dB per step, so the target is a gap of about 4-7 dB.

**Why it matters (inferred).** The flute's held pp E flat 6 at the end of bar 44 drops out instead of closing the duet. The two-voice texture of bars 41-44 reads as a cor anglais solo.

**Fix.** `build/score_config.py`:
```
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES.get("Flute 1", []) + [[(133.8, 0.0), (134.3, 5.0), (139.0, 5.0), (139.5, 0.0)]]
```
The shape is released after the flute's last note ends (139.0).

**Simulated.** Gap at 134-138: -2.9, -7.8, -6.9, -6.1, -1.0 (at 138 the cor anglais is ending its phrase). Bars 41-43 unchanged. Master +0.4..+0.9 dB at 134-138. At 138-139 it is +1.5 dB: the flute holds alone there as the cor anglais ends, which fills the gap before Oboe 1's entry (inferred). If that is too much, end the shape at 3 dB from 138.

## 5. Two solo entries are masked for their first beat by a pp accompaniment: the bass clarinet's pickup run in bar 31 and Oboe 1's pickup at qn 139 (measured)

**Bass clarinet, qn 91-93 (bar 31, "solo, espr.", p, the rising eighths into E flat 3).**
- Measured (each eighth from onset + 0.05 qn to its end): in 300-2000 Hz the solo leads Bassoon 2's pp A flat 2 pedal (qn 90-100) by only -0.2, +0.8, +2.8 and +3.5 dB on its four eighths. Over the whole accompaniment (K-weighted) it is at -0.7, +1.1, +5.8 and +3.5 dB.
- Causes (read):
  - Bassoon 2's `soft_trim_db` pp +8 is the largest soft trim in the orchestra (global +3).
  - Its envelope swells +0.1 → +1.5 dB over 90-94, exactly under the entry.
- Fix: `build/roles.json` Bassoon 2 `[90.4, 96.0, -3, 0.4]`.
  - The pedal falls 3 dB over 0.4 qn before the solo's first note, inside the bassoon's held note. This is slow, before any tail, and at a constant dynamic.
  - Simulated: 300-2000 Hz lead +2.8, +3.8, +5.8 and +6.5 dB on the four eighths. Over the accompaniment: +0.9, +2.8, +7.6 and +5.2 dB.

**Oboe 1, qn 139 (bar 44 beat 4, "dolce espr.", p, the pickup to the B flat minor theme).**
- Measured: the pickup body is -46.2 against -37.9 for the next note.
- The celli's pp pickup on the same beat ("sul D") swells from -53.5 to **-38.2** at 139.8. That is the head of its legato transition (v124) into 140.
- So the celli are up to 9 dB over the oboe's p entry, and the oboe's phrase is heard only from 140.
- Fix:
  - `build/score_config.py`: `LEVEL_SHAPES["Violoncellos"] += [[(139.3, 0.0), (139.5, -7.0), (140.15, -7.0), (140.4, 0.0)]]`. This dips the transition head; the celli's 140 note is back at full level by 140.4.
  - `build/note_trims.json` Oboe 1: `"139": 2`.
  - Simulated at 139.4-139.9 (0.1 qn frames): celli -45.2..-52.9 (peak -45.2 at 139.8), oboe -43.0..-46.2. The oboe is level with or over the celli on every frame.
- Low priority (one beat), but these are the first notes of two solos.

## Checks asked for in this lens

All measured unless marked inferred.

**Solos over their accompaniment (note bodies).** Each entry gives the median and minimum over the accompaniment sum, then over the loudest single stem.

| Solo | Over accompaniment (median / min) | Over loudest stem (median / min) | Notes |
|---|---|---|---|
| Horn 1, bars 7-14 | +1.9 / -1.3 | +5.5 / +3.2 | Lowest at qn 30, Bassoon 2 |
| Oboe 1, bars 15-16 | +4.4 / +0.4 | +6.2 / +4.3 | |
| Solo violin, bars 17-18 | +5.0 / +0.2 | +8.8 / +4.7 | |
| Oboe 1, bars 19-20 | +4.3 / -1.6 | +6.7 / +2.3 | 54 entry: celli |
| Solo violin, bars 21-22 | +2.1 / -1.2 | +6.5 / +2.6 | |
| Bass clarinet, bars 31-36 | +1.8 / -0.7 | +3.4 / +1.4 | Finding 5. At 98 it is level with the cor anglais, whose p entry here also carries the line (inferred) |
| Flute 1, bars 37-40 | +3.9 / +1.3 | +8.2 / +4.5 | |
| Cor anglais, bars 41-44 | +3.7 / -0.2 | +6.5 / +2.8 | |
| Oboe 1, bars 45-47 | +1.5 / -5.1 | +6.6 | The -5.1 is the 139 pickup, finding 5. The celli double the theme an octave lower, so a smaller margin is right here |
| Cor anglais, bars 47-50 | +3.9 / +1.0 | +6.7 / +3.9 | |
| Clarinet 1, coda | | 9-12 dB over the pedal | Too far over: finding 1 |

**Climaxes, bars 61-64 and 79-82 (group power sums, 2 qn frames).**
- **qn 204-212.**
  - strings -12.6..-14.5;
  - winds -15.7..-18.3;
  - horns -18.9..-21.8;
  - low brass -19.4..-21.3;
  - timpani (the printed f roll) -32.2..-48.2, ranked 22nd of the sounding stems.
- **qn 262-270.**
  - strings -18.7..-22.8;
  - winds -18.4..-22.7;
  - horns -24.0..-28.0;
  - timpani -31.7..-35.6, ranked 18th-19th.
  - The bar 81 roll falls with its printed decrescendo.
- **Timpani rule.** Only in the printed pp < f crescendo roll at 202-204 does the timpani rise to 7th (-26.9), as the score asks. Dan's roll rule is met.
- **Low brass.** At f the trombones (Tbn2 -23.0..-24.2, B.tbn -24.1..-25.8, tuba -25.4..-29.5) are 4-6 dB over single horns at f. That fits Rimsky's one trombone ≈ two horns. As a group they are 6-7 dB under the ff strings. In bars 63-64 Trombone 1's ff quotation (-20.5..-21.0) leads while the strings fall from sf to p as printed. Nothing covers.
- **Climax order.** Plain RMS per bar: bars 61/62 -14.5/-15.0 against bars 79/80 -19.6/-20.1. Findings 2-3 add at most 0.2 dB to either.

**Dynamic mapping across families (median note bodies, notes of 0.75 qn or more).**
- **pp.** Winds -43.5..-47.6, strings sections -44.9..-47.1, basses -49.9 (low register on the K scale). Consistent.
- **p.** The solos sit at -38.4..-39.9 and the accompanying winds at -41.4..-44.9. The violins and celli are at -37.9..-39.7; the violas at -43.5 are mostly inner and pp-marked passages.
- **ff.** Single winds -26.6..-30.7 and string sections -23.8..-24.7. That is 3-6 dB, Rimsky's forte ratio, except for the violas (finding 2).
- **Exceptions.** Clarinet 1, whose pp is louder than its p (finding 1). Basses arco p -45.7 against pp -49.9 is a clear step; the pizzicato p notes (-53.7) are short notes measured in their decay, not a mapping error.
- **Harp.** p in bars 37-44 peaks at -42..-47, against pp in bars 9-14 at -40..-47. The p chords there are low bass-clef chords doubling the pizzicato basses, and the K scale discounts that register. The p of bars 55-56 (-37) and 75 (-35) sits clearly over the pp of 53-54 (-40) and 71-74 (-42). No change.

**Half-section DIV and 4 soli tracks against the full sections.**
- Violins II div (Flautando, bars 37-40, pp) is within 0-2.8 dB of the other half on the Violins II track. Together they are 7-12 dB under Flute 1.
- Violas div against Violas: within 1-4 dB in bars 23-30 and in the coda. In bars 87-91 both halves together are 1-3 dB under Violins II.
- Celli 4 soli on the DIV track (bars 83-86, ppp): -48.3..-51.8, against the tutti basses' ppp at -50.3..-51.2.
- Basses' 4 soli: bars 87-92 at -51.6..-54.6 (median -53.4) meet c34 B #3's target of 3-4 dB under their tutti pp (-49.9). Bars 65-70 are 7-16 dB under Horn 1's solo.

**Bass (master 20-100 Hz and 100-300 Hz power against the K-weighted total, 1 s windows; the Dvořák 9/i mp3 measured the same way).**
- 20-100 Hz: soft 30% -14.4 (ref -17.5), middle -18.3 (-21.9), loud 10% -21.3 (-25.3).
- 100-300 Hz: soft -5.1 (-7.5), middle -7.8 (-7.1), loud -8.4 (-6.7).
- c33: 20-100 Hz -14.2 / -19.5 / -20.3.
- The heaviest bars come from the score's own low passages, not from a boomy stem:
  - Bars 83-84: the coda's ppp A flat 1/A flat 2 pedal, about -8 dB in 20-100 Hz. The basses supply 34-44% and the celli 4 soli 17-25%.
  - Bars 31 and 35: the bass clarinet's chalumeau (v600 put it an octave lower), with 93% from the bass clarinet itself.
- The loud passages are lighter in 100-300 Hz than the reference. The mp3 reference is lossy, and the Brahms references in `metrics.md` carry far more 20-100 Hz. The bass is solid but not boomy (inferred). No change.

**Track gains and soft trims.** Two tables matter for the findings above:
- Clarinet 1's soft trim pp +5.4 is higher than its p trim (+1.4), which inverts the step (finding 1).
- Bassoon 2's pp +8 is the largest soft trim in the orchestra (finding 5).

The other soft trims rise from ppp to p or stay flat. The DIV tracks' gains (+4 to +8.5) match their Close-only states, and their levels against the sections are as listed above.

**Do not touch:**
- The climax order, and the timpani and low-brass levels at bars 61-64 and 79-82.
- The c34 bar 61-62 string holds for Violins I/II and celli, and the cadence `_all` -1.5.
- Violins II's f/ff trims and roles.
- Violas `dyn_trim_db` f 0 / ff -1.5, and the c34 viola role at 249.9-258.5.
- Trombone 1's quotation levels, accents, CC7 lanes and the 2 kHz shelf.
- Flute 1's CC7 at 211.96-213, and its bar 79 -6.
- The bar 63 and niente CC7 lanes.
- The solo levels of Oboe 1, the Violin I solo (CC1 72, gain +0.4), Flute 1 in bars 37-40, the cor anglais in bars 41-50, and the bass clarinet's bar 31 trims.
- The celli 4 soli on the DIV track, and the basses' coda 4 soli at +2.
- The Violoncellos 286 bloom role.
- The Cb and timpani side shelves.
- The horn CC1 map and the soft-horn loud_eq.
- Harp env_sustain 1.0, and the harmonics level (their peaks are 2-4 dB over the coda pedal).
- The timpani mic volumes (Close 0.2 / Main 0.5) and gain -7.
- The pre-fader send scheme (send x channel volume).
