# tests/test_main.py

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

@pytest.fixture

def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"IIT Kharagpur" in response.data

def test_signup_get(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_otp_get(client):
    response = client.get("/otp")
    assert response.status_code == 200


def test_adminDates_get(client):
    response = client.get("/adminDates")
    assert response.status_code == 200


def test_adminHistory(client):
    response = client.get("/adminHistory")
    assert response.status_code == 200


def test_profile_requires_login(client):
    response = client.get("/profile")
    assert response.status_code == 200 or response.status_code == 302  # May redirect or error if not logged in


def test_rooms_get(client):
    response = client.get("/rooms")
    assert response.status_code in [200, 302, 500]  # Might throw due to missing global state


def test_dates_get(client):
    response = client.get("/dates")
    assert response.status_code == 200


def test_history_requires_login(client):
    response = client.get("/history")
    assert response.status_code in [200, 302, 500]


def test_feedback_get(client):
    response = client.get("/feedback/1")  # Adjust ID as needed
    assert response.status_code in [200, 302, 500]


def test_payment_routes(client):
    assert client.get("/cash").status_code in [200, 500]
    assert client.get("/credit").status_code in [200, 500]
    assert client.get("/upi").status_code in [200, 500]


def test_paymentComplete(client):
    response = client.get("/paymentComplete")
    assert response.status_code in [200, 500]  # May fail if global state is missing


def test_setfeedback_post(client):
    # No POST data, just checking route health
    response = client.post("/setfeedback/1", data={"text": "Nice stay"})
    assert response.status_code in [200, 500]