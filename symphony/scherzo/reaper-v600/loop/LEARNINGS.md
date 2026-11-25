# Movement III (Scherzo) mockup: learnings

Lessons from this series that would help someone mock up a different score with this library and pipeline, especially where the scherzo (a fast 3/4 movement, quarter 264) differs from `mockup-kit/LEARNINGS.md`, Movement I's `symphony/mvt1/reaper-v621/loop/LEARNINGS.md` and Movement II's `symphony/mvt2/reaper-v600/loop/LEARNINGS.md`. One short dated bullet each under a topic heading; actors append. Skip anything specific to this score's bars.

## Pipeline: porting the tools from two forks
- 2026-11-07 (c00): Movement II's tools were copied from Movement I's at its c36 and both evolved after. Movement I's `cycles/c37/before/` snapshot is the fork point (Movement II's port tools equal it except its own edits), so a three-way `git merge-file <mvt2 file> <fork-point file> <mvt1 file>` per tool merged 14 of 16 files cleanly and left one small conflict in two. Find the fork point by diffing one fork's earliest snapshot against the other's per-cycle `before/` folders. A tool constant that one fork set for its own score (Movement II's delivery ratio 2.2 for slow crescendos) comes in with the merge: read every constant the merge changed.

## Score extraction
- 2026-11-07 (c00): on a score whose players share staves, dynamics and texts printed only in a player's part (`\tag #'part`) are real marks for that player (here a crescendo target ff and a p > on the second clarinet, hidden in the score beside the first's). Extracting each player with `\removeWithTag #'part` drops them; `\removeWithTag #'score` keeps them when the 'score tags hold only labels, clefs and rest positions (check that no note is tagged).
- 2026-11-07 (c00): "sul A" and similar spans written as TextSpanner (`\startTextSpan` with the text in a tweak) are not text-script events, so the event list had no trace of them; listening to `text-span-event` in the extraction engraver logs their start and stop.
- 2026-11-07 (c00): harp harmonics written as chords inside `\transposition c''` already sound an octave up in the MIDI; Movement II's "harm" rule (keep only the top note at each harmonic onset, because it wrote written + sounding pitch) would have dropped the lower chord notes (`HARM_ALL_PITCHES`).
- 2026-11-07 (c00): "sfp" was not in the dynamic table and would have been an unread dynamic (a tutti sf attack falling to p under a crescendo); it is now read as an fp whose attack reaches the sf level.

## Timing
- 2026-11-07 (c00): lead, gap and fill rules in seconds were fitted at quarter 126 (Movement I) and 52-60 (Movement II). At quarter 264 one eighth lasts 0.114 s, so a 0.17 s string legato lead or a 0.12 s entry lead is longer than an eighth, and qn-based shapes (FP_SPIKE 0.12 / 0.25 qn) shrink to 27 / 57 ms. Measured in the c00 parts.json with Movement I's settings: Violins I leads median 0.045 s, max 0.22 s, 111 of 513 notes moved more than 0.1 s early (celli 167 of 436); the shortest played notes last 0.052 s. Re-check every seconds-based rule against note lengths on the first render of a fast movement; FP_SPIKE was set in qn to Movement I's seconds (0.25 / 0.5 qn).

## Articulation (c01)
- 2026-11-07 (c01): at quarter 264 a theme-head accent after staccato eighths, moved from Leg Slur MAX's first-note layer to a fresh Sus MAX stroke (DOWNBOW_STROKE_AT, REBOW_VEL_BY_CC velocity 52 at p, 0.12 s lead), still sat 13-15 dB under the staccato before it in its first 150 ms: at p the Sus MAX stroke is as slow as the legato first note. A short note at a fast tempo needs a faster-speaking sample or a higher stroke velocity, not only a row change.
- 2026-11-07 (c01): making one note of an accented hemiola a stroke turns the following accented notes into strokes through STR_ACC_AFTER_SUS at their LilyPond velocity (127, no lead), and a same-pitch note after the stroke falls back to a Leg Slur re-attack; list the whole run.
- 2026-11-07 (c01): woodwind "Stac DblTng RRx9" with one velocity table for all winds came out +4.9 dB (Oboe 1) to -4.5 dB (cor anglais) against the Sus MAX slices it replaced; repeat dips deepened by 0.8-2.3 dB. Set the row's velocity table per track.
- 2026-11-07 (c01): Hollywood Strings staccatissimo recordings live under different row names per section (1st Violins "Stac RRx14", 2nd Violins "Stac Slur RRx6", violas / celli "Staccatissimo RRx16", all StacSs pp/mp/f/ff); on ff tutti repeated eighths at quarter 264 they deepened the master's pair dips only by about 0-2 dB and played the 2nd Violins 2-6 dB louder than the Stac row at the same velocity.

## Hall (c01, Dan S4)
- 2026-11-07 (c01): halving the shared Opus hall return (fx_volume 0.19 -> 0.095, sends unchanged) plus a 160 Hz hall input low cut took the master's drop 0.3 s after tutti cut-offs from 10.3-11.7 to 13.9-16.2 dB, but left the late decay slope unchanged (T60 3.5-3.7 s from -20..-40 dB): fx volume sets the tail level, not its length. The soft bar after a ff lost 6-9 dB of low-instrument hall tail.

## Levels (c01)
- 2026-11-07 (c01): per-pitch trims of simultaneous notes add in the track envelope: a div. octave whose two pitches both carry -5/-6 dB trims would drop 11 dB; trim octaves on one pitch only.
- 2026-11-07 (c01): re-bow fills fitted by fit_rebows.py on a fast movement's held ppp notes took 1st Violins re-bow dips from -7.5..-10.4 to -1.1..-2.3 dB on the next render (12 re-bows' worth of data unchanged except the hall); skip a re-bow just after a printed decrescendo's arrival (fit -6 dB) and cap holds under a final fermata.

## Memory (c01)
- 2026-11-07 (c01): 13 more articulation rows (8 woodwind staccato rows, 4 string staccatissimo rows, Leg Port MAX) raised the 31-instance project from 45 to 49 GB settled (16 GB compressed); the render passed the attack probe.

## Memory (c02)
- 2026-11-07 (c02): a row's memory cost follows its sample-region count in the `.oib` (layerMatrix row index of every region), not how many notes it plays: KS Master legato rows hold 10-27 thousand regions (1st Violins "StacSl Leg BC + Slur + Port MAX" 54 thousand, Leg Port MAX 22 thousand), short rows 2-8 thousand. 92 thousand added regions cost about 4 GB settled; moving 124 thousand regions of rarely played rows onto rows already loaded (`ROW_REMAP`) took 31 instances from 49 to 45 GB. Count regions per used row before adding one, and look first for legato rows that only play a slur's first note (brass heads with nothing joined).

## Articulation (c02)
- 2026-11-07 (c02): Hollywood Strings "Sus Marc LITE" on p theme-head accents (a 0.45 s half note after staccato eighths at quarter 264) sat +4..+15 dB over the staccato before it at v70-86, against -9..-15 dB for a Sus MAX stroke at v52; an exact level step per note from the moved onset (-2.4..-12 dB) brought every one to +2.0..+2.6 dB. Its 2-5 kHz front then stands +2..+7 dB over the body (Sus MAX -11..-13): a level step does not change that.
- 2026-11-07 (c02): the woodwind "Stac DblTng RRx9" rows barely respond to velocity in level: 12 velocity steps down (Oboe 1) and 10 up (cor anglais) moved the accent-to-staccato relation by 0.3-0.5 dB. Balance them with level, not velocity.
- 2026-11-07 (c02): the 2nd Violins "Spiccato RRx9" did not separate ff tutti repeated eighths at quarter 264 any better than the StacSs row (stem dips 1.3-1.6 dB on most pairs).

## Envelope (c02)
- 2026-11-07 (c02): parts.json `vol_db` is a step lane (build_reaper `step_at`), not a linear one: when reading it outside the pipeline, interpolate by step, or a held level reads as a long ramp.
- 2026-11-07 (c02): per-note envelope bumps written once per note double on a chord (a 2-note timpani stroke got +12 dB for +6): apply attack bumps once per onset, as the pitch trims are.

## Pipeline (c03)
- 2026-11-08 (c03): `ROW_REMAP` renames a note's row before the other rules run, so every rule keyed on the old row name stops applying (remapping the clarinets' "Leg Slur" to "Leg Slur Rep" dropped their entry leads and shortened notes before legato notes). To swap a row and keep the rules, use a `REP_ROW` span (keyswitch only); a whole-piece span also unloads the replaced rows.
- 2026-11-08 (c03): build_reaper's tail hold keeps a track's envelope at its last note's level through every rest, so a `LEVEL_SHAPES` cut placed after a note's end (e.g. to damp a ringing timpani stroke in a G.P.) has no effect. A drum's own ring has to be stopped before the hall (CC7 / a short row), which also keeps the hall tail.

## Hall and releases (c03, Movement I c44 values)
- 2026-11-08 (c03): `ir_setup` (envelopeMode 2, endPos 0.5, decayLength 0.5) took the scherzo's orchestral late decay at the G.P. from T60 1.76 to 1.12 s (all stems but the timpani) and the master's -5..-25 dB slope from 2.46 to 1.31 s. The late slope of the master stayed near 3 s because a felt timpani Lng stroke rings about 15 dB/s on its own: measure the hall on the stem sum without the drum, or the drum's ring is read as the hall (c01's 3.5-3.7 s was mostly the drum).
- 2026-11-08 (c03): release caps 150 ms (mf-ff) / 350 ms (pp/p) on the strings: no phrase ending fell more than 5 dB in its first 0.05 s; at +0.15 s Violins II 4.0 -> 7.6 dB and basses 4.1 -> 9.1 dB. The celli fell 2-4 dB more over whole passages than their new roles alone predicted: re-measure balance after a release change.
- 2026-11-08 (c03): the "Timpani Flt Sht" row on a printed staccato stroke shortens only that stroke; earlier long strokes still ring through a following rest.

## Repeated notes (c03)
- 2026-11-08 (c03): STR_REP_NEW_BOW at quarter 264: loud strokes 0.9 -> 6.7 dB stem dip, unslurred Sus repeats ("sus_min_s") 2.9 -> 7.5 dB, soft re-bows 3.7 -> 4.2 dB, but slurred-tenuto (portato) repeats only -0.5 -> 1.5 dB: Movement I's 0.05 s portato gap is a smaller share of a note here and the stems barely dip; the scherzo needs a longer portato gap or fall.
- 2026-11-08 (c03): the clarinet "Leg Slur Rep" row (whole-piece REP_ROW, REP_ROW_GAP_S 0.06-0.15 s) separated slurred repeated quarters at f by 3.6 dB median on the stem (0.0 merged).

## Timpani and the hall (c04)
- 2026-11-08 (c04): a CC7 fall on the felt timpani (127 -> 1 over 0.16 s, `TIMP_DAMP_AT`), placed after the last stroke has spoken, damps every earlier Lng stroke still ringing before the Opus hall. At +0.3 s after the stroke, the stem fell from -43.8 to -71.0 dB and the master from -43.6 to -57.0. The orchestra's hall tail was untouched, because CC7 acts pre-hall.

## Delivery (c04)
- 2026-11-08 (c04): when the climax is boxed in by the limiter, `RIDE_TRIMS` (delivery ride only) on the earlier ff arrivals is the cheapest way to restore the margin. -2 dB on two four-bar arrivals moved the delivered summit margin from 1.3 to 3.4 dB, and the summit itself lost only 0.2 dB after loudness normalisation.

## Articulation (c04)
- 2026-11-08 (c04): the 1TP "StacSs DblTng RRx9" row puts a staccato trumpet quarter's peak on the beat (+0.0..+0.02 s against +0.06..+0.1 s for a cut Sus Non Vib MAX slice), and the second of two repeated eighths at quarter 264 gets its own attack. At low velocity (v50) it plays about 6 dB louder than the Sus slice it replaced; at v96 it plays at about the same level.
- 2026-11-08 (c04): a horn re-tongue of 0.07 s / 8 CC fall (was 0.1 s / 12 CC) brought soft tenuto repeats to 5-6 dB (were 7-11) and the other horn of the pair to 3.7 dB. Repeats at mp from the volume envelope stayed 8-11 dB: the dip there is the sample's own decay as well as the gap.

## Measurement (c04)
- 2026-11-08 (c04): the attack probe's pcx legato spread can flip by 20-25 ms between renders with identical data: violas 92 -> 116 ms, same leads, joins 50-200 ms earlier. Check a flagged section's parts.json against the previous render before you change anything for it.
- 2026-11-08 (c04): a section with no printed staccato in a span has not loaded that section's staccato row, even when the other sections' rows for the same span are loaded. Count the regions per used row (cycles/c02/actor_scripts/rowcost.py) after every ART_SPANS extension.

## Hall (c05)
- 2026-11-08 (c05): the Opus IR envelope at endPos / decayLength 0.7, against 0.5, with fx_volume 0.095, a 160 Hz low cut and 150 / 350 ms string release caps, changed a fast movement's master drop after a tutti cut-off by +0.3 / -2.0 / -2.6 dB at +0.3 / +0.6 / +1.0 s (22.2 / 34.8 / 47.5 dB). The late slope moved from T60 1.25 to 1.47 s (-12..-40 dB). The first 0.3 s, which is the capped releases plus the early hall, did not move. A short cut-off into silence still falls 35 dB in 0.6 s. Only the late tail responds to the envelope length.

## Levels (c05)
- 2026-11-08 (c05): `ROW_TRIM_DB`'s string branch trims a row only near a Leg-row note, so an `ART_SPANS` row swap over all-staccato bars plays the new row untrimmed. The 2nd Violins "Spiccato RRx9" came out 7-12 dB over the previous render. Check `row_trimmed` in parts.json after every staccato-row span.
- 2026-11-08 (c05): `fit_accents.py` predicts against the new build, roles included. A hand-set role cut on an accent plus the fitted swell (which it may set to 0, removing the gentle swell) counts the cut twice: the flute's accented top notes landed 4-5 dB under target. Fit after setting roles, or set roles to the residual only.

## Timing (c05)
- 2026-11-08 (c05): `REATTACK_LEAD_AT` ends the previous note 0.02 qn before the moved onset. On a re-tongued wind repeat that replaces the re-tongue gap (35 ms -> 5 ms). Use `RETONGUE_LEAD_S` (per track) for repeats instead, which keeps the gap.

## EastWest template mix (c06)
- 2026-11-08: the template's family EQs take K-weighted loudness off every track (c05 stems through the EQ, ffmpeg ebur128): brass 6.1-9.6 dB, woodwinds 2.0-4.8 (bass clarinet 2.0), harp 6.3-7.1, strings 1.0-2.3, basses with Duc's 230 Hz cut 4.6, timpani 1.7. Give each track's gain that loudness back if the existing balance is to survive; the EQ then changes colour, not balance.
- 2026-11-08: the template's mic levels (woodwinds Close 1.0 as the main mic, Main 3-21 dB under; harp Mid added) left the flutes +3.3/+3.5, Clarinet 2 +2.7, bassoons +1.5/+2.1 and the harp +2.2 dB louder (K-weighted, whole stem), the low brass 1.1-2.1 dB softer, strings and horns within 1 dB. Measure stems against the previous render and fix the gains once.
- 2026-11-08: Spaces II returns at the template's levels (full IRs, sends -5.6/-8.8/-8.4/-6.4 dB) carry -3.9 dB of the dry stems' energy. G.P. after the fff summit fell 13.9 / 22.4 / 31.5 dB at +0.3 / +0.6 / +1.0 s (Opus hall at fx 0.095 with the 0.7 IR envelope: 22.2 / 34.8 / 47.5). S4's minimum (13 dB at +0.3 s) still holds. In a fast movement the wetter hall fills repeated-note gaps on the master: unchanged staccatissimo pairs lost 1-2.4 dB of master dip (43: 4.0 -> 1.6, 763: 5.2 -> 2.9).
- 2026-11-08: memory: four Spaces II instances, the harp's Mid mic, the timpani's Surround mic and one 775-region row left REAPER's settled footprint at 45 GB (as c05).
- 2026-11-08: with REAPER return tracks and post-fader sends the reverb tail lives on the return, so a fast fall in a track's volume envelope no longer cuts the tail (BRIEF S3's Opus-hall mechanism no longer applies; inferred from the routing, not measured).
- 2026-11-08: delivery: the wetter master needs a gentler ride. On the c06 master 3.0 / 5 gave LRA 12.7 LU, 2.2 / 5.5 gave 14.0 LU, span 19.0 dB, limiter 3.4 dB.

## Pipeline (c06)
- 2026-11-08: a REAPER send volume envelope created by script stays inactive ("ACT 0 -1") if its state chunk is edited before the points are inserted; set ACT 1 after inserting the points (template_mix.py SENDS_LUA).
- 2026-11-08: an ART_SPANS note bypasses the lead, re-tongue and portato rules: Horn 1's Port Lng notes came out at their score onsets, and the violas' pair first notes on Sus MAX took the portato gap and lead from the second notes (16 ms re-attack on the beat). Give span notes a REATTACK_LEAD_AT, or use level trims instead of a span.
- 2026-11-08: an fp / sfp entry led early held the curve's pre-spike level (the spike starts 0.02 qn after the mark): the bar-301 winds started at p and swelled 35-60 ms late. FP_SPIKE_FROM_ONSET reads the spike for the pull; the pull's end on the mark itself must read it too, or CC11 (and the clarinets' CC1) notches to p for 4.5 ms.

## Hall and returns (c07)
- 2026-11-08 (c07): REAPER return reverbs can be simulated on a render's stems. The master is the dry stems plus the return stems, and each return is a linear system from its send input (sum of dry stems x send gains, post-fader) to its stem. Estimate the 2 x 2 (true-stereo) transfer per return with averaged cross-spectra over the whole piece. Use rectangular 10.9 s windows (2^19 at 48 kHz), quarter hop, and divide the IR by the lag weight (1 - lag/N). Hann windows under-estimated the late tail. The fit reproduced the return stems to -19..-24 dB residual and the G.P. decay within 0.1-1.4 dB. The model is then exact for fader and EQ changes on the returns and near-exact for per-track send changes. Use the original stems from before any stem fix as the inputs.
- 2026-11-08 (c07): on the EW template returns (Spaces II, 3.3-3.4 s IRs) the drop 0.3 s after a cut-off follows the return level. The late tail follows the IR envelope. Register sends (low brass, bassoons and basses off) changed neither by more than 0.6 dB in a fast movement where the strings carry most of the hall. Faders -6 dB, a 180 Hz return high-pass, the IR envelope 0.5 / 0.5 and the low sends off measured: G.P. +0.3 s 12.9 -> 20.9 dB, t20 0.65 -> 0.27 s, RT60 2.46 -> 1.38 s, returns at -13.4 dB of the dry energy (template level: -4.8).
- 2026-11-08 (c07): a 2.3 kHz low-pass on the returns moved the simulated cut-off drops by 0.0-0.3 dB. It is a colour choice, not a wetness fix.
- 2026-11-08 (c07): drying the returns and raising the string Close mics made the master brighter (6-20 kHz share -27.2 -> -24.8 dB, 2-5 kHz -10.4 -> -8.7). With the template's family shelves the dark returns had been masking the top end, so re-check brightness after any wetness cut.
- 2026-11-08 (c07): template_mix sends: a track with an empty "sends" list gets no SENDS_LUA, so its old REAPER send stays. Turn a send off with a level of -150 dB instead.

## Width (c07)
- 2026-11-08 (c07): the template's full-width Main pairs left the scherzo master at correlation 0.17 below 250 Hz and side/mid -2.4 dB, the same anti-phase Movement I found. Main at the seat ±0.8 plus side-only 200 Hz -6 dB shelves (strings, brass, timpani, harp) gave 0.68 / 0.57 (250 Hz-5 kHz) / -5.6 dB.

## Round robins (c07)
- 2026-11-08 (c07): Opus's round-robin reset CC (16 here, from its preferences) also works inside the music. Sent before each head of a printed three-bar group, it made the celli pizz. repeat one three-sample pattern per group (stem peaks -49 / -48 / -41 dB per group, before a four-note cycle with 8 dB spread running across the groups). The reset fixes which sample plays but not its level: trim the loud member afterwards.

## Tempo map (c07)
- 2026-11-08 (c07): a RAMP_SPANS ramp whose end tempo equals the last printed step left no tempo event at the span end, so the ramp's last 0.25 qn value (226.17) held through the whole Trio instead of the printed 228. smooth_tempo now writes the tempo in force at each span's end.

## MIDI rules at quarter 264 (c07)
- 2026-11-08 (c07): EW's 45-80 ms legato overlap is 40-70 % of an eighth at quarter 264. Capping the overlap floor at 35 % of the target's length raised 1,242 joins from 9-11 ms, and the string legato spread stayed within the probe limits (Violins I 74, Violins II 84, violas 88, celli 68 ms).
- 2026-11-08 (c07): string staccato eighths here were already 50 % of the slot (p90 0.50-0.65), inside the research's 50-62 % spiccato length.
- 2026-11-08 (c07): repeat gaps 0.09 s at 30 % of the note (strings) plus the theme's Staccatissimo / Stac RRx9 rows on the merging pairs raised the tutti stem pair dips from 1.9-9.2 to 4.7-10.4 dB, with the drier returns.

## Brightness and EQ (c08)
- 2026-11-09 (c08): an EQ simulation on the previous render's stems (non-resonant shelves and bells, K-weighted gain give-back) predicted the master's 6-20 kHz share within 0.8 dB (-29.7 simulated, -28.9 rendered) but the 2-6 kHz share 1.2 dB too low (-10.7 vs -9.5). Aim the 2-6 kHz cut about 1 dB past the target.
- 2026-11-09 (c08): turning the template's timpani 84 Hz bell off took the timpani share of the master's 40-100 Hz in tutti from 70 to 46-49 % (simulated 47 %).
- 2026-11-09 (c08): Horn 1's pp release-trail sample set the final chord's RT60. Release trails at -6 dB (`rt_gain_db`) gave 1.68 -> 1.28 s; lowering the returns had changed nothing in simulation.

## Rows and memory (c08)
- 2026-11-09 (c08): moving the reprise's string shorts to other rows (Spiccato RRx9 for phrases 1 / 3, Staccatissimo RRx9 for 2 / 4) cut the attacks identical to the first statement from 29 to 2 of 38. The round-robin counter alone does not keep a repeat section from replaying the same samples.
- 2026-11-09 (c08): unloading one Leg Port MAX row (22,428 regions) paid for three short rows (+26,419 regions); REAPER settled at 45 GB, as before.

## REAPER and Opus loading (c08)
- 2026-11-09 (c08): a reopen can hang inside Opus with no I/O: one instance constructed in 20 min, REAPER flat at 1.2 GB and 3 % CPU, the main thread (VST3_LoadState) and another Opus thread both waiting on mutexes (`sample REAPER 2`). This differs from the slow cold-cache load, where memory keeps growing. Since the quit before it had saved, killing REAPER and starting again lost nothing; the next open took 4 min. Check `sample` before waiting the full 10 minutes.
- 2026-11-09 (c08): with other processes holding most of the Mac's 96 GB, macOS compressed 21 of REAPER's 45 GB within 2 minutes of settling, and a restart does not clear that. Rendering with --force-memory straight after audio_init kept every entry probe within limits except one section's legato spread, which a re-render reproduced (so not the compression).
- 2026-11-09 (c08): a one-track test render (select only that track, RENDER_SETTINGS 3, render to a scratch folder, restore RENDER_FILE / RENDER_SETTINGS afterwards) takes one real-time pass (about 5 min here). Use it to tell render variance from a data or state cause before rendering everything again. The stem carries the pre-roll; cut it before comparing.

## Opus state saved after a render (c09)
- 2026-11-09 (c09): after an Opus instance has played, REAPER's saved state holds runtime values: the AHDSR `attack` of the legato sustain groups (Violas KS Master "V1s pp..ff", 52 groups, 841-1501 ms written -> 20 ms saved), the EWSO filter's `legato_speed_active` (true -> false), every `Controller 1` processor value (127 -> 0) and the CC11 / CC1 start-mode defaults. A `--midi-only` build reloads that saved state. A one-track test with only the 52 attacks set to 20 ms reproduced the flipped legato state exactly (joins at velocity 112+ about 0.08 s early, window 114-122 ms, legato passages 1.3-1.6 dB louder; joins under v112 unchanged); the written state gave -3 ms and 88 ms. Fully rebuild every legato instance before a render (`MIDI_ONLY_REBUILD_LEGATO`); to inspect, decode the .rpp's VST3 block (base64 lines, gzip JSON) and diff against the generated state.
- 2026-11-09 (c09): every legato KS Master (strings, woodwinds, brass, DIV patches) maps controller_22 "True Legato: Mono"; CC22 was not the cause here (the state stays mono by default), but sending 127 in the pre-roll costs nothing.

## Articulation (c09)
- 2026-11-09 (c09): two slurred eighths after an accented half note at quarter 264 (0.114 s each) played as Leg Slur MAX targets joined from the Sus Marc LITE head (overlap, legato lead, same velocities) came within 8 dB of the half note's body on all 18 tails (as Sus MAX re-attacks at p: up to 17 dB under). The KS Master's legato script joins a Leg Slur target to a note held on another row.
- 2026-11-09 (c09): a soft (p / pp) slow-attack string entry did not come earlier with more lead: celli 504 with 0.12 s entry lead plus a 4 dB early fill read +367 ms (was +285), basses at v53 with 0.06 s more lead +166 ms (was +146).

## Levels (c09)
- 2026-11-09 (c09): note trims ramp over 0.6 s by default; on a 0.11 s staccato a -8 dB trim moved the note by 0.7 dB. Give short notes and held-note attacks `NOTE_TRIM_RAMP_S` 0.02-0.1.
- 2026-11-09 (c09): K-weighted and plain-RMS balance figures differ by 2-3 dB on high woodwinds (critic B's +8.4 dB oboe over flute read +6.2 dB in plain RMS); simulate a role on the stems with the measure you will check it by before writing it (stem_fix.py --out).
- 2026-11-09 (c09): pitch trims with `_all_arts` on a flute's tutti notes moved the stem about twice the table value (-2.5..-4 dB gave -5.4 dB median); halve and re-measure.

## Hall and returns (c09)
- 2026-11-09 (c09): the c07 return simulator (2 x 2 transfer per return from averaged cross-spectra, 2^19 rectangular windows, lag-weight correction, send inputs with send_row_db envelopes from build_reaper.send_list) fitted the returns to -21..-28 dB residual and predicted the rendered G.P. decay within 0.1 dB at +0.3 / +0.6 s and the returns' share within 0.1 dB (`cycles/c09/actor_scripts/retsim09.py`). It missed the late +1.0 s point by 6 dB and the final-chord RT60 by 0.14 s.
- 2026-11-09 (c09): putting the trombones, tuba and bassoons back into their families' halls 3 dB under (with the returns' 180 Hz high-pass), trumpets at the horns' send, high winds +3 dB and the DIV tracks +3.6 / +4 dB moved the G.P. drop at +0.3 s by only 0.6 dB (21.1 -> 20.5) and RT60 1.30 -> 1.34 s; the returns rose from -12.9 to -11.6 dB re dry.
- 2026-11-09 (c09): a soft-end check on stem + R Strings counts whatever else rings in that return: sending the harp harmonics to R Strings at a handover read 0.71 s instead of the strings' own 0.29 s.

## Hairpins at fast tempi (c10)
- 2026-11-09 (c10): an early-rising crescendo curve (70 % of the rise at 40 %) on a four-bar p < ff under a theme put a held wind chord at f two bars early: one oboe was the loudest stem a bar before the arrival and every wind fell 4-8 dB at its ff. Long crescendos (over 3.5 bars) at 35 % of the rise at 60 % took that oboe from 4 dB over the violins to 9 dB under. Applying the late curve to the 3-bar sfp < ff hemiolas too changed their legato velocities, leads and lengths (rules keyed on the dynamic lane), so set the length threshold above those.
- 2026-11-09 (c10): capping one-beat untargeted crescendos at 6 CC (from 22) moved the soft horn and clarinet swells only 0.3-2 dB on the stems: on CC1-dynamic tracks the swell came mostly from the sample's own layer and the note change, not the lane. A post-hall level shape over the crest (-2.5..-3.5 dB) did the rest.
- 2026-11-09 (c10): a lone decrescendo's dB gain was released 1 qn after its arrival even inside a held note (the last note of the movement swelled +2.5 dB into the fermata); hold it to the note's end. The rest of the swell (+2.7 dB at constant CC) is the sustain sample's own.

## Articulation (c10)
- 2026-11-09 (c10): the MIDI notes of printed staccatos are already shortened by the extraction, so a rule that scales "the written value" must read the event list's duration, not the MIDI note. Lengthening a flute staccato quarter followed by another note made the next note lose 0.09 qn of entry lead (the wind detach gap keeps 0.05 s after the previous end); lengthen only before rests. That moved Flute 1's median note-off step 7.6 -> 5.8 dB.
- 2026-11-09 (c10): a velocity rise (100 -> 118) plus 0.03 s more lead on an unslurred flute Sus MAX entry at an sfp did not change its sf-to-p drop (6.9 -> 7.1 dB): the sample peaks about 0.23 s in, after the CC11 fall.
- 2026-11-09 (c10): string legato targets at v80 instead of 106-112 on a p espress. line (quarter 228), with 0.03 s more lead, moved the perceived joins from -63 to -19 ms median; the probe's window and spread did not change (66 -> 65 ms, SD 53 -> 49). [Corrected in c11: with the previous note's pitch excluded the joins were +51 -> +39 ms, not -63 -> -19; see "Legato timing (c11)".]
- 2026-11-09 (c10): ending the note before a horn tenuto repeat 0.10 s early (from 0.07 s) raised the repeat dips only from 0.2-1.3 to 1.9-3.6 dB at ff; the release trail fills most of a gap that short.

## Mix (c10)
- 2026-11-09 (c10): REAPER track width 0.5-0.6 on brass whose seat is set inside Opus pulls the image toward the centre; raising reaper_pan by seat x (1 - width) x about 0.5 (0.075-0.155) kept each stem's left/right balance within 0.6 dB (simulated on the previous stems as mid/side width then balance pan). L-R correlation rose from 0.50-0.64 to 0.81-0.89. The master's sample peak at the summit rose 0.4 dB with no stem peak changing.
- 2026-11-09 (c10): a soft-end check on stem + one family return counts every track routed into that return; routing a harp's harmonics through its own family return instead returned the strings' handover to 0.29 s with the same send level.


## Legato timing (c11)
- 2026-11-09 (c11): a legato lead cap measured from the previous note's score onset makes the note after a led short note late (+135..+180 ms after a slurred eighth). Measuring the cap from the previous note's moved onset fixed those and cut the joins over +60 ms by 30-60 % per string section.
- 2026-11-09 (c11): removing the cap also lengthens leads in runs of longer notes. Predict each join from the previous render's attack time plus the lead change and fit negative per-onset offsets where the prediction is under -40 ms. A section already on time at the capped lead keeps the cap for notes longer than an eighth.
- 2026-11-09 (c11): when a per-articulation lead extra is added, subtract it from the per-onset offsets already fitted on that articulation, or those joins move twice.
- 2026-11-09 (c11): clamp the total lead (base + extras + per-onset offset), not the base, or negative per-onset rows are mostly lost (finale technique 20).
- 2026-11-09 (c11): measure join times with the previous note's pitch excluded. Measured that way, c10's v80 legato targets on the celli moved the joins +51 -> +39 ms (not -63 -> -19); 0.06 s more lead at v85 or less brought the median to -8 ms.
- 2026-11-09 (c11): 0.04 s more legato lead on a second flute moved its median join by 7 ms (+53 -> +46); lead alone did not close the gap to the first flute at +2 ms.
- 2026-11-09 (c11): fitted re-bow points are keyed by moved onsets. After any lead or tempo change, rename the keys or the fills miss their notes.

## Attacks and re-attacks (c11)
- 2026-11-09 (c11): Sus MAX string strokes speak 60-110 ms after the note-on at CC11 75 or more and 210-380 ms at CC11 60-74. A CC11 lift at the stroke (+22, back to the curve 0.5 qn later) with a 0.07-0.09 s lead moved soft re-attacks after an sfp from +31..+177 ms to -47..+50 ms; a volume swell does not change the time.
- 2026-11-09 (c11): at a chord stroke, check every track. One section had no stroke of its own (its note-on sat at the soft point before the spike) and read 115 ms late; a lead on the abutting note gave it one (-17 ms).
- 2026-11-09 (c11): a stroke measured against a later stretch of the same note changes meaning when the track gains an earlier stroke; measure against the note before.
- 2026-11-09 (c11): an entry-lead extra on a note re-tongued after a gap under 0.2 qn removes its lead. A per-onset re-tongue lead of 0.13 s kept the lead but did not move a horn's attack (+84 -> +83 ms).
- 2026-11-09 (c11): measure a re-attack hole against the note before (lowest 10 ms frame within 0.15 s of the note-on). Ending the note before 21 ms ahead of a horn re-attack instead of 63 ms cut the hole from 12.7 to 7.3 dB.
- 2026-11-09 (c11): soft Sus entries with 300 ms total lead and a +4 dB early fill still read +138..+167 ms late (from +272..+281). Entries that started 130-160 ms late came inside +60 ms with 220-240 ms lead.
- 2026-11-09 (c11): reject an automatic early fill whose ramp falls inside a led legato transition; keep the previous values.

## Levels and envelopes (c11)
- 2026-11-09 (c11): a family-wide phrase-shape scale must skip tracks whose dynamics run on CC1. There it moved the whole dynamic layer (+2.6..+4.5 dB), not the shape.
- 2026-11-09 (c11): note trims on pizzicato notes act as steps and are realised as requested. On bowed and blown notes they ramp in over 0.6 s: give short notes a 0.1 s ramp, or a level shape where the trim falls short (a -3 dB trim left +2.4..+4.6 dB in the simulation; a -5.5 dB shape reached +0.4).
- 2026-11-09 (c11): a join trim that ends at the next note-on is cut short when a longer lead moves that note-on earlier (+5.5 dB requested, +3.5 realised). Hold the plateau to just before the next score onset.
- 2026-11-09 (c11): end a role row inside the next entry's lead. A longer entry lead can shorten the rest before it to under the 0.5 s tail-hold minimum, and the row's release then lifts the previous note's hall tail (3 dB).
- 2026-11-09 (c11): on the first render after a full rebuild, recheck trims fitted on earlier renders; one fitted on stale audio no longer applied and was removed.
- 2026-11-09 (c11): simulations on the previous stems show volume-envelope changes only. CC, velocity and lead changes need the render, so run the same measuring script on both renders.

## Tempo (c11)
- 2026-11-09 (c11): a ritardando ramp interpolated to the next tempo mark overshoots its last printed step (127 where 140 was printed). Hold the last step until the next mark (`RAMP_LAST_STEP_HOLD_QN`).

## Delivery (c11)
- 2026-11-09 (c11): a delivery ride ramp must not run against a printed hairpin. A 2 dB fall inside a crescendo cut a +2.9 dB step to +1.7 in the mp3; moved into the last 0.4 qn before the subito it gave +2.8. Otherwise spread the ramp over a hairpin of the same direction.
- 2026-11-09 (c11): a +1.5 dB flat-fit ride row after a subito p cut the delivered step from 8.8 to 7.1 dB (master 10.2). Not adopted.

## Extraction (c11)
- 2026-11-09 (c11): texts printed on full-bar rests (stick changes, mutes, instrument changes, harp damping) do not reach an event list built from notes. A multi-measure-rest text listener in the engraving file adds them; the harp damping marks then set note ends (ring 0.3-0.6 s after the mark: -47 dB to silent).

## REAPER / Opus state (c11)
- 2026-11-09 (c11): Movement I's `state_guard.py` on the project saved after a render found 5 of 31 tracks stale; after a full build of every track and a save, 0; in the project saved after the next render, 5 again. Fully build every track before each render and run the guard after the save.
- 2026-11-09 (c11): after a full build, no unchanged track moved against the previous render (median 0.00 dB and 0 ms on all 31 tracks), so the whole-track level and timing drift seen after --midi-only builds elsewhere did not occur.
- 2026-11-09 (c11): this project's per-dynamic volume trim reads the dynamic curve, not the printed mark, so an fp spike is a one-grid-point bump in the trim and needs no `fp_falls` key.

## Render checks (c11)
- 2026-11-09 (c11): two renders of identical data differ on single notes. Staccato woodwind notes differ by 1-6 dB (round robins); horn notes re-tongued 7-14 ms after the end of the note before lost their attack in one render (holes up to 26 dB for 0.5 s) and not in the other. Compare every stem per half beat with the previous render before deleting that render.
- 2026-11-09 (c11): such notes can be repaired without a second render: splice the previous render's stem over spans whose data is identical (30 ms crossfades), splice the matching return spans, and rebuild the master as the stem sum. This is offline work and can follow the unlock.
- 2026-11-09 (c11): choose splice points where the two renders correlate. A sustained note can sit at opposite phase between renders (correlation -0.75), and a crossfade there makes a dip.
- 2026-11-09 (c11): a perceived-attack reading can change when only the next note's onset moved (the stems were identical through the note). Compare the stems before treating it as a regression.
- 2026-11-09 (c11): the hall return's level on single sustained notes varied 2-3 dB between renders whose dry stems agreed within 0.6 dB.

## REAPER / Opus state (c12)
- 2026-11-09 (c12): what the tracks stale after two renders had in common: each had left its legato row for a sustain row 2-70 ms after its last legato note and repeated that pitch on the sustain row. No track whose legato row was still selected at the end was stale (8 of 8 in both renders). The stale set is not deterministic: a track with identical data was stale after one render and clean after the next.
- 2026-11-10 (c12): sending the legato row's keyswitch once more after the last note (5 qn after the last release) does not prevent the stale save: all three treated tracks were stale after the render, as were the controls. A track that was clean after two earlier renders with the same closing notes was stale this time.
- 2026-11-10 (c12): what does give a clean save after a render: rebuild the stale tracks in full with no playback, then save (7 tracks, 24 s). Run the guard on that save.
- 2026-11-10 (c12): a full build started 5 s after the project opened, while the instances were still loading samples, crashed REAPER inside Opus (EXC_BAD_ACCESS). Wait for memory to settle after an open before replacing instances.
- 2026-11-10 (c12): when two consecutive cycles each render after a full build of every track, tracks with identical data reproduce to 0.00 dB median (largest single note 0.45 dB, lag 0 ms). The 1-6 dB single-note differences of c11 were against a render made from a partly stale project.
- 2026-11-09 (c12): the shared lock has no queue. A new waiter that starts polling can take the lock ahead of one that has waited longer; start waiting only after the longest waiter has had its turn.
- 2026-11-09 (c12): a foreground shell call is moved to the background after about 3 minutes here. Wait for the lock in calls of 160 s (`perl -e 'alarm shift; exec @ARGV' 160 ...`) and read the lock file after each one.

## Velocity tables (c12)
- 2026-11-09 (c12): a velocity-cap shift anchored on a span's top velocity lets one loud note set the rest: in five harp spans 30-50 notes each fell to the floor (mean -1 to -12 steps). Per-note velocities keyed (onset, pitch) and applied after the caps did the same job without moving other notes.
- 2026-11-09 (c12): per-pitch velocity offsets measured at one velocity layer overstated the level differences at a softer layer by 2-3 times. Fit them at the layer the passage plays.
- 2026-11-09 (c12): a fixed-velocity table must be applied after the caps and clips, or the cap rewrites it.

## Attacks and re-attacks (c12)
- 2026-11-10 (c12): a minimum gap of 32 ms before a legato-row note that starts a phrase on the pitch just ended (`LEG_HEAD_MIN_GAP_S`, wind and brass) removed the re-tongue holes where the gap had been under about 20 ms (8.5 -> -1.3, 7.7 -> 1.7, 5.6 -> 3.8 dB) and left alone the ones that already had a longer gap (7.0, 9.7, 5.8 dB unchanged): those are not a gap problem.
- 2026-11-09 (c12): a re-attack lead table does not apply to a note after a rest; a wind row with no articulation entry lead gets one only from a per-onset entry-lead extra.
- 2026-11-10 (c12): accented string half notes that start under their body: a body cut starting 0.18 s after the onset does not change a front-minus-body reading taken at 100-200 ms, and a symmetric swell lowers it. Entry leads 0.03-0.05 qn with a front-weighted swell (+4.5 dB, peak at 0.08 s, gone by 0.24 s) raised the stems' fronts by 1.3-3.4 dB and moved their onsets from +19..+53 ms to -13..+10 ms. The master's front moved 0.2-1.6 dB only: in a tutti the other tracks set it.
- 2026-11-09 (c12): compare an sf front with the same track's ff accent on the same pitch class or register; against a different pitch the reading mixed in a 5-8 dB pitch difference.

## Levels and envelopes (c12)
- 2026-11-09 (c12): at quarter 264 a 0.6 s trim ramp is longer than most notes: 30 of 95 note trims on bowed or blown notes reached under 80 % of the request (0.11 s notes got +0.3..+1.2 of +1.5..+7 dB). List trims against note length (`trims12.py`) before fitting more.
- 2026-11-09 (c12): the level a narrowed track loses can be read from its own stem as mid/side energy (0.6-1.1 dB at widths 0.5-0.6 here); add it to the gain once, not on top of a level finding that already includes it.
- 2026-11-09 (c12): a parked CC11 value on a staccato note reads as a reversed crescendo in a hairpin count. Exclude parked notes before counting.
- 2026-11-09 (c12): one weak pitch on a section (basses' arco E2, -4.9 dB against the other pitches at equal CC11, from a regression of body level on CC11) is better fixed by per-onset trims with short ramps than by a pitch trim when the same pitch is in tune on the pizzicato row.

## Round robins (c12)
- 2026-11-09 (c12): a CC16 reset before a staccato passage and before its reprise starts both on the same take; the first render after adding it differs from the previous one by 1-6 dB on single notes there, which is a take change.

## Legato timing (c12)
- 2026-11-10 (c12): a positive pitch trim on a legato target that starts with the mirror ramp ([moved onset - 0.05, + 0.03] qn; Movement II c50) left the joins at +3 to +15 ms (7 horn joins, +3 dB).
- 2026-11-10 (c12): fitting join offsets from another measurer's perceived onsets by `0.7 x (pc - 20 ms)`, clipped to 0.15 qn, moved 45 early string joins from medians of -77 to -105 ms to -13 to -19 ms, none left outside +-50 ms.
- 2026-11-10 (c12): a track whose joins another measurer reads 40-80 ms later than an old render: rebuild it in full and measure again before changing a lead. Here the readings were identical to the ms after the rebuild, so neither stale state nor the data was the cause.

## Levels and envelopes (c12, after the render)
- 2026-11-10 (c12): a regression measure that removes the volume lane cannot show a lane trim's effect; read the note body directly.
- 2026-11-10 (c12): a level shape on a pickup is judged against its downbeat, and the downbeat of a repeated pitch varied 6.8 dB between a passage and its reprise with identical data. Set the pickup from the smaller of the two differences.
- 2026-11-10 (c12): a gain change in mix.json moved every note of the track by exactly that amount (+2.00 / +3.00 dB), and the brass return rose 0.65 dB re dry with RT60 unchanged.

## Range tests (c13)
- 2026-11-10 (c13): the first one-track range render after a rebuild is not usable even 50 s after the build: 27-29 of 30 legato joins read up to 400 ms off, while the second render 20 s later agreed with a later one. After a full build of 31 tracks the memory was not settled. Render each variant twice or three times and discard the first.
- 2026-11-10 (c13): a variant that passes on the range render reproduced in the full render to the millisecond when the line stays on one sustain row (nine figures, every start and length equal). Range renders play every track, so the state guard finds stale tracks afterwards: run it before the full render.
- 2026-11-10 (c13): a dominant-pitch measure (harmonics 1-4, 2048-point STFT, 2 ms hop: for how long each note of a figure is the strongest pitch) shows a swallowed note that an onset measure hides, and shows a ringing note covering the next one.

## Fast slurred notes (c13)
- 2026-11-10 (c13): two slurred eighths of 114 ms after a half note: as Leg Slur MAX targets the second was the dominant pitch for 0-44 ms; on "Slur Runs" (v85, 0.05 s leads) the first came +55..+103 ms late and two renders differed; on Sus Marc LITE with 0.09 s leads both were dominant for 124-192 ms and started within 50 ms of the beat. Sus Marc LITE eighths at v78-85 play 5-14 dB over a p half note's body on the same row and ring over a soft staccato after them: level steps per note, hold the last step to just before the next beat (a return at the next note-on lifts the ringing note), and end the last eighth 60 ms early.
- 2026-11-10 (c13): a legato-row note that follows a note on another row with no rest gets no lead from the entry or join rules and sounds late (winds +30..+96 ms, strings +45..+186). One lead per wind track with a 32 ms gap brought the winds to 0..-19 ms (median); measured lateness times 0.85 was twice too much on the oboe, because ending the previous note early moves the reading too. After an eighth the lead costs the eighth: at half of its length a Sus MAX pickup was cut from 171 to 85 ms of note.
- 2026-11-10 (c13): positive per-onset legato rows on notes after short notes do nothing while the lead cap (0.75 of the previous slot) or the minimum gap (0.1 s between note-ons) binds: 12 of 12 such rows left the join where it was. Print the realised lead next to the requested one before rendering.
- 2026-11-10 (c13): one legato row for a string line (Leg BC MAX notes moved to Leg Slur MAX) put all 30 joins of a tune 120-260 ms early: every lead on the line has to be refitted, as Movement II found.
- 2026-11-10 (c13): keyswitches 0.15 s before the note on a line with 13 row changes in 30 joins: 16 joins outside 25 ms against 14, 10 joins moved by 25-70 ms in either direction. No cure by itself.
- 2026-11-10 (c13): staccato notes at 0.7 of their length on the 1TP "StacSs DblTng" and string "Stac RRx9" rows did not deepen same-pitch pair dips (2.2 -> 2.2, 2.5 -> 2.3 dB): these rows play the sample out past the note-off.

## Mix (c13)
- 2026-11-10 (c13): the Close-mic seat formula L-R = 20 log10((1 - seat) / (1 + seat)) predicted the woodwind stems within 0.5 dB after narrowing, and the stems' K level stayed within 0.3 dB: no make-up gain.
- 2026-11-10 (c13): REAPER's return-track pan follows the balance law 20 log10(1 - pan) on the far channel: pans 0.17 / 0.06 / 0.07 / 0.05 moved the returns' L-R by -1.5 / -0.6 / -0.9 / -0.5 dB against their dry senders.
- 2026-11-10 (c13): the Stereo Double processor of a DIV patch (instrument Global Group, class StereoDouble) at spread 0.4: correlation 1.00 -> 0.93, level -2.5 dB, tone within 0.4 dB, soft end 0.19 s longer on the stem plus return.
- 2026-11-10 (c13): halving a 3 dB send offset (to 1.5) lowered the wind return by 2.4 dB against its dry senders, not 1.5, in the same render that narrowed the seats: measure wet / dry after any seat change.

## Tempo (c13)
- 2026-11-10 (c13): removing 22 stretched beats moved no re-bow point (none lay in a stretched beat) and no per-onset key (all keyed by score onset); leads in seconds next to those beats changed by 0.01-0.1 qn. Check which tables are keyed by moved onsets before renaming anything.

## Lock (c13)
- 2026-11-10 (c13): a waiter that follows the longest-waiter rule without running a waiter process is invisible to the others and was passed three times (9 h). Start the waiter process as soon as the offline work is done, and let the others see its start time.

## One legato row per string line (c14)
- 2026-11-11 (c14): Violins I, Violoncellos and the DIV A solo moved to one legato row (Leg BC MAX notes on Leg Slur MAX, keyswitch 0.15 s before the remaining row changes): two whole-piece passes of identical data differed by 25 ms or more on 1 of 100, 1 of 200 and 0 of 18 joins (mixed rows, c12 against c13: 10 of 138 row-change joins moved by about 100 ms). Before the refit the lines were far off (outside 25 ms: 59 of 100, 178 of 200, 13 of 18; cello median +72 ms).
- 2026-11-11 (c14): refit = per-onset offset + the mean S of two agreeing passes (gain 1.0, at most 160 ms), then a second step at gain 0.8 on what was left: joins outside 25 ms went Violins I 48 (c13) -> 59 -> 13 -> 9 of 100, celli 101 -> 178 -> 46 -> 25 of 200, solo 10 -> 13 -> 6 -> 3 of 18; outside 60 ms 7 -> 2, 23 -> 9, 2 -> 0. Once a line is repeatable, the refit converges in two steps; three passes per step (the first discarded) cost about 15 minutes for 4 min 40 s of music.
- 2026-11-11 (c14): a guess before the refit can be wrong in sign: an earlier one-track test had read the celli 120-260 ms early on one row, so the row's lead was cut by 0.10 s first, and the whole-piece pass then read them +72 ms late. Start from the old leads and let the first pass decide.
- 2026-11-11 (c14): Leg Slur MAX against Leg BC MAX on notes of 0.45 s or more, first 0.5 s, envelope change removed: Violins I -2.0 dB (median of 7), celli -6.2 dB (22 notes, up to -11.9 at ff), solo -1.0. A flat level step per note (the shortfall, at most 6 dB, only from 3 dB) gives it back.
- 2026-11-11 (c14): a per-onset lead on the note after a long held note changes where the automatic re-bow of that held note falls, and its fitted fill then has no re-bow (score_to_parts prints the warning). Leave such a join out of the refit.
- 2026-11-11 (c14): the full rebuild of three string instances in a running session left REAPER at 65-68 GB (51 GB compressed) until the restart; the passes rendered in that state still agreed with each other to 25 ms on all but 3 of 318 joins. After the restart the project settled at 43 GB (45 before: three Leg BC MAX rows unloaded).

## Levels at the source or in the envelope (c14)
- 2026-11-11 (c14): Hollywood Strings "Sus Marc LITE" does not take its level from velocity: eighths at velocity 56-70 instead of 78-94 played at -26..-31 dB against -32..-39 for the half note before them on the same row (5-11 dB over, as before). On LITE rows the level of a single note can only be set by CC11 / CC1 or the volume envelope.
- 2026-11-11 (c14): a figure's level contour can be fitted on the previous render's stem when only post-fader envelope rows change: remove the old row's gain, fit one level per part of the figure against the first 300 ms of its accented note, and the next pass reproduced the simulated levels within 1 dB on nine figures (pair 2.3-4 dB under the half note's start, landing staccato within 1 dB of the pair).
- 2026-11-11 (c14): a pitch trim hits every dynamic. Three clarinet pitches that stood 6.5-9.6 dB out in soft solos would also have lost 3-5 dB over 46 qn of ff tutti: use note trims with a short ramp when the fault is in the soft layer only.
- 2026-11-11 (c14): a tool's `by_name` lookup that matches a key contained in the track name gives "Violins I" settings to "Violins II" as well; list the longer name first with its own value.
- 2026-11-11 (c14): a lead request above the cap changes nothing. A second flute's legato request had grown to 100 ms over two cycles while the default cap (0.45 of the previous eighth) held every join of its running eighths at 51 ms; print the realised lead before concluding that more lead does not help. A cap raised only for listed onsets (LEG_CAP_FRAC "listed") moves just the slow pitch pairs.

## EQ carried over from another movement (c14)
- 2026-11-11 (c14): narrow note cuts fitted on another movement's bass notes sat on this movement's tonic and dominant (87.3 Hz -10 and 61.7 Hz -6 on the basses, 84 Hz -5 on the tuba). Removing them and a cello +3 / +3 dB pair at 170 / 125 Hz, simulated on the stems with RBJ peaking filters: 70-112 Hz share of the two tuttis -16.3 / -16.9 -> -14.8 / -14.9 dB, 140-355 Hz share of the cello tune -5.1 -> -6.5 dB, master level within 0.6 dB per passage.
- 2026-11-11 (c14): removing a 98 Hz -4 dB bell from the basses' tutti EQ lifted G1 / G sharp 1 / A1 (second harmonics at 98-110 Hz) by 1.9-3.9 dB and E1 / B1 by 0.7: the cut had been balancing pitches, not only colour. Check every removed bell per pitch before the render (here it was halved and E1 / B1 got +2 dB note trims).
- 2026-11-11 (c14): removing the cello bells cost the cello stem 2.9 dB of plain level (most of its energy lies at 100-250 Hz); themes need a role to stay where they were.

## Crescendos and trim tables (c14)
- 2026-11-11 (c14): per-dynamic trim tables that fall 9-11 dB from p to f (ours; Movement II's fall 4.5-6.3) took back single winds' crescendos. An opt-in hold in build_reaper (`cresc_trim_hold`: inside a crescendo the trim falls by 0.3 of its fall, at most 3.5 dB held, released over 0.5 s after the arrival, winds and strings only, not on sfp hairpins) with f anchors 2.5-2.8 dB higher moved four named clarinet and flute crescendos from -5.8..+1.9 dB to -0.8..+5.9 dB (simulated on the stems). Overlapping hairpins must take the largest hold, not the sum.

## Lock (c14)
- 2026-11-11 (c14): where background processes are refused, the queue waiter can run in foreground calls of under three minutes if the list of folders ahead is kept in a file between calls; other threads' waiters see the process while it runs.
- 2026-11-11 (c14): the full render in a new session reproduced the last refit pass: 2 of 100, 1 of 200 and 0 of 18 one-row joins moved 25 ms or more.
- 2026-11-11 (c14): a level step that falls on the beat of a short note whose note-on lies 45 ms earlier makes measure S read that note 60-130 ms early with unchanged MIDI; compare S only between renders with the same level rows, or read such notes with a dominant-pitch measure.
- 2026-11-11 (c14): 0.13 s more entry lead on a pp legato entry made it read later (+187 -> +261 ms), as in c09: soft slow-attack entries do not come earlier with lead.

## Volume envelope: slow balance only (c15, Dan 2026-11-11)
- 2026-11-11: Dan's rule after opening REAPER and hearing Movement I c56: no per-note track volume moves at all. `score_to_parts.py` tags every envelope item (`vol_add("class:layer", ...)`; classes slow / level / shape) and `VOL_CLASSES = ("slow",)` writes only roles, hairpin gains, roll shapes, held decrescendos and the fade; the other lanes stay in parts.json `vol_cls` as a record. Points 40,724 -> 4,545 (146.6 -> 16.4 per second over 31 tracks), notes with over 3 dB inside the note 22 % -> 6 %.
- 2026-11-11: three things drew most of the points before any rule was removed: trims that returned to 0 dB between the notes of a run (a row trim merged notes only when the next one started within 0.06 qn of the written note end, so no staccato run ever merged), slow ramps sampled as stairs (a 0.25 qn lane sampled on a 0.125 qn grid), and collinear grid samples. Sampling the lane on the builder's own grid plus a 0.1 dB Douglas-Peucker pass removed three quarters of the points with the sound unchanged.
- 2026-11-11: REAPER draws a volume envelope's line in its fader scale and in seconds. `ScaleToEnvelopeMode(1, amplitude)` is not a power law: 716.2 at 0 dB, 483.9 at -12, 363.3 at -20, 171.0 at -40, 79.5 at -60, 1000 at +12 (table in `tools/env_scale.json`, read with `jobs/env_scale.lua`). A simplification done on a wrong law (amplitude ^ 0.25) differed from the full envelope by up to 0.9 dB on long segments; on the table, or with no kept segment over 4 dB, by 0.1 dB.
- 2026-11-11: a level step into a note belongs where the old note stops sounding, not at the MIDI note-on: 60 ms or more of MIDI gap, at the new note-on; otherwise after the SCORE onset (the clarinet's legato carries the old pitch about 50 ms past it although its MIDI gap is 11 ms: join holes 8.4 / 10.2 / 7.7 / 8.6 dB with the step at the moved note-on, 2.4 / 4.3 / 2.2 / 2.6 with it 50 ms after the score onset, equal to the stem without any envelope).
- 2026-11-11: an envelope change can be judged on rendered stems without REAPER (stem x new / old envelope, `cycles/c15/actor_scripts/sim15.py`). Compare levels as the mean of the two channels' powers; a mono sum reads wide string stems 1.2-1.8 dB lower and looked like a balance shift.

## Levels inside Opus instead of the fader (c15)
- 2026-11-11: per-region `volume` in the Opus state works as a per-pitch level correction (`build_reaper.py region_gain`, mix.json `region_gain_db` {"rows", "pitch_db", "row_db"}): absent keys count as 1.0; a whole row can be scaled the same way. On a whole-piece pass the per-note levels of Oboe 1 / 2, Clarinet 2, Cor anglais, Trumpet 1 and Flute 1 matched the envelope version within 1 dB on 90-100 % of notes; on the four horns 10-18 % of notes came out 2-5 dB under it (legato-joined notes: the transition regions are not keyed by the target pitch alone). State guard stayed clean after the build.
- 2026-11-11: Violins I "Sus Marc LITE" 8 dB lower as a row (`row_db`) replaced nine fitted per-figure level rows on the theme head: half notes and slurred eighths within 1-4 dB of the fitted levels, and the landing staccato's pitch dominant 20 ms after its beat in 7 of 9 figures (c14: 2 of 9), since the row's loud release trails fall with it.
- 2026-11-11: timpani single strokes at f: velocity +22 (85-98 -> 107-120) in place of a +6 dB fader spike gave -1.1 dB (median, 20-170 ms) against the spike, but the 2-5 kHz share of the first 80 ms rose 5 dB: the louder layers are harder. For weight without bite use about +14 and a role.
- 2026-11-11: with CC11 parked at 120 on string short rows the printed level has to come back through the fader (2-8 dB per section here); without the park the short rows take it from CC11 again and the stems kept their levels.

## Instrument-side fixes after the per-note fader moves (c16)
- 2026-11-15: a re-bow of a soft held string note cannot be closed on one instance (the new Sus MAX bow needs over a second; a same-pitch overlap stops the new note). A second instance on another patch file (a DIV half section) holding the same pitch with bow changes halfway between, each at the same level, and a CC11 lift of 7 units for about 1.5 s on the holding track took 12-13.5 dB dips to 4-6.5 dB. The DIV A patch read 8.5 dB under the full section at the same CC11: measure both stems before setting levels.
- 2026-11-15: a string note of 5.3-5.6 s in one bow (one pass over the 3.95 s loop point) shows no dip or pulse at ppp; the automatic re-bow limit of 4.5 s was the cause of the hole.
- 2026-11-15: a post-pass on the written envelope ("no unprinted move over 1.9 dB inside a sounding note": finish a move at the note's start before the note-on, otherwise hold to the note's end and return in the next rest, across the next printed hairpin or mark, or at 2 dB/s) removed every such move (231 notes changed). A return drawn as one line to a later point skipped whole passages; a slew-limited return that stops at the next rest or printed zone did not. Holding crescendo arrivals raises the arrival bars by 1-2 dB per section on bass lines.
- 2026-11-15: accents by CC11 with the printed ff resting at 104: strings +20 units (ceiling 124) for 0.15 s gave only +0.8 dB at ff, +1.6 at mf-f, +2.2 at p-mp (+12 units); woodwinds +20 gave +4.0 dB at ff and +10 units for 0.08 s gave +2.7. Clarinet (CC11 is plain volume) reads +5 with the same numbers as the other woodwinds: give CC1-layered patches their own, smaller value.
- 2026-11-15: rules that pick leads, rows and velocities from the CC11 value must read it before an accent bump or a resting-level map is applied; with the bump in, entry-lead classes changed on accented notes (up to 60 ms).
- 2026-11-15: region gains: row names differ in case between patches ("Sus Max" on the cor anglais KS Master, "Sus MAX" elsewhere); a gain keyed to the wrong spelling is silently not applied. Sustain rows have one group per dynamic layer (name ending pp / p / mf / f / ff, release trails with " RT"), short rows have velocity ranges per region (woodwinds 1-74, 75-114, 115-127; timpani Lng 16 ranges with 93-98, 99-110, 111-120 at the top): a gain can be set per layer. Critics' first values (4-7 dB) moved whole sections by 2-6 dB; half of them kept sections within 2 dB.
- 2026-11-15: a played gap of 0.09 s before a same-pitch brass repeat gives 5.6-10.4 dB of separation (median per track) where 6-35 ms gave 1.5-5.9 dB.
- 2026-11-15: the timpani "Rls" roll at a held CC1 of 118 keeps its level through a bar (within 4 dB); a CC1 ramp 62 -> 104 over one bar grew only 2.3 dB.
- 2026-11-15: row-change legato joins given the "first note" time as lead (0.2-0.245 s) overshot on the celli and violas (joins outside 25 ms 28 -> 58 of 200 on the pass); a refit on a single pass brought the over-60 ms count under c15's but left the celli worse inside 25 ms. Refit on two agreeing passes.

## Lock and long stops (c16)
- 2026-11-15: an actor stopped by a usage limit keeps the REAPER lock (here four days). Before a stretch of analysis under the lock, decide whether to release it; keep each lock-phase step a short detached command with a done-file so that a resumed actor can see where it stopped.
- 2026-11-15: with about 50 GB held by other processes REAPER settled at 43 GB with 27 GB compressed; the render with `--force-memory` passed the attack probe (0 late, 0 holes).

## Cycle 17 (2026-11-15; data and patch files only, no render)

### Patches
- 2026-11-15: woodwind KS Masters (FL, FL2, OB, EH) have three sustain layers named pp / mf / f, no p or ff group; a region gain for "ff" must name "f". Their staccato rows split by velocity at 75 and 115 (cor anglais: one split at 109).
- 2026-11-15: legato rows ("Leg Slur MAX", "Leg Slur Rep") keep their transitions in groups named by pitch ("TLeg A#3"), with no dynamic suffix; only the sustain groups inside the row carry one. The clarinet's "Leg Slur Rep" has no dynamic-layer groups at all, so a pitch gain there acts at every dynamic.
- 2026-11-15: 1st Violins "Sus Marc LITE": only its attack overlay is velocity-split (1-65 / 66-108 / 109-127); the sustain layers are 1-127. A velocity-limited gain cannot separate soft and loud notes on that row.
- 2026-11-15: pizzicato layer edges, read from the patches: celli 50 / 51, 85 / 86, 110 / 111; basses 55 / 56, 100 / 101. A pp line written at velocity 41-49 on the celli sits just under an edge of 6-13 dB.
- 2026-11-15: the timpani patch has no CC11 (the pipeline writes CC7); `channelMap` (Channel Routing) is a top-level key of every instrument, 0 in every patch read.
### Pipeline
- 2026-11-15: a lead cap that uses the previous note's score slot is wrong when that note is itself led; measure the room from its moved note-on and leave it 60 ms alone.
- 2026-11-15: a rounded note-on compared with its unrounded value by a tight epsilon made a note count as its own predecessor (keyswitch left 7 ms before the note). Compare with 1e-3 qn.
- 2026-11-15: a range render must start before a track's last keyswitch, which can be bars earlier than the note tested (here 85 qn).
- 2026-11-15: at quarter 264 a 1 qn release is 0.23 s: every crescendo gain released after the arrival falls inside a sounding note, so the guard holds nearly all of them. 112 of the envelope's crescendo gains had to move to CC11 or go.
- 2026-11-15: a chord rule keyed to simultaneous notes of one track finds nothing where the score writes the two notes as separate voices; check the count before deleting the row it should replace.
### Measurement
- 2026-11-15: decay readings: 2 x (t at -35 dB minus t at -5 dB) covers 0.1-0.8 s after a cut-off and shifts 0.1 s per 0.1 s of cut-off error; a fit between -25 and -55 dB covers 0.4-1.3 s and is stable. State which one a limit refers to.

### Cycle 17, from the range tests and renders (2026-11-15 / 16)
- 1FH KS Master, Main pair: G sharp 4 has its fundamental in anti-phase (L/R -0.69). With Close 3.8 dB over Main (Close -1.4 / Main -5.2 dB) it reads +0.65 and the mono loss falls 8.1 -> 0.9 dB. Cost: the stem turns nearly mono (correlation 0.82 -> 0.98) and loud and soft passages change level unequally (+4.7 dB mf call, +1.2 dB pp note), so one gain cannot give the old balance back.
- Horn CC11 at pp (CC11 about 35): 0.22 dB per unit (+5 units = +1.1 dB), not the 0.55-0.61 measured at mf elsewhere.
- Hollywood Strings, a ppp held note doubled on the DIV A instance: with both on "Sus MAX", bow changes 3.0 s apart and the holder's CC11 +10 complete on the other's change (held 0.30 s, back 0.55 s), dips of the sum are 1.6-3.5 dB; five changes 1.9 s apart with a late lift of 7 gave 4.3-8.2 dB. The DIV A "Sus MAX" matches the section's colour; its "Leg Slur MAX" re-attacks are 7 dB weaker in the fundamental.
- Celli "Pizzicato RRx4": velocity 41 -> 52 crosses the 50 / 51 layer edge and raised a pp pedal 9.2 dB.
- A crescendo gain moved into CC11 is lost when the arrival's played CC11 is 100 or more (flat above 104 on strings and woodwinds): 16 of 84 gains lost 1.5-4 dB; keep those in the envelope.
- A gain on a row's f / ff sustain groups of the celli "Leg Slur MAX" gave 0.2 dB for +1.5 on tutti notes: the transition groups, which carry no dynamic suffix, set the level of short legato notes.
- Lowering a short row by region gain raises the reading of every accent next to it: fit row levels first, accents second, on the same render.
- Removing a one-bar role together with a row gain on the same notes cost 8.6 dB in one exposed bar: check the per-bar master against the previous cycle after every role deletion (20 bars moved over 1.5 dB down here).
- REAPER grew from 43 to 56 GB (35 compressed) after 33 full track rebuilds in one run; after a restart it settles at 43 GB in about 8 minutes. A project saved after `--mix-only` held 4 stale legato states: rebuild them, save, guard, restart before a render.
- A full build of 31 tracks takes under 2 minutes once the samples are in memory; the 4 min 38 s render takes about 6 minutes.
- Two lock waiters that each list the other as ahead leave a free lock untaken; a waiter should drop a folder from its list once that folder has held the lock since the waiter first queued.

## Cycle 18 (2026-11-17)
### Controllers and patches
- 2026-11-17: crescendo gain moved into CC11 reached the arrival (within 0.5 dB) only where the measured slope at the arrival's CC11 was 0.16 dB per unit or more: Flute 1, cor anglais, Violins I / II at CC11 94-108. On bassoons, clarinets, oboe, horns, low brass, violas, celli and basses at CC11 88-98 the slope was 0.14 or less, negative on bassoons. Measure the slope per track (stem change less envelope change, over the CC11 change) before converting.
- 2026-11-17: a CC11 dip of 3-12 units over a "Leg Slur MAX" string transition (moved note-on + 0.03 s to the beat) left the swell before the beat unchanged (join excess median 3.2 -> 3.1 dB). The transition sample's level does not follow a short CC11 dip.
- 2026-11-17: Hollywood Strings "Sus MAX" at p, held notes: CC11 41-55 gave 0.27 dB per unit on violas, 0.48 on 2nd Violins (+30 units = +14 dB). Low-CC11 slopes differ by section; size large offsets from the section's own reading.
- 2026-11-17: 1st Violins accented theme note moved from "Sus Marc LITE" to "Sus MAX" at velocity 56-61 fell 7-8 dB: the Marc row's attack overlay carries most of a soft note's level.
- 2026-11-17: 1FH "Mono From Left" (channelMap 2) removed the G sharp 4 anti-phase (correlation -0.70 -> +0.99, mono loss -8.3 -> -0.2 dB) but raised the stem 3.7 dB and made it mono; re-level after switching.
- 2026-11-17: brass legato velocity 72 instead of 106-112 did not fill the sag after a slur on Horn 1 (hole -16 dB, unchanged).
### Delivery at -14 LUFS
- 2026-11-17: at -14 LUFS the limiter took about 5 dB on the scherzo's summit (tutti peaks); a fast compressor before it (threshold -6 dB, 2:1, 2 / 60 ms) brought the whole file from 4.4 to 3.3 dB on the c17 master but not the summit.
- 2026-11-17: the quiet lift and the 3:1 top ride left the summit 0.1 LU over the trio's ff and bar 72 on the delivered file, although it led by 1.6 LU on the master; ride rows of -1.5 to -2 dB on those passages gave +0.7 LU. Top ride 3:1 gave LRA 11.7, 2.5:1 gave 12.0.
- 2026-11-17: limiter ceiling 0.87 measured -0.9 dBTP after the 192 kb/s mp3 encode; 0.85 gives -1.3. The limiter lowers integrated loudness about 0.6 LU at -14; aim the pre-limiter level that much higher.
- 2026-11-17: measure the limiter's gain reduction per passage with the output moved back by its 5 ms look-ahead, and ignore near-silent windows (the faded tail read 44 dB).
### Pipeline
- 2026-11-17: removing the gap of a tongued wind join in the note pass took away the next note's lead (the lead rules look for the gap); keep the gap there and move the old note's end in the output stage.
- 2026-11-17: a slow gain release that crosses a G.P. into the next entry is held by the envelope guard at the entry's note-on level for the whole note (violas lost a +6 dB pp trim); finish releases inside the rest.
- 2026-11-17: a lock holder can stop without releasing (the finale held it idle 22:55-05:22); a waiter only sees it by the holder's own log going quiet.

## Cycle 19 (2026-11-17)
### Controllers and patches
- 2026-11-17: Hollywood Strings KS Master "Leg Slur MAX": the region volume of the "TLeg <pitch>" transition groups
  (celli, -2 dB) did not lower the legato join swell. On a range render the median moved +3.9 -> +3.5 dB and single
  joins moved ±2 dB (round-robin scatter). Together with c18's CC11 dip and Movement II's velocity test, three
  controls now leave the swell unchanged; none reaches it.
- 2026-11-17: 1FH KS Master: one legato transition (A4 to G sharp 4) holes 10-12 dB at +0.30-0.34 s at every velocity.
  The same target on "Sus MAX", 0.05 s early with the old note ended just before it, holes 1.6-3.4 dB and loses
  1-2 dB of body. A per-interval row change fixes a bad transition sample; velocity does not.
- 2026-11-17: CC1 6-10 units lower on the Clarinet KS Master's f-fff map moved the ff stem only 0.9 dB (a layer
  plateau, as the finale's c21 found). Use a level trim for balance there.
- 2026-11-17: "Sus Marc LITE" (1st Violins): -4 dB on the velocity 1-65 marcato short regions alone took the accented
  halves 2.7-3.8 dB down and left the theme's eighths and the sustain groups unchanged.
### Pipeline
- 2026-11-17: a rule that reads a note's row must read the row its keyswitch plays. REP_ROW changes only the keyswitch,
  so a "polyphonic rows only" overlap reached the clarinets' monophonic "Leg Slur Rep" and slurred 34 tongued notes
  (+30 ms late).
- 2026-11-17: at the scherzo's quarter 264 a 2-quarter note lasts 0.455 s. A 0.4 s minimum for the wind overlap caught
  the hemiola half notes and delayed them 30-180 ms. Overlap only notes of 0.6 s or more in a fast 3/4.
- 2026-11-17: RETONGUE_LEAD_CAP (0.3 x the previous note's written length) holds a re-tongue lead to 79 ms after a
  quarter at quarter 228. Lift the cap per note (RETONGUE_LEAD_CAP_AT) rather than raising the lead.
- 2026-11-17: a DOWNBOW_STROKE on a track with one legato row leaves the next slurred note on "Sus MAX" at re-bow
  velocity with no lead. Set that note's row (ART_AT) and legato velocity explicitly.
### Delivery at -14 LUFS
- 2026-11-17: a ride row that reaches its full cut on a printed ff arrival flattens that arrival on the mp3 (trio bar
  209: master +2.3 LU over the bar before, mp3 0.0). Start the ramp on the arrival and reach the cut a bar later
  (+1.2). Check every crescendo arrival on the mp3 after any ride row.
- 2026-11-17: top ride 2:1 instead of 2.5:1 at -14 LUFS raised LRA from 11.8 to 12.3 with the same limiter figures and
  climax order. The loudness loop landed -14.0 in 2 passes (one pass gave -14.2).
- 2026-11-17: a ride row on the bars before an fff downbeat could not give the downbeat a step on the momentary
  measure: the 400 ms window of the last bar's maximum is the downbeat itself.

## Cycle 20 (2026-11-17)
### Controllers and patches
- 2026-11-17: Hollywood Strings 1st Violins KS Master "Detache" for two slurred eighths (0.12 s each) inside a staccato line: 1 of 12 pairs held a note 10 dB or more under its detached neighbours, against 4 of 12 on "Sus MAX". The Detache groups have no MidiVelocity processor, so their level follows CC11 (4 thousand regions). On 2nd Violins it was no better than Sus MAX.
- 2026-11-17: "StacSl Leg BC + Slur + Port MAX" (Legato Slur Staccato) on the same pairs: the soft pairs sat 10-14 dB under and the f pairs 6-14 dB over their neighbours; 54 thousand regions. Not usable for level evenness.
- 2026-11-17: string legato swell, three more controls that failed on range tests: Violas "TLeg" region gain -6 dB (no fall, a 10.8 dB hole), celli LegatoSpeed RELEASE 443 -> 200 ms (inside the control scatter), "Sus MAX" on a long arrival (the swell went, but the slurred note before it collapsed 14 dB for its whole length).
- 2026-11-17: 2nd Violins "Stac RRx9" ships a 749 ms release on groups whose names carry no dynamic word; capped at 150 ms (`any_dyn`), repeated staccato eighths 114 ms apart dipped 3.3 dB instead of 0.4 (range test), 60 ms peaks -1.4 dB, master G.P. fall unchanged.
- 2026-11-17: a CC1 cap at the mf layer (51) on 1FH "Sus MAX" notes under a diminuendo lowered their 1.5-5 kHz share only 3.7-4.1 dB but their level 6.3-6.9 dB; the brightness gap to a slurred note before it (11-15 dB) stays.
- 2026-11-17: CC1 45 on the English horn KS Master (non-vibrato side) took the bloom swing of hemiola half notes from 8.5-13.4 to 1.7-6.9 dB at +0.1..+0.4 s.
- 2026-11-17: an extra 0.04 s lead on accented woodwind "Sus MAX" half notes after staccato eighths, with a +6 CC11 bump, raised the first-100 ms accent reading 1.8-2.4 dB (Flute 1, cor anglais).
- 2026-11-17: "Sus Marc LITE" on one accented ff Violins I half note (G6) did not lift it over its staccato neighbours (-3.7 -> -4.9 dB).
### Range renders
- 2026-11-17: a range render does not chase keyswitches or controller values from before its start: a "Leg Slur" keyswitch 45 qn before the range played the old row in every pass (identical numbers). Start each range before the last keyswitch of every track in it.
- 2026-11-17: notes in the first seconds of a short range (11 qn) read up to 18 dB apart between passes at the same start; control-to-control scatter on a 54 qn celli range was 0.7 dB on the join excess median and 0.9 dB on the body std. Use ranges of 10 s or more and judge notes after the first bars.
- 2026-11-17: `rpr.py run` waits 20 s by default; a 12 s range render at 1x takes longer and the client gives up while REAPER keeps rendering. Pass `--timeout 150`.
- 2026-11-17: about 25 track rebuilds over three range-test passes took REAPER to 52 GB (36 GB compressed); a restart settled it at 43 GB.

## Cycle 21 (2026-11-17)
### Controllers and patches
- 2026-11-17: 1st Violins KS Master "Detache" ships AHDSR releases of 5286 ms on its "1V mp" / "1V ff" groups, names that no dynamic-word release cap matches. On two slurred eighths (0.114 s each) in a staccato line its release ran under the next two notes: Dan heard the figure "blur together and overlap" (c20). A 150 ms cap plus a 0.09 s lead on the second note put that note's peak on the beat and lowered the landing note 3.6 dB, but soft pairs still decayed only 2.7-2.9 dB before the next note-on; the c19 "Sus MAX" pairs decayed 5.0-5.4 dB (range test). Read every row's group releases before adopting a row for a fast figure.
- 2026-11-17: a 150 ms release cap on 1st Violins "Staccatissimo RRx9" / "Stac RRx14" / "Spiccato RRx9" cut the peaks of notes written 40-80 ms long (p10 -6..-8 dB, median -1 dB): the cap ends samples whose attack peaks 70-100 ms after the note-on. The same cap on Violas "Stac RRx9" / "Staccatissimo RRx16" and 200 ms on celli / basses left peaks unchanged (median 0 / +1 / 0 dB) and halved the violas' 20 dB fall at a tutti stop (0.215 -> 0.105 s). Check note peaks, not only separation, after a release cap on a short row.
- 2026-11-17: Hollywood Strings "Leg Slur MAX" connected-sustain groups ("V1s ...", 841-1501 ms attacks): capping their attack at 400 / 250 ms on celli lowered the join swell 1.8 -> -0.1 / +0.1 dB, but by lowering the whole new note (body at 0.7-1.0 s -3.5 dB, sag 2-4 dB deeper, holes over 5 dB 8 -> 12 at 400). Not a fix; the fourth control on the swell that failed.
- 2026-11-17: oboe KS Master "Sus Accent MAX" at velocity 70-90 with no CC11 bump on four p accented half notes after staccatos: first 100 ms against the neighbours -3.8 -> -2.2 dB median, peak 0.29 -> 0.03 s after the beat, 2-5 kHz attack minus body -3.4..+1.0 dB. The same on the English horn was no better (one note -6 dB).
- 2026-11-17: Opus Stereo Double on a Close-only DIV B patch: spread 0.6 gave L/R correlation 0.78 and 1.3 dB of level loss; 0.4 gave 0.19 and a 2.3 dB mono loss (too wide). Spread is not linear in correlation.
- 2026-11-17: 1FH KS Master with "Mono From Left" removed: Close -6.3 + Mid 0 and Close -1.4 + Main -5.2 both kept the stem at correlation 0.94-0.97 (300 Hz-8 kHz) in the drone and the recall; the Main / Mid pairs of this patch add little width.
### Range renders
- 2026-11-17: a range render does not chase the keyswitch, and a track whose only keyswitch before the range is the pre-roll one plays whatever row it last played: render the pre-roll (-3 .. -0.3 qn) of those tracks first, then the range (`ranges21.sh` prime). A multi-track range has to start before every track's last keyswitch; split ranges per track rather than starting 100 qn early.
- 2026-11-17: memory reached 57 GB (41 GB compressed) after two batches of about 10 track rebuilds; a restart between batches brought it to 42 GB.
### Phrase shape
- 2026-11-17: the PHRASE_SHAPE "build" test (printed rise, or a crescendo in the last quarter) made 41 lyric or accompaniment phrases builds; a crescendo arrival within 1.5 s of the phrase end (`build_end_s`) and no rise test in lyric spans turned all 41 to lyric. Their crescendo rises were unchanged (the shape fades out inside hairpins), but the phrase ends fell 8-17 units, so the rule was limited to the trio (`build_rule_spans`).

## Cycle 22 (2026-11-17)
### Controllers and patches
- 2026-11-17: Hollywood Strings 1st Violins "Sus MAX", two slurred eighths (0.114 s) at CC11 54-73: a +16..+20 CC11 lift that stays on through the second note and steps back 0.1 qn before the landing note's note-on brought the pair to within 1-7 dB of its neighbours (was 7-17 dB under), but the second note, now on the mf groups with their slow attack, was still rising when the landing note started (decay before the next note-on 1.5 -> -4.2 dB). Ending the lift 0.06 qn after the second note's note-on (the group is chosen at the note-on; Opus then fades CC11 over 120 ms under the note) gave 4.1-5.5 -> 5.3-8.2 dB with the pair at -4..+2 dB. A lift that starts under the preceding staccato's release raises that tail (decay before the next note 3.8 -> -2.9 dB): start it after the release.
- 2026-11-17: the same pairs on "Sus Marc LITE" (the theme-head treatment, velocity by CC11 70-94, 0.09 s leads) reached their neighbours' level but decayed less before the landing note than on Sus MAX (bar 263 5.0 -> 0.0 dB).
- 2026-11-17: flute KS Master "Sus Accent MAX" (StacSs overlay; layers 1-74 / 75-114 / 115-127) at velocity 70 (CC11 under 80) / 90 with no CC11 bump on accented half notes after staccatos: first 100 ms against the neighbours -4.0 -> +3.2 dB (p) and -2.2 -> +0.4 dB (tutti), peak 0.30 -> 0.01-0.09 s after the beat. Oboe "Sus Accent MAX" at velocity 96 / 105 (middle layer) instead of 70 / 90: -2.4 -> +0.2 dB.
- 2026-11-17: 2nd Violins and Violas "Sus Marc LITE" (region gain -9 dB, soft layer -4, 120 ms cap) on accented tutti notes was negative on a range test: Violins II's accents read -47 / +49 dB against their neighbours at the hemiola, the violas' median -0.8 -> -2.8 dB. The finale's c24 found the same on held chords. 1st Violins is the only section where this row works here.
- 2026-11-17: 0.07 s of lead on the first of two same-pitch staccato eighths (1st Violins Staccatissimo / Stac RRx14, second at 0.045 s): separation median 4.5 -> 3.8 and 4.6 -> 5.1 dB on two ranges, p10 0.4 -> 0.8 / 3.1 -> 0.9: no measurable gain.
### Range renders
- 2026-11-17: a row change on two notes moves the round-robin position of every later note on the rows involved: an unchanged landing staccato read 4-11 dB apart between passes from the same start (bar 42's unchanged pair 5.2 / 2.0 / 5.2 dB decay in three passes). Judge a change on the notes it changes and on several occurrences, not on one neighbour.
### Hairpins
- 2026-11-17: a crescendo whose stop is printed one beat before the next dynamic (p < ... | ff) stays at one hairpin step and jumps at the mark (flute +46 CC11 units, +11 dB). `HP_TARGET_LOOKAHEAD_QN` (2.5 qn here, only when the gap is at most half the hairpin) takes the mark as the target; two hairpins in the movement matched.
### Delivery
- 2026-11-17: on this master the -9 dB 3:1 peak compressor before the limiter decided the climax margin: with it the summit took 2.7 dB of limiting and led every rival tutti by 0.6-0.7 LU (f -> ff 2.2 LU, LRA 10.6); without it, the same rides gave 9.7 dB of limiting at the summit and a 0.4 LU lead (LRA 12.3). The scherzo's summit crests come from the summed strings plus hall (+1 to +4 dBFS pre-limiter), unlike the finale, which met the spec without the compressor.

## Cycle 23 (2026-11-17)
### Controllers and patches
- 2026-11-17: Hollywood Strings 1st Violins "Sus MAX", two slurred eighths at CC11 56-63: a CC1 floor of 108 (Molto Vib) made the second note 3.5 dB louder than its staccato neighbours, and it was still rising when the landing note started (decay before the next note-on -1.9 dB). On fast figures CC1 adds level and also slows the attack.
- 2026-11-17: the same pair with 0.10 s of lead on both notes, each ending 0.03 s before the next moved note-on: decay before the landing note 1.5 -> 6.6 / 7.1 dB (two passes), pair 4-9 dB nearer its neighbours. The earlier first note sat in the preceding staccato's ring (decay 3.8 -> 1.1 dB). On loud pairs (CC11 92) the same lead cut the second note's decay 2.0 -> 0.4 dB: lead helps soft, slow-speaking pairs only.
- 2026-11-17: a 150 ms release cap on the 1st Violins "Sus MAX" p groups had no measurable effect on two slurred eighths (decay 1.5 -> 1.4 dB).
- 2026-11-17: 1st Violins short rows, note-off moved after the attack peak (0.094 s sounding) plus a 150 ms any_dyn release cap: 60 ms peaks still fell 5-20 dB. The cap cuts these samples whatever the note length. The short rows' extra group (721 ms attack, 1000 ms release) is caught by any_dyn as well.
- 2026-11-17: 2nd Violins "Marc Lng RRx4" on f / ff accents (velocity 80 / 100, no lead): accents read 12-52 dB under their neighbours, and the staccatos after them lost 20 dB of peak. Not usable as a per-note row switch in a staccato line.
- 2026-11-17: English horn "Sus Accent MAX" (overlay 1-109 / 110-127) at velocity 90 and Clarinet "Sus Accent" (1-60 / 61-96 / 97-116 / 117-127) at 90 on ff tutti half notes were no better than Sus MAX / Leg Slur Rep (-1.2 / -2.3 dB). The oboe's middle layer worked (+1.3 dB, peak 0.27 -> 0.18 s).
- 2026-11-17: flute "Sus Accent MAX" overlay vel>=75 -3 dB plus a G6 -3.5 dB region gain took tutti accents 2-4 dB under their neighbours. Half of each was right. The overlay carries most of the first 100 ms.
### Pipeline
- 2026-11-17: CC11_ADD_SPANS is applied before CC11_REST_MAP, so an add cannot lift a woodwind or string above the map's top (108 here): a +20 ramp toward ff raised the stem 0.1-0.4 dB. A hairpin gain that no note sounds 0.25 s past its release is never converted by HP_GAIN_TO_CC11, so `max_arrival_cc` does nothing for it.
- 2026-11-17: rr23's keyswitch check refuses many multi-track wind ranges in the scherzo (each wind's last keyswitch lies 50-130 qn before its next note). One range per track with its own start works.
- 2026-11-17: `cat >> /dev/null` in a compound shell command waits on stdin and hangs the step; the ranges did not run.
### Delivery
- 2026-11-17: the -60 LUFS room-noise bed after the limiter changed none of I, TP, LRA, p10, the climax order or the G.P. drop at +0.3 s (18.9 dB) on the scherzo mp3. Only a late-slope fit down to -55 dB reaches it.

## Cycle 24 (2026-11-17)
### Volume envelope
- 2026-11-17: a guard that reads only parts.json vol_db, or that exempts printed hairpins and the windows after printed marks, misses most steps inside notes: on the envelope REAPER gets (build_reaper vol_points: roles + dynamic trims + holds + note_move_guard) 175 notes held a step of 1.5 dB or more at over 6 dB/s, and 205 a change of 1.5 dB or more in their first 0.35 s; the c17-c23 guard listed 9. Most were dynamic-trim steps at printed marks keyed to the score onset of led notes, the trims following an sfp's spike shape, and role edges.
- 2026-11-17: a generic rate limit inside sounding stretches (build_reaper `note_slew`: notes less than 5 ms apart make one stretch; a backward pass so each move ends at its written time and starts earlier; a stretch after a rest takes its first value in that rest) at 4 dB/s took both counts to 0. 236 notes moved 1 dB or more somewhere inside; the written level at a printed hairpin's end was kept except at 23 of 237 hairpins (a step just after the hairpin, anticipated). The largest change: a p < f crescendo of 0.6 s on the trombones and tuba, whose trim table falls 15 dB against the crescendo, now enters 10 dB lower and reaches the written f level on time.
- 2026-11-17: roles.json's optional fourth value is an end-ramp length in qn, not an end level: [a, b, 3.2, -3.8] is not a ramp from 3.2 to -3.8 dB.
- 2026-11-17: 17 of 31 trim tables are U-shaped (falling from pp to f, rising again to ff: trombones 14.6 -> -0.9 -> 0.8 dB, Oboe 1 7 -> 3.1 -> 7.2), so on a held note the trim moves against a crescendo up to f and with it above f.
### Patches
- 2026-11-17: every 1st Violins KS Master short row ("Staccatissimo RRx9", "Stac RRx14", "Stac On Bow RRx9") carries one group with no start mode beside its RoundRobin groups (721-733 ms attack, 1000 ms release). Switched off in the Opus state, no note was lost (166 notes on three ranges, settled renders) and the tail of isolated staccato quarters at +0.5 s after the peak fell from -44..-50 to -66..-93 dB; same-pitch separation 3.0 -> 6.7 dB (bars 16-44, together with the Spiccato pitches).
- 2026-11-17: 1st Violins same-pitch staccato eighths on D5 / D sharp 5 / F sharp 5 blurred on every short row (0.8 / 4.3 / -0.4 dB); on "Spiccato RRx9" they separate by 5.7 / 9.2 / 5.1 dB with 60 ms peaks 5-9 dB higher. The blur is per pitch, not per row or velocity: route by pitch before trying caps.
- 2026-11-17: the 1st Violins hemiola accents lose no CC11 bump to a crescendo cap: they play "Sus Marc LITE", which ACCENT_CC skips as a row with its own accent; Violins II's bump is the configured 2 units below loud_cc 98.
### Range renders
- 2026-11-17: range renders made within a minute of a rebuild, after one 5 s discard, lost 1-10 notes each (-130 dB, on rows the change did not touch, Spiccato included); after the memory settled (129 s) and two discards, the same state lost none and two passes were identical to the decimal. Wait for memory to settle after every rebuild, and count missing notes before reading any range measure.
- 2026-11-17: zsh does not word-split `${@:-R1 R8 R2}`: with no arguments the loop ran once with the whole string as one range name. Pass the ranges explicitly.
- 2026-11-18: the rate limit and passage levels pull against each other: with no cap on how far back a ramp may start, 0 notes failed but 56 track-bars changed their mean level by more than 1.5 dB (moves up to 7 qn); a 2 qn cap left 25 + 64 notes failing and 16 track-bars over 1.5 dB. A step that is joined on both sides has to leave the envelope (CC7, or a rest), not be ramped.
- 2026-11-18: anticipating a pp trim rise across a joined sub. p (celli 828) lifted the forte bar before it by 4.7 dB: never let a rate limit pull a later, softer section's trim into an earlier, louder one.
### Delivery
- 2026-11-18: the scherzo's c23 bed and Movement I's c62 bed differed in seeds, low-cut slope, normalisation and whether the final fade takes the bed; neither difference moved I, LRA or TP on the c23 master. Copy the function, not the description.

## c25 (2026-11-18)
### Opus / Hollywood Orchestra controllers
- 2026-11-18 (c25): CC7 follows 20·log10(CC7/127) on the HO woodwind and brass KS Masters and on the HS string KS Masters alike (range test: Clarinet 1 CC7 44-127, Horn 1 95-127, violas 51-127; per-bar level against the same data with the trims in the envelope, median +0.00 / +0.01 / +0.01 dB, no bar over 1 dB). A track with no CC7 lane plays as CC7 127. The dynamic trims can move from the post-hall envelope into CC7 with no level change.
- 2026-11-18 (c25): the 1st Violins KS Master's "Spiccato RRx9" row has four velocity layers, v1-54 / 55-89 / 90-114 / 115-127 (load_oib). A `row_dyn_db` "vel>=N" cut acts on whole regions, so N must be a layer boundary (80 would miss every note at v80-89). Moving notes 13 velocity steps down into the 1-54 layer and cutting that layer by 2 dB lowered them by 2.6-5.2 dB against their neighbours (two passages); 10 steps alone gave 1.4 dB.
### Pipeline / measurement
- 2026-11-18 (c25): with the trims as a CC7 lane, the volume envelope of a soft-trimmed brass track (gain + vol_db + largest trim) can pass REAPER's +24 dB envelope range (trombones +28): cap it (23 dB here) and leave the rest of the softest trim in the envelope.
- 2026-11-18 (c25): reading the trims on moved time needs only the dynamic curve's anchors (marks, hairpin starts and ends) moved to the led note's moved note-on; a piecewise-linear warp between them keeps hairpin shapes. With note_move_guard and note_slew unchanged, the guard's fader steps inside notes fell 25 -> 12 and first-0.35 s changes 64 -> 30 from this alone; hairpin ramps started at the moved onset took them to 10 / 9.
- 2026-11-18 (c25): holding a hairpin gain to the end of the note sounding across its hold end must require a rest after that note: otherwise the release lands inside the next joined note, note_move_guard holds it there, and whole bars rise (a 4 dB bar in a test build).
- 2026-11-18 (c25): a range render from score qn -3 starts at project time 0, and the 3 qn pre-roll runs at 60 bpm (3.0 s), not at the first tempo: measurement scripts that map qn -> s with the score tempo map put every note 2.3 s off.
- 2026-11-18 (c25): in a 3/4 movement at quarter 264, the delivery LRA moved 0.1-0.2 LU for a 0.5 dB change of a 12-bar quiet-passage ride lift; the fugato lifts were the cheapest place to win back the spec's last 0.1 LU (p10 short-term moved only 0.2 LU).

## c26 (2026-11-18)
### Opus / Hollywood Orchestra patches
- 2026-11-18 (c26): HO woodwind KS Masters' legato rows (FL / FL2 / OB "Leg Slur MAX", CL "Leg Slur Rep"): sustain groups ship 177-237 ms releases, the transitions ("TLeg <pitch>", no dynamic word) 177-237 ms, and the release trails (one-shot, chosen by CC11 range: pp 0-55, mf 56-93, f 94-127) 1000-1245 ms. On a slurred eighth before a staccato at quarter 264 (f tutti), a 120 ms cap on the f sustain groups and every TLeg group plus the f trails at -6 dB moved the old pitch 70 ms after the staccato's note-on from -9..-6 to about 0..+5 dB over it on Flute 1 (range test); ending the slurred note 35 ms before the staccato's moved note-on as well gave +12..+31 dB on all four winds, with every legato join's first 60 ms unchanged.
- 2026-11-18 (c26): HS 2nd Violins and Violas "Sus Marc LITE" on a single fff downbeat (v92, lead 0.085 s, CC11 already at its ff resting value) plus a CC11 counter-shape (-10 units over the held note's second and third beats) moved the strings' 10 ms peak from +0.41..+0.52 s to +0.08..+0.13 s after the downbeat (range test). c22's negative result for these rows was on accented notes inside a running line, not on a fresh chord stroke.
### Pipeline
- 2026-11-18 (c26): the post-hall envelope's moves inside sounding stretches can all go into CC7 without changing the level heard: give each stretch (notes less than 5 ms apart, here up to 16 qn) one envelope level, its highest, and let CC7 carry the difference. Net level against the old envelope: p99 0.1-0.3 dB per track (CC7 quantisation); the fixed guard went 9 + 9 notes -> 0 + 0. Four things were needed: apply it after any rate limit or guard on the envelope (otherwise they pull the stretch-end step back into the note: 7 dB errors), resample envelope ramps into CC7 every 10 ms (CC7 is a step lane, the envelope is linear between points), pin the stretch's level with an explicit point at the note end (a grid point at the end belongs to the rest), and start the next stretch's level 2 ms after it.
- 2026-11-18 (c26): an accent's CC11 bump keyed to the score onset starts after the moved note-on of a led note; starting it 0.06 s before the moved note-on, with a CC11 body dip (-8 units from +0.22 to +0.36 s), took the 1st Violins accents' front minus body from -0.7 to +0.6 dB and their peak from 0.34 to 0.18 s after the beat (2nd Violins 0.27 -> 0.23 s, cor anglais 0.24 -> 0.19 s), but the accents still read 0.2-3.6 dB under their neighbours in the first 100 ms.
- 2026-11-18 (c26): a hairpin gain held to the end of a sounding note (HP_HOLD_TO_NOTE_END) must skip notes under a printed decrescendo: 6 of 32 holds sat there and took 3-9 dB out of the decrescendos.

## c27 (2026-11-18)
### Opus / Hollywood Orchestra patches and controllers
- 2026-11-18 (c27): HS 1st Violins "Sus Marc LITE" at soft velocities (v56-64, the marcato overlay's 1-65 layer): a -4 dB extra cut on that layer (vel<66 -8 total with the row's -8) took the head's first 100 ms from +3.0 to -2.1 dB over its unaccented neighbours and the 2-5 kHz front from +7.3 to +2.5 dB (range test, 4 heads): about 1.2 dB of front per dB of layer cut. With -2 dB extra (vel<66 -6, adopted) the full render read -0.9 dB front and +3.3 dB 2-5 kHz over the neighbours (9 heads).
- 2026-11-18 (c27): a CC11 lift of +14 units 0.10-0.22 s after a soft marcato head did not fill the hole behind the spike (0.21-0.39 s mean unchanged, lowest 30 ms +1.5 dB): Opus's CC11 smoothing and the sustain layer sitting 16+ dB under the marcato leave too little to lift in 0.2 s.
- 2026-11-18 (c27): HS soft legato heads after a rest (CC11 31-60): CC11 +10 from 0.06 s before the moved note-on, held to +0.25 s, gone by +0.45 s (finale technique 139) moved the -6 dB point of 11 heads from +92..+295 ms to -22..+198 ms (median 213 -> 131 ms) with peaks within 1 dB, except a head that was not late (celli 564, CC11 46: +5.1 dB peak): apply it to listed heads or skip the on-time ones.
- 2026-11-18 (c27): HS Violas "Staccatissimo RRx16" double stops v95 -> v82 lowered beats 2-3 by 5.2 dB (range test): a layer step, more than the 2-4 dB a velocity move of 13 suggests.
- 2026-11-18 (c27): HS celli pizzicato round robins after a CC36/CC16 reset play in a fixed level order (-48.4 / -45.8 / -49.9 dB at the same velocity, three samples, two renders): a reset one note before a downbeat puts the loudest sample on it. The basses' order (-50.2 / -48.6 / -51.8) gave no position a gain over the reset-at-head layout.
### Pipeline / measurement
- 2026-11-18 (c27): holding a crescendo gain "until the next printed mark" moves balance: with a 16 qn cap the trio climax celli sat +5.4 dB over the previous render for 13 qn. A cap of 8 qn plus a release in the next rest or at the next re-attack (a step at its note-on) kept the arrivals whole and cut the net in-note moves outside hairpins 70 -> 48 (net counter, 60 ms after the note-on to 25 ms before the next one).
- 2026-11-18 (c27): the CC7 trim lane is read through the moved-time warp (trim_at(W(q))); a hold or release placed at a moved position must be converted with W, or it lands up to one lead (0.45 qn on the violas at 632) early, inside the note before.
- 2026-11-18 (c27): extending a unison-boost span to the next rest carries the boost onto notes that are not doubled (Horn 4 912: +3 dB for 8 qn); end it in a rest within a few qn, otherwise as a step at the next note's moved note-on.
- 2026-11-18 (c27): a soft-head CC11 shape on a window / split track (solo violin, Violas div) must skip the window's first note: before it the lane follows the source part's curve (CC11 112-117, 10 ms before the note-on's 51).
- 2026-11-18 (c27): removing 0.04-0.05 s of accent lead in the tutti moved the accent onsets (-6 dB point) from -31 / -55 ms to +33 / -11 ms (Violins I / cor anglais) and lowered their first 100 ms over the neighbours by 1-2.4 dB: a measure of the first 100 ms from the beat rewards early attacks; judge accent timing and weight separately.

## c28 (2026-11-18)
### Opus / Hollywood Orchestra patches and controllers
- 2026-11-18 (c28): for f tenuto quarters at quarter 264 (0.227 s), HS Basses "Marc Lng RRx4" and HB trombone / tuba "Portato" are no faster than "Sus MAX" (range test, same CC): peaks +155..+190 ms against +120..+185, the -6 dB point 35-90 ms later once the Sus MAX lead is gone, the trombones / bass trombone 5.4-6.6 dB softer, the bass downbeat over beats 2-3 +1.5 -> +0.3 dB. The downbeat weight of a fast tutti does not come from these rows.
- 2026-11-18 (c28): "Timpani Hrd KS" has the felt patch's rows, keys and group layout; its stroke layers (Lng: ... 65-69, 70-74, 75-84 ...) play +1.9..+5.6 dB louder than felt at v50-69 and 1.0-3.2 dB softer at v70-109, with the 1-5 kHz share of the first 50 ms +9..+20 dB at soft velocities but only +1..+3 dB at loud ones; rolls (CC1) +1.4 dB. A per-layer region gain (vel<70 -2, vel>=70 +2, roll row -1.5) matched the felt levels within 1 dB.
- 2026-11-18 (c28): HS 1st Violins "Sus Marc LITE" eighths at v62 (the marcato overlay's 1-65 layer) instead of v78-94: 2-5 kHz front over the neighbouring staccato +5.6 -> -0.1 dB, level -3 dB; the gap between two such eighths is unchanged (the row has no legato join).
### Pipeline / measurement
- 2026-11-18 (c28): a pitch-based row reroute meant for same-pitch pairs also caught single notes (a slur-end landing fell 2.5 dB under the slurred note before it); limit such rules to the pairs they were measured on.
- 2026-11-18 (c28): an arrival hold that stops at the first 0.5 qn gap releases inside fast staccato textures (the first bar of the ff tutti); stopping only at rests of 2 qn or more and holding to the next printed decrescendo cut the 1.5 dB+ arrival sags 35 -> 7. In this 3/4 Allegro the cost is long plateaus (trio celli +5.4 dB for 14 qn) that need a listener's verdict.
- 2026-11-18 (c28): dropping a crescendo's gain where it arrives at an ff tutti (so the hold cannot lift the tutti) lowers the crescendo's last bar by 0.6-0.9 LU on the mp3; the shared spec's f -> ff measure counts those bars as ff (2.10 -> 1.77 LU).
- 2026-11-18 (c28): NOTE_END_AT cannot overlap a note past the next moved onset (clipped to onset - 0.02 qn); an overlap needs another rule.
- 2026-11-18 (c28): a single-note arrival weight replaced by a passage level of 2.5 dB over the fff bars raised the summit lead on the mp3 only +0.1 LU (+0.57 -> +0.67) and lowered the 0.5 qn step +1.4 -> +1.1 dB: the -14 LUFS normalisation and the limiter (3.3 -> 3.7 dB on the summit) take most of a summit-only lift.

## c29 (2026-11-18)
### Opus / Hollywood Orchestra patches and controllers
- 2026-11-18 (c29): HB trombone / tuba / horn "Sus Accent MAX" at v70 (manual p.100: velocity sets the attack) on ff tenuto quarters at quarter 264 played a darker, later swell than "Sus MAX": peak +185..+195 ms against +165, -6 dB point +55..+90 ms against +25, 2-5 kHz front minus body -11..-18 dB against -4..-6. At soft-to-mid velocities the accent overlay adds no front.
- 2026-11-18 (c29): HS Basses "Marc Sus LITE" at v80 on f tenutos: peak +180 ms against +128 on Sus MAX and +4 dB level; no faster than Sus MAX.
- 2026-11-18 (c29): ending a Sus MAX tenuto quarter 0.15 qn (34 ms) before the next beat, so the KS release falls in the rest, raised the low group's downbeat over beats 2-3 from +2.0 to +3.9 dB without changing its attack shape; the master gained only +0.4..+0.6 dB because strings and woodwinds fill beats 2-3.
- 2026-11-18 (c29): HO "Mono From Left" channel routing changes level by pitch, not by a constant: switching a horn back to Stereo moved its level +3.4..+3.8 dB on most pitches and -2.9..-3.7 dB on the one pitch it was set for (the left channel was louder there). Refit the gain and that pitch's region gain separately.
- 2026-11-18 (c29): HS Violas "Staccatissimo RRx16" v82 -> v88 changed nothing (+0.5 dB); v92 +5.3 dB: the layer boundary lies between 88 and 92.
### Pipeline / measurement
- 2026-11-18 (c29): a printed stick change that one instance cannot follow fits the second render pass: a windowed alias on the felt patch (one timpani instance and one return, 1.2 GB) reproduced the felt 1-5 kHz shares of c18 within 0.3 dB while the source's notes, CC1 and envelope stayed identical inside the windows.
- 2026-11-18 (c29): an alias built on another patch inherits the source's mix entry only by name; give it its own mix.json entry (copied from the state the tables were fitted on) and add it to every track-name list (`soft_trim_db._except`, `note_slew.skip_tracks`, analysis scripts that skip the source by name).
- 2026-11-18 (c29): a non-legato note that follows the previous note's written end with no rest gets no lead from any branch (0 lead after an ART_SPANS row change from legato to Sus); give it REATTACK_LEAD_AT explicitly.
- 2026-11-18 (c29): a fixed harmonics 2-5 band reads upward leaps of a fourth or more as unclean crossovers (shared partials, E6's band above a flute's strong partials); harmonics 1-3 for leaps of 5+ semitones gave 0 crossovers under +3 dB on all four woodwinds in two renders, where the 2-5 band gave 3-5 per track varying with round robins.
- 2026-11-18 (c29): a CC7 passage lift on a line already at CC7 127 (the build's cap warning) should be a volume-envelope passage row with edges in rests instead.

## c30 (2026-11-18)
### Opus / Hollywood Orchestra patches and controllers
- 2026-11-18 (c30): in a fast 3/4 (quarter 264, 0.227 s) a "Leg Slur MAX" target after a quarter cannot be led enough to arrive on its beat: the lead (0.22 s) puts its note-on 0.04 qn after the quarter's own note-on, the pitch crossover measured -316 ms (the new pitch's band over the old one before the old note began) and the new pitch's attack was still +38..+107 ms late; the quarter was never heard (Dan: "the strings overlapping slur together really bad"). The same notes as fresh "Sus MAX" heads: crossover +4..+68 ms after the beat, the quarter sounds its value; HS Sus MAX f heads need a 0.10-0.18 s lead (perceived attack +61..+143 ms at 0.06 s).
- 2026-11-18 (c30): HB horn CC11 is far from linear at the soft end: c17's +5 units = +1.1 dB at CC11 about 35, Movement I's 0.55-0.61 dB per unit at 46-58. Replacing a fader row with CC11 needs a render check.
### Pipeline / measurement
- 2026-11-18 (c30): check legato joins with `pcx.py` (pitch crossover re the score onset) on every fast slurred passage, not only on the theme: a crossover far before the beat (more than the lead) means the previous note was swallowed, a late perceived attack means the old pitch lasts into the beat. Both survive envelope and CC work unchanged for many cycles (here c16-c29).
- 2026-11-18 (c30): unison-boost role runs split where the unison count changes (two players, then three on one note); the two spans' rest-placed edges overlapped and summed inside the notes (+4.8 dB swells). Merge adjacent runs whatever their boost (`UNI_RUN_MERGE_VALUES`); widening the merge gap instead (3 qn) filled the boost into other tracks' rests.
- 2026-11-18 (c30): a role edge moved onto a led note's score onset is pinned only when the row is not chained to its neighbour (rows that meet crossfade over [a - 0.1, a + 0.15] around the score onset, after a 0.2 s lead): `ROLE_EDGE_MOVED_CHAINED_AT` pins chained edges too. The CC7 lane's own point grid still leaves about 1.5-2 dB of a 6 dB step in the first 50 ms.
- 2026-11-18 (c30): a CC11 change shifts the lead rules that read CC11 (a horn note-on moved 1100.772 -> 1100.81 after +6 units); pin the lead (LEAD_SET_AT) when LEVEL_SHAPES rows depend on the moved onset.
- 2026-11-18 (c30): the delivery's momentary cap at knee + 3 dB put exposed p / pp solos at the level of the f passages on the mp3 (horn call -10.3 LUFS momentary against the f hemiola -11.3); cap 0 plus three -2 dB ride rows lowered them 2-3 LU with every spec item still passing (p10 -21.1).
- 2026-11-18 (c30): a range render plays the tracks and leaves their Opus states stale (7 tracks after 4 ranges); a build sent while REAPER is still busy after the ranges fails ("bridge not running"). Restart, wait for memory, then build every track fully before the render.
