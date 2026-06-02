from pathlib import Path
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "data/videos/CCTV Footage/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

frame_number = 0
sample_every = 300  # roughly every 10 seconds for 30 FPS video

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_number % sample_every == 0:
        results = model(frame, verbose=False)

        people = 0

        for box in results[0].boxes:
            cls = int(box.cls[0])

            if model.names[cls] == "person":
                people += 1

        print(
            f"Frame {frame_number}: "
            f"{people} people"
        )

    frame_number += 1

cap.release()

print("Done")