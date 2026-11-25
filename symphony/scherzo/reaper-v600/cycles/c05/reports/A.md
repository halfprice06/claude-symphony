# Cycle 05, critic A: articulation and phrasing (render c04)

Render under review: `cycles/c04/render/` (stems and master), made from `cycles/c04/build_render/parts.json`. Times are seconds of score time on that parts.json's tempo map. Unless noted, levels are plain RMS from a 10 ms envelope, and perceived attacks are `tools/pcx.py attack_pcx` values (pc, seconds after the score onset).

## Manual notes (A6: PDF pages 68-71, Hollywood Harp, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| Sustain RR alternates Pluck Long (RRx1) and Thumb Pick (RRx2) by round robin at velocity 1-123; Nail Pick at 124-127 regardless of the cycle (p.69) | Harp track on `Harp Sus RR.oib`, all 346 notes | Yes (measured). Velocities run 40-64, so no note reaches the nail pick. The round robin does not make the off-beat chords lumpy. In the trio chords (456-504, 552-576, 672-708) the beat-2 and beat-3 chords sit within 1.1 dB of each other, and successive chord peaks vary with an SD of 1.1-1.5 dB. In 1020-1044 the SD is 2.2-2.5 dB. |
| CC11 and velocity control loudness; velocity also picks the dynamic layer (5 layers) (p.69-70) | Harp CC11 is held at 110; dynamics come from velocity, `VEL_CAP_SPANS` (216-264) and roles | Yes (read) |
| Harmonics patch: upper partials only, 2 velocity layers (p.70) | Harp harmonics track (`Harp Harmonics.oib`) at qn 445, 451, 1123, v58 | Yes (measured). At each onset it is the loudest stem (-46 dB against -49 for the next) and rings 1.3-1.4 s to -20 dB. |
| Repetition Rep lets earlier notes ring on fast repeats (p.70) | The trio's repeated off-beat chords | Not needed (inferred). The chords repeat a beat apart, and the pipeline ends each chord at the next pluck of the same string, as a harpist's re-pluck does. |
| Double Hit, Gliss Technique, Bisbigliando, Nail Pick, Près de la table, FX / Gliss key map (p.68-71) | Not printed in the score | n/a |
| (Score, not manual) "étouffez" at bar 192 (qn 575.5) | Every harp note ends at 575.5 | Yes (measured). The stem falls 25 dB in 0.2 s at the note-off. |
| (Score) arpeggiated chords at 708 and 1080 | Rolled bottom to top in 0.152 qn steps, about 0.04 s per note | Yes (read) |

MANUAL-GAPS items that bear on the findings below: #10 (horn portato rows: 1FH "Port Lng", 775 regions) for finding 3, and #8 (legato velocity) as a later option for the trio lines.

## Findings, ranked by what a listener would gain

### 1. The accented hemiola half notes swell instead of accenting: in bars 101-104 and 301-304 every family peaks 150-340 ms after the beat (measured)

**Where.** "Ritmo di quattro battute", the f hemiola before both tutti statements. Score onsets 300, 302, 304, 306, 308, 310 and 900 (sfp), 902-910. These are accented half notes, 0.45 s long at quarter 264, in a crescendo. All string tracks play them as fresh Sus MAX strokes (`DOWNBOW_STROKE_AT` with `_HEM`, score_config.py), and the winds and brass play them as `GENTLE_ACCENT` Sus notes.

**What is wrong.** Every accent's weight lands on the second quarter of the half note. The ear hears six swells, each growing after the beat, so the bar-against-bar hemiola, the point of the passage, is blurred.

**Evidence (measured).**
- **Master, peak position.** The 10 ms envelope peaks +270, +310, +280, +200, +290, +260 ms after 300-310. After the sfp it peaks +290, +150, +340, +320, +260 ms after 902-910.
- **Master, front minus body** (0-0.1 s against 0.2-0.4 s): -3.9, -5.7, -1.7, -2.9, -0.1, -1.9 dB at 300-310, and -1.7, -1.6, -1.8, -2.3, -2.4 dB at 902-910. The rising crescendo explains only about 0.5 dB of this over 0.4 s.
- **Stems, median peak after the beat over 302-308.**
  - Strings: Violins I +240 ms, Violins II +330, violas +280, celli +135, basses +225.
  - Winds and brass: Oboe 1 +300, cor anglais +255, Horn 4 +335, tuba +280.
  - The same pattern after the sfp: Violins I +360, Violins II +340, celli +300.
- **Stems, front (20-150 ms) minus body (180-400 ms).**
  - Violins I: -7.4 / -4.1 / -2.1 / -2.2 / -3.0 / -4.1 dB at 300-310, and -7.1 / -6.9 at 902 / 904.
  - Violins II: -2.6..-4.5 at 300-310, and -2.6 / -5.9 at 902 / 904.
  - Over the whole piece, accented Sus MAX string notes of 0.45 s or longer sit -0.4..-5.1 dB front-to-body (median per track). Unaccented ones sit -1.7..+3.1. The accent makes the front relatively weaker, not stronger.
- **Cause (read plus measured).** The swell (`GENTLE_ACCENT["string"]["swell_s"]` (0.03, 0.15, 0.4), +3 dB) peaks over 0.03-0.15 s after the score onset, while the f Sus MAX sample is still rising. The sample reaches its body after the swell has started to fall. The perceived attacks are late too:
  - Violins I: +0.03..+0.11 s at 300-310.
  - After the sfp, at p (CC11 57-60), Violins I +0.171 / +0.136, Violins II +0.126 / +0.141, violas +0.053 / +0.121, celli +0.053 / +0.214 at 902 / 904.
  - Current leads are only 0.08-0.12 s.
  - Violins I/II play 904 at v65 while the violas and celli play it at v105: the velocities are inconsistent.

**Fix.**
- (a) **Body cuts so that each accent's front stands over its body.** Add `ACCENT_BODY_S_SHORT = (0.15, 0.26)` in score_config.py; the default (0.25, 0.45) is longer than these 0.45 s notes. In `build/accent_bodies.json`, enter -3.0 dB at the 11 onsets of `_HEM` (300-310, 902-910) for Violins I, Violins II, Violas, Violoncellos and Double basses, and -2.0 dB for Oboe 1, Oboe 2 and Cor anglais at their hemiola accents. Each next accent's front then rises from the cut, so the crescendo still climbs one stroke at a time.
- (b) **More lead on the late strokes.** Use `REATTACK_LEAD_AT` (or entry_leads.json extras, if those reach the DOWNBOW_STROKE_AT path; check `qn` in parts.json):
  - 902 and 904: 0.20 s on Violins I, Violins II and Violoncellos, 0.18 s on Violas.
  - 300-310: 0.13 s on Violins I.
  - The c04 leads stay elsewhere.
- (c) **Velocities.** Give Violins I/II 904 the stroke velocity of its neighbours (about 85, between 902's 105 and 906's 78), not 65.
- **Targets:** master peak within +0.15 s of each beat; master front minus body at least +1 dB; string stems front minus body at least +1 dB; string pc within ±0.06 s; bar-to-bar crescendo 300-310 / 902-910 still rising. The cuts are level only, so `stem_fix.py` can refit them after the render.

### 2. The trio's con sordino arpeggios in Violins II limp: the first note of every slurred group comes early, the rest late (measured)

**Where.** Violins II, bars 168-196 (score qn 501.5-588), pp con sord., dolce. Each group is five slurred eighths starting off the beat (501.5, 502, 502.5, 503, 503.5, rest, 504.5 ...), under the celli's trio tune (169-184) and Violins I (177-184). All 85 notes play on Sus MAX at v41.

**What is wrong.** Only the group's first note gets the string entry lead (0.12 s); the four slurred followers get none.
- On the pcx medians, the first note lands -0.021 s (504-528) and -0.013 s (528-552), n = 8 each, and the followers land +0.050 / +0.052 s, n = 32 each.
- The step from the first to the second note is therefore 0.06-0.07 s too long on the median. At 504.5 it is 0.105 s (-0.055 to +0.050). At quarter 228 an eighth lasts 0.132 s.
- Every group starts with a hiccup, long then short, twelve times in four bars of a soft accompaniment figure. No other string passage shows this: a scan of every 24 qn window for led heads against unled followers flagged only these two windows.

**Fix.** `GROUP_LEAD_AT["Violins II"] = [(501.5, 587.5, 0.05)]` in score_config.py. It replaces each note's lead with 0.05 s, so the followers move from +0.05 to about 0 and the heads from -0.02 to about +0.03. If the single span disturbs the note ends at group boundaries, split it into one span per five-note group. Check in parts.json that every note in the span has its onset 0.05 s early. Target: head and follower pc medians within 0.03 s of each other, both inside ±0.04 s.

### 3. Horn 1's repeated tenuto dotted halves in the trio's return have holes 80-140 ms wide (measured; c04 open item)

**Where.** Horn 1, bars 210-222 (score 627-666). Repeated tenuto dotted halves (627 -> 630 -> 633 on B4, 636 -> 639 on C sharp 5, 648 -> 651, 660 -> 663), all on Sus MAX, re-tongued (`rep_retongued`), with a 0.05 s re-tongue lead.

**What is wrong.** Tenuto means full value with a gentle re-articulation. The stem instead dips 11.1 / 11.1 / 8.4 / 7.2 / 9.8 dB at 630 / 633 / 639 / 651 / 663. It stays more than 3 dB below the surrounding level for 140 / 140 / 80 / 110 / 130 ms, and the minimum falls +40 ms after the beat at 630, 633 and 663: the new attack rises slowly after a 0.07 s gap (`WIND_REP_RETONGUE_BY["Horn"]` gap 0.07 s, fall 8 CC over 0.12 s). Horn 3's repeats reached 5-6 dB with the c04 values, but Horn 1's did not. At quarter 228 a 0.14 s hole is half a beat of silence in a sustained horn line.

**Fix.** Give Horn 1 its own entry, `{"gap_s": 0.035, "frac": 0.15, "fall_cc": 4, "fall_s": 0.08}`. It must sit before `"Horn"` in `WIND_REP_RETONGUE_BY`: the lookup takes the first key that matches the track-name prefix, so rebuild the dict with "Horn 1" first. Also set `RETONGUE_LEAD_S["Horn 1"] = 0.09`, so that the new note's rise overlaps the old note's end. Target: dips 3-6 dB, under 80 ms below -3 dB. If the sample's own decay still leaves 8 dB, the next step is MANUAL-GAPS #10, the 1FH "Port Lng" row on these 12 notes (775 regions).

### 4. Soft arco entries after pizzicato speak late: the celli's trio tune enters 0.11 s after the beat (measured)

**Where and evidence.** First arco notes after a pizz. passage, on Leg Slur MAX's first-note layer with the 0.12 s entry lead:
- Celli at 504 (bar 169, mp, "arco, espress.", the trio tune passing from Clarinet 1 to the celli): pc +0.112 s.
- Celli at 756 (bar 253, p, "arco, espress."): +0.080 s.
- Basses at 840 (bar 281, p arco <): +0.083 s.
- For comparison, the loud or Sus MAX arco entries are on time: basses 90 / 504 / 576 / 624 / 1071 at -0.045..+0.032 s, celli 828 at +0.007 s.

At quarter 228, 0.11 s is 40 % of a beat, on the first note of the melody.

**Fix.** In `build/entry_leads.json`, add Violoncellos `{"504.0": 0.10, "756.0": 0.07}` and Double basses `{"840.0": 0.07}`. The total stays under `ENTRY_CAP_S` 0.30. Target: pc within ±0.04 s.

### 5. Outside the hemiola, about a third of the string and oboe accents sit level with or under their neighbours; `accent_fits.json` is empty (measured)

**Where and evidence.** For every printed accent, level over 20-150 ms against the same window of the notes on each side (within 3 qn). Count shown is accents at or under their neighbours.

| Track | Median over neighbours | At or under |
|---|---|---|
| Violins I | +1.0 dB | 17 of 47 |
| Violins II | +0.5 | 15 of 37 |
| Violas | -0.3 | 17 of 31 |
| Oboe 1 | -1.0 | 17 of 27 |
| Flute 2 | -3.4 | 5 of 9 |

Dan's rule is +2..+4 dB of weight.
- **Outside the hemiola**, the accents at or under their neighbours are:
  - Violins I: 111, 213, 351, 819, 915, 951, 999 (-0.1..-4.9 dB).
  - Violins II: 132, 195, 327, 927, 981 (-2.1..-7.5).
  - Violas: 132, 183, 267, 723, 879, 978 (-0.1..-7.8).
  - Oboe 1's counterstatement heads 87 / 99 / 111 (on Leg Slur MAX, `keep_legato`): -0.5..-1.4. Its accents at 351 / 915 / 951 sit at -1.5 dB.
- **Bite (BRIEF item 9).** 2-5 kHz energy over the first 80 ms minus the body: medians -1.1..-6.7 dB on the winds and -1.5..-3.6 on the upper strings. The basses sit at +1.4. No family bites.
- **Caveat.** The neighbours include staccato notes, whose front-loaded rows read hot in this window, so part of the deficit belongs to the window.
- `tools/fit_accents.py` was written for exactly this (unaccented neighbours at the same CC11, swell fitted into [2, 4] dB), but `build/accent_fits.json` is `{}` in this series.

**Fix.** Run `fit_accents.py 4 cycles/c04/build_render/parts.json --family string --write`, then the same with `--family wind`, after the finding 1 edits so the hemiola is predicted with its new shape. Its defaults (lo 2, hi 4, target 3) fit Dan's rule. Skip the hemiola onsets (finding 1) and the Marc LITE heads (fitted in c02-c03).

### 6. The violas' div. portato pairs in bars 209-224 still have no pulse (measured; c03 open item)

**Where.** Violas and Violas div, the slurred tenuto pairs at 629, 638, 641 ... 671 (`_PORT_PAIRS`). They are now split by `STR_REP_NEW_BOW` "portato": the first note is on Leg Slur MAX, the second a Sus MAX stroke led 0.079 s, and the gap of 0.05 s falls 0.08-0.13 s before the beat.

**What is wrong.** Measured with a window that covers the moved gap (-0.22..+0.1 s around the onset), the dip at the second note has a median of 1.2 dB on Violas (range -1.2..+5.6) and -0.7 dB on Violas div (range -1.6..+4.2). The louré re-articulation the score asks for is not heard.

**Fix.** In `STR_REP_NEW_BOW["portato"]` (score_config.py), set gap_s 0.05 -> 0.08, frac 0.25 -> 0.3, fall_cc 6 -> 12, fall_cc_loud 8 -> 14, fall_s 0.04 -> 0.08. Target: dips of 3-5 dB on both viola tracks. Check that the stroke lead still puts the second note's pc within ±0.05 s.

## Also measured (not ranked)

- **Pizzicato timing (S2).** Every pizzicato section lands on the beat: pc medians -0.013..+0.013 s in 6-90, 264-300, 408-504 and 756-816. The Violins I staccato theme at 36-84 and 756-816 lands at +0.008. The harp's trio chords land at +0.010 / -0.008.
- **Coda pairs (S1).** The master's eighth-pair dips at 984-1003 are 2.7-7.1 dB, and every string stem dips 2.2-16 dB. Trumpet 2, still on Sus slices, dips 1.5-6.0 dB.
- **Loop pulsing (item 8).** No 3.95 s periodicity on the held notes. Autocorrelation of the detrended band level and centroid at 3.95 s: Violins I 0-23 -0.04 / 0.00, 1089-1126 +0.08 / +0.01, 420-445 -0.30 / -0.10; celli 605-624 -0.06 / -0.03; Horn 3's drone 456-504 -0.03 / +0.13.
- **Legato lines.** Join holes have a median of 2.2 dB (celli 504-552), 1.3-3.3 (Violins I, 528-552 and 624-672), 3.0 (Violins II 624-672), 3.2 (the solo, 1044-1068) and 3.1 (Flute 1 col Vl. solo). All legato targets except the solo's second half (v90) and the flute (v100) play at v124. Envelope-corrected neighbour steps have a median of 1.6-2.5 dB. Clarinet 1's trio tune: its B4 at 459 is still about 4-7 dB hot in the raw stem (B's area).
- **S3 sub. p** (360, 828). The drops are in CC11, before the onset, and no role steps in vol_db sit under the subito, apart from the celli's -1.5 dB step at 828. The hall tail is kept (read).
- **Timpani rolls.** Each roll (300, 384, 612, 708, 852, 906, 993, 1005) is a "Rls" note ending into a printed stroke on Lng (read).

## Do not touch

The harp setup: Sus RR velocities 40-64, the let-ring note lengths ended at each re-pluck, the étouffez note-offs at 575.5, the rolled arpeggios, and the Harp harmonics track. The pizzicato leads (`PIZZ_LEAD_S`). The coda staccato rows (c04 A #3). The re-bow fills and the CC70 / CC15 lanes. Subitos in CC11. Plus the earlier critics' items: the Marc LITE heads with their level steps, the clarinets' whole-piece Leg Slur Rep, the wind "Stac DblTng RRx9" rows and their leads, `GENTLE_ACCENT`'s no-bite rule (finding 1 changes the timing of the body, not the bite), `PORT_TARGETS` 640, ir_setup and the release caps.
