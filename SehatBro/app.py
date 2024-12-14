import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session, flash, jsonify, send_from_directory
from psycopg2.extras import DictCursor
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


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

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# homepage umum
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
                    p.ID_Perawat
                FROM 
                    Users u
                LEFT JOIN 
                    Perawat p ON u.ID_User = p.ID_User
                WHERE 
                    u.Username = %s AND u.Passwords = %s
            """, (username, password))
            user = cursor.fetchone()

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
            'Pasien/JadwalTemu/index.html',
            upcoming_appointments=upcoming_appointments,
            history_appointments=history_appointments
        )
    except Exception as e:
        print(f"Error in /jadwaltemu route: {e}")
        return "Internal Server Error", 500



@app.route('/Booking', methods=['GET', 'POST'])
def booking():
    return render_template("Pasien/Booking/index.html")


@app.route('/Profile')
def profile():
    if 'user_id' not in session or session.get('role') != 'Pasien':
        flash("Unauthorized access. Please log in.", "danger")
        return redirect(url_for('login'))
    user_id = session['user_id']

    # Informasi pasien
    cursor.execute("""
            SELECT 
                u.Nama AS nama_pasien, 
                p.Alamat AS alamat,
                p.nomor_rekam_medis,
                p.tanggal_lahir AS tanggal_lahir,
                p.gender AS jenis_kelamin,
                p.kontak AS telepon
            FROM 
                Users u
            JOIN 
                Pasien p ON u.ID_User = p.ID_User
            WHERE 
                u.ID_User = %s;
        """, (user_id,))
    patient_info = cursor.fetchone()


    return render_template("Pasien/Profile/index.html", patient_info=patient_info)

@app.route('/Profile/EditProfile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        user_id = session['user_id']
        if not user_id:
            flash("Anda harus login untuk mengedit profil.", 'danger')
            return redirect(url_for('login'))

        # Ambil data dari form
        nama = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        alamat = request.form.get('address')
        gender = request.form.get('gender')
        tanggal_lahir = request.form.get('birthdate')
        kontak = request.form.get('phone')

        try:
            # Update tabel Users
            if username or password or nama:
                cursor.execute("""
                    UPDATE Users
                    SET
                        Username = COALESCE(%s, Username),
                        Passwords = COALESCE(%s, Passwords),
                        Nama = COALESCE(%s, Nama)
                    WHERE ID_User = %s
                """, (username, password, nama, user_id))
            
            # Update tabel Pasien
            if alamat or gender or tanggal_lahir or kontak:
                cursor.execute("""
                    UPDATE Pasien
                    SET
                        Alamat = COALESCE(%s, Alamat),
                        Gender = COALESCE(%s, Gender),
                        Tanggal_Lahir = COALESCE(%s, Tanggal_Lahir),
                        Kontak = COALESCE(%s, Kontak)
                    WHERE ID_User = %s
                """, (alamat, gender, tanggal_lahir, kontak, user_id))

            connection.commit()
            flash("Profil berhasil diperbarui!", 'success')
            return redirect(url_for('profile'))
        except Exception as e:
            connection.rollback()
            flash(f"Terjadi kesalahan saat memperbarui profil: {str(e)}", 'danger')

        return redirect(url_for('edit_profile'))

    # GET request: Tampilkan halaman edit profil
    user_id = session['user_id']
    if not user_id:
        flash("Anda harus login untuk mengakses halaman ini.", 'danger')
        return redirect(url_for('login'))

    try:
        # Ambil data profil pengguna dari database
        cursor.execute("""
            SELECT 
                u.Nama, u.Username, p.Alamat, p.Gender, 
                p.Tanggal_Lahir, p.Kontak
            FROM Users u
            LEFT JOIN Pasien p ON u.ID_User = p.ID_User
            WHERE u.ID_User = %s
        """, (user_id,))
        user_data = cursor.fetchone()
    except Exception as e:
        flash(f"Terjadi kesalahan saat memuat data: {str(e)}", 'danger')
        user_data = None

    return render_template("Pasien/Profile/editProfile.html", user_data=user_data)

@app.route('/Profile/RiwayatMedis')
def riwayat_medis():
    user_id = session['user_id']
    
    # File path untuk file riwayat medis
    cursor.execute("""
            SELECT p.nomor_rekam_medis
            FROM Pasien p
            WHERE p.id_user = %s
        """, (user_id,))
    res = cursor.fetchone()
    nrm = res['nomor_rekam_medis']

    cursor.execute("""
            SELECT * FROM Files_RiwayatMedis WHERE nomor_Rekam_medis=%s ORDER BY Upload_Date DESC LIMIT 1
        """, (nrm,))
    file = cursor.fetchone()
    file_path = file['file_path'] if file else None
    
    return render_template("Pasien/Profile/riwayatMedis.html", file_path=file_path)


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