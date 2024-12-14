import calendar
from datetime import date, timedelta
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, redirect, url_for, json, session, flash
from psycopg2.extras import DictCursor
from werkzeug.utils import secure_filename
import random
import string

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=DictCursor)  # Use DictCursor

app.secret_key = 'your_secret_key'
# Konfigurasi folder upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # Lokasi folder upload
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Pastikan folder ada

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return redirect(url_for('homepage'))
#     return render_template("LoginPage/index.html")

def generate_nomor_rekam_medis():
    while True:
        # Generate nomor rekam medis
        angka = f"{random.randint(0, 999):04}"  # Generate angka 3 digit
        huruf = ''.join(random.choices(string.ascii_uppercase, k=2))  # Generate huruf 2 digit
        nomor_rekam_medis = f"P{angka}{huruf}"

        # Cek di database apakah sudah ada
        cursor.execute("SELECT COUNT(*) FROM Pasien WHERE Nomor_Rekam_Medis = %s", (nomor_rekam_medis,))
        count = cursor.fetchone()['count']

        if count == 0:
            # Jika tidak ada di database, nomor ini valid
            return nomor_rekam_medis
        
from datetime import datetime, timedelta

def calculate_next_date(day):
    today = datetime.today()
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    target_day = days.index(day)
    current_day = today.weekday()

    delta_days = (target_day - current_day) % 7
    if delta_days == 0:  # Jika hari ini hari yang sama, jadwal minggu depan
        delta_days = 7

    return (today + timedelta(days=delta_days)).date()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required.', 'danger')
            return render_template('LoginPage/index.html')
        print(f"Username: {username}, Password: {password}")
        try:
            cursor.execute("""
                SELECT 
                    u.ID_User, u.Username, u.Passwords, u.Roles, u.Nama,
                    p.Nomor_Rekam_Medis, pr.ID_Perawat, pa.id_petugas_admin
                FROM 
                    Users u
                LEFT JOIN   
                    Pasien p ON u.ID_User = p.ID_User
                LEFT JOIN 
                    Perawat pr ON u.ID_User = pr.ID_User
				left join
					petugas_administrasi pa on u.id_user = pa.id_user
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

                # Simpan Nomor Rekam Medis jika role adalah Pasien
                if user['roles'] == 'Pasien' and user['nomor_rekam_medis']:
                    session['nomor_rekam_medis'] = user['nomor_rekam_medis']
                else:
                    session['nomor_rekam_medis'] = None

                # Tambahkan id_perawat ke sesi jika role adalah Perawat
                if user['roles'] == 'Perawat' and user['id_perawat']:
                    session['id_perawat'] = user['id_perawat']
                    print(f"ID Perawat dimuat ke sesi: {session['id_perawat']}")
                else:
                    session['id_perawat'] = None

                if user['roles'] == 'Petugas Admin' and user['id_petugas_admin']:
                    session['id_petugas_admin'] = user['id_petugas_admin']  # Simpan id_petugas_admin ke sesi
                    print(f"ID Petugas Admin: {session['id_petugas_admin']}")  # Debug log
                else:
                    session['id_petugas_admin'] = None



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
                elif user['roles'] == 'Petugas Admin':
                    return redirect(url_for('dashboardTagihan'))
                else:
                    flash('Role is not supported for this login.', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('Invalid username or password.', 'danger')
        except Exception as e:
            connection.rollback()
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('LoginPage/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Debug input form
            print(request.form)  # Lihat semua data yang dikirim dari form

            # Ambil data dari form
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '').strip()
            nama = request.form.get('nama', '').strip()
            gender = request.form.get('gender', '').strip()
            tanggal_lahir = request.form.get('tanggal-lahir', '').strip()
            no_hp = request.form.get('noHP', '').strip()
            alamat = request.form.get('alamat', '').strip()

            # Debug untuk memastikan input tidak None
            print(f"Data yang diterima: {username}, {password}, {nama}, {gender}, {tanggal_lahir}, {no_hp}, {alamat}")

            # Validasi input
            if not (username and password and nama and gender and tanggal_lahir and no_hp and alamat):
                flash("Semua field wajib diisi!", "danger")
                return render_template('LoginPage/register.html')

            # Periksa apakah username sudah ada di database
            cursor.execute("SELECT * FROM Users WHERE Username = %s", (username,))
            if cursor.fetchone():
                flash("Username sudah digunakan. Silakan pilih username lain.", "danger")
                return render_template('LoginPage/register.html')

            # Tambahkan data ke tabel Users
            cursor.execute("""
                INSERT INTO Users (Username, Passwords, Roles, Nama) 
                VALUES (%s, %s, %s, %s) RETURNING ID_User
            """, (username, password, 'Pasien', nama))
            id_user = cursor.fetchone()[0]  # Ambil ID_User yang baru saja dimasukkan

            # Debug untuk memastikan ID_User berhasil di-generate
            print(f"ID_User Baru: {id_user}")

            # Generate Nomor Rekam Medis secara unik
            while True:
                nomor_rekam_medis = generate_nomor_rekam_medis()
                cursor.execute("SELECT * FROM Pasien WHERE Nomor_Rekam_Medis = %s", (nomor_rekam_medis,))
                if not cursor.fetchone():
                    break  # Jika nomor tidak ada di database, gunakan nomor ini

            # Debug untuk memastikan Nomor Rekam Medis benar
            print(f"Nomor Rekam Medis Baru: {nomor_rekam_medis}")

            # Tambahkan data ke tabel Pasien
            cursor.execute("""
                INSERT INTO Pasien (Nomor_Rekam_Medis, ID_User, Alamat, Gender, Tanggal_Lahir, Kontak) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nomor_rekam_medis, id_user, alamat, gender, tanggal_lahir, no_hp))

            # Commit perubahan ke database
            connection.commit()

            flash("Pendaftaran berhasil! Silakan login.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Error: {str(e)}")  # Debug error
            flash(f"Terjadi kesalahan saat mendaftarkan pengguna: {str(e)}", "danger")
            return render_template('LoginPage/register.html')
    else:
        return render_template('LoginPage/register.html')


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
    if 'user_id' not in session or session.get('role') != 'Pasien':
        flash('Anda harus login sebagai pasien untuk melihat jadwal temu.', 'danger')
        return redirect(url_for('login'))

    nomor_rekam_medis = session.get('nomor_rekam_medis')  # Ambil nomor rekam medis dari sesi

    try:
        # Query untuk janji temu mendatang
        upcoming_query = """
        SELECT d.npa AS Dokter, d.Spesialisasi, bj.Tanggal_Janji, jd.Jam_Mulai, jd.Jam_Selesai, bj.Nomor_Antrian
        FROM Buat_Janji bj
        JOIN Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
        JOIN Dokter d ON jd.NPA = d.NPA
        WHERE bj.Tanggal_Janji >= CURRENT_DATE
        AND bj.Nomor_Rekam_Medis = %s
        ORDER BY bj.Tanggal_Janji, jd.Jam_Mulai;
        """
        cursor.execute(upcoming_query, (nomor_rekam_medis,))
        upcoming_appointments = cursor.fetchall()

        # Query untuk history janji temu
        history_query = """
        SELECT d.npa AS Dokter, d.Spesialisasi, bj.Tanggal_Janji, jd.Jam_Mulai, jd.Jam_Selesai, bj.Nomor_Antrian
        FROM Buat_Janji bj
        JOIN Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
        JOIN Dokter d ON jd.NPA = d.NPA
        WHERE bj.Tanggal_Janji < CURRENT_DATE
        AND bj.Nomor_Rekam_Medis = %s
        ORDER BY bj.Tanggal_Janji DESC, jd.Jam_Mulai;
        """
        cursor.execute(history_query, (nomor_rekam_medis,))
        history_appointments = cursor.fetchall()

        return render_template(
            'Pasien/JadwalTemu/index.html',
            upcoming_appointments=upcoming_appointments,
            history_appointments=history_appointments
        )
    except Exception as e:
        print(f"Error in /jadwaltemu route: {e}")
        return "Internal Server Error", 500


@app.route('/booking')
def booking():
    if 'user_id' not in session or session.get('role') != 'Pasien':
        flash('Silakan login sebagai pasien untuk melakukan booking.', 'danger')
        return redirect(url_for('login'))

    try:
        cursor.execute("SELECT DISTINCT spesialisasi FROM dokter")
        specializations = cursor.fetchall()
    except Exception as e:
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return redirect(url_for('homepage'))

    return render_template('Pasien/booking.html', specializations=[s[0] for s in specializations])

@app.route('/booking/<specialization>')
def list_doctors(specialization):
    if 'user_id' not in session:  # Jika tidak login, redirect ke login
        flash('Anda belum login. Silakan login terlebih dahulu.', 'danger')
        print("Redirect ke login: Tidak ada sesi.")
        return redirect(url_for('login'))

    if session.get('role') != 'Pasien':  # Jika role bukan Pasien, redirect ke homepage
        flash('Anda tidak memiliki akses untuk fitur ini.', 'danger')
        print(f"Redirect ke homepage: Role tidak valid ({session.get('role')}).")
        return redirect(url_for('homepage'))

    print(f"Sesi valid untuk user_id: {session['user_id']}, role: {session['role']}")

    try:
        cursor.execute("""
            SELECT d.npa, u.nama, d.spesialisasi 
            FROM dokter d
            JOIN users u ON d.id_user = u.id_user
            WHERE d.spesialisasi = %s
        """, (specialization,))
        doctors = cursor.fetchall()
        print(f"Dokter ditemukan untuk spesialisasi {specialization}: {doctors}")
        if not doctors:
            flash('Tidak ada dokter yang ditemukan untuk spesialisasi ini.', 'danger')
            return redirect(url_for('booking'))
    except Exception as e:
        print(f"Kesalahan saat mengambil daftar dokter: {str(e)}")
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return redirect(url_for('booking'))

    return render_template('Pasien/list_doctors.html', doctors=doctors, specialization=specialization)



@app.route('/booking/schedule/<npa>')
def doctor_schedule(npa):
    # Validasi login
    if 'user_id' not in session:
        flash('Silakan login untuk melihat jadwal.', 'danger')
        return redirect(url_for('login'))

    # Validasi role sebagai pasien
    if session.get('role') != 'Pasien':
        flash('Anda tidak memiliki akses untuk fitur ini.', 'danger')
        return redirect(url_for('homepage'))

    try:
        # Query untuk mengambil jadwal dokter berdasarkan NPA
        cursor.execute("""
            SELECT jd.id_jadwal, jd.hari, jd.jam_mulai, jd.jam_selesai, jd.kuota_pasien
            FROM jadwal_dokter jd
            WHERE jd.npa = %s
        """, (npa,))
        schedules = cursor.fetchall()

        # Konversi tipe data kuota_pasien menjadi integer
        schedules = [
            [row[0], row[1], row[2], row[3], int(row[4])]
            for row in schedules
        ]
        print(f"Jadwal Dokter (setelah konversi): {schedules}")

        # Query untuk mengambil informasi dokter
        cursor.execute("""
            SELECT u.nama, d.spesialisasi
            FROM dokter d
            JOIN users u ON d.id_user = u.id_user
            WHERE d.npa = %s
        """, (npa,))
        doctor = cursor.fetchone()
        print(f"Informasi Dokter: {doctor}")

        if not doctor:
            flash('Dokter tidak ditemukan.', 'danger')
            return redirect(url_for('booking'))

        # Render template dengan data jadwal dan informasi dokter
        return render_template('Pasien/doctor_schedule.html', doctor=doctor, schedules=schedules)

    except Exception as e:
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        print(f"Kesalahan saat mengambil data dokter: {e}")
        return redirect(url_for('booking'))






@app.route('/booking/book', methods=['POST'])
def book_schedule():
    if 'user_id' not in session or session.get('role') != 'Pasien':
        flash('Silakan login sebagai pasien untuk melakukan booking.', 'danger')
        return redirect(url_for('login'))

    id_jadwal = request.form.get('id_jadwal')
    nomor_rekam_medis = session.get('nomor_rekam_medis')  # Ambil dari sesi

    try:
        # Ambil informasi jadwal dokter berdasarkan ID jadwal
        cursor.execute("""
            SELECT jd.hari, jd.npa, jd.kuota_pasien
            FROM jadwal_dokter jd
            WHERE jd.id_jadwal = %s
        """, (id_jadwal,))
        jadwal = cursor.fetchone()
        if not jadwal:
            flash('Jadwal tidak ditemukan.', 'danger')
            return redirect(request.referrer)

        hari_jadwal, npa, kuota_pasien = jadwal['hari'], jadwal['npa'], jadwal['kuota_pasien']

        # Tentukan tanggal janji berdasarkan hari jadwal
        today = date.today()
        days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        day_index_today = today.weekday()
        day_index_jadwal = days_of_week.index(hari_jadwal)

        # Hitung perbedaan hari untuk menentukan tanggal janji
        days_diff = (day_index_jadwal - day_index_today + 7) % 7
        if days_diff == 0:  # Jika hari yang dipilih adalah hari ini, arahkan ke minggu depan
            days_diff = 7
        tanggal_janji = today + timedelta(days=days_diff)

        # Periksa total pasien yang sudah mendaftar pada tanggal yang dipilih
        cursor.execute("""
            SELECT COUNT(*) AS jumlah_pasien
            FROM buat_janji bj
            JOIN jadwal_dokter jd ON bj.id_jadwal = jd.id_jadwal
            WHERE jd.npa = %s AND bj.tanggal_janji = %s
        """, (npa, tanggal_janji))
        jumlah_pasien = cursor.fetchone()['jumlah_pasien']

        if jumlah_pasien >= kuota_pasien:
            flash(f'Kuota penuh pada tanggal {tanggal_janji}. Silakan pilih jadwal lain.', 'danger')
            return redirect(request.referrer)

        # Tambah janji ke tabel buat_janji
        cursor.execute("""
            INSERT INTO buat_janji (tanggal_janji, nomor_rekam_medis, id_jadwal, nomor_antrian)
            VALUES (%s, %s, %s, %s)
        """, (tanggal_janji, nomor_rekam_medis, id_jadwal, jumlah_pasien + 1))
        connection.commit()

        flash(f'Janji berhasil dibuat untuk tanggal {tanggal_janji}.', 'success')
    except Exception as e:
        connection.rollback()
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return redirect(request.referrer)

    return redirect(url_for('booking'))



# @app.route('/Booking', methods=['GET'])
# def booking():
#     try:
#         # Query spesialisasi dokter
#         cursor.execute("SELECT DISTINCT spesialisasi FROM dokter")
#         specializations = [row[0] for row in cursor.fetchall()]

#         # Query dokter dan jadwal
#         cursor.execute("""
#             SELECT 
#                 u.nama AS doctor_name,
#                 d.spesialisasi,
#                 jd.id_jadwal,
#                 jd.hari,
#                 jd.jam_mulai,
#                 jd.jam_selesai
#             FROM dokter d
#             JOIN jadwal_dokter jd ON d.npa = jd.npa
#             JOIN users u ON u.id_user = d.id_user
#         """)
#         raw_data = cursor.fetchall()

#         # Restrukturisasi data
#         doctors_data = {}
#         for row in raw_data:
#             doctor_name, specialization, id_jadwal, day, start_time, end_time = row
#             if specialization not in doctors_data:
#                 doctors_data[specialization] = {}

#             if doctor_name not in doctors_data[specialization]:
#                 doctors_data[specialization][doctor_name] = {
#                     "schedules": []
#                 }

#             doctors_data[specialization][doctor_name]["schedules"].append({
#                 "id_jadwal": id_jadwal,
#                 "day": day,
#                 "start_time": start_time,
#                 "end_time": end_time
#             })

#         # Debugging
#         print("Doctors Data:", doctors_data)

#         return render_template(
#             'Pasien/Booking/index.html', 
#             specializations=specializations, 
#             doctors_data=doctors_data
#         )
#     except Exception as e:
#         flash(f"Terjadi kesalahan: {str(e)}", "danger")
#         return redirect(url_for('homepage'))



# @app.route('/api/confirm_booking', methods=['POST'])
# def confirm_booking():
#     try:
#         data = request.json
#         id_jadwal = data['idJadwal']
#         nomor_rekam_medis = session.get('nomor_rekam_medis')  # Pastikan pasien login

#         if not nomor_rekam_medis:
#             return jsonify({"success": False, "message": "Pasien tidak ditemukan."})

#         # Dapatkan tanggal janji berdasarkan hari jadwal
#         cursor.execute("""
#             SELECT hari FROM jadwal_dokter WHERE id_jadwal = %s
#         """, (id_jadwal,))
#         hari_jadwal = cursor.fetchone()[0]

#         tanggal_janji = calculate_next_date(hari_jadwal)

#         # Hitung nomor antrian berdasarkan jumlah pasien untuk jadwal tertentu
#         cursor.execute("""
#             SELECT COUNT(*) FROM buat_janji WHERE id_jadwal = %s AND tanggal_janji = %s
#         """, (id_jadwal, tanggal_janji))
#         nomor_antrian = cursor.fetchone()[0] + 1

#         # Simpan data ke tabel buat_janji
#         cursor.execute("""
#             INSERT INTO buat_janji (tanggal_janji, nomor_rekam_medis, id_jadwal, nomor_antrian)
#             VALUES (%s, %s, %s, %s)
#         """, (tanggal_janji, nomor_rekam_medis, id_jadwal, nomor_antrian))
#         connection.commit()

#         return jsonify({"success": True, "nomor_antrian": nomor_antrian})
#     except Exception as e:
#         connection.rollback()
#         return jsonify({"success": False, "message": str(e)})

@app.route('/Profile')
def profile():
    return render_template("Pasien/Profile/index.html")

@app.route('/Tagihan')
def tagihan():
    if 'user_id' not in session or session.get('role') != 'Pasien':
        flash("Unauthorized access. Please log in.", "danger")
        return redirect(url_for('login'))

    try:
        user_id = session['user_id']
        
        # Informasi pasien
        cursor.execute("""
            SELECT 
                u.Nama AS nama_pasien, 
                p.Alamat AS alamat
            FROM 
                Users u
            JOIN 
                Pasien p ON u.ID_User = p.ID_User
            WHERE 
                u.ID_User = %s;
        """, (user_id,))
        patient_info = cursor.fetchone()

        # Total tagihan
        cursor.execute("""
            SELECT 
                SUM(d.Tarif) AS total_tagihan
            FROM 
                Buat_Janji bj
            JOIN 
                Dokter d ON bj.ID_Jadwal IN (SELECT ID_Jadwal FROM Jadwal_Dokter WHERE NPA = d.NPA)
            JOIN 
                Pasien p ON bj.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
            WHERE 
                p.ID_User = %s;
        """, (user_id,))
        total_tagihan = cursor.fetchone()['total_tagihan'] or 0

        # Tagihan data
        cursor.execute("""
            SELECT 
                u_dokter.Nama AS nama_dokter,
                bj.Tanggal_Janji AS tanggal_janji,
                d.Tarif AS tarif
            FROM 
                Buat_Janji bj
            JOIN 
                Pasien p ON bj.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
            JOIN 
                Dokter d ON bj.ID_Jadwal IN (SELECT ID_Jadwal FROM Jadwal_Dokter WHERE NPA = d.NPA)
            JOIN 
                Users u_dokter ON d.ID_User = u_dokter.ID_User
            WHERE 
                p.ID_User = %s;
        """, (user_id,))
        tagihan_data = cursor.fetchall()

        return render_template(
            "Pasien/Tagihan/index.html",
            patient_info=patient_info,
            total_tagihan=total_tagihan,
            tagihan_data=tagihan_data
        )
    except Exception as e:
        print(f"Error fetching tagihan: {e}")
        return "Internal Server Error", 500


###########################################################

# ADMIN ##################################################
@app.route('/Admin')
def homepageAdmin():
    if 'role' in session and session['role'] == 'Admin':
        return render_template("Admin/Homepage/homepage.html", nama=session.get('nama'))
    flash("Unauthorized access. Please log in as an admin.", "danger")
    return redirect(url_for('login'))


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
@app.route('/Perawat')
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
@app.route('/PetugasAdmin')
def dashboardTagihan():
    if 'role' in session and session['role'] == 'Petugas Admin':
        nama = session.get('nama')  # Ambil nama dari sesi
        return render_template('Petugas/dashboardTagihan.html', nama=nama)
    flash('Unauthorized access. Please log in as a Petugas Admin.', 'danger')
    return redirect(url_for('login'))


@app.route('/PetugasAdmin/pendaftaranPasien', methods=['GET', 'POST'])
def pendaftaranPasien():
    if request.method == 'POST':
        try:
            # Ambil data dari form
            nama = request.form['nama'].strip()
            jenis_kelamin = request.form['jenis_kelamin']
            tanggal_lahir = request.form['tanggal_lahir']
            kontak = request.form['kontak'].strip()
            username = request.form['username'].strip()
            password = request.form['password'].strip()
            alamat = request.form['alamat'].strip()
            
            # Generate Nomor Rekam Medis yang unik
            nomor_rekam_medis = generate_nomor_rekam_medis()
            print(nomor_rekam_medis)
            
            # Insert ke tabel Users
            cursor.execute("""
                INSERT INTO Users (Username, Passwords, Roles, Nama)
                VALUES (%s, %s, 'Pasien', %s) RETURNING ID_User
            """, (username, password, nama))
            id_user = cursor.fetchone()['id_user']
            
            # Insert ke tabel Pasien
            cursor.execute("""
                INSERT INTO Pasien (Nomor_Rekam_Medis, ID_User, Alamat, Gender, Tanggal_Lahir, Kontak)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nomor_rekam_medis, id_user, alamat, jenis_kelamin, tanggal_lahir, kontak))
            
            # Commit perubahan
            connection.commit()
            flash(f"Pasien {nama} berhasil didaftarkan dengan Nomor Rekam Medis: {nomor_rekam_medis}", 'success')
            return redirect(url_for('pendaftaran_pasien'))
        except Exception as e:
            # Rollback jika terjadi error
            connection.rollback()
            flash(f"Terjadi kesalahan: {str(e)}", 'danger')
    
    return render_template("Petugas/pendaftaranPasien.html")


# @app.route('/PetugasAdmin/pendaftaranPasien')
# def pendaftaranPasien():
#     return render_template("Petugas/pendaftaranPasien.html")

@app.route('/PetugasAdmin/Invoice', methods=['GET'])
def invoice():
    if 'role' in session and session['role'] == 'Petugas Admin':
        search_query = request.args.get('search', '').strip()
        try:
            if search_query:
                # Query untuk mencari tagihan berdasarkan nama pasien
                cursor.execute("""
                    SELECT 
                        t.nomor_rekam_medis, 
                        u.nama, 
                        t.jumlah_pembayaran,
                        t.status_pembayaran
                    FROM 
                        transaksi t
                    INNER JOIN 
                        pasien p ON t.nomor_rekam_medis = p.nomor_rekam_medis
                    INNER JOIN 
                        users u ON p.id_user = u.id_user
                    WHERE 
                        u.nama ILIKE %s
                        AND t.tanggal_transaksi = CURRENT_DATE
                """, (f"%{search_query}%",))
            else:
                # Query default untuk daftar tagihan hari ini
                cursor.execute("""
                    SELECT 
                        t.nomor_rekam_medis, 
                        u.nama, 
                        t.jumlah_pembayaran,
                        t.status_pembayaran
                    FROM 
                        transaksi t
                    INNER JOIN 
                        pasien p ON t.nomor_rekam_medis = p.nomor_rekam_medis
                    INNER JOIN 
                        users u ON p.id_user = u.id_user
                    WHERE 
                        t.tanggal_transaksi = CURRENT_DATE
                """)
            invoices = cursor.fetchall()

            return render_template(
                'Petugas/Invoice.html', 
                invoices=invoices, 
                search_query=search_query
            )
        except Exception as e:
            flash(f"Terjadi kesalahan saat mengambil data tagihan: {str(e)}", 'danger')
            return redirect(url_for('dashboardTagihan'))
    else:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('login'))


@app.route('/PetugasAdmin/Invoice/MarkAsPaid', methods=['POST'])
def mark_as_paid():
    if 'role' in session and session['role'] == 'Petugas Admin':
        try:
            # Ambil id_transaksi dari form
            id_transaksi = request.form.get('id_transaksi')
            
            if not id_transaksi:
                flash("ID Transaksi tidak ditemukan.", "danger")
                return redirect(url_for('invoice'))

            # Update status pembayaran menjadi "Lunas"
            cursor.execute("""
                UPDATE transaksi
                SET status_pembayaran = 'Lunas'
                WHERE id_transaksi = %s
            """, (id_transaksi,))
            connection.commit()

            flash("Status pembayaran berhasil diperbarui menjadi Lunas.", "success")
            return redirect(url_for('invoice'))
        except Exception as e:
            connection.rollback()
            flash(f"Terjadi kesalahan saat memperbarui status pembayaran: {str(e)}", "danger")
            return redirect(url_for('invoice'))
    else:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('login'))


@app.route('/PetugasAdmin/Invoice/Detail', methods=['POST'])
def detail_invoice():
    if 'role' in session and session['role'] == 'Petugas Admin':
        try:
            nomor_rekam_medis = request.form.get('nomor_rekam_medis')
            if not nomor_rekam_medis:
                flash("Nomor Rekam Medis tidak ditemukan.", "danger")
                return redirect(url_for('invoice'))

            # Query detail invoice
            cursor.execute("""
                SELECT 
                    t.id_transaksi, 
                    p.nomor_rekam_medis, 
                    u_pasien.nama AS nama_pasien, 
                    t.tanggal_transaksi, 
                    t.jumlah_pembayaran, 
                    t.status_pembayaran,
                    p.kontak
                FROM 
                    transaksi t
                INNER JOIN 
                    pasien p ON t.nomor_rekam_medis = p.nomor_rekam_medis
                INNER JOIN 
                    users u_pasien ON u_pasien.id_user = p.id_user
                WHERE 
                    t.nomor_rekam_medis = %s and t.tanggal_transaksi = CURRENT_DATE
                ORDER BY 
                    t.tanggal_transaksi DESC
                LIMIT 1
            """, (nomor_rekam_medis,))
            invoice_detail = cursor.fetchone()

            if not invoice_detail:
                flash("Detail tagihan tidak ditemukan.", "danger")
                return redirect(url_for('invoice'))

            # Query untuk mendapatkan layanan terkait
            cursor.execute("""
                SELECT 
                    u_dokter.nama AS nama_dokter, 
                    d.spesialisasi, 
                    d.tarif
                FROM 
                    buat_janji bj
                INNER JOIN 
                    jadwal_dokter jd ON bj.id_jadwal = jd.id_jadwal
                INNER JOIN 
                    dokter d ON jd.npa = d.npa
                INNER JOIN 
                    users u_dokter ON d.id_user = u_dokter.id_user
                WHERE 
                    bj.nomor_rekam_medis = %s and bj.tanggal_janji = CURRENT_DATE
                ORDER BY 
                    bj.tanggal_janji DESC
            """, (nomor_rekam_medis,))
            services = cursor.fetchall()

            total_payment = sum(service[2] for service in services)

            return render_template(
                'Petugas/detail_invoice.html',
                patient_info=invoice_detail[1:7],
                services=services,
                total_payment=total_payment,
                transaction_id=invoice_detail[0]

                
            )
        except Exception as e:
            flash(f"Terjadi kesalahan saat mengambil detail invoice: {str(e)}", "danger")
            return redirect(url_for('invoice'))
    else:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('login'))




@app.route('/PetugasAdmin/Invoice/BuatInvoice', methods=['GET'])
def buat_invoice():
    if 'role' in session and session['role'] == 'Petugas Admin':
        try:
            # Query untuk mendapatkan daftar dokter
            cursor.execute("""
                SELECT u_dokter.nama, d.tarif 
                FROM dokter d
                INNER JOIN users u_dokter ON u_dokter.id_user = d.id_user
            """)
            doctors = cursor.fetchall()  # [(NamaDokter1, Tarif1), (NamaDokter2, Tarif2), ...]

            return render_template("Petugas/buat_invoice.html", doctors=doctors)
        except Exception as e:
            flash(f"Terjadi kesalahan saat memuat data dokter: {str(e)}", 'danger')
            return redirect(url_for('invoice'))
    else:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('login'))

@app.route('/PetugasAdmin/Invoice/BuatInvoice', methods=['POST'])
def buat_invoice_submit():
    if 'role' in session and session['role'] == 'Petugas Admin':
        try:
            # Ambil data dari form
            nama_pasien = request.form.get('nama_pasien').strip()
            tanggal_transaksi = request.form.get('tanggal_transaksi').strip()
            selected_doctors = request.form.getlist('selected_doctors')  # Daftar tarif dokter yang dipilih
            id_petugas_admin = session.get('id_petugas_admin')

            # Hitung total tarif
            total_tarif = sum([float(tarif) for tarif in selected_doctors])

            print(f"Selected Doctors: {selected_doctors}")  # Daftar tarif dokter
            print(f"Total Tarif: {total_tarif}")  # Total tarif yang dihitung


            # Validasi data
            if not (nama_pasien and tanggal_transaksi and selected_doctors):
                flash("Semua field wajib diisi!", "danger")
                return redirect(url_for('buat_invoice'))

            # Dapatkan nomor rekam medis berdasarkan nama pasien
            cursor.execute("""
                SELECT nomor_rekam_medis 
                FROM pasien p
                INNER JOIN users u ON p.id_user = u.id_user
                WHERE u.nama = %s
            """, (nama_pasien,))
            result = cursor.fetchone()
            print(result)

            if not result:
                flash("Nama pasien tidak valid.", "danger")
                return redirect(url_for('buat_invoice'))

            nomor_rekam_medis = result[0]
            print(nomor_rekam_medis)

            print(f"Nama Pasien: {nama_pasien}")
            print(f"Nomor Rekam Medis: {nomor_rekam_medis}")
            print(f"Tanggal Transaksi: {tanggal_transaksi}")
            print(f"Total Tarif: {total_tarif}")
            print(f"ID Petugas Admin: {id_petugas_admin}")


            # Insert data ke tabel transaksi
            cursor.execute("""
                INSERT INTO transaksi (status_pembayaran, tanggal_transaksi, jumlah_pembayaran, nomor_rekam_medis, id_petugas_admin)
                VALUES (%s, %s, %s, %s, %s)
            """, ("Belum Lunas", tanggal_transaksi, total_tarif, nomor_rekam_medis, id_petugas_admin))
            connection.commit()

            flash("Invoice berhasil dibuat!", "success")
            return redirect(url_for('invoice'))
        except Exception as e:
            print(f"Error saat INSERT INTO transaksi: {str(e)}")  # Debug log kesalahan
            connection.rollback()
            flash(f"Terjadi kesalahan saat membuat invoice: {str(e)}", "danger")
            return redirect(url_for('buat_invoice'))
    else:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('login'))