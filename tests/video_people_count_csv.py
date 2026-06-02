from ultralytics import YOLO
import cv2
import csv

model = YOLO("yolov8n.pt")

video_path = "data/videos/CCTV Footage/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

frame_number = 0
sample_every = 300

rows = []

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

        rows.append([frame_number, people])

        print(f"Frame {frame_number}: {people} people")

    frame_number += 1

cap.release()

with open("outputs/cam1_occupancy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["frame", "people_count"])
    writer.writerows(rows)

print("\nSaved: outputs/cam1_occupancy.csv")