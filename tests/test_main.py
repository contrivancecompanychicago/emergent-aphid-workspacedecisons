from fastapi.testclient import TestClient
from app.main import app
from app.models import EmployeeOnboarding

client = TestClient(app)

def test_create_and_get_onboarding():
    payload = {"full_name": "Jane Doe", "email": "jane@example.com", "position": "Nurse"}
    resp = client.post("/onboarding", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["full_name"] == "Jane Doe"
    emp_id = data["id"]

    get_resp = client.get(f"/onboarding/{emp_id}")
    assert get_resp.status_code == 200
    got = get_resp.json()
    assert got["email"] == "jane@example.com"
