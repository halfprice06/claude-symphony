"""Give every General MIDI program its own channel (skipping drums on 9).

LilyPond wraps channels modulo 16 when a score has more than 15 instruments, so two
instruments can end up sharing a channel and the later program change wins. This
rewrites the file in place so each distinct program gets a distinct channel.
"""
import sys
import mido

path = sys.argv[1]
mid = mido.MidiFile(path)
prog_of_track = {}
for i, tr in enumerate(mid.tracks):
    for msg in tr:
        if msg.type == 'program_change' and msg.channel != 9:
            prog_of_track[i] = msg.program
            break
free = [c for c in range(16) if c != 9]
chan_of_prog = {}
for i in sorted(prog_of_track):
    p = prog_of_track[i]
    if p not in chan_of_prog:
        if not free:
            sys.exit(f"more than 15 distinct programs; cannot assign {p}")
        chan_of_prog[p] = free.pop(0)
for i, tr in enumerate(mid.tracks):
    if i not in prog_of_track:
        continue
    c = chan_of_prog[prog_of_track[i]]
    for k, msg in enumerate(tr):
        if hasattr(msg, 'channel') and msg.channel != 9:
            tr[k] = msg.copy(channel=c)
mid.save(path)
print("channels:", {p: c for p, c in chan_of_prog.items()})
