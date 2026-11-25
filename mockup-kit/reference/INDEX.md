# Reference mockups for study

> **Not in this repository.** The project files and MIDI files described below (`eastwest-templates/`, `bernard-duc/`, `cubase-vsl/`, `expert-midi/`, `lorne-balfe/`) are other people's work and were removed from the repository and its history. This page stays as the list of what was studied and where each file came from. Claude's measurements of them are in `symphony/mockup-research/ew-template-2026-11-08/` and `rppstrip.py` is the project's own tool.

These are other people's mockup files, collected on 2026-11-08 by the thread "Find sample mockup projects to study", so the mockup threads and their critics can open the originals. What was measured in them is in `symphony/mockup-research/ew-template-2026-11-08/FINDINGS.md` (parts are named below), with the statistics next to it (`expert-report.txt`, `cubase-report.txt`, `balfe-report.txt` and the others listed in that folder's `README.md`).

Most of these files are fan or composer mockups of copyrighted film scores, shared free by their authors for study. They were used for study only and are not redistributed here.

## Analysis tools
The scripts are in `symphony/mockup-research/ew-template-2026-11-08/scripts/` (run with `python3 -I`):
- `smf2.py out.json file.mid ...`: per-track timing, overlap, repeated-note, velocity and CC statistics and phrase shapes (`LANES=1,11,2` picks the CC lanes). `rubato.py` (beat-level tempo), `async.py` (tutti entry spread), `balfe_extra.py` (shared CC lanes, CC11 against CC1, phrase entries), `accent.py` (short-note velocity by position in the beat).
- `cpr2mid.py in.cpr out.mid` converts a Cubase project's MIDI parts, tempo track and controller curves into a MIDI file; `vepdump.py file.cpr` prints the Vienna Ensemble Pro mixer stored inside it.
- `rppmix.py`, `rppau.py`, `proq2.py`, `extract_fx.py`, `fxstate.py` read REAPER projects: routing, sends, plugin states, Pro-Q 2 bands.
- `rppstrip.py` (in this folder) removes large plugin-state blobs from a REAPER project; it made the EastWest study copies below.

## Contents

### `eastwest-templates/`: EastWest's own REAPER templates (FINDINGS parts 1-2)
Templates 2 (2026), free from https://www.soundsonline.com/templates-2.
- `hollywood-orchestra/EW Hollywood Orchestra Template (Midi Included) - study copy.RPP`: 59 tracks with EastWest's demo MIDI, routing, bus EQ and Spaces II reverbs.
- `composercloud-plus/EastWest ComposerCloud+ Template (Midi Included) - study copy.RPP`: 86 tracks, with the "CC+ demo" MIDI.
- The two Media MIDI files that came with them, both ReadMe PDFs and the Setup Guide.

In the study copies, each Opus instrument's plugin state (96-100 MB of the 97-102 MB original) has been replaced by a one-line note, so the files are for reading, not for opening in REAPER. What was read from those states (loaded mics and levels, the CC1 macro) is in `opus-mics.txt` and FINDINGS section 6. The full templates, and their No-Midi and Reaticulate variants, are in the zips at https://media.soundsonline.com/zip/HO-Reaper-EW-2026-Template.zip and https://media.soundsonline.com/zip/CC-Reaper-EW-2026-Template.zip.

### `bernard-duc/`: two complete REAPER projects with their MIDI (FINDINGS part 4, sections 13-14; `duc-mix.txt`)
- `Duc_Bernard_Adagietto_Mahler5th_v1.RPP` and `Duc_Bernard_Mahler_adagietto.MID`: Mahler 5 Adagietto (Cinematic Studio Strings, Embertone solo violin, VSL harp). The tempo map follows a commercial recording beat by beat; the recording itself and the room-noise WAV are not included (only referenced by path).
- `DucBernard_LOTR The White Tree_v2.RPP` and `DucBernard_LOTR_TheWhiteTree_v1.MID`: LOTR "The White Tree" (VSL woodwinds, Spitfire Symphonic Brass, Cinematic Studio Strings).
Both projects keep their full Vienna Ensemble Pro state (21 MB in the Mahler). Found through VI-Control's "Consolidated list of MIDI mockups and project files for study" (https://vi-control.net/community/threads/consolidated-list-of-midi-mockups-and-project-files-for-study.169383/).

### `cubase-vsl/`: two Cubase projects with VSL Synchron instruments (FINDINGS part 5; `cubase-report.txt`, `cubase-mix.txt`)
- `Goldsmith - Mulan overture.cpr` (68 MIDI tracks) and `Hisaishi - Howl's Moving Castle - Merry-Go-Round.cpr` (63 tracks). Each holds its tempo track, controller curves, Lexicon hall settings and the whole Vienna Ensemble Pro mixer. Use `cpr2mid.py` and `vepdump.py` to read them. Shared on Dropbox via the same VI-Control list.

### `expert-midi/`: MIDI mockups (FINDINGS parts 3-4; `expert-report.txt`, `polar-report.txt`)
| file | tracks | notes | notes on the file |
|---|---|---|---|
| `ashton-gleckman/atonement.mid` | 54 | 3,676 | Ashton Gleckman suite, mostly Spitfire |
| `ashton-gleckman/bandofbrothers.mid` | 19 | 1,080 | |
| `ashton-gleckman/danish.mid` | 38 | 6,919 | The Danish Girl |
| `ashton-gleckman/davinci.mid` | 39 | 4,416 | The Da Vinci Code |
| `ashton-gleckman/hp78.mid` | 86 | 10,329 | Harry Potter 7/8 |
| `ashton-gleckman/hunger.mid` | 205 | 6,911 | The Hunger Games |
| `ashton-gleckman/imitation.mid` | 69 | 10,649 | The Imitation Game |
| `ashton-gleckman/lionking.mid` | 32 | 1,808 | |
| `ashton-gleckman/martian.mid` | 61 | 2,306 | |
| `ashton-gleckman/pirates.mid` | 46 | 4,672 | Pirates of the Caribbean |
| `ashton-gleckman/shape.mid` | 122 | 4,930 | The Shape of Water |
| `ashton-gleckman/polar-express.mid` | 36 | 1,041 | Polar Express suite, hand-played (FINDINGS part 3); from https://www.youngcomposers.com/t39728/ |
| `four-cue-set/Finding Nemo - Main Title.mid` | 18 | 328 | Spitfire Originals, LABS, Symphonic Strings |
| `four-cue-set/LOTR - Concerning Hobbits.mid` | 17 | 1,798 | |
| `four-cue-set/No Time to Die - Final Ascent.mid` | 17 | 1,973 | |
| `four-cue-set/No Time to Die - Matera.mid` | 24 | 819 | |
| `other/Star Wars main title (2024).mid` | 67 | 5,851 | Cinematic Studio series, played in, tempo map |
| `other/Zimmer - Time.mid` | 29 | 5,158 | VSL brass, hybrid |
| `other/Newton Howard - The Village.mid` | 43 | 4,001 | track names lost in export, all played in |

The Ashton Gleckman suites came from his Dropbox links on VI-Control (https://vi-control.net/community/threads/film-score-project-files-download-hub.73680/ and the consolidated list); the others from the consolidated list and the threads it links.

### `lorne-balfe/`: Lorne Balfe's own sketch mockups (FINDINGS part 6; `balfe-report.txt`)
The Crown main titles, Kung Fu Panda 3 "Father and Son", Bad Boys for Life main theme (with Mark Mancina), 6 Underground "I Am the Danger", Penguins of Madagascar main theme and Genius season 2 main titles. From 14th Street Music's Hightail shares, downloaded and uploaded by Dan. The share pages are listed in `symphony/mockup-research/ew-template-2026-11-08/README.md`.

## Not included
- The full EastWest template projects (download links above).
- Lorne Balfe's Cubase projects for the six cues (on the same Hightail pages) and nine other 14th Street Music shares, which nobody has downloaded yet.
- Ludwig Göransson's "Can You Hear the Music" (Oppenheimer) MIDI: its Dropbox link needs a key the post doesn't give. Two downloads named `oppenheimer.mid` and `opp.mid` turned out not to be MIDI files and were dropped.
