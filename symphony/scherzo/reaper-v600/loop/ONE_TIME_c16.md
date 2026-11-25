# One-time notes for the cycle 16 actor

The cycle 15 actor received items 1 and 2 as messages while it worked. Read `cycles/c15/CHANGES.md` first and skip what it already did.

## 1. Movement II envelope measurement (reports in `symphony/mvt2/reaper-v600/cycles/c55/reports/`, read only)

SAFETY: never exec or import `tools/build_reaper.py` whole to reuse `vol_points` while you do not hold the lock. The file sends bridge jobs to whoever holds REAPER. Cut the source before `ENV_LUA`, as `stem_fix.py` does.

- About 22,000 points for 1,507 onsets; 77 % of envelope travel inside single notes; by class: shape 59 %, slow 23 %, per-note level 17 %.
- No measured benefit there, removed: SWELL_DB, SOST_SUSTAIN_DB on winds and brass, METRIC_DB on harp and pizzicato, PT_DB_PER_ST / phrase tops, SLUR_PAIR_RELEASE.
- Measured benefit, kept: re-bow fills, early fills (about 60 rows hurt and went), join notches, level fits, pitch and note trims. With the whole shape class off, join holes rose 298 to 371 and the cello counter-melody step 1.50 to 3.48 dB. Remove shapes by kind and line, not the class wholesale.
- Faults: level trims keyed to the moved note-on cut the previous note's last 140 ms by 2 dB at 67 joins; trims fall to 0 dB between neighbours that both carry a lift (85 pairs); start shapes stack (16 notes at 8 dB or more) and peak after the beat on 155 of 392 notes.
- A 3 dB cap must clip the deviation from the note's mean, not the absolute value.
- 16,000 points remained with both per-note classes off because hairpins and roles are stairs on the 0.125 qn grid; ramps plus a 0.1 dB simplification gave about 8,400.
- Balance does not depend on the shape class but does on per-note levels (up to 6.3 dB).

## 2. Movement I c56 results (first render there with the envelope cut back)

- Points written 52,200 to 32,612; strings 9-14 points/s to 5-10. Notes with 3 dB or more inside the note fell only 2,334 to 2,129 (strictly inside the sounding note 1,331 to 1,054). What remains: fitted per-note level steps, kept accents and fills, repeated-note dips, body lifts, re-bow fills. Report both counts each cycle.
- A generic NOTE_LEVEL pass (one level per onset) removed trims that returned to 0 dB between notes of a run (314 notes).
- Level changes and lift ends keyed to the next note's score onset with a 40 ms crossfade: join holes over 9 dB on Violins I 66 to 49, theme timing kept.
- Repeated-note dips are needed: separation falls from 5.5-7.3 to 2.1-4.8 dB without them.
- A plain +4 dB cap on final-chord re-bow fills left 6-10 dB holes in simulation; a residual refit was used.
- Point thinning at 0.1 dB tolerance is safe (largest change 0.11 dB).
- Level steps on the beat move measure S readings with no note-on changed.
- Basses: deleting mute_eq and raising the 87.3 Hz bell from -10 to -4 dB lifted the 70-112 Hz share -15.0 to -13.7 dB with no peak problem.

## 3. Dan's direction on per-note shaping (2026-11-11 16:25Z, after hearing Movement I c56)

"the notes say the per note volume shaping was cut back, it definitely sounds better so im wondering if we should go further or why we couldn't"

The default is to remove a per-note layer. Keep one only where its removal causes a fault a listener would hear (a join hole, lost repeated-note separation, a main line dropping under its accompaniment, a click), shown by measurement on the stem. A slightly worse step median is not a reason to keep it. In CHANGES.md list each per-note layer kept, on which lines, and the audible fault its removal caused, with before/after counts.

## 4. Dan's method direction (2026-11-11 16:27Z): volume envelope for slow balance only

"i still don't understand, is this volume shaping done in any of the example projects or the east west guide is it desribed? i don't understand why its really necessary at all on a per note basis"

Goal for all four movements: follow the reference practice (example projects, EastWest templates). The track volume envelope carries slow balance only: roles, section levels, hairpins as ramps. Each per-note fix that is still needed (re-bow dips, sagging long notes, repeated-note separation, uneven sample levels, join bumps) moves to the instrument side: CC11/CC1, velocity, patch or articulation choice, note lengths and overlap, keyswitch timing. A per-note volume move stays only where no instrument-side fix works and the fault is audible on the stem. List every such exception in CHANGES.md with line, bars and fault. Movement I is writing the rule into the shared guide (mockup-kit, read only); read it if present.

This is the first priority of cycle 16. Start from "left for cycle 16" in `cycles/c15/CHANGES.md`.

## 5. Dan's decision (2026-11-11 16:30Z): no per-note volume adjustments. This replaces items 3 and 4 where they differ.

"yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem"

Rule: no per-note track volume adjustments at all, and no exceptions list. The track volume envelope keeps only slow balance: roles, section dynamics (hairpins as ramps), fades. Every fault the per-note moves covered is fixed on the instrument side: CC11/CC1, velocity, patch or articulation choice, note lengths, gaps and overlaps, keyswitch timing. If a fault cannot be fixed that way, leave it audible and list it in CHANGES.md (line, bars, measured size). Do not put a per-note volume move back.

Balance depended on per-note levels by 2-8 dB (c15 critic B), so carry those levels in velocity, CC11 or a per-line constant, and check the balance table after. Acceptance check for the render: on every track, the volume envelope has no point pair closer than one beat except at a printed dynamic change or fade, and no change keyed to a note onset.

## 6. Finale c16 techniques (first render there with every per-note fader rule off)

Items 60-69 in `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` (read only). Read them before the envelope work. In short: tag each envelope item with its rule so rules switch off by name (60); evaluate envelope changes on dry stems with `symphony/mvt3/reaper-v600/cycles/c16/actor_scripts/envsim.py` (61); piecewise-linear lanes and 0.1 dB thinning, REAPER fader scale values (62); string short rows take 3.4-11.0 dB from 16-22 velocity steps, layer boundary 88-100 on Violins I (63); row levels in the patch via layerMatrix.rows[].volume (64); basses' repeated eighths on "Stac On Bow RRx9" at 58 % of the slot with velocity by bar position, but that row came out early and scattered on their full render (65); tail-only return rides at tutti stops (66); crescendo trim holds per confirmed hairpin only, 104 changed against 7 needed (67, check our c14 `cresc_trim_hold`); ReaEQ narrow bells cut more than the RBJ model (68); range renders need the last keyswitch before each range (69).

Audible there after removal, not yet fixed: weak printed accents (CC bump of 5 units is not enough), basses uneven by pitch (12 dB spread), brass tongued changes running together, softer timpani strokes. Check for the same here.

## 7. Finale c17 critic findings, instrument-side only (`symphony/mvt3/reaper-v600/cycles/c17/reports/`, read only)

1. Accents cannot sound at ff because the controller has no headroom: strings and woodwinds sit at CC11 114 where the slope is 0.1-0.2 dB per unit, and accent velocity does nothing on sustain rows. Fix there: lower the resting CC (about 104-106 strings, 98 winds, 100 brass and clarinets), the slow dynamic trim makes up the level, accents at 121-124 held 0.15 s.
2. "Leg Slur MAX" is 3-7 dB under "Sus MAX" at f/ff on strings, horns, trombone: per-row offset by dynamic.
3. Tongued notes run together only where the played gap is under 60 ms; 90 ms gaps give 5-13 dB of separation: gap floor 0.09 s brass, 0.065-0.07 s winds.
4. "Stac On Bow RRx9" on basses: 76-101 ms from note-on to half-rise, each of nine round-robin samples has its own start time (75-118 ms), velocity 65-95 does not change its level.
5. Timpani 0.17-0.24 dB per velocity step.
6. Leftovers to check after removing per-note rules: unison plateaus covering one or two notes, hairpin-gain releases and role edges that step 2-3 dB inside a sounding note (keyed to the score onset after a led note-on), timpani roll gains.
7. A wet stop there came from a dry cello open-string release, not the hall.
8. Bass pitch spread must be measured with the printed dynamic removed (12.2 dB pooled, 7-10 dB real); the basses' F2 excess exists only in the loud sample layer.
