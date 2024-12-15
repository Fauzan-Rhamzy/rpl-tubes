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

SELECT * FROM USERS
SELECT * FROM ADMINS
SELECT * FROM DOKTER
SELECT * FROM PASIEN
SELECT * FROM PERAWAT
SELECT * FROM PETUGAS_ADMINISTRASI
SELECT * FROM CATATAN_VITAL	
SELECT * FROM JADWAL_DOKTER
SELECT * FROM RIWAYAT_MEDIS
SELECT * FROM FILES_RIWAYATMEDIS
SELECT * FROM TRANSAKSI
SELECT * FROM BUAT_JANJI

-- HAPUS DULU DATA SEBELUMNYA BARU DINSERT SAMA YANG BARU 
DELETE FROM USERS
DELETE FROM ADMINS
DELETE FROM DOKTER
DELETE FROM PASIEN
DELETE FROM PERAWAT
DELETE FROM PETUGAS_ADMINISTRASI
DELETE FROM CATATAN_VITAL
DELETE FROM JADWAL_DOKTER
DELETE FROM RIWAYAT_MEDIS
DELETE FROM FILES_RIWAYATMEDIS
DELETE FROM TRANSAKSI
DELETE FROM BUAT_JANJI

--BUAT TIPE DATA BARU
CREATE TYPE GenderType AS ENUM ('Male', 'Female');
CREATE TYPE StatusPembayaranType AS ENUM ('Lunas', 'Belum Lunas');

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
    ID_User INT NOT NULL,          -- ID_User adalah Foreign Key yang merujuk ke ID_User di tabel Users
    Nama VARCHAR(100) NOT NULL,    -- Nama admin akan diisi berdasarkan data dari tabel Users
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User) 
        ON DELETE CASCADE          -- Jika data user dihapus, data admin juga ikut terhapus
);

CREATE TABLE Dokter (
    NPA VARCHAR(25) PRIMARY KEY,  -- Nomor Praktik Nasional
    Spesialisasi VARCHAR(50) NOT NULL,
	Tarif NUMERIC(10,2) NOT NULL,
    ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    Nama VARCHAR(100) NOT NULL,   -- Nama Dokter diambil dari tabel Users berdasarkan ID_User
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika User dihapus, data dokter ikut terhapus
);

CREATE TABLE Pasien (
    Nomor_Rekam_Medis VARCHAR(8) PRIMARY KEY,
	ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    Nama VARCHAR(100) NOT NULL,   -- Nama Pasien diambil dari tabel Users berdasarkan ID_User
	Alamat TEXT,
    Gender GenderType NOT NULL,  -- ENUM memastikan hanya 'Male' atau 'Female' yang valid
    Tanggal_Lahir DATE,
    Kontak VARCHAR(15),
	FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika User dihapus, data pasien ikut terhapus
);
--TRIGGER UNTUK MENGHASILKAN NOMOR RANDOM
CREATE OR REPLACE FUNCTION generate_nomor_rekam_medis()
RETURNS TRIGGER AS $$
DECLARE
    new_nomor VARCHAR(8);
BEGIN
    LOOP
        -- Generate angka random 8 digit
        new_nomor := LPAD(CAST(FLOOR(RANDOM() * 99999999) AS TEXT), 8, '0');
        
        -- Pastikan nomor unik dengan memeriksa tabel Pasien
        IF NOT EXISTS (SELECT 1 FROM Pasien WHERE Nomor_Rekam_Medis = new_nomor) THEN
            EXIT; -- Keluar dari loop jika nomor unik
        END IF;
    END LOOP;

    -- Tetapkan nomor ke kolom
    NEW.Nomor_Rekam_Medis := new_nomor;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
--TRIGGER UNTUK TABEL PASIEN
CREATE TRIGGER before_insert_pasien
BEFORE INSERT ON Pasien
FOR EACH ROW
EXECUTE FUNCTION generate_nomor_rekam_medis();

CREATE TABLE Perawat (
    ID_Perawat SERIAL PRIMARY KEY,
	Nama VARCHAR(100) NOT NULL,   -- Nama Perawat diambil dari tabel Users berdasarkan ID_User
	ID_User INT NOT NULL,         -- ID_User sebagai Foreign Key yang merujuk ke ID_User di tabel Users
    FOREIGN KEY (ID_User) REFERENCES Users(ID_User)  -- Foreign Key ke tabel Users
        ON DELETE CASCADE -- Jika Perawat dihapus, data pasien ikut terhapus
);

CREATE TABLE Petugas_Administrasi (
    ID_Petugas_Admin SERIAL PRIMARY KEY,
	Nama VARCHAR(100) NOT NULL,   -- Nama Petugas Admin diambil dari tabel Users berdasarkan ID_User
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

CREATE TABLE Riwayat_Medis (
    ID_Diagnosa SERIAL PRIMARY KEY,
    Keterangan TEXT NOT NULL,
	Nomor_Rekam_Medis VARCHAR NOT NULL,
    FOREIGN KEY (Nomor_Rekam_Medis) REFERENCES Pasien(Nomor_Rekam_Medis)
);

--KOLOM BARU UNTUK UPLOAD FILE
CREATE TABLE Files_RiwayatMedis (
    ID_File SERIAL PRIMARY KEY,
    ID_Diagnosa INTEGER NOT NULL,
    File_Name VARCHAR(255) NOT NULL,
    File_Path VARCHAR(255) NOT NULL,
    Upload_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Diagnosa) REFERENCES Riwayat_Medis(ID_Diagnosa)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Transaksi (
    ID_Transaksi SERIAL PRIMARY KEY,
    Status_Pembayaran StatusPembayaranType NOT NULL,  -- Kolom dengan tipe ENUM
    Tanggal_Transaksi DATE,
    Jumlah_Pembayaran DECIMAL(10, 2),
    Nomor_Rekam_Medis VARCHAR REFERENCES Pasien(Nomor_Rekam_Medis),
    ID_Petugas_Admin INTEGER REFERENCES Petugas_Administrasi(ID_Petugas_Admin)
);

CREATE TABLE Buat_Janji (
    ID_Janji SERIAL PRIMARY KEY,
    Tanggal_Janji DATE NOT NULL,
    Nomor_Rekam_Medis VARCHAR NOT NULL,  -- Diambil dari Pasien
    ID_Jadwal INTEGER NOT NULL,  -- Diambil dari Jadwal_Dokter
    Nomor_Antrian INTEGER NOT NULL,  -- Menyimpan nomor antrian pasien
	Counts INTEGER, --Untuk menghitung banyak antrian sekarang, bakal di reset 0 ketika weekend
    FOREIGN KEY (Nomor_Rekam_Medis) REFERENCES Pasien(Nomor_Rekam_Medis),  -- Referensi ke Pasien
    FOREIGN KEY (ID_Jadwal) REFERENCES Jadwal_Dokter(ID_Jadwal)  -- Referensi ke Jadwal_Dokter
);