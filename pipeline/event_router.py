from datetime import datetime
from app.models import Event
from app.constants import ZONE_ENTER

class EventRouter:
    def route_zone_change(
        self,
        visitor_id: str,
        store_id: str,
        camera_id: str,
        zone_id: str
    ):
        timestamp = datetime.utcnow().isoformat()

        return Event(
            event_id=f"zone_enter_{visitor_id}_{timestamp}",
            store_id=store_id,
            camera_id=camera_id,
            visitor_id=visitor_id,
            event_type=ZONE_ENTER,
            timestamp=timestamp,
            zone_id=zone_id,
            confidence=1.0
        )