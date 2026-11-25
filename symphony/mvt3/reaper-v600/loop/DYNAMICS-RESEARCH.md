# Dynamics for headphone listening: research and recommendations

Written 2026-10-11 for the mvt2 REAPER mockup loop. Problem: at one headphone volume the soft passages are too quiet and the loud ones too loud. The unprocessed master measures about -24 LUFS integrated with an LRA of 20-24 LU.

## 1. Recommendations

### Targets for the delivered mp3

| Measure | Target | Why |
|---|---|---|
| Integrated loudness | -19 LUFS (acceptable range -18 to -20) | AES TD1008 / EBU R 128 s2 put streamed music at -20 to -16 LUFS; German culture radio and rbbKultur use about -20 to -21 LUFS for classical. At -19 the true-peak limiter does about 3 dB of work on this mockup; at -18 it does about 4 dB. |
| Loudness range (LRA) | 14-16 LU | BBC Radio guideline maximum for classical music is 15 LU on every distribution path, including online (EBU Tech 3401, Table 1). The rbb/"News & Classics" profile also uses 15 LU for music. 11 LU is the speech-and-pop range and is narrower than any classical guidance found. |
| Span from quiet to climax | 16-19 dB between the 10th-percentile short-term loudness and the loudest short-term (3 s) value | Measured spread of the current chain is 8.9 dB, which is why the climax no longer sounds like a climax. |
| True peak | -1.5 dBTP before mp3 encode (measured -1.4 dBTP after a 256 kb/s encode) | Spotify asks for -1 dBTP or lower; mp3 encoding adds a little overshoot. |
| Peak limiter work | at most 3 dB on the loudest transients, none elsewhere | Mastering guidance for acoustic music: more than 1-2 dB of limiting on the loudest passage starts to compress the dynamics. |
| Direction of change | No section may move in the opposite direction from the source (0 "inversions"); at least 80% of each 5-second rise or fall kept | rbbKultur removed automatic levelling because it caused "inversion of intended volume variations" in classical music. |

The common claim that commercial orchestral releases measure 10-15 LU is wrong for the recordings themselves. Measured examples: the Dvorak 9/i Columbia reference used by this loop is 21.8 LU at -14.8 LUFS; Boulez's DG Mahler 1 is 23.5 LU at -16.9 LUFS. 15 LU is a broadcast and listening-comfort guideline, which is what this brief needs.

### Recommended delivery chain

Replace `acompressor -> loudnorm (dynamic)` with three steps:

1. **Offline gain ride (upward compression of macro dynamics only).** Compute short-term loudness (EBU 3 s window, 10 Hz) of the master, shift it 1.5 s earlier so it is centred, and smooth it with a zero-phase Gaussian (sigma 3 s). Let `loud` = the 95th percentile of short-term loudness. Below a knee at `loud - 6 dB`, add gain `(knee - L) * (1 - 1/2)` (ratio 2:1), capped at +10 dB. Above the knee, gain is 0 dB, so the climax is not touched. Smooth the gain curve again (Gaussian, sigma 3 s, zero-phase) so it starts rising before a quiet passage arrives and has no audible steps. Multiply the audio by the gain curve.
2. **One constant gain** to -19 LUFS integrated (measure, then apply `volume=<dB>`). Do not use loudnorm in dynamic mode. If you use loudnorm at all, use two-pass with `linear=true` and an LRA target equal to or above the measured LRA, so it stays linear.
3. **True-peak limiter** at -1.5 dBTP: `aresample=192000,alimiter=limit=0.841:attack=5:release=80:level=0:asc=1,aresample=48000` (0.841 = -1.5 dB; the 4x oversampling makes the sample-peak limiter approximate a true-peak limiter). Check that the limiter takes no more than about 3 dB; if it takes more, lower the loudest transients in the mix (timpani and brass hits) rather than pushing the limiter.

Measured on `render/mvt2-v77-mockup.wav` (source: -24.2 LUFS, LRA 19.9 LU; prototype scripts in the session scratchpad, `dyn/proto.py` and `dyn/run.py`):

| Chain | I (LUFS) | LRA (LU) | p10 short-term | max short-term | p10-to-max span | Climax rise over preceding 20 s (source 15.0 dB) | Share of 5 s moves kept | Inversions |
|---|---|---|---|---|---|---|---|---|
| Current: acompressor -36 dB 2.5:1 + loudnorm dynamic | -16.6 | 7.8 | -21.1 | -12.2 | 8.9 dB | 5.3 dB | 49% | 11 |
| Linear gain + limiter only | -18.2 | 19.9 | -31.8 | -9.2 | 22.6 dB | 14.3 dB | 100% | 0 |
| Ride, knee loud-10, 2:1, cap +9 | -18.2 | 16.1 | -27.9 | -9.2 | 18.7 dB | 13.2 dB | 88% | 0 |
| **Ride, knee loud-6, 2:1, cap +10 (recommended)** | -18.2 | 14.1 | -26.5 | -9.5 | 17.0 dB | 11.6 dB | 84% | 0 |

The current chain keeps only a third of the climax's rise and reverses the direction of 11 five-second dynamic changes. The gain ride lifts the soft passages by up to 10 dB and lands at the BBC classical guideline of about 15 LU, while the climax still rises 11-12 dB above what comes before it.

Example gain-ride core (numpy; `S` is the 10 Hz short-term loudness from `ffmpeg -af ebur128=metadata=1,ametadata=print:key=lavfi.r128.S:file=-`):

```python
S = np.nan_to_num(np.maximum(S, -70), nan=-70.0)
S = np.concatenate([S[15:], np.full(15, S[-1])])      # centre the 3 s window
def smooth(v, sec, rate=10):                           # zero-phase Gaussian
    n = int(sec*rate); k = np.exp(-0.5*(np.arange(-3*n, 3*n+1)/n)**2); k /= k.sum()
    return np.convolve(np.pad(v, (3*n, 3*n), mode='edge'), k, 'valid')
loud = np.percentile(S[S > -59], 95)
knee = loud - 6.0
gdb = np.clip((knee - smooth(S, 3.0)) * (1 - 1/2.0), 0, 10.0)
gdb = smooth(gdb, 3.0)
gain = 10**(np.interp(np.arange(len(x))/sr, np.arange(len(gdb))/10, gdb)/20)
y = x * gain[:, None]
```

The same curve can instead be written into REAPER's master volume envelope so it is visible and editable, which is what a mastering engineer riding the fader by hand produces. ReaComp and ReaXcomp are not suited to this: they are downward compressors with no look-ahead on a time scale of seconds, so they would behave like the current acompressor stage.

### What to do in the mix (before the master ride)

The professional order of preference in the sources is: (1) the performance and the mix carry the dynamic arc, (2) fader riding of whole sections, (3) gentle compression, (4) a limiter only for peaks. For this mockup:

- **Raise the soft dynamics in the track volume envelopes, not with CC11 alone.** CC11 in Hollywood Orchestra crossfades dynamic layers, so it sets timbre; the level of a pp passage should be set by the existing `soft_trim_db` mechanism (mix.json). Mike Senior's guidance for classical is to ride the quietest sections up by about 6 dB at most; the loop already measured that +2 dB on ppp/pp/p cut LRA from 25.4 to 23.9 LU. A further +2 to +4 dB on ppp/pp (and +1 to +2 dB on p), tapered so that mf and louder are not raised, should bring the unprocessed master to about 17-19 LU. The master ride then does the remaining 3-4 LU.
- **Keep pp sounding soft through timbre.** Use the soft CC11 layers, less vibrato (CC1), fewer doublings and thinner textures; the level lift then does not make pp sound like mf. This matches the VI-Control and VSL advice that softness in sample libraries comes from layer and velocity choice, not from volume alone.
- **Lift exposed soft solos separately.** Soft solo lines (a flute or clarinet over pp strings) are the parts that disappear on headphones; give them their own +2 to +3 dB rather than lifting the whole section.
- **Control the loudest transients in the mix.** If the limiter does more than about 3 dB at the climax, lower timpani strokes and brass accents by 1-2 dB with automation rather than limiting harder.
- **Do not compress individual orchestral tracks to reduce macro dynamics.** Forum consensus and Sound On Sound both say this makes acoustic instruments sound false and multiband compression changes the tonal balance between sections.

### What to avoid

- **loudnorm in dynamic mode on music.** Its code clamps every 3 s short-term loudness value to within +/- LRA/2 of the running integrated loudness, using a 3 s Gaussian-smoothed gain. That is a high-ratio automatic gain control with no knowledge of the score: it pulls climaxes down and pushes every quiet passage up by about the same amount, and it can reverse crescendos and diminuendos. The measurements above show this.
- **A downward compressor with a threshold below the soft passages** (acompressor at -36 dB: the source's 10th-percentile short-term loudness is -38 LUFS). Almost the whole piece is above threshold, so it acts as a full-range 2.5:1 compressor; with an 80 ms attack it also flattens accents and note attacks.
- **Multiband compression on the master** (tonal balance shifts with level; Sound On Sound).
- **Heavy limiting to reach a loudness number** (more than 1-2 dB on the loudest passage compresses the dynamics; Violet Recording).
- **dynaudnorm as the main tool.** It normalises each frame towards a peak target, so it pushes every section towards the same level within its gain cap; it is not loudness-weighted and has no knee that leaves loud passages alone.
- **Matching an LRA number at the cost of the shape.** EBU Tech 3343: LRA "should not be a brick wall parameter"; experienced listeners have to judge the result. Check the climax rise and the inversion count, not only LRA.

### Checks for the critics

For each delivered mp3, report: integrated LUFS, LRA, true peak, the 10th-percentile and maximum short-term loudness and their difference, the rise of the climax over the 20 s before it (compare with the unprocessed master), the share of 5-second rises and falls kept (output change divided by source change, median), the count of inversions, and the limiter's maximum gain reduction.

## 2. Evidence

### Broadcast standards

- **EBU Tech 3343 (2023), Guidelines for production in accordance with R 128.** https://tech.ebu.ch/publications/tech3343
  - §3.3: R 128 sets no maximum LRA. "It is impossible and not useful to define a strict limit for LRA for all broadcasters and all programmes. LRA should not be a brick wall parameter." Guiding upper values depend on genre, platform, replay environment and "listening comfort zone".
  - §3.3: a generic, open mix is made in production; lower LRA for specific platforms is produced downstream.
  - §6.1: programmes with LRA above about 20 LU may use an anchor signal for normalisation.
  - §9.3.2: classical music tends to be listened to 2-3 LU louder than other genres; a slow movement may have a deliberately lower loudness and should keep its relationship to the other movements (album normalisation).
  - Manual processing for wide-range content: "compression, limiting and gain riding of the whole mix or individual channels". Offline, iterative algorithms "can leave deliberate loudness jumps intact" and are preferred over real-time processors "which typically react without knowledge of the coming audio signal".
- **EBU Tech 3401, Guidelines for Radio production and distribution in accordance with R 128.** https://tech.ebu.ch/docs/tech/tech3401.pdf
  - Table 1, BBC Radio loudness by genre. Classical music: studio output -27 LUFS, max true peak -6 dBTP, **max LRA 15 LU**; DAB -23 LUFS / -2 dBTP / 15 LU; non-linear online (podcasts, web clips) **-18 LUFS / -2 dBTP / 15 LU**. Popular music max LRA is 3-7 LU, speech 6 LU.
  - Table 2, loudness profiles: "Music" LRA 8 LU in a news/magazine profile, 15 LU in the "News & Classics" profile.
  - §7.3 rbbKultur: old aggressive processing caused "deformations of the dynamics … which partially led to the inversion of intended volume variations, especially in classical music". After listening tests rbb removed automatic levelling completely, because "current automatic levelling cannot deal with intended large loudness variations in classical music … the machine has no information about the intention and the temporal behaviour of these variations". They use moderate compression and limiting and deliver about -20.2 LUFS (day) and -20.9 LUFS (evening), "similar to other classical music Radio stations in Germany". They were prepared to add offline LRA processing of very wide pieces at the source if soft parts proved too quiet.
  - Quotes R 128 s2: streaming may use -20 to -16 LUFS; German public broadcasters recommended -20 LUFS for culture channels.
- **EBU Tech 3344, Distribution and reproduction.** https://tech.ebu.ch/docs/tech/tech3344.pdf §6.9: mobile devices should have enough positive gain for -23 LUFS content, followed by a limiter. Phones often do not, which is why streamed classical sits higher than -23.
- **EBU Tech 3342, Loudness Range.** https://tech.ebu.ch/docs/tech/tech3342.pdf LRA is the spread between the 10th and 95th percentiles of gated 3 s short-term loudness.
- **AES TD1008 (via Production Advice and Radio World summaries).** https://productionadvice.co.uk/td1008/ , https://www.radioworld.com/?p=115138 Distribution loudness for music -16 LUFS (range -20 to -16). I did not obtain the document itself.

### Streaming platforms

- **Spotify.** https://support.spotify.com/artists/article/loudness-normalization/ Normal -14 LUFS, Quiet -19, Loud -11 (Loud uses a limiter at -1 dB, 5 ms attack, 100 ms release). Albums are normalised as a whole, so movement-to-movement relationships are kept; shuffled or playlist tracks are normalised individually. Quiet masters are raised only as far as their peaks allow with 1 dB headroom (example: -20 LUFS with -5 dBTP is raised only to -16). Recommends -1 dBTP or lower.
- **Apple Music Sound Check: -16 LUFS, LUFS-based since 2022.** https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html , https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why . Kirk McElhearn (Macworld) recommends turning Sound Check off for classical; his example has a quiet string-quartet section played at +15 dB. https://www.macworld.com/article/1139415/adjust_volume.html
- **Tidal: album normalisation, loudest track to -14 LUFS, attenuation only.** Based on Eelco Grimm's analysis of 4.2 million albums, which suggested -14 LUFS for mobile and -18 LUFS or lower for stationary playback. https://audioxpress.com/news/tidal-implements-album-loudness-normalization-and-activates-it-by-default-for-mobile-players

### Mastering engineers

- **Bob Katz, K-System.** https://www.digido.com/portfolio-item/level-practices-part-2/ K-20 (average level 20 dB below full scale, 20 dB of headroom) is "intended for wide dynamic range material", including classical symphonic music. Classical engineers should "mix by the calibrated monitor" (83 dB SPL at 0 on the meter). Peaking every recording to full scale makes a quartet sound unnaturally louder than a symphony.
- **Bob Katz interviews.** https://weiss.ch/blog/highend-hifi/bob-katz-interview-part-2/ , https://aes2.org/?p=59290 He judges by ear and uses LRA as a warning of extremes; for high-LRA material the perceived loudness follows the loudest passages more than the integrated value.
- **Mike Senior, Sound On Sound, "How should I compress a classical recording?"** https://www.soundonsound.com/sound-advice/q-how-should-compress-classical-recording Reduce dynamic range with fader automation, "riding up the quieter sections", by no more than about 6 dB on the quietest sections; duck brief peaks with automation rather than limiting. If compressing the master: ratio about 1.1:1, no more than 4-5 dB of gain reduction, fairly fast attack; listen for artefacts on isolated accented chords. Avoid multiband compression. Parallel compression with the compressed path below about 1.3:1 is more transparent; some engineers raise the compressed path only in quiet passages.
- **Production Expert on manual riding.** https://www.production-expert.com/production-expert-1/how-to-avoid-these-common-mistakes-with-compressors , https://www.production-expert.com/production-expert-1/we-check-out-automatic-level-rides-with-waverider-tg Classical engineers still prefer riding the fader to automatic gain control; rides are slower than a compressor, can go up as well as down, and follow the music rather than amplitude.
- **Violet Recording, How to master classical music.** https://violetrecording.com/how-to-master-classical-music/ Full orchestral works -16 to -20 LUFS; true peak -1 dBTP; if the limiter takes more than 1-2 dB on the loudest passage it is compressing the dynamics; optional glue compression at about 1.5:1, 30-50 ms attack, catching only the loudest 1 dB; many acoustic masters need none.
- **PureMix (Fab Dupont), mixing orchestral dynamics for streaming (2026).** https://www.puremix.com/blog/how-to-mix-orchestral-dynamics-for-streaming The problem is the ratio between quiet and loud passages, not peak level; "ride the arc, do not just compress it"; keep the contrast immediately before a climax; normalisation does not fix it because it moves the whole track.

### Orchestral mockup practice

- **VI-Control, "Techniques for managing macro dynamics in orchestral music"** https://vi-control.net/community/threads/techniques-for-managing-macro-dynamics-in-orchestral-music.149996/ and **"How to tame a huge dynamic range"** https://vi-control.net/community/threads/how-to-tame-a-huge-dynamic-range.119435/ (pages blocked to direct fetch; content from search excerpts). Suggested methods: choose an acceptable range, raise ppp to fit it and taper the fader through pp and p so that passages already loud enough are not raised; automate compressors to engage only at problem spots; heavy compression on individual orchestral tracks makes them sound false; upward and parallel compression were proposed for soft passages.
- **VI-Control, CC11 and dynamics threads; VSL forum.** https://vi-control.net/community/threads/questions-about-prepping-ahead-for-dynamics-and-volume-for-orchestral-mock-ups.159951/ , https://forum.vsl.co.at/post/305132 Use CC1/CC11 for dynamic layer and timbre; set level balance with trim or DAW volume; soft passages need a timbre change, not only a level change.
- **VI-Control, maintaining classical dynamics on streaming** https://vi-control.net/community/threads/how-to-maintain-dynamics-in-classical-style-music-when-mastering-for-streaming-services-that-turn-up-quiet-pieces.117516/ The conflict between per-track normalisation and quiet pieces; limiting soft material to make room for normalisation gain changes its tone.

### Measured loudness of commercial classical releases

- Dvorak 9/i, Columbia (this loop's reference, measured here with ffmpeg ebur128): -14.8 LUFS, LRA 21.8 LU, 10th-percentile short-term -35.7 LUFS, max short-term -9.6 LUFS.
- Mahler 1, Boulez/DG: -16.9 LUFS, LRA 23.5 LU; Bach violin sonatas, Harmonia Mundi: -19.1 LUFS, LRA 8.9 LU. https://discourse.ardour.org/t/complete-classical-music-workflow/101827?page=11 (forum measurements).
- I found no systematic study of LRA across classical catalogues. Skovenborg and Lund's AES papers on wide-range material (AES Paper 7948, 2009) are behind the AES paywall.

### ffmpeg loudnorm internals

- Original patch and code: https://ffmpeg.org/pipermail/ffmpeg-devel/2016-April/192668.html Dynamic mode uses a 3 s buffer, 100 ms gain updates and a 21-tap Gaussian (sigma 3.5 updates) over the gain deltas; each update clamps `shortterm - global` to +/- `target_lra/2`. The look-ahead true-peak limiter has 10 ms attack and 100 ms release. Linear mode is only used with two-pass measured values and when the LRA and true-peak targets allow it: https://ffmpeg.org/pipermail/ffmpeg-user/2022-March/054421.html
