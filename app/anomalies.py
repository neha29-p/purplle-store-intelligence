from app.database import get_db_connection

def get_store_anomalies(store_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    anomalies = []

    # 1. Billing Queue Spike
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) 
        FROM events 
        WHERE store_id = ? AND event_type = 'BILLING_QUEUE_JOIN' 
        AND visitor_id NOT IN (SELECT visitor_id FROM events WHERE store_id = ? AND event_type = 'EXIT')
    ''', (store_id, store_id))
    queue_depth = cursor.fetchone()[0] or 0
    
    if queue_depth >= 5:
        anomalies.append({
            "type": "BILLING_QUEUE_SPIKE",
            "severity": "CRITICAL" if queue_depth >= 8 else "WARN",
            "message": f"Queue depth is {queue_depth} — unusually high",
            "suggested_action": "Open additional billing counter"
        })

    # 2. Conversion Drop (High entry, low billing)
    cursor.execute('''
        SELECT 
            (SELECT COUNT(*) FROM events WHERE store_id = ? AND event_type = 'ENTRY') as entry_count,
            (SELECT COUNT(*) FROM events WHERE store_id = ? AND event_type = 'BILLING_QUEUE_JOIN') as bill_count
    ''', (store_id, store_id))
    row = cursor.fetchone()
    entry_count, bill_count = row['entry_count'] or 0, row['bill_count'] or 0
    
    if entry_count > 10 and (bill_count / entry_count) < 0.05:
        anomalies.append({
            "type": "CONVERSION_DROP",
            "severity": "WARN",
            "message": "Conversion rate is below 5%",
            "suggested_action": "Check product placement or checkout accessibility"
        })

    conn.close()
    return {"store_id": store_id, "anomaly_count": len(anomalies), "anomalies": anomalies}