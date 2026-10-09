# v25: response to critic 5 (lens: engraving), report critics/reports/c005.md

Accepted:
1. **Part-combiner errors in tutti woodwinds.** `\partCombineApart` is now forced at 27–32, 123–130, 163–166 and 82, so both players show complete rhythms, rests included.
2. **Hairpins running through empty bars** fixed at 14, 84 (horns 3·4 and timpani), 107 and 136. Each hairpin now ends on a note with a target dynamic, or on a terminated rest in an unshared staff.
3. **Duplicated dynamics on shared staves.** The critic proposed deleting player 2's copy in assemble.py. Instead, the Dynamic_engraver now runs at Staff level (score.ly), so a shared dynamic or hairpin prints once per staff. Two simultaneous different dynamics on one staff are now reported as conflicts; the two that occurred (bassoons at 91 and 107) were made equal. This does not undo cycle 4's trumpet-2 decision: trumpets 1·2 still share one marking.
   - Rejected sub-point: a first attempt also moved Dynamic_align_engraver to Staff level, and LilyPond reported 280 layout programming errors, so that engraver stays in Voice.
4. **First page** shows every instrument (`\RemoveEmptyStaves`). The percussion staff is named "Cymbals / Tam-tam", hides when empty, and the two strokes carry "l.v.". Splitting it into two staves was not done: two staves for two notes adds height without information.
5. **Rehearsal marks** are boxed and larger, with new letters at 69, 97, 109, 139, 154 and 167. That gives twelve marks; the development now has three.
6. **Tempo words:**
   - "a tempo" at 69 and 77;
   - "Poco più tranquillo" at 73;
   - "Allegro appassionato (Tempo dell'Allegro)" at 163;
   - "Tempo I (Lento)" at 175.
7. **System breaks** before 47, 77, 139 and 163. The score is now 14 pages.
8. **Flute ottavas** removed from the shared flute staff. Horns 3·4 use bass clef at 11–12.

One cosmetic warning remains ("decrescendo too small" at a horn hairpin in the development).
