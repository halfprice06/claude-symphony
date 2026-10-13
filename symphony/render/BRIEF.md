# Audio rendering: actor–critic cycles

Goal (Dan, 2026-10-09): improve the quality of the MP3 recording of movement I, using techniques found on the web, through actor–critic cycles.

Source: the score is final at /mnt/project-files/symphony/mvt1/v120 (LilyPond; score.midi is the MIDI LilyPond writes, after tools/fixmidi.py). Do NOT change the score or anything in mvt1/. Rendering-only changes to the MIDI (expression curves, velocity, timing, articulation, program choice, panning, reverb sends) are allowed, and must be made by scripts in the render folder that read v120's MIDI (or the LilyPond source, compiled in a scratch copy) and write a new MIDI. The printed notes, dynamics and tempos are the reference: a rendering must not contradict them.

Folders: /mnt/project-files/symphony/render/rNN/ holds one cycle's pipeline: render.sh (or a Python script) that rebuilds the output from v120 with one command, any scripts, a config, out.mp3, and NOTES.md (what changed and why, with sources). r00 is the baseline: FluidR3_GM.sf2 through FluidSynth, gain 0.6, loudnorm -20 LUFS, 192 kb/s. Large downloaded assets (soundfonts, impulse responses, samples) go in /mnt/project-files/symphony/render/assets/ with a line in assets/README.md giving source URL and licence. Use only freely licensed assets.

Cycle N: actor N builds rN from r(N-1) and critic (N-1)'s report; critic N reviews rN and writes critics/cNN.md. HISTORY.md logs accepted and rejected ideas.

Nobody in this process can hear audio. Judge with measurements: spectrograms and long-term average spectrum, loudness range (EBU R128 LRA), short-term loudness against the score's dynamics, onset timing, stereo image, reverb decay, clipping, noise, and comparison with real orchestral recordings of similar music that are freely available (for example public-domain or CC recordings on archive.org, Musopen, Wikimedia Commons). Say clearly which judgements are measured and which are inferred.

Tools available: fluidsynth, ffmpeg, lilypond, python3 (mido, numpy, scipy, soundfile installable with pip). 4 CPUs. Rule: never delete files in /mnt/project-files; put new outputs in new folders.

## Dan's priorities (2026-10-09)
Dan: "Articulations and volume of individual tracks and blend are really important." So every cycle must address, and every critic must measure:
1. Articulations: staccato, accents, tenuto, marcato, slurs/legato, tremolo, pizzicato and the printed articulation marks in v120 must be audible as different note lengths, attacks and (where the samples allow) different sample sets or programs. Critics check this per instrument against the score (sections/*.ily in mvt1/v120).
2. Volume of individual tracks: each instrument's level must match its printed dynamic and its role (melody above accompaniment), at every dynamic level. Critics measure per-track levels by rendering stems (one track at a time) and comparing with the printed dynamics and with orchestral balance norms (e.g. one horn equals two woodwinds in forte; Rimsky-Korsakov).
3. Blend: sections must sound as one ensemble in one room (common reverb, seating panning, matched tone colours, no instrument sticking out because of a sample set).

## Software rule (coordinator, 2026-10-09)
Do not install new software packages (apt, .deb, pip, binaries) unless the coordinator's prompt names that package. Data assets (samples, impulse responses) with free licences are fine. If a sample set needs a player that is not installed, write the playback in Python (numpy/scipy/soundfile are available) or use what is installed (fluidsynth, ffmpeg, lilypond).

## Dan on timpani rolls (2026-10-09, after hearing r01)
"The timpani rolls need help also, especially where they are very long they need to not drown other things and should fade softer unless explicit crescendo." Rule: a roll starts at its printed dynamic and then decays gradually (a real roll is sustained by strokes but settles below its attack level; long rolls should sit under the texture as support). Only a printed crescendo hairpin makes a roll grow. Long rolls must never be the loudest stem unless the score marks the timpani as the leading part. Critics measure timpani level against the other stems in every roll longer than one bar.
Dan also: "the roll doesn't sound very realistic." Options, best first: (1) a real recorded timpani roll sample from a free library (e.g. VSCO 2 CE / Virtual Playing Orchestra timpani rolls, looped and crossfaded for long rolls); (2) if only single strokes exist, build the roll from alternating-hand strokes with round-robin samples, random timing jitter (±5–10 ms), velocity variation (±8–12 %), overlapping decays, a stroke rate that drops for soft rolls, and no identical repeated sample. Critics check the roll for audible machine-gun repetition (periodicity in the envelope at the stroke rate).

## Series 2 (Dan, 2026-10-10): 20 more cycles, r03–r22, on both movements
Dan: "an independent thread work on render quality in an actor critic loop, like 20 loops ... use latest versions of
the two movements to test (they should be merging periodically)". Run in the thread "Render quality loops".
Procedure and test inputs: LOOP2.md and TESTSET.md in this folder. Changes from series 1:
- The renderer must render ANY version folder of movement I (symphony/mvt1/vNN, 4/4, has percussion) or movement II
  (symphony/mvt2/vNN, mixed metre 3/4 and 4/4, no percussion) with one command, without hand-edited bar lists. Anything
  tied to bar numbers of one version (the melody list, roll lists) must be derived from the score's own markings
  (espr., dolce, cantabile, solo, hairpins, rolls) in the LilyPond event log, or it breaks when the movements change.
- Every cycle renders and measures BOTH test inputs. A change that helps one movement and hurts the other is rejected
  or made conditional on what the score prints, never on the movement number.
- Both movements are still being revised in other threads. Never write into symphony/mvt1/ or symphony/mvt2/.
- The r02 copy in symphony/mvt2/render/r02 belongs to the movement II thread; leave it alone.

## Dan on accents (2026-10-10 12:08 UTC, after hearing r04-era renders)
"Accented notes have too much attack." Rule: accents must be softened. The earlier target (accent peak boost >= 3 dB,
reached 6-8 dB in the strings with VPO accent samples plus +8 velocity, and 4.6-7.7 dB in the Iowa woodwinds) was too
high. An accent should stand out by emphasis and weight, not by a hard transient: aim for about 2-4 dB peak boost, a
less sharp onset (compare attack time and onset crest with unaccented notes and with accents in the reference
recordings), and no click-like front edge. Critics measure accent boost and onset sharpness per instrument against this.

## Movement III (2026-10-12)
Movement III (symphony/mvt3/vNN) also has to render with the same renderer. It uses cymbals and bass drum. Open:
perc.py must parse drum chords and \tweak in \drummode, and the bass drum needs a sound (free sample, e.g. VPO/VSCO 2 CE).
