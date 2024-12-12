import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session
from psycopg2.extras import DictCursor
from flask import flash

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor(cursor_factory=DictCursor)  # Use DictCursor

app.secret_key = 'your_secret_key'

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return redirect(url_for('homepage'))
#     return render_template("LoginPage/index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required.', 'danger')
            return render_template('LoginPage/index.html')

        try:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND passwords = %s",
                (username, password)
            )
            user = cursor.fetchone()

            if user:
                session['user_id'] = user['id_user']
                session['username'] = user['username']
                session['role'] = user['roles']
                session['nama'] = user['nama']
                flash(f"Welcome, {user['nama']}!", 'success')

                # Redirect berdasarkan role
                if user['roles'] == 'Pasien':
                    return redirect(url_for('homepage'))
                elif user['roles'] == 'Dokter':
                    return redirect(url_for('homepageDokter'))
                elif user['roles'] == 'Admin':
                    return redirect(url_for('homepageAdmin'))
                elif user['roles'] == 'Perawat':
                    return redirect(url_for('homepagePerawat'))
                else:
                    flash('Role is not supported for this login.', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('Invalid username or password.', 'danger')
        except Exception as e:
            connection.rollback()
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('LoginPage/index.html')


@app.route('/logout')
def logout():
    session.clear()  # Hapus semua data dari session
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

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

    return render_template("Booking/index.html", doctors_data=doctors_data)
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
    cursor.execute("""
        SELECT COUNT (*)
        FROM pasien
    """)
    banyakPasien = cursor.fetchone()[0]

    cursor.execute("""
        SELECT SUM (jumlah_pembayaran)
        FROM Transaksi 
        WHERE Status_Pembayaran='Lunas'
    """)
    pembayaran=cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT (*)
        FROM USERS
        WHERE Roles <> 'Pasien'
    """)
    pekerja = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT (*)
        FROM BUAT_JANJI
    """)
    jadwal=cursor.fetchone()[0]

    # cursor.execute("select * from buat_janji join transaksi on buat_janji.nomor_rekam_medis=transaksi.nomor_rekam_medis")
    # aktivitas=cursor.fetchall()
    return render_template("Admin/Homepage/homepage.html", 
                           banyakPasien=banyakPasien, 
                           pembayaran=pembayaran,
                           pekerja=pekerja,
                           jadwal=jadwal,
                           user=session)

#kelola dokter
@app.route('/Admin/KelolaDokter', methods=['GET', 'POST'])
def kelolaDokter():
    if request.method == 'POST':
        # form_type = request.form('form_type')

        # if form_type == 'doctor':
        nama= request.form['doctor-name']
        username= request.form['doctor-username']
        password= request.form['doctor-password']
        role = 'Dokter'

        cursor.execute("""
            INSERT INTO Users (Username, Passwords, Roles, Nama)
            Values (%s, %s, %s, %s) RETURNING ID_USER
        """, (username, password, role, nama))
        user_id = cursor.fetchone()[0]
        connection.commit()

        npa = request.form['doctor-npa']
        spesialisasi= request.form['doctor-specialty']
        kuota= request.form['doctor-quota']
        tarif= request.form['doctor-fee']

        cursor.execute("INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User) VALUES (%s, %s, %s, %s)", (npa, spesialisasi, tarif, user_id,))
        connection.commit()

            # flash("Doctor added successfully!", "success")

        # elif form_type == 'schedule':
            # 
        print("add")

        return redirect(url_for('kelolaDokter'))

    cursor.execute("""
        select * from dokter 
        left outer join jadwal_dokter on dokter.npa = jadwal_dokter.npa 
        JOIN Users on Users.id_user = dokter.id_user
        ORDER BY jadwal_dokter.hari DESC  
    """)

    jadwal_dokter = cursor.fetchall()
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
        """, (npa, kuota, hari, mulai, akhir, id_jadwal,))
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
        SELECT *
        FROM jadwal_detail
        WHERE id_jadwal = %s
    """, (id_jadwal))
    dokter_data = cursor.fetchone()
    
    cursor.execute("SELECT * FROM dokter_detail")
    list_dokter = cursor.fetchall()
    return render_template("Admin/KelolaDokter/editDokter.html", dokter=dokter_data, list_dokter=list_dokter)

#kelola perwat
@app.route('/Admin/KelolaPerawat', methods=['GET', 'POST'])
def kelolaPerawat():
    if request.method == 'POST':
        username = request.form['nurse-username']
        password = request.form['nurse-password']
        role = 'Perawat'
        nama = request.form['nurse-name']

        cursor.execute("""
            INSERT INTO Users (username, passwords, roles, nama)
            VALUES (%s, %s, %s, %s) RETURNING ID_USER
        """, (username, password, role, nama,))
        user_id = cursor.fetchone()[0]
        connection.commit()
        print(user_id)
        cursor.execute("INSERT INTO Perawat (id_user) VALUES (%s)", (user_id,))
        connection.commit()

        # cursor.execute("""
        #     INSERT INTO Perawat ( ID_User)
        #     SELECT u.ID_User
        #     FROM Users u
        #     WHERE u.Roles = 'Perawat';
        # """)
        # connection.commit()
        return redirect(url_for('kelolaPerawat'))  

    cursor.execute("""
        SELECT *
        FROM Perawat_detail
    """)
    perawat=cursor.fetchall()

    return render_template("Admin/KelolaPerawat/kelolaPerawat.html", perawat=perawat)

#edit perawat
@app.route('/Admin/KelolaPerawat/EditPerawat', methods=['GET', 'POST'])
def editPerawat():
    id_user = request.args.get('id_user')

    if not id_user:
        return "No ID Perawat", 400

    if request.method == 'POST':
        nama = request.form['nurse-name']
        username = request.form['nurse-username']
        password = request.form['nurse-password']
        cursor.execute("""
            UPDATE Users SET nama=%s, username=%s, passwords=%s WHERE id_user=%s
        """, (nama, username, password, id_user,))

        return redirect(url_for(kelolaPerawat))

    cursor.execute("""
        SELECT *
        FROM perawat_detail
        WHERE id_user = %s
    """, (id_user,))
    perawat = cursor.fetchone()

    return render_template("Admin/KelolaPerawat/editPerawat.html", perawat=perawat)

#kelola petugas
@app.route('/Admin/KelolaPetugas', methods=['GET', 'POST'])
def kelolaPetugas():
    if request.method == 'POST':
        nama = request.form['admin-name']
        username = request.form['admin-username']
        password = request.form['admin-password']
        role = "Petugas Admin"

        cursor.execute("""
            INSERT INTO Users (username, passwords, roles, nama)
            VALUES (%s, %s, %s, %s) RETURNING ID_USER
        """, (username, password, role, nama,))
        user_id = cursor.fetchone()[0]
        connection.commit()
        
        cursor.execute("INSERT INTO Petugas_Administrasi (id_user) VALUES (%s)", (user_id,))
        connection.commit()

    cursor.execute("SELECT * FROM Petugas_Detail")
    petugas=cursor.fetchall()
    return render_template("Admin/KelolaPetugas/kelolaPetugas.html", petugas=petugas)

#edit petugas
@app.route('/Admin/KelolaPetugas/EditPetugas', methods=['GET', 'POST'])
def editPetugas():
    id_user = request.args.get('id_user')

    if not id_user:
        return "No ID Petugas Admin", 400

    if request.method == 'POST':
        nama = request.form['admin-name']
        username = request.form['admin-username']
        password = request.form['admin-password']
        cursor.execute("""
            UPDATE Users SET nama=%s, username=%s, passwords=%s WHERE id_user=%s
        """, (nama, username, password, id_user,))

        return redirect(url_for('kelolaPetugas'))

    cursor.execute("""
        SELECT *
        FROM petugas_detail
        WHERE id_user = %s
    """, (id_user,))
    petugas = cursor.fetchone()

    return render_template("Admin/KelolaPetugas/editPetugas.html", petugas=petugas)

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
@app.route('/Perawat', methods=['GET', 'POST'])
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
    
###################################################################
