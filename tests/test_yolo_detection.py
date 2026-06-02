from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("outputs/sample_frames/CAM 1.jpg")

print("Detection completed.")