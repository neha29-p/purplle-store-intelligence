from pathlib import Path
import cv2

video_dir = Path("data/videos/CCTV Footage")
output_dir = Path("outputs/sample_frames")

output_dir.mkdir(parents=True, exist_ok=True)

for video_path in video_dir.glob("*.mp4"):
    cap = cv2.VideoCapture(str(video_path))

    success, frame = cap.read()

    if success:
        output_file = output_dir / f"{video_path.stem}.jpg"
        cv2.imwrite(str(output_file), frame)
        print(f"Saved: {output_file}")

    cap.release()