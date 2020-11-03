

def test_health_success(client):

    response = client.get("/health", headers={})
    assert response.status_code == 200
