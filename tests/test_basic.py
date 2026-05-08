def test_home_status(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"online" in rv.data