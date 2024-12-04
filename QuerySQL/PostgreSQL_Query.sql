CREATE TABLE Admin (
    ID_Admin SERIAL PRIMARY KEY,
    Nama VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL
);

CREATE TABLE Pasien (
    Nomor_Rekam_Medis SERIAL PRIMARY KEY,
    Nama VARCHAR(100) NOT NULL,
    Alamat TEXT,
    Gender VARCHAR(10),
    Tanggal_Lahir DATE,
    Kontak VARCHAR(15),
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL
);

CREATE TABLE Dokter (
    ID_Dokter SERIAL PRIMARY KEY,
    Nama VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Spesialisasi VARCHAR(50),
    Kuota_Pasien INTEGER,
    Tarif DECIMAL(10, 2)
);

CREATE TABLE Perawat (
    ID_Perawat SERIAL PRIMARY KEY,
    Nama VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL
);

CREATE TABLE Petugas_Administrasi (
    ID_Petugas_Admin SERIAL PRIMARY KEY,
    Nama VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL
);

CREATE TABLE Catatan_Vital (
    ID_Catatan_Vital SERIAL PRIMARY KEY,
    Tekanan_Darah VARCHAR(20),
    Tinggi_Badan DECIMAL(5, 2),
    Berat_Badan DECIMAL(5, 2),
    Suhu_Badan DECIMAL(4, 2),
    Keluhan TEXT,
    Nomor_Rekam_Medis INTEGER REFERENCES Pasien(Nomor_Rekam_Medis)
);

CREATE TABLE Jadwal_Dokter (
    ID_Jadwal SERIAL PRIMARY KEY,
    Hari VARCHAR(20) NOT NULL,
    Jam TIME NOT NULL,
    ID_Dokter INTEGER REFERENCES Dokter(ID_Dokter)
);

CREATE TABLE Riwayat_Medis (
    ID_Diagnosa SERIAL PRIMARY KEY,
    Keterangan TEXT NOT NULL,
    Nomor_Rekam_Medis INTEGER REFERENCES Pasien(Nomor_Rekam_Medis)
);

CREATE TABLE Transaksi (
    ID_Transaksi SERIAL PRIMARY KEY,
    Status_Pembayaran VARCHAR(20),
    Tanggal_Transaksi DATE,
    Jumlah_Pembayaran DECIMAL(10, 2),
    Nomor_Rekam_Medis INTEGER REFERENCES Pasien(Nomor_Rekam_Medis),
    ID_Petugas_Admin INTEGER REFERENCES Petugas_Administrasi(ID_Petugas_Admin)
);

CREATE TABLE Buat_Janji (
    ID_Janji SERIAL PRIMARY KEY,
    Tanggal_Janji DATE NOT NULL,
    Nomor_Rekam_Medis INTEGER REFERENCES Pasien(Nomor_Rekam_Medis),
    ID_Jadwal INTEGER REFERENCES Jadwal_Dokter(ID_Jadwal)
);
