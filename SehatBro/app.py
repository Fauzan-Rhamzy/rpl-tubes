import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session, flash
from psycopg2.extras import DictCursor
from werkzeug.utils import secure_filename
from flask import flash

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor(cursor_factory=DictCursor)  # Use DictCursor

app.secret_key = 'your_secret_key'
# Konfigurasi folder upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # Lokasi folder upload
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Pastikan folder ada

@app.route('/')
def home():
    return render_template('LandingPage/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required.', 'danger')
            return render_template('LoginPage/index.html')
        try:
            cursor.execute("""
            SELECT 
                u.ID_User, u.Username, u.Passwords, u.Roles, u.Nama,
                p.Nomor_Rekam_Medis, pr.ID_Perawat
            FROM 
                Users u
            LEFT JOIN 
                Pasien p ON u.ID_User = p.ID_User
            LEFT JOIN 
                Perawat pr ON u.ID_User = pr.ID_User
            WHERE 
                u.Username = %s AND u.Passwords = %s
            """, (username, password))
            user = cursor.fetchone()
            print(f"Hasil query login di Flask: {user}")  # Log hasil query
            if user:
                session['user_id'] = user['id_user']
                session['username'] = user['username']
                session['role'] = user['roles']
                session['nama'] = user['nama']

                # Tambahkan id_perawat ke sesi jika role adalah Perawat
                if user['roles'] == 'Perawat' and user['id_perawat']:
                    session['id_perawat'] = user['id_perawat']
                    print(f"ID Perawat dimuat ke sesi: {session['id_perawat']}")
                else:
                    session['id_perawat'] = None

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
    if 'role' in session and session['role'] == 'Pasien':
        return render_template("Pasien/HomepagePasien/index.html")
    flash("Unauthorized access. Please log in.", "danger")
    return redirect(url_for('login'))




@app.route('/jadwaltemu')
def jadwaltemu():
    try:
        # Query untuk janji temu mendatang
        upcoming_query = """
        SELECT d.npa AS Dokter, d.Spesialisasi, bj.Tanggal_Janji, jd.Jam_Mulai, bj.Nomor_Antrian
        FROM Buat_Janji bj
        JOIN Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
        JOIN Dokter d ON jd.NPA = d.NPA
        WHERE bj.Tanggal_Janji >= CURRENT_DATE
        ORDER BY bj.Tanggal_Janji, jd.Jam_Mulai;
        """
        cursor.execute(upcoming_query)
        upcoming_appointments = cursor.fetchall()

        # Query untuk history janji temu
        history_query = """
        SELECT d.npa AS Dokter, d.Spesialisasi, bj.Tanggal_Janji, jd.Jam_Mulai, bj.Nomor_Antrian
        FROM Buat_Janji bj
        JOIN Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
        JOIN Dokter d ON jd.NPA = d.NPA
        WHERE bj.Tanggal_Janji < CURRENT_DATE
        ORDER BY bj.Tanggal_Janji DESC, jd.Jam_Mulai;
        """
        cursor.execute(history_query)
        history_appointments = cursor.fetchall()

        return render_template(
            'jadwaltemu.html',
            upcoming_appointments=upcoming_appointments,
            history_appointments=history_appointments
        )
    except Exception as e:
        print(f"Error in /jadwaltemu route: {e}")
        return "Internal Server Error", 500



@app.route('/Booking')
def booking():
    query = """
        SELECT d.Spesialisasi, d.Nama, 
       STRING_AGG(j.Hari || ' ' || j.Jam_Mulai::TEXT || '-' || j.Jam_Selesai::TEXT, ', ') AS Jadwal
FROM Dokter d
JOIN Jadwal_Dokter j ON d.NPA = j.NPA
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

@app.route('/Booking/Doctor', methods=['GET', 'POST'])
def book_for_doctor():
    id_jadwal = request.args.get('id_jadwal')  # Doctor's schedule ID
    nomor_rekam_medis = session.get('nomor_rekam_medis')  # Assume the user is logged in and their record number is stored in the session

    if not id_jadwal or not nomor_rekam_medis:
        return "Invalid request", 400

    if request.method == 'POST':
        # Get data from the form
        tanggal_janji = request.form.get('tanggal_janji')

        try:
            # Fetch the current queue count
            cursor.execute("""
                SELECT Counts 
                FROM Jadwal_Dokter 
                WHERE ID_Jadwal = %s
            """, (id_jadwal,))
            current_count = cursor.fetchone()[0] or 0

            # Increment the count for the new booking
            new_count = current_count + 1

            # Insert into Buat_Janji
            cursor.execute("""
                INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
                VALUES (%s, %s, %s, %s, %s)
            """, (tanggal_janji, nomor_rekam_medis, id_jadwal, new_count, new_count))

            # Update the count in Jadwal_Dokter
            cursor.execute("""
                UPDATE Jadwal_Dokter 
                SET Counts = %s 
                WHERE ID_Jadwal = %s
            """, (new_count, id_jadwal))
            connection.commit()

            return redirect(url_for('jadwaltemu'))  # Redirect to the user's schedule page
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while booking.", 500

    # Fetch schedule details
    cursor.execute("""
        SELECT Hari, Jam_Mulai, Jam_Selesai
        FROM Jadwal_Dokter
        WHERE ID_Jadwal = %s
    """, (id_jadwal,))
    schedule = cursor.fetchone()

    return render_template("Pasien/Booking/doctor_schedule.html", schedule=schedule, id_jadwal=id_jadwal)



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
    if 'role' in session and session['role'] == 'Admin':
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
    
    flash("Unauthorized access. Please log in as an admin.", "danger")
    return redirect(url_for('login'))

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

    cursor.execute("SELECT * FROM jadwal_detail WHERE id_jadwal = %s", (id_jadwal,))
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
    if 'role' in session and session['role'] == 'Dokter':
        return render_template("Dokter/Homepage/index.html", nama=session.get('nama'))
    flash("Unauthorized access. Please log in.", "danger")
    return redirect(url_for('login'))

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
    if 'role' in session and session['role'] == 'Perawat':
        try:
            # Query total pasien hari ini
            cursor.execute("SELECT COUNT(*) FROM buat_janji WHERE tanggal_janji = CURRENT_DATE")
            total_pasien_hari_ini = cursor.fetchone()[0]

            # Query total pasien bulan ini
            cursor.execute("""
                SELECT COUNT(*) FROM buat_janji 
                WHERE EXTRACT(MONTH FROM tanggal_janji) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM tanggal_janji) = EXTRACT(YEAR FROM CURRENT_DATE)
            """)
            total_pasien_bulan_ini = cursor.fetchone()[0]
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            total_pasien_hari_ini = 0
            total_pasien_bulan_ini = 0  # Default jika query gagal

        return render_template(
            "Perawat/index.html",
            nama=session.get('nama'),
            total_pasien_hari_ini=total_pasien_hari_ini,
            total_pasien_bulan_ini=total_pasien_bulan_ini
        )
    flash("Unauthorized access. Please log in as a nurse.", "danger")
    return redirect(url_for('login'))




@app.route('/Perawat/CatatVital', methods=['GET', 'POST'])
def catatVital():
    if 'role' in session and session['role'] == 'Perawat':
        if request.method == 'POST':
            try:
                # Validasi data dari form
                nomor_rekam_medis = request.form.get('nrm-pasien')
                if not nomor_rekam_medis:
                    flash('Nomor Rekam Medis tidak boleh kosong.', 'danger')
                    return redirect(url_for('catatVital'))
                nomor_rekam_medis = nomor_rekam_medis.strip()

                tekanan_darah = request.form.get('tekanan-darah').strip()
                tinggi_badan = float(request.form.get('tinggi-badan').strip())
                berat_badan = float(request.form.get('berat-badan').strip())
                suhu_badan = float(request.form.get('suhu-tubuh').strip())
                keluhan = request.form.get('keluhan').strip()
                id_perawat = session.get('id_perawat')
                if not id_perawat:
                    flash('ID Perawat tidak ditemukan. Silakan login ulang.', 'danger')
                    return redirect(url_for('login'))
                
                print("Form data received:")
                print(f"Tekanan Darah: {tekanan_darah}")
                print(f"Tinggi Badan: {tinggi_badan}")
                print(f"Berat Badan: {berat_badan}")
                print(f"Suhu Badan: {suhu_badan}")
                print(f"Keluhan: {keluhan}")
                print(f"Nomor Rekam Medis: {nomor_rekam_medis}")
                print(f"ID Perawat: {id_perawat}")

                

                # Query untuk menyimpan data ke tabel Catatan_Vital
                print("Executing query...")
                cursor.execute("""
                    INSERT INTO Catatan_Vital 
                    (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, id_perawat, Nomor_Rekam_Medis)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (tekanan_darah, tinggi_badan, berat_badan, suhu_badan, keluhan, id_perawat, nomor_rekam_medis))
                print("Query executed successfully.")

                connection.commit()  # Simpan perubahan ke database
                flash('Data vital pasien berhasil direkam.', 'success')
            except Exception as e:
                connection.rollback()  # Batalkan perubahan jika terjadi error
                print(f"Database error: {e}")
                flash(f'Terjadi kesalahan: {str(e)}', 'danger')

        return render_template("Perawat/catatVital.html", nama=session.get('nama'))
    flash("Unauthorized access. Please log in as a nurse.", 'danger')
    return redirect(url_for('login'))



@app.route('/Perawat/UploadDokumen', methods=['GET', 'POST'])
def uploadDokumen():
    if 'role' in session and session['role'] == 'Perawat':
        if request.method == 'POST':
            nama_pasien = request.form.get('nama-pasien')
            nomor_rekam_medis = request.form.get('nrm-pasien')
            file = request.files.get('file')
            id_perawat = session.get('id_perawat')

            if not nama_pasien or not nomor_rekam_medis or not file or not id_perawat:
                flash('Semua field harus diisi.', 'danger')
                return redirect(url_for('uploadDokumen'))

            # Validasi file
            if file.filename == '':
                flash('File tidak boleh kosong.', 'danger')
                return redirect(url_for('uploadDokumen'))

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                # Simpan file ke folder uploads
                file.save(filepath)

                # Simpan metadata ke tabel Files_RiwayatMedis
                cursor.execute("""
                    INSERT INTO Files_RiwayatMedis (File_Name, File_Path, id_perawat, nomor_rekam_medis)
                    VALUES (%s, %s, %s, %s)
                """, (filename, filepath, id_perawat, nomor_rekam_medis))
                connection.commit()

                flash('Dokumen berhasil diunggah.', 'success')
            except Exception as e:
                connection.rollback()
                flash(f'Terjadi kesalahan: {str(e)}', 'danger')

        return render_template('Perawat/uploadDokumen.html', nama=session.get('nama'))
    flash('Unauthorized access. Please log in as a nurse.', 'danger')
    return redirect(url_for('login'))


@app.route('/Perawat/DaftarPasien', methods=['GET'])
def daftarPasien():
    if 'role' in session and session['role'] == 'Perawat':
        search_query = request.args.get('query', '').strip()  # Ambil parameter pencarian
        try:
            # Query default (tanpa filter pencarian)
            sql = """
                SELECT
                    bj.Nomor_Rekam_Medis,
                    u_pasien.Nama AS Nama_Pasien,
                    u_dokter.Nama AS Nama_Dokter
                FROM 
                    Buat_Janji bj
                JOIN 
                    Pasien p ON bj.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
                JOIN 
                    Users u_pasien ON p.ID_User = u_pasien.ID_User
                JOIN 
                    Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
                JOIN 
                    Dokter d ON jd.NPA = d.NPA
                JOIN 
                    Users u_dokter ON d.ID_User = u_dokter.ID_User
                WHERE bj.tanggal_janji = CURRENT_DATE
            """
            # Tambahkan filter pencarian jika query diberikan
            if search_query:
                sql += " AND u_pasien.Nama ILIKE %s"
                cursor.execute(sql, (f"%{search_query}%",))
            else:
                cursor.execute(sql)
            
            daftar_pasien = cursor.fetchall()
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            daftar_pasien = []  # Default jika query gagal

        return render_template(
            "Perawat/daftarPasien.html", 
            daftar_pasien=daftar_pasien,
            search_query=search_query
        )
    flash("Unauthorized access. Please log in as a nurse.", 'danger')
    return redirect(url_for('login'))



    
###################################################################
