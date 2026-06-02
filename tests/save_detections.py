from pathlib import Path
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

input_dir = Path("outputs/sample_frames")
output_dir = Path("outputs/detections")

output_dir.mkdir(parents=True, exist_ok=True)

for image_path in input_dir.glob("*.jpg"):
    results = model(str(image_path), verbose=False)

    annotated = results[0].plot()

    output_path = output_dir / image_path.name
    cv2.imwrite(str(output_path), annotated)

    print(f"Saved: {output_path}")

print("\nAll detection images saved.")