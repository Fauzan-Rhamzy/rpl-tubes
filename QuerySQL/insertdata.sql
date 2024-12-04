INSERT INTO Admin (Nama, Username, Password)
VALUES
('Fauzan', 'admin_fauzan', 'password123'),
('Johnson', 'admin_johnson', 'securepass456'),
('Debby', 'admin_debby', 'debbypass1234'),
('Junita', 'admin_junita', 'securejunita');

INSERT INTO Pasien (Nama, Alamat, Gender, Tanggal_Lahir, Kontak, Username, Password)
VALUES
('Ahmad Fauzi', 'Jl. Merdeka No. 12, Bandung', 'Laki-laki', '1990-05-12', '081234567890', 'ahmad_fauzi', 'pass123'),
('Siti Nurhaliza', 'Jl. Pahlawan No. 3, Jakarta', 'Perempuan', '1985-09-20', '081987654321', 'siti_nurhaliza', 'siti456'),
('Deni Ramadhan', 'Jl. Sudirman No. 5, Bandung', 'Laki-laki', '1995-01-15', '081345678910', 'deni_ramadhan', 'denipass'),
('Lina Permata', 'Jl. Kembang No. 7, Surabaya', 'Perempuan', '1998-07-20', '081987651234', 'lina_permata', 'lina456');

INSERT INTO Dokter (Nama, Username, Password, Spesialisasi, Kuota_Pasien, Tarif)
VALUES
('Dr. Andreas', 'dokter_andreas', 'dokpass123', 'Penyakit Dalam', 10, 150000),
('Dr. Maria', 'dokter_maria', 'securemaria', 'Anak', 15, 200000),
('Dr. Fauziah', 'dokter_fauziah', 'dokfauziah', 'Gigi', 20, 250000),
('Dr. Kevin', 'dokter_kevin', 'dokkevin123', 'Mata', 12, 180000);

INSERT INTO Perawat (Nama, Username, Password)
VALUES
('Nina Pratiwi', 'perawat_nina', 'nina123'),
('Budi Santoso', 'perawat_budi', 'budi456'),
('Ika Nuraini', 'perawat_ika', 'ikapass'),
('Yusuf Aditya', 'perawat_yusuf', 'yusuf123');

INSERT INTO Petugas_Administrasi (Nama, Username, Password)
VALUES
('Rizki Amelia', 'admin_rizki', 'rizkiadmin'),
('Hendra Wijaya', 'admin_hendra', 'securehendra'),
('Amelia Yuliana', 'admin_amelia', 'amelia456'),
('Rian Setiawan', 'admin_rian', 'rianpass123');

INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
VALUES
('120/80', 170.5, 65.0, 36.5, 'Sakit kepala dan mual', 1),
('110/70', 160.0, 50.0, 37.0, 'Demam tinggi', 2),
('130/85', 165.0, 70.0, 36.8, 'Nyeri punggung', 3),
('100/60', 158.0, 48.0, 37.2, 'Batuk kering', 4);

INSERT INTO Jadwal_Dokter (Hari, Jam, ID_Dokter)
VALUES
('Senin', '09:00:00', 1),
('Selasa', '10:30:00', 2),
('Rabu', '08:00:00', 3),
('Kamis', '14:00:00', 4);

INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
VALUES
('Pemeriksaan tekanan darah rutin', 1),
('Pemeriksaan dan terapi untuk demam', 2),
('Pengobatan nyeri punggung', 3),
('Terapi untuk batuk kering', 4);

INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
VALUES
('Lunas', '2024-11-29', 150000, 1, 1),
('Belum Lunas', '2024-11-28', 200000, 2, 2),
('Lunas', '2024-11-30', 250000, 3, 3),
('Belum Lunas', '2024-11-27', 180000, 4, 4);

INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal)
VALUES
('2024-12-01', 1, 1),
('2024-12-03', 2, 2),
('2024-12-05', 3, 3),
('2024-12-07', 4, 4);
