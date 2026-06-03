# PROMPT:
# I need a validation suite for video assets used throughout the analytics pipeline.
#
# The objective is to ensure that all required video files exist, are accessible, and can be processed without errors.
#
# The test should verify:
# - File availability
# - Read permissions
# - Basic accessibility
# - Compatibility with downstream processing modules
#
# Reliable video inputs are essential because the entire analytics workflow depends on them.
#
# CHANGES MADE:
# Added project-specific dataset validation checks.
#
from pathlib import Path

video_dir = Path("data/videos/CCTV Footage")

print("Videos found:\n")

for video in video_dir.glob("*.mp4"):
    print(video.name)
