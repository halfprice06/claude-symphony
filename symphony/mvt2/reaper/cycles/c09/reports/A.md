# Cycle 9, critic A: articulation and phrasing (on the cycle 8 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c09-A/`; run them with `~/.venvs/claude-composes-reaper/bin/python`. The c08-A scripts were copied there with the default cycle set to 08. New scripts:
- `wjoin2.py "<tracks>" -v`: legato join dips on stereo power, measured twice: on the stem as rendered ("post") and with the parts.json `vol_db` envelope divided out ("pre"). The difference is the part of a dip that the volume envelope makes. `WTH=-99` lists every join.
- `shape2.py <track> 08 <qn...>`: 20 ms stereo-power envelope from 0.2 s before each score onset.
- `envstep.py`, `vib.py` (vibrato amplitude per note), `breath.py` (every breath mark), `sord.py` (spectral balance per note with CC15 state).

All levels are dB re full scale on the c08 stems. Onsets are score onsets (`sq`) on the c08 tempo map. Comparisons with c06/c07 stems after qn 29 are not valid because c08 added caesuras.

## 1. Exposed wind solos still have 9-12 dB holes at nine legato joins (Oboe 1 bars 19-20 and 82, cor anglais bars 34 and 42-43, Flute 1 bars 57-58 and 75-77)

**Measured** (`wjoin2.py`; dip = the softer of the two note bodies minus the minimum within -0.15 to +0.5 s; time of the minimum after the onset in brackets):

| Track | qn (bar) | step | dip post / pre envelope |
|---|---|---|---|
| Oboe 1 | 55.5 (19.5) | 73->72, v80 | 10.1 / 10.0 (+0.14 s) |
| Oboe 1 | 57 (20) | 70->68, v60 | 12.1 / 9.1 (+0.13 s) |
| Oboe 1 | 271 (82) | 70->68, v60 | 10.6 / 10.6 (+0.15 s) |
| Cor anglais | 99 (34) | 58->56, v80 | 9.4 / 9.6 (+0.12 s) |
| Cor anglais | 129.5 (42.4) | 70->68, v90 | 8.8 / 8.8 |
| Cor anglais | 133.5 (43.4) | 63->65, v90 | 7.7 / 7.6 |
| Flute 1 | 190 (57.5) | 85->89, v60 | 7.2 / 7.9 (+0.11 s) |
| Flute 1 | 252 (75.7) | 84->89, v60 | 9.3 / 9.0 |
| Flute 1 | 256 (77) | 92->91, v60 | 8.7 / 8.0 (+0.23 s) |

- Shape of Ob1 qn 57 (`shape2.py`, 20 ms steps from the onset): -42, -44, -46, -48, -51, -53, -54, -54, -52, -50, -49, -48 ... -45 at +0.36 s, -42 at +0.6 s. The note before sits at -39 to -43.
- None of these onsets is in `early_fills.json`. The c08 `fill.py` test compared the note's first 0.35 s with its own body, and these targets have soft bodies too, so they did not qualify. The hole is in the transition sample: a 1-2 semitone step down at v60-90.
- The c08 fills work. Every onset they cover now dips 2-5 dB, and `fill.py` finds only 4 wind/horn targets with a sag of 5 dB or more (it found 35 in c07).

**Inferred.** These are the oboe's answer to the violin solo (bars 19-20), the cor anglais "solo, dolce cantabile" (bars 33-34, 41-44), and the flute's top line at both climaxes. A 10 dB hole of about 0.3 s at a slurred step sounds like a re-tongued or cracked note in the most exposed lines of the movement.

**Fix.** Use the c08 method. Add to `build/early_fills.json` (dB = pre-envelope dip - 3, cap 8):
- Oboe 1: `"55.5": 7, "57": 6, "271": 7`
- Cor anglais: `"99": 6, "129.5": 5, "133.5": 4`
- Flute 1: `"190": 5, "252": 6, "256": 5`

Ob1 57's other 3 dB come from the envelope; finding 2 fixes that part. Do not raise the existing fills.

**Check:** `wjoin2.py "Oboe 1,Cor anglais,Flute 1"`: every listed join dips 6 dB or less, and none of the c08-filled joins rises above 5.

## 2. The volume envelope makes holes and bumps at joins: adjacent `roles.json` spans add together, and trims are still applied during the next note's transition (11 places)

**Measured.**

(a) **Adjacent role spans double up.** In `score_to_parts.py` `vol()`, the `"span"` branch ramps each role in over [a - 0.5, a] and out over [b2, b2 + 0.5]. Where one span ends at the qn where the next begins, both are at full value at that qn. Values from parts.json `vol_db` at the shared boundary (expected value in brackets):
- Violas qn 146: -7.0 (-4 -> -3). Qn 298: **+9.0** (+4 -> +7). This is a 4-5 dB bump in the ppp coda chord: the stem goes -52 -> -47 for 0.4 s at qn 298.
- Violins II qn 216: **-18.5** (-6 -> -8). Qn 218: -10.0 (-8 -> -2). Qn 220: -9.5 (-2 -> -3), then -4.8 at 220.1.
  - Effect at 216: the p tremolo re-entry in bar 64 drops to -57 for 0.3 s, then plays at -52 to -54.
- Violoncellos qn 78: -7.0 (-1 -> -6). Qn 262 (bar 79, the f arrival): **-12.0**, with note trim 261 -8 on top, then -3.4 at 262.1. The stem enters bar 79 at -49 and reaches -36 only after 0.5 s.
- Harp qn 124: -11.0 (-4 -> -7). Horn 1 qn 188: -5.7 -> +4.2 within 0.2 qn.

(b) **Trims that end after the join.** The pitch-trim and note-trim `"note"` part holds the outgoing note's trim to its score end and releases it over the next 0.1 qn. But the legato transition belongs to the *new* note-on, which starts up to 0.2 s earlier because of the leads. The transition sample therefore plays under the old note's trim.
- Flute 1 qn 255: the B flat 6 trim (-4 pitch, -4 note) is still -6.6 dB at 255.0, while the G flat 6 transition sounds. Dip 7.3 dB post, 2.5 pre.
- The same effect at Fl1 270.5 (10.7 / 7.6), Ob1 57 (12.1 / 9.1), and Vc 292 (9.7 / 5.9). At Vc 292 the role [292, 304, -4] ramps in from 291.5, under the outgoing note.

(c) **At qn 146 (bar 46.5), Violas and Violins II dip together at the start of a printed crescendo (pp < mp).**
- The c07 `bcsoft` CC11 dip (34 -> 29) sits on the Leg BC target, and the doubled Vla role (-7) adds to it.
- Dips: Vla 11.4 dB, Vln II 8.3 dB. Vla goes from -53 to -66 in the 0.4 s after the bow change, and both sections are still at -58 to -60 dB 0.5 s later.
- Inferred: the inner parts disappear for half a beat under the oboe solo just as their crescendo starts.

**Fix (`tools/score_to_parts.py`).**
1. Roles: before building `vol_parts`, merge each track's role rows into one chain. Where span B starts within 0.5 qn of span A's end:
   - interpolate from A's dB to B's dB over [B.a - 0.1, B.a + 0.15];
   - do not ramp A out to 0 or B in from 0.

   Isolated spans keep the 0.5 qn ramps.
2. `"note"` parts (pitch trims and note trims): if a note follows within 0.1 qn, the outgoing note's trim ends with a ramp over [next onset's *moved* qn - 0.05, moved qn + 0.03]. The new note's own trim begins at its moved onset. The same applies to the `"env"` pitch-trim shape: set its last point to the next moved onset instead of `e + 0.1`.
3. A role span that *starts* on a legato target ramps in over [a, a + 0.25], after the join, not [a - 0.5, a].
4. `bcsoft` is skipped when a `cresc` hairpin starts within 0.25 qn of the target (`hps` rows with k == "cresc").

**Check:**
- `vol_db` at Vla 146 / 298, Vln II 216 / 218 / 220, Vc 78 / 262 and Harp 124 lies between the two neighbouring role values.
- `wjoin2.py`: post minus pre is under 1.5 dB at every join.
- Vla and Vln II at qn 146-146.5 do not fall more than 3 dB below qn 145.5.

## 3. Bow-change legato across more than an octave, or from the soloist to the tutti, leaves a 10-20 dB hole: the coda's cello pedal enters about 1 s late (bar 83), and the tutti entry at bar 22 dips 10 dB

**Measured.**
- **Violoncellos qn 274 (bar 83, [K] a tempo):** the C4 -> A flat 2 step (-16 semitones), ppp, "change bow at will". It is unslurred, so the has_bc rule makes it Leg BC MAX at v124, overlapped with the C4.
  - The stem falls from -58 to -76 dB at the onset. It is still -76 at +0.6 s, -65 at +0.8 s, and -58 only at +1.0 s (`shape2.py`). Join dip 20.0 dB, with or without the envelope.
  - The double basses enter on the same beat on Sus MAX and are at body level (-51) within 0.2 s.
- HO manual p. 51: the legato script selects "a legato slur cross-faded into sustain" for connected notes "up to an octave in either direction". The same applies to the Leg BC script. This is the only Leg join in the movement wider than 12 semitones (a scan of every Leg target).
- **Violins I qn 65 (bar 22):** the end of "solo, senza sord." (E flat 5) into "tutti (gli altri con sord.), espr." on E flat 4.
  - It is played as a Leg BC join (slur-to-slur rule), with a dip of 10.7 dB post and 10.0 pre.
  - The stem reads -49 before, -56 to -58 for 0.15 s, -52 to -56 to +0.35 s, then -44.
  - In the score these are different players: the soloist stops and the section enters.

**Inferred.** The coda section opens with the cello pedal missing for a second under the harp harmonics, so the low octave seems to fade in. The bar 22 tutti phrase starts with a gap instead of a fresh, warm entry.

**Fix (`score_to_parts.py`, the c02 Leg BC block, before `o["art"] = "Leg BC MAX"`).** Skip the join (`continue`) when either:
- `abs(o["pitch"] - n["pitch"]) > 12`, or
- a text at `o["qn"]` in `staves` matches `has(t, "tutti")` or `has(t, "solo")`.

Then n ends `min(0.05, 0.15 * dur)` early (the existing `elif o.get("art") and "Leg" in o["art"]` branch).
- Vc 274: play the note on Sus MAX, like the basses, with the family entry lead (strings 0.12 s; the c06 Leg -> Sus path).
- Vln I 65: stays Leg Slur MAX as a disconnected first note (sustain layer), with the entry lead. Add `entry_leads.json` extras only if the check fails.

**Check:**
- Vc qn 274: within 4 dB of its qn 275 level by +0.25 s.
- Vln I qn 65: no point between +0.05 and +0.35 s more than 4 dB under the level at +0.5 s.
- Attack gate still 19 of 19.

## 4. Horns 3-4 "con sord." (bars 87-89) sound exactly like open horns: CC15 does nothing on the 1FH KS Master

**Measured.**
- CC15 is 127 from qn 271.5 on Horn 3 and Horn 4. The 1FH KS Master maps CC15 to "Con Sordino" and has the `ConSordino` script active (read from the .oib).
- Same pitch (A flat 3, 56), same patch, same CC11:

| Note | CC11 | 2-8 kHz minus f0..4f0 | centroid |
|---|---|---|---|
| Horn 3 muted, qn 289 / 292 | 34 | -17.7 / -17.7 dB | 476 / 475 Hz |
| Horn 4 open, qn 9 / 12 / 15 | 34 | -17.7 / -17.7 / -17.7 dB | 474 Hz |

- The spectra are identical to 0.1 dB, so the mute has no effect.
- For comparison, the celli (Celli KS Master, CC15 127 in bars 23-28, CC11 about 49) measure a 2-8 kHz ratio about 3-4 dB lower than their senza notes at the same CC11 in bars 71-74 (-23.9 against -20.0 median).
- HO manual p. 91: Con Sordino "emulates playing strings con sordino" (an EQ; the hyper-orchestra text, line 6372, says the same of Hollywood Strings). It is a strings script, and it is inert on the horn.
- The horn folders have no muted samples. `05 Mutes` holds only stopped horn (`1FH Stop Sus`), which Adler (p. 291) says sounds different from a muted horn. Do not use it for a pp con sord. chord.

**Inferred.** The last brass colour of the symphony, the only muted brass (coda.ily c030), is missing. The pp horn chord in bars 87-89 sounds open and round where the score asks for a veiled, distant colour under the clarinet's "dolce".

**Fix.** Emulate the mute with a second ReaEQ that is switched in by automation.
- `build/mix.json` Horn 3 and Horn 4: add `"mute_eq": {"from_qn": 278.0, "bands": [{"band": "lowshelf", "hz": 300, "db": -6}, {"band": "bell", "hz": 1800, "db": 3, "bw_oct": 1.0}, {"band": "highshelf", "hz": 4500, "db": -8}]}`. Horns 3-4 rest from qn 271.5 to 286.
- `tools/build_reaper.py`:
  - add a second ReaEQ after the first (`set_eq` deletes every ReaEQ, so add this one after it runs);
  - set the bands with the existing search;
  - give its Wet parameter (`TrackFX_GetNumParams(tr, fx) - 2`) an envelope with `GetFXEnvelope(tr, fx, wet, true)`: 0 at qn 0 and 1 from `from_qn` (pre-roll shifted, square shape);
  - apply it in `--midi-only` and `--mix-only` too.
- `build/roles.json`: Horn 3 and Horn 4 `[286, 293, -2]`. A mute also takes off some level.

The bands are inferred from how a straight mute sounds (less fundamental and body, a nasal mid, softer top). Use the hyper-orchestra "virtual mute" idea; a 3 kHz cut alone would make the horn darker, not muted.

**Check:**
- `sord.py "Horn 3"`: qn 286-292 differ from the open Horn 4 notes at qn 9-15 by at least 6 dB in the 300 Hz-and-below to 1-2.5 kHz balance.
- Horn 3/4 are unchanged before qn 278.

## 5. Trombone 1's marcato quotation (bars 63-64): the accent at qn 218 is +0.4 dB, and the line has no accent shape at ff

**Measured** (`acc.py`, 20 ms frames; pre = median of the 0.3 s before):
- qn 212.5, accent: peak -23.9, body -26.6 (the bar's first note, from silence).
- qn 213, accent (v121, Sus Accent MAX): peak -24.6 against -29.2 just before.
- The unaccented eighths at qn 214.5-217.5 (v91, Sus MAX, CC11 114): peaks -26.2 to -29.7.
- qn 218, accent (`VEL_SET` v105, c06): peak -28.3 against -28.8 before, so **+0.5 dB**.
- Why: the accent's CC11 bump goes from 114 to 122, where CC11 moves about 1.2 dB per 10 CC (LEARNINGS c06). And v105 on Sus Accent MAX is no louder than the v91 Sus notes around it.
- The score has accents on qn 212.5, 213 and 218, "marcato", ff, with the decrescendo starting at the qn 218 accent (h-5.png, bars 63-64).

**Inferred.** The only brass solo in the movement, and the only printed accents, play as an even ff line. The accent at bar 64, which starts the dying fall, is lost.

**Fix (`score_to_parts.py`).**
- For notes in `accent_q`, add a volume-envelope part in the same form as the early fill: `("env", [(q - 0.02, 0), (sec_qn(q, 0.03), 3), (sec_qn(q, 0.25), 3), (sec_qn(q, 0.5), 0)])`. That is +3 dB of weight with a 30 ms rise, so no click (Dan's 2-4 dB).
- `VEL_SET["Trombone 1"][218.0]`: 105 -> 118.

**Check:** the first 0.3 s of each accented note is 2-4 dB over the median peak of the two unaccented notes either side (qn 214.5-215 for 213, qn 217-217.5 for 218), and peak-minus-body stays under +4 dB.

## 6. Harp broken-chord figure, bars 53-58 (qn 172-196): B flat 3 is 4-7 dB under the line and F4 up to +5 over it, at one velocity

**Measured.** The attack energy of each single note above the ring of the earlier notes (`harp` inline script in the scratch history; stereo power):
- Bars 53-54 (p, v64): spread p10-p90 6.1 dB. B flat 3 (58) -4.4, C4 (60) -2.7, F4 (65) +4.9, G flat 4 (66) +2.7.
- Bars 55-58 (mp, v76): spread 9.0 dB. B flat 3 -7.4 (6 notes), A3 (57) -3.9, E flat 4 (63) -3.4.
- Same-pitch pairs at two velocities give 0.3-0.6 dB per velocity step (Harp Sus RR).

**Inferred.** The figure accompanies the clarinet/horn duet and the bar 57 flute/oboe tune. A harpist plays it evenly, and here every group has a soft or loud note that nothing in the score asks for.

**Fix (`score_to_parts.py`, the harp velocity block after the `value_at` curve).** Add `HARP_PITCH_VEL = {58: +12, 57: +7, 60: +5, 63: +5, 65: -8, 66: -4}` and apply it to `family == "harp"` notes that are not arpeggio top notes, clamped 1-127.

**Check:** the same measure, with a p10-p90 spread of 5 dB or less in both spans and no pitch more than 3 dB from the median.

## Also measured, not ranked

- **Flute 1, C6 and above:** the vibrato amplitude (p90-p10 of the 20 ms envelope in the note body, `vib.py`) is 7-9 dB at CC1 92-100. Below C6 it is 2-5 dB. Oboe is 4, violins 4-5.
  - It adds to the join dips in finding 1. It does not follow CC1 clearly (Fl1 qn 271, CC1 88: 8.2 dB), so no fix is proposed.
  - If finding 1 leaves Fl1 252-258 above 6 dB, test CC1 70 on Fl1 pitches 84 and up.
- **Breath marks:** all 29 produce a clear break: 0.19-0.49 s gaps, with the level 14-36 dB down. Hn1 196 and 265 dip only 6-7 dB because of the hall tail, which is fine.

Do not touch: the c08 early fills and the F4 `{early, body}` shape (sag targets now 2-5 dB); VLA_BC_SOFT; the Leg Slur/Leg BC split and v124 for strings (median string join dips 2.8-4.0 dB); the legato leads; the sostenuto portato joins; the breaths and caesuras; the timpani roll settle (the coda roll holds -61 dB for 18 s); harp roll timing; the pizz. pitch trims.
