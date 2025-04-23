from uptime_monitor.app import app  # Make sure app.py is inside uptime_monitor/ folder

def test_check_endpoint():
    client = app.test_client()
    response = client.post("/check", json={"urls": ["https://google.com"]})
    assert response.status_code == 200
    assert "https://google.com" in response.get_json()

