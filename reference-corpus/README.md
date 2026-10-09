# Reference corpus: orchestral scores in LilyPond

Purpose: models to compare the symphony against while composing (form, orchestration, texture, harmonic rhythm, idiomatic writing). All sources were upgraded to LilyPond 2.24 syntax with `convert-ly` and test-compiled with LilyPond 2.24.3. Compiled PDFs are in `pdf/`.

Works are public domain; the typeset editions carry the licences listed below.

## Layout

- `mutopia/<Composer>_<Opus>/…` — hand-engraved LilyPond sources from the Mutopia Project (https://www.mutopiaproject.org, git mirror github.com/MutopiaProject/MutopiaProject). Each work keeps Mutopia's own folder structure: one file per instrument, included into a conductor score.
- `musicxml-converted/xml/` — MusicXML of four complete symphonies from the MCTL Symphony Dataset (github.com/kyuchia/mctl-symphony-dataset, MIT licence for the dataset; scores are MuseScore community editions, source URL in each file's header).
- `musicxml-converted/ly/` — the same symphonies converted to LilyPond with `musicxml2ly` (machine-generated: correct notes and instruments, cruder layout and spelling of some markings).
- `musicxml-converted/annotations/` — MCTL's form, harmony and cadence analyses (CSV + PDF) for the movements where they are small enough to keep. The full note-level and orchestral-layer annotations (~570 MB) were left in the upstream repository.
- `pdf/` — PDFs compiled from the entry files below.

## Index

Status: **clean** = compiles with no errors; **minor errors** = PDF produced, a few markings lost; **source only** = LilyPond source is readable but does not compile under 2.24.

### Late-Romantic and Romantic (primary models)

| Composer | Work | Movements | Instrumentation | Source / licence | Entry file | Status |
|---|---|---|---|---|---|---|
| Tchaikovsky | Symphony No. 6 in B minor "Pathétique", Op. 74 | all 4 | 3 fl (3rd doubling picc), 2 ob, 2 cl (A), 2 bsn, 4 hn, 2 tpt, 3 tbn, tuba, timp, perc, strings | MCTL / MuseScore (musescore.com/user/19710/scores/7569779 etc.) | `musicxml-converted/ly/Tchaikovsky_Sym6_mvt{1-4}.ly` | mvt 1, 2 minor errors (mvt 1 lays out on very large pages); mvt 3, 4 minor errors |
| Dvořák | Symphony No. 9 in E minor "From the New World", Op. 95 | all 4 | 2 fl (picc), 2 ob (ca), 2 cl, 2 bsn, 4 hn, 2 tpt, 3 tbn, tuba, timp, perc, strings | Mutopia #1793, CC BY-SA 3.0 | `mutopia/DvorakA_O95/Sym9/Sym9-lys/Mvt{1..4}_*.ly` | minor errors (a transposition macro fails in places) |
| Dvořák | Symphony No. 9 (second edition) | all 4 | as above | MCTL / MuseScore (musescore.com/score/4602736, 4820736) | `musicxml-converted/ly/Dvorak_Sym9_mvt{1-4}.ly` | minor errors |
| Dvořák | Symphony No. 7 in D minor, Op. 70 | all 4 | 2 fl (picc), 2 ob, 2 cl, 2 bsn, 4 hn, 2 tpt, 3 tbn, timp, strings | Mutopia #1901, Public Domain | `mutopia/DvorakA_O70/DvorakSYMPH7/DvorakSYMPH7-lys/DvorakSYMPH7_conductor.ly` (210 pp.) | clean (after patching two 2.24 incompatibilities) |
| Tchaikovsky | Violin Concerto in D, Op. 35 | all 3 | solo vn, 2 fl, 2 ob, 2 cl, 2 bsn, 4 hn, 2 tpt, timp, strings | Mutopia #466, Public Domain | `mutopia/TchaikovskyPI_O35/tchai_op35/tchai_op35-lys/tchai_op35.ly` | clean |
| Grieg | Peer Gynt Suite No. 1, Op. 46: "Åse's Death", "Anitra's Dance" | 2 nos. | strings (+ triangle) | Mutopia, Public Domain | `mutopia/GriegE_O46/03-anitrasdance/…/anitrasdance.ly`, `02-lamortdase-strings/…/aasesdeath.ly` | clean |
| Mendelssohn | Psalm 42 "Wie der Hirsch schreit", Op. 42 | complete | SATB soli and choir, orchestra | Mutopia #1947, Public Domain | `mutopia/Mendelssohn-BartholdyF_O42/…/score.ly` | clean |

### Beethoven (motivic development, sonata-form pacing)

| Work | Movements | Instrumentation | Source / licence | Entry file | Status |
|---|---|---|---|---|---|
| Symphony No. 9 in D minor, Op. 125 | all 4 | full orchestra, choir in finale | MCTL / MuseScore | `musicxml-converted/ly/Beethoven_Sym9_mvt{1-4}.ly` | mvts 1, 2 clean; 3, 4 minor errors |
| Symphony No. 3 in E♭ "Eroica", Op. 55 | all 4 | 2 fl, 2 ob, 2 cl, 2 bsn, 3 hn, 2 tpt, timp, strings | Mutopia #1655, CC BY-SA 3.0 | `mutopia/BeethovenLv_O55/…/ScoreMvt{I..IV}.ly` | clean (after a small 2.24 patch in `defs.lyi`) |
| Symphony No. 7 in A, Op. 92 | 1 and 2 | 2 fl, 2 ob, 2 cl, 2 bsn, 2 hn, 2 tpt, timp, strings | Mutopia #595, #891, Public Domain | `mutopia/BeethovenLv_O92/Symphony7_{1,2}/…` | clean |
| Coriolan Overture, Op. 62 | — | classical orchestra | Mutopia #57, Public Domain | `mutopia/BeethovenLv_O62/Coriolan/Coriolan-lys/coriolan.ly` | clean |
| Egmont Overture, Op. 84 | — | classical orchestra + picc | Mutopia #547, Public Domain | `mutopia/BeethovenLv_O84/Egmont/Egmont-lys/Egmont.ly` | clean |
| Piano Concerto No. 3 in C minor, Op. 37 | 1 | piano, classical orchestra | Mutopia #899, Public Domain | `mutopia/BeethovenLv_O37/…/Concerto_No3.ly` | clean |
| Violin Concerto in D, Op. 61 | all 3 | violin, classical orchestra | Mutopia #990, #1021, #1165, Public Domain | `mutopia/BeethovenLv_O61/violin_concerto_{1,2,3}/…` | clean |

### Classical and early-Romantic (clarity of texture, part-writing)

| Composer | Work | Instrumentation | Source / licence | Entry file | Status |
|---|---|---|---|---|---|
| Mozart | Symphony No. 41 in C "Jupiter", K. 551, all 4 mvts | fl, 2 ob, 2 bsn, 2 hn, 2 tpt, timp, strings | MCTL / MuseScore (musescore.com/score/4861738) | `musicxml-converted/ly/Mozart_Sym41_mvt{1-4}.ly` | clean |
| Mozart | Symphony No. 25 in G minor, K. 183, mvts 1–2 | 2 ob, 2 bsn, 4 hn, strings | Mutopia #1380, Public Domain | `mutopia/MozartWA_KV183/…` | clean |
| Mozart | Symphony No. 18 in F, K. 130 | 2 fl, 4 hn, strings | Mutopia #346, Public Domain | `mutopia/MozartWA_KV130/k130/k130-lys/k130-score.ly` | clean |
| Mozart | Masonic Funeral Music, K. 477 | winds, strings | Mutopia #448, Public Domain | `mutopia/MozartWA_KV477/k477/k477-lys/k477-score.ly` | source only (LilyPond 2.4 syntax) |
| Méhul | Symphony No. 1 in G minor, all 4 mvts | classical orchestra | Mutopia #1644, Public Domain | `mutopia/MehulEN_Symphonie-1/Symphonie-1-lys/Score-{1..4}.ly` | minor errors (title markup) |
| Rossini | Eduardo e Cristina, overture | full early-Romantic orchestra with trombone, percussion | Mutopia #1634, Public Domain | `mutopia/RossiniG_Eduardo_e_Cristina/Eduardo_e_Cristina-lys/Score.ly` | minor errors (title markup) |

## Changes made to upstream files

- All Mutopia `.ly/.ily/.lyi/.lyp` files run through `convert-ly` to 2.24 (files without a `\version` converted from the version the rest of the work uses).
- Dvořák 7, `Common/Paper-*.ly`: `\on-the-fly #not-first-page` etc. replaced by 2.24's `\if`/`\unless` page conditions; `Common/Fonctions.ly`: accented-capital helper reduced to `string-upcase` (the original split UTF-8 bytes, which fails under Guile 2).
- Eroica, `defs.lyi`: `override-auto-beam-setting` calls commented out (removed from LilyPond); `unfold-repeats` call given its 2.24 signature.
- MusicXML conversions: bracket and parenthesis pseudo-dynamics (`[`, `]`, `(`, `)`) that `musicxml2ly` emitted as invalid identifiers were removed.
- Grieg's "In the Hall of the Mountain King" and piano "Åse's Death" in the Mutopia folder are piano arrangements and were left out.

## Gaps

Nothing from after about 1895 is here yet: no Mahler, Elgar, Rachmaninoff, Sibelius, Vaughan Williams, Barber or Korngold. LilyPond editions of their orchestral works are not freely available (most are either still in copyright in some editions or exist only as PDFs on IMSLP). Possible later additions: MuseScore/OpenScore MusicXML of Elgar, Rachmaninoff or Sibelius symphonies via the PDMX dataset, converted with `musicxml2ly` the same way as above.
