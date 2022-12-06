def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_create(client):
    response = client.post('/add',
                           data={'title': 'test_create'},
                           follow_redirects=True)

    assert b'test_create' in response.data


def test_update(client):
    response = client.post('/update/0',
                           data={'title': 'test_update'},
                           follow_redirects=True)
    assert b'test_create' not in response.data
    assert b'test_update' in response.data


def test_delete(client):
    response = client.get('/delete/0', follow_redirects=True)
    assert b'test_' not in response.data
