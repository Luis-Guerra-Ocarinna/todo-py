def test_index(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}