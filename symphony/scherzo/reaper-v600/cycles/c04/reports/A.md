# Cycle 04, critic A: articulation and phrasing (render c03)

Material: `cycles/c03/render/` (stems after the c03 stem fix, master), `build/parts.json` (the c03 data: tempo map, moved onsets, keyswitches, lanes), `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py`, `tools/auto_fills.py`, `tools/pcx.py`, the brass KS Master `.oib` files (row sample folders and region counts read with `opus_state.py`), score pages 1 and 4, and May 2021 HO manual PDF pages 100 and 103-107 (group A5) in full, with pages 101-102 read for the Long and Short folders the A5 pages refer to. Times come from the parts.json tempo map (qn 0 = 0 s of the rendered files). Levels are RMS on the stems in 10 ms windows (2.5 ms hop) unless stated. Labels: **measured** (a number from this render or parts.json), **read** (code, patch file, score, manual), **inferred**.

## Manual notes (A5: PDF pages 100, 103-107; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 100 | Hollywood Brass has solo instruments and sections (Solo Horn, Solo Trumpet, Solo Trombone, Solo Tuba, 2 French Horns, 2 Trumpets, 2 Trombones, 3 Trumpets, 6 Horns...). | Trumpets 1-2 play a third apart (101-120, 331-339); Hn 3-4's a2 countermelody (105-120, 305-320). | Followed. Solo patches for the divided trumpets; the a2 horn unison plays on Horn 3 with Horn 4's copy dropped (Horn 4 `unison_dropped` 28, read). The 2FH a2 patch would be the alternative (kit section 8); not needed now. |
| 101 (read for context) | **Portato**: each note held its full length, or nearly, without being tied: non-legato, not staccato. Rows: 1FH "Port Lng"/"Port Shrt", 1TB/1TU "Portato". | Every printed brass tenuto: the tutti chord quarters of Tbn 1-2, B.tbn, tuba and Hn 1-2 (105-120, 305-320, 331-339), the dolce Hn 3-4 tenuto dotted halves (73-88), Hn 1's mp tenutos (209-222). | **Not followed.** All are Sus MAX slices with tenuto CC11 bumps (finding 2). |
| 102 (read for context) | Short notes have no release trails; brass staccato at the highest velocity adds an overblown attack. | Any brass staccato row. | No brass staccato row is used. Keep a staccato row's velocity under its top band (finding 1). |
| 103 | **Repetitions** (Fst 170 / Med 145 / Slw 120 bpm, synced to tempo, best near the base tempo; with release trails). | Trumpets' repeated B4s (q, e, e, q at quarter 264 and 288). | Correctly not used: no base tempo near 264 / 288 (MANUAL-GAPS #15). |
| 103 | **Triple Performance** (3 Trumpets only: exactly three repeats). | None (the head is q, e, e, q). | Not applicable. |
| 103 | **Double Tongue** ("tiki tiki") lets a player articulate fast note sequences. 1TP has "Stac DblTng RRx9" (5,595 regions) and "StacSs DblTng RRx9" (4,080), read. | The trumpets' staccato theme head (56 printed staccatos per trumpet). | **Not followed.** Every trumpet staccato is a cut Sus Non Vib MAX slice (finding 1). |
| 103 | **Sforzando Crescendo** (Solo Horn, Solo Tuba: accented attack, then a strong crescendo; short notes act as sfz staccato). | No brass sf / sfp is printed (the sfp of bar 301 is woodwinds and strings; read). | Not applicable. |
| 104-105 | Effects: trills, rips, shakes, flutter, clusters; recorded **Crescendos** (Fast/Medium/Slow, or MOD SPEED on CC1 in three bands), no release trails. | The brass pp < f dotted halves of bars 101-104 (qn 300-309, about 2 s) could be a recorded crescendo. | Not used: CC1 crossfade instead. Inferred low gain (a 2 s swell under the tutti hemiola); not ranked. |
| 105 | Legato only with no gap and at most an octave between notes; trombone slide legato; legato patches mono (CC22 0-63 = poly). | Hn 1 call (bars 3-6), motto tail (357-360), Hn 3 countermelody, horn legato lines. | Followed. No brass legato step over 12 semitones and no chord on a brass legato row (read in parts.json). |
| 106 | Legato Slur: CC1 sets volume and, near 127, opens an overblow filter; **velocity sets the transition speed**. | Every horn legato target. | CC1 peaks at 108 (Hn 1-2) and 115 (Hn 3-4), clear of overblow (read). Targets play v124 (fastest slur): crossovers Hn 1 +0.04..+0.10 s at 9, 14, 1071, 1074, 1077, Hn 3 +0.01..+0.13 s at 105-120 (pcx, measured), so timing is fine. A slower velocity for the p espress. call and motto tail is a matter of taste: not ranked. |
| 106 | Legato Slur Accent (accent strength by velocity); **Legato Slur Repetitions** (re-tongued 2nd/3rd same-pitch notes inside a slur); Slur Runs. | No brass accents (score c200, Dan's rule); no slurred brass same-pitch repeats (`slur_rep_merged` empty on every brass track, read). | Correctly not used. |
| 106-107 | Mutes and stopped horn; keyswitch rows highlight when selected. | No mute or stopped passage printed. No keyswitch clashes (`ks_clash` empty on every brass track, read). | Followed. |
| (read, .oib) | The 1TB "Portato" row maps the Solo French Horn "Nvb mp" sustain folders next to its own "1Tb Port Cln f/mp" samples (a patch-file quirk). | Any trombone portato. | Use it only at f, and check one note's pitch-class spectrum after the render. |

MANUAL-GAPS additions: #10 should list the trumpets' staccato head under #1/#2 (1TP Stac DblTng RRx9, 5.6 thousand regions) and the portato row sizes (1FH Port Shrt 815 / Port Lng 775, 1TB Portato 730, 1TU Portato 600 regions: cheap). #2 can drop the trumpet "LegRep RRx4" idea: the trumpets' repeats are staccato, not legato.

## Findings, ranked by what a listener would gain

### 1. The trumpets' staccato theme head is played on cut sustain samples: each quarter peaks one eighth late, and the second of the repeated eighths does not re-attack (S1).

- **Where.** Trumpet 1 and 2, every printed staccato: bars 101-103 pp (qn 300-308), the ff tutti 105-120 (qn 312-356, the head q-e-e-q on B4 / F sharp 4 / E4 every second bar), and the coda build 331-336 (qn 993-1004). 56 staccatos per trumpet (read).
- **Read.** All 63 notes per trumpet are on "Sus Non Vib MAX". In parts.json the heads also have uneven leads: the quarter and the first eighth start 0.22-0.264 qn (50-60 ms) early, the second eighth and the closing quarter 0.075 qn (17 ms) early. So the two eighths are 0.645-0.689 qn apart instead of 0.5 (33-43 ms too far apart), as an entry lead after the detach gap and a re-tongue lead.
- **Measured (per note, 10 ms envelope, peak in the note's own window, dip = lower peak minus the minimum between the two peaks).**
  - Trumpet 1, qn 300-358: peak after the score onset, median: quarters on beat 1 +115 ms, first eighth +67 ms, closing quarter +112 ms. One eighth at quarter 264 lasts 114 ms. Dip from the first to the second eighth: median 1.5 dB, minimum -0.7. At 319.5, 325.5 and 331.5 the second eighth has no peak of its own; the first one's swell carries straight through it.
  - Trumpet 1, coda 993-1005: first-to-second eighth -0.6 dB median. Trumpet 2: 3.5 dB (101-120) and 2.5 dB (coda).
  - Note shape (notes followed by at least 0.3 s): Trumpet 1 peak at +115 ms, -10 dB only at +219 ms. In the same bars the woodwind "Stac DblTng RRx9" peaks at +35..+78 ms and the string staccatissimo rows at +50..+80 ms.
  - The trumpets are not loud (each about -18 dB of the master's 1-5 kHz energy in bars 105-120, measured). Even so, they are the only instruments carrying the head rhythm on one repeated pitch through the tutti, and they swell instead of articulating.
- **Fix (manual p.103 double tonguing; p.102 short rows; the woodwind precedent, MANUAL-GAPS #1).**
  - In `build/score_config.py` (c04 block):
    `_TSTAC = [(22, 50), (34, 58), (46, 66), (58, 74), (72, 84), (88, 96), (114, 106), (124, 110)]`
    `for _t in ("Trumpet 1", "Trumpet 2"): ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": 0.0, "to": SCORE_END, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _TSTAC}]`
    The velocity stays under the top band, because brass staccato at the highest velocity adds overblow (p.102; Dan: weight, not bite). The held notes (309, 357, 1005-1014) stay on Sus Non Vib MAX.
  - `tools/score_to_parts.py`, about line 3405: `STAC_LEAD_S` acts only on `family in ("string", "wind")`. Add "brass" (generic), then `STAC_LEAD_S.update({"Trumpet 1": 0.02, "Trumpet 2": 0.02})`, so all four notes of a head get one lead and the uneven entry/re-tongue leads go.
  - Memory: +5,595 regions per track, about 0.25 GB each at c02's 4 GB per 92 thousand (read, inferred). If the 45 GB cap does not allow both, do Trumpet 1 first, or use "StacSs DblTng RRx9" (4,080).
  - Level: the woodwind row came out -4.5..+4.9 dB against the Sus slices it replaced (c01). `ROW_TRIM_DB` acts on strings and winds only, so balance the trumpets with roles in `roles.json` after measuring, not with velocity (the row barely follows velocity, c02).
  - Pass: first-to-second-eighth dip of 4 dB or more on both trumpet stems; quarters peak within +70 ms; trumpet level within 1 dB of c03 in bars 105-120 (measured).

### 2. Brass tenutos play as Sus MAX swells: the tutti chord quarters peak 150-160 ms late and ring past their value, and the soft tenuto repeats dip 10-14 dB in one horn and 2-3 dB in the other.

- **Where (read).**
  - (a) The tutti chord quarters on beat 1 (tenuto): Trombone 1-2, Bass trombone and tuba in bars 105-120 (qn 312-357) and 331-339 (993-1014). Hn 1-2 in 105-120 and 305-320 (tenuto on beat 1, staccato on beat 3).
  - (b) The dolce Hn 3-4 tenuto dotted halves of the F major episode, bars 73-88 (qn 216-261, pp, winds and harp without strings).
  - (c) Hn 1's mp tenuto dotted halves under the trio's ff return (624-666).
- **Measured.**
  - (a) Notes followed by at least 0.3 s, qn 312-360. Peak after the score onset / -10 dB point (written quarter = 227 ms): Trombone 1 +162 / +391 ms, Bass trombone +145 / +343, tuba +153 / +296, Horn 1 +85 / +315.
    The string staccatissimo rows in the same bars peak at +50..+72 ms and are 10 dB down by +150..+227 ms. The double basses' Sus MAX quarters peak at +231 ms, the same swell.
    Coda 993-1017: Trombone 1 +195 ms, Horn 1 +161, Horn 2 +158, tuba +152.
    The envelope is front-weighted (CC11 93 -> 88 and +2 dB -> 0 over the quarter), so the late peak is the sample, not the lanes. Each brass chord quarter grows through the beat ("waa") instead of speaking on it, and then rings into the rest.
  - (b) Re-tongue dips (mean of -0.2..-0.08 s minus the minimum over -0.08..+0.06 s), same-pitch repeats with the 0.1 s horn gap:
    - Horn 3: 219 6.7, 225 8.2, 243 9.3, 255 10.7, 258 10.8 dB.
    - Horn 4 at the same bar lines: 219 2.4, 243 2.5, 258 2.6 dB.
    - Master: 3.3-5.4 dB.
    - Horn 3's CC11 falls from 36 to 25 before each repeat (`WIND_REP_RETONGUE_BY["Horn"]` fall_cc 12 at pp, read). The pair of dolce horns pulses unevenly, and one of them chops.
  - (c) Horn 1 at 630 / 633 / 639 / 663: 13.6 / 14.1 / 11.6 / 12.2 dB. Also 999 12.9 and Horn 3 1011 14.0. A tenuto is a full-value note: 3-6 dB is the target (kit section 7: portato dips).
- **Fix (manual p.101: Portato is exactly this articulation; MANUAL-GAPS #10).**
  - Generic, `tools/score_to_parts.py` about line 2201: let an `ART_SPANS` entry take `"mark": "tenuto"`, matching `ten_q` as "staccato" matches `stacc_q`.
  - Then in `build/score_config.py`:
    - `ART_SPANS` on Trombone 1, Trombone 2, Bass trombone: `{"from": 300.0, "to": 1017.0, "art": "Portato", "mark": "tenuto"}`. Tuba: the same with its "Portato".
    - Horn 1-4: `"Port Shrt"` for the tenuto quarters, spans (311.9, 360.1), (911.9, 960.1), (992.9, 1017.0). `"Port Lng"` for the tenuto dotted halves, spans (215.9, 262.0), (623.9, 667.0), (599.9, 610.0), (683.9, 706.0).
    - Hn 1-2's beat-3 staccato quarters can take "Port Shrt" at 0.5 of their written length in the same spans. This is inferred; the horn staccato row "StacSs RRx9" costs 6,910 regions.
  - Memory: Port Shrt 815, Port Lng 775, trombone Portato 730, tuba 600 regions (read): about 4-6 thousand in all, about 0.2 GB.
  - The portato samples have only mp and f/ff layers (folders read). Check that the pp dolce horns (b) do not jump in level against Sus MAX, and note the trombone row's quirk (Manual notes, last row).
  - Fallback, if portato is not adopted: per-dynamic horn re-tongue `WIND_REP_RETONGUE_BY["Horn"] = {"gap_s": 0.06, "frac": 0.2, "fall_cc": 6, "fall_s": 0.1}` for tenuto repeats. Target 3-6 dB on both horns of a pair.
  - Pass: (a) brass chord quarters peak by +90 ms and are 10 dB down by +300 ms; (b) and (c) tenuto repeats 3-6 dB, with Horn 3 and Horn 4 within 2 dB of each other at each bar line.
  - Whether the portato samples speak faster than Sus MAX is inferred (they are recorded detached notes); measure the first render.

### 3. The coda build's staccato eighth pairs blur in the inner strings and on the master (S1), because the coda still plays the plain Stac rows that the two ff tutti statements replaced.

- **Where.** Bars 328-335 (qn 981-1005, Più mosso, quarter 288: an eighth lasts 0.104 s), the head's repeated eighths at 982, 985, 988, 991, 994, 997, 1001 and 1003, mf rising to ff at 996 (read).
- **Measured (first-to-second eighth dip, peaks in the two eighth windows).**
  - Master: 3.0 / 2.1 / 5.8 / 1.5 / 8.0 / 0.0 / 3.0 / 2.7 dB, median 2.4. Against that, theme A 36-84 4.4, reprise 756-804 5.1, tutti 312-360 3.7.
  - Violins II (Stac RRx9): median 1.7, with 0.0 at 985, 991 and 994. Violas (Stac RRx9): median 1.2, with 0.0 at 985, 994, 997 and 1003.
  - In bars 105-120, on the tutti rows (`_TUTTI_STAC`: Violins II Spiccato RRx9, violas Staccatissimo RRx16, Violins I Stac RRx14), the same sections dip 5.4 / 5.7 / 6.4 dB.
  - At 991 the violas' first eighth rises only about 2 dB over the tail of the quarter before it, and the second eighth sits 7 dB higher. The pair is heard as one note.
- **Fix (no new rows: all are loaded already).** In `build/score_config.py`, extend the c01 `_TUTTI_STAC` spans (and the c02 Violins II Spiccato swap that reads them) with `(981.0, 1005.0)` for Violins I "Stac RRx14", Violins II (Spiccato RRx9 via the c02 rewrite), and Violas and celli "Staccatissimo RRx16". Keep their `ROW_TRIM_DB` values.
  - The coda heads at 999-1004 that are strokes (`DOWNBOW_STROKE_AT` 999, 1005) stay as they are.
  - Pass: master dips of 3.5 dB or more at every coda pair, and Violins II / violas 4 dB or more on the stems.

### 4. Woodwind legato joins still dig 5-9 dB holes where the line is exposed. auto_fills has never run in this series (`early_fills.json` is empty).

- **Measured** (hole = lower neighbouring body minus the 30 ms minimum from the moved onset to +0.08 s, on the stem):
  - Clarinet 1: 578 8.1, 638 8.0, 634 7.3, 590 6.2, 850 7.7, 857 5.4 dB. This is no better than c02 (critic A c03: 578 8.9, 634 8.8, 638 7.8, 850 11.6, 857 8.7) despite the pitch trims and the Leg Slur Rep row. The trio tune itself (456-504) is now fine: median 1.0 dB, one join over 5 (466, 5.6).
  - Clarinet 2: 848 9.0, 142 8.4, 859 7.9, 857 6.6, 376 5.8.
  - Bassoon 1: median 2.9 dB, 18 joins of 5 dB or more (353 8.7, 953 8.5, 729 8.3, 140 6.9, 321 6.3, 921 6.2; the tenor countermelody and the retransition).
  - Flute 1: 152 8.3, 659 8.1, 664 8.0, 101 7.7, 1054 7.0 (the "col Vl. solo" join of bar 352).
- **Fix.** Add "Clarinet 2" and "Bassoon 1" to `TRACKS` and `RAISE_TRACKS` in `tools/auto_fills.py`. Run `tools/auto_fills.py 3 build/parts.json` (dry run), check the list against the joins above, then run it with `--write`. Rerun on every later render, with the overshoot rule (kit section 6).
  - Pass: no exposed woodwind join of 5 dB or more, and no fill rising more than 2 dB over the louder body.

### 5. The celli's printed bow changes on the held pp E3 (bars 358-359) dip 7-10 dB on the stem, in the exposed Meno mosso under Hn 1's motto tail.

- **Where.** Violoncellos qn 1074 and 1077: same-pitch Sus MAX pieces from the printed bow changes (`STR_REP_NEW_BOW` re-bow points). 1080 already has a fitted fill (`rebow_fills.json`).
- **Measured** (50 ms envelope, relative to the level over -0.45..-0.1 s):
  - 1074: -1.8 at the onset, -5.5 at +0.15 s, -9.2 at +0.2 s, -3.7 at +0.3 s, -2.1 at +0.4 s.
  - 1077: +3.5 at the onset, -2.0 at +0.2 s, -5.8 at +0.25 s, back to +1.0 at +0.4 s.
  - Master dips at these times: 3.0 and 3.5 dB. 1080 with its fill: stem 3.0 dB.
  - A bow change at pp should dip about 2-4 dB (kit section 6). fit_rebows skipped these pieces as shorter than MIN_PIECE_S (c03 CHANGES).
- **Fix.** Hand entries in `build/rebow_fills.json` under "Violoncellos", in the format of the 1080 entry:
  - 1074: 0 dB at -0.04 s, +3 dB at +0.1, +7 dB from +0.17 to +0.24, +3 dB at +0.32, 0 at +0.45.
  - 1077: 0 at +0.12, +4 dB from +0.2 to +0.28, 0 at +0.4.
  - Convert the seconds to the file's qn offsets at quarter 228.
  - Pass: stem dips of 4 dB or less at both.

## Also measured (not ranked)

- **Horn legato** (manual p.105-106) is in good shape (measured). Hn 1 call joins: 9 6.2 dB hole, 14 none, crossovers +0.09..+0.10 s. Motto tail 1071 / 1074 / 1077: holes -1.4 / 3.6 / -0.8 dB, crossovers +0.04..+0.09 s. Hn 3's a2 countermelody (105-120, 305-320): 39 joins, holes -6..+5.3 dB, crossovers within -0.16..+0.13 s.
- **Hn 1's last G sharp** (qn 1101-1128, one Sus MAX note of about 11 s): no loop period. Detrended level 4.3 dB peak-to-peak; the level and centroid autocorrelation peaks at 5.44 s at 0.33, -0.09 at 3.95 s. The centroid dips from about 860 to 650 Hz over about 4.5-6 s, as the CC1 decrescendo crosses a layer. Leave it (measured).
- **Theme A pairs** are fine (measured): Violins I first-to-second eighth median 8.2 dB (36-84) and 7.5 (756-804); master 4.4 and 5.1.
- **The trio horn drone** (Hn 3-4, 456-504) is tied in four-bar groups of about 3 s with a beat's rest between (read): no loop or S1 issue.

## Do not touch

The Marc LITE heads with their level steps; the clarinets' whole-piece Leg Slur Rep `REP_ROW` (trio tune joins now median 1.0 dB); the woodwind "Stac DblTng RRx9" rows and their leads; `_TUTTI_STAC` in 105-120 / 305-320 (extend it, do not replace it); the horn legato velocities and leads (crossovers +0.01..+0.13 s); `GENTLE_ACCENT` and the absence of brass accent rows; `PORT_TARGETS` 640, the re-bow fills, the CC70 / CC15 lanes; plus c03's items (ir_setup, release caps, `STR_REP_NEW_BOW`).
