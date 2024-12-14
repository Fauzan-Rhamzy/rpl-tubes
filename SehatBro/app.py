import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session, flash
from psycopg2.extras import DictCursor
from werkzeug.utils import secure_filename
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
