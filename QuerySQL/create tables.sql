DROP TABLE IF EXISTS Buat_Janji CASCADE;
DROP TABLE IF EXISTS Transaksi CASCADE;
DROP TABLE IF EXISTS Files_RiwayatMedis CASCADE;
DROP TABLE IF EXISTS Riwayat_Medis CASCADE;
DROP TABLE IF EXISTS Jadwal_Dokter CASCADE;
DROP TABLE IF EXISTS Catatan_Vital CASCADE;
DROP TABLE IF EXISTS Petugas_Administrasi CASCADE;
DROP TABLE IF EXISTS Perawat CASCADE;
DROP TABLE IF EXISTS Pasien CASCADE;
DROP TABLE IF EXISTS Dokter CASCADE;
DROP TABLE IF EXISTS Admins CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

--BUAT TABLE
CREATE TABLE Users (
    ID_User SERIAL PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Passwords VARCHAR(100) NOT NULL,
    Roles VARCHAR(20) NOT NULL, -- Admin, Dokter, Pasien, Perawat, Petugas Admin
    Nama VARCHAR(100) NOT NULL
);

CREATE TABLE Admins (
    ID_Admin SERIAL PRIMARY KEY,   -- ID_Admin akan otomatis bertambah
    ID_User INT NOT NULL,          -- ID_User adalah Foreign Key yang merujuk ke ID_User di tabel User
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User) 
        ON DELETE CASCADE          -- Jika data user dihapus, data admin juga ikut terhapus
);

CREATE TABLE Dokter (
    NPA VARCHAR(25) PRIMARY KEY,  -- Nomor Praktik Nasional
    Spesialisasi VARCHAR(50) NOT NULL,
	Tarif NUMERIC(10,2) NOT NULL,
    ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika User dihapus, data dokter ikut terhapus
);

CREATE TABLE Pasien (
    Nomor_Rekam_Medis VARCHAR(8) PRIMARY KEY,
	ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
	Alamat TEXT,
    Gender TEXT NOT NULL, 
    Tanggal_Lahir DATE,
    Kontak VARCHAR(15),
	FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika User dihapus, data pasien ikut terhapus
);

CREATE TABLE Perawat (
    ID_Perawat SERIAL PRIMARY KEY,
	ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika Perawat dihapus, data pasien ikut terhapus
);

CREATE TABLE Petugas_Administrasi (
    ID_Petugas_Admin SERIAL PRIMARY KEY,
	ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika Petugas Admin dihapus, data pasien ikut terhapus
);

CREATE TABLE Catatan_Vital (
    ID_Catatan_Vital SERIAL PRIMARY KEY,
    Tekanan_Darah VARCHAR(20),
    Tinggi_Badan DECIMAL(5, 2),
    Berat_Badan DECIMAL(5, 2),
    Suhu_Badan DECIMAL(4, 2),
    Keluhan TEXT,
	id_perawat serial references perawat(id_perawat),
    Nomor_Rekam_Medis VARCHAR REFERENCES Pasien(Nomor_Rekam_Medis)
);

CREATE TABLE Jadwal_Dokter (
    ID_Jadwal SERIAL PRIMARY KEY,
	Kuota_Pasien INT NOT NULL, 
    Hari VARCHAR(20) NOT NULL,
    Jam_Mulai TIME NOT NULL,
    Jam_Selesai TIME NOT NULL,
    NPA VARCHAR(20) REFERENCES Dokter(NPA)
);

CREATE TABLE Diagnosa (
    ID_Diagnosa SERIAL PRIMARY KEY,
    Keterangan TEXT NOT NULL,
	Nomor_Rekam_Medis VARCHAR NOT NULL,
	npa varchar(25) references dokter(npa),
    FOREIGN KEY (Nomor_Rekam_Medis) REFERENCES Pasien(Nomor_Rekam_Medis)
	
);

drop table files_riwayatmedis;

--KOLOM BARU UNTUK UPLOAD FILE
CREATE TABLE Files_RiwayatMedis (
    ID_File SERIAL PRIMARY KEY,
    File_Name VARCHAR(255) NOT NULL,
    File_Path VARCHAR(255) NOT NULL,
    Upload_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_perawat serial,
	nomor_rekam_medis varchar(8) references pasien(nomor_rekam_medis),
    FOREIGN KEY (id_perawat) REFERENCES perawat(id_perawat)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Buat_Janji (
    ID_Janji SERIAL PRIMARY KEY,
    Tanggal_Janji DATE NOT NULL,
    Nomor_Rekam_Medis VARCHAR NOT NULL,  -- Diambil dari Pasien
    ID_Jadwal INTEGER NOT NULL,  -- Diambil dari Jadwal_Dokter
    Nomor_Antrian INTEGER NOT NULL,  -- Menyimpan nomor antrian pasien
    FOREIGN KEY (Nomor_Rekam_Medis) REFERENCES Pasien(Nomor_Rekam_Medis),  -- Referensi ke Pasien
    FOREIGN KEY (ID_Jadwal) REFERENCES Jadwal_Dokter(ID_Jadwal)  -- Referensi ke Jadwal_Dokter
);

CREATE TABLE Transaksi (
    ID_Transaksi SERIAL PRIMARY KEY,
    Status_Pembayaran text NOT NULL,
    Tanggal_Transaksi DATE,
    Jumlah_Pembayaran DECIMAL(10, 2),
    Nomor_Rekam_Medis VARCHAR REFERENCES Pasien(Nomor_Rekam_Medis),
    ID_Petugas_Admin INTEGER REFERENCES Petugas_Administrasi(ID_Petugas_Admin)
);

SELECT * FROM USERS
SELECT * FROM ADMINS
SELECT * FROM dokter
SELECT * FROM pasien
select * from perawat
select * from petugas_administrasi
select * from catatan_vital
select * from jadwal_dokter
select * from files_riwayatmedis
select * from buat_janji
select * from transaksi

-- -- BUAT VIEW TABLE
CREATE VIEW perawat_detail AS
SELECT 
        p.id_perawat AS id_perawat, 
        u.nama AS nama, 
        u.username AS username, 
		u.passwords AS passwords,
        p.id_User AS id_User
FROM Perawat p 
JOIN Users u ON p.ID_User = u.ID_User

CREATE VIEW dokter_detail AS
SELECT 
        d.npa AS npa, 
        u.nama AS nama, 
        u.username AS username, 
        u.passwords AS passwords,
		d.spesialisasi AS spesialisasi,
		d.tarif AS tarif,
        u.id_User AS id_User
FROM dokter d 
JOIN Users u ON d.ID_User = u.ID_User

CREATE VIEW jadwal_detail AS
SELECT 
        d.npa AS npa, 
        u.nama AS nama, 
        u.username AS username, 
        u.passwords AS passwords,
		d.spesialisasi AS spesialisasi,
		d.tarif AS tarif,
        u.id_User AS id_User,
		j.id_jadwal as id_jadwal,
		j.kuota_pasien as kuota_pasien,
		j.hari as hari,
		j.jam_mulai as jam_mulai,
		j.jam_selesai as jam_selesai
FROM dokter d 
JOIN Users u ON d.ID_User = u.ID_User 
JOIN jadwal_dokter j ON j.npa = d.npa

CREATE VIEW petugas_detail AS
SELECT 
        p.ID_Petugas_Admin AS ID_Petugas_Admin, 
        u.nama AS nama, 
        u.username AS username, 
        u.passwords AS passwords,
        u.id_User AS id_User
FROM Petugas_Administrasi p
JOIN Users u ON p.ID_User = u.ID_User

CREATE VIEW pasien_detail AS
SELECT 
        p.nomor_rekam_medis AS nomor_rekam_medis, 
        u.nama AS nama, 
        u.username AS username, 
		u.passwords AS passwords,
        p.id_User AS id_User
FROM pasien p 
JOIN Users u ON p.ID_User = u.ID_User

-- 
SELECT * FROM Transaksi INNER JOIN buat_janji ON Transaksi.nomor_rekam_medis = buat_janji.nomor_rekam_medis
SELECT * from diagnosa inner join buat_janji on diagnosa.nomor_rekam_medis = buat_janji.nomor_rekam_medis
SELECT * from diagnosa inner join pasien on diagnosa.nomor_rekam_medis = pasien.nomor_rekam_medis
select * from catatan_vital cv inner join pasien ps on cv.nomor_rekam_medis = ps.nomor_rekam_medis
select * from catatan_vital cv inner join perawat pr on cv.id_perawat = pr.id_perawat inner join users u on pr.id_user = u.id_user
