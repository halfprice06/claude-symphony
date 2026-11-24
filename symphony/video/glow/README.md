# Glowing-score videos (all four movements)

A video style made in October 2026 for movement II to match a screen recording Dan shared (the look of animated-score channels on YouTube), now made for every movement. The whole movement is engraved on one long line and shown as a dark sheet seen at an angle by a slowly moving camera. Each note lights up in its part's colour while it sounds, and a light for each part jumps through the air from note to note. The audio is each movement's final REAPER mockup.

![Movement II, frame at bar 57 (October excerpt)](preview-bar57.jpg)

## Rebuild

```
apt-get install -y lilypond ffmpeg      # LilyPond 2.24
pip install numpy pillow opencv-python-headless cairosvg
symphony/video/glow/make-glow-video.sh mvt1 path/to/mvt1-mockup-c63.mp3                  # whole movement
symphony/video/glow/make-glow-video.sh mvt2 path/to/mvt2-mockup-c57.mp3 --bars 53 64      # excerpt
symphony/video/glow/make-glow-video.sh finale path/to/mvt3-mockup-c30.mp3 --still 212     # test frames (score seconds), no MP4
```

| Movement | Score (main) | Mockup audio | Tempo map, stem loudness | Head |
|---|---|---|---|---|
| `mvt1` | `symphony/mvt1/v621` | `mvt1-mockup-c63.mp3` | `data/mvt1-c63-*` | 0 |
| `mvt2` | `symphony/mvt2/v600` | `mvt2-mockup-c57.mp3` | `data/mvt2-c57-*` | 0 |
| `scherzo` | `symphony/scherzo/v600` | `scherzo-mockup-c30.mp3` | `data/scherzo-c30-*` | 0 |
| `finale` | `symphony/mvt3/v600` | `mvt3-mockup-c30.mp3` | `data/finale-c30-*` | 0.30 s |

The mp3s are not in the repo (they are in the project's shared folder and in the local REAPER work folders on the Mac, `symphony/<mvt>/reaper-v6xx/cycles/cNN/`). The first run engraves the strip into `build/<movement>/` (1 to 5 minutes); later runs reuse it, so delete that folder after changing the score or the tools. The MP4 goes to `<movement>-glow-video.mp4` here (or `OUT=`) and is not committed. A whole movement takes 20 to 35 minutes on 4 cores (`JOBS=` parallel parts, default all cores).

`data/` holds what the video needs from the local mockup work folders, which are not committed:
- `<mvt>-<cycle>-tempo.json`: the `tempo` list of that cycle's `parts.json` (`[qn, bpm]` steps, the tempo map REAPER played) and `head_s`, the audio before score qn 0 in the delivered mp3 (the finale keeps 0.30 s of pre-roll since its c23; the others start at qn 0). Checked against the audio: the onsets of all four land within 0.02 s of the map.
- `<mvt>-<cycle>-stems.npz`: the loudness of every stem of that render in 50 ms frames (`db`, one row per stem in `names`), for the camera.

## How it works

1. **`tools/build-strip.sh`** copies the version's sources and runs **`tools/make_strip_ly.py`**, which edits `score.ly` as text: titles and the front-matter bookpart go, staff size 18, `ly:one-line-breaking` so the whole movement is one system, `\RemoveEmptyStaves` removed so every staff stays, MIDI-only scores dropped, and SVG `output-attributes` added to the score's own `\layout`: noteheads get the score moment `data-m` and duration `data-d` in quarter notes, bar lines `data-m`, and a small engraver names each staff symbol after its staff (the unnamed percussion staff is "Percussion"). LilyPond writes `strip.svg`; **`tools/svg_to_png.py`** renders `strip2.png` **from that same SVG** at the scale of the approved movement II strip (9.335 px per staff space), in tiles of 12000 px because Cairo stops at 32767 px (the finale's line is 44010 px). An earlier attempt engraved the PNG in a separate LilyPond run, and its line width differed slightly, so the lights missed the noteheads.
2. **`tools/glow_video.py`** reads note positions from the SVG and renders 1920×1080 frames at 30 fps into ffmpeg (H.264 CRF 18 preset slow, AAC 320k):
   - **Time:** the tempo map converts score quarter notes to seconds; `head_s` shifts the audio and its loudness envelope.
   - **Sheet:** ink on a dark blue-grey paper (`PAPER`) with slight texture, built once per strip into `build/<mvt>/flat-*.npy` and shared by the parallel parts. Light falls off away from the playing area, the sheet blurs with distance (depth of field), and there is a vignette.
   - **Camera:** a 3D pinhole camera behind and to the left of the playhead, looking along the line (`CAM` az 45°, el 38°, roll 12°, distance 1450, focal 2600; override with `CAM='{"az":40}'`). It drifts slowly. The sheet is mapped with a homography, and the jumping lights are projected with the same camera so they sit in 3D above the paper.
   - **Where the camera looks up and down the score:** the October excerpt followed hand-written featured lines (`features.py`, for v77's bars). For the whole movements the camera goes by the mockup itself: each stem's loudness over the next 2 seconds is summed per staff (winds weighted ×1.6, strings ×0.8, timpani and percussion ×0.6, since a solo wind line stands out at a lower level than a string section), and only staves that have notes in that window count, so a reverb tail does not count on bars of rest. Until the second full renders the camera chased the loudest group frame by frame with a spring, and a note on the score or a split took the target over 2 s before its time. Dan (2026-11-23): "there's a lot of moments where the camera is really jerking around, like it seems like it wants to scroll to highlight to something but before its really obvious what's trying to be focused, it jumps up to the top of the page or somewhere else". Measured over the four videos that camera made 122 moves of 100 px or more, 35 of them turned back before they arrived, 17 were followed by a stop of under 2.5 s, and in 41 of the 43 stacked splits the lower panel scrolled down the page while it opened. Now the whole path is planned before the first frame (`plan_camera`), as stays and moves. A stay is scored by how much of the loudness of the playing staves is in shot, relative to the best place at that moment; a move has a price worth 3 to 5 seconds of that, so the camera moves only where the new place is clearly better for a while. While a note on the score is shown the camera must be where the note, its box and its label are in shot, and it does not move if they already are. At a stacked split the camera's own view becomes the panel whose staves are nearer and the other panel opens over the other half of the frame, from the top or from the foot, already at its place; when the split closes, the panel nearer to what comes next becomes the whole frame again. A move starts and stops gently and never passes 1200 px/s on the paper (`MOVE_V`; a move across the whole page takes about 3 s), and it is timed to arrive before the note it is for appears or the part it brings into shot comes in (Dan, same day: "by the tiem the camera catches up the thing we want to show has passed"; the spring camera was more than half a second late for 11 of the 124 notes, up to 2.9 s). The time on the way counts against a move, so a few seconds somewhere do not look worth a long trip. A stay that no note or split asks for and that would last under 3 s is left out. Where the time between two notes is too short for the move between them, the first ends earlier or the second starts later (neither shorter than 4 s). The same measurement now gives 61 moves, none that turns back, no stop under 2.5 s and no scrolling panel; the camera is moving 5 to 11 % of the time (was 22 to 45 %), and outside the splits the view holds 71 to 88 % of what the best view at each moment would hold (was 61 to 80 %). `--camera-report` prints every move with its time and reason, which panel the camera becomes at each split, and any note that is out of shot. `--focus-report` prints the loudest group of staves in every bar.
   - **Notes:** each note gets a core about the size of its notehead (0.62 × 0.48 staff spaces, projected) and a white centre. Two halos are added: a tight one (σ 4.5 px) and a wide, faint one that tints the paper. Both pass through a soft limit so that overlapping halos of close notes do not add up to one white blob. Notes that are sounding brighten and dim with the loudness of the recording (RMS envelope). A thin ring spreads from each note as it starts. Finished notes stay faintly lit as a trail.
   - **Jumping lights:** for each part, up to three lights (one per chord voice) jump along a parabolic arc from each onset to the next, arriving as the next note starts. A light stays fully lit while it sits on a note. Before a real rest it lifts off and fades, then drops onto the next entry. Airborne lights leave a short motion trail and cast a pool of light on the paper below them.
   - Notes and lights less than 300 px in front of the camera are not drawn. In the fast movements the head of a long note can be behind the camera, and it projected as a light covering the whole frame.
   - Light film grain stops the dark gradients from banding. Keep it small (σ 1.0): at 2.2 the excerpt grew from 30 MB to 130 MB.
   - `--jobs N` splits the video into N parts rendered by separate processes; each part works out the same camera path and first steps the camera along the line through the earlier frames, so the joined video is the same as one process makes.

## One file with all four movements (Dan, 2026-11-23)

For a single upload: the four movement videos joined, with the title and each movement's heading. The movements are
not rendered again, and only the first seconds of each are encoded again (with the words on them).

Words in the corner (Dan, 2026-11-24: "the music starts as soon as the video starts and we get through the title and
movement cards faster, maybe move them into the top left corner as the music starts so we can see the score faster").
There is no title screen and no card. `tools/title_cards.py --spec cards/cards-corner.json` makes for each movement
one short segment: the movement's own first frames (to frame `corner`, a key frame) with the words on them. The join
goes on with the movement from that frame (`MOVEMENT.mp4@K`).

```
python3 tools/title_cards.py --spec cards/cards-corner.json --credits credits.json --out-dir cards/out \
  --video 10-mvt1=mvt1-glow-video.mp4 --video 20-mvt2=mvt2-glow-video.mp4 \
  --video 30-scherzo=scherzo-glow-video.mp4 --video 40-finale=finale-glow-video.mp4
python3 tools/join_videos.py --out symphony-glow-video.mp4 \
  --chapters "I. Lento — Allegro appassionato|-|II. Adagio|-|III. Scherzo: Allegro vivace|-|IV. Finale: Allegro con fuoco|-" \
  cards/out/10-mvt1.mp4 mvt1-glow-video.mp4@1000 cards/out/20-mvt2.mp4 mvt2-glow-video.mp4@500 \
  cards/out/30-scherzo.mp4 scherzo-glow-video.mp4@500 cards/out/40-finale.mp4 finale-glow-video.mp4@500
```

- Movement I (`"opening": true, "start": 90, "corner": 1000`): the segment starts 1.5 s into the movement's file, so
  the timpani roll starts 0.5 s after the video. The title stands large in the middle over the page, which is dim and
  a little out of focus; after 2.5 s it moves in 1.2 s into the top left corner and the page comes into focus. In the
  corner it reads "Symphony No. 1 in C minor" with the movement's heading and the credits under it; these words go
  at about 14 s. The strings enter at 4.1 s.
- Movements II to IV (`"corner": 500`): the heading stands in the top left corner from about 1 s to 7 s of the
  movement's file, with a soft dark patch behind it. The scherzo's heading stands in the lower left corner instead
  (`"at": "lower left"`), because its first label on the score lies in the top left corner; the lower left corner
  shows the dark space beside the page at the start of a movement.
- The sound of a movement whose segment starts later than its first frame (`"start"`) is cut at the front by the same
  amount; `join_videos.py` does this for any `@K` segment whose words segment has fewer than K frames.
- Lengths: the whole video 25:14 (with title screen and cards it was 25:39); 7.3 s of silence between two movements
  (5.3 s at the end of one, 2 s before the next) instead of 12.3 s.
- Checked on trial joins made in the cloud (Movement I's first 19 s and last 9 s, Movement II's first 11 s): first
  sound at 0.5 s, the sound offset by 0 samples against the movement's file, the pictures from frame K on are the
  movement's own.

The first design, a title screen and a card before each movement (`cards/cards.json`), is still in the tools:

```
# one frame of each movement video, one second in (the opening page before the music), as the cards' backgrounds
ffmpeg -ss 1 -i mvt1-glow-video.mp4 -frames:v 1 cards/frames/mvt1-page.png      # and mvt2, scherzo, finale
python3 tools/title_cards.py --spec cards/cards.json --credits credits.json --out-dir cards/out \
  --video 10-mvt1=mvt1-glow-video.mp4
python3 tools/join_videos.py --out symphony-glow-video.mp4 \
  --chapters "I. Lento — Allegro appassionato|-|-|II. Adagio|-|III. Scherzo: Allegro vivace|-|IV. Finale: Allegro con fuoco|-" \
  cards/out/00-title.mp4 cards/out/10-mvt1.mp4 mvt1-glow-video.mp4@250 cards/out/20-mvt2.mp4 mvt2-glow-video.mp4 \
  cards/out/30-scherzo.mp4 scherzo-glow-video.mp4 cards/out/40-finale.mp4 finale-glow-video.mp4
```

- `tools/title_cards.py` draws the cards: the opening page of the movement that follows, out of focus and dim and
  coming slowly nearer, with the words over it in the gold and the fonts of the labels on the score. Title screen 8 s
  (title, then the credits under it), movement cards 5 s. A card starts and ends in black, as every movement video
  does, so the joins need no cross-fade. `cards/cards.json` holds the words; the credits are given with `--credits`
  (a JSON list of `[role, name, detail]`) and are not kept in the repository. `--stills` writes one PNG per card.
- The cards are encoded exactly like the parts of a movement video (libx264, preset slow, CRF 18, yuv420p, 60 fps), so
  `tools/join_videos.py` can copy all pictures as they are. It refuses segments that are encoded differently.
- The sound is built once for the whole length and encoded once more (AAC, 320 kbit/s): a card has no sound, and a
  movement's sound stops about 5 s before its last frame, so a plain copy would leave holes in the sound track. Each
  segment's sound is filled or cut to exactly the length of its pictures (800 samples a frame), so sound and picture
  stay together from the first segment to the last. Checked on a test join: every frame one sixtieth of a second after
  the one before, no decoding error, the sound of a clip inside the joined file offset by 0 samples.
- `--chapters` prints the start time of each chapter for the video's description. The title screen is shorter than
  the 10 s a chapter must have on YouTube, so the first chapter starts at 0:00 and includes it.
- The first design's opening (Dan, 2026-11-23: "we could start the timpani roll somewhere behind the opening two cards its a bit slow
  opening before we get to any sounds"). Movement I's file has 2 s of silence and then the timpani roll alone for three
  beats (3.6 s). With the title 12 s and the card 5 s, the first sound came after 19 s. Now Movement I's card
  (`"handover_cut": 250` in `cards/cards.json`, 4.5 s) lies over the first 250 frames of the movement: its background
  is the movement's own picture, out of focus and dim, the roll starts 2.3 s into the card, then the picture comes
  into focus, the words go, and the card's last ten frames are the movement's own. The join takes the movement from
  frame 250 (`mvt1-glow-video.mp4@250`, a key frame: x264 sets one every 250 frames, and the copy can only start at
  one) and starts its sound 250 frames earlier, behind the card. First sound after 10.3 s, the strings after 13.9 s.
  Checked on a test join made from the first 9 s of the movement: the frames from 250 on are identical to the
  movement's, the sound is offset by 0 samples, and it starts at 10.333 s.
- A 4K copy for the upload (Dan, 2026-11-23, chose it over a true 4K render of 3.5 to 7 hours). It is the joined
  1080p file enlarged to 3840x2160: no more detail, but YouTube gives an upload of 1440p or more a better codec and
  bit rate. The pictures are scaled in YUV, so their values are not converted; the colour fields are only labelled
  bt709 (the 1080p files have no labels). The sound is copied.
  ```
  ffmpeg -i symphony-glow-video.mp4 \
    -vf "scale=3840:2160:flags=lanczos,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv" \
    -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a copy -movflags +faststart symphony-glow-video-4k.mp4
  ```
  For the 25:39 file: 36 minutes on the Mac Studio, 4.95 GB (3.5 times the 1080p file). Checked: 92,354 frames, the
  whole file decodes, the sound packets are identical, and frames scaled back to 1080p differ from the 1080p file by
  about 0.5 of 255 on average.

## Changes Dan asked for (2026-10-13/14, movement II excerpt)

| Pass | Dan's note | Change |
|---|---|---|
| 1 | Match the paper angle of his recording; the notes bounce through the air; the lights were not exactly on the notes | 3D camera tuned against frames of the recording; jumping lights added; PNG rendered from the same SVG |
| 2 | "much closer", but close notes blurred together | Notehead-sized cores, tighter halo, soft limit on summed glow |
| 3 | The lights faded on landing, then lit up again before the jump | Lights stay fully lit until they jump. Also added the loudness-driven glow, strike rings, motion trails and grain |

"ok that looks good" after pass 4 (excerpt bars 53–64). The four whole-movement videos (2026-11-23) keep that look; what changed is listed above (the camera's vertical aim from the stems and how it moves, the guard against lights behind the camera, CRF 18 instead of 17 to keep a movement under 400 MB).

## Split screen, instrument names and notes on the score (Dan, 2026-11-23)

Dan saw concept clips and chose: a stacked split screen for moments where two distant groups matter at once (a pull back, or a split whose panel pulls back, where that suits the moment better), instrument names written on the paper, and analysis notes drawn on the score. His other notes: tied notes get no new jump; a note on the score must be in shot; string names were missing in the concept clip.

- `--annotations annotations/<mvt>.json`: the movement's moments, `{"splits": [...], "captions": [...]}` (format and rules in `annotations/BRIEF.md`; each file's `review` array lists what the independent check changed). Each split has its own `mode` (`stack` or `pullback`), `upper`/`lower` staves and `upper_zoom`/`lower_zoom`. Captions are drawn on the score (`--caption-style score`, the default): a bracket round the passage on its `anchor` staff, the `short` label above the bracket, chord names below the staff as the music reaches them (above, they ran into the label and the staff over it). From 2 s before a note until it ends, the camera aims at its anchor staff.
- What a panel shows. The camera looks along the line at an angle, so at the place being played a view shows much more of the paper above its focus than below (one stacked panel at zoom 1: about 300 px up, 70 px down). The annotations assumed 300 px × zoom either side of the named staff, so `fit_splits` fits each panel instead: first to any note on the score shown during the split, then to the playing staves that the split's `what` text names, then to other playing staves that need no further pull-back. It sets the panel's focus and pull-back (at most 2.0; 2.2 for a note). A pull-back is fitted the same way to its two staves.
- Travel time. A split starts to open 1.7 s before its time and has closed 0.5 s after it ends. `settle_times` trims the times where a note sits next to a split that does not show its staff, or two notes on distant staves follow each other directly (the note if it stays 4 s long, else the split if it stays 3.5 s long, else the note is shifted). The camera's plan then asks for more where a move is long (`cam_fix_times`: a move of 1,600 px takes 2.2 s), and lets a note that outlasts its split by a few seconds end with the split. The JSON files are not changed.
- `--annotations-check` prints every split with what its panels show, every note, each trim, and any problem that is left (rules of the brief, a note that fits in no panel, a note the camera cannot reach or that is out of shot for more than 1.5 s). All four files give 0 problems. Run it after editing an annotations file: `./make-glow-video.sh mvt1 AUDIO.mp3 --annotations-check`.
- A note's label is written at one fixed place on the paper: at the bracket's start, or further right when the passage is long enough that the start would leave the frame before the note goes. It is moved along its row only as far as needed to stay inside its view (`visible_span_x`), which happens mostly in the narrower panels of a split.
- The box, the label and the chord names clear the note heads: heads on ledger lines reach up to 5 staff spaces above or below the staff (a quarter of the notes in the first full render had a box line or a label through them), so the box grows to hold the passage's heads, the label sits above the box and above any heads under it, and chord names sit below the box, each as far as the gap to the next staff allows (`--annotations-check` remarks where it is not enough). A label that has been moved along its row onto an instrument name makes that name give way. A chord name gives way when the next one would run into it. A label shown in a split panel or a pull-back is written up to 1.6 times larger, but only where that does not change what the split shows or how far it pulls back. A box, label or chord name is drawn only where it lies in front of the camera (`front_runs`): in the upper panel of a split, the box of a note on a staff of the lower panel is behind the camera, and projected from there it appeared as a gold line across the panel (third videos: Movement I 6:26 to 6:28, scherzo near 1:05, 1:28 and 2:01, finale one frame at 2:15).
- `annotations/reports/<mvt>-bars.txt` (`--focus-report --focus-report-full`): the staff layout with vertical positions, then per bar the start time, the staff the automatic camera follows and the note onsets per staff. The annotation passes worked from these.
- `--labels names`: every name is printed at a fixed place on the paper and never moves on it. (The first version wrote a name at each phrase start and then kept it at the left edge of the frame; Dan, 2026-11-23: "inconsistency and almost randomness with how the instrument names appear and shift around on the page".) Two rules place them. Entry: where a part comes in after 2.5 s or more of rest, its name ends just before its first note. Column: at set bar lines about 800 px apart, the same for every staff, each part playing through that bar line has its name again, ending at the bar line, so the names line up down the page as at the start of a system. A staff never has two names closer than 500 px. A name is dim while its part rests and bright while it plays, and gives way while a note on the score is drawn over its place.
- Frame rate and camera speed (Dan, 2026-11-23: text blurred when the camera panned): the default is 60 fps. The second videos limited the camera to 900 px/s up and down the page (the first allowed 1300 px/s at 30 fps); after Dan found it too slow to reach things in time, the planned camera is allowed 1200 px/s (`MOVE_V`), about 32 px a frame on the screen at its fastest. 60 fps takes about 1.8 times as long to render.
- Ties: `make_strip_ly.py` marks every note head a tie arrives at (`data-t="1"`, from each Tie's right bound). Such a head is the same note continued: the light glides along the paper to it in 0.45 s instead of jumping, the note lights without the attack flash and the strike ring. Counts: I 341, II 148, scherzo 546, finale 517.
- Also available, not chosen: `--split slant|inset`, `--labels letters|icons`, `--caption-style bar|card` (with `--captions FILE`), and stem-based automatic split detection (it split during most loud tutti passages, so the moments are written by hand). C059 has no ♭ or ♯; `overlays.py` switches to FreeSerif/FreeSans for those characters.
