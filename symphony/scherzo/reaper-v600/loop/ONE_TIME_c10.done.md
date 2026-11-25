# One-time task for the c10 actor: finale techniques and Movement I c51 lessons not adopted in c09

Sources (read only, never write there): `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` (code in
`symphony/mvt3/reaper-v600/tools/`; copy what you use into our `tools/`), `mockup-kit/README.md` last section
(Movement I c51). The orchestrator passed both to the c09 actor after its render was done; c09 checked items 2 and 9
offline and left the rest here. Adopt each item alongside the critics' fixes unless measured numbers say no (record
them in LEARNINGS), and record the result in cycles/c10/CHANGES.md. Rename this file to ONE_TIME_c10.done.md when done.

Already true here (checked in c09, nothing to do):
- Finale item 2 (a crescendo on the sfp onset overwriting the spike): our `FP_SPIKE_FROM_ONSET` holds. In parts.json the
  bar-301 sfp notes start on the sf value at the moved note-on (Flute 1 CC11 114 at 899.75, Oboe 1 119, Violins I 114,
  Violas 120, Clarinet 1 CC1 108 from 899.5) and fall at 900.5. Their p-row roles (each part's own drop 10 dB or more)
  are not checked: measure each part's drop on the c09 stems first.
- Finale item 9 (harp velocity 124+ triggers the Nail Pick layer): our harp's highest velocity is 56 (VEL_CAP_SPANS).
- Movement I c51 item 1 (brass bells 475 / 821 Hz, 3.2 kHz): in our mix since c08.

To try (simulate or measure on the c09 stems first; keep Dan's limits: G.P. drop at least 15 dB at +0.3 s, RT60 1.5 s
or less, soft ends 0.30 s or less):
1. Low-end width (finale item 4): side-only 60 Hz -3 dB low shelf plus a 180 Hz -5.5 dB bell (1.5 oct) on the low
   tracks, the returns and the harp, against our side-only 200 Hz -6 dB shelf (c07 width07.py). Compare correlation
   below 250 Hz, 250 Hz-5 kHz and side/mid on the c09 master (c07: 0.68 / 0.57 / -5.6 dB).
2. Brass track width (finale item 5): mix.json `track_width` (REAPER D_WIDTH, `--mix-only`): trumpets 0.5, trombones
   0.6. Needs the key ported into build_reaper.py (it writes D_WIDTH 1 now).
3. Low-mid cuts (finale item 6): horn family 315 Hz -5 dB bell (1 oct) with +1.0 dB gain, violas 315 Hz -3 dB with
   +0.8 dB. Measure our 250-500 Hz excess over the references first (c08 critic C found the tuttis not heavy at 250-500 Hz).
4. FINAL_RING (finale item 7): the final chord rings 0.45 s past the written end under a falling volume shape. Our final
   chord already measures RT60 1.42 s and drop 20.2 dB at +0.3 s (c09): check it against the 0.30 s soft-end limit
   before adopting.
5. CC16 round-robin reset before ostinato spans (finale item 8) plus a per-span metric level table: our RR_RESET_AT
   already resets the pizz. groups 264-291; candidates are the theme heads' repeated eighths and the trumpets' repeated
   quarters (105-120, 305-320).
6. sub. p (finale item 3): PHRASE_SHAPE type "drop" (no positive offset on a phrase that starts on a subito or a drop
   of 6 CC or more) and HELD_DECRESC_CARRY, at our sub. p's (bar 121 qn 360, bar 277 qn 828). Check whether our
   PHRASE_SHAPE puts a positive offset on the phrases starting there.
7. Template EQ tone (finale item 11): strings 1 kHz -2.5, winds 1 kHz -1.55, brass 821 Hz -4 / 3.2 kHz -4 with
   make-up gains. Compare band shares with the references first (c09 master: 500 Hz-2 kHz -3.27 dB, Dvorak -3.46).
8. Basses' template high-pass 53 -> 35 Hz (finale item 12).
9. Hall (finale item 1): ours already uses the same irSetup, low sends off and drier returns (returns -11.6 dB re dry
   in c09, RT60 1.34 s at the G.P.); no change unless a critic measures a reason.
10. Movement I c51 item 2: phrase shapes on winds need the offsets x1.4 (PHRASE_SHAPE has no per-family scale; add one,
    off by default, and measure the winds' rise on the stems).
11. Movement I c51 items 3-5 as checks: fit soft brass levels on the whole render (not a range test); string repeat
    gaps separate on the stems but not always in the master (our S1 master pair dips 4.0-6.0 dB in c09); after any
    held-note dynamic change check the inner held notes under a tune (c09: Horns 3-4 under Clarinet 1 at 456-504
    unchanged, -53.5 / -50.2 against -38.9).
