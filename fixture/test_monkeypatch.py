import pytest
import requests

# The function we want to test
def get_temperature_alert(city: str) -> str:
    # This makes a real network request over the internet
    response = requests.get(f"https://api.weather.com/v1/{city}")
    data = response.json()
    
    if data["temp"] > 40:
        return "Extreme Heat Warning!"
    return "Weather is normal."

# The Must-Know Pytest Concept
def test_get_temperature_alert_heatwave(monkeypatch):
    # 1. Define a fake response object
    class FakeResponse:
        def json(self):
            return {"temp": 45} # Simulate a dangerous 45°C day
            
    # 2. Use monkeypatch to intercept requests.get and return our fake response
    monkeypatch.setattr(requests, "get", lambda url: FakeResponse())

    # 3. Run the test. It won't actually touch the internet!
    result = get_temperature_alert("Sahara")
    assert result == "Extreme Heat Warning!"