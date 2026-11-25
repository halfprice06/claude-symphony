# Cycle 19, critic A: articulation and phrasing (on the cycle 18 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c19-A/`: the c18-A set, plus `cbvc.py` (cello and bass attack times at shared pitch changes; variants `cbvc10.py` and `cbvc2k.py`) and `cbatt.py`. `lib.py` now measures levels (`env`, `lvl`) on stereo power instead of the mono fold, because c18 found L/R anti-phase frames. Run the scripts with `CYC=18 ~/.venvs/claude-composes-reaper/bin/python`. Onsets are score onsets (`sq`). I regenerated parts.json from the current tools into scratch, and it is identical to `build/parts.json`, so the data matches the c18 render.

## Checked and working (measured, c18)

- **Chords, slurs, ties and keyswitches.**
  - No chord goes to a legato patch (`chords_leg.py`).
  - Every slurred pitch change plays on a Leg articulation, except the intended ones: the viola sextuplets in bars 59-60 and the CA portato at 157.
  - All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
  - Every keyswitch is at least 20 ms before its note, except the known Ob1 207.952 (13 ms).
- **Legato joins on the new c18 tracks** (`wjoin2.py`):
  - Horns 1-2 a2: 6 joins, median dip 1.7 dB, largest 3.3 dB.
  - Violas div: 8 joins, median 2.6 dB, largest 6.7 dB at 69.
  - Every legato track has a median dip of 0.6-3.7 dB. Only Vln I has a join of 8 dB or more (1), and Vc has 2.
- **The a2 horns' breath at 265.** The level falls from -32 to -44.6 dB, which is still at least 10 dB.
- **Printed breaths.** Every other printed breath dips 9.6-29 dB (`breath.py`).
- **Divisi tracks.**
  - Violins II div plays its 5 Flautando notes with the planned holds.
  - Violas div at 66-90 plays Leg Slur/Leg BC single lines. This is right: the quarter-note dyads in bars 24 and 28 are unslurred.
  - CC15 follows the printed con/senza sord. on all three split tracks. The DIV B patches carry the same ConSordino filter (CC15) as the full sections.

## 1. Horn 4 loses the first two beats of its held A flat 3 in bar 80, then re-attacks it 0.1 qn before beat 3. Measured.

**Where:** Horn 4 at qn 265-268 (bar 80, f). The score prints Hn4 A flat 3 as a dotted half from 265 to 268, under the Hn 1-2 a2 line, whose own A flat 3 lasts 265-267.

**What is wrong:**
- `find_unisons()` (tools/score_to_parts.py) still groups Horn 4 with Horn 1 because they share a patch (Solo FH KS Master). It does not know that Horn 1's notes in 261-272 now play on the "Horns 1-2 a2" track (2FH KS Master).
- The regenerated log shows `unison qn 265.00 pitch 56: keep Horn 1, drop ['Horn 2', 'Horn 4']`. Because Horn 4's note outlasts the kept one, `UNI_DELAY` moves its start to 266.9 instead of dropping it.
- So Horn 4 plays `qn 266.9, dur 1.1` in parts.json.

**Evidence (Horn 4 stem, stereo power):**

| qn | 265.0 | 265.25 | 265.5 | 266.0 | 266.5 | 266.75 | 267.0 | 267.5 |
|---|---|---|---|---|---|---|---|---|
| dB | -33.1 | -49.6 | -53.8 | -72.7 | -81.5 | -90.2 | -37.2 | -33.2 |

- `rebow.py` reports this as a 33 dB dip that lasts 0.69 s.
- The horn chord on beats 1-2 has three players instead of four.
- Beat 3 gets an unprinted tongued f attack in the middle of a tied-through dotted half.

The rule was right in c17, when Horn 1 played the a2 line on the same patch. The new track makes it wrong.

**Fix:** in `find_unisons()`, leave out notes that `TRACK_WINDOWS` takes away from a track. Build `allnotes` like this:

```python
def _owned(tn, q):
    w = TRACK_WINDOWS.get(tn)
    return w is None or (w[0] - EPS <= q < w[1] - EPS) == w[2]
allnotes = [(t[0], n) for t in ts for s_ in t[1] for n in notes[s_] if _owned(t[0], n["qn"])]
```

- The a2 track is the only track on 2FH, so it is never grouped.
- Horn 4 then plays 265-268 from the start.
- The Horn 2 drops inside 261-272 are unaffected, because Horn 2 is windowed out there anyway.
- Nothing else changes. The other unisons (Ob 210, Cl 259, Bn 196) lie outside every window.

Then run `--midi-only` (no state change).

**Check:**
- Horn 4 stays within 3 dB of its body over 265-268.
- No new attack at 266.9.
- The horn sum (Hn3 + Hn4 + a2) at 265-267 is about 1-1.5 dB higher than c18. That is expected: a fourth player on the chord.

## 2. Rerun the wind fills on c18. Cor anglais 132 swings between overshoot and hole, so change its shape, not only its size. Measured.

**Evidence** (`fljoin.py`, 200 ms window; `auto_fills.py 18 build/parts.json` without `--write`):

| Join | c17 fill -> 200 ms result | c18 fill -> 200 ms result | auto_fills proposal |
|---|---|---|---|
| CA 132 | 5.2 -> over +3.1 | 3.1, hold 0.16 -> dip 7.2 at +0.16 s, over +1.9 | 6.1, hold 0.21 |
| CA 134 | 4.0 -> over +3.3 | 1.7, hold 0.30 -> dip 5.9 at +0.18 s | 3.6, hold 0.23 |
| Ob1 143 | 5.3 -> over +3.1 | 2.8 -> dip 6.7 / auto dip 2.5 | 1.3 |
| Cl1 178 | (removed in c18) | dip 6.2 at +0.02 s | new 3.2, hold 0.10 |
| Hn1 36 | - | dip 5.1 at +0.31 s | new 2.1, hold 0.35 |
| Vc 203 | - | dip 5.7 at +0.10 s | new 2.7, hold 0.15 |

- At CA 132 the same join shows a peak and then a hole. The c18 fill ends (hold 0.16 s) exactly where the dip sits (+0.16 s), so the hole comes after the fill.
- Raising the amount back to 6.1 will bring the c17 overshoot back.

**Fix:**
- Run `tools/auto_fills.py 18 build/parts.json --write` as usual. Keep its new and removed entries.
- For CA 132 and CA 134, set the fill by hand in `build/early_fills.json` and list both under `_auto` as "c19 shape":
  - CA 132: `{"db": 4.0, "pre_s": 0.0, "hold_s": 0.30}`
  - CA 134: `{"db": 3.0, "pre_s": 0.0, "hold_s": 0.32}`

  This gives a lower lift held past the dip, instead of a taller and shorter one. It is inferred from the dip time; nothing was rendered.

**Check:** CA 132 and CA 134 both show a 200 ms dip of at most 4.5 dB and an overshoot of at most +2.5 dB.

## 3. The double basses change pitch about 0.1 s after the celli in the loud bass line. Measured, but the measurement is noisy. The fix is a test.

**Where:** shared Vc/Cb pitch changes, mostly bars 53-62 and 72-78 (mf-ff). Cb plays every arco note on Sus MAX with no lead: 91 of its 94 notes start on the score onset. The celli play Leg BC/Leg Slur, led by 0.15-0.22 qn.

**Evidence** (`cbvc.py`: harmonics 2-5 of the new pitch, leaving out harmonics shared with the old pitch, time to reach body - 6 dB):

| Measurement | Cb | Vc | Cb - Vc |
|---|---|---|---|
| All 58 shared changes, c18 (median) | +0.21 s | +0.06 s | +0.095 s (p75 +0.31) |
| Same changes, c17 | | | +0.11 s |
| Body - 10 dB threshold | | | +0.10 s |
| 2048-sample window | | | +0.05 s |
| Bars 53-62 and 72-78 only (31 changes) | | | +0.11 s (p25 -0.10, p75 +0.34) |

The worst changes are around +0.4 to +0.57 s: qn 162, 193, 200, 220 and 243.

**Caveats:**
- The spread is wide.
- c15's `ABUT_LEAD` test, the same mechanism on pp bassoons, gave mixed arrivals and new holes on same-pitch repeats.
- So I am not certain a fixed lead helps. It is worth one guarded test, because the basses carry the harmony changes at both climax approaches.

**Fix (test):** use the existing `ABUT_LEAD` code with a loud-only condition:

```python
ABUT_LEAD = {"Double basses": {"lead_s": 0.08, "max_cc": 127, "min_cc": 70, "overlap_qn": 0.02}}
```

- Add a `final(q) >= abut_["min_cc"]` test next to the `max_cc` test.
- Skip a led note whose next note has the same pitch (the c15 failure).
- Leave pizz. and the pp coda as they are.

**Pass criterion:** on the same 31 changes, the median Cb - Vc is at most +0.03 s. No new 6 dB trough in `rebow.py` for Double basses, against 31 re-attacks of 4 dB or more in c18 with a mean of 3.8 dB. If it fails, set `ABUT_LEAD = {}` again.

## Not findings, checked

- **Horns 3-4 con sord. (286 on).** The drive has only stopped-horn patches (`1FH Stop Sus`). Adler (reference-books/text/adler1.txt, lines 16977-16987, "Muted and Stopped Horn") says a stopped horn sounds different from a muted one, so keep `mute_eq`.
- **Vln I "div." in bar 63 (212-216, ff/sf tremolo).** Two full-section tremolos at -3 dB. A DIV A Close-only half section would stand out in a tutti ff, so leave it.
- **Viola "non div." double stops at 204-210** on the full section. These are correct as written.

**Do not touch:**
- **Ties, slurs, keyswitches.** Tie handling and the timpani tie strokes. Keyswitch placement. Slur-scoped overlap. The Leg Slur/Leg BC split with its leads and v124.
- **Joins.** `BC_SOFT`/`BC_SOFT_SKIP`, `SOST_HOLD_THROUGH`, `slur_out`, `JOIN_NOTCH`.
- **c18 tracks.** The three new tracks and their splits. The a2 window and its legato.
- **Marcato and accents.** The Tbn1 marcato and accent shapes.
- **Pizzicato and harp.** Pizzicato steps. The harp rolls and the harmonics track.
- **Mutes.** CC15 placement and `mute_eq`.
- **Breaths and phrase ends.** Breath gaps and phrase-end releases.
- **The `UNI_DELAY` rule itself.** Keep it for real same-patch unisons. Only its grouping changes in #1.
