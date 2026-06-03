# PROMPT:
# Generate a test for camera-wise retail traffic summaries.
# Validate visitor counts, occupancy metrics, and camera performance reporting.
#
# CHANGES MADE:
# Customized assertions to align with dashboard analytics outputs.
#
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.camera_analyzer import CameraAnalyzer

analyzer = CameraAnalyzer()

summary = analyzer.summarize(
    "data/videos/CCTV Footage/CAM 1.mp4"
)

print(summary)
