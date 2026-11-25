# Cycle 7, critic C: tempo, timing and transitions (on the cycle 6 render)

Under review: `cycles/c06/render` (master and 27 stems), `cycles/c06/metrics`, `build/parts.json`, `tools/score_to_parts.py`, `tools/probe_attacks.py`, `tools/render_cycle.py`, `v77/global.ily`, and score pages 5 and 8.

Method. Envelopes are RMS on 10 ms windows with a 5 ms hop. All times are measured against the score onset `sq` through the parts.json tempo map, caesuras included. I used three measures:
- **Entry arrival:** the time a note after at least 0.3 s of silence reaches 6 dB under its own body level (mean over sq+0.25 to +0.6 s).
- **Legato crossover:** the time the new pitch's harmonic energy (4 harmonics, 85 ms FFT) overtakes the old pitch's and stays ahead for 40 ms.
- **Ensemble spread:** at every score onset shared by 3 or more tracks, the latest arrival minus the earliest.

The MIDI notes for Vln I, Vln II, Cb, all winds, brass, timpani and harp are identical in c05 and c06; I diffed `cycles/c06/before/build/parts.json` against `build/parts.json`. So c05 is a clean control for those tracks: whatever moved between the two renders was moved by the render, not the data. Scripts are in `/private/tmp/claude-501/mockup-loop/c07-C/`: `entries.py`, `ent2.py`, `leg.py`, `dom.py` and `lib.py`.

The tempo map is not a problem. For every rit./allargando span, the map's duration matches the printed `\mt` steps to within 0.2 s: bars 33-36 14.58/14.60 s, bar 47 4.13/4.14, bars 53-60 31.55/31.37, bars 61-64 19.30/19.30, bars 78-82 19.24/19.10, bars 89-92 18.66/18.67. The problems are all in how notes sit on that map.

## 1. The c06 render's strings, horns and timpani are 0.1-0.3 s late because of memory pressure; the next render will be worse unless memory is dealt with first (measured)

Where: every string track, the horns and the timpani, across the whole piece. The winds are not affected.

Evidence (measured; MIDI identical between the two renders):
- **String legato crossovers, c05 → c06 median:**
  - Vln I +0.008 → +0.078 s
  - Vln II +0.053 → +0.120 s
  - Vc +0.028 → +0.118 s
  - Hn1 +0.033 → +0.068 s
- **String legato crossovers later than 0.15 s, c05 → c06:**
  - Vln I 3 → 27
  - Vln II 11 → 46
  - Vla 15 → 36
  - Vc 3 → 39
- **Winds:** Fl1, Ob1, CA, Cl1, BCl and Bn1 measured within 0.003 s of c05 at every percentile.
- **Entries:** 41 of 165 arrive more than 0.1 s later than in c05. Brass median arrival -0.005 → +0.151 s. String median arrival +0.032 → +0.096 s.
- **Ensemble spread at shared onsets:** median 0.120 → 0.220 s, p90 0.254 → 0.426 s.
- **Climax downbeat, bar 61 (qn 204), c06:** winds +0.02 to +0.10, violins +0.12/+0.15, timpani +0.23, Horns 2/3 +0.26/+0.27. In c05 all of them were within -0.06 to +0.12.

The c06 actor recorded REAPER at 57 GB, with 42 GB of it compressed. I read it again now (`top -l 1 -o mem -stats pid,command,mem,cmprs`): **REAPER 72 GB, of which 62 GB is compressed, on a 96 GB Mac.** The samples stream from `/Volumes/MAC DRIVE` over USB.

ONE_TIME.md wants `PreloadSize` 0 ("HDD"). The Opus manual (EW-Opus-Software-Manual, Audio Engine, manual page 27) says the HDD setting "needs considerable memory": it loads more of each sample into RAM than the SSD setting. Inferred: in the present state this would add to the cause of the lateness. Dan approved the change to fix late soft entries, but those entries were late in c06 because of memory, not because of the preload size. The actor should put this to Dan before applying it.

Fix:
- **(a) `render_cycle.py`, before the render:**
  - Read REAPER's CMPRS column from `top`. Refuse to render while it is above about 4 GB.
  - Restart REAPER after a full rebuild and before rendering: save, quit, reopen, and wait for the quiet-memory check. Each rebuild sets 27 Opus states, and memory has grown from 57 to 72 GB between cycles (inferred: the old instruments are not freed).
  - Quit other memory users (the chrono-25d Python jobs) before rendering.
- **(b) `render_cycle.py`, after the render:** if `probe_attacks.py` fails, render once more before handing over. Do not publish a render that fails the probe.
- **(c) Add a legato check to `probe_attacks.py`.** Use these c05 crossovers as the baseline: Vln I qn 174/178/184/186/192, Vln II 172/178/186/192, Vc 178/184/192, Hn1 178/186. Fail if the median crossover is more than 0.04 s above the c05 median of the same notes. The present probe has only isolated attacks, and it would not have caught the legato drift.

## 2. Soft string entries arrive 0.15-0.26 s after the other sections, including the opening chord (measured on c05, which had clean timing)

Where:
- Opening chord, qn 0: Vln I +0.16, Vc +0.17 (Hn3 +0.01).
- Vln I: qn 48 (bar 17) +0.18, 171 (bar 52.75) +0.24, 292 (bar 89) +0.26.
- Vln II: qn 42 (bar 15) +0.15, 108 (bar 37, flautando) +0.17, 286 (bar 87) +0.20.
- Vla: qn 54 +0.14, 140 +0.12.
- Vc: qn 152 +0.17.
- Cb: qn 60 +0.18.

All are body-6 dB arrival times in c05. For comparison, the c05 medians are: winds +0.036, harp +0.002, timpani +0.002, brass -0.005. Strings have a median of +0.032 but a p90 of +0.176.

Evidence (measured):
- Arrival order at shared onsets in c05:
  - qn 292: Timp +0.00, Vc +0.03, Cl2 +0.04, Vla +0.07, Vln I +0.27.
  - qn 286: Hn3/4 -0.08, Cl +0.05, Vln II +0.22.
  - qn 171: CA -0.02, Vln I +0.27.
  - qn 42: Ob1 +0.01, Vln II +0.19.
- These notes start about 0.1 s before the beat at about -70 dB (the 0.12 s soft entry lead), then take 0.3-0.4 s to reach their body. That is the soft Leg Slur first-note sample (inferred from the envelope shapes).
- The opening chord gets no lead at all. In `score_to_parts.py` (the entry-lead block after `ent_s = by_name(ENTRY_LEAD_S)`), the condition `q > 0.5` and the clamp `L = min(q, ...)` both date from before the c06 pre-roll.
- Vln I qn 48 has CC11 54, over the 50 threshold, so it gets only the 0.06 s "louder" lead.
- `probe_attacks.py` passed Vln I 171 at +0.04 s. Its threshold is peak-20 dB, which measures when a note becomes audible, not when it arrives.

Fix:
- **(a) The opening chord.** In the entry-lead branch, replace `q > 0.5` with `q > -EPS`, and `L = min(q, ...)` with `L = min(q + PREROLL_QN - 0.5, ...)`. The qn 0 notes then start inside the pre-roll; `build_reaper.py` already adds 3 qn to everything. Check that `build_reaper.py` accepts a negative note qn, and that the CC11 `pulls` span may begin below 0.
- **(b) An onset-keyed extra lead.** Add a new file `build/entry_leads.json` in the style of `note_trims.json`, `{track: {sq: extra seconds}}`. Add the value to `L` in the same branch, cap the total at 0.30 s, and convert it through the tempo map (see #4). Values (measured lag - 0.05 s):
  - Vln I: {0: 0.11, 48: 0.13, 171: 0.19, 292: 0.21}
  - Vln II: {42: 0.10, 108: 0.12, 286: 0.15}
  - Vla: {54: 0.09, 140: 0.07}
  - Vc: {0: 0.12, 152: 0.12}
  - Cb: {60: 0.13}
- **(c) The probe.** Add a body-6 dB criterion to `probe_attacks.py` for Vln I 171 and 292 and Vln II 286, with a limit of 0.10 s.

Risk (inferred): the first 0.2 s of these notes will sound at -20 to -25 dB under the body before the beat. In a pp entry this should read as the bow starting, but check it against the c07 render.

## 3. Second violins, violas and Horn 1 make their legato changes late against the first violins and the winds (measured on c05)

Where:
- **Vln II.** All 113 transitions have v124 and a 0.17 s lead, as Vln I does. Median crossover +0.063 s against Vln I's +0.013. On the 90 transitions the two sections share, Vln II is later by a median of +0.022, and by more than 0.1 s in 18. Worst:
  - bar 27.7 (+0.27)
  - bar 53.5 (+0.26)
  - bar 75.7 (+0.27)
  - bar 81.8 (+0.24)
  - bar 29.8 (+0.23)
- **Violas.** Median +0.063, 15 transitions over 0.15 s:
  - The 8th-note triplets in bars 37-40 (0.33 s notes) cross at +0.15 to +0.22. In bars 39.4-40.4, 8 of 24 notes are the strongest pitch for less than half of their own slot (dom.py; median own share 0.71).
  - The C4 departures in bars 71-75 cross at +0.23 to +0.29 in c05, before c06's `LEG_EXTRA_S`. Because of #1, c06 cannot show whether that fix worked.
- **Horn 1.** In the build to the climax, the notes at v112 (the >0.9 s notes in `LEG_VEL_STRONG` brass) cross late: qn 184 +0.20, 193 +0.28, 200 +0.16, 202 +0.31. At the same onsets the strings and winds cross at -0.05 to +0.10. Hn1 at v124 has a median of +0.028; at v112, +0.048.

Fix:
- **(a) `score_to_parts.py` `LEG_LEAD_S`:** add `"Violins II": 0.20` and `"Violas": 0.20`. Caution: `by_name` tests `k_ in tname`, so a `"Violins I"` key would also match "Violins II". Add only the "Violins II" key, or change `by_name` to test `k_ == tname` first.
- **(b) `LEG_VEL_STRONG`:** set brass to `(124, 124)`. The manual (HO User Manual, True Legato, about line 3400 of the text) says velocity sets the transition time, not loudness, from 110 to 127 for "tightening up the timing."
- **(c) Viola triplets in bars 37-40:** apply the deferred A #4b (`short_sus` up to 0.38 s for Violas) to qn 108-124 only. The c05 render had clean timing and supports the change: the slots the notes do not own are the measured problem.

## 4. Note leads are converted to qn at the onset's tempo, so they come out too long after a slower span; the cellos reach the bar 61 climax note 0.17 s before the beat (measured)

Where: every lead that crosses a tempo change or a caesura.
- qn 204 (bar 61, after the 0.22 s caesura): Vln I, Vln II and Vc legato leads are 0.298 s instead of 0.17.
- qn 268 (bar 81): Vln I, Vln II and Vla 0.249 s.
- qn 220 (bar 65): Vc 0.236 s.
- qn 108 (bar 37): Vln II and Vla 0.167 s instead of 0.12.
- Cbn and Hn2/3 at qn 204: 0.105/0.088 s instead of 0.06/0.05.

Evidence (measured): I compared `q2s(sq) - q2s(qn)` with the intended seconds for every note in parts.json. Only these notes differ, all by +0.035 to +0.128 s.

The cause is in `score_to_parts.py`. `L = leg_s * bpm_at(q) / 60`, and the entry equivalent, use the tempo at the score onset. But the moved start lies in the 0.25 qn before it, which runs at 30.8 bpm at qn 203.75 and 31.8 bpm at 267.75, and at 43 or 37 bpm before the a tempo/Tempo I bars.

In c05, the Vc crossed into the bar 61 climax note at -0.17 s, during the winds' breath, while the timpani hit at +0.01 and the horns entered at -0.04. The cellos arrive before the downbeat that the caesura sets up.

Fix: add a helper in `score_to_parts.py` that returns the qn lying a given number of seconds before q on the real map (the inverse of `qn_to_sec`, caesuras included). Use it for all three lead types: legato, entry and the new entry_leads. Then `L = q - qn_before(q, seconds)`, and the cap `0.45 * (q - pv["qn"])` stays.

## 5. The final fermata is faded out: the chord is 15 dB down 2.6 s after it arrives, and the fermata beat itself sounds 20-30 dB under the arrival (measured)

Where: bar 92 (qn 301-304), all tracks.

Score (page 8): decrescendo in bars 91-92 to ppp, then a fermata on a dotted half in every part; Cl2 has morendo. Nothing is printed after the ppp.

Evidence (measured):
- **Tempo map:** bar 92 runs at about 35 bpm for two beats, then 20 bpm for the fermata beat (3.0 s). The chord lasts 6.3 s, 339.9 → 346.2 s.
- **Fade:** `vol_db` drops 2 dB per 0.25 qn from 301.75 to 304, -20 dB in all (the timpani -11 → -31). This runs on top of the CC11 decrescendo to 22.
- **Master, 0.5 s windows:** 340.0 s -45.5, 341.0 -49.4, 342.0 -56.2, 343.0 -61.3, 344.0 -62.1, 345.0 -67.9, 346.0 -74.0.

The listener hears a ppp chord for about 2.5 s and then a fade to nothing. The 20 bpm beat that stands for the fermata is spent between -61 and -74 dB.

Fix: in `build_reaper.py`, where the final fade is built (`vol_points`), hold 0 dB to qn 303.0. Then fall -2 dB at 303.5 and -10 dB at 304, which is the last 3 s. The timpani keep their offset: -11 to 303, -21 at 304. The ppp body then lasts the whole fermata and dies in its last 1.5 s.

This is the c02 "final-bar fade" do-not-touch. Only its timing changes; its depth and existence stay.

## 6. Winds re-entering after the bar 81 breath, and Horn 1's soft entries, arrive 0.1-0.15 s behind (measured on c05; the same in c06)

Where:
- qn 268 (bar 81, after the 0.15 s caesura): Ob1 +0.12, Cl1 +0.15, Cl2 +0.09. At the same onset the strings are at -0.04 to +0.01, and Bn/BCl/Hn4 at +0.04.
- Cl1 qn 280 (bar 85): +0.11.
- Hn1 qn 226 (bar 67): +0.11, and qn 261 (bar 78.67): +0.13.

Evidence (measured): these notes have their first transient on time (Cl1 268 is at -48 dB at +0.05 s), then take 0.15-0.2 s to reach their body (-34 dB at +0.17). `ENTRY_LEAD_S` has no oboe or clarinet entry. Horn entries with CC11 over 50 get 0.05 s.

Fix: in `ENTRY_LEAD_S`, add `"Oboe": (0.05, 0.07)` and `"Clarinet": (0.05, 0.08)`. This is case-sensitive, so it does not match "Bass clarinet". Add Hn1 {226: 0.06, 261: 0.08} to `entry_leads.json` from #2.

**Do not touch:**
- The tempo map: `RAMP_SPANS`, the extrapolated ends and the two caesura amounts. Durations match the printed steps to within 0.2 s per span.
- Keyswitch placement. No keyswitch falls inside a moved note's lead; the smallest keyswitch-to-note gap is 28 ms, in the Leg BC/Slur alternation in bars 58-60.
- The harp, pizzicato and timpani attacks. In c05 their median arrival was 0.00-0.01 s.
- The wind legato tables. Medians were 0.00-0.06 s, unchanged in c06.
- The pre-roll.
- The section-arrival note ends before qn 204 and 268. Winds breathe about 0.48 s before and strings about 0.2 s before, as printed.
