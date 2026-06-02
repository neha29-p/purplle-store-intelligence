from app.database import get_db_connection

def get_store_metrics(store_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Unique visitors (exclude staff)
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0 AND event_type = 'ENTRY'
    ''', (store_id,))
    unique_visitors = cursor.fetchone()[0] or 0

    # Conversion rate: visitors who reached billing / total visitors
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0
        AND event_type IN ('BILLING_QUEUE_JOIN', 'ZONE_ENTER')
        AND zone_id LIKE '%BILLING%'
    ''', (store_id,))
    billing_visitors = cursor.fetchone()[0] or 0

    conversion_rate = round(billing_visitors / unique_visitors * 100, 2) if unique_visitors > 0 else 0.0

    # Avg dwell time across all zones (seconds)
    cursor.execute('''
        SELECT AVG(dwell_ms) FROM events
        WHERE store_id = ? AND is_staff = 0 AND dwell_ms > 0
    ''', (store_id,))
    avg_dwell_ms = cursor.fetchone()[0] or 0
    avg_dwell_seconds = round(avg_dwell_ms / 1000, 1)

    # Current queue depth (latest billing queue join count)
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND event_type = 'BILLING_QUEUE_JOIN'
        AND visitor_id NOT IN (
            SELECT visitor_id FROM events
            WHERE store_id = ? AND event_type = 'EXIT'
        )
    ''', (store_id, store_id))
    queue_depth = cursor.fetchone()[0] or 0

    # Abandonment rate: left billing without purchase
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND event_type = 'BILLING_QUEUE_ABANDON'
    ''', (store_id,))
    abandoned = cursor.fetchone()[0] or 0

    abandonment_rate = round(abandoned / billing_visitors * 100, 2) if billing_visitors > 0 else 0.0

    conn.close()

    return {
        "store_id": store_id,
        "unique_visitors": unique_visitors,
        "conversion_rate": conversion_rate,
        "avg_dwell_seconds": avg_dwell_seconds,
        "queue_depth": queue_depth,
        "abandonment_rate": abandonment_rate
    }