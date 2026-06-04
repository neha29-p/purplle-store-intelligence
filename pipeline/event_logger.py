import json
from datetime import datetime
from pathlib import Path

EVENT_FILE = Path("data/events/events.jsonl")

def write_event(event):

    EVENT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(EVENT_FILE, "a") as f:
        f.write(
            json.dumps(event) + "\n"
        )

def create_entry_event(visitor_id):

    return {
        "event_type": "entry",
        "id_token": f"ID_{visitor_id}",
        "store_code": "store_1076",
        "camera_id": "cam1",
        "event_timestamp": datetime.utcnow().isoformat(),
        "is_staff": False,
        "gender_pred": None,
        "age_pred": None,
        "age_bucket": None,
        "is_face_hidden": False,
        "group_id": None,
        "group_size": None
    }

def create_exit_event(visitor_id):

    return {
        "event_type": "exit",
        "id_token": f"ID_{visitor_id}",
        "store_code": "store_1076",
        "camera_id": "cam1",
        "event_timestamp": datetime.utcnow().isoformat(),
        "is_staff": False,
        "gender_pred": None,
        "age_pred": None,
        "age_bucket": None,
        "is_face_hidden": False,
        "group_id": None,
        "group_size": None
    }