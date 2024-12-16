import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_mark_invoice_as_paid(client):
    """Test untuk menandai tagihan sebagai lunas."""

    login_response = client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)

    assert login_response.status_code == 200
    assert b'Selamat Datang' in login_response.data 

    invoice_id = 'P0001RM' 
    list_response = client.get('/PetugasAdmin/Invoice', follow_redirects=True) 

    assert list_response.status_code == 200
    assert b'P0001RM' in list_response.data 
    # Status awal
    assert b'Belum Lunas' in list_response.data  

    detail_response = client.post('/PetugasAdmin/Invoice/Detail', data={
        'nomor_rekam_medis': invoice_id
    }, follow_redirects=True)

    assert detail_response.status_code == 200
    assert b'Invoice Detail' in detail_response.data

    # Tandai Lunas
    mark_paid_response = client.post('/PetugasAdmin/Invoice/MarkAsPaid', data={
        'id_transaksi': invoice_id
    }, follow_redirects=True)

    assert mark_paid_response.status_code == 200

    list_response_after = client.get('/PetugasAdmin/Invoice', follow_redirects=True) 
    assert b'P0001RM' in list_response_after.data
    assert b'Lunas' in list_response_after.data  