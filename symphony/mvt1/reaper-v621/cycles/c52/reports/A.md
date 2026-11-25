# Cycle 52, critic A: articulation and phrasing

Under review: the c51 render (`cycles/c51/render`: dry stems 01-40, the master; returns 91-94 used only to split the master,
not tabled per track; `render_first/` for the brass stems before the stem fix) and its data (`cycles/c51/rendered_build/`,
`rendered_build_pass2/`, `build/`). The Opus states each render loaded were decoded from the timestamped project saves
(`Backups/mvt1-v621-mockup-2026-11-08_173805.rpp-bak`: the restart save the c50 render loaded;
`...-2026-11-09_084809` and `_090017`: the c51 restart and pre-render saves; the current `mvt1-v621-mockup.rpp` and
`mvt1-v621-mockup-pass2.rpp`, read only) and compared with the written states in `jobs/NN_*.b64`. Scratch scripts were in
`/private/tmp/claude-501/mockup-loop/mvt1-c52-A/` and are deleted; the methods are given in each finding.

## Manual notes

Third round: pages chosen for this lens's open problems (the legato state, the basses' round robins, the sf, the harp cap,
the repeated violas).

| Source (PDF page) | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| 2021 p.145 (2025 p.92) | Opus remembers, per note, which round-robin sample plays next, so the cycle carries on from wherever it stopped; a reset forces a known order, and the manual suggests resets "at important positions throughout the sequence". The reset listens to the Preferences CC (16 here). | Basses' Sus MAX eighth pedals 104-124, 520-536, 556-568, 664-676 | Partly. One reset in the pre-roll only; the same C2 strokes play in three different phases (finding 3). |
| 2021 p.91 | Sustain bow direction is a two-sample round robin alternating up and down bow. | Same pedals | The alternation is audible as 1.2-3.7 dB strong/weak strokes, on the off-beats in four segments. |
| 2021 p.91-92 | Marcato Sustain plays a marcato sample over the looped sustain, giving "extra power at the start of the note". | The string sf at qn 160 and 78 | Not used for sf. Violins I, Violins II and celli already load "Sus Marc LITE" (no memory cost). |
| 2021 p.144, p.105, p.143 | True legato: velocity sets transition time (50-60 slow, 110-127 fast), not loudness; legato is monophonic by default, CC22 64-127 keeps it mono; joins need no gap and at most an octave. | Every legato track; the stale-state finding | Joins: yes (0 chords on legato rows, 0 same-pitch overlaps, overlap 19-21 ms). CC22 is never sent in Movement I (the scherzo now pins it to 127 in the pre-roll). |
| 2021 p.101 | Brass Sustain Accent: velocity sets the attack; Sustain Marcato: velocity sets a low-pass on the marcato attack. | Brass sf at 160 | Plain Sus under GENTLE_ACCENT; not changed here. |
| 2021 p.98 | Violas and basses have a "Repetitions" patch: one note re-bowed about twelve times in a little over a second, tempo-synced, CC11 three layers. | S1 viola runs | Not suitable: the runs are eighths at 126 bpm (4.2 per second). Inferred. |
| 2021 p.69 | Harp Sustain RR: pluck and thumb round robin at velocity 1-123, a nail pick at 124-127. | Harp | Yes: harp maximum velocity 112, no note at 124 or above. |

MANUAL-GAPS items still open for this lens: #5 (expressive wind rows), #7 (half-section divisi), #9 (horn portato rows),
#12 (Felt Cresc), #13 (bass trombone low notes). All rank below the six findings.

## Coordinator's items, short answers

| Item | Answer | Finding |
|---|---|---|
| Scherzo legato-state check | Four main-project instances rendered c51 from a stale state: Horn 1, Horn 3, Trumpet 1, Trumpet 2. Their legato joins came 18-45 ms earlier (median) and 2-6 dB louder than their own other notes. Strings, other brass and winds did not move. Rebuild those four fully, plus Bassoon 1 stac in pass 2. Revert the c51 corrections that were fitted on the stale audio. | 1 |
| Finale 2 (sfp / fp / sf) | No sfp in v621. One fp (basses, qn 128) works. Two sf marks: bar 20 (Violins I/II, qn 78) and the bar-41 tutti (qn 160, 20 tracks). Every led sf note starts on the pre-spike layer, and Violins I, celli and basses peak 0.28-0.57 s late. | 2 |
| Finale 13 (string sf bump) | Needed on Violins I (78, 160), celli and basses (160), with a bloom cut on Violins I 160. | 2 |
| Finale 8 (CC16 reset before ostinato spans) | Adopt for the four basses pedals. The phase flips at pitch changes inside spans. The coda pedal is already downbeat-strong, but upstream resets will change it, so reset it too. | 3 |
| Finale 14 (two players, separate join leads) | Flute 2 lands 58-133 ms behind Flute 1 on 7 of 9 shared joins (bars 70-71, 159-161). Oboe 2 lands 70-149 ms ahead of Oboe 1 on 3 shared notes. Bassoons scatter both ways. Horns and trumpets share too few notes for a per-track rule. | 4 |
| Finale 9 (harp cap 123) | Already met in the data (maximum v112). Add the cap as a guard. | 6 |
| S1 violin and viola blur in the master | Accept, with numbers. No gap, send or row change on these voices can deepen the master dip by more than 0.15-0.8 dB. | 5 |
| Re-bows 44.0 / 180.0 | 180.0: drop it (the celli are 12 dB under the band; the 6.4 dB master dip belongs to other parts). 44.0: a printed down-bow at the f arrival. Accept the 80 ms bow-change dip, but trim the fill that overshoots it by 4.5 dB. | 5 |
| Vc macro | Adopt on Violoncellos only with a map that keeps the dolce vibrato, and check joins on the main render. | 6 |

## Findings, ranked by what a listener would hear

### 1. Horn 1, Horn 3, Trumpet 1 and Trumpet 2 rendered c51 from a stale legato state: the Horn 1 dolce tune is early and too loud (measured)

**Where.** Horn 1 legato joins in bars 43-52 (the "1. dolce" tune, mp), 103-106 (mf) and 147-154 (the recap dolce). Horn 3 in
bar 42 (164-165, under the Horns a2 tune), 104-106 and 160. Trumpet 1 in bars 69-71 (f), 113-114 and 161. Trumpet 2 in bar 114.
In pass 2, Bassoon 1 stac (the current save).

**State evidence** (decoded Opus states against `jobs/NN_*.b64`). Compared groups are the AHDSR attacks of every
group.
- The restart save that the c51 render loaded (08:48, identical at 09:00) holds the legato sustain groups at 20 ms instead of the written values:
  - Horn 1: 16 groups ("1FHs pp..ff", written 325-1076 ms).
  - Horn 3: 16 groups (the same groups and values).
  - Trumpet 1: 24 groups ("1Tps pp..ff", written 267-1076 ms).
  - Trumpet 2: 24 groups.
- Every other main-project instance matched its written attacks exactly.
- The c50 render's restart save (17:38) matched on all 33 tracks.
- The current main project still holds the same four stale instances. The current pass-2 project holds Bassoon 1 stac at 20 ms on 18 groups ("Bss mp..ff", written 438 ms).
- `legato_speed_active` was false (written true) on Violins II, Violas, Double basses, Horn 2, Horn 4 and Bass trombone in the c51 load. Those tracks did not move (below), so that flag alone has no measured effect.

**Render evidence.** Every legato join present in both renders was matched by score onset and pitch pair, with the same lead. pcX was measured with `tools/pcx.py`. Level is the stem over the note, minus the written-envelope change (build_reaper `vol_points`, gains included).

| Track | Joins | pcX c51 minus c50, median | Joins >40 ms earlier | Legato targets / other notes, level change |
|---|---|---|---|---|
| Horn 1 (stale) | 47 | -45 ms (bars 43-52 -46, 103-106 -45, 147-154 -49) | 25 | +9.4 / +4.3 dB |
| Trumpet 1 (stale) | 15 | -45 ms | 8 | +9.5 / +3.5 dB |
| Horn 3 (stale) | 11 | -18 ms (164 -65, 416 -99, 420 -43) | 3 | +6.6 / +3.8 dB |
| Trumpet 2 (stale) | 1 | -45 ms | 1 | +5.2 / +3.0 dB |
| Horn 2, Horn 4, Trombones 1-2, Bass trombone, Horns a2 | 80 | -8..+3 ms | 1 | legato minus other +0.1..+3.3 dB |
| Violins I/II, Violas, Celli, Basses | 765 | 0 ms on every track | — | +0.3..+0.7 dB |
| Winds (rebuilt in c51) | 420 | 0 ms on every track | — | -0.5..-2.1 dB |

- The +3..+4 dB on every brass track's non-legato notes is the c51 brass EQ change (bells halved). state_check does not model EQ, so it reads this change as level.
- So the c51 CHANGES "11 brass state runs +3.1..+4.3 dB" are the EQ change, not sample-state flips. Only Trumpet 1 643 (-86 ms, +5.2 dB) among state_check's flagged notes is the legato state.
- After allowing up to about 3 dB for phrase shapes on unaffected legato notes, the stale excess is about +3..+5 dB on Horn 1 and Trumpet 1. It has the same signature as the earlier Movement I "Solo Horn / Solo Trumpet flips" (c42, c43, c46, c47, c49: 40-65 ms early, 4-15 dB louder, cured by a full rebuild). Those were this mechanism.
- What a listener hears: the most exposed horn solo in the movement plays every slurred note 45 ms ahead and noticeably heavier than its own detached notes. The trumpet line in bars 69-71 does the same.

**The c51 corrections fitted on this audio** (each matches the stale excess in place and size):
- Horn 1 mf soft trim -3.4 dB. kres51 measured +3.4 dB on 7 mf windows, which are the bar 103-106 tune.
- Horn 3 mp -1.7 dB. Its windows include the stale joins 415-422.
- roles.json Horn 3 [163.75, 168.0, -4]. The stale joins 164/165 were +8.1/+9.7 dB against Horn 3's +3.8 elsewhere.
- Cor anglais [584, 608, +1.5]. CA minus Horn 1 at 147-152 moved -4.5 -> -6.6 dB while Horn 1's joins there were stale.

**Fix.**
1. Before building, revert those four values to their c50 settings. Do not write the two roles rows that ONE_TIME.md lists; tell the coordinator why.
2. Fully rebuild Horn 1, Horn 3, Trumpet 1 and Trumpet 2 in the main project, and Bassoon 1 stac in pass 2 (`build_reaper.py build/parts.json jobs "Horn 1" "Horn 3" "Trumpet 1" "Trumpet 2"`, before the restart).
3. Port the scherzo's two build_reaper settings (symphony/scherzo/reaper-v600/tools/build_reaper.py lines 1043-1054 and 1071-1072, 1222-1226):
   - `MIDI_ONLY_REBUILD_LEGATO = True`.
   - `LEGATO_MONO_CC22 = 127`.
   - If rebuilding all 29 legato tracks costs too much lock time, add a state guard instead. After the restart (the save the render will load), decode every Opus block and fully rebuild any instance whose AHDSR attacks differ from its jobs file, then restart again. The non-obvious part of the decode is that the VST3 block holds several base64 segments, so decode it line by line:

   ```python
   b = b"".join(base64.b64decode(l) for l in block_lines)   # one RPP <VST "VST3i: Opus ...> block, inner lines
   js = json.loads(zlib.decompressobj(31).decompress(b[b.find(b"\x1f\x8b\x08"):]))
   att = [p.get("attack") for g in js["zones"][0]["instrument"]["groups"]
          for p in g.get("processors", {}).get("processors", []) if p.get("class") == "AHDSR"]
   # compare with the same list from opus_state.split(open("jobs/NN_*.b64").read())[1]
   ```
4. After the render, re-measure B's rows Horns a2 over loudest other 41-42 (c50 +0.3) and CA minus Horn 1 147-152 (c50 -4.5), and kres for Horn 1 mf / Horn 3 mp. Refit only if they miss.

**Pass.**
- Horn 1, Horn 3 and Trumpet 1 joins within ±15 ms (median) of c50 on unchanged leads.
- Legato-minus-other level within 1.5 dB of Horn 2's.
- 0 attack differences in the decoded pre-render state.

### 2. The sf at bar 41 (and bar 20) plays as a swell in the strings; every led sf note starts on the old layer (measured; fix values inferred)

**Where.** qn 160 (bar 41: f, a tutti sf, decrescendo to mf at 164) on 20 tracks; qn 78 (bar 20) on Violins I and II. The only fp
(basses, qn 128) works: it reaches its peak at +130 ms and is -15 dB by +0.5 s. There is no sfp in v621.

**What parts.json does.**
- The sf spike starts at the mark + 0.02 qn (`base_points` sf branch, `SF_ARRIVAL_AT` {78, 160: "ff"}). A led note's pull reads the level at its score onset, so every led sf note plays its first 35-150 ms on the pre-spike layer:
  - CC11 at the moved note-on 86-90 against a spike of 114 on Violins I, Violas, Oboe 1, Bassoon 2, Trumpet 3, the trombones and the basses (leads 35-120 ms).
  - The celli at 89 (a Leg BC join, lead 150 ms).
  - Violins II at qn 78: CC11 58 (its mp) for 120 ms before the spike.
- Opus's 120 ms CC11 fade then delays the ff layer further.

**What the stems show** (20 ms frames, re the level just before the mark, peak time after the mark):

| Track at 160 | Peak at | Frames at +25 / +75 / +150 / +400 / +900 ms |
|---|---|---|
| Violins I | +565 ms | +4.8 / +7.0 / +8.0 / +11.5 / +9.9 dB |
| Violoncellos (Leg BC join) | about +300 ms | +1.0 / -2.1 / +3.0 / +5.7 / -0.4 |
| Double basses | +280 ms | -0.9 / +0.9 / +2.6 / +1.0 / -3.9 |
| Violas (tremolo) | +75 ms | +5.5 / +9.9 / +6.8 / -4.4 / -6.3 |
| Violins II | +35 ms | +12.0 / +8.4 / +5.1 / +1.6 / -4.5 |
| Oboe 1 | +500 ms | -4.2 / -3.7 / -0.3 / +2.6 / +3.1 |
| Trumpets, trombones, tuba | +170..+240 ms | the sample rise |

At qn 78, Violins I's first 0.1 s sits only +1.2 dB over the f before, and the level wanders +2..+6 dB until +0.5 s.

- At bar 41, the two loudest stems (celli -31.0, Violins I -32.2 dB) both peak 0.3-0.57 s after the mark and stay up, so the strings play "< >" where the score has "sf >".
- The Violins I G6 Sus MAX sample itself rises about 9 dB from +50 to +400 ms. The written envelope already has a +4.6 dB front bump falling by +0.24 s. So this is a bloom, not a missing bump.
- The celli's sf is played as a bow-change legato join from the held A-flat, so it has no attack at all.

**Fix** (`tools/score_to_parts.py`, `build/score_config.py`):
1. Port the finale's `FP_SPIKE_AT_MARK` (mvt3 tools/score_to_parts.py 772-775, 1865-1873) and extend it to sf. In the sf branch, write `(q, spike)` and, in the SF_ARRIVAL_AT branch, `(q, arr_)` instead of `q + 0.02`, so that the pulls read the sf value at the moved note-on. Port `FP_VEL = 96` as the default too. The basses' fp note plays v53, but Sus MAX ignores velocity (DIGEST 2.1), so expect no audible change.
2. String sf shapes with `POST_SHAPES_S` (exists since c42; seconds re the score onset). The finale's item 13 values are the starting point:
   - Violoncellos and Double basses 160.0: `[(-0.13, 0), (-0.12, 5), (0.17, 5), (0.25, 0)]`.
   - Violins I 78.0: `[(-0.07, 0), (-0.06, 3), (0.17, 3), (0.25, 0)]`.
   - Violins I 160.0 also needs the bloom taken out: `[(-0.07, 0), (-0.06, 2), (0.12, 2), (0.30, -3), (0.9, -4), (2.0, -2), (3.0, 0)]`. These are starting values (inferred); fit them to the pass criteria on the render.
   - Leave Violins II and the violas alone; they already peak at +35 / +75 ms.
3. Celli 160: make the sf a fresh stroke instead of a Leg BC join. Use an ART_SPANS row `{"from": 159.9, "to": 160.01, "art": "Sus Marc LITE", "vel": 95}` (the f attack zone 61-102). The row is already loaded on the celli. Because ART_SPANS notes bypass the lead rules (scherzo LEARNINGS c06), add `REATTACK_LEAD_AT` 0.05 s. c48's celli 456 stroke on this row passed with a 0.05 s lead.

**Pass** (string stems at 160 and 78):
- Peak within 0.09 s of the mark.
- First 0.1 s within 2 dB of the peak.
- Level at +0.5 s at least 1.5 dB under the first 0.1 s (the sf falls into the decrescendo).
- 2-5 kHz first 80 ms minus body at or under 0 dB (Dan: weight, not bite; c51 string accents median -10.9 on this measure).
- Master bars 41-42 within +0.5 dB of c51.

### 3. Basses' eighth pedals: the bow-direction round robin puts the strong stroke on the off-beats in four segments (measured; the reset's phase is inferred, so test it)

**Where.** Double basses, f-ff Sus MAX eighths at 104-124, 520-536, 556-568 and 664-676.

**Measured.** Front = 40-300 Hz energy over the first 80 ms after the moved onset, minus the written envelope at the onset.
Strong minus weak stroke, by same-pitch segment:

| Segment | Pitch | Strong minus weak stroke |
|---|---|---|
| 104-107.5 | C2 | downbeats +3.7 dB |
| 108-111.5 | D2 | off-beats +1.5 |
| 122-123.5 | D2 | off-beats +1.4 |
| 520-525.5 | C2 | off-beats +3.6 |
| 526-527.5 | G1 | downbeats +2.5 |
| 528-531.5 | A-flat 1 | off-beats +3.5 |
| 532-535.5 | G1 | downbeats +1.2 |
| 556-559.5 | C-sharp 2 | off-beats +1.3 |
| 564-567.5 | G1 | off-beats +0.9 |
| 664-675.5 (coda) | C2 | downbeats +1.7 |

- In the coda, off-beats are even within 0.7 dB except 664.5 and the last two strokes.
- The same C2 plays in three phases (104 downbeat-strong, 520 off-beat-strong, 664 downbeat-strong). That is p.145's per-note memory: each C2 stroke advances the C2 counter, so the phase depends on how many C2s came before.
- An off-beat-strong bass line under the recap theme (bars 131-134, 520-536) reads as a syncopated accent in the loudest stem of the 40-200 Hz band.
- The coda's "+3.4 dB brighter downbeats" is the strong stroke landing on the beat. Keep it; it is the stroke a player would put there.

**Fix** (finale item 8).
1. Port `RR_RESET_AT` and its cc16 lane from mvt3 tools/score_to_parts.py (lines 443-447 and 5751-5757, plus the parts.json `cc16` key and the build_reaper lane writer).
2. Set `RR_RESET_AT = {"Double basses": [104.0, 108.0, 112.0, 116.0, 120.0, 122.0, 520.0, 526.0, 528.0, 532.0, 556.0, 560.0, 562.0, 564.0, 664.0]}`, one reset at each same-pitch segment start (127, 0.02 qn before the moved onset).
   - The coda is included because the upstream resets change its C2 count, so its present phase would not survive.
3. After the render, measure the same table:
   - If every segment comes out downbeat-strong, refit the c48 coda shapes down.
   - If every segment comes out off-beat-strong (the reset's first sample is the weak stroke), add `METRIC_BOWED_DB_SPANS` (port from mvt3 with the reset) with `{"down": 1.5, "mid": 1.0, "beat": 0.0, "off": -2.5}` on all four spans, as the finale did (+3.0..+3.8 dB in every span).

**Pass.** In every segment, downbeat minus off-beat front at least +1 dB after the table; adjacent off-beats within 1.5 dB; master
520-536 repeat dip at least the c51 8.3 dB.

### 4. Flute 2 trails Flute 1 on their shared slurred line; Oboe 2 leads Oboe 1 (measured)

**Where.** Flutes 1 and 2 in unison or octaves, bars 69-71 and 159-161.

**Measured.** pcX of every note both tracks play at the same score onset (unison or octave), c51 stems.
- **Flute 2 minus Flute 1 on shared Leg Slur joins:** 276 +58, 280 +85, 633 +62, 636 +118, 639.5 +74, 640 +63, 642 +133, 643 +69 ms. 634 is -36 ms.
  - Flute 1 itself lands early at 633 / 639.5 / 640 / 643 (-94 / -70 / -28 / -35 ms).
  - Flute 2 lands at -32..+181 ms.
- **Flute 2's leads come from `LEG_LEAD_S["Flute 2"] = 0.05`**; Flute 1 has per-onset `leg_leads`.
  - In 271-282 Flute 2 already leads 0.105 qn against Flute 1's 0.063 qn and still lands 58-85 ms later.
  - FL2 KS Master is another player, which is the finale's finding.
- **Flute 2's detached notes at 456-472 land 30-53 ms ahead of Flute 1** (entry lead 50 ms against 35 ms).
- **Other pairs:**
  - Oboe 2 lands 70-149 ms ahead of Oboe 1 on 3 of 5 shared notes (122, 556, 628; Oboe 2 leads 120-195 ms against 40-50).
  - The bassoons (25 shared notes) scatter both ways: median +20 ms, 14 of 25 over 40 ms. That calls for a per-note fix, not a per-track one.
  - Horn 2 / Horn 4: median -5 ms on 15 notes. Horn 3 / Horn 4 and Trumpets 1 / 2: 9 and 3 notes. No per-track change.

**Fix** (finale item 14, `build/score_config.py`):
1. `LEG_LEAD_S["Flute 2"]` 0.05 -> 0.11 s (joins only).
2. Flute 2's entry / Sus lead at 456-472 set to Flute 1's 0.035 s.
3. Flute 1 `leg_leads` 633.0 -0.05 -> -0.08, 639.5 and 640.0 -0.03, 643.0 0.05 -> 0.02.
4. Oboe 2's entry leads at 122, 556 and 628 set to Oboe 1's.
5. If Movement I has sostenuto joins on the flutes, port the finale's per-track `SOST_JOIN_LEAD_S` dict as well ({"Flute 1": 0.085, "Flute 2": 0.16, "default": 0.12}).

**Pass.** Flute 2 minus Flute 1 on shared joins: median within ±30 ms, at most 2 of 9 over 40 ms; both flutes' joins within ±40 ms of the beat.

### 5. Close two open items: the violas' and violins' master S1 dips and the two re-bows (measured)

**S1 in the master: accept.** For every same-pitch repeat in the c51 runs, I measured each component in the note's own harmonic band (pcx exclusion bands): the section's dry stem, the R Strings return, all returns, and the other dry stems (master minus stem minus returns).

| Run | Gap | Own-band dip, stem / master | Own body re master | At the master's dip: all returns / other dry stems | Most the master dip could gain if the section went silent |
|---|---|---|---|---|---|
| Violas 86-100 | 80 ms | 7.9 / 1.6 dB | -7.8 dB | -10.5 / -1.0 dB | 0.8 dB |
| Violas 440-468 | 77 ms | 5.2 / 1.9 dB | -11.9 dB | -12.6 / -0.4 dB | 0.3 dB |
| Violas 552-568 | 80 ms | 8.3 / 0.4 dB | -14.7 dB | -10.2 / -0.4 dB | 0.15 dB |
| Violins II 86-100 | 80 ms | 7.7 / 3.0 dB | -11.5 dB | -9.9 / +0.1 dB | 0.3 dB |
| Violins II 536-548 | 80 ms | 7.0 / 1.6 dB | -11.5 dB | -7.9 / -1.3 dB | 0.3 dB |

- The repeated notes are inner voices shared by four to six other parts. At the gaps, Violins II, the bassoons, Horn 3, the clarinets, Oboe 1 and the flutes each hold -5..-10 dB of that band.
- Removing every return there would deepen the master dip by at most 0.2-0.8 dB.
- The re-attacks also carry almost no transient: the 2-5 kHz rise in the first 50 ms is -0.9..+1.8 dB on the stems and -1.9..+0.3 dB in the master.
- So shorter notes, lower sends and a different row on these voices cannot reach the 3.5 dB master target. The target does not fit inner voices.

Fix:
- Keep the REP_SPLIT gaps (stem dips 5-8 dB).
- Drop the master-dip criterion for these five runs. Keep it for exposed lines and the basses (master 520-536 8.3 dB).
- If Dan still hears blur there, the lever is balance (the repeated voice against its doublers), which is critic B's lens.

**Re-bow 180.0 (celli, bar 46): drop it from the list.** The celli sit 12.1 dB under the master in that band. With that share, a perfect re-bow can change the master dip by at most 0.3 dB, so the 6.4 dB dip belongs to other parts.

**Re-bow 44.0 (Violins I, bar 12): accept the dip, trim the fill.**
- The score prints a down-bow and f on the tied A-flat at 44, so the re-bow is a real bow change.
- Own-band frames re the note before: -4.2 dB at 0 ms, -6.1 at +80 ms, back to 0 at +120 ms, then +4.6 / +3.9 / +3.4 dB at +160 / +200 / +250 ms. The master is the same shape.
- The 80 ms dip is a plausible section bow change at an f arrival. The overshoot is the `rebow_fills.json` 44.0 fill (+11.6 dB at 44.07-44.14 qn) landing after the hole.
- Fix: in that list, start the fill 0.04 s earlier and lower its peak by 4 dB.
- Pass: no frame over +2 dB in +0.1..+0.4 s, dip no deeper than c51's 6.1 dB.

### 6. Small defaults to port and one accent that gained bite (measured; macro map inferred)

- **Vc macro: adopt on Violoncellos with a map, not as identity.**
  - The c51 test passed the plan's "no worse" rule: AM p95-p5 4.7 -> 4.4 dB, level -0.1 dB median, centroid -1 Hz. One note was at -2.3 dB, a level the envelope can take.
  - It gained nothing measurable, and the dolce tune's vibrato share fell 0.39 -> 0.34. The identity map takes the celli's CC1 from 95-105 to 72-84 there, and Molto Vib from about 1.0 to 0.26-0.5 (patch table in c51 report A).
  - Use `CC1_FROM_CC11 = {"Violoncellos": [(0, 0), (58, 58), (72, 90), (127, 127)]}`. At mf this gives CC1 90, Molto Vib 0.72.
  - Joins were never measured: the test stem was deleted. Measure them on the main render with the 18-note vibrato check, and drop the map if any join dip grows by 2 dB or more.
- **Harp:** add `HARP_VEL_MAX = 123` (mvt3 tools/score_to_parts.py, next to `FP_SPIKE_S`). No note changes today (maximum v112), but a later velocity table cannot reach the nail pick.
- **CC22:** pin mono in the pre-roll (finding 1).
- **Clarinet 1 qn 414 (bar 104, accented G5): bite from the phrase shape.**
  - Its 2-5 kHz first-80-ms minus body went -7.9 -> +4.4 dB. It is the only one of 581 accents to cross 0 dB; median change 0.0.
  - The phrase shape raised CC1 86 -> 90 and CC11 88 -> 92 on this CC1-layer track.
  - Fix: exclude accent onsets ±0.25 qn from PHRASE_SHAPE's CC1 offset on `CC1_DYN_TRACKS`, or a NOTE-level CC1 cap of 86 on Clarinet 1 414.

## EW-TEMPLATE-PLAN sections this lens touches that are not yet applied (c51 render)

- **Section 5:**
  - Legato overlap is 19-21 ms (median, all families) against 45-80 / 33-58 ms. Low priority; c51 report A inferred no gain.
  - Legato velocity does not follow the dynamic: strings v124 on 718 of 767 joins (v112 or higher on 736).
  - The CC1 macro is a test only (finding 6).
- **Section 6:** two tracks per string section, not applied.
- **Section 7:** per-note lean-off inside slurs, not applied (by choice).
- **Section 8:** a tutti entry spread as a rule is not applied. The bar-41 sf already spreads its perceived peaks from +35 to +565 ms, which is too much, not too little (finding 2).
- **Section 10:** beat-position short velocity outside the listed spans, not applied.

Met: string short rows parked; repeat gaps 77-80 ms; spiccato 50 %, celli strokes 55 %; doublings share one curve.

**Do not touch:**
- GENTLE_ACCENT and the accent fits. 2-5 kHz first 80 ms minus body, c50 -> c51 medians: strings -11.1 -> -10.9, winds -11.7 -> -11.8, brass -18.6 -> -18.1 dB.
- Keyswitch placement: 0 clashes, 0 within 0.004 qn of a note.
- No chords on legato rows; no same-pitch overlaps.
- The string and wind legato joins: c50 -> c51 median 0 ms on all 1185 matched joins.
- REP_SPLIT gaps (stem dips 5-8 dB, basses master 520-536 8.3 dB).
- The fp at 128.
- AUTO_REBOW: no note longer than 7 s on one sample.
- The celli 55 % tremolo strokes.
- Harp velocities.
- The coda pedal's present downbeat lead, until RR_RESET_AT is measured.
