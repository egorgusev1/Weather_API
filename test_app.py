import sys
import os

# add current directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from weather_app.main import app as flask_app
from flask import json


# Defines a mock response simulating weatther data as returned from the real API
MOCK_WEATHER_RESPONSE = {
    "weather": {
        "main": {
            "temp": 22.5,
            "humidity": 60,
            "pressure": 1012
        },
        "weather": [{
            "description": "clear sky",
            "icon": "01d"
        }],
        "wind": {
            "speed": 5.1
        },
        "dt": 1650000000,
        "timezone": -14400
    },
    "forecast": [{}] * 5,
    "time": "2022-04-15 14:00:00"
}


# Define a reusable pytest fixture that sets up a test client for the Flask app
@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


# Test when the city is provided, verifies that response status is OK (code 200), and that 'weather' key
# is present in the response.
def test_api_weather_with_city(client, monkeypatch):
    monkeypatch.setattr("weather_app.main.get_weather", lambda city: MOCK_WEATHER_RESPONSE)
    response = client.get("/api/weather?city=London")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "weather" in data

# Test when the city is not provided, and is using IP based loaction verifies that response status is OK (code 200), and that 'weather' key
# is present in the response.
def test_api_weather_without_city(client, monkeypatch):
    monkeypatch.setattr("weather_app.main.get_user_location", lambda req: "Paris")
    monkeypatch.setattr("weather_app.main.get_weather", lambda city: MOCK_WEATHER_RESPONSE)
    response = client.get("/api/weather")
    assert response.status_code == 200

# Test a failure case where weather data retrieval fails
def test_api_weather_failure(client, monkeypatch):
    monkeypatch.setattr("weather_app.main.get_weather", lambda city: None)
    response = client.get("/api/weather?city=InvalidCity")
    assert response.status_code == 400
