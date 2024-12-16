# test_invoices.py
import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_display_invoices(client):
    # Login
    client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)
    
    # Invoice page
    response = client.get('/PetugasAdmin/Invoice', follow_redirects=True)
    
    #Pengecekan isi tabel
    assert b'Invoice' in response.data
    assert b'Nomor Rekam Medis' in response.data
    assert b'Nama Pasien' in response.data
    assert b'Jumlah Pembayaran (Rp)' in response.data
    assert b'Detail' in response.data
    assert b'Status Pembayaran' in response.data
    
    assert b'P0001RM' in response.data and b'Ahmad Fauzi' in response.data and b'180,000.00' in response.data and b'Lunas' in response.data
    assert b'P0002SN' in response.data and b'Siti Nurhaliza' in response.data and b'199,000.00' in response.data and b'Lunas' in response.data
    assert b'P1002MA' in response.data and b'Maria Agnes' in response.data and b'400,000.00' in response.data and b'Lunas' in response.data
    assert b'P2001ES' in response.data and b'Eko Susilo' in response.data and b'100,000.00' in response.data and b'Lunas' in response.data
    assert b'P2002RM' in response.data and b'Riana Maharani' in response.data and b'150,000.00' in response.data and b'Lunas' in response.data
    assert b'P4002MI' in response.data and b'Melati Indah' in response.data and b'190,000.00' in response.data and b'Lunas' in response.data