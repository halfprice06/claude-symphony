# Cycle 11 changes (actor)

Snapshot of the c10 tools and build/*.json: `before/`. Scratch and analysis scripts: `/private/tmp/claude-501/mockup-loop/c11-actor/` (`sim.py` level simulation on the c10 stems, `envfix.py` post-render envelope fix, `port.py`/`port2.py` glide checks, `A/bcdips.py` soft-join dips, `B/chk*.py` K-weighted level checks, `C/` critic C's crossover scripts).

## Process

1. Edited `tools/score_to_parts.py` and the build JSON files, regenerated parts.json, and diffed it against `before/build/parts.json`. In a trial build, the B #3 swell cap cut Horn 1's bar 7 p swell from CC 68 to 52, so the cap was narrowed before rendering (see B #3).
2. Simulated the level-only changes on the c10 stems: master peak -4.0 dBFS, mp3 LRA 14.4, span 19.1, limiter 3.1.
3. Ran `build_reaper.py --midi-only` on all tracks. Violins I got a full rebuild because its Opus state now loads the Leg Port MAX row. Then I saved and quit REAPER.
4. The restart hung twice at startup. `sample` showed REAPER's startup project load waiting in `CheckFaultyProject` on an alert, because reaper.ini had a `faultyproject=` entry. I did not use the GUI. Instead I killed REAPER, started it with `open -a REAPER --args -new`, and opened the project with a bridge job `reaper.Main_openProject("noprompt:...")`. It loaded in 17 s, and the samples streamed in to 52 GB with 0 GB compressed.
5. Rendered once (`render_cycle.py 11`). The attack gate passed 19 of 19. During the render, other work on the Mac compressed 36 GB of REAPER's memory, but the gate still passed.
6. After the render, Horn 3's qn 204 and Horn 2's qn 210 early fills measured 4-10 dB over the note body. I reshaped both in `early_fills.json`, updated REAPER (`--midi-only "Horn 2" "Horn 3"`, then saved), and applied the new-minus-rendered volume envelope to stems 13 and 14. The master was rebuilt as the stem sum; before the fix the stems summed to REAPER's master to -121.6 dBFS. This equals a re-render, up to the small difference between REAPER's envelope interpolation and linear-in-dB interpolation. The originals are in `render_pre_envfix/` (with the first mp3) and `metrics_pre_envfix/`. I then re-ran measure.py, probe_attacks.py (19/19) and deliver_master.py.

## Accepted

**A #1: soft string bow-change joins** (`BC_SOFT`, `BCSOFT`)
- The c08 VLA_BC_SOFT rule now applies to Violins II, Violas and Violoncellos at any note length. Joins at CC11 52 or lower stay Leg Slur MAX, overlapped, with a bow-change notch: 6 CC at CC11 40 or lower, otherwise 8.
- `BCSOFT["depth"]` 7 -> 0.
- Leg BC MAX counts went from 49/28/58 to 28/13/27 (Vln II/Vla/Vc).

**A #2: early fills with holds**
- `early_fills.json` dict values take `hold_s` (default 0.10). The fill holds to onset + hold_s and is 0 by + hold_s + 0.25 s. `pre_s` defaults to 0.
- 15 new or changed fills: Bn1 231/262/269, Hn1 203, Vln I 71/80/86, Vln II 65/66, CA 129.5/168, Ob1 142.5, Cl1 184/186, Vla 251.5.
- `note_trims.json` Bn1 231: 4 -> 1.

**A #3: Trombone 1 accents** (`ACCENT_DB_AT`)
- The accent at qn 212.5 is +4 dB and the one at 218 is +3 dB, with a 10 ms rise, held 0.12 qn, and 0 by 0.3 qn (exact breakpoints).
- Velocities unchanged (v108/105/110).

**A #4: portamento trial** (`PORT_TARGETS`)
- Violins I qn 82 (F5 -> B flat 5) and 172 (C5 -> F5) play Leg Port MAX at v100.
- The keyswitch goes in while the previous note sounds, and Leg Slur comes back before the next note.

**B #1/#2: the bar 61-62 wind chord and bass** (roles.json)
- Fl1 [204,208,-4]/[208,212,1.5], Ob1 [204,208,-3]/[208,212,-1], Ob2 [204,210.1,8], Fl2 -3 -> +1, Cl2 [204,208,-2.5].
- BCl [204,208.5,-4], Tuba 2 -> 5, BTbn 2 -> 4, Cbn [204,212,3].

**B #3: theme A arch** (`base_points`, `HP_GAIN_MF_DB`)
- An untargeted crescendo with no mark within 6 qn now looks ahead to the next rest of 2 qn or more, at most 16 qn.
  - Starting from mp or louder, it stays 8 CC under the next louder mark (minimum +6 CC). Vln I/II qn 68: CC 80 -> 64.
  - Starting from p or softer, it only stops at that mark. This is the narrowed version: Hn1 qn 20: 68 -> 58; Vln I/II qn 240: 68 -> 58.
- Crescendos that arrive on a printed mf get an hpgain of {wind 2, string 2, brass 1} dB. These arrivals do not chain into a following crescendo (`hpgain` item flag), and a chain keeps the f+ crescendo's own gain (`max()`).

**B #4:** `mix.json` `soft_trim_db.ppp` 1 -> 3.

**B #5: timpani p strokes**
- `timp_db`: p strokes +12 -> +16.
- Timpani [168,172,-4] -> [168,171.5,-4].

**B #6: bar 63**
- Tbn1 [212.4,213.6,3].
- Violins I, Violins II, Violas, Violoncellos and Double basses get [212.6,213.6,-2]. This ramps in from 212.1, after the sf attack. The critic's 212.35 start would have ramped in from 211.85, through the sf.

**C #1:** `LEG_EXTRA_S` Horn 1 {65: 0.15} (F4 departures).

**C #2: Horn 3 at qn 204**
- `entry_leads.json` Horn 3 204 +0.10.
- Early fills Horn 3 204 and Horn 2 210. After the render these were reshaped to {8, hold 0.10} and {5, hold 0.22}; see Process step 6.

**C #3:** new `build/leg_leads.json` (per-onset legato lead offsets, total clamped 0.03-0.35 s):
- Vln I {204: 0.07, 208: 0.05, 210: 0.05}
- Vc {204: -0.07}

**C #4:** `LEG_LEAD_S` "Violin I solo" 0.12; entry lead at qn 48 0.13 -> 0.20.

**C #5:** `LEG_PAIR_EXTRA_S` Vc (56,60) +0.15, Vla (60,63) +0.10, (65,61) +0.12.

**C #6:** `SHORT_SUS_DETACH`: slurred string short_sus notes (under 0.2 s, CC11 86 or higher) end 0.01 qn before the next onset, at v100 or more. The critic's threshold of CC 90 missed the f (CC 88) start of the figure.

## Rejected or deferred

- **A #5 (solo legato v96, lead 0.20): rejected.** It conflicts with C #4, which was measured (the solo crossed up to 0.10 s early). It was also unknown how v96 would move the timing.
- **B #3, the general "enter-on-arrival" hpgain rule: not done.** The roles in B #1 cover bars 61-62.
- **B #6, optional Vln II [212,212.3,-3]: not done.** It needed a check against the sf peak.

## Measured, c10 -> c11

**Delivery** (after the envelope fix; the first render measured the same to 0.1)

| | c10 | c11 |
|---|---|---|
| Master integrated | -23.6 LUFS | -23.7 LUFS |
| Master LRA | 21.6 LU | 21.5 LU |
| Master true peak | -3.6 dBFS | -3.6 dBFS (qn 205, strings) |
| mp3 integrated | -20.0 LUFS | -19.9 LUFS |
| mp3 LRA | 14.6 LU | 14.4 LU |
| mp3 true peak | -1.5 dBTP | -1.6 dBTP |
| mp3 span | 19.5 dB | 18.9 dB (now inside the 16-19 target) |
| Limiter | 3.6 dB | 3.5 dB (simulated 3.1) |

**A #1** (dip of every join moved from Leg BC to Leg Slur, c10 -> c11; `A/bcdips.py`)

| Section | Median dip (dB) | Joins of 7 dB or more |
|---|---|---|
| Violas (15) | 5.6 -> 3.1 | 5 -> 1 |
| Violins II (20) | 4.8 -> 6.2 | 4 -> 6 |
| Violoncellos (31) | 5.1 -> 5.3 | 10 -> 11 |

- The critic's long bcsoft targets mostly improved: Vc 157 10.0 -> 4.8, 162 9.3 -> 5.1, 48 7.5 -> 3.0; Vla 60 10 -> 5, 146 9.8 -> 3.5, 160 10 -> 2.5; Vln II 164 9.7 -> 6.8.
- New holes appeared on short joins that were fine on Leg BC:
  - Vln II 146 4.7 -> 9.5, 154 6.7 -> 10.8
  - Vc 45 4.1 -> 8.4, 144 3.8 -> 7.1, 160 7.5 -> 9.7
- Net: an improvement for the violas, a regression for Violins II, and mixed for the celli.

**A #2: holes.py dips (dB)**

| Join | c10 | c11 |
|---|---|---|
| Bn1 231 | 10.8 | 5.2 |
| Bn1 262 | 7.9 | 6.3 |
| Bn1 269 | 7.9 | 3.7 |
| Vln I 71 | 8.9 | 4.4 |
| Vln I 80 | 7.7 | 4.2 |
| Vln I 86 | 7.1 | 3.1 |
| Vln II 65 | 8.7 | 6.7 |
| Vln II 66 | 8.0 | 2.9 |
| CA 129.5 | 9.4 | 4.2 (CA 129: 5.7 -> 7.1) |
| CA 168 | 7.7 | 3.8 |
| Ob1 142.5 | 8.3 | 3.3 |
| Cl1 184 | 8.1 | 3.4 |
| Cl1 186 | 7.2 | 3.4 |
| Vla 251.5 | 8.1 | 3.0 |
| Hn1 203 | 8.2 | 7.2 (not fixed; the hole now starts before -0.15 s) |

**A #3/B #6: Trombone 1**

| Note | Measure | c10 | c11 |
|---|---|---|---|
| 212.5 | attack minus body | -1.7 | +2.0 |
| 212.5 | Tbn1 minus master, 0-150 ms | -5.4 | -1.5 |
| 213 | Tbn1 minus master, 0-150 ms | -2.7 | -1.2 |
| 218 | attack over the 217.5 note | +2.0 | +3.9 |
| 212.5 / 213 / 213.5 | Tbn1 minus all strings, K-weighted | -2.9 / +1.2 / +3.6 | +3.6 / +6.2 / +8.3 |

The Tbn1 stem's peak at 212.5 rose from -15.6 to -9.8 dBFS. The master peak did not rise.

**A #4: portamento**
- Crossovers: Vln I 82 -0.022 s, 172 +0.123 s.
- The f0 tracker (harmonic sum, 43 ms window) shows no frame where an intermediate pitch dominates, in c10 or c11. The intermediate-pitch energy measure is confounded by vibrato. The glide length is therefore not measured; the trial is inconclusive.
- The port notes have no holes (82: 5.3 -> 3.0 dB, 172: 3.2).

**B #1/#2: K-weighted levels, qn 204-212**
- The spread of the woodwind levels went from 13.3 to 5.1 dB.
- Ob2 went from -36.2 to -28.2 (Ob1 -26.5). Fl1 bar 61/62 went from -22.3/-27.3 to -26.3/-26.2.
- Tuba -32.4 -> -28.4, BTbn -32.6 -> -29.6, Cbn -33.5 -> -30.5, BCl -24.9 -> -28.9.
- Master bar 61/62: -13.3/-15.5 -> -13.8/-15.0. The fall went from 2.2 to 1.2 dB. Bar 61 is 4.7 dB over bar 79.

**B #3**
- Vln I+II at qn 81-84 minus qn 66-69: -0.9 -> 0.0 dB. The target was +2.5, so this is not met. Bar 25 (qn 72-75) is still the phrase's loudest bar.

**B #5: timpani attack minus the p strings, K-weighted, 150 ms**

| qn | Instrument | c10 | c11 |
|---|---|---|---|
| 172 | Vln I | -8.4 | -1.6 |
| 172 | Vln II | -6.1 | -3.4 |
| 271 | Ob1 | -3.7 | -2.7 |

**C #1: Hn1 crossovers**

| qn | c10 | c11 |
|---|---|---|
| 184 | +0.193 | +0.053 |
| 193 | +0.283 | +0.183 |
| 202 | +0.308 | +0.178 |
| 34 | +0.09 | -0.04 |
| 178 | +0.12 | -0.01 |

**C #2: Horn 3 at qn 204** (level relative to its body)
- c10: -12.4 dB at +0.10 s, body - 6 dB reached at +0.34 s.
- c11 after the fix: -5.4 dB at +0.10 s, a peak of +2.0 at +0.35 s.
- Before the fix, the plain 8 dB fill peaked at +9.9 dB over the body.

**C #3: Largamente crossovers**
- Vln I 204/208/210: +0.138/+0.068/+0.103 -> +0.068/+0.018/+0.053.
- Vc 204: -0.057 -> +0.018.

**C #4: the solo**
- Crossover median -0.027 -> +0.023 s. Range -0.102..+0.038 -> -0.052..+0.088.

**C #5**
- Vc 74/246: +0.233 -> -0.052.
- Violas: no change. The legato lead is capped at 0.45 x the previous note's length (0.15-0.225 qn there), and that cap was already binding.

**C #6**
- The median dominance share in qn 196-204 went from 0.27 to 0.26. There was no effect: the blur does not come from the overlap.

## Open
- **Soft-join regression in Vln II and Vc from A #1.** Suggested fix: keep BC_SOFT for the violas, and for Vln II/Vc only on targets of 1.4 s or longer at CC11 40 or lower (the old bcsoft set); otherwise return them to Leg BC MAX (BCSOFT depth stays 0). Re-measure with `A/bcdips.py`.
- **Hn1 203:** a 7.2 dB hole from -0.15 s, now that 202 starts earlier (C #1).
- **Hn1 193/202:** still +0.18 s late.
- **B #3:** the mf goal of bars 27-28 is still level with the phrase start. The CC cap and the mf hpgain gave about 1 dB.
- **C #6:** the viola sextuplets are still blurred. Next: try the Detache row (key 30) on a short range.
- **C #5 for the violas:** needs a different mechanism than lead, because the cap binds.
- **A #4:** the glide needs a better measure (a short-window f0 track on a range render), or a listening check by Dan.
