# Critic C, cycle 1: blend and space (one room)

Under review: cycle 0 render (`cycles/c00/render`, `metrics/`), `build/parts.json`, `tools/build_reaper.py`, and the Opus patch states the tools write (read with `opus_state.load_oib` on each track's `.oib`). Scratch scripts: `/private/tmp/claude-501/mockup-loop/c01-C/a1.py` to `a7.py`.

One correction to the brief first. "No reverb" is wrong. Every KS Master patch carries its own Opus reverb, and the render includes it: a `ConvolutionReverb` on the `fx:0` channel, fed by a post-fader `Reverb Send` (level 0.25) from each mic channel. The IR files exist in `/Library/Application Support/East West/ImpulseResponseData/`. The cycle 0 tracks use seven different reverbs at different levels (finding 3). The REAPER master has no effects, but the room is set inside each Opus instance.

A warning that applies to every Opus-state fix below: `build_reaper.track_job()` writes `jobs/NN_<stem>.b64` only when the file does not already exist (`if not os.path.exists(b64file)`). Any change to `state_for()` takes effect only after the old `.b64` files are deleted or moved, or after that check is removed.

## 1. Double basses fill the low end and are the loudest stem in most of the piece (measured)

Where: Double basses, whole piece. Worst in bars 21-30, 45-47 and 53-64, and in bars 71-88 where the bass is accompaniment at p/pp.

What is wrong: the bass stem sits 10-19 dB above the cellos at the same printed dynamic. It carries all of the mix's energy from 40 to 100 Hz. The result is a boomy bottom that a real orchestra does not have, with the accompaniment above the melody.

Evidence:
- Median stem level by printed dynamic (metrics.md), Cb against Vc: pp -39.9 vs -49.8, p -35.2 vs -46.2, mf -28.7 vs -37.9, f -26.7 vs -34.2.
- Bars 53-56: both parts are marked p, then mp and mf. Cb measures -33.6/-30.9/-31.6/-26.0 dB and Vc -52.5/-48.3/-46.1/-47.4, so the bass is 19 dB louder in bar 53.
- Bar 21: Cb at pp (-39.1) is the loudest stem, above the Violin I solo at p (about -50).
- Cb is the loudest stem in about 50 of 92 bars. Its peak is 0.408, against 0.149 for Vc.
- Spectrum: in every bar, Cb's share of the master's 40-100 Hz band is 0.0 dB, i.e. all of it (a7.py).
- Low band against mid band (40-100 Hz over 500-2000 Hz, per bar): the master's median is -7.3 dB. The Dvorak reference's median over 2-second windows is -18.2 dB, 11 dB less. Bars 23, 83 and 84 exceed +15 dB.
- Long-term third-octave band at 63 Hz relative to 1 kHz: mix +14.1, reference -6.2.
- Below 100 Hz the master holds 17.3% of all energy; the reference holds 0.6% (a5.py).
- The reference is a live student recording on 128 kb/s MP3, so it may be light in the bass. Even so, the gap is far larger than that would explain. The other reference recordings listed in `render/assets/README.md` (Brahms 1/ii, 4/ii) are not in `assets/refs/`; only the Dvorak file is there.

Fix:
- Add a per-track gain to the `TRACKS` table in `tools/score_to_parts.py` (a sixth field `gain_db`, written into parts.json). In `build_reaper.track_job()`, apply it with `reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 10^(gain_db/20))`. Putting the gain on the REAPER track keeps the Opus state unchanged.
- Start Double basses at -10 dB. Leave its CC11 curve alone.
- Targets for cycle 1:
  - Cb median level at each printed dynamic 0-3 dB below Vc.
  - Master 40-100/500-2000 Hz median at -12 dB or lower, with no bar above +5.
  - 63 Hz band relative to 1 kHz at +5 or lower.
- Re-check bars 53-56 and 21-28 in the per-bar stem levels.

## 2. Woodwinds, horns and harp are heard through different microphones than the strings, so they do not sit in the same room (measured config, effect inferred)

Where: all woodwinds, Horns 1-4, Harp. Mic settings are the `mixer.channels[sub:N].volume` values in each patch, together with `layerMatrix.columns[N].loaded`.

What is wrong: HO recorded every section in its seat in EastWest Studio 1, and the Main (Decca tree) mics hold that seating and depth (HO manual, Microphone Positions, pp. 85-86). The strings are heard mostly through Main (Close 0.66, Main 1.0). The woodwinds are heard almost only through their Close mics:

| Patch | Close | Main |
|---|---|---|
| Flutes | 1.0 | 0.28 |
| Oboes | 1.0 | 0.04 |
| Cor anglais | 1.0 | 0.05 |
| Clarinets | 1.0 | 0.06 |
| Bass clarinet | 1.0 | 0.01 |
| Bassoons | 1.0 | 0.13 |
| Contrabassoon | 1.0 | 0.24 |

That puts Main 11 to 40 dB below Close. The horns are Close 1.35, Main 0.44. The harp has only Close loaded: Main (column 4) is unloaded.

On a real stage the woodwinds sit behind the strings. Here they are miked closer than the strings, so they come out in front, with close-mic presence and the patch's own close-mic panning. Inferred: a listener hears the strings in a hall with soloists on a different, nearer stage.

The harp also does not blend:
- Inter-channel coherence -0.25 (anti-phase content).
- Placed 9 dB to the left.
- At mp in bars 53-56 it measures -43 to -48 dB, under Violins I at -38 to -42.

Fix, in `build_reaper.state_for()`, after `load_oib` (set the sub-channel volumes by label, and the `loaded` flags on the matching `layerMatrix.columns`):
- Woodwinds: Close 0.5, Main 0.8.
- Horns: Close 0.5, Main 1.0.
- Trombones, tuba, strings: keep as they are.
- Harp: set `columns[4].loaded = True` (Main), Close 0.6, Main 1.0.
- Timpani: set `columns[3].loaded = False` (Surround); see finding 5.

These changes alter stem levels. Measure each changed stem's median level per dynamic against cycle 0 and correct with the `gain_db` field from finding 1, so balance does not move while depth does. Loading the harp's Main adds samples; `render_cycle.py` already waits for memory to settle.

## 3. Seven different reverbs at levels 11 dB apart: the instruments are in different halls (measured, from the patch states)

Where: every track, the `fx:0` channel and the `Reverb Send` inserts in `mixer.channels`.

What is wrong: each patch keeps its factory reverb.

IRs:

| IR | Tracks |
|---|---|
| S. Cal. Hall strings LR Rear | strings, bass clarinet |
| S. Cal. Hall strings LR Front | Flute 2, harp |
| New Hollywood Hall 2.6 | Flute 1, oboes, cor anglais, bassoons |
| New Hollywood Hall 2.0 | clarinets, contrabassoon |
| S. Cal. Hall All Brass | horns, trombones, tuba |
| S. Cal Hall Perc TS FR 3.3s | timpani |

Return levels (`fx:0` volume): strings 0.143-0.186, harp 0.125, Flute 2 0.131 against Flute 1 0.224, oboes 0.278, bass clarinet 0.445 with wet 0.5 (all others 2.0), brass 0.589. Effective reverb level per mic (send × return × wet):

| Tracks | Effective reverb level |
|---|---|
| Strings | -22 dB |
| Harp | -24 dB |
| Flute 2 | -24 dB |
| Flute 1 | -19 dB |
| Oboes | -17 dB |
| Timpani | -19 dB |
| Horns, trombones, tuba | -10.6 dB |

So the two flutes play in different halls, and the brass is 11-12 dB wetter than the strings in a third hall.

The total amount of reverb is reasonable and should be kept. The final cutoff (bar 92) decays to -11.3 dB at 0.25 s, -18.9 at 0.5 s and -29.5 at 1.0 s. The reference's final cutoff decays to -10.5, -18.7 and -36.3 dB at the same times (a3.py, a4.py). The problem is consistency, not quantity.

Fix, in `build_reaper.state_for()`:
1. Replace the `ConvolutionReverb` insert on `fx:0` in every patch with one shared configuration: the strings' current one (`impulseA` `//ir/QL SPACES TEASER/S. Cal. Hall strings LR Rear`, wet 2.0, delay 0.008). This IR is known to load, and it is the hall of HO's Classic mood (HO manual p. 82).
2. Set `fx:0` volume to 0.151 on every patch, and wet to 2.0 (this fixes the bass clarinet).
3. Express depth only through the per-mic `Reverb Send` `level`: strings 0.25 (unchanged), harp 0.3, woodwinds 0.35, trombones and tuba 0.45, horns 0.5, timpani 0.45. That gives effective reverb levels of -22.4, -20.9, -19.5, -17.3, -16.4 and -17.3 dB.

Stronger option for a later cycle, once this works: EW Spaces II is installed and registered in REAPER (`EW Spaces II (East West)`, VST3). Its presets are the same `ConvolutionReverb` JSON as Opus's insert, for example `Presets/Concert Halls/Northwest Orchestral Hall/S-S/Northwest Hall TS FR 2.6s.preset`. That allows one true-stereo hall on a single REAPER send bus, with the Opus reverbs switched off (`SendProcessor.active = False`). Inferred and not checked: whether Opus's own insert accepts a Spaces II `//ir/...` path. Test it on one track and read the state back before relying on it. The CC BY Detmold IRs in `symphony/render/assets/ir/` (8 orchestra source positions) are the licensed alternative through ReaVerb, but its IR setting has to go through the FX chunk.

## 4. Panning is applied twice and the image has no centre (measured)

Where: all tracks.
- REAPER `D_PAN` comes from the pan field in `score_to_parts.py` `TRACKS`, applied in `build_reaper.track_job()`.
- The patches also pan their own Close channel: Flutes +0.25, Clarinets -0.31, Bassoons +0.41, Contrabassoon +0.44, Horns -0.25, Trombones +0.25, Tuba +0.35, Cb +0.62, Vc +0.33, Vln I -0.31.
- The Main mics already carry the recorded seating.
- REAPER's pan on a stereo track is a balance control, so it tilts a wide source rather than placing a narrow one.

Evidence (energy right minus left over each stem's active frames, a1.py):

| Stem | Measured R-L (dB) | REAPER pan | Patch Close pan |
|---|---|---|---|
| Cor anglais | +15.0 | | |
| Bassoon 1 | +15.3 | | |
| Bassoon 2 | +15.2 | | |
| Contrabassoon | +14.7 | | |
| Violoncellos | +8.5 | | |
| Double basses | +10.5 | | |
| Clarinet 1 | -10.2 | | |
| Violins I | -13.2 | | |
| Flute 1 | -5.2 | -0.15 | +0.25 |

The woodwind section spans a wider stereo angle than the string section, with bassoons and cor anglais further right than cellos and basses. Flute 1's two pan settings contradict each other.

Inter-channel coherence (real part of the cross-spectrum over the magnitude product, a6.py), master against reference:
- 800-3000 Hz: 0.07 vs 0.70.
- 3-10 kHz: 0.02 vs 0.72.
- Side/mid ratio: -0.4 dB vs -5.6 dB.

Oboe 1 has negative coherence (-0.28 at 50-200 Hz, -0.21 at 0.8-3 kHz), and Clarinet 1 and Harp are negative in total. Inferred: the mix sounds like two loudspeakers with a hole between them, and solo winds have no fixed position.

Fix:
- Keep one seat per track, and apply it once, inside Opus.
- In `build_reaper.track_job()`, set `D_PAN` to 0.
- In `state_for()`, set every sub-channel's `pan` to 0.
- Use the Opus master channel's `panLeft`/`panRight` as a dual pan: seat ± width/2. Inferred and to be verified on one track: that these fields act as left/right channel placement, like Play's stereo pan.
- Suggested seats (American layout, audience view), as seat (width):

| Group | Track | Seat | Width |
|---|---|---|---|
| Strings | Vln I | -0.55 | 0.5 |
| | Vln II | -0.25 | 0.5 |
| | Vla | +0.15 | 0.5 |
| | Vc | +0.35 | 0.5 |
| | Cb | +0.5 | 0.4 |
| Harp | Harp | -0.6 | 0.3 |
| Woodwinds | Fl 1 | -0.1 | 0.3 |
| | Fl 2 | -0.15 | 0.3 |
| | Ob 1 | +0.1 | 0.3 |
| | Ob 2 | +0.15 | 0.3 |
| | CA | +0.2 | 0.3 |
| | Cl 1 | -0.15 | 0.3 |
| | Cl 2 | -0.2 | 0.3 |
| | BCl | -0.25 | 0.3 |
| | Bn 1 | +0.15 | 0.3 |
| | Bn 2 | +0.2 | 0.3 |
| | Cbn | +0.25 | 0.3 |
| Brass and timpani | Hn 1-4 | -0.45, -0.4, -0.35, -0.3 | 0.3 |
| | Tbn 1-2 | +0.3, +0.35 | 0.3 |
| | BTbn | +0.4 | 0.3 |
| | Tuba | +0.45 | 0.3 |
| | Timp | -0.05 | 0.4 |

- Widths below about 0.3 fold the spaced Main pair to near mono and risk comb filtering, so stay at or above 0.3.
- Targets: each stem's measured R-L within about 2 dB of its seat; woodwind stems within ±6 dB; master coherence at 0.8-3 kHz of 0.35 or more; side/mid of -3 dB or lower.

## 5. Timpani make up most of the 100-300 Hz band whenever they play (measured)

Where: Timpani, bars 2-3, 52, 60-62, 67-70, 79-81 and 89-92.

What is wrong: in these bars the timpani hold 85-100% of the master's 100-300 Hz energy (share -0.1 to -1.2 dB, a7.py).

Low-mid against mid (100-300 Hz over 500-2000 Hz):
- Bar 2: +5.9 dB. Bar 92: +6.1 dB.
- Reference median: -4.8 dB.
- Across the whole piece the mix's median is +0.9 dB, also above the reference.

Over the whole piece, the timpani's share of the long-term 250 Hz band is -1.7 dB, so they set the colour of the low mids. Cause: three mics are loaded (Close 0.43, Main 0.24, Surround 0.46), with the 3.3 s percussion IR. The roll dynamics themselves (BRIEF rule 5) belong to the timpani lens.

Fix:
- Unload Surround (`layerMatrix.columns[3].loaded = False`, as in finding 2).
- Move the timpani to the shared reverb (finding 3).
- Set `gain_db` -4 to start. Then hand the roll shape (CC7 lane in `score_to_parts.py`) to the timpani critic's numbers.
- Target: 100-300/500-2000 Hz in timpani bars at +1 dB or lower, with the timpani no longer the loudest stem at mp (now -29.8 dB, against strings at mp of -47 to -49).

## 6. Do not correct the dark top end with EQ yet (inferred)

Where: master, 4-8 kHz.

What: relative to 1 kHz, the mix is 4.8 dB below the reference at 4 kHz (-18.9 vs -14.1) and 5.2 dB below at 8 kHz (-35.4 vs -30.2). Part of this comes from the horns' brass reverb (horn stems' 3-10 kHz share is -35 to -42 dB) and from the bottom-heavy balance. The reference is an MP3 of a different piece that includes a fast movement.

Fix: no master EQ in cycle 1. Re-measure after findings 1-5, which move the balance toward Main mics and lower the bass and timpani. Only then consider a broad shelf.

Do not touch:
- The strings' perspective (Close 0.66 + Main 1.0) and their current IR, which become the reference room for everything else.
- The overall reverb amount: the final-chord decay already matches the reference to within a few dB through 0.5 s.
- The CC11/CC1 dynamic and vibrato lanes, the keyswitch logic and the tempo map. They are outside this lens and nothing here requires changing them.
- Stereo Double stays off in every patch.
