#!/usr/bin/env python3
"""Join title cards and movement videos into one file without encoding the pictures again.

  join_videos.py --out OUT.mp4 [--chapters "NAME|NAME|..."] SEGMENT.mp4 ...

The segments must have been encoded alike (same size, frame rate and x264 settings: the movement videos of
glow_video.py and the cards of title_cards.py are). The pictures are copied as they are (ffmpeg's concat reader).

The sound is built once for the whole length, because the segments do not line up for a plain copy: a card has no
sound, and a movement's sound stops a few seconds before its last frame. Each segment's sound is decoded, filled with
silence or cut to exactly the length of its pictures (800 samples a frame at 48 kHz and 60 fps), the pieces are put in
a row and encoded once more (AAC, 320 kbit/s). So sound and picture cannot drift apart from one segment to the next.

A segment written as MOVEMENT.mp4@K is taken from its frame K on (K must be a key frame, so that the copy can start
there), and its sound starts K frames earlier, behind the end of the segment before it, which must be a silent card
(title_cards.py makes such a card with "handover_cut": K or "corner": K; its last frames lead into frame K). If the
card has fewer than K frames it starts inside the movement ("start" in the card's spec): the sound then starts with
the card, and the movement's sound before that point is left out.

Prints each segment's start time; with --chapters (one name per segment, separated by "|"; "-" for a segment that
starts no chapter) also a chapter list for the video's description.
"""
import argparse, json, os, subprocess, sys, tempfile

def probe(path):
    skip = 0
    if "@" in os.path.basename(path) and path.rsplit("@", 1)[1].isdigit():
        path, k = path.rsplit("@", 1); skip = int(k)
    path = os.path.abspath(path)
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-show_streams", "-of", "json", path],
                                  capture_output=True, text=True, check=True).stdout)
    st = j["streams"]
    if not st or st[0]["codec_type"] != "video": sys.exit(f"{path}: the first stream is not the video")
    v = st[0]; num, den = (int(x) for x in v["r_frame_rate"].split("/"))
    a = next((s for s in st if s["codec_type"] == "audio"), None)
    if skip:    # the copy can only start at a key frame
        t = skip * den / num
        pk = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-read_intervals", f"{max(t - 0.5, 0):.3f}%{t + 0.5:.3f}",
                                        "-show_entries", "packet=pts_time,flags", "-of", "json", path], capture_output=True, text=True, check=True).stdout)["packets"]
        if not any(abs(float(q["pts_time"]) - t) < 0.4 / (num / den) and "K" in q["flags"] for q in pk):
            sys.exit(f"{path}: frame {skip} is not a key frame, so the copy cannot start there")
    return dict(path=path, total=int(v["nb_read_packets"]), skip=skip, frames=int(v["nb_read_packets"]) - skip, fps=(num, den), size=(v["width"], v["height"]),
                key=(v["codec_name"], v.get("profile"), v.get("level"), v["pix_fmt"], v["width"], v["height"], v["r_frame_rate"], v["time_base"]),
                audio=a is not None)

def clock(s):
    s = int(s); return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--chapters", help='one name per segment, separated by "|"; "-" for a segment that starts no chapter')
    ap.add_argument("--rate", type=int, default=48000)
    ap.add_argument("segments", nargs="+")
    A = ap.parse_args()
    segs = [probe(p) for p in A.segments]
    chapters = [c.strip() for c in A.chapters.split("|")] if A.chapters else None
    if chapters and len(chapters) != len(segs): sys.exit("--chapters needs one name per segment")
    for s in segs[1:]:
        if s["key"] != segs[0]["key"]: sys.exit(f"{s['path']} is encoded differently from {segs[0]['path']}:\n  {s['key']}\n  {segs[0]['key']}")
    num, den = segs[0]["fps"]
    if (A.rate * den) % num: sys.exit(f"{A.rate} Hz has no whole number of samples per frame at {num}/{den} fps")
    spf = A.rate * den // num                                       # samples per frame

    tmp = tempfile.mkdtemp(prefix="join-", dir=os.path.dirname(os.path.abspath(A.out)))
    lst, snd = os.path.join(tmp, "list.txt"), os.path.join(tmp, "sound.m4a")
    try:
        # 1. the sound of the whole length
        cmd, graph, k = ["ffmpeg", "-y", "-v", "error"], [], 0
        for i, s in enumerate(segs):
            if s["skip"] and (i == 0 or segs[i - 1]["audio"]):
                sys.exit(f"{s['path']}@{s['skip']}: the segment before it must be a silent card")
        pieces = []
        for i, s in enumerate(segs):
            if s["audio"]:
                # the sound of all its pictures, the frames before K included; where the card before it has fewer
                # than K frames, the sound starts with the card and its head is left out
                h = max(s["skip"] - segs[i - 1]["frames"], 0) * spf if s["skip"] else 0
                n = s["total"] * spf - h
                cmd += ["-i", s["path"]]
                graph.append(f"[{k}:a]aresample={A.rate},aformat=sample_fmts=fltp:channel_layouts=stereo,"
                             + (f"atrim=start_sample={h},asetpts=N/SR/TB," if h else "")
                             + f"apad=whole_len={n},atrim=end_sample={n},asetpts=N/SR/TB[a{i}]")
                k += 1; pieces.append(i)
            else:
                # the silence of a card is shorter by the frames that the next segment's sound starts early
                n = max(s["total"] - (segs[i + 1]["skip"] if i + 1 < len(segs) else 0), 0) * spf
                if n:
                    graph.append(f"anullsrc=r={A.rate}:cl=stereo,aformat=sample_fmts=fltp,atrim=end_sample={n},asetpts=N/SR/TB[a{i}]")
                    pieces.append(i)
        graph.append("".join(f"[a{i}]" for i in pieces) + f"concat=n={len(pieces)}:v=0:a=1[a]")
        cmd += ["-filter_complex", ";".join(graph), "-map", "[a]", "-c:a", "aac", "-b:a", "320k", snd]
        subprocess.run(cmd, check=True)
        # 2. the pictures, copied, with that sound
        # each file's length is stated as that of its pictures, so that the next one starts exactly one frame after
        # its last frame whatever the length of its sound
        open(lst, "w").write("".join(f"file '{s['path']}'\n" + (f"inpoint {s['skip'] * den / num + 5e-7:.6f}\n" if s["skip"] else "")
                                     + f"duration {s['frames'] * den / num:.6f}\n" for s in segs))
        total = sum(s["frames"] for s in segs) * den / num
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", snd, "-map", "0:v:0", "-map", "1:a:0",
                        "-c", "copy", "-movflags", "+faststart", "-t", f"{total:.6f}", A.out], check=True)
    finally:
        for f in (lst, snd):
            if os.path.exists(f): os.remove(f)
        os.rmdir(tmp)
    got = json.loads(subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries", "stream=nb_read_packets",
                                     "-of", "json", A.out], capture_output=True, text=True, check=True).stdout)["streams"][0]["nb_read_packets"]
    if int(got) != sum(s["frames"] for s in segs): sys.exit(f"{A.out} has {got} frames, expected {sum(s['frames'] for s in segs)}")

    t = 0.0
    print(f"{A.out}: {len(segs)} segments, {sum(s['frames'] for s in segs)} frames, {total:.3f} s ({clock(total)})")
    for i, s in enumerate(segs):
        print(f"  {t:9.3f} s  {clock(t):>8s}  {s['frames']:6d} frames  {'sound' if s['audio'] else 'silent'}  {os.path.basename(s['path'])}"
              + (f" from frame {s['skip']}; its sound starts at {t - min(s['skip'], segs[i - 1]['frames']) * den / num:.3f} s"
                 + (f", {s['skip'] - segs[i - 1]['frames']} frames into the movement" if segs[i - 1]["frames"] < s["skip"] else "") if s["skip"] else ""))
        t += s["frames"] * den / num
    if chapters:
        print("chapters:"); t = 0.0
        for name, s in zip(chapters, segs):
            if name != "-": print(f"{clock(t)} {name}")
            t += s["frames"] * den / num
