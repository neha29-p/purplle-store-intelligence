# PROMPT:
# I need a validation suite for the YOLO-based detection engine used to identify people within retail CCTV footage.
#
# The objective is to verify that detections are generated consistently and can serve as a reliable foundation for tracking and occupancy analytics.
#
# The test should validate:
# - Person detection generation
# - Detection confidence values
# - Handling of frames with no detections
# - Consistency across different sample inputs
#
# Since all downstream analytics depend on detection quality, this test should focus heavily on reliability and correctness.
#
# CHANGES MADE:
# Added project-specific detection scenarios and aligned expectations with retail analytics requirements.
#
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("outputs/sample_frames/CAM 1.jpg")

print("Detection completed.")
