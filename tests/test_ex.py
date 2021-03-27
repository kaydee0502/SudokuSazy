def test_example(app,client):
    print(client)
    response = client.post("/")
    assert response.status_code == 405