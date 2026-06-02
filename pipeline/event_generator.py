from datetime import datetime
from app.models import Event
from app.constants import ENTRY

def create_entry_event(
    visitor_id: str,
    store_id: str,
    camera_id: str
) -> Event:

    timestamp = datetime.utcnow().isoformat()

    return Event(
        event_id=f"entry_{visitor_id}_{timestamp}",
        store_id=store_id,
        camera_id=camera_id,
        visitor_id=visitor_id,
        event_type=ENTRY,
        timestamp=timestamp,
        confidence=1.0
    )