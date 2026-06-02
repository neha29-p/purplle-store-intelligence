from math import sqrt

class VisitorTracker:

    def __init__(self):

        self.visitors = {}
        self.next_id = 1

        self.entries = 0
        self.exits = 0

        self.counting_line = 300

    def _centroid(self, box):

        x1, y1, x2, y2 = box

        return (
            (x1 + x2) // 2,
            (y1 + y2) // 2
        )

    def update(self, detections):

        for box in detections:

            cx, cy = self._centroid(box)

            matched_id = None

            for visitor_id, data in self.visitors.items():

                vx = data["x"]
                vy = data["y"]

                distance = sqrt(
                    (cx - vx) ** 2 +
                    (cy - vy) ** 2
                )

                if distance < 50:
                    matched_id = visitor_id
                    break

            if matched_id is None:

                self.visitors[self.next_id] = {
                    "x": cx,
                    "y": cy
                }

                self.next_id += 1

            else:

                previous_y = self.visitors[matched_id]["y"]

                # ENTRY
                if (
                    previous_y > self.counting_line
                    and cy <= self.counting_line
                ):
                    self.entries += 1

                # EXIT
                elif (
                    previous_y < self.counting_line
                    and cy >= self.counting_line
                ):
                    self.exits += 1

                self.visitors[matched_id] = {
                    "x": cx,
                    "y": cy
                }

        return {
            "visitors": len(self.visitors),
            "entries": self.entries,
            "exits": self.exits
        }