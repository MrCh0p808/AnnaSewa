"""
Simple tests to ensure /health and /status exist and return expected fields.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_status_keys():
    r = client.get("/status")
    assert r.status_code == 200
    body = r.json()
    assert "api_version" in body
    assert "db_status" in body

