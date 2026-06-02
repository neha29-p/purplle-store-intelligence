import requests

# 1. Define a completely fresh unique test event payload
duplicate_payload = {
    "event_id": "evt_idempotency_test_777",
    "store_id": "STORE_BANGALORE_02",
    "camera_id": "CAM_AISLE_3",
    "visitor_id": "shopper_555",
    "event_type": "ZONE_ENTER",
    "timestamp": "2026-05-30T20:45:00Z",
    "zone_id": "perfume_section",
    "dwell_ms": 12000,
    "is_staff": False,
    "confidence": 0.96,
    "metadata": {}
}

# 2. Fire the exact same request TWICE consecutively
print("--- Sending First Request ---")
res1 = requests.post("http://127.0.0.1:8000/api/events", json=duplicate_payload)
print("First Response:", res1.json())

print("\n--- Sending Duplicate Request ---")
res2 = requests.post("http://127.0.0.1:8000/api/events", json=duplicate_payload)
print("Second Response:", res2.json())