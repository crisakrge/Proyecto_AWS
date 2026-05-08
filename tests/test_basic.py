def test_home_status(client):
    """Valida que la raíz responda 200 OK"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"online" in rv.data