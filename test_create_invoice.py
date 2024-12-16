import pytest
from flask import session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_create_invoice(client):
    # Login 
    client.post('/login', data={
        'username': 'admin_rizki',
        'password': 'rizkiadmin'
    }, follow_redirects=True)

    new_invoice_data = {
        'nama_pasien': 'Ahmad Fauzi', 
        'tanggal_transaksi': '2024-12-16',
        'selected_doctors': ['D001'],  
        'total_tarif': '200000'  
    }

    response = client.post('/PetugasAdmin/Invoice', data=new_invoice_data, follow_redirects=True)

    print("Response Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Data:", response.data.decode('utf-8'))  

    assert response.status_code == 405
   
def test_invoice_display_after_creation(client):
    response = client.get('/PetugasAdmin/Invoice', follow_redirects=True)

    print("Invoice Listing Response Data:", response.data.decode('utf-8'))