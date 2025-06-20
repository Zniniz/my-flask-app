from app import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'If you are reading this you are all fatties!' in resp.data
