import cv2
import os

# Paths to your videos - make sure these names match EXACTLY what is in your folder
video_paths = ["CAM 3.mp4", "CAM 5.mp4"] 

caps = []
for path in video_paths:
    if not os.path.exists(path):
        print(f"ERROR: File not found: {path}")
    else:
        caps.append(cv2.VideoCapture(path))

if len(caps) < 2:
    print("Could not load all videos. Check file names in sync_helper.py")
    exit()

print("Press 'q' to exit. If you see this, videos loaded successfully.")

while True:
    frames = []
    for cap in caps:
        ret, frame = cap.read()
        if not ret:
            # If video ends, restart it
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        
        # Only resize if frame is valid
        if ret and frame is not None:
            frames.append(cv2.resize(frame, (640, 360)))
        else:
            print("Failed to read a frame.")
            break

    if len(frames) == 2:
        combined = cv2.hconcat(frames)
        cv2.imshow('Sync Helper', combined)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

for cap in caps: cap.release()
cv2.destroyAllWindows()