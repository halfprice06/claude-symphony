# c49 actor: waiting for disk (2026-11-08 12:08)

The lock came at 12:06 (after the finale's c05 actor). Free space on /System/Volumes/Data was 27 GB, under the 30 GB
the coordinator set for a render. I deleted my own scratch (`/private/tmp/claude-501/mockup-loop/mvt1-c49-actor/sim`,
about 1 GB of simulated stems): 27.7-27.8 GB free over the next minute. No other folder of mine holds audio. I released
the lock without starting REAPER, so nothing was built or rendered.

## State of the cycle (resume from here: `before/` exists, so do not snapshot again)

- `before/`: the c48 tools and data, taken at 10:17.
- Data edits are made and `build/parts.json` is regenerated from them (not yet in REAPER):
  - `build/score_config.py`: the c49 block at the end (A #1 pedal aliases "Cb pedal A" window 613.5-680 and
    "Cb pedal B" 618-680, both tests, the main basses unchanged; A #2 celli 156 back to Sus MAX; A #3 Violas 358 -2 dB;
    B #1 Clarinet 1 700 cuts; B #3 Violins II 372 / 380 cuts (second row ends before the 381 note's moved onset);
    B #5 cor anglais 586.5 +3 dB step; C #2 test aliases "Vla send35 test" / "Vla rt3 test"; the coordinator's
    Main-width variant on eight test aliases "... mainw test"). B #2 is rejected there, with the measurement.
  - JSON edits: `cycles/c49/actor_scripts/apply49.py` (re-applies them from `before/`): mix.json (test alias entries,
    Trumpets a2 coda 3.2 kHz bell 664.4-679.7), retongue_leads.json (celli 156 0.09), roles.json (bar 81: basses
    [320.75, 324, -2, 0.25], timpani [322, 324, -2, 0.25], Violas -1.5 -> -3).
  - `tools/build_reaper.py`: `reverb.width` / track `reverb_width` (the ConvolutionReverb Width, p.220). The shared hall
    is not changed (coordinator: no hall change this cycle); the hall-width test is in `cycles/c49/halltest/`
    (`make_halltest.py` already wrote parts.json / mix.json for widths 1.0 / 1.5 / 2.0; `render_halltest.py`,
    `measure_width49.py`).
- Decided without a render: basses pp cap 600 ms everywhere (`actor_scripts/cbcap49.py`); B #2 rejected
  (`vc156_49.py`); B #4 timpani row moved to 322 (`bar81_49.py`); C #3 melody check (`tpta2_49.py`); B #1
  (`cl700_49.py`).

## Remaining steps once at least 30 GB is free

1. Lock (longest-waiter rule), check the disk again.
2. Main: `reaper_ctl.py start`, `open`, `build_reaper.py build/parts.json jobs --midi-only`, `restart`, check memory
   and 33 tracks, `render_cycle.py 49`, `quit`.
3. Pass 2: `start`, `--pass2 open`; hall test (`build_reaper.py cycles/c49/halltest/parts.json cycles/c49/halltest/jobs
   --pass2 "Hall test w100" "Hall test w150" "Hall test w200"`, `render_halltest.py w`, `measure_width49.py`,
   `render_halltest.py --delete`); then `build_reaper.py build/parts.json jobs --pass2 --midi-only` (19 pass-2 tracks,
   12 of them tests), `--pass2 restart`, `render_cycle.py 49 --pass2`.
4. Decide with `actor_scripts/pedal49.py`, `vla49.py`, `mainw49.py`, `width49.py`; splice with `swap49.py`; state check
   against c48; delete the test tracks from the data and the pass-2 project; `render_cycle.py 49 --measure-only`;
   records; `--pass2 quit`; `unlock`.
