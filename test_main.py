from main import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Aleksander" in res.data