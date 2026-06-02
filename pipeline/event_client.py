import requests

def send_event(event):
    # Sends the Pydantic event object to our FastAPI endpoint
    response = requests.post(
        "http://127.0.0.1:8000/api/events",
        json=event.model_dump()
    )
    return response.json()