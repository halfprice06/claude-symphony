# Cycle 7 changes (actor)

Snapshot of the tools and build/*.json before this cycle: `cycles/c07/before/`.

## ONE_TIME.md (Opus PreloadSize 0): deferred, file left in place

Not applied. Critic C (#1) pointed out that the Opus manual (Audio Engine, manual page 27) says the HDD preload setting "needs considerable memory": it keeps more of every sample in RAM than the SSD setting (1). The late entries in c06 were caused by memory pressure (REAPER at 57 GB with 42 GB compressed; 72 GB with 69 GB compressed at the start of this cycle, on a 96 GB Mac), not by the preload size. Raising the preload would add to that cause. It could also raise the risk of another freeze like this morning's. Dan approved the change to fix late entries. That premise turned out to be wrong, so the change goes back to him with this evidence before anyone applies it. This cycle's render, from a freshly loaded REAPER at preload 1, passed every attack check (see below). PreloadSize is still 1.

## Render health

- New `build_reaper.py --midi-only`: replaces each track's MIDI item, volume envelope and ReaEQ without reloading the Opus patch. It is used only when the Opus state that would be written equals the state in `jobs/NN_*.b64` from the track's last full build; otherwise the track is fully rebuilt. All 26 unchanged tracks were updated this way in 26 s. Flute 2's state changed (its first articulation is now Leg Slur MAX), so it was fully rebuilt.
- Then the project was saved, REAPER was quit and reopened, and the patches loaded again (about 12 minutes). Fresh, REAPER held 49 GB with 0 GB compressed. The c06 session had grown to 72 GB with 69 GB compressed.
- `render_cycle.py` refuses to render while REAPER has more than 6 GB compressed (`--force` overrides). It writes `metrics/memory.txt`. This render: 49 GB, 0 GB compressed, before and after.
- Attack gate: **0 of 19 checks failed** (c06: 10 failed).
- Median entry arrival (body -6 dB, 165 entries): c05 0.062 s, c06 0.102, **c07 0.060**; p90 0.274 / 0.425 / 0.307.
- One render, no second render.
- The pre-roll warning threshold is now -40 dBFS. The qn 0 string leads start inside the pre-roll at about -53 dBFS, and the cut removes that part.

## Accepted

**A #1, Largamente portato (bars 61-62).** `score_to_parts.py`: `SOSTENUTO_SPANS = [(204, 212)]`.
- A slurred wind tenuto to a new pitch plays Leg Slur. It is a legato target with velocity 100 and a CC11 notch of 10.
- A repeated pitch is re-tongued on Sus. The note before it ends 0.01 qn early, the new note gets a 0.04 s lead and velocity 100 or more, and its keyswitch comes 0.012 qn before the note.
- Unslurred tenutos (Cl2, Bn, BCl, Cbn, Fl1) overlap by 0.03 qn into a new pitch, with the same lead and velocity.
- Measured join dips, c05 → c07: Ob1 208 8.0 → 4.9 dB; Cl2 208 6.8 → 5.2; Bn2 208 5.7 → 4.1; Fl2 206 8.7 → 6.1; Fl2 208 12.2 → 10.5.
- The 4 dB target is met only for Bn2. Fl2 still dips inside its Leg Slur transition up to F6.

**A #2, viola div. joins.** The c06 A #3 entry rule is widened on Violas and Violoncellos: a Sus MAX chord after any sounding note, below f, gets the entry lead and velocity 105 or more. The old chord's notes end 0.03 qn after the new chord's score onset.
- Violas qn 66-87: median dip 3.4 → 3.1 dB; joins of 6 dB or more 8 → 2. The worst is qn 82 at 6.4.

**A #3, soft Leg BC bump.** A CC11 contour `bcsoft` (-7 CC from +0.15 s to +0.5 s, back to 0 by +0.9 s) on Leg BC MAX targets at CC 40 or less that last 1.4 s or longer. It applies to 37 notes.
- Peak minus body, c05 → c07: Vln II qn 48 +7.9 → +6.4, qn 57 +6.4 → +5.4.
- Medians: Vla 4.7 → 3.3, Vc 2.9 → 2.1, Vln II 4.2 → 3.7.
- Partial: the 3 dB target is not met. A deeper dip, or an earlier one, is the next step.

**B #1-#6, levels.**
- `pitch_trims.json` takes `"_all_arts": true`, so its trims apply to Sus notes too. Values: Horns 1-4 F4 -5 / G flat 4 +4 / A flat 4 +3; Cb A flat 1 -5; Bn2 D flat 3 -5. Bn2's note trims are reduced by 5 dB to match.
- Climax bass line: Vc role split [250,262,-5] + [262,274,-1]; Cb role [262,276,-2] removed; Cb ff +1; Cbn f/ff 0.5/-2; Bn2 ff 0; BCl ff -3; Bn1 ff -0.5.
- Flutes: Fl1 262 -3 (was -6), Fl2 262 -6, Fl2 role [204,212,-3].
- Hn3 role at 79-81 eased from -4 to -1. Cb and Bn2 [146,151,-3] under the bar 47 oboe. Horn 4 286 -5 / 289 -3.
- Measured (K-weighted per beat):

| Check | c06 | c07 |
|---|---|---|
| Horn 2 at qn 204-207 | -27.9 | -32.2 to -33.7 |
| Horn 2 step at qn 208 | -8 dB | +4.1 dB (a rise inside the crescendo) |
| Cb against Cbn, qn 262-267 | 5-7 dB under | 1-2 dB over |
| Vc against Bn1 on the tenor line | 5-6 dB under | level |
| Bar 69 margin (Hn1) | -2.1 | +2.8 |
| Horn 4 over Horn 3, bars 87-89 | 5-7 dB | 1-4 dB |
| Oboe 1 over Cb/Bn2, bar 47 | -1 to -2 dB | +0.5 to +1.2 dB |

- Melody margins: bars 57-62 +4.2 to +6.2; bars 79-80 +3.3 / +3.5.

**C #2, entry leads.**
- Entry leads now apply from qn 0 for strings; the lead starts in the pre-roll.
- New `build/entry_leads.json` adds seconds per onset, with the total capped at 0.30 s. It holds Vln I/II, Vla, Vc, Cb, Hn1 226/261, Ob1 268 and Cl1/Cl2 268/280. These are the C #6 wind values, given per onset instead of a family-wide ENTRY_LEAD_S.
- Body arrival, c05 → c07:

| Entry | c05 (s) | c07 (s) |
|---|---|---|
| Vln I 48 | 0.30 | 0.22 |
| Vln I 171 | 0.38 | 0.20 |
| Vln I 292 | 0.36 | 0.18 |
| Vc 0 | 0.36 | 0.12 |
| Cb 60 | 0.25 | 0.19 |
| Hn1 226 | 0.12 | 0.06 |
| Hn1 261 | 0.21 | 0.13 |
| Cl1 268 | 0.17 | -0.04 |
| Cl1 280 | 0.12 | 0.07 |

- Not improved: Vln I 0 (0.18 → 0.60), Vln II 42 (0.24 → 0.45), Vla 54 (0.33 → 0.54), Hn3 0 (0.02 → 0.25; Hn3 has no lead, c06 was 0.23, so the opening block is suspect).

**C #3.** LEG_LEAD_S: Violins II and Violas 0.20 s; brass legato velocity 124 for long notes too.
- Median crossover, c05 → c07: Vln II +0.053 → +0.023 (Vln I +0.013); Vla +0.060 → +0.043.
- Vln II crossovers earlier than -0.05 s went from 10 to 25.
- Hn1 is unchanged (+0.033).

**C #4.** Leads are converted with `qn_before()` on the real tempo map, caesuras included. Leads into qn 204 and 268 are now 0.17 s, where they had been 0.25-0.30 s.

**C #5, final fermata.**
- The vol_db fade is now 0 dB to qn 303, -2 at 303.5, -10 at 304 and -20 at 304.5. The CC11 die-away starts at 303.5; it had started at 302.
- Master from qn 301, in 1 s steps: c06 -46.7 / -49.4 / -55.7 / -60.7 / -62.7 / -68.4; c07 -47.0 / -48.1 / -47.5 / -48.1 / -47.5 / -50.5 / -61.2.

## Rejected or deferred

- A #4 (solo violin track, DIV A patch): deferred. It adds an Opus instance; memory is the binding constraint, although a fresh load is now 49 GB.
- A #5 (Leg Port MAX on sul G/C/A leaps): deferred. It changes three string states and needs full rebuilds. It is a style gain on five notes.
- C #1b/c (re-render on probe failure; legato baseline in the probe): deferred. C #1a is done (the compression gate).
- C #2c (body -6 dB criterion in the probe): deferred.
- C #3c (viola triplets on short_sus in bars 37-40): deferred.

## Measured result

-25.3 LUFS integrated, LRA 23.7 LU, true peak -5.4 dBFS (c06: -25.1 / 23.9 / -4.2). 63 Hz -2.7 (c06 -4.7, ref -6.2); 125 Hz +0.3 (ref +7.0).

## Open

- Fl2 Leg Slur dips at qn 206/208.
- Vln II soft Leg BC bump still 5-6 dB.
- Vln I/Vln II/Vla soft entries at qn 0, 42 and 54 got later with the extra lead (measure the early part of the envelope before adding more).
- Fl1 at qn 262 is within 1 dB of Vln I.
- Bar 30: Cb is 5-10 dB over Vc, because Vc's role [78,90,-6] is low.
- 63 Hz rose 2 dB with the Cb ff trim.
- PreloadSize decision returned to Dan.
