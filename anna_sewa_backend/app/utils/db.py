"""
Small helper to check DB connectivity for /status endpoint.
If DATABASE_URL is not set, we return "not_configured".
If set, we try a quick psycopg2 connect with a short timeout.
"""
import os
import psycopg2

def check_db_connection():
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        return "not_configured"
    try:
        conn = psycopg2.connect(db_url, connect_timeout=2)
        conn.close()
        return "connected"
    except Exception:
        # Do not bubble real DB errors to clients here, return simple status
        return "disconnected"

