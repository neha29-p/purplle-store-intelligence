import os
import sqlite3
import json

# 1. Absolute path setup targeting the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data/store_intelligence.db")

# 2. Root-level import for the models module
from app.models import Event

# 3. Core Database Connection Configuration
def get_db_connection():
    """Creates and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 4. Database Ingestion Function with Idempotency Guard
def add_event(event_id, store_id, camera_id, visitor_id, event_type, timestamp, zone_id=None, dwell_ms=0, is_staff=0, confidence=0.0, metadata=None):
    """Inserts a new shopper intelligence event into the database. Returns True if inserted, False if duplicate."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    metadata_json = json.dumps(metadata) if metadata else "{}"
    
    try:
        cursor.execute('''
            INSERT INTO events (event_id, store_id, camera_id, visitor_id, event_type, timestamp, zone_id, dwell_ms, is_staff, confidence, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (event_id, store_id, camera_id, visitor_id, event_type, timestamp, zone_id, dwell_ms, is_staff, confidence, metadata_json))
        conn.commit()
        print(f"Successfully logged event {event_id} ({event_type}) to local DB!")
        return True
    except sqlite3.IntegrityError:
        print(f"Warning: Event {event_id} already exists in database. Idempotency safeguard triggered.")
        return False
    finally:
        conn.close()

# 5. Database Initialization (Tables setup)
def initialize_db():
    """Initializes the SQLite database and creates the events table if it doesn't exist."""
    # Ensure data directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            store_id TEXT NOT NULL,
            camera_id TEXT NOT NULL,
            visitor_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            zone_id TEXT,
            dwell_ms INTEGER DEFAULT 0,
            is_staff INTEGER DEFAULT 0,
            confidence REAL DEFAULT 0.0,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Automatically initialize database when module loads
if __name__ == "__main__":
    initialize_db()
    print("Database initialization check complete.")