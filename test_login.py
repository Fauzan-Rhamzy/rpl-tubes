import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_login_administrator(client):
    response = client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)

    assert b'Selamat Datang' in response.data
    assert b'Klinik SehatBro.' in response.data

    assert session.get('role') == 'Petugas Admin' 