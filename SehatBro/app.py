import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session
from psycopg2.extras import DictCursor

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=DictCursor)  # Use DictCursor


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('homepage'))
    return render_template("LoginPage/index.html")

@app.route('/')
def logout():
    return render_template("LoginPage/index.html")

# PASIEN #################################################################
@app.route('/HomePage')
def homepage():
    return render_template("Pasien/HomepagePasien/index.html")

@app.route('/JadwalTemu')
def jadwaltemu():
    return render_template("Pasien/JadwalTemu/index.html")

@app.route('/Booking')
def booking():
    query = """
        SELECT d.Spesialisasi, d.Nama, STRING_AGG(j.Hari || ' ' || j.Jam::TEXT, ', ') AS Jadwal
        FROM Dokter d
        JOIN Jadwal_Dokter j ON d.ID_Dokter = j.ID_Dokter
        GROUP BY d.Spesialisasi, d.Nama
        ORDER BY d.Spesialisasi, d.Nama
    """
    cursor.execute(query)
    result = cursor.fetchall()

    doctors_data = {}
    for row in result:
        specialization = row[0].lower()
        if specialization not in doctors_data:
            doctors_data[specialization] = []
        doctors_data[specialization].append({
            "name": row[1],
            "schedule": row[2]
        })

    return render_template("Pasien/Booking/index.html", doctors_data=doctors_data)
    # return render_template("Booking/index.html")

@app.route('/Profile')
def profile():
    return render_template("Pasien/Profile/index.html")

@app.route('/Tagihan')
def tagihan():
    return render_template("Pasien/Tagihan/index.html")

###########################################################

# ADMIN ##################################################
@app.route('/Admin')
def homepageAdmin():
    return render_template("Admin/Homepage/homepage.html")

#kelola dokter
@app.route('/Admin/KelolaDokter', methods=['GET', 'POST'])
def kelolaDokter():
    if request.method == 'POST':
        npa = request.form['doctor-npa']
        nama= request.form['doctor-name']
        spesialisasi= request.form['doctor-specialty']
        kuota= request.form['doctor-quota']
        tarif= request.form['doctor-fee']
        username= request.form['doctor-username']
        password= request.form['doctor-password']

        cursor.execute

    cursor.execute("""
        SELECT dokter.npa as npa, dokter.nama as nama, dokter.spesialisasi as spesialisasi, 
            jadwal_dokter.kuota_pasien as kuota_pasien, dokter.tarif, 
            jadwal_dokter.hari as hari, jadwal_dokter.jam_mulai as jam_mulai, 
            jadwal_dokter.jam_selesai as jam_selesai, 
            jadwal_dokter.id_jadwal as id_jadwal  -- Ensure this field is included
        FROM dokter
        JOIN jadwal_dokter ON dokter.npa = jadwal_dokter.npa
    """)

    jadwal_dokter = cursor.fetchall()
    # print(jadwal_dokter)
    return render_template("Admin/KelolaDokter/kelolaDokter.html", jadwal_dokter = jadwal_dokter)

#edit dokter
@app.route('/Admin/KelolaDokter/EditDokter', methods=['GET', 'POST'])
def editDokter():
    id_jadwal = request.args.get('id_jadwal')

    if not id_jadwal:
        return "No ID Jadwal", 400

    if request.method == 'POST':
        npa = request.form['doctor-npa']
        kuota = request.form['doctor-quota']
        hari = request.form['doctor-day']
        mulai = request.form['schedule-time-start']
        akhir = request.form['schedule-time-end']
        tarif = request.form['doctor-fee']

        cursor.execute("""
            update jadwal_dokter
            SET npa=%s, 
                kuota_pasien=%s, 
                hari=%s, 
                jam_mulai=%s, 
                jam_selesai=%s
            WHERE id_jadwal=%s
        """, (npa, kuota, hari, mulai, akhir, id_jadwal))
        connection.commit()

        cursor.execute("""
                update  dokter 
                       SET tarif=%s
                       where npa=%s
                       """, (tarif, npa))
        
        connection.commit()
        print("success")
        return redirect(url_for('kelolaDokter'))

    cursor.execute("""
        SELECT dokter.npa as npa, dokter.nama as nama, dokter.spesialisasi as spesialisasi, 
            jadwal_dokter.kuota_pasien as kuota_pasien, dokter.tarif, 
            jadwal_dokter.hari as hari, jadwal_dokter.jam_mulai as jam_mulai, 
            jadwal_dokter.jam_selesai as jam_selesai, 
            jadwal_dokter.id_jadwal as id_jadwal  -- Ensure this field is included
        FROM dokter
        JOIN jadwal_dokter ON dokter.npa = jadwal_dokter.npa
        WHERE id_jadwal = %s
    """, (id_jadwal))
    dokter_data = cursor.fetchone()
    
    cursor.execute("SELECT * FROM dokter")
    list_dokter = cursor.fetchall()
    return render_template("Admin/KelolaDokter/editDokter.html", dokter=dokter_data, list_dokter=list_dokter)

#kelola perwat
@app.route('/Admin/KelolaPerawat')
def kelolaPerawat():
    return render_template("Admin/KelolaPerawat/kelolaPerawat.html")

#edit perawat
@app.route('/Admin/KelolaPerawat/EditPerawat')
def editPerawat():
    return render_template("Admin/KelolaPerawat/editPerawat.html")

#kelola petugas
@app.route('/Admin/KelolaPetugas')
def kelolaPetugas():
    return render_template("Admin/KelolaPetugas/kelolaPetugas.html")

#edit petugas
@app.route('/Admin/KelolaPetugas/EditPetugas')
def editPetugas():
    return render_template("Admin/KelolaPetugas/editPetugas.html")

#kelola pasien
@app.route('/Admin/KelolaPasien')
def kelolaPasien():
    return render_template("Admin/KelolaPasien/kelolaPasien.html")

#edit pasien
@app.route('/Admin/KelolaPasien/EditPasien')
def editPasien():
    return render_template("Admin/KelolaPasien/editPasien.html")

#detail pasien
@app.route('/Admin/KelolaPasien/DetailPasien')
def detailPasien():
    return render_template("Admin/KelolaPasien/detailPasien.html")
    

##################################################################

# DOKTER #########################################################
@app.route('/Dokter')
def homepageDokter():
    return render_template("Dokter/Homepage/index.html")

@app.route('/Dokter/JanjiTemu')
def janjiTemu():
    return render_template("Dokter/JanjiTemu/janjiTemu.html")

@app.route('/Dokter/JanjiTemu/CekPasien')
def cekPasien():
    return render_template("Dokter/CekPasien/cekPasien.html")

@app.route('/Dokter/JanjiTemu/CekPasien/BuatDiagnosa')
def buatDiagnosa():
    return render_template("Dokter/BuatDiagnosa/buatDiagnosa.html")

@app.route('/Dokter/JanjiTemu/CekPasien/RiwayatMedis')
def riwayatMedis():
    return render_template("Dokter/RiwayatMedis/riwayatMedis.html")

####################################################################

# Perawat ##########################################################
@app.route('/Perawat')
def homepagePerawat():
    return render_template("Perawat/index.html")

@app.route('/Perawat/CatatVital')
def catatVital():
    return render_template("Perawat/catatVital.html")

@app.route('/Perawat/UploadDokumen')
def uploadDokumen():
    return render_template("Perawat/uploadDokumen.html")

@app.route('/Perawat/DaftarPasien')
def daftarPasien():
    return render_template("Perawat/daftarPasien.html")
