# Symphony No. 1 — Movement I: plan and brainstorm

Status: draft plan, waiting on Dan's go-ahead before composing.

## 1. The symphony as a whole (~15 minutes)

| Mvt | Character | Key | Length | Form |
|---|---|---|---|---|
| I | Lento introduction, then Allegro appassionato | C minor → (ends C minor, unresolved) | ~6:00 | Sonata form with slow introduction |
| II | Adagio cantabile | A-flat major (VI of C) | ~5:00 | ABA' song form |
| III | Allegro con fuoco → Maestoso | C minor → C major | ~4:00 | Sonata-rondo, cyclic return of the motto |

The three movements share one **motto** (see below), stated quietly at the opening of I, transformed into a lyrical line in II, and returned in C major as the brass chorale climax of III. This is the cyclic plan that Tchaikovsky (Symphony 5), Dvořák (Symphony 9) and Franck use, and it gives a short symphony a sense of being one argument.

The language is neo-Romantic in the line of Rachmaninoff (Symphony 2), Barber (Symphony 1, Adagio), Vaughan Williams, Korngold and Elgar: tonal and functional at phrase level, chromatic in the inner voices, rich in modal mixture and third relations, with long-breathed melodies and a full but transparent orchestra.

## 2. Orchestra

- 2 flutes (2nd doubling piccolo), 2 oboes, cor anglais, 2 clarinets in B♭ (A in the second theme area), bass clarinet, 2 bassoons, contrabassoon
- 4 horns in F, 3 trumpets in B♭, 2 tenor trombones, bass trombone, tuba
- Timpani (4 drums), 2 percussion (suspended cymbal, clash cymbals, bass drum, tam-tam, triangle)
- Harp
- Strings (with divisi)

This is the late-Romantic standard (Dvořák 9 / Tchaikovsky 6 / Rachmaninoff 2 size). Percussion beyond timpani is used only at two or three structural points in movement I.

## 3. Thematic material for movement I

**Motto (M).** Four notes: G – E♭↑(minor sixth) – D – C, the leap rising and then sinking by step, harmonised over a C-minor chord whose inner voice slides chromatically (E♭–E♮–F) under it. Every theme in the movement derives from either the rising sixth or the falling three-note step.

**First theme (T1), Allegro.** Restless and syncopated, first violins and violas over a pulsing cello/bass pedal. It opens with the rising sixth compressed to a fourth and rushes up in eighth notes; 8 + 8 bars (antecedent ending on V, consequent sequencing up a step and breaking off on a diminished seventh).

**Transition (Tr).** The falling three-note cell in imitation between woodwinds and strings, horns sustaining; modulates C minor → E♭ → (via its dominant) to A♭ major. Builds to a forte and then thins out.

**Second theme (T2), A♭ major, poco meno mosso.** The long-breathed melody of the movement, first in cellos and first horn in octaves (the Rachmaninoff/Tchaikovsky sound), accompanied by harp arpeggios and divided violas; 16-bar sentence with an expanded cadence. Restated by the violins (on the G string, then in octaves) with countermelody in clarinet. It is the motto's falling step stretched over two bars.

**Closing (C).** Quiet codetta in A♭ with the motto in the flute over a tonic pedal, slight darkening via the flat sixth (F♭).

## 4. Form and timings

Tempi: Lento ♩ = 50; Allegro appassionato ♩ = 120–126; T2 poco meno mosso ♩ = 104. In 4/4 throughout the Allegro (about 2 s per bar).

| Section | Bars (approx.) | Time | Key / harmony | Content and orchestration |
|---|---|---|---|---|
| Introduction | 1–14 | 0:00–1:05 | C minor, ends on V | Motto pp in low strings and bassoons over a timpani roll, answered by cor anglais; the chromatic inner voice in divided violas; swells once to f and falls back; horn call on the dominant leads to Allegro |
| Exposition: T1 | 15–32 | 1:05–1:40 | C minor | Strings, woodwinds adding weight on the consequent |
| Transition | 33–48 | 1:40–2:10 | C minor → A♭ | Imitative, crescendo to first tutti, then dissolve |
| T2 | 49–72 | 2:10–3:05 | A♭ major | Cellos + horn, then violins; harp, divided violas |
| Closing | 73–80 | 3:05–3:20 | A♭ | Flute motto, pedal, darkening |
| Development | 81–124 | 3:20–4:45 | Unstable: E minor, G minor, B major/minor, to dominant pedal | (a) T1 fragments in sequence by major thirds (A♭–E–C); (b) fugato on T1 head, low strings first; (c) T2 in minor, distorted, against T1 rhythm; (d) motto in augmentation in trombones over dominant pedal, climax ff with cymbal |
| Recapitulation: T1 | 125–136 | 4:45–5:10 | C minor | Shortened, full orchestra, then subsides |
| T2 | 137–152 | 5:10–5:45 | C major | Violins and horns, broader, the emotional high point of the movement |
| Coda | 153–170 | 5:45–6:25 | C major → C minor | Darkens via A♭ and the Neapolitan; motto in muted horns, then low strings; ends pp on a bare C-minor chord with the chromatic inner voice left unresolved, pointing to movement II |

Total about 170 bars, 6 to 6.5 minutes.

## 5. Harmonic and textural vocabulary

- Functional tonality at phrase level; colour from modal mixture (♭VI, iv in major, ♭II), third-related key areas, half-diminished and French/German sixth chords, appoggiatura chords, chromatic voice leading in inner parts, long dominant and tonic pedals.
- Avoid: pure triadic Classical phrasing for its own sake, parallel fifths/octaves in exposed outer voices, unprepared modernisms that break the style, harmonic rhythm that stays uniform for long stretches.
- Texture changes every 4 to 8 bars, as in the reference scores; tutti used sparingly (about four times in the movement) so that each one counts.
- Melody doubling conventions to follow: cello + horn, violins in octaves, flute + oboe at the octave over clarinet, bassoon doubling cellos in lyrical passages, horns as harmonic glue.
- Ranges and idioms checked against the reference scores per instrument (e.g. trumpets kept mostly below written C6, bass clarinet and contrabassoon in their idiomatic low registers, harp pedalling kept possible).

## 6. Working method: comparing against the corpus

1. Sketch first: a short-score (4 to 6 staves) LilyPond draft of the whole movement, so form, themes and harmony can be judged before orchestration.
2. Orchestrate section by section into the full score, one LilyPond file per instrument part included into a conductor score (the layout the Dvořák 7 and Beethoven 3 Mutopia scores use).
3. After each section, compile to PDF and MIDI and check:
   - **Against specific models:** Tchaikovsky 6 / I (dark slow intro into Allegro, lyrical second theme, development fugato), Dvořák 9 / I (intro to Allegro transition, horn writing, cyclic motto), Dvořák 7 / I (D-minor sonata-form drama, development technique), Beethoven 3 and 7 (motivic economy, development and recap pacing). Equivalent passages are compared side by side for texture density, doubling, register spacing, phrase length and harmonic rhythm.
   - **Automated checks** (a small Python script over the generated MusicXML/MIDI): instrument ranges, notes per bar per section compared with the reference scores, exposed parallel fifths and octaves between outer voices, unplayable intervals or double stops, bar-length errors.
   - **A critique pass** written into `symphony/critique/` listing what still sounds generic or student-like, and fixing it before moving on.
4. Render the MIDI to audio (FluidSynth with a General MIDI orchestral soundfont, if one can be installed) so the result can be heard as well as read.

## 7. Open questions for Dan

- Key and character: C minor, dark-to-heroic arc (my default), or something warmer such as a D-major pastoral opening.
- Orchestra size: the late-Romantic orchestra above (my default), or smaller (Brahms-sized, no tuba or harp).
