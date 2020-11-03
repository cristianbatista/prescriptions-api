def test_prescriptions_success(client):
    body = {
        "clinic": {"id": 1},
        "physician": {"id": 4},
        "patient": {"id": 56},
        "text": "Dipirona ao dormir - 30 gotas quando sentir dor",
    }

    response = client.post("/prescriptions", headers={}, json=body)
    assert response.status_code == 201
