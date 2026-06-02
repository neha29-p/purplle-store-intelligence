import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.camera_analyzer import CameraAnalyzer

analyzer = CameraAnalyzer()

video_dir = Path("data/videos/CCTV Footage")

for video_path in sorted(video_dir.glob("*.mp4")):
    summary = analyzer.summarize(str(video_path))

    print(f"\n{video_path.name}")
    print(f"Samples: {summary['samples']}")
    print(f"Average Occupancy: {summary['average_occupancy']}")
    print(f"Max Occupancy: {summary['max_occupancy']}")