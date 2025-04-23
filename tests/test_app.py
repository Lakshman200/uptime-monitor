from app import app

def test_check_endpoint():
    client = app.test_client()
    response = client.post("/check", json={
        "urls": ["https://google.com"]
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "https://google.com" in data

