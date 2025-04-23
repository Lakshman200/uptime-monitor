import requests

def test_check_endpoint():
    response = requests.post("http://localhost:5050/check", json={
        "urls": ["https://google.com"]
    })
    assert response.status_code == 200
    assert "https://google.com" in response.json()

