import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_search_invoice_by_patient_name(client):
    """Test untuk memastikan pencarian tagihan berdasarkan nama pasien berfungsi dengan baik."""

    #Login
    login_response = client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)

    assert login_response.status_code == 200
    assert b'Selamat Datang' in login_response.data

    
    search_query = 'Siti Nurhaliza'  # Nama pasien yang ingin dicari
    search_response = client.get(f'/PetugasAdmin/Invoice?search={search_query}', follow_redirects=True)

    # Verifikasi hasil pencarian
    assert search_response.status_code == 200
    assert b'Siti Nurhaliza' in search_response.data  
    assert b'P0002SN' in search_response.data 
    
    # Pastikan pasien lain tidak ada dalam hasil pencarian
    assert b'Ahmad Fauzi' not in search_response.data  
