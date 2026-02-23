def test_api_response(client):
    response = client.get("/api/data")
    assert response.status_code == 200