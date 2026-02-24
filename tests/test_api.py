def test_api_response(client):
    response = client.get("/api/data")
    assert response.status_code == 200


def test_api_post_data(client):
    payload = {
        "temperature": 36.5,
        "humidity": 55.0
    }
    response = client.post("/api/data", json=payload)
    assert response.status_code == 201


def test_api_data_structure(client):
    response = client.get("/api/data")
    data = response.get_json()

    assert isinstance(data, list)

    if len(data) > 0:
        item = data[0]
        assert "temperature" in item
        assert "humidity" in item
        assert "created_at" in item


def test_api_values_range(client):
    payload = {
        "temperature": 37.0,
        "humidity": 60.0
    }
    client.post("/api/data", json=payload)

    response = client.get("/api/data")
    data = response.get_json()

    assert data[0]["temperature"] >= 0
    assert data[0]["humidity"] >= 0