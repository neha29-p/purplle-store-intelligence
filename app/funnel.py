from app.database import get_db_connection

def get_store_funnel(store_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Stage 1: Total unique visitors who entered (exclude staff)
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0 AND event_type = 'ENTRY'
    ''', (store_id,))
    entry_count = cursor.fetchone()[0] or 0

    # Stage 2: Visitors who visited at least one zone
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0
        AND event_type = 'ZONE_ENTER'
        AND visitor_id IN (
            SELECT DISTINCT visitor_id FROM events
            WHERE store_id = ? AND event_type = 'ENTRY'
        )
    ''', (store_id, store_id))
    zone_visit_count = cursor.fetchone()[0] or 0

    # Stage 3: Visitors who joined billing queue
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0
        AND event_type = 'BILLING_QUEUE_JOIN'
        AND visitor_id IN (
            SELECT DISTINCT visitor_id FROM events
            WHERE store_id = ? AND event_type = 'ENTRY'
        )
    ''', (store_id, store_id))
    billing_queue_count = cursor.fetchone()[0] or 0

    # Stage 4: Visitors who completed a purchase
    # A purchase = visitor was in billing zone and did NOT abandon
    cursor.execute('''
        SELECT COUNT(DISTINCT visitor_id) FROM events
        WHERE store_id = ? AND is_staff = 0
        AND event_type = 'BILLING_QUEUE_JOIN'
        AND visitor_id NOT IN (
            SELECT DISTINCT visitor_id FROM events
            WHERE store_id = ? AND event_type = 'BILLING_QUEUE_ABANDON'
        )
        AND visitor_id IN (
            SELECT DISTINCT visitor_id FROM events
            WHERE store_id = ? AND event_type = 'ENTRY'
        )
    ''', (store_id, store_id, store_id))
    purchase_count = cursor.fetchone()[0] or 0

    conn.close()

    # Drop-off percentages
    entry_to_zone = round((1 - zone_visit_count / entry_count) * 100, 1) if entry_count > 0 else 0.0
    zone_to_billing = round((1 - billing_queue_count / zone_visit_count) * 100, 1) if zone_visit_count > 0 else 0.0
    billing_to_purchase = round((1 - purchase_count / billing_queue_count) * 100, 1) if billing_queue_count > 0 else 0.0

    return {
        "store_id": store_id,
        "funnel": {
            "entry": entry_count,
            "zone_visit": zone_visit_count,
            "billing_queue": billing_queue_count,
            "purchase": purchase_count
        },
        "dropoff_percentages": {
            "entry_to_zone": entry_to_zone,
            "zone_to_billing": zone_to_billing,
            "billing_to_purchase": billing_to_purchase
        },
        "conversion_rate": round(purchase_count / entry_count * 100, 2) if entry_count > 0 else 0.0
    }