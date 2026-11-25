# Cycle 29, critic C (blend and space): the c28 render of v600

Lens: one room. Covers reverb, seating and panning, mic positions, tone matching between sample sets (DIV tracks against their sections, harp harmonics against the harp, muted against open strings), and low-end build-up against several reference recordings. Material: the c28 stems and master, the c27 and c26 renders for comparison, `build/parts.json`, `build/mix.json`, the Opus states in `jobs/*.b64` (decoded: every mic channel's load, volume, send and pans), the Dvořák 9/i mp3 (analysed with the same code as the master), and the stored third-octave spectra of Brahms 1/ii and 4/ii (`symphony/render/critics/c04/ref_brahms*_musopen/metrics.json`). Analysis frames are 4096-point FFTs every 21 ms, summed into third-octave bands, with qn mapped to seconds through the parts.json tempo map. "Measured" means a number from these files. "Inferred" means reasoned from those numbers, the manual or earlier cycles.

## Manual notes (L1: PDF pages 138-139, 141-142 of the May 2021 HO Opus manual; MANUAL-GAPS.md read)

| Page | What it says | Where it applies here | Render follows it? |
|---|---|---|---|
| 138 | Close mics sit in front of each section: presence, "but far enough away to allow room for them to breathe". Mid mics sit at the stage edge: "definition without the sound of close proximity". Main mics are a Decca tree at about the fifth row: mostly room reflections, "a big, unified sound". Surround and Vintage mics are lush but lack definition. Stage mics exist only on the expansion instruments. | Every instance loads Close + Main and nothing else (decoded states): woodwinds Close 0.5 / Main 0.8 (send 0.35), horns 0.5 / 1.0 (send 0.5), strings 0.66 / 1.0 (send 0.25), DIV tracks Close only (send 0.5). The Mid channel exists in the KS Masters but is never loaded. | Partly. The Main mic gives the unified hall. The woodwinds still measure drier and closer than the strings (finding 2), which is the proximity that p.138 says the Mid position avoids (MANUAL-GAPS #4). |
| 139 | Each mic sub-mix can be loaded or unloaded, which loads or frees its samples. The page lists the microphone models per position. | Memory: 44-45 GB settled. A Close-to-Mid swap costs no memory; adding Mid or Surround would. | Yes. Only two mics are loaded, and the unloaded ones hold no samples. |
| 141 | Channel routing (stereo, mono, swap); Stereo Double width, which works only on a stereo source; one convolution reverb per instrument; "Load with Effects Off". | All 32 tracks stereo. Widths come from the mic-channel pans (seat ± width), not Stereo Double. One true-stereo IR ("S. Cal Hall Perc TS FR 3.3s") on every instance. | Yes. Every instance has the same IR, fx volume 0.19, wet 2.0, 30 ms pre-delay and 5.5 kHz high cut (read in all 32 states). Master stereo matches the references (Do not touch). |
| 142 | Reverb preset, pre-delay and volume; the MASTER reverb shares one reverb across the instruments of one instance. AHDSR envelope: instruments are programmed "to achieve a natural result, so please be careful when changing them". | Release tails into the shared hall; the harp and harp-harmonics decay (decay 5990 ms to sustain 0.001, release 3019 ms, read). | Yes. Envelopes are at factory values (mix.json sets no `env_*`). MASTER reverb does not apply here, because each instance holds one instrument and the reverb settings are identical anyway. |

## Findings, ranked by what a listener would hear

### 1. The coda's ppp pedal (bars 83-86, qn 274-286) is bass-heavy and pulses: c28's re-bow refit raised the double basses 5-9 dB over the celli's 4 soli (measured)

- **Where.** Double basses (stem 26) A♭1 re-bows at 273.229, 276.05, 278.351, 282.203 and 283.605. Violoncellos (stem 25, "4 soli") re-bows 277.566, 281.683 and 284.151. Above them: the harp harmonics (dolce, bar 83) and the timpani answer.
- **What is wrong.** Series 1 (c26, which Dan heard) and the c27 port both had the full bass section 6-10 dB (A-weighted) under the four celli. In c28 the basses are louder than the celli, and the master's lowest octave stands far over its midrange in a ppp passage.
  - A-weighted levels per 3 qn window, basses / celli: c27 17.7/25.7, 17.7/26.4, 17.1/24.4, 13.3/23.6. c28 22.6/24.9, 24.2/22.8, 23.9/21.7, 21.7/18.1 (dB, one arbitrary scale; c26 bars 83-84 had the basses at 20.1 against 29.2).
  - The master's 40-140 Hz band relative to its 250 Hz-2 kHz band in bars 83-84 is +8.9 dB (c27 +5.7, c26 +4.7). In bars 83-84 the basses are 65-89% of the master's 45-140 Hz energy.
  - The ppp bars are now 8-10 dB louder in the basses' 40-300 Hz band than the pp "4 soli" bars that follow from 286 (half-qn levels 15-24 dB before qn 286, then 7-12). The score has ppp from 274, a crescendo from 283 and pp at 286.
  - The basses' 100-300 Hz level has an autocorrelation of 0.52 at the 3.95 s loop period over qn 274-298 (master 0.21; every other string stem is under 0.2 there). In half-qn windows the pedal swings between 14 and 24 dB. BRIEF item 8 calls this pulsing.
  - Meanwhile the celli fall about 7 dB from bar 83 to bar 86, which is through their printed crescendo (283 to pp at 286).
- **Cause (read).** `build/rebow_fills.json` gained these entries in c28: Double basses 273.229 mean +3.8 dB (max +8.9), 276.05 +6.8, 278.351 +6.7, 282.203 +8.1 (hold +9.0), 283.605 +8.7; Violoncellos 277.566 -4.1, 281.683 -4.2, 284.151 -5.1. In c27 none of these existed. The vol_db difference against c27 is, for the basses, +5.3 / +6.3 / +6.9 / +8.8 dB over 274-277 / 277-280 / 280-283 / 283-286, and for the celli -0.6 / -3.3 / -2.5 / -5.1. Inferred mechanism: the first re-bow (273.23) falls at the end of the printed p-to-ppp decrescendo (271-274). `fit_rebows.py` targets each piece at the level before the note's first re-bow, minus a planned 0.25 dB per CC11 step. The real level falls faster than that as CC11 crosses into the lowest layer. So the fit read the decrescendo as a re-bow dip, lifted the piece to the p level, and chained the lift through the later pieces, up to its +9 dB clamp.
- **Fix** (`build/rebow_fills.json`, level only, so `tools/stem_fix.py` can simulate it on the c28 stems before the render). Subtract a constant from every point of the bass entries: 273.229 -4.5 dB, 276.05 -6, 278.351 -6, 282.203 -7, 283.605 -6. Add +3 dB to every point of the cello entries 277.566, 281.683 and 284.151. Do not refit these pedals with the decrescendo inside the reference window. If they are refit, pass `--skip "Double basses:273.229"` and take the target from the ppp level over 274.3-275.9 instead. My band-power simulation of these offsets (incoherent sum, so approximate) gives:
  - basses -0.8 / -0.1 / -0.8 / about -2.7 and celli 6.6 / 7.0 / 4.4 / 3.5 (A, same scale), so the celli are 4-7 dB over the basses;
  - master 40-140 Hz relative to 250-2k: +0.1 / +5.3 dB in bars 83 / 84 (c26 +4.7 over both);
  - the step into the 286 "4 soli" pp down to about 3 dB.

  Targets for the actor's stem_fix check: basses flat within 2 dB across 274-286, celli 4-8 dB A over them, and the celli no lower at 283-286 than at 277-280. Re-measure the 3.95 s autocorrelation on the bass stem (aim under 0.3).

### 2. The woodwinds sound closer and drier than the strings, so the solos sit in front of the orchestra instead of behind the strings (measured; cause inferred)

- **Where.** All 11 wind tracks. Exposed: Oboe 1 bars 15-22 and 45-47, the bass clarinet solo 31-36, Flute 1 and the cor anglais 37-50, Clarinet 1's coda solo 85-89. The Violin I solo (bars 17-22, DIV A, Close only) shows the same dry tail.
- **Evidence.** I took every note that ends before a rest of 1.1 s or more, 500 Hz-4 kHz, and measured two things:
  - the level 0.15-0.25 s after the note-off, relative to the sustain just before it (the early drop);
  - the hall tail's level, extrapolated back to the note-off from the 0.35-0.9 s decay (the tail intercept).

  | Group | Notes | Early drop, median (IQR) | Tail intercept |
  |---|---|---|---|
  | Winds | 51 | 13.1 dB (11.3-14.2) | -9.3 dB |
  | Solo winds | 23 | 13.4 dB | -8.3 dB |
  | String sections | 27 | 7.5 dB (5.2-12.0) | -1.9 dB |
  | Horns | 15 | 7.8 dB | -5.5 dB |
  | Violin I solo | 2 | 13.9 dB | -9.0 dB |

  So a wind note's room is about 5.5 dB weaker at the cut-off and about 7 dB weaker in the hall tail than a string note's. The winds already send relatively more to the hall than the strings: send/dry 0.35 against 0.25, read in the states. The difference is therefore in the samples: the wind sound is mostly direct, while the strings' Main mic carries the studio's room. KIT §12 noted "woodwinds then sound nearer than the strings" in series 1; the c01 mic change did not close the gap. On a stage the winds sit behind the strings, so they should be at least as reverberant. Inferred listener effect: the classic "close-miked solo over a roomy section" mockup sound. It matters most in the exposed solos above.
- **Fix** (`build/mix.json`, `groups.wind.send` 0.35 -> 0.6). Movement I c09 measured +3.2 dB of send giving 3-4 dB less early drop (trumpet 12-13 -> 8.4-9.7 dB), at +0.3-0.5 dB of level. So +4.7 dB of send should bring the winds to about 8-9 dB, within 2 dB of the strings (inferred). This is a state change: the 11 wind tracks are rebuilt by `--midi-only`, at no memory cost. Give "Violin I solo" `send` 0.5 -> 0.8 for the same reason. If a second test is wanted: the manual's own remedy (p.138) is Mid in place of Close on Oboe 1, the cor anglais, Clarinet 1, the bass clarinet and Flute 1 (MANUAL-GAPS #4: `"mics": {"Mid": 0.5, "Main": 0.8}`, gains re-matched). That swap changes the direct timbre too and needs every level table on those tracks checked, so do the send first. Check: early drop and tail intercept per family as above, and the K-weighted solo levels against their accompaniment (B's lens).

### 3. Solo wind images jump from note to note (measured; fix from movement I)

- **Where.** Oboe 1 (bars 15-22, 45-47), Clarinet 1 (coda 85-89 and bars 61-63), Clarinet 2, the cor anglais (37-50).
- **Evidence.** Per-note right-minus-left level in the steady part of each note, with the image steps measured at 1.25-4 kHz:

  | Track | Notes | R-L SD, 400-1000 Hz | Largest step, 1.25-4 kHz |
  |---|---|---|---|
  | Oboe 1 | 43 | 5.3 dB | 7.0 dB |
  | Clarinet 1 | 27 | 4.6 dB (3.2 dB at 1.25-4 kHz) | 10.0 dB |
  | Clarinet 2 | 29 | 4.9 dB | 4.8 dB |
  | Cor anglais | 40 | 3.2 dB | 5.4 dB |

  The string sections are 0.4-0.7 dB SD at 1.25-4 kHz. The winds play at width 0.5 (group; cor anglais and bass clarinet 0.3). Movement I c25 and c35 (`symphony/mvt1/reaper-v621/loop/LEARNINGS.md`, "Mics, panning and width") measured width 0.05 on these same KS Masters, with the seat moved to keep the image: SD 4.2-6.0 -> 2.4-3.7 dB at 400-1000 Hz, note-to-note steps 8.2 -> 1.4 dB, note levels within 0.3 dB. Their conclusion: give every exposed solo wind the narrow width.
- **Fix** (`build/mix.json`). `"width": 0.05` on Flute 1, Flute 2, Oboe 1, Oboe 2, Cor anglais, Clarinet 1, Clarinet 2, Bassoon 1 and Bassoon 2 (movement I's set). Keep the seats and check the measured images (now Fl1 -3.6, Ob1 +1.5, CA +3.2, Cl1 -0.4, Cl2 -4.0, Bn1 +3.5 dB R-L at 1.25-4 kHz). Leave the bass clarinet and contrabassoon as they are (SD 0.8 and 0.3). The same rebuild as finding 2. Both are state changes, so make them together in one cycle.

### 4. Violins II div (bars 37-40, sul tasto) is 11 dB brighter than the other half of its own section (measured)

- **Where.** Violins II div (stem 30, `2nd Violins KS Master DIV B`, Close only) and Violins II (stem 23), qn 108-124. Both are on Flautando ("senza sord., div., sul tasto", pp). The div track plays the upper voice (G♯4-B♭4) and the section the lower (C♯4-F♯4).
- **Evidence.** Over the same frames, relative to each stem's 250 Hz-1 kHz band:

  | | 1-4 kHz | 4-10 kHz | Spectral centroid |
  |---|---|---|---|
  | Violins II div | -1.6 dB | -17.0 dB | 716 Hz |
  | Violins II | -12.9 dB | -28.2 dB | 420 Hz |

  The register difference (5-7 semitones) explains only a small part. The other divisi pairs, with their div voice similarly higher, differ by 0.3-2.5 dB at 1-4 kHz: Violas div / Violas +1.6, +0.3 and 0 dB in 66-90, 279-304 and 266-268; Violoncellos div / Violoncellos +2.5 and +1.4 dB in bars 18 and 21-22. The div half is even 7 dB brighter than the Violins II's own open sustains at mp-mf (about -9 dB in qn 140-200). Inferred listener effect: an airy close-miked upper line over a dull lower one, where the score has one muted-toned section playing sul tasto. The Close-only DIV mic is the likely cause (KIT §8: DIV patches have only Close).
- **Fix** (`build/mix.json`, Violins II div `eq`). Add `{"band": "highshelf", "hz": 1500, "db": -6}` beside the 40 Hz high pass. This is a ReaEQ change, so `--mix-only` / `--midi-only` without an Opus rebuild. Target: the 1-4 kHz gap at 3 dB or less. Re-check the div voice's K-weighted level against the section afterwards; the shelf lowers it by roughly 1 dB (inferred).

### 5. The celli are the narrowest string image: nearly mono above 1 kHz in their exposed counter-melodies (measured; fix from movement I)

- **Where.** Violoncellos (stem 25), and the Violoncellos div track. The cantabile counter-melodies of bars 23-28 and 71-74 (sul D) and the B flat minor head with Oboe 1 in bars 45-52.
- **Evidence.** Stereo correlation at 1.25-4 kHz: Violoncellos 0.83, Violoncellos div 0.80. The other sections: Violins I 0.42, Violins II 0.66, Violas 0.69, Double basses 0.74. Movement I c29 found the same patch at width 0.28 nearly mono above 4 kHz (0.87), and fixed it with a side-only high shelf at 1.5 kHz, +4 dB. That took the cello stem to 0.61 and moved its level by 0.2 dB K and its seat by 0.6 dB; the Opus width stays narrow so the low-end correlation work is kept. Inferred listener effect: the cello line collapses to one point while the violas beside it are spread. The coda's 4 soli (bars 83-86) should stay narrow; four players are a narrow source.
- **Fix** (`build/mix.json`, Violoncellos). `"side_shelf": [{"band": "lowshelf", "hz": 200, "db": -2}, {"band": "highshelf", "hz": 1500, "db": 4}]`, the list form the contrabassoon already uses. This is applied by `--mix-only` / `--midi-only`. Target: correlation at 1.25-4 kHz about 0.6-0.7. Check that the master's correlation below 250 Hz stays at 0.6 or above.

### 6. Low-mid tilt: the 250 Hz octave is strong against the 125 Hz octave compared with all three references (measured; small levers, inferred)

- **Evidence.** Octave sums relative to 250 Hz-2 kHz, using octave bands so that each piece's key matters less:

  | | 125 Hz octave (88-178 Hz) | 250 Hz octave (178-355 Hz) | 250 minus 125 |
  |---|---|---|---|
  | c28 master | -9.8 dB | -5.6 dB | +4.2 dB |
  | Brahms 1/ii | -7.7 dB | -8.3 dB | -0.6 dB |
  | Brahms 4/ii | -5.8 dB | -7.5 dB | -1.7 dB |
  | Dvořák 9/i | -6.6 dB | -6.5 dB | +0.1 dB |

  So the master's 125 Hz octave is 2-4 dB low and its 250 Hz octave 1-3 dB high against every reference. The wide-band shares are inside the reference range: 100-250 Hz -8.3 dB against -6.6..-8.75. Below 100 Hz the references disagree too much to tune to (Brahms -8.5/-7.9 dB, with a 17 dB jump between their 50 and 63 Hz third-octaves that looks like mains hum; Dvořák -21.7, lossy). Movement I's c29 found the same shape: 198 and 315 Hz 2-4 dB over every reference, 125 Hz 4-7 dB under. Contributors: celli 48% of 140-280 Hz and basses 62% of 90-140 Hz over the whole piece. In soft passages the bass clarinet is 41% of 90-140 Hz, through its solo and pedals in bars 3-6 and 31-36.
- **Fix: small, optional.** My band-power simulation of moving the celli's static bell (170 Hz +3, 1.5 oct) to 125 Hz +3 changes the 250-minus-125 difference by only about 0.3 dB. Removing it changes it by 0.2-0.5 dB, at -1.7 dB on the celli. The real lever is the basses' `bell2` (80 Hz -6 dB, 1 oct), whose upper skirt cuts 90-115 Hz. That is on the series 1 do-not-touch list, so I do not propose changing it. Do finding 1 first: it removes the worst passage of low-end build-up. After that, if the actor wants a step, `"bell"` on Violoncellos to 125 Hz +3 dB (bw 1.5). Do not add any boost at 150-250 Hz (the loud_eq bells already sit there; movement I c29 found that its boost went into the band that was already high).

## Checks for items 8-9 and S1-S3 through this lens

- Loop pulsing: final chord (qn 292-304) master 100-300 Hz autocorrelation at 3.95 s 0.02, centroid -0.11. Bars 1-6 -0.15. The bar 65-70 pedal 0.14. Only the coda bass pedal fails (finding 1).
- S3 (cut hall tails): the c28 stem fix role on Violas `[152.45, 167.98, -13, 0.08]` begins its fall at 152.0. That is the moment the fp-decrescendo note 147.78-152.0 is released, so the volume envelope (post-hall) takes the viola stem down 26 dB in 0.42 s. A natural cut-off in this render drops 15 dB in 0.3 s and 23 dB in 0.6 s. The master hides it (the cor anglais is 8 dB over the viola there), so it is not ranked. When this span is next rebuilt, the cut belongs in CC7, which acts before the hall (`CC7_POINTS["Violas"] = [(152.36, 28), (167.95, 127)]`, about -13 dB on Opus's linear CC7), not in the envelope.
- Accents (item 9), S1 and S2 are not measured here (A's lens).

**Do not touch:**
- The shared true-stereo hall and the seats. Master correlation is 0.53 (Brahms 0.51/0.55), side/mid -5.2 dB (-4.9/-5.4), below 250 Hz 0.61 (Brahms 0.60/0.62, Dvořák 0.55), 250 Hz-4 kHz 0.53 (0.48/0.52, 0.56), above 4 kHz 0.48 (0.38/0.47, 0.52). Per-section images run from Violins I -7.9 to Double basses +7.7 dB R-L in concert order.
- The con sordino. On the same theme, the muted Violins I (bars 23-30) are 6-10 dB darker at 2-4 kHz than the open ones (bars 71-77); Violins II and violas 3-6 dB.
- The Violas div / Violas match: 1-4 kHz within 0-1.6 dB, images within 1.2 dB.
- The harp harmonics' image against the harp: within 2 dB at 1.25-4 kHz.
- Horns 3-4 mute EQ.
- The series 1 Cb EQ set (bell2 80 Hz, 160 Hz +4.5, climax shelf -3).
- The factory AHDSR envelopes.
