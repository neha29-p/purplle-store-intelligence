import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2
from pipeline.person_counter import PersonCounter

counter = PersonCounter()

image = cv2.imread(
    "outputs/sample_frames/CAM 1.jpg"
)

count = counter.count_people(image)

print(f"People detected: {count}")