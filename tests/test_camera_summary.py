import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.camera_analyzer import CameraAnalyzer

analyzer = CameraAnalyzer()

summary = analyzer.summarize(
    "data/videos/CCTV Footage/CAM 1.mp4"
)

print(summary)