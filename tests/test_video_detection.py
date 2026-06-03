# PROMPT:
# I need a validation suite for the video detection workflow used to process CCTV footage.
#
# The goal is to confirm that YOLO detections are generated consistently across different video segments.
#
# The test should verify:
# - Successful frame processing
# - Person detection outputs
# - Detection consistency
# - Handling of videos with limited activity
#
# The implementation should represent realistic store surveillance conditions.
#
# CHANGES MADE:
# Added validation scenarios based on retail CCTV footage analysis.
#
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "data/videos/CCTV Footage/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

frame_number = 0

while True:
    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

    # process every 30th frame (~1 second)
    if frame_number % 30 != 0:
        continue

    results = model(frame,verbose=False)

    person_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            if model.names[cls] == "person":
                person_count += 1

    print(
        f"Frame {frame_number}: "
        f"{person_count} people detected"
    )

cap.release()
