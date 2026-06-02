from fastapi import FastAPI, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

# Internal imports
from app.models import Event
import app.database as database
from app.health import check_db_health
from app.metrics import get_store_metrics
from app.funnel import get_store_funnel
from app.anomalies import get_store_anomalies
from app.logger import log_request_middleware # Ensure this is imported

# Initialize the app
app = FastAPI(title="Apex Retail Store Intelligence API", version="1.0.0")

# Register the middleware immediately after initialization
app.add_middleware(BaseHTTPMiddleware, dispatch=log_request_middleware)

# --- ROUTES ---

@app.get("/")
def read_root():
    return {"status": "online", "message": "Apex Retail Analytics Engine is running"}

@app.get("/health")
def get_health():
    is_db_healthy = check_db_health()
    if is_db_healthy:
        return {"status": "healthy", "database": "connected"}
    else:
        raise HTTPException(status_code=503, detail={"status": "unhealthy", "database": "disconnected"})

@app.get("/stores/{store_id}/metrics")
def get_metrics(store_id: str):
    return get_store_metrics(store_id)

@app.get("/stores/{store_id}/funnel")
def get_funnel(store_id: str):
    return get_store_funnel(store_id)

@app.get("/stores/{store_id}/anomalies")
def get_anomalies(store_id: str):
    return get_store_anomalies(store_id)

@app.post("/api/events")
def ingest_event(event: Event):
    try:
        is_new = database.add_event(
            event_id=event.event_id,
            store_id=event.store_id,
            camera_id=event.camera_id,
            visitor_id=event.visitor_id,
            event_type=event.event_type,
            timestamp=event.timestamp,
            zone_id=event.zone_id,
            dwell_ms=event.dwell_ms,
            is_staff=1 if event.is_staff else 0,
            confidence=event.confidence,
            metadata=event.metadata
        )
        if is_new:
            return {"status": "success", "message": f"Event {event.event_id} ingested successfully"}
        else:
            return {"status": "duplicate", "message": f"Event {event.event_id} already processed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))