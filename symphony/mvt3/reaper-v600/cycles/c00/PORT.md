# Cycle 0: port of the mockup pipeline to the Finale (score v600)

2026-11-07. Source: Movement I series 2 at its c42 (`symphony/mvt1/reaper-v621/`), the most developed version of the pipeline; Movement II series 2 (`symphony/mvt2/reaper-v600/`) for the port pattern (its c27).

## Extraction
- `build/mockup.ly` is Movement I's file unchanged (same 37 staves: v600's part variables have the same names). `build/score-defs.ily` is v600's `score.ly` from `sec =` to the last `\addQuote` (v600's `sec` takes bars and beats). All `.ily` files run through `convert-ly` (2.24 -> 2.26).
- `mockup-events.tsv`: 19 541 events; last note qn 1112 (bar 279). Percussion: crash cymbals at 888, 1048, 1108 (tied) and 1112; bass drum at 888 and 1108-1112.
- Tempo from the score MIDI's \mt steps (README of the loop BRIEF "The music"); eight ramp spans in `RAMP_SPANS`; length of the stepped vs ramped spans differs by at most 0.05 s.

## Config decisions
- Generic settings: every value of Movement I's config that names no score onset (listed by executing its config over the tool defaults and comparing; `build/score_config.py` "generic settings" block). `LEG_CAP_FRAC` spans over the whole score for all four upper string sections (Movement I had Violins I from qn 56 and a "listed" variant); `TIMP_ROLL_RESTRIKE` with no forced points; `SYNCO_SHAPE` written out (Movement I set it in two steps).
- Left out (score-specific in Movement I): LEVEL_SHAPES(_S), NOTE_TRIM_RAMP_S, ALIAS_TRACKS / PASS2_TRACKS / TEST_TRACKS, TRACK_WINDOWS, REBOW_AT, HP_TARGET_AT, BREATH_*_AT, JOIN_NOTCH, PICKUP_LIFT, PORTATO_JOIN_AT, DOWNBOW_STROKE_AT, ART_SPANS (Movement I's), REP_ROW spans, STR_REP_DETACH spans, METRIC_BOWED spans, LEAD_SPANS, GROUP_LEAD_AT, SUL_SPANS, NOTE_END_AT, PHRASE_ARCS, TEMPO_PUSH, BEAT_STRETCH, CAESURA, SF_ARRIVAL_AT, ARRIVAL_WEIGHT_AT, SHARED_DYN/HP, VEL_SET, TIMP_VEL, TIMP_TIE_STROKES, PORT_TARGETS, STACLEG_SPANS, TREM_JOIN, HP_SOFT_EXTRA_SPANS, RIDE_TRIMS, every skip list.
- Note: `STR_REP_DETACH` and `METRIC_BOWED` are span tables in Movement I; with none set the Finale's string repeats use the defaults only. They are candidates for c01 (S1: the hammered eighths).

## Tracks and patches
- 31 tracks: Movement I's 26 instruments + Trumpets 1-3 and the crash cymbals, the bass drum new (36in Ludwig Bass Drum, Felt Long key 38, 7 velocity layers, RR1-4, read from its region map). No pass-2 project.
- Timpani: `Timpani Hrd KS` (score: "hard sticks"); the felt-fitted `TIMP_CC1_MAP` and `TIMP_ROLL_TRIM_DB` kept for c00.
- Trumpet 1: "Mute Sus" (1TP KS Master row key 36) from qn 679.9 to 791.9 (24 notes).
- Pitch ranges checked against each used row's sample keys (region maps): all inside, except the bass trombone's one B flat 1 (34) below 1TB's key 36.

## parts.json at c00
- No WARNING. 31 tracks. Notes per string section: Violins I 752, Violins II 888, Violas 948, Violoncellos 615, Double basses 690; Trumpet 1 200 (24 muted); Timpani 179 (19 rolls); Crash 3, Bass drum 2, Harp 300.
