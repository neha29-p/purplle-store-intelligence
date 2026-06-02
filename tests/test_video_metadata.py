from pathlib import Path
import cv2

print("SCRIPT STARTED\n")

video_dir = Path("data/videos/CCTV Footage")

print("Looking in:", video_dir.resolve())
print("Folder exists:", video_dir.exists())

videos = list(video_dir.glob("*.mp4"))

print("Videos found:", len(videos))

for video_path in videos:
    print("\n" + "=" * 50)
    print("Processing:", video_path.name)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        print("ERROR: Could not open video.")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = frames / fps if fps > 0 else 0

    print(f"Resolution : {width} x {height}")
    print(f"FPS        : {fps:.2f}")
    print(f"Frames     : {frames}")
    print(f"Duration   : {duration:.2f} sec")

    cap.release()

print("\nSCRIPT FINISHED")