# Assets (source URL, licence)

Note: the project file store adds a C2PA provenance block (about 5.8 kB) to audio files when they are written here,
so checksums differ from the source files; the audio streams are unchanged.

## Reference recordings (assets/refs/), measured with tools/measure.py (results in critics/c00/ref_*)
- refs/brahms1_i_musopen.flac — Brahms, Symphony No. 1 in C minor, Op. 68, I. Un poco sostenuto – Allegro (15:09). Czech National Symphony Orchestra, Musopen Kickstarter recording (2012), 24-bit/48 kHz FLAC. Source: https://archive.org/details/musopen-dvd-in-lossless-flac-format (file "Brahms - Symphony No 1 in C Major/Symphony No. 1 in C Minor, Op. 68 - I. Un poco sostenuto - Allegro.flac"). Licence: Public Domain Mark 1.0 (http://creativecommons.org/publicdomain/mark/1.0/).
- refs/brahms4_i_musopen.flac — Brahms, Symphony No. 4 in E minor, Op. 98, I. Allegro non troppo (12:41). Same orchestra, source and licence as above (file "Brahms - Symphony No 4 in E minor/Symphony No. 4 in E Minor, Op. 98 - I. Allegro Non Troppo.flac").
- refs/dvorak9_i_columbia.mp3 — Dvořák, Symphony No. 9 in E minor, I. Adagio – Allegro molto (9:50). Columbia University Orchestra, 2002, live, 128 kb/s MP3 (student orchestra; lower technical quality, use for dynamics more than for timbre). Source: https://archive.org/details/Dvorak_Symphony_9 (file 01.Adagio-Allegro_Molto.mp3). Licence: Creative Commons public domain dedication (http://creativecommons.org/licenses/publicdomain/).
- refs/brahms1_ii_musopen.flac — Brahms, Symphony No. 1, Op. 68, II. Andante sostenuto (8:37), and refs/brahms4_ii_musopen.flac — Brahms, Symphony No. 4, Op. 98, II. Andante moderato. Slow-movement references for movement II, added by critic 4 (2026-10-10), measured in critics/c04/ref_brahms1_ii_musopen and ref_brahms4_ii_musopen. Same orchestra, source archive and licence as the Brahms first movements above: https://archive.org/details/musopen-dvd-in-lossless-flac-format (files "Brahms - Symphony No 1 in C Major/Symphony No. 1 in C Minor, Op. 68 - II. Andante sostenuto.flac" and "Brahms - Symphony No 4 in E minor/Symphony No. 4 in E Minor, Op. 98 - II. Andante Moderato.flac"), Public Domain Mark 1.0.
- refs/tchaikovsky6_i_musopen.flac — FAILED DOWNLOAD, do not use: it holds a 2 kB Wikimedia "429 Too many requests" HTML page, not audio (kept because files here are never deleted). Intended source: https://commons.wikimedia.org/wiki/File:Tchaikovsky_-_Symphony_No._6_in_B_minor,_Op._74_%27Path%C3%A9tique%27_-_I._Adagio_-_Allegro_non_troppo_(Musopen_Symphony).flac (Musopen, public domain). upload.wikimedia.org rate-limits this container's shared IP; retry later into a new file name.

## Soundfonts (assets/sf2/)
- sf2/MuseScore_General.sf2 (v0.2, 216 MB) with MuseScore_General_License.md and _Readme.md. Source: https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/ . Licence: MIT (derived from FluidR3 / FluidR3Mono; the acknowledgements in the licence file must be kept). Calibration: critics/c00/sfcal_MuseScore_General/.

## Impulse responses (assets/ir/)
- ir/detmold_konzerthaus_setC_R163/ — Omni_S{1..8}R163.wav and Fig8_S{1..8}R163.wav (48 kHz, 1.5 s, unchanged files): Detmold Konzerthaus (about 600 seats, RT30 about 1.6 s), Set C "loudspeaker orchestra" (8 loudspeakers at orchestra positions, S1-S4 on the stage floor, S5-S8 on the second step; S1 and S5 are audience left, checked from the dummy-head level differences), receiver seat R163 (stalls, about 20 m from the stage), omnidirectional and figure-of-eight microphones measured together (figure-of-eight positive lobe to the left). Source: Zenodo record https://zenodo.org/records/4116247 (file DetmoldSRIR_v01.zip, folders SetC_DenseKH_LSOrchestra/Data/Omni and /Fig8; only these 16 files were extracted, by HTTP range requests, because the full 986 MB zip downloads at about 50 kB/s here). Licence: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Credit: S. V. Amengual Garí, B. Sahin, D. Eddy, M. Kob, "Open Database of Spatial Room Impulse Responses at Detmold University of Music", 149th AES Convention, 2020. Used by r01/stem.py.

## Virtual Playing Orchestra 3 subset (assets/vpo3/), added by actor 2 (r02)
- vpo3/Strings/{1st-violin,2nd-violin,viola,cello,bass}-SEC-{sustain,staccato,pizzicato,tremolo,accent}.sfz,
  vpo3/Percussion/{timpani-roll,timpani-hit,cymbals,misc}.sfz (unchanged "Standard" SFZ files, VPO 3.3 scripts) and only
  the 450 wave files these string and timpani files reference plus the gong, suspended-cymbal crescendo and crash
  samples r02 uses (vpo3/libs/..., unchanged, same relative paths as in the release), and vpo3/Documentation/license.htm.
  Source: Virtual Playing Orchestra 3.2 wave files, https://archive.org/download/virtual-playing-orchestra-3-2-wave-files/Virtual-Playing-Orchestra3-2-wave-files.zip
  (also https://drive.usercontent.google.com/download?id=17bY90ybtA5CyNJMnQ4KK9i5YO3tCN7HR&export=download&confirm=t), SFZ scripts
  https://virtualplaying.com/vp-downloads/Virtual-Playing-Orchestra3-3-standard-scripts.zip ; downloaded by critic 1 to /tmp and copied here.
  Licence (https://www.virtualplaying.com/virtual-playing-orchestra/ and Documentation/license.htm): free for any music; redistribution with
  credit allowed, not for sale. Sources inside: Sonatina Symphonic Orchestra (CC Sampling Plus 1.0), Mattias Westlund samples (CC BY-SA 3.0),
  No Budget Orchestra (CC BY-SA 4.0), VSCO 2 Community Edition (CC0 1.0), University of Iowa MIS (free use). Credit: Paul Battersby, virtualplaying.com.
  Played by r02/sfzplay.py (own Python SFZ player; no SFZ software installed).

## VSCO 2 Community Edition harp and flute staccato (assets/vpo3/libs/VSCO2-CE/), added by actor 4 (r04)
- vpo3/libs/VSCO2-CE/Strings/Harp/KSHarp_*.wav (18 files, 16 mf + D7/F7 f, 44.1 kHz stereo) and
  vpo3/libs/VSCO2-CE/Woodwinds/Flute/stac-PB/LDFlute_stac_*-PB.wav (10 files, 44.1 kHz mono), unchanged, same relative
  paths as in the release. Fetched one by one from the zip index of the Virtual Playing Orchestra 3.2 wave archive:
  https://archive.org/download/virtual-playing-orchestra-3-2-wave-files/Virtual-Playing-Orchestra3-2-wave-files.zip/
  (folder Virtual-Playing-Orchestra3/libs/VSCO2-CE/...). Licence: VSCO 2 Community Edition is CC0 1.0
  (https://versilian-studios.com/vsco-community/); VPO redistribution terms as above. Played by r04/sfzplay.py through
  r04/sfz/harp-vsco2.sfz (harp, used) and r04/sfz/flute-stac-vsco2.sfz (flute staccato; tested in r04 and not enabled,
  see r04/NOTES.md). Pitch check (r04): harp names follow C4 = MIDI 60, about 8 cents flat; the flute file names are one
  octave below MIDI convention (file C3 = MIDI 60).
- iowa/ (added by actor 5, r05, 2026-10-10): University of Iowa Electronic Music Studios, Musical Instrument Samples
  (MIS), pre-2011 woodwind sets: Bb clarinet, bass clarinet, oboe, flute (vibrato), bassoon, each as chromatic runs per
  octave at pp, mf and ff (44.1 kHz mono AIFF), from https://theremin.music.uiowa.edu/MIS.html (pages MISBbclarinet.html,
  MISbassclarinet.html, MISoboe.html, MISflute.html, MISbassoon.html; files under
  https://theremin.music.uiowa.edu/sound%20files/MIS/Woodwinds/). Terms on the site: the samples "may be downloaded and
  used for any projects, without restrictions". iowa/src/<instrument>/ holds the downloaded files unchanged (62 files,
  about 200 MB); iowa/<instrument>/ holds the per-note WAVs cut from them by r05/build_iowa.py (key_dyn.wav, 24-bit,
  levelled per layer, with build_log.txt); the SFZ maps are r05/sfz/*-iowa*.sfz (played by r05/sfzplay.py).
- iowa/bassoon-r06/, iowa/oboe-r06/, iowa/bassclarinet-r06/ (added by actor 6, r06, 2026-10-10): per-note WAVs re-cut by
  r06/build_iowa.py --pitch-onset from the unchanged files in iowa/src/ (same source and terms as iowa/ above). A note whose
  run was played without a gap starts where its own pitch is established (YIN f0 in 10 ms hops), not in the previous
  note's tail, with a 5 ms fade-in (critic 5: 105 of 122 bassoon and 13 of 102 oboe samples began with the previous
  semitone). The r05 folders iowa/bassoon, iowa/oboe, iowa/bassclarinet are left unchanged for r05.
- iowa/src/horn/ (downloaded by actor 6, r06, 2026-10-10, not yet used): University of Iowa MIS pre-2011 French horn
  chromatic runs, 12 AIFF files (Horn.{pp,mf,ff}.*.aiff), from https://theremin.music.uiowa.edu/MISFrenchhorn.html (files under
  https://theremin.music.uiowa.edu/sound%20files/MIS/Brass/frenchhorn/), same terms ("may be downloaded and used for any
  projects, without restrictions"). The set has no pp C2-B3 and no mf C3-B3 (those URLs return 404), the horn's core
  register, so a horn map needs layer filling or the 2014 per-pitch ff files (MIS-Pitches-2012/MISHorn2012.html).
