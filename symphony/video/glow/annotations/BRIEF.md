# Brief: split-screen moments and notes on the score, for one movement's glow video

You are preparing annotations for the glow score video of one movement of Dan's four-movement symphony (I C minor, II Adagio in A♭, III scherzo in E, IV finale in C; the finale's files live in `symphony/mvt3/`). The video shows the whole movement engraved on one long line, seen at an angle by a moving camera; each note lights up while it sounds in the mockup recording. The prompt that sent you here names your movement, its files and your output path.

## What Dan asked for (his words, 2026-11-23)

- "sometimes the top instruments might be playing something in unison or that we might want to highlight with something at the bottom of the screen. What if we could do something like a jump to Split screen in those moments to highlight both and then back to normal after."
- "highlight important musical analysis like things you might point out in a music theory class about the composition. Repeating motives, interesting chords and harmonies, melody and countermelody, and interesting bits of the form. Eg we have a piece of the main melody in mov 2 in trombone solo that comes from Mov 1 etc."
- After seeing concept clips he chose: a stacked split screen; analysis notes drawn on the score. Then: "we should look for more examples more carefully where there are more than one thing we may want to highlight on the score, I think we are missing some points now where we'd probably want to show multiple things." And: "I'd be fine with the pull back happening occasionally at times if it makes more sense then a split, or even a split being able to pull back."
- Dan dislikes mannered prose. Write plainly and literally: no metaphors, no flourish.

## How the two features look

**Split screen (`stack`).** For the given bars the frame divides with a level seam into an upper view and a lower view. Each view centres on one staff (`upper`, `lower`) and follows the music along the line. Each half shows about ±300 px of the score's height around its staff at zoom 1.0; `upper_zoom` / `lower_zoom` up to 1.8 pull that panel back to show more staves (about ±300 × zoom px).
**Pull back (`pullback`).** No split: the one camera rises and pulls back far enough to show both staves (and everything between) at once, then returns. Good when the two groups are moderately far apart (roughly 700–1300 px), when three or more layers matter at once, or when a split would cut a passage that is really one texture.
**Notes on the score (captions).** A bracket draws itself round a passage on one staff (`anchor`), a short label (`short`) is written on the paper above it with a small kind word (`kind`), and optional chord names (`chords`) appear above a staff as the music reaches them. While a note is shown, the camera aims at its anchor staff, so the anchor must be where the music worth looking at is. During a split, a note's anchor must be within one of the two panels (near `upper` or `lower`).

## Your inputs

- Score source (concert pitch; check the version's `score.ly` / `global.ily` to confirm, and allow for any transposing instruments if it is not): `<version>/sections/*.ily`, with `<version>/sections.txt` giving the sections in order with their bar counts (and beats per bar when a third column is present), and `<version>/global.ily` for keys, metres, tempo marks. Bar numbers count from 1 at the start of the first section. Many .ily files have comments with the composer's and critics' analysis; use them, but check every claim against the notes.
- Analysis notes: `symphony/coherence/<movement>.md` (form tables, orchestration facts, cross-movement links), the theme records in `symphony/coherence/themes-*.ly/.md`, `symphony/cyclic-notes.md`, and the movement's plan or README where one exists.
- Bar report: `symphony/video/glow/annotations/reports/<movement>-bars.txt`. It lists the staves top to bottom with their vertical centre in px (only these exact names are valid staff names), then for every bar: its start time in seconds in the mockup, the staff the automatic camera follows, and the number of note onsets per staff in that bar. Use it for timings (durations in seconds), for distances between staves, and to see where the automatic camera shows only one of two important groups.

## Choosing split moments

Go through the whole movement bar by bar. Dan said the first pass missed moments, so be thorough: list every place where two groups far apart in the score both carry material worth watching at the same time, for example:
- melody and countermelody; two themes combined; a theme in the bass under a melody on top;
- a line doubled in distant parts (flutes with cellos, violins with horns, unison or octaves across the score);
- dialogue or imitation between distant groups within a bar or two (call and answer, canon, fugato entries);
- a solo answered or accompanied by an important figure far from it.
Do not split for a melody over plain held chords or repeated accompaniment, for tutti block chords, or where both groups fit in one normal view (centres less than about 600 px apart). Each moment should last at least 3 s and normally a phrase (2–8 bars); merge neighbours; leave at least 4 s between moments. Choose `stack` by default and `pullback` where it serves better (say why in `what`). `upper` must lie above `lower` in the layout.

## Choosing notes

Cover the movement: roughly one note every 20–40 seconds of music, more where several things happen close together, none in long uneventful stretches. Each note is shown for 4–12 s and notes do not overlap in time. Point out what a music theory class would: themes and their returns and transformations, repeated motives, notable chords and modulations, melody and countermelody, imitation, the form (where sections begin), orchestration that matters, and quotations of other movements.
- `kind`: one of Theme, Motive, Harmony, Counterpoint, Form, Orchestration, Quotation.
- `short`: the words written on the paper, at most 48 characters, plain (e.g. "Movement I's first theme, now in A minor").
- `text`: one or two plain sentences for Dan's review that state the full point with bars and instruments.
- `chords`: only where the chord names help; each name must match the sounding pitches in all parts at that moment (spell as in the score: D♭, F♭, E7, Fr6, dim7, "F♭ = E"). Use ♭ and ♯ characters.
- Every claim must be checked in the .ily files: bar numbers (from sections.txt offsets), instruments, pitches, rhythms, keys. A quotation claim must be compared with the theme records. If you cannot confirm something, leave it out.
Movement II's bars 60–65 already have four reviewed sample notes in `symphony/video/glow/concepts/captions-mvt2-60-65.json`; they show the tone and format.

## Positions

Positions are strings `"bar.q"`: `q` is 1 plus the offset from the barline in quarter notes. `"63.1"` is the downbeat of bar 63; `"64.4.5"` is the second half of beat 4 in a 4/4 bar; in 3/4 bars `q` runs 1 to 3.99; in 6/8 a dotted quarter is 1.5 quarter notes (the second dotted-quarter beat is `".2.5"`). A `to` of `"66.1"` ends at the downbeat of bar 66. Stay within the movement's bars.

## Output

Write one JSON file (the path is in your prompt), UTF-8, in this shape:

```json
{
  "movement": "mvt2",
  "splits": [
    {"from": "69.1", "to": "73.1", "mode": "stack", "upper": "Oboes 1·2", "lower": "Horns 1·2",
     "upper_zoom": 1.0, "lower_zoom": 1.0, "bars": "69–72",
     "what": "One sentence: what each group plays and why both matter.",
     "check": "Where you confirmed it, e.g. clos.ily closFluteOne/closHnOne, bars 69–72."}
  ],
  "captions": [
    {"from": "63.1", "to": "64.3", "kind": "Quotation", "bars": "63–64",
     "short": "Movement I's first theme, now in A minor",
     "text": "Trombone 1 plays its only notes of the movement: ...",
     "anchor": {"staff": "Trombones 1·2", "from": "63.1", "to": "65.1"},
     "chords": [["63.1", "A minor"]],
     "check": "bSec.ily bSecTbnOne bars 63–64 against themes-mvt1.ly mvtOneThemePHead."}
  ]
}
```

`chord_staff` (optional) puts the chord names over another staff than the anchor. Keep `splits` and `captions` each sorted by time. Validate before you finish: the file loads with `python3 -c "import json; json.load(open(PATH))"`, every staff name is one of the report's names, every position is inside the movement, durations and gaps follow the rules above (use the bar report's times).

Do not change any other file. Return a short plain summary: how many splits and notes, the bars of each, and anything you were unsure of and left out.
