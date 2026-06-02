import app.database as database

def check_db_health() -> bool:
    """Verifies the database connection by executing a simple query."""
    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        # Execute a lightweight test query
        cursor.execute("SELECT 1;")
        cursor.fetchone()
        conn.close()
        return True
    except Exception as e:
        print(f"Database health check failed: {e}")
        return False