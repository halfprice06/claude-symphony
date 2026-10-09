# Critique of v5 (first full score)

Method: engraved score (pages 1 and 7 read at 70 dpi, the rest at thumbnail size), `analysis.txt`, MIDI channel dump. Rendered length 7:27. I cannot hear the audio; judgements about sound are inferred from the score.

## What v5 achieved
- All 176 bars orchestrated for the late-Romantic orchestra planned in v4, compiling without warnings.
- The introduction keeps the motto bare (cellos, basses, bass clarinet over a ppp timpani C), and the horn's premonition of the second theme is now a real solo colour.
- The second theme is split cleanly: cellos and first horn in unison over harp, then violins with the clarinet and viola countermelody, flute and oboe added only for the climb to c'''.
- The recapitulated second theme has the brass enter only for the ♭VI apotheosis, so the fff arrives as a change of colour as well as of volume.

## Tooling problems found and fixed in this loop
- **The v5 audio was wrong until this loop's last build.** With 23 staves LilyPond wrapped MIDI channels modulo 16, so the harp shared the oboes' channel, the violins the clarinets', and the double basses the flutes'. `build.sh` was filtering out the warning. Added `tools/fixmidi.py`, which gives each General MIDI program its own channel; the current `score.mp3` uses it.
- The parallels check now uses every sounding note and ignores runs of three or more parallel moves (deliberate doublings). Baseline from the corpus: Tchaikovsky 6/i gives 14 flags in 26 minutes; v5 gives 13 in 7½ minutes.
- Staves are named so the analyser reports each instrument separately; partCombine marks now read "1." / "2." / "a2" instead of "Solo".

## Real voice-leading faults (all inherited from the short score)
1. **Second theme, bars 3–4 of every statement** (bars 49–50, 58–59, 137–138, 146–147): the melody falls f→e→e♭ while the bass falls f→e→e♭ an octave or two below. These are exposed parallel octaves in the main lyrical idea, the place a listener is most attentive. Fix: bass f→d (half-diminished seventh) → e♭, which moves in contrary motion.
2. **Introduction bars 6–8**: the chromatic chord chain E♭–D♭–C in root position under the clarinet's b♭'–a♭' gives parallel fifths with the bass. Fix: first-inversion bass (g, f, e) so the outer voices move in tenths.
3. **D1 (bars 77–82)**: the tremolo chords plane A♭m–Em–Cm in root position, fifths against the bass on every change. Fix: voice-lead through the common tones (c♭ = b, g), top voice e♭'–e'–e♭'.
4. **D3 bar 101**: the melody anticipates f'' on the last eighth and the bass moves g♭→f on the downbeat, giving octaves. Fix: bass to d♭ (B♭m6/D♭) in bar 101.
5. **Coda bar 162**: horn d♭'–c' over bass d♭–c. Fix: Neapolitan sixth (bass f) resolving to C.

## Orchestration
- **Fugato first entry is too heavy.** Cellos, basses, bass clarinet and second bassoon all play the subject at f in the D2 register. A fugato should start thin so its growth is audible; start with cellos and basses at mf and add the reeds at the third entry.
- **The A-section accompaniment** (second violins and violas con sordino, harp) is idiomatic. The basses' pizzicato under a sustained horn melody may sound thin; consider arco pp.
- **Woodwinds are idle in the transition's first eight bars and through most of the fugato.** That is defensible, but the oboe and clarinet doubling at the fugato climax (bars 94–96) arrive without preparation.
- **Percussion**: only three cymbal crashes and one tam-tam stroke. That is restrained enough for the style.
- **Trumpet 1 at f'' on the B°7 hits (bar 84)** is high for a short accented chord after a rest; consider d''.

## Melody: the larger problem for later loops
Dan's brief asks for melodies that stay with the listener. The second theme's eight-bar antecedent repeats one two-bar rhythm four times (dotted half tied to an eighth, chromatic slide, turn). The consequent (bars 60–68) keeps the same rhythm. Long-breathed Romantic themes by Tchaikovsky, Rachmaninoff or Elgar usually break their opening rhythm in the consequent, with a longer note, a syncopation or a new leap, and they place one unexpected interval at the high point. This theme has no such interval. The cyclic link is available: the motto's rising minor sixth (G→E♭) could become a rising major sixth at the theme's climax. That would make the theme both more memorable and more clearly part of the motto's family.

## Plan for v6
- Fix the five voice-leading faults above.
- Thin the fugato's first entries.
- Rewrite the second theme's consequent: break the two-bar rhythm, add the rising sixth at the high point, then carry the change into D3 and the recapitulation.
