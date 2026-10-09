# Assets (source URL, licence)

Note: the project file store adds a C2PA provenance block (about 5.8 kB) to audio files when they are written here,
so checksums differ from the source files; the audio streams are unchanged.

## Reference recordings (assets/refs/), measured with tools/measure.py (results in critics/c00/ref_*)
- refs/brahms1_i_musopen.flac — Brahms, Symphony No. 1 in C minor, Op. 68, I. Un poco sostenuto – Allegro (15:09). Czech National Symphony Orchestra, Musopen Kickstarter recording (2012), 24-bit/48 kHz FLAC. Source: https://archive.org/details/musopen-dvd-in-lossless-flac-format (file "Brahms - Symphony No 1 in C Major/Symphony No. 1 in C Minor, Op. 68 - I. Un poco sostenuto - Allegro.flac"). Licence: Public Domain Mark 1.0 (http://creativecommons.org/publicdomain/mark/1.0/).
- refs/brahms4_i_musopen.flac — Brahms, Symphony No. 4 in E minor, Op. 98, I. Allegro non troppo (12:41). Same orchestra, source and licence as above (file "Brahms - Symphony No 4 in E minor/Symphony No. 4 in E Minor, Op. 98 - I. Allegro Non Troppo.flac").
- refs/dvorak9_i_columbia.mp3 — Dvořák, Symphony No. 9 in E minor, I. Adagio – Allegro molto (9:50). Columbia University Orchestra, 2002, live, 128 kb/s MP3 (student orchestra; lower technical quality, use for dynamics more than for timbre). Source: https://archive.org/details/Dvorak_Symphony_9 (file 01.Adagio-Allegro_Molto.mp3). Licence: Creative Commons public domain dedication (http://creativecommons.org/licenses/publicdomain/).
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
