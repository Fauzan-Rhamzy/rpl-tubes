# test_invoice_details.py
import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_invoice_detail(client):
    # Login 
    client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)
    
    response = client.get('/PetugasAdmin/Invoice/Detail/P0001RM', follow_redirects=True)
    assert response.status_code == 200

    # detail view
    assert b'Invoice Detail' in response.data
    assert b'Nomor Rekam Medis: P0001RM' in response.data
    assert b'Nama: Ahmad Fauzi' in response.data
    assert b'Detail Layanan' in response.data
    assert b'dr. Jessica Anggraeni, SpA' in response.data 
    assert b'Spesialisasi: Anak' in response.data  
    assert b'Total Pembayaran: Rp 180,000.00' in response.data
    assert b'Tanggal Janji: 2024-12-16' in response.data
    assert b'Kontak: 081234567890' in response.data