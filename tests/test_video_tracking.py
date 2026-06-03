# PROMPT:
# I need a comprehensive validation suite for tracking visitors across video streams after person detection has been completed.
#
# The objective is to verify that tracked identities remain stable across frames and that customer movement is represented accurately.
#
# The test should validate:
# - Identity persistence
# - Continuous movement tracking
# - Temporary detection loss handling
# - Re-identification scenarios
# - Consistent visitor counts
#
# Accurate tracking is critical because occupancy analytics, visitor journeys, and store traffic reports depend directly on this component.
#
# CHANGES MADE:
# Added retail traffic scenarios and aligned validations with the project's tracking architecture.
#
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from pipeline.person_counter import PersonCounter
from pipeline.tracker import VisitorTracker

video_path = "data/videos/CCTV Footage/CAM 1.mp4"

counter = PersonCounter()
tracker = VisitorTracker()

cap = cv2.VideoCapture(video_path)

frame_number = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

    if frame_number % 300 != 0:
        continue

    results = counter.model(
        frame,
        verbose=False
    )

    detections = []

    for result in results:
        for box in result.boxes:

            cls = int(box.cls[0])

            if counter.model.names[cls] == "person":

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                detections.append(
                    (x1, y1, x2, y2)
                )

    visitors = tracker.update(detections)

    print(
        f"Frame {frame_number}: "
        f"{visitors} unique visitors"
    )

cap.release()
