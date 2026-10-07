"""Prepare the September terminal footage for the existing BluPrint carousel.

Preserves aspect ratios; DAY then SIDE form one clip, Editable is 1.5x,
and Vertical starts 1.8 seconds into its source. Saturation is increased by 10%.
Outputs H.264 1080p/30, silent autoplay, fast-start MP4 and content-hashed posters.
Original footage is read-only. Run with --source pointing at VIDEO_SOURCE/SIMULATION.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    ("air-to-terminal", ["1. AIR_TO_TERMINAL.mp4"], 15, 1),
    ("terminal-flow-3d", ["2. TER_3D_VERTICAL.mp4"], 7, 1),
    ("terminal-digital-twin", ["3. TER_3D_DAY.mp4", "5. TER_3D_SIDE.mp4"], 8, 1),
    ("terminal-editable", ["4.5 Editable.mp4"], 4, 1.5),
]
TRIM_STARTS = {"terminal-flow-3d": 1.8}
SATURATION = 1.1


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size:stream=codec_type,codec_name,width,height,r_frame_rate,duration,nb_frames",
        "-of", "json", str(path)]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--only", choices=[job[0] for job in JOBS])
    args = parser.parse_args()
    output = ROOT / "web/airport-designer"
    work = ROOT / "output/playwright/bluprint-terminal-20260922"
    work.mkdir(parents=True, exist_ok=True)
    jobs = [job for job in JOBS if not args.only or job[0] == args.only]
    for _, names, _, _ in jobs:
        for name in names:
            if not (args.source / name).is_file():
                raise FileNotFoundError(args.source / name)

    def build(job):
        slug, names, poster_at, speed = job
        trim_start = TRIM_STARTS.get(slug, 0)
        poster_at = max(0, poster_at - trim_start / speed)
        sources = [args.source / name for name in names]
        destination = work / (slug + ".mp4")
        command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-filter_complex_threads", "2"]
        for source in sources:
            if trim_start:
                command += ["-ss", str(trim_start)]
            command += ["-i", str(source)]
        normalize = f"scale=1920:1080:force_original_aspect_ratio=decrease:force_divisible_by=2:flags=lanczos,eq=saturation={SATURATION},pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,setpts=(PTS-STARTPTS)/{speed},fps=30"
        filters = [f"[{i}:v:0]{normalize}[v{i}]" for i in range(len(sources))]
        if len(sources) > 1:
            filters.append("".join(f"[v{i}]" for i in range(len(sources))) + f"concat=n={len(sources)}:v=1:a=0[out]")
        command += ["-filter_complex", ";".join(filters), "-map", "[out]" if len(sources) > 1 else "[v0]",
                    "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-maxrate", "4M", "-bufsize", "8M", "-threads", "4",
                    "-pix_fmt", "yuv420p", "-g", "60", "-movflags", "+faststart", str(destination)]
        subprocess.run(command, check=True)
        digest = sha(destination)
        video = output / f"{slug}.{digest[:12]}.mp4"
        shutil.copyfile(destination, video)
        poster = work / (slug + ".webp")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(poster_at),
                        "-i", str(video), "-vf", "scale=1280:720", "-frames:v", "1", "-c:v", "libwebp",
                        "-quality", "86", str(poster)], check=True)
        published_poster = output / f"{slug}.{sha(poster)[:12]}.webp"
        shutil.copyfile(poster, published_poster)
        result = {"slug": slug, "sources": [{"path": str(p), "sha256": sha(p), **probe(p)} for p in sources],
                  "video": video.relative_to(ROOT).as_posix(), "poster": published_poster.relative_to(ROOT).as_posix(),
                  "sha256": digest, "output": probe(video), "posterAtSeconds": poster_at, "speed": speed,
                  "trimStartSeconds": trim_start, "saturation": SATURATION}
        print(json.dumps({"done": slug, "bytes": video.stat().st_size}), flush=True)
        return result

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(build, jobs))
    manifest = work / "media-manifest.json"
    if args.only and manifest.exists():
        previous = {clip["slug"]: clip for clip in json.loads(manifest.read_text(encoding="utf-8"))["clips"]}
        previous.update({clip["slug"]: clip for clip in results})
        results = [previous[job[0]] for job in JOBS if job[0] in previous]
    report = {"method": "Saturation 1.1x from original footage; Vertical trims its opening 1.8 seconds; DAY then SIDE, Editable at 1.5x; aspect-ratio preserved without cropping; H.264 CRF 24 / max 4Mbps 1080p/30, faststart, no audio. Additional carousel playback speeds are configured in solutions.html.", "clips": results}
    (work / "media-manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Prepared {len(jobs)} carousel clip(s) and posters.", flush=True)


if __name__ == "__main__":
    main()
