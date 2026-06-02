import sys
from pathlib import Path
import pandas as pd
import uuid

# --- PATH FIX: This allows imports from the 'app' folder ---
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.database import add_event

def ingest_transactions(csv_path):
    # Load the CSV
    df = pd.read_csv(csv_path)
    
    # Combine date and time into a proper datetime object
    # Matches your '10-04-2026 14:30:00' format
    df['datetime'] = pd.to_datetime(df['order_date'] + ' ' + df['order_time'], format='%d-%m-%Y %H:%M:%S')
    
    # Filter for April 10th
    target_date = pd.Timestamp('2026-04-10')
    daily_sales = df[df['datetime'].dt.date == target_date.date()]
    
    count = 0
    for _, row in daily_sales.iterrows():
        # Ingest into DB
        success = add_event(
            event_id=str(uuid.uuid4()),
            store_id=str(row['store_id']),
            camera_id="CAM_5_CHECKOUT",
            visitor_id=f"cust_{row['customer_number']}",
            event_type="BILLING_QUEUE_JOIN",
            timestamp=row['datetime'].isoformat(),
            zone_id="BILLING_ZONE"
        )
        if success:
            count += 1
            
    print(f"Successfully ingested {count} transactions into the database.")

if __name__ == "__main__":
    # Ensure this path is correct relative to where you run the script
    path = "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
    ingest_transactions(path)