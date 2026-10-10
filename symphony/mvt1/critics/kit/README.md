# Movement I loop kit (copied from the mvt I thread's scratchpad, 2026-10-10)

- `critic_prompt.txt`: template for each critic's task file (genprompt.sh fills cycle number, lens from ../LENSES.md, reading from ../READING.md).
- `genprompt.sh N "focus"`: writes the prompt for cycle N (the copy here still points at the scratchpad paths; edit the paths before reuse).
- `promote.sh NEW PREV SRC`: copies a critic's scratch work into mvt1/vNEW, sets the "draft vNEW" header, builds, and prints warnings, parallels and page count.
- Other *.py: small LilyPond editing helpers used in the first series.

These are reference copies; the live loop runs from the scratchpad.
