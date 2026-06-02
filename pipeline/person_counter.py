from ultralytics import YOLO


class PersonCounter:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def count_people(self, frame):

        results = self.model(
            frame,
            verbose=False
        )

        count = 0

        for result in results:
            for box in result.boxes:

                cls = int(box.cls[0])

                if self.model.names[cls] == "person":
                    count += 1

        return count