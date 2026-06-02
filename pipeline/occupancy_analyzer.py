from pipeline.person_counter import PersonCounter
import cv2


class OccupancyAnalyzer:

    def __init__(self):
        self.counter = PersonCounter()

    def analyze_video(self, video_path):

        cap = cv2.VideoCapture(video_path)

        frame_number = 0

        occupancy_samples = []

        while True:

            success, frame = cap.read()

            if not success:
                break

            frame_number += 1

            # sample roughly every second
            if frame_number % 30 != 0:
                continue

            people = self.counter.count_people(frame)

            occupancy_samples.append(people)

        cap.release()

        return occupancy_samples