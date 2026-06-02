from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("outputs/sample_frames/CAM 1.jpg")

person_count = 0

for result in results:
    for box in result.boxes:
        cls = int(box.cls[0])

        if model.names[cls] == "person":
            person_count += 1

print(f"People detected: {person_count}")