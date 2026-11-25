# Coordinator notes for cycle 54 (critics and actor read this first)

Under review: cycles/c53/. Read cycles/c53/CHANGES.md, including its addendum.

## Facts about the c53 render that change how to measure it
1. **Seventeen stems carry level corrections applied after the render** (`tools/stem_fix.py --apply`, once), and the master was summed again. The stems as rendered are in cycles/c53/render_first/. The four return stems were not re-simulated, so a wet/dry ratio on a corrected stem is off by the correction. The rows are in build/ and reach REAPER with the next full build.
2. **The delivered mp3 was re-made** with the 3 kHz delivery shelf at -1.3 dB (addendum in CHANGES.md). cycles/c53/mvt1-mockup-c53-shelf10.mp3 is the earlier file.
3. **Sampler variation.** With unchanged data and a clean state guard, single notes move 2-6.7 dB between renders (finale c12, 12 of 31 tracks; medians 0.00 dB). Report a level change on unchanged data only when a run of consecutive notes or a bar median moves.
4. **Time maps.** In c53 critic C reported horn and double-bass sound at bars 25 and 137 beat 2 starting 0.3-0.45 s late. The actor found onsets within 13 ms of the mapped note-ons: the error was in the critic's own time map. Take score-qn-to-seconds from build/parts.json (its tempo map and each note's moved note-on, including leads), not from a map rebuilt from printed tempos. Check any timing finding over 100 ms a second way on the stem before reporting it.
5. **Onset measures.** pcx reads swelling notes late or early; the c53 actor found Flute 2 minus Flute 1 "over 50 ms" on 5 of 28 shared onsets by pcx while band envelopes read them on time. Use a band-envelope measure beside pcx on soft or swelling attacks.

## Open items from c53 (critics: confirm or reject with a measurement; actor: fix what is confirmed)
- Cor anglais at qn 275: +158 ms late in c52, -84 ms early in c53 (overcorrected; a value fitted on a range render did not carry to the full render). Proposed: reduce its `retongue_leads` entry from +0.06 toward +0.02 and verify on a full render.
- Oboe 1 at qn 582: -52 ms after the clamp-order fix.
- Four Lento re-bow rows still over the limits: celli 12.163 (stem 3.9 dB), basses 47 (stem 3.8), celli 21.442 (master 3.4), basses 26.003 (master 4.8).
- Brass tail 0.3-0.6 s after cut-offs is still 6.1-12.3 dB under the strings' tail at bars 31 / 82 / 169 after the half step on R Brass. The master is drier than c49 at all five clean tutti stops. Decision: the half step stays. No further return raise unless a critic shows the brass reads as a different room by a measure other than this ratio; BRIEF S4 stays in force. Bar-14 horn ending went from 0.425 s to 0.48 s to -20 dB; say whether that is audible as too long.
- Trumpets 1-3 release: `rt_gain_db` acts only from 0.3 s after the note end, so it cannot fix the first 180 ms. Not applied. Any other proposal needs a range test.
- Oboe 1's front at qn 160 came out 3 dB lower than c52 on unchanged notes (possibly item 3 above).
- Double basses pizzicato at 704-712 differs from c50 but equals c52.
- First of the four bar-30 staccato notes against Violins I was not verified.
- Stops at bars 71 and 141 are 1.0 dB wetter than c49; they are not clean stops. Say whether they should count.
- CC1 floor of 64 on held Oboe 1/2 and Flute 2 notes gave +2.3 dB in a range test; not shipped. Decide with a measurement whether it is needed after the level shapes.
- Finale item 18 on the Double basses (bars 27-31, 131-134, 140-142): not done.

## State guard (actor)
The legato attack value is a runtime value of the Opus instance; the save stores whatever it holds when playback stops. c53: 0 stale before each render, 1 and 2 stale in the saves after the renders, audio unaffected (Horn 1 against c52: 46 joins, +0.0 ms, 0.00 dB). Run state_guard.py before each render and on each post-render save, rebuild stale tracks in full, and read 0 before the next load. Wait 45 s after a restart, a full rebuild or creating a track before any render. Never render into a folder that already holds files.

## Techniques from the other movements not yet tried here
/private/tmp/claude-501/-Users-gooby-sandbox-claude-composes/14e09066-475e-46e9-9cac-174084980a38/scratchpad/c54-actor-notes.md (finale c12 items 24-33 with the Movement I places to measure).

## PRIORITY 1 (Dan, 2026-11-10): the string theme at rehearsal A is choppy and not in steady time
Dan's words: "in movement 1 the main theme that comes in at rehearsal mark A, the melody in the strings feels choppy and doesn't feel like it's really playing in perfect time/rhythm". This outranks every other item in c54. The score is not the cause (tOne.ily bars 15-23 are plain eighths, quarters and dotted quarters at 126, no tempo marks).

Measurement (coordinator, `cycles/c54/coordinator_scripts/theme_onsets.py c53 "Violins I" 56 90`, output beside it): the time each note becomes the dominant pitch in the Violins I stem, against the score beat on the parts.json tempo map (no pre-roll in the stems). An eighth at 126 is 238 ms.
1. **Onsets scatter**: -99 to +114 ms around the beat, sd 48 ms, 15 of 39 found notes more than 40 ms from the median (+26 ms). The note-ons are moved early by a separately fitted amount per note (0 to -220 ms: leg_leads, slur_head_leads, group_leads, retongue_leads, stac_leads, lead_short) and the fitted values do not match what the patch does in this line. Examples: bar 20 beats 1.5 and 2 sound +108 and +114 ms; bar 23 beat 1 sounds -99 ms; bar 18 beat 2 -65 ms; bar 16 beat 3 +98 ms.
2. **Swallowed notes**: three notes never become the sounding pitch (the pickups g' at bar 15 beat 1.5 and bar 17 beat 1.5, and the downbeat c'' of bar 16: the c'' eighth before it is 0.077 qn = 37 ms long in the MIDI and the next note-on is 151 ms early, so the two C's sound as one 630 ms note and bar 16 has no downbeat articulation; the score has c''8 slurred to c''4-- which needs a re-articulation). Five more sound for only 60-120 ms and 8-16 dB under their neighbours (bar 15 beat 4 d-flat'', bar 16 beat 4.5 g', bar 18 beat 1 b', bar 21 beat 4.5, bar 23 beat 3). Peak levels of adjacent notes run from -30 to -48 dB.
3. **Tempo steps that are not printed** inside the theme, from PHRASE_ARCS (56, 72, "sub"), (72, 88) and TEMPO_PUSH (88, 100): 126 → 121 for bar 17 beat 2, 123 / 120 / 122 / 128 over bar 18 beat 3 to bar 19 beat 2, 123 for one beat in bar 20, 121 / 116 on bar 22 beats 3-4, then 128.

Decisions for the actor:
- Remove the phrase arcs and tempo push over qn 56-100 so the theme runs at a constant 126 (keep the printed poco rit. later). Do the same for the theme's return in the recapitulation (find its qn span; the arcs near 488-504 and TEMPO_PUSH 552-564 are candidates) and say which spans you changed. Leave arcs in the Lento and in lyrical second-theme passages alone.
- Refit Violins I note starts over bars 15-32 on a render so that every note's sounding onset is within ±25 ms of the beat (one common offset is fine); iterate with range renders under the range-render rules, then verify on the full render with the same script. Target: sd under 20 ms, 0 notes over 40 ms from the median.
- Every printed note must sound: at least 60% of its printed length as the dominant pitch, and no eighth more than 6 dB under the eighths beside it unless a hairpin says so. The repeated c'' across the bar 15-16 barline gets a real re-articulation (not a 37 ms stub). If the legato patch cannot give even eighths at this tempo, test the line on a sustain/marcato articulation with overlaps, or the short-legato path, and take whichever measures steadier; report both sets of numbers.
- Run the same script on Violins II, Violas, Violoncellos and any wind doubling the theme in bars 15-32 and on the recapitulation of the theme, and fix what fails the same limits. Check ensemble: the melody's onsets against the accompaniment's beat (celli half notes, Violins II/Violas).
- Report before/after tables for these measures at the top of CHANGES.md.

## Coordinator decisions on the c54 critic reports (actor: this order)
0. **Priority 1 above (Dan's theme at rehearsal A)** comes first and may take most of the cycle. Critic C's overall figure agrees with it: string per-note spread 43-56 ms robust SD, 21-28 % over 60 ms, unchanged since c47; legato notes after a Sus-row note are the worst (SD 82 ms). If time is short, drop items from the bottom of this list, not from priority 1.
1. C #2 Violins I qn 128 (printed C6 reaches level 210 ms late): add 128.0 to DOWNBOW_STROKE_AT. Yes.
2. C #5 string legato after Sus-row notes: apply C's nine SHORT_SUS_AT rows where they fall in thematic lines; inside bars 15-32 use whatever priority 1 finds steadier.
3. C #1 slur-start joins in winds/brass (two pitches together for a median 140 ms): range test first; apply `head_end_s` 0.03 and SOST_JOIN_LEAD_S 0.07 only if the test confirms. Cor anglais 275: A and C both confirm early by 40-65 ms. Take C's fix (delete the row) if the join change ships, otherwise A's (+0.06 → +0.02). Verify on the full render.
4. C #3 wind entry leads that play early (Bassoon 1 14 of 14 at 91-115 ms, Contrabassoon, Oboe 2 44/520/664, Flute 2 100/160/548): apply C's ENTRY_LEAD_S values and entry_leads.json rows.
5. A #1 cor anglais solo qn 26 (A-flat 6-8 dB under for 340 ms, master dip 5.6 dB): apply. A #2 final chord basses 712-728 (re-bow steps up to 10.7 dB): RR_RESET_AT 712.0 and refit the six fills; verify on the full render.
6. B #1 celli covering the tune (bars 25, 31, 40, 132, 140): apply the note trims and shapes as given, but keep the theme-over-celli margin from c53 (median +5.47 dB, 0 quarters under) as a check. B #2 bass clarinet pedal 464-492 -5 dB: yes. B #3 Oboe 1 pitch trims 77/79/80: yes. B #4 basses E2 +4 and the pizzicato resets: yes if the resets do not disturb A #2's fit (do both together).
7. A #3 first bar-30 staccato of Violins I 60-80 ms early: fix with the smallest change that works (a row in an existing lead table is preferred to a tool addition). A #5 Flute 1 115.5 breath gap: yes.
8. C #4 bar 152 32nd run, A #6 three join holes, B #5 timpani 532-536, C's wind hang at tutti stops: only if time allows; otherwise list as open.
Closed, no action: Oboe 1 582; Oboe 1 front at 160 (sampler variation); CC1 floor 64 (rejected by B); basses 704-712 vs c50 (covered by A #2); bar-14 horn ending (not too long); the four Lento re-bow rows (two are the cor anglais item, two read 2.7 dB on the master). Brass tail: half step stays, no return change. Finale item 18 on the basses stays open.
The 17 stem-fix rows of c53 are in build/ and must come out of REAPER in this cycle's full build; confirm on the rendered stems that they did. Delivery: `master_eq` as it stands (shelf 3000 Hz -1.3 dB); re-check the delivery limits after the celli and bass changes and adjust only if a limit fails.
