from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()

def test_signup_success():
    response = client.post("/activities/Chess Club/signup?email=teststudent@mergington.edu")
    assert response.status_code == 200
    assert "Signed up teststudent@mergington.edu for Chess Club" in response.json()["message"]

def test_signup_duplicate():
    # First signup
    client.post("/activities/Programming Class/signup?email=dup@mergington.edu")
    # Duplicate signup
    response = client.post("/activities/Programming Class/signup?email=dup@mergington.edu")
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"

def test_signup_activity_not_found():
    response = client.post("/activities/Nonexistent/signup?email=someone@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"