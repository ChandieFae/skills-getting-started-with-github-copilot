import sys
import os

# Ensure the repository root is on PYTHONPATH so `src` can be imported during tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.app import app


client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    # A known activity from the seed data should be present
    assert "Chess Club" in data


def test_signup_activity():
    email = "ci-test@example.com"
    activity = "Chess Club"
    # Use query params to sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    # Ensure the email was appended to the participants list
    all_activities = client.get("/activities").json()
    assert email in all_activities[activity]["participants"]
