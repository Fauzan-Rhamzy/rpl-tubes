import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session
from psycopg2.extras import DictCursor
from werkzeug.utils import secure_filename
import random
import string
from flask import flash
from flask import send_from_directory

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor(cursor_factory=DictCursor)  # Use DictCursor

app.secret_key = 'your_secret_key'
# Konfigurasi folder upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # Lokasi folder upload
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Pastikan folder ada

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

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# homepage umum
@app.route('/')
def home():
    return render_template('LandingPage/index.html')

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ambil input username dan pass
        username = request.form.get('username')
        password = request.form.get('password')

        # cek jika username dan pass tidak diisi
        if not username or not password:
            # mengembalikan pesan eror
            flash('Username and password are required.', 'danger')
            return render_template('LoginPage/index.html')

        # mengecek ke database jika pengguna terdaftar
        try:
            cursor.execute("""
            SELECT 
                *
            FROM 
                Users u
            LEFT JOIN 
                Pasien p ON u.ID_User = p.ID_User
            LEFT JOIN 
                Perawat pr ON u.ID_User = pr.ID_User
            LEFT JOIN
                Dokter d ON u.ID_User = d.ID_User
            LEFT JOIN
                Admins a ON u.ID_User = a.ID_User
            LEFT JOIN
                petugas_administrasi pa ON u.ID_User = pa.ID_User
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
                # if user['roles'] == 'Perawat' and user['id_perawat']:
                #     session['id_perawat'] = user['id_perawat']
                #     print(f"ID Perawat dimuat ke sesi: {session['id_perawat']}")
                # else:
                #     session['id_perawat'] = None

                #     flash(f"Welcome, {user['nama']}!", 'success')

                # Redirect berdasarkan role
                if user['roles'] == 'Pasien' and user['nomor_rekam_medis']:
                    session['nomor_rekam_medis'] = user['nomor_rekam_medis']
                    return redirect(url_for('homepage'))
                
                elif user['roles'] == 'Dokter' and user['npa']:
                    session['npa'] = user['npa']
                    session['spesialisasi'] = user['spesialisasi']
                    return redirect(url_for('homepageDokter'))
                
                elif user['roles'] == 'Admin' and user['id_admin']:
                    session['id_admin'] = user['id_admin']
                    return redirect(url_for('homepageAdmin'))
                
                elif user['roles'] == 'Perawat' and user['id_perawat']:
                    session['id_perawat'] = user['id_perawat']
                    return redirect(url_for('homepagePerawat'))

                else:
                    flash('Role is not supported for this login.', 'danger')
                    return redirect(url_for('login'))

            # jika user tidak terdaftar di database mengembalikan pesan eror
            else:
                flash('Invalid username or password.', 'danger')
        except Exception as e:
            connection.rollback()
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('LoginPage/index.html')

# routing logout
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




@app.route('/jadwaltemu', methods=['GET'])
def jadwaltemu():
    if 'role' in session and session['role'] == 'Pasien':
        nomor_rekam_medis = session.get('nomor_rekam_medis')
        print(nomor_rekam_medis)

        try:
            # Query untuk jadwal mendatang
            jadwal_mendatang = cursor.execute("""
                SELECT 
                    u_dokter.nama AS NamaDokter, 
                    d.Spesialisasi, 
                    bj.Tanggal_Janji, 
                    jd.Jam_Mulai, 
                    jd.Jam_Selesai, 
                    bj.Nomor_Antrian
                FROM 
                    Buat_Janji bj
                JOIN 
                    Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
                JOIN 
                    Dokter d ON jd.NPA = d.NPA
                JOIN 
                    Users u_dokter ON d.ID_User = u_dokter.ID_User
                WHERE 
                    bj.Tanggal_Janji >= CURRENT_DATE 
                    AND bj.Nomor_Rekam_Medis = %s
                ORDER BY 
                    bj.Tanggal_Janji, jd.Jam_Mulai;
            """, (nomor_rekam_medis,))
            jadwal_mendatang = cursor.fetchall()

            # Query untuk history jadwal
            jadwal_history = cursor.execute("""
                SELECT 
                    u_dokter.nama AS NamaDokter, 
                    d.Spesialisasi, 
                    bj.Tanggal_Janji, 
                    jd.Jam_Mulai, 
                    jd.Jam_Selesai, 
                    bj.Nomor_Antrian
                FROM 
                    Buat_Janji bj
                JOIN 
                    Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
                JOIN 
                    Dokter d ON jd.NPA = d.NPA
                JOIN 
                    Users u_dokter ON d.ID_User = u_dokter.ID_User
                WHERE 
                    bj.Tanggal_Janji < CURRENT_DATE 
                    AND bj.Nomor_Rekam_Medis = %s
                ORDER BY 
                    bj.Tanggal_Janji DESC, jd.Jam_Mulai;
            """, (nomor_rekam_medis,))
            jadwal_history = cursor.fetchall()

            return render_template(
                'Pasien/JadwalTemu/index.html', 
                jadwal_mendatang=jadwal_mendatang, 
                jadwal_history=jadwal_history, 
                nama=session.get('nama')
            )
        except Exception as e:
            flash(f"Terjadi kesalahan: {str(e)}", 'danger')
            return redirect(url_for('homepage'))

    flash('Unauthorized access. Please log in as a patient.', 'danger')
    return redirect(url_for('login'))




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
        try:
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

        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            banyakPasien = 0
            pembayaran = 0
            pekerja = 0
            jadwal = 0

        try:
            cursor.execute("""
                select p.nomor_rekam_medis as id_pasien, u.nama as nama, t.tanggal_transaksi as tanggal_kunjungan, t.status_pembayaran as status_pembayaran
                from transaksi t 
                left join pasien p on t.nomor_rekam_medis=p.nomor_rekam_medis
                left join users u on u.id_user=p.id_user
                order by t.tanggal_transaksi desc
            """)
            aktivitas=cursor.fetchall()
        except Exception as e:
            flash(f"An error occurred while retrieving activities: {str(e)}", 'danger')
            aktivitas=[]

        return render_template("Admin/Homepage/homepage.html", 
                           banyakPasien=banyakPasien, 
                           pembayaran=pembayaran,
                           pekerja=pekerja,
                           jadwal=jadwal,
                           user=session,
                           list=aktivitas)
    
    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#kelola dokter
@app.route('/Admin/KelolaDokter', methods=['GET', 'POST'])
def kelolaDokter():
    if 'role' in session and session['role'] == 'Admin':

        if request.method == 'POST':
            form_type = request.form.get('form_type')

            if not form_type:
                flash('Form type is missing. Gagal menambahkan data.', 'danger')
                return redirect(url_for('kelolaDokter'))  # Redirect if form type is not present

            try:
                if form_type == 'doctor':
                    nama= request.form['doctor-name']
                    username= request.form['doctor-username']
                    password= request.form['doctor-password']
                    role = 'Dokter'

                    # Check if the username already exists
                    cursor.execute("""
                        SELECT id_user FROM users WHERE username = %s
                    """, (username,))
                    existing_user = cursor.fetchone()

                    if existing_user:
                        flash('Username is already taken. Please choose another one.', 'danger')
                        return redirect(url_for('kelolaDokter'))

                    cursor.execute("""
                        INSERT INTO Users (Username, Passwords, Roles, Nama)
                        Values (%s, %s, %s, %s) RETURNING ID_USER
                    """, (username, password, role, nama))
                    user_id = cursor.fetchone()[0]
                    connection.commit()

                    npa = request.form['doctor-npa']
                    spesialisasi= request.form['doctor-specialty']
                    tarif= request.form['doctor-fee']

                    cursor.execute("INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User) VALUES (%s, %s, %s, %s)", (npa, spesialisasi, tarif, user_id,))
                    connection.commit()
                    flash("Berhasil menambahkan dokter baru!", "success")

                elif form_type == 'schedule':
                    npa = request.form['doctor-select']
                    hari = request.form['schedule-day']
                    jam_mulai = request.form['schedule-time-start']
                    jam_akhir = request.form['schedule-time-end']
                    kuota = request.form['doctor-quota']

                    cursor.execute("""
                        INSERT INTO jadwal_dokter
                        (kuota_pasien, hari, jam_mulai, jam_selesai, npa)
                        VALUES
                        (%s, %s, %s, %s, %s)
                    """, (kuota, hari, jam_mulai, jam_akhir, npa,))
                    connection.commit()
                    flash("Berhasil menambahkan jadwal dokter!", "success")

                else:
                    flash('Unknown form type.', 'danger')

            except Exception as e:
                # In case of an error during any operation
                connection.rollback()
                flash(f"An error occurred: {str(e)}", 'danger')

            return redirect(url_for('kelolaDokter'))

        try:
            cursor.execute("""
                select * from jadwal_dokter jd 
                left join dokter d on d.npa = jd.npa 
                JOIN Users u on u.id_user = d.id_user
                ORDER BY jd.hari DESC  
            """)
            jadwal_dokter = cursor.fetchall()

            cursor.execute("""
                select d.npa as npa, u.nama as nama, d.spesialisasi as spesialisasi, d.tarif, u.username, u.passwords as passwords
                from dokter d left join users u on d.id_user=u.id_user
                order by spesialisasi
            """)
            list_dokter=cursor.fetchall()

        except Exception as e:
            flash(f"An error occurred while retrieving data: {str(e)}", 'danger')
            jadwal_dokter = []
            list_dokter = []

        return render_template("Admin/KelolaDokter/kelolaDokter.html", jadwal_dokter = jadwal_dokter, list_dokter=list_dokter)

    flash("Unauthorized access. Tolong login sebagai admin.", 'danger')
    return redirect(url_for('login'))

#edit dokter
@app.route('/Admin/KelolaDokter/EditDokter', methods=['GET', 'POST'])
def editDokter():
    if 'role' in session and session['role'] == 'Admin':
        id_jadwal = request.args.get('id_jadwal')

        if not id_jadwal:
            flash("No ID Jadwal provided", 'danger')
            return redirect(url_for('kelolaDokter'))

        if request.method == 'POST':
            npa = request.form['doctor-npa']
            kuota = request.form['doctor-quota']
            hari = request.form['doctor-day']
            mulai = request.form['schedule-time-start']
            akhir = request.form['schedule-time-end']
            tarif = request.form['doctor-fee']

            if not npa or not kuota or not hari or not mulai or not akhir or not tarif:
                flash('Please complete all fields before submitting.', 'danger')
                return redirect(url_for('editDokter', id_jadwal=id_jadwal))

            try:
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

            except Exception as e:
                connection.rollback()
                flash(f"An error occurred: {str(e)}", 'danger')

        try:
            cursor.execute("SELECT * FROM jadwal_detail WHERE id_jadwal = %s", (id_jadwal,))
            dokter_data = cursor.fetchone()
            
            cursor.execute("SELECT * FROM dokter_detail")
            list_dokter = cursor.fetchall()

        except Exception as e:
            flash(f"Error retrieving data: {str(e)}", 'danger')
            dokter_data = None
            list_dokter = []

        return render_template("Admin/KelolaDokter/editDokter.html", dokter=dokter_data, list_dokter=list_dokter)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#kelola perwat
@app.route('/Admin/KelolaPerawat', methods=['GET', 'POST'])
def kelolaPerawat():
    if 'role' in session and session['role'] == 'Admin':

        if request.method == 'POST':
            username = request.form['nurse-username']
            password = request.form['nurse-password']
            role = 'Perawat'
            nama = request.form['nurse-name']
            
            # Check if the username already exists
            cursor.execute("""
                SELECT id_user FROM users WHERE username = %s
            """, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username is already taken. Please choose another one.', 'danger')
                return redirect(url_for('kelolaPerawat'))

            cursor.execute("""
                INSERT INTO Users (username, passwords, roles, nama)
                VALUES (%s, %s, %s, %s) RETURNING ID_USER
            """, (username, password, role, nama,))
            user_id = cursor.fetchone()[0]
            connection.commit()
            
            cursor.execute("INSERT INTO Perawat (id_user) VALUES (%s)", (user_id,))
            connection.commit()
            flash("Berhasil menambahkan perawat!", "success")

            return redirect(url_for('kelolaPerawat'))  

        cursor.execute("""
            SELECT *
            FROM Perawat_detail
        """)
        perawat=cursor.fetchall()

        return render_template("Admin/KelolaPerawat/kelolaPerawat.html", perawat=perawat)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#edit perawat
@app.route('/Admin/KelolaPerawat/EditPerawat', methods=['GET', 'POST'])
def editPerawat():
    if 'role' in session and session['role'] == 'Admin':
        id_user = request.args.get('id_user')

        if not id_user:
            flash("No ID Perawat provided", "danger")
            return redirect(url_for('kelolaPerawat'))

        if request.method == 'POST':
            nama = request.form['nurse-name']
            username = request.form['nurse-username']
            password = request.form['nurse-password']

            # Validate required fields
            if not nama or not username or not password:
                flash('All fields must be filled out.', 'danger')
                return redirect(url_for('editPerawat', id_user=id_user))

            # Check if the username already exists (excluding the current user)
            cursor.execute("""
                SELECT id_user FROM users WHERE username = %s AND id_user != %s
            """, (username, id_user))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username is already taken. Please choose another one.', 'danger')
                return redirect(url_for('editPasien', id_user=id_user))

            try:
                cursor.execute("""
                    UPDATE Users SET nama=%s, username=%s, passwords=%s WHERE id_user=%s
                """, (nama, username, password, id_user,))
                connection.commit()

                flash("Berhasil mengganti data perawat!", "success")
                return redirect(url_for('kelolaPerawat'))
            except Exception as e:
                connection.rollback()
                flash(f"An error occurred: {str(e)}", 'danger')

        try:
            cursor.execute("""
                SELECT *
                FROM perawat_detail
                WHERE id_user = %s
            """, (id_user,))
            perawat = cursor.fetchone()

            if not perawat:
                flash("Perawat not found", "danger")
                return redirect(url_for('kelolaPerawat'))
        except Exception as e:
            flash(f"Error fetching data: {str(e)}", 'danger')
            perawat = None

        return render_template("Admin/KelolaPerawat/editPerawat.html", perawat=perawat)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#kelola petugas
@app.route('/Admin/KelolaPetugas', methods=['GET', 'POST'])
def kelolaPetugas():
    if 'role' in session and session['role'] == 'Admin':
        if request.method == 'POST':
            nama = request.form['admin-name']
            username = request.form['admin-username']
            password = request.form['admin-password']
            role = "Petugas Admin"

            # Validate required fields
            if not nama or not username or not password:
                flash('All fields must be filled out.', 'danger')
                return redirect(url_for('kelolaPetugas'))
            
            # Check if the username already exists
            cursor.execute("""
                SELECT id_user FROM users WHERE username = %s
            """, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username is already taken. Please choose another one.', 'danger')
                return redirect(url_for('kelolaPetugas'))

            try:
                cursor.execute("""
                    INSERT INTO Users (username, passwords, roles, nama)
                    VALUES (%s, %s, %s, %s) RETURNING ID_USER
                """, (username, password, role, nama,))
                user_id = cursor.fetchone()[0]
                connection.commit()
                
                cursor.execute("INSERT INTO Petugas_Administrasi (id_user) VALUES (%s)", (user_id,))
                connection.commit()

                flash("Berhasil menambahkan petugas adminstrasi!", "success")
            except Exception as e:
                connection.rollback()  # Rollback in case of error
                flash(f"An error occurred: {str(e)}", 'danger')

        try:
            cursor.execute("SELECT * FROM Petugas_Detail")
            petugas=cursor.fetchall()

        except Exception as e:
            flash(f"An error occurred while fetching petugas data: {str(e)}", 'danger')
            petugas = []

        return render_template("Admin/KelolaPetugas/kelolaPetugas.html", petugas=petugas)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))


#edit petugas
@app.route('/Admin/KelolaPetugas/EditPetugas', methods=['GET', 'POST'])
def editPetugas():
    if 'role' in session and session['role'] == 'Admin':
        id_user = request.args.get('id_user')

        if not id_user:
            flash('No ID Petugas Admin provided.', 'danger')
            return redirect(url_for('kelolaPetugas'))

        if request.method == 'POST':
            nama = request.form['admin-name']
            username = request.form['admin-username']
            password = request.form['admin-password']

            # Validate required fields
            if not nama or not username or not password:
                flash('All fields are required to update the petugas data.', 'danger')
                return redirect(url_for('editPetugas', id_user=id_user))

            # Check if the username already exists (excluding the current user)
            cursor.execute("""
                SELECT id_user FROM users WHERE username = %s AND id_user != %s
            """, (username, id_user))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username is already taken. Please choose another one.', 'danger')
                return redirect(url_for('editPetugas', id_user=id_user))

            try:
                cursor.execute("""
                    UPDATE Users SET nama=%s, username=%s, passwords=%s WHERE id_user=%s
                """, (nama, username, password, id_user,))
                connection.commit()

                flash("Berhasil mengganti data petugas administrasi!", "success")
                return redirect(url_for('kelolaPetugas'))

            except Exception as e:
                connection.rollback()
                flash(f"An error occurred: {str(e)}", 'danger')
                return redirect(url_for('editPetugas', id_user=id_user))

        try:
            cursor.execute("""
                SELECT *
                FROM petugas_detail
                WHERE id_user = %s
            """, (id_user,))
            petugas = cursor.fetchone()

            if not petugas:
                flash('Petugas not found.', 'danger')
                return redirect(url_for('kelolaPetugas'))

        except Exception as e:
            flash(f"An error occurred while fetching petugas data: {str(e)}", 'danger')
            return redirect(url_for('kelolaPetugas'))

        return render_template("Admin/KelolaPetugas/editPetugas.html", petugas=petugas)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))


#kelola pasien
@app.route('/Admin/KelolaPasien')
def kelolaPasien():
    if 'role' in session and session['role'] == 'Admin':
        try:
            cursor.execute("""
                SELECT * FROM pasien p JOIN users u on p.id_user=u.id_user
            """)
            list_pasien = cursor.fetchall()
            return render_template("Admin/KelolaPasien/kelolaPasien.html", pasien=list_pasien)
        
        except Exception as e:
            flash(f"An error occurred while fetching patient data: {str(e)}", "danger")
            return render_template("Admin/KelolaPasien/kelolaPasien.html", pasien=[])

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#edit pasien
@app.route('/Admin/KelolaPasien/EditPasien', methods=['GET', 'POST'])
def editPasien():
    if 'role' in session and session['role'] == 'Admin':
        id_user = request.args.get('id_user')
        if not id_user:
            flash('No ID Pasien provided', 'danger')
            return redirect(url_for('kelolaPasien'))

        if request.method == 'POST':
            nama = request.form['patient-name']
            gender = request.form['patient-gender']
            alamat = request.form['patient-address']
            lahir = request.form['patient-birthdate']
            kontak = request.form['patient-contact']

            # Check if any of the required fields are missing
            if not nama or not gender or not alamat or not lahir or not kontak:
                flash('All fields are required to update patient data.', 'danger')
                return redirect(url_for('editPasien', id_user=id_user))

            try:
                cursor.execute("""
                    UPDATE Users SET nama=%s
                    WHERE id_user=%s
                """, (nama, id_user,))
                connection.commit()

                cursor.execute("""
                    UPDATE pasien SET alamat=%s, gender=%s, tanggal_lahir=%s, kontak=%s
                    WHERE id_user=%s 
                """, (alamat, gender, lahir, kontak, id_user,))
                connection.commit()

                flash("Berhasil mengubah data pasien!", "success")
                return redirect(url_for('kelolaPasien'))

            except Exception as e:
                connection.rollback()  # Rollback if any error occurs
                flash(f"An error occurred while updating the patient data: {str(e)}", 'danger')
                return redirect(url_for('editPasien', id_user=id_user))

        try:
            cursor.execute("""
                SELECT * FROM pasien p JOIN users u on p.id_user=u.id_user
                WHERE p.id_user=%s
            """, (id_user,))
            pasien = cursor.fetchone()

            if not pasien:
                flash("Patient not found.", 'danger')
                return redirect(url_for('kelolaPasien'))

        except Exception as e:
            flash(f"An error occurred while fetching patient data: {str(e)}", 'danger')
            return redirect(url_for('kelolaPasien'))

        return render_template("Admin/KelolaPasien/editPasien.html", pasien=pasien)

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

#detail pasien
@app.route('/Admin/KelolaPasien/DetailPasien')
def detailPasien():
    if 'role' in session and session['role'] == 'Admin':
        id = request.args.get('id_user')
        if not id:
            flash("No ID Pasien provided", "danger")
            return redirect(url_for('kelolaPasien'))

        try:
            cursor.execute("""
                SELECT * FROM pasien p JOIN users u on p.id_user=u.id_user
                WHERE p.id_user=%s
            """, (id,))
            pasien = cursor.fetchone()

            if not pasien:
                flash("Patient not found.", 'danger')
                return redirect(url_for('kelolaPasien'))

            return render_template("Admin/KelolaPasien/detailPasien.html", pasien=pasien)

        except Exception as e:
            flash(f"An error occurred while fetching patient details: {str(e)}", 'danger')
            return redirect(url_for('kelolaPasien'))

    flash("Unauthorized access. Tolong login sebagai admin.", "danger")
    return redirect(url_for('login'))

##################################################################

# DOKTER #########################################################
@app.route('/Dokter')
def homepageDokter():
    if 'role' in session and session['role'] == 'Dokter':
        print("Selamat datang dokter")
        # try:
        #     # Query total pasien hari ini
        #     cursor.execute("SELECT COUNT(*) FROM buat_janji WHERE tanggal_janji = CURRENT_DATE")
        #     total_pasien_hari_ini = cursor.fetchone()[0]

        #     # Query total pasien bulan ini
        #     cursor.execute("""
        #         SELECT COUNT(*) FROM buat_janji 
        #         WHERE 
        #         AND EXTRACT(YEAR FROM tanggal_janji) = EXTRACT(YEAR FROM CURRENT_DATE)
        #     """)
        #     total_pasien_bulan_ini = cursor.fetchone()[0]
        # except Exception as e:
        #     flash(f"An error occurred: {str(e)}", 'danger')
        #     total_pasien_hari_ini = 0
        #     total_pasien_bulan_ini = 0  # Default jika query gagal

        # return render_template(
        #     "Perawat/index.html",
        #     nama=session.get('nama'),
        #     total_pasien_hari_ini=total_pasien_hari_ini,
        #     total_pasien_bulan_ini=total_pasien_bulan_ini
        # )
        # totalPasien = 
        return render_template("Dokter/Homepage/index.html", nama=session.get('nama'))
    
    flash("Unauthorized access. Please log in.", "danger")
    return redirect(url_for('login'))

@app.route('/Dokter/JanjiTemu')
def janjiTemu():
    if 'role' in session and session['role'] == 'Dokter':
        cursor.execute("""
            select * from buat_janji bj join jadwal_dokter j on bj.id_jadwal=j.id_jadwal join dokter d on d.npa=j.npa
            join pasien p on p.nomor_rekam_medis=bj.nomor_rekam_medis join users u on u.id_user=p.id_user
            where d.npa=%s
        """, (session.get('npa'),))
        list=cursor.fetchall()
        return render_template("Dokter/JanjiTemu/janjiTemu.html", list=list, npa=session.get('npa'))
    
    flash("Unauthorized access. Please log in as a doctor.", 'danger')
    return redirect(url_for('login'))

@app.route('/Dokter/JanjiTemu/CekPasien', methods=['GET', 'POST'])
def cekPasien():
    if 'role' in session and session['role'] == 'Dokter':
        session['nrm'] = request.args.get('nomor_rekam_medis')
        nomor_rekam_medis = session['nrm']
        print(nomor_rekam_medis)
        if nomor_rekam_medis:
            cursor.execute("""
            select 
                u.nama as nama,
                bj.id_janji as id_janji,
                bj.tanggal_janji as tanggal_janji,
                bj.nomor_antrian as nomor_antrian,
                j.id_jadwal as id_jadwal,
                j.hari as hari,
                d.npa as npa,
                d.spesialisasi as spesialisasi,
                p.nomor_rekam_medis as nomor_rekam_medis,
                c.tekanan_darah as tekanan_darah,
                c.tinggi_badan as tinggi_badan,
                c.berat_badan as berat_badan,
                c.suhu_badan as suhu_badan,
                c.keluhan as keluhan
            from 
                buat_janji bj join jadwal_dokter j on bj.id_jadwal=j.id_jadwal 
                join dokter d on d.npa=j.npa
                join pasien p on p.nomor_rekam_medis=bj.nomor_rekam_medis 
                join users u on u.id_user=p.id_user
                join catatan_vital c on c.nomor_rekam_medis=bj.nomor_rekam_medis
                where p.nomor_rekam_medis=%s
            """, (nomor_rekam_medis,))
            
            pasien=cursor.fetchone()
            return render_template("Dokter/CekPasien/cekPasien.html", pasien=pasien)
    
    flash("Unauthorized access. Please log in as a doctor.", 'danger')
    return redirect(url_for('login'))


@app.route('/Dokter/JanjiTemu/BuatDiagnosa', methods=['GET', 'POST'])
def buatDiagnosa():
    if 'role' in session and session['role'] == 'Dokter':
        session['nrm'] = request.args.get('nomor_rekam_medis')
        nomor_rekam_medis = session['nrm']
        print(nomor_rekam_medis)

        if request.method == 'POST':
            catatan = request.form['catatan']
            cursor.execute("""
                INSERT INTO diagnosa (keterangan, nomor_rekam_medis, npa)
                VALUES (%s, %s, %s) 
            """, (catatan, session['nrm'], session['npa'],))
            connection.commit()
            print("Catatan sukses")
            return redirect(url_for('janjiTemu'))

        if nomor_rekam_medis:
            cursor.execute("""
            select 
                u.nama as nama,
                bj.id_janji as id_janji,
                bj.tanggal_janji as tanggal_janji,
                bj.nomor_antrian as nomor_antrian,
                j.id_jadwal as id_jadwal,
                j.hari as hari,
                d.npa as npa,
                d.spesialisasi as spesialisasi,
                p.nomor_rekam_medis as nomor_rekam_medis,
                c.tekanan_darah as tekanan_darah,
                c.tinggi_badan as tinggi_badan,
                c.berat_badan as berat_badan,
                c.suhu_badan as suhu_badan,
                c.keluhan as keluhan,
                p.kontak as kontak
            from 
                buat_janji bj join jadwal_dokter j on bj.id_jadwal=j.id_jadwal 
                join dokter d on d.npa=j.npa
                join pasien p on p.nomor_rekam_medis=bj.nomor_rekam_medis 
                join users u on u.id_user=p.id_user
                join catatan_vital c on c.nomor_rekam_medis=bj.nomor_rekam_medis
                where p.nomor_rekam_medis=%s
            """, (nomor_rekam_medis,))
            
            pasien=cursor.fetchone()

            return render_template("Dokter/BuatDiagnosa/buatDiagnosa.html", pasien=pasien, dokter = session)
    
    flash("Unauthorized access. Please log in as a doctor.", 'danger')
    return redirect(url_for('login'))

@app.route('/Dokter/JanjiTemu/RiwayatMedis')
def riwayatMedis():
    if 'role' in session and session['role'] == 'Dokter':
        session['nrm'] = request.args.get('nomor_rekam_medis')
        nomor_rekam_medis = session['nrm']
        print(nomor_rekam_medis)
        if nomor_rekam_medis:
            cursor.execute("""
            select 
                u.nama as nama,
                bj.id_janji as id_janji,
                bj.tanggal_janji as tanggal_janji,
                bj.nomor_antrian as nomor_antrian,
                j.id_jadwal as id_jadwal,
                j.hari as hari,
                d.npa as npa,
                d.spesialisasi as spesialisasi,
                p.nomor_rekam_medis as nomor_rekam_medis,
                c.tekanan_darah as tekanan_darah,
                c.tinggi_badan as tinggi_badan,
                c.berat_badan as berat_badan,
                c.suhu_badan as suhu_badan,
                c.keluhan as keluhan,
                f.id_file as id_file,
                f.file_path
            from 
                buat_janji bj join jadwal_dokter j on bj.id_jadwal=j.id_jadwal 
                left join dokter d on d.npa=j.npa
                left join pasien p on p.nomor_rekam_medis=bj.nomor_rekam_medis 
                left join users u on u.id_user=p.id_user
                left join catatan_vital c on c.nomor_rekam_medis=bj.nomor_rekam_medis
                left join files_riwayatmedis f on f.nomor_rekam_medis=bj.nomor_rekam_medis
                where bj.nomor_rekam_medis=%s
            """, (nomor_rekam_medis,))
            
            pasien=cursor.fetchone()

            cursor.execute("""
                SELECT * FROM Files_RiwayatMedis WHERE nomor_Rekam_medis=%s ORDER BY Upload_Date DESC LIMIT 1
            """, (session['nrm'],))
            file = cursor.fetchone()
            file_path = file['file_path'] if file else None
            return render_template("Dokter/RiwayatMedis/riwayatMedis.html", pasien=pasien, file_path=file_path)
    
    flash("Unauthorized access. Please log in as a doctor.", 'danger')
    return redirect(url_for('login'))

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
                    flash('ID Perawat not found. Silakan login ulang.', 'danger')
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
            filepath = os.path.join('uploads', filename)

            try:
                # Simpan file ke folder uploads
                file.save(filepath)

                # Simpan metadata ke tabel Files_RiwayatMedis
                print("Inserting to database:", (filename, filepath, id_perawat, nomor_rekam_medis))
                cursor.execute("""
                    INSERT INTO Files_RiwayatMedis (File_Name, File_Path, id_perawat, nomor_rekam_medis)
                    VALUES (%s, %s, %s, %s)
                """, (filename, filepath, id_perawat, nomor_rekam_medis))
                print("Berhasil upload")
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