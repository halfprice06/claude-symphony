# Cycle 12 changes (actor)

Snapshot of the c11 tools and build/*.json: `before/`. Scratch and analysis scripts: `/private/tmp/claude-501/mockup-loop/c12-actor/` (`sim.py`/`sim2.py`/`sim3.py` level simulation on the c11 stems, `sect.py` section loudness, `beats.py` per-beat levels, `band.py` horn/bass-clarinet bands, `env212.py`, `Aold/` critic A's scripts pointed at the c11 tempo map for c11 comparisons).

## Process

1. Edited `tools/score_to_parts.py` and the build JSON files, regenerated parts.json and diffed it against `before/build/parts.json` (note counts unchanged; Violins II, Violas and Violoncellos changed articulations as intended).
2. Simulated the level-only changes on the c11 stems before touching REAPER. The first version of the bar 79 lift put Clarinet 1 4 dB over Oboe 1, so Cl1's role was dropped and Ob1's raised. A global ppp soft trim of 1.5 (critic C #2) moved the intro only 0.3 dB, so it was not used; a Horn 3/4 cut in bars 1-6 was used instead (see C #2).
3. `build_reaper.py build/parts.json jobs --midi-only --tempo` (new tempo map from the phrase arcs; Violins II and Violoncellos were fully rebuilt because their Opus states now load the Leg Port MAX row). Saved, quit, reopened REAPER (16 GB, 0 GB compressed at the start).
4. One render (`render_cycle.py 12`). During the render, other work on the Mac compressed 31 of REAPER's 53 GB. The attack gate passed 18 of 19; the failure is Violoncellos qn 212 with a 6.6 dB dip (limit 6; c11 4.3). The 25 ms envelopes of c11 and c12 around qn 212 match within about 1 dB (`env212.py`); the probe takes the minimum of 10 ms frames inside the tremolo, so this is a threshold crossing, not a new hole. Not re-rendered.

## Accepted

**A #1: pizz. pitch trims as a step** (`score_to_parts.py`, pitch-trim loop)
- A pitch trim on a note whose articulation contains "izz" is a step: 0 at the moved onset - 0.03 s, full at - 0.01 s, held to the next onset (at most 1.5 s), released over 0.02 s, with exact breakpoints (`vol_bp`). Table values unchanged.
- Envelope at the F4 attacks: -0.9 -> -8.0 dB. Cb A flat 1 at 130/136 now 0 (role +5, trim -5) instead of +5/+3.

**A #2:** `BC_SOFT_SKIP` keeps the listed joins on Leg BC MAX (Vln II 48/54/57/146/154/159/271, Vla 159, Vc 45/50/60/62/132/144/160/220). Leg BC counts 28/13/27 -> 35/14/35.

**A #3:** `PORT_TARGETS` Violins II {82, 172} and Violoncellos {83}, v100 (full rebuilds of both tracks).

**A #4:** roles Vln I [170.4,171.75,-4,0.15] and Vln II [170.4,171.7,-2.5,0.15]. The cut is at full value on the pickup's moved onset (170.80/170.87) and gone before the Leg Port targets' moved onsets (171.85/171.82); the end_ramp form keeps it off the F5.

**A #6:** `leg_leads.json` Violins I {262: 0.05}. The target and the three grace notes moved 0.041 qn earlier together.

**B #1:** `note_trims.json` Vln I 68 +4, 72 -3, 80 3 -> 6, 82 2 -> 3.5; Vln II 68 +6, 70 +3, 80 3 -> 8, 82 +2.

**B #2:** roles Vln I [0,9.2,-5]; [292,304,-3] -> -6.

**B #3 + C #1: bars 79-81 and bars 61-62** (roles.json, note_trims.json, `score_to_parts.py`)
- New roles.json key `"_all"`: rows applied to every track. `[204,212,-1]` takes 1 dB back at bars 61-62.
- Strings: Vln I/Vln II/Vla/Cb [262,268,2.5], Vc [262,268,2] (on top of its [262,274,-1]). Plain spans, so Vln I's chains from its [244,262,2].
- Winds: Fl1 [262,270,-2] removed (Fl1 rises with Vln I and keeps its relation to it); Ob1 [262,268,6]/[268,271,4]; Cl2, Bn2 [262,268,4]; BCl, Cbn [262,268,2]. Note trims at 262: Fl2 -6 -> -3, Ob2 -4 -> -1, Bn1 -5 -> -2. Not taken: C's +3 on Fl1/Cl1/Bn1 (simulated Cl1 4 dB over Ob1 and Fl1 the loudest wind) and Bn2 259 -5 -> -2 (the c09 reason, its f arrival over the melody flute, still holds).

**B #4:** Horn 3 [286,298] -4 -> +1, Horn 4 -4 -> -1.

**B #5:** Cor anglais [98.5,102,-3].

**C #2 (alternative):** Horns 3-4 [0,17,-2]. In bars 1-6 the pp horn chord (Hn3 -49.7, Hn4 -51.3 dB) was the loudest stem, 2-4 dB over the clarinets and strings. The global ppp soft trim stays at 3: 1.5 simulated only -0.3 dB in the intro, and critic B asked to keep the soft-trim table.

**C #3: phrase arcs** (`score_to_parts.py` `PHRASE_ARCS`, applied after `smooth_tempo`, before `add_caesuras`)
- For 14 phrases (C's list minus (90,102), which ends on the printed rit. at 102, so its last beats would slow and then jump back to 52): x1.015 from start + 1 qn to the midpoint, x0.96 over [end - 2, end - 1), x0.92 over [end - 1, end). Steps on whole qn only.
- +0.025 to +0.114 s per phrase, +1.06 s in total (0.3%). The tempo map has 385 entries (was 323).

**C #4:** Bass clarinet `soft_trim_db` {ppp 0, pp 1, p 3.5} and a ReaEQ high shelf 2.5 kHz -4 dB.

**C #5:** Horns 2-4 [204,212,2] (net +1 with the `_all` -1), Horns 2 and 4 [262,268,2].

## Rejected or deferred

- **A #5 (viola sextuplet articulation test): deferred.** It needs range renders of three articulations. The cycle allows one render, and the c04 freeze came from back-to-back renders.
- **C #6 (Vln I [286,292,-2]): not needed.** Violins I rests in bars 87-88; the bar 89 rise is its entry, which B #2's -6 now covers.
- **C #2 as written (global ppp 3 -> 1): not used** (see above).

## Measured, c11 -> c12

**Delivery**

| | c11 | c12 |
|---|---|---|
| Master integrated | -23.7 LUFS | -23.6 LUFS |
| Master LRA | 21.5 LU | 23.9 LU |
| Master true peak | -3.6 dBFS | -3.9 dBFS |
| mp3 integrated | -19.9 LUFS | -19.8 LUFS |
| mp3 LRA | 14.4 LU | 15.7 LU |
| mp3 true peak | -1.6 dBTP | -1.6 dBTP |
| mp3 span (p10 to max) | 18.9 dB | 18.4 dB |
| Limiter | 3.5 dB | 3.0 dB (simulated 2.4) |

**Climaxes (C #1, B #3)**
- S max of bars 59-64 minus bars 78-82: master 4.8 -> 1.6 LU (target 1.5-2.5); mp3 4.1 -> 1.4.
- Bar RMS (momentary power mean), master: bar 60 -17.7 -> -18.1, bar 61 -13.9 -> -14.7, bar 79 -18.5 -> -16.4 (now 1.7 dB over bar 60), bar 81 -22.5 -> -21.6.
- Simulated per-stem levels at qn 262-265: Vln I -30.4 -> -28.0; woodwind spread (Cl1 .. Bn2) 8.6 -> 6.6 dB, Ob1 -40.1 -> -35.1. Vln I stays 4.7 dB over the loudest wind (Cl1).

**Soft perspective (C #2, B #2)**
- Section power mean in the mp3, LU relative to integrated: intro (bars 1-6) -5.4 -> -6.5, horn solo (7-14) -5.6 -> -5.5, coda (83-92) -6.7 -> -6.5. The intro is now 1.0 LU under the horn solo (was 0.2 over); target 1.5-2.5, not met. The coda is 1.0 LU under it (target 2), not met.
- Bar 1: Vln I -49.6, Vln II -51.5, Vla -52.6 (Vln I was 6 dB over Vln II). Bars 89-90: Vln I -48.4 -> -51.9 dB RMS, now under Vln II (-50.2).

**A #1 pizz. (critic A's `pizz.py Violas`)**: p10-p90 spread 8 -> 5.7 dB; largest note-to-note jump 14.5 -> 6.7 dB; median -38.8 -> -38.0. F4 peaks -30.7/-29.8 -> -36.6/-36.0/-44.6 (two within 2.5 dB of the median, one 6.6 under, a round robin). Vc 112/122 -37.3/-37.4 against a median of -38.3.

**A #2 join dips (`holes.py`, c11 -> c12)**

| Track | Listed joins | Median of all joins | Joins of 7 dB+ |
|---|---|---|---|
| Violins II | 48 3.1->1.1, 54 5.5->2.8, 57 3.5->-0.2, 146 9.5->4.6, 154 10.8->5.4, 159 7.2->4.7, 271 2.6->-0.2 | 4.4 -> 4.5 | 12 -> 11 |
| Violas | 159 7.9->6.4 | 3.4 -> 3.1 | 8 -> 7 |
| Violoncellos | 45 8.4->4.1, 50 8.9->5.3, 60 4.9->1.1, 62 6.9->3.6, 132 7.9->4.7, 144 7.1->4.4, 160 9.7->6.2, 220 3.9->3.9 | 4.7 -> 4.5 | 22 -> 11 |

**A #3 portamento (`pitchtrack.py`, mean energy 0.15-0.45 s after the window start)**: Vln II 82 G5/A flat 5 -26.0/-22.0 -> -5.3/-3.1 dB (a glide like Vln I's). Vc 83 B flat 3 / C4 -4.4/-18.6 -> -0.1/-12.3 (a smaller rise).

**A #4 pickup into bar 53 (`upbeat.py`)**: downbeat minus pickup Vln I -5.5 -> -2.8 dB, Vln II -3.1 -> -2.1. Target 0 to +2, not met.

**A #6 (`dom.py`)**: Vln I B flat 6 dominates from +0.105 -> +0.055 s. The grace notes now sound 0.045 s earlier against their score slots (own share 1.00/0.82/1.00 -> 0.65/0.41/1.00 measured on score slots).

**B #1 theme A (Vln I + II RMS per beat)**: qn 68/69/70 -42.3/-42.4/-39.7 -> -39.0/-39.5/-40.2 against a qn 65-67 mean of about -37.9 (1.1-2.3 dB under; was 4.4-6). qn 82 -37.9 -> -34.2: 3.7 dB over the phrase start and 2.5 dB over qn 72 (both checks met).

**B #4 coda horns (RMS per bar from qn 286/289/292/295)**: Hn3 -54.6/-57.3/-56.9/-57.7 -> -49.7/-52.3/-52.3/-54.5; Hn4 -51.4/-53.0/-54.0/-54.5 -> -48.9/-50.4/-51.3/-48.8. Violas -44.2/-51.0/-50.1/-52.0.

**B #5**: CA minus BCl at qn 99/100/101: +1.3/+2.6/+2.0 -> -3.0/-1.0/-0.1 dB.

**C #4 (qn 18-42)**: Hn1 minus BCl overall 5.5 -> 7.4 dB (target 7 met); in 2-6 kHz -3.4 -> +0.3 dB (target +2, not met).

**C #3**: total length +1.06 s. Attack gate 18/19 (see Process step 4).

## Open
- The intro and coda are each 1.0 LU under the horn solo in the mp3; the targets are 1.5-2.5 and 2. The intro sits at the ride's +10 dB cap. Next: Hn3/Hn4 another -1 to -2 dB in bars 3-6, or the coda strings' pp.
- Pickup into bar 53 still 2-3 dB over its downbeat: the remaining step is the F5 Leg Port target's own sample level (try +2 dB on the target rather than more cut on the pickup).
- Violas pizz. F4 at 131.67 now 6.6 dB under the line (a round robin); refit the table over the whole figure.
- Bass clarinet 2-6 kHz still level with Horn 1 in bars 7-14.
- A #5 viola sextuplets: still untested.
