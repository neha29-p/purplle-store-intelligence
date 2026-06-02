from pathlib import Path

video_dir = Path("data/videos/CCTV Footage")

print("Videos found:\n")

for video in video_dir.glob("*.mp4"):
    print(video.name)