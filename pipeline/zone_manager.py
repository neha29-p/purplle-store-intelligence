class ZoneManager:

    def __init__(self):
        self.visitor_zones = {}

    def assign_zone(self, visitor_id: str, zone_id: str):
        previous_zone = self.visitor_zones.get(visitor_id)
        self.visitor_zones[visitor_id] = zone_id
        return previous_zone

    def get_zone(self, visitor_id: str):
        return self.visitor_zones.get(visitor_id)

    def remove_visitor(self, visitor_id: str):
        self.visitor_zones.pop(visitor_id, None)