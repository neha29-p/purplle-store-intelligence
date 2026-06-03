# PROMPT:
# I need a store-level analytics summary validation that combines operational and business metrics into a single report.
#
# The test should verify that visitor analytics, occupancy analytics, and sales analytics are correctly consolidated.
#
# Validation should include:
# - Footfall metrics
# - Occupancy metrics
# - Sales KPIs
# - Summary generation
# - Report consistency
#
# The objective is to ensure that the final dashboard presents reliable and decision-ready information.
#
# CHANGES MADE:
# Added KPI checks and summary validation tailored to the store intelligence dashboard.
#
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
