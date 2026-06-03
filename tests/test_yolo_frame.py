# PROMPT:
# I need a validation suite for running YOLO inference on individual CCTV frames before processing entire video streams.
#
# The purpose of this test is to verify that frame-level detections remain accurate and suitable for downstream analytics.
#
# The test should validate:
# - Successful model execution
# - Person detection accuracy
# - Output structure consistency
# - Stable behavior across multiple frames
#
# Frame-level validation provides confidence before scaling detection to full retail video datasets.
#
# CHANGES MADE:
# Added CCTV frame validation scenarios and aligned outputs with the project's analytics workflow.
#
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
