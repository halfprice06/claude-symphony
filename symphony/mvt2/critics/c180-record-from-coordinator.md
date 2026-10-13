# Record of movement II v181 (cycle 180), saved by the coordinator

The movement II thread's container lost access to /mnt/project-files around 21:00 UTC on 2026-10-12, with v181 built only in its local scratch. It sent this record so v181 can be rebuilt from v180 if that scratch is lost. If mvt2/v181 already exists with these changes, this file is redundant.

No music changed; score.midi is byte-identical to v180's.

1. sections/coda.ily line 27 (timpani, part-only text). In v180 the right-column text names the D♭→G retuning "(for III, during the pause)". Replace the whole line with:

```
  R2.*2 | R2.*3 | R2.\fermata -\tag #'part _\markup \small \italic \right-column { "muta A♭ in E, C in G, D♭ in B, E♭ in E" "(for the Scherzo, during the pause)" } |  % c150: part-only retuning note for the next movement (MOLA PDF 5: a change is marked at the end of the previous passage; Rimsky-Korsakov PDF 21, axiom II); c180: retuning for the scherzo (E2 G2 B2 E3), which now follows; was "muta D flat in G (for III)"
```

2. sections/bSec.ily lines 140–141 (comments only). "Movement III's chorale arrival" becomes "The finale's (now movement IV) chorale arrival", and "and III's D flat episode" becomes "and the finale's D flat episode".

Build in scratch: 0 warnings, 8 pages, 0 outer-voice parallels. The parts book was regenerated and shows the new timpani text.

## c180 report summary (cyclic lens; A&S Unit 28 Neapolitan, PDF 482–502)

- Accepted: (1) timpani muta now for the scherzo, wording from the scherzo's E, G, B, E. (6) stale "movement III" comments updated.
- Recorded, no change: (2) handover facts for the scherzo: last chord A♭1 A♭2 E♭3 E♭4 A♭4 C5, pp→ppp, fermata, rit.; strings and Cl 2 only at the end; Hn 3·4 muted to 90 with "via sord." at 91; harp silent from 83; violins peak B♭6. Common tones A♭=G♯ (3̂ of E) and E♭=D♯ (7̂). F♭/E sounds as ♭VI in mvt II, and at 62–64 it works as the dominant of the ♭ii area. Recommended scherzo opening: a direct third relation with G♯ as 3̂; keep its Neapolitan (F) until E is established. Keep C major, the D♭→C resolution, the viola D♯→E and the trumpets' B→C for the finale. (3) The symphony's long-range Neapolitan (D♭ = ♭II of C) is to be resolved in the finale, not the scherzo. (4) 61–65 follows A&S's ♭VI–♭ii–applied °7–V model; this adds a reason to keep it protected. (5) chromatic spelling is correct. (7) keep the coda's plagal close.
- Rejected: nothing.
- Open: none (the timpani text follows the scherzo's v03 tuning; update it if the scherzo's tuning changes).
- Do-not-touch: link 1–6, both quotations, the 61–65 climax, the F♭→E♭ thread, the plagal close on C5, the trumpets' silence, the 8-page layout.
