from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

image_path = "outputs/sample_frames/CAM 1.jpg"

results = model(image_path)

for result in results:
    print("\nDetections:")
    for box in result.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])

        print(
            f"Class: {model.names[cls]}, "
            f"Confidence: {conf:.2f}"
        )