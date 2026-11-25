# Cycle 6, critic A: articulation and phrasing (on the cycle 5 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c06-A/` and run with `~/.venvs/claude-composes-reaper/bin/python` (`lib.py` and `arts.py` are c05-A's, pointed at c05):
- `leg.py [-v]`: legato crossover for every legato target (the moment the new pitch's first four harmonics overtake the old pitch's), against `sq`.
- `dom.py <track> q0 q1`: for a fast figure, the share of each note's score slot in which its own pitch dominates, and the delay until it first does.
- `bulge.py`, `bulge2.py` (vol_db removed), `pitchres.py`, `notes.py`, `even.py`: note-by-note body levels in melodic lines against their neighbours and the CC11 curve.
- `dropped.py [cycle]`: entries after a rest that never sound. `acc.py`: attack peak against the note body. `chords.py`: chords sent to a legato patch. `harp.py`: harp level at and after note-offs. `am.py`, `amall.py`: amplitude modulation on held notes.

"Body" means the median 20 ms RMS level from 30% to 85% of a note's slot. Bars: 1-36 = qn/3+1, 37-64 = (qn-108)/4+37, 65-92 = (qn-220)/3+65.

## 1. The first chord of the movement loses voices at random: Horn 3 is silent in c05, Violins II and Violas were silent in c04

**Measured.** Bar 1 starts at qn 0 with Horn 3 (C4, ppp, 2 qn) and Violins I/II, Violas and Celli (ppp). The first note of each track sits on sample 0 of the render, together with that track's first CC11, CC1, CC15 and CC70 points.

Mean level of each stem over qn 0-2, per render:

| Track | c03 | c04 | c05 |
|---|---|---|---|
| Horn 3 | -63 | -63 | **-98** (peak -75, then decays to -141; only the release sample at qn 2 sounds) |
| Violins II | -62 | **silent (-180) until qn 3** | -60 |
| Violas | -62 | **silent (-180) until qn 3** | -58 |
| Violins I | -60 | -62 | -58 |

- parts.json did not change for these notes between the cycles (Horn 3: qn 0, v31, CC11 22, CC1 57, CC15 0, all at qn 0).
- `dropped.py` checks every entry after a rest in all 27 stems. In c05 the only entry that never sounds is Horn 3 at qn 0. Every later entry sounds.
- `probe_attacks.py` has no check before qn 42, so the gate passed c04 and c05 with the opening chord broken.

**Inferred.** Opus is not ready on the first block of an offline render. Notes and controllers on sample 0 are dropped or applied in the wrong order, and which ones fail changes from render to render. The listener's first sound is the chord that the horn is supposed to colour, so this is the most audible articulation fault in the render. The c03 "qn 0 pre-roll" item (C5, deferred) is this problem, and it is now measured.

**Fix: a silent pre-roll bar, cut off after the render.**
- `tools/build_reaper.py`: add `PREROLL_QN = 3.0` (one 3/4 bar at 52 bpm = 3.4615 s).
  - `tempo_job()` writes a 52 bpm, 3/4 marker at 0 and every existing marker at `qn + PREROLL_QN`.
  - `track_job()` and `vol_points()` write every note, keyswitch, CC point and volume-envelope point at `qn + PREROLL_QN`.
  - The first point of every CC lane (cc11, cc1, cc15, cc70, cc7) and the first keyswitch are also written at qn 0.25 of the pre-roll, so each instance has its state before the music starts.
- `tools/render_cycle.py`: after the render and before `measure.py`, cut the first `round(PREROLL_QN * 60 / 52 * 48000)` = 159692 samples from `00_Master.wav` and every stem (soundfile read and write, sample-exact). Everything downstream (measure, probe, the critics' scripts, the mp3) then stays on the current timeline.
- `tools/probe_attacks.py`: add opening checks. For Horn 3, Violins I, Violins II, Violas and Violoncellos at qn 0, the 50 ms maximum over the first 1.5 s must be above -70 dB. In c05, Horn 3 measures -75 there; in c03 and c04 it was about -60. In c04, Violins II and Violas measured -180.
- **Check:** all five opening voices sound in two consecutive renders.

## 2. Single notes bulge or sag 6-14 dB inside wind and horn lines at a flat CC11 (sample unevenness by pitch)

**Measured** (`bulge.py`, `pitchres.py`). The residual is each note's body level against its neighbours after the CC11 slope is removed. The vol_db trims are already included in these numbers.
- **Horn 1, bars 55-60 (qn 180-203).** Here Horn 1 plays the melody in unison with Clarinet 1, and then leads into the climax. Every F4 (65) is 8-9 dB over the line and every G flat 4 (66) is 6-8.5 dB under it:
  - 180 Gb4 -50.4, then 182 F4 -37.7 dB, with CC11 68 on both.
  - Clarinet 1, playing the same notes at the same time, measures -45.8 / -44.7 / -47.3 on 180 / 182 / 184. Its line is even, and the horn's saw-tooth is not.
  - The same holds through bars 58-60: deviations 192 +8.3, 195 +8.2, 201 +9.0 on F4; 190 -6.0, 196 -7.7, 202 -8.5 on Gb4.
  - Over the whole part, Horn 1's per-pitch residual is F4 +5.0 dB (n=7), Gb4 -5.3 (n=4) and A flat 4 -4.8 (n=2).
  - Inferred: the late horn crossovers in `leg.py` (184 +0.20 s, 193 +0.28, 202 +0.31; every other horn transition has a median of +0.03) are the same fault. The loud F4 keeps sounding over its quieter target.
- **Clarinet 1, bars 76-81.**
  - A flat 5 (80) sags. At qn 255 it holds -45 dB for 0.375 qn and then drops to -54 for the rest of the note.
  - G5 (79) jumps. At qn 256 it comes in at -40 to -44 dB. Deviations: 255 -9.9, 256 +7.8, 266 -13.6, 268 +13.3 dB.
  - Per-pitch residual: G5 +9.9, A flat 5 -4.6.
  - `note_trims.json` already has Cl1 266 at -3. That note is A flat 5, the quiet one, so the existing trim makes the sag worse.
- **Cor anglais, solo espr., bars 48-53.** A4 (69) is the loud note:
  - qn 163 swells to -36 dB against -43 to -46 on both neighbours, at CC11 66.
  - qn 152, also A4, is still +5 dB over the line with its -8 trim.
  - Per-pitch residual: +9.1 dB (n=2).
- **Flute 1, bars 37-41 (p, the first flute melody).** The top note of each slur is G flat 5 (78), and it is the quietest note of the slur: 110 -7.6, 117.33 -5.2, 127.5 -7.6 dB.
  - These notes are also the only flute notes at CC1 110 (the +10 "top of the slur" vibrato). Notes at CC1 105 or higher average -2.9 dB of residual; other notes average +0.2.
  - Inferred: the vibrato boost on the flute patch costs level. The pitch could also be the cause; the data cannot separate the two.

**Inferred effect.** These are the exposed solo lines: the horn and clarinet duet, the cor anglais solo, the first flute tune. A note that jumps out or drops away by 6-14 dB at a flat dynamic sounds like a wrong note or a bad sample. It is the clearest phrasing fault left in the winds.

**Fix (`tools/score_to_parts.py` and a new `build/pitch_trims.json`).**
- Add `pitch_trims.json`: `{track: {pitch: dB}}`, applied like a note trim (`("note", q, end, dB, ramp)` in `vol_parts`) to every note of that pitch on a Leg articulation of that track. Starting values:
  - `"Horn 1": {"65": -5, "66": +4, "68": +3}`
  - `"Clarinet 1": {"79": -6, "80": +5}`
  - `"Cor anglais": {"69": -5}`
  - `"Flute 1": {"78": +4}`
- In `note_trims.json`, delete Clarinet 1 "266": -3 (it deepens the A flat 5 sag). Keep Cl1 256 -5 and CA 152 -8: the measured excess at those notes is larger than the trims.
- Flute alternative: drop the `+10` top-of-slur CC1 for flutes (`cc1_fn`, `tgt = min(120, tgt + 10)`) and re-measure before adding the 78 trim.
- **Check:** `bulge.py` and `even.py` report no step over 5 dB in Horn 1 at qn 176-204, Clarinet 1 at 250-272, CA at 150-172 or Flute 1 at 108-136. Horn 1's crossovers at 184, 193 and 202 drop under 0.15 s.

## 3. Celli div. (bars 18 and 22): a 10 dB hole at each div. entry, and the upper line is not legato

**Measured.**
- At qn 51 and 63 the celli move from a Leg BC line into two voices on Sus MAX. Notes: 51/51.5/52/53 and 63/63.5/64/65, velocity 90, no entry lead.
- Stem level:
  - qn 51: falls from -55..-60 to -69.8 dB, back by 51.75.
  - qn 63: falls from -53..-59 to -66.0, and is under -61 until 63.6 (0.6 qn, about 0.7 s).
- The guard added in c05 ends the preceding Leg BC note at 50.93 and 61.85+1.08 = 62.93, before the keyswitch.
- The new notes start on the beat on a soft Sus MAX attack. At pp, that attack measured 300-800 ms of bloom in c03.
- The c04 report measured the same 8-10 dB drop. Nothing has changed it.

**Inferred.** The celli's answering figure in bars 18 and 22 ("div.", under Violin I's solo) starts with a gap and then plays detached. A cellist in div. plays the upper voice legato. The hole is small in level because the passage is pp, but it falls on the second beat of an otherwise seamless string texture.

**Fix.**
- **Cheap, no new instance (`score_to_parts.py`).** Treat a Sus MAX string note that starts within 0.1 qn of the end of a Leg note on the same track (an articulation change without a rest) as a soft entry: apply `ENTRY_LEAD_S["string"]` (0.12 s at CC11 ≤ 50) and hold CC11 at the entry level, exactly as for entries after a rest. Raise these notes' velocity to at least 105.
- **Full fix, only when memory allows.** Give the upper voice its own Leg Slur MAX track: `Celli Divisi/06 Keyswitch/Celli KS Master DIV B.oib`, appended last, for qn 51-54 and 63-66. At 09:41 REAPER held 63 GB, two `chrono-25d` Python processes held another 15 GB and 6 GB, and 0.7 GB was free. Do not add instances until that memory is back.
- **Check:** the Vc dip at qn 51 and 63 is 4 dB or less (add both to the probe's `HOLES`).

## 4. Viola accompaniment figures: legato transitions leaving C4 take half the note

**Measured** (`dom.py`).
- **Bars 71-75 (qn 238-252).** Slurred viola eighths, pp-p, "unis., ord.", 0.58 s each, Leg Slur/BC MAX at v124 with a 0.15 s lead.
  - Five of the six transitions that leave C4 (60) are slow. The new pitch takes over 0.22-0.37 s after its score onset and owns only 14-51% of its slot: 238.5 (60→63) 0.26 s / 47%, 240.5 (60→56) 0.37 s / 14%, 244.5 0.27 s / 48%, 246.0 0.27 s / 46%, 250.5 0.29 s / 51%.
  - All other transitions in the passage are at a median of 0.05 s with 80-100% ownership.
- **Bars 37-40 (qn 108-122).** Pp triplet eighths, 0.33 s each. The median ownership is 71% and the median takeover is +0.09 s. Twelve of 45 notes are under 50% (worst: 109.0, 111.0, 113.67, 117.67, 119.0, 119.67, 120.67, at 33-44%).
- **Bars 57-58 (qn 188-196).** Ownership 78%, takeover +0.075 s.
- The CC70 lane does not explain the C4 effect: it is 0 at bar 71.

**Inferred.** The accompaniment's eighths smear into each other on these intervals, so the figure under the flute and violin tunes sounds blurred and late on every second or third note.

**Fix (`score_to_parts.py`).**
- **Bars 71-75.** Add a per-source-pitch extra lead: `LEG_EXTRA_S = {"Violas": {60: 0.10}}`, added to `LEG_LEAD_S` when the previous legato note's pitch is the key. Re-tune against `sq` with `leg.py`.
- **Triplets, bars 37-40 and 57-58 (0.33-0.37 s notes).** Raise the `short_sus` limit for Violas from 0.25 s to 0.38 s. They then play overlapping Sus MAX notes, as the bar 59-60 sextuplets already do (c03 C #3 measured those connected and in time).
  - Accept this only if `dom.py Violas 108 124` shows median ownership of 80% or more and no new gaps.
  - The soft Sus MAX attack at pp is the risk: compare the triplets' level against c05.

## 5. Printed bow marks are ignored: the bar 80 up-bow retake is lost inside a 4-qn tied note

**Measured.**
- `mockup-events.tsv` has 6 up-bow and 2 down-bow marks. `score_to_parts.py` reads neither.
- At qn 265 (bar 80, ff), Violins I, Violins II and Violas have a fresh up-bow ("V") on the tied-to note. parts.json plays one 4.045-qn note (qn 262-266), with no notch or re-attack at 265.
- The other marks are Vln I at qn 292 V, 295 ⊓, 298 V and 301 ⊓ (the final ppp held note, under "change bow at will"), and Vla at 122 V (the end of the bar 40 triplets).

**Inferred.** At bar 80 the composer asks for a new bow at the top of the second climax. A real section re-bows there with a small re-articulation. The mockup plays a held note that fades.

**Fix (`score_to_parts.py`, the same-pitch merge block that builds `notches`).**
- For a `script upbow/downbow` at q inside a sounding note of a string track, append `(q, 14 if base(q) > 40 else 8)` to `notches`. That is the existing bow-change notch, about 3 dB at ff, 8 CC at pp.
- **Check:** a 2-4 dB dip in Vln I/II/Vla at qn 265 that recovers within 0.25 qn.

## Do not touch

- **Legato timing.** Every wind and brass legato part crosses over at a median of +0.003 to +0.073 s; strings at +0.013 to +0.063 s.
- **Chords on legato patches.** No legato-patch note overlaps another legato note on its track by more than 0.1 qn (`chords.py`, all tracks).
- **Trombone 1's marcato accents** (Sus Accent MAX, bar 63-64). Attack peaks are +2.7 and +1.3 dB over the note body at 212.5 and 213, and +3.3 dB over the preceding level at 218. That is within Dan's 2-4 dB.
- **The string sf > p at qn 212.** +6 to +9 dB, falling to p within 1 qn.
- **Harp ring.** No level drop at any note-off.
- **Final fermata fade and tail.** The master decays to silence 2.5 s after qn 304, with no cut.
- **Breath and caesura timing; after-grace runs; the c05 keyswitch guard and `short_sus`-without-caesura rule.**

Not raised: held soft string notes show 6-14 dB of 3-5 Hz amplitude modulation on every channel (winds 0.8 dB). It has been there since c00 and does not depend on CC1 (r = -0.26). Without a matched reference I cannot say it is wrong.
