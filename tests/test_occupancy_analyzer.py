import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.occupancy_analyzer import OccupancyAnalyzer

analyzer = OccupancyAnalyzer()

samples = analyzer.analyze_video(
    "data/videos/CCTV Footage/CAM 1.mp4"
)

print(f"Samples collected: {len(samples)}")
print(f"Maximum occupancy: {max(samples)}")
print(f"Average occupancy: {sum(samples)/len(samples):.2f}")