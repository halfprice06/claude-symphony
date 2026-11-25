> **c07 actor (2026-10-11): deferred, not applied.** The Opus manual says the HDD preload (0) keeps more of each sample in RAM. The c06 late entries came from memory compression (REAPER 72 GB, 69 GB compressed, on a 96 GB Mac), so a larger preload would add to the cause. The c07 render from a freshly restarted REAPER at PreloadSize 1 passed every attack check. This needs Dan's decision again with that evidence; until he answers, later actors should skip this file. See cycles/c07/CHANGES.md.

# One-time task for the next actor (written 2026-10-11 by the thread)

Dan approved raising Opus's streaming preload ("sure", 2026-10-11 13:21 UTC) so soft entries stop starting late. Do this at the start of your cycle, before any other REAPER work:

1. Save the project (job: `reaper.Main_SaveProject(0, false)`), then quit REAPER with a job calling `reaper.Main_OnCommand(40004, 0)` (File: Quit). Wait until `pgrep -x REAPER` finds nothing.
2. With REAPER closed, set `"PreloadSize": 0` (0 = Harddrive, 1 = SSD/SATA, the old value; 2 = SSD/PCIe; order from the Opus binary's preference list) in `/Library/Application Support/East West/Opus/Preferences.json`. Change only that value. A backup of the original is in `loop/Opus-Preferences.backup-2026-10-11.json`.
3. `open -a REAPER`; it reopens the last project. Wait until `rpr.py status` says alive and all 27 tracks are loaded (about 15 minutes), then check the file still says 0.
4. Record in your CHANGES.md and in HISTORY.md that renders from this cycle on use PreloadSize 0, and measure late entries against the previous cycle. Then delete this file.
