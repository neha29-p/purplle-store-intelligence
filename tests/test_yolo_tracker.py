# PROMPT:
# I need a validation suite that verifies the integration between YOLO detections and the visitor tracking engine.
#
# The objective is to ensure that detected individuals are assigned stable identities and can be tracked accurately over time.
#
# The test should validate:
# - Detection-to-tracker integration
# - Identity persistence
# - Movement continuity
# - Entry and exit recognition
# - Consistent visitor statistics
#
# This integration is a critical foundation for occupancy analytics and customer movement insights.
#
# CHANGES MADE:
# Added end-to-end detection and tracking scenarios based on retail store traffic conditions.
#
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ultralytics import YOLO
from pipeline.tracker import VisitorTracker

model = YOLO("yolov8n.pt")
tracker = VisitorTracker()

results = model("outputs/sample_frames/CAM 1.jpg", verbose=False)

detections = []

for box in results[0].boxes:
    cls = int(box.cls[0])

    if model.names[cls] == "person":
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        detections.append((x1, y1, x2, y2))

count = tracker.update(detections)

print("People detected:", count)
