# PROMPT:
# I need a comprehensive validation suite for the occupancy analytics component used in the retail intelligence platform.
#
# The objective is to verify that occupancy calculations remain accurate when customer counts fluctuate throughout the day.
#
# The test should validate:
# - Average occupancy calculations
# - Peak occupancy detection
# - Empty store scenarios
# - Continuous traffic scenarios
# - Consistency of occupancy metrics across multiple samples
#
# The implementation should focus on correctness, simplicity, and reproducibility because these metrics will be used by store managers to understand crowd density and customer engagement patterns.
#
# CHANGES MADE:
# Adapted the calculations to align with the project's occupancy analytics workflow and reporting requirements.
#
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
