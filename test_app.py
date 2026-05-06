import pytest
from application import application  # Cambiar 'app' por 'application'

@pytest.fixture
def client():
    with application.test_client() as client:  # Cambiar 'app' por 'application'
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b'Hello, World!'