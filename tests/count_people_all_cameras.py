from pathlib import Path
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

image_dir = Path("outputs/sample_frames")

for image_path in image_dir.glob("*.jpg"):
    results = model(str(image_path), verbose=False)

    person_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            if model.names[cls] == "person":
                person_count += 1

    print(f"{image_path.name}: {person_count} people")