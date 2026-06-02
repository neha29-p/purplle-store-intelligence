from datetime import datetime

class VisitorRegistry:

    def __init__(self):
        self.visitors = {}

    def register(self, visitor_id: str):
        now = datetime.utcnow().isoformat()

        if visitor_id not in self.visitors:
            self.visitors[visitor_id] = {
                "first_seen": now,
                "last_seen": now,
                "visit_count": 1,
                "current_zone": None
            }
        else:
            self.visitors[visitor_id]["last_seen"] = now

    def get(self, visitor_id: str):
        return self.visitors.get(visitor_id)

    def count(self):
        return len(self.visitors)