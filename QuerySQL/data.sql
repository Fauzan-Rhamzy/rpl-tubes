INSERT INTO Users (Username, Passwords, Roles, Nama) VALUES

--ADMIN
('admin_fauzan', 'password123', 'Admin', 'Fauzan'),
('admin_johnson', 'securepass456', 'Admin', 'Johnson'),
('admin_debby', 'debbypass1234', 'Admin', 'Debby'),
('admin_junita', 'securejunita', 'Admin', 'Junita'),

--DOKTER: PENYAKIT DALAM
('dokter_andreas', 'dokpass123', 'Dokter', 'dr. Andreas Siregar, SpPD'),
('dokter_maria', 'securemaria', 'Dokter', 'dr. Maria Eva, SpPD'),
('dokter_fauziah', 'dokfauziah', 'Dokter', 'dr. Fauziah Heny, SpPD'),
('dokter_kevin', 'dokkevin123', 'Dokter', 'dr. Kevin Wibisono, SpPD'),
('dokter_yuliana', 'yuliana123', 'Dokter', 'dr. Yuliana Kurniawan, SpPD'),
-- DOKTER: GIGI
('dokter_alexsander', 'dokpass123', 'Dokter', 'drg. Alexander Tampubolon'),
('dokter_novita', 'novitaaa123', 'Dokter', 'drg. Novita Afni'),
('dokter_dian', 'dokdian123', 'Dokter', 'drg. Dian Prasetyo'),
('dokter_amelia', 'dokamelia456', 'Dokter', 'drg. Amelia Wijaya'),
('dokter_ronald', 'ronald1234', 'Dokter', 'drg. Ronald Hutapea'),
-- DOKTER: MATA
('dokter_lukman', 'lukman321', 'Dokter', 'dr. Lukman Hakim, SpM(K)'),
('dokter_silvia', 'doksilvia123', 'Dokter', 'dr. Silvia Tjandra, SpM'),
('dokter_james', 'dokjames234', 'Dokter', 'dr. James Kusuma, SpM'),
('dokter_angela', 'dokangela345', 'Dokter', 'dr. Angela Putri, SpM'),
('dokter_felix', 'dokfelix456', 'Dokter', 'dr. Felix Sudarmono, SpM'),
-- DOKTER: ANAK
('dokter_reza', 'dokreza123', 'Dokter', 'dr. Reza Mahendra, SpA'),
('dokter_nurul', 'doknurul321', 'Dokter', 'dr. Nurul Arifah, SpA'),
('dokter_gabriel', 'dokgabriel234', 'Dokter', 'dr. Gabriel Manulang, SpA'),
('dokter_jessica', 'dokjessica456', 'Dokter', 'dr. Jessica Anggraeni, SpA'),
('dokter_alvina', 'dokalvina789', 'Dokter', 'dr. Alvina Tarigan, SpA'),

--PASIEN
('ahmad_fauzi', 'pass123', 'Pasien', 'Ahmad Fauzi'),
('siti_nurhaliza', 'siti456', 'Pasien', 'Siti Nurhaliza'),
('deni_ramadhan', 'denipass', 'Pasien', 'Deni Ramadhan'),
('lina_permata', 'lina456', 'Pasien', 'Lina Permata'),
('agus_saputra', 'agus123', 'Pasien', 'Agus Saputra'),
('maria_agnes', 'maria456', 'Pasien', 'Maria Agnes'),
('bambang_prasetyo', 'bambang789', 'Pasien', 'Bambang Prasetyo'),
('nurul_hidayah', 'nurul321', 'Pasien', 'Nurul Hidayah'),
('eko_susilo', 'eko123', 'Pasien', 'Eko Susilo'),
('riana_maharani', 'riana456', 'Pasien', 'Riana Maharani'),
('yusuf_kurniawan', 'yusuf789', 'Pasien', 'Yusuf Kurniawan'),
('tiara_andini', 'tiara321', 'Pasien', 'Tiara Andini'),
('andi_rahman', 'andi123', 'Pasien', 'Andi Rahman'),
('angela_putri', 'angela456', 'Pasien', 'Angela Putri'),
('fikri_akbar', 'fikri789', 'Pasien', 'Fikri Akbar'),
('melati_indah', 'melati321', 'Pasien', 'Melati Indah'),
('dian_firmansyah', 'dian123', 'Pasien', 'Dian Firmansyah'),

-- PERAWAT : Anggapnya tuh satu perawat kerja buat satu dokter makanya ada 20, tapi bebas gitu bisa nukar-nukar
('perawat_nina', 'nina123', 'Perawat', 'Nina Pratiwi'),
('perawat_budi', 'budi456', 'Perawat', 'Budi Santoso'),
('perawat_ika', 'ikapass', 'Perawat', 'Ika Nuraini'),
('perawat_yusuf', 'yusuf123', 'Perawat', 'Yusuf Aditya'),

('perawat_siti', 'siti123', 'Perawat', 'Siti Rahmawati'),
('perawat_andi', 'andi456', 'Perawat', 'Andi Saputra'),
('perawat_maya', 'mayapass', 'Perawat', 'Maya Handayani'),
('perawat_toni', 'toni789', 'Perawat', 'Toni Wirawan'),

('perawat_linda', 'linda321', 'Perawat', 'Linda Maharani'),
('perawat_hendra', 'hendra456', 'Perawat', 'Hendra Gunawan'),
('perawat_nurul', 'nurul123', 'Perawat', 'Nurul Fadillah'),
('perawat_joko', 'joko678', 'Perawat', 'Joko Wijaya'),

('perawat_anggi', 'anggi123', 'Perawat', 'Anggi Kusuma'),
('perawat_wahyu', 'wahyu456', 'Perawat', 'Wahyu Setiawan'),
('perawat_dewi', 'dewi789', 'Perawat', 'Dewi Hartini'),
('perawat_ahmad', 'ahmad234', 'Perawat', 'Ahmad Firdaus'),

('perawat_melati', 'melati111', 'Perawat', 'Melati Anggraini'),
('perawat_farhan', 'farhan222', 'Perawat', 'Farhan Wijaya'),
('perawat_anisa', 'anisa333', 'Perawat', 'Anisa Rahmadani'),
('perawat_roni', 'roni444', 'Perawat', 'Roni Pratama'),


--PETUGAS ADMINISTRASI
('admin_rizki', 'rizkiadmin', 'Petugas Admin', 'Rizki Amelia'),
('admin_hendra', 'securehendra', 'Petugas Admin', 'Hendra Wijaya'),
('admin_amelia', 'amelia456', 'Petugas Admin', 'Amelia Yuliana'),
('admin_rian', 'rianpass123', 'Petugas Admin', 'Rian Setiawan'),
('admin_dian', 'dianadmin123', 'Petugas Admin', 'Dian Prakoso'),
('admin_silvia', 'silviaadmin456', 'Petugas Admin', 'Silvia Hartono'),
('admin_firman', 'firman789', 'Petugas Admin', 'Firman Sutrisno'),
('admin_linda', 'lindaadmin321', 'Petugas Admin', 'Linda Pratiwi');

INSERT INTO Admins (ID_User)
SELECT ID_User
FROM Users
WHERE Roles = 'Admin';

INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.03.01.051792',   -- NPA (input oleh admin)
    'Penyakit Dalam',  -- Spesialisasi (input oleh admin)
    200000.00,    -- Tarif (input oleh admin)
    u.ID_User   -- ID_User diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_andreas'; --Username yang diinput Admin
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.03.01.051743',   
    'Penyakit Dalam',  
    300000.00,   
    u.ID_User   
FROM Users u
WHERE u.Username = 'dokter_maria';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.03.01.051784',   
    'Penyakit Dalam', 
    150000.00,  
    u.ID_User     
FROM Users u
WHERE u.Username = 'dokter_fauziah';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.03.01.051762',   
    'Penyakit Dalam',  
    200000.00,   
    u.ID_User   
FROM Users u
WHERE u.Username = 'dokter_kevin';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.03.01.051766',   
    'Penyakit Dalam',  
    250000.00,   
    u.ID_User   
FROM Users u
WHERE u.Username = 'dokter_yuliana';

--GIGI
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.01.01.054453',   -- NPA (input oleh admin)
    'Gigi',  -- Spesialisasi (input oleh admin)
    199000.00,    -- Tarif (input oleh admin)
    u.ID_User
FROM Users u
WHERE u.Username = 'dokter_alexsander';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.01.01.054853',   
    'Gigi',  
    150000.00,    
    u.ID_User  
     
FROM Users u
WHERE u.Username = 'dokter_novita';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.01.01.054353',   
    'Gigi',  
    145000.00,   
    u.ID_User   
       
FROM Users u
WHERE u.Username = 'dokter_dian';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.01.01.054903',  
    'Gigi',  
    150000.00,    
    u.ID_User   
       
FROM Users u
WHERE u.Username = 'dokter_amelia';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.01.01.054978',   
    'Gigi',  
    200000.00,   
    u.ID_User   
       
FROM Users u
WHERE u.Username = 'dokter_ronald';

--MATA
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.02.01.051401',   -- NPA (input oleh admin)
    'Mata',  -- Spesialisasi (input oleh admin)
    190000.00,    -- Tarif (input oleh admin)
    u.ID_User   -- ID_User diambil dari Users berdasarkan username
       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_lukman';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.02.01.051411',  
    'Mata', 
    150000.00, 
    u.ID_User 
     
FROM Users u
WHERE u.Username = 'dokter_silvia';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.02.01.051441',  
    'Mata', 
    200000.00, 
    u.ID_User 
     
FROM Users u
WHERE u.Username = 'dokter_james';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.02.01.051422',  
    'Mata', 
    160000.00, 
    u.ID_User 
     
FROM Users u
WHERE u.Username = 'dokter_angela';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.02.01.051442',  
    'Mata', 
    170000.00, 
    u.ID_User 
     
FROM Users u
WHERE u.Username = 'dokter_felix';

--ANAK
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.08.01.051638',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    100000.00,    -- Tarif (input oleh admin)
    u.ID_User   -- ID_User diambil dari Users berdasarkan username
       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_reza';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.08.01.051634',  
    'Anak', 
    130000.00,
    u.ID_User
    
FROM Users u
WHERE u.Username = 'dokter_nurul';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.08.01.051627',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    150000.00,    -- Tarif (input oleh admin)
    u.ID_User   -- ID_User diambil dari Users berdasarkan username
       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_gabriel';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.08.01.051621',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    180000.00,    -- Tarif (input oleh admin)
    u.ID_User   -- ID_User diambil dari Users berdasarkan username
       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_jessica';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User)
SELECT
    '013281.08.01.051611',  
    'Anak',  
    175000.00,   
    u.ID_User   
       
FROM Users u
WHERE u.Username = 'dokter_alvina';

-- Insert data into Pasien table
INSERT INTO Pasien (Nomor_Rekam_Medis, ID_User, Alamat, Gender, Tanggal_Lahir, Kontak)
VALUES
('P0001RM', (SELECT ID_User FROM Users WHERE Username = 'ahmad_fauzi'), 'Jl. Sudirman No. 1, Jakarta', 'Laki-laki', '1990-01-15', '081234567890'),
('P0002SN', (SELECT ID_User FROM Users WHERE Username = 'siti_nurhaliza'), 'Jl. Merdeka No. 23, Bandung', 'Perempuan', '1992-03-21', '081223344556'),
('P0003DR', (SELECT ID_User FROM Users WHERE Username = 'deni_ramadhan'), 'Jl. Diponegoro No. 45, Surabaya', 'Laki-laki', '1988-07-10', '081334455667'),
('P0004LP', (SELECT ID_User FROM Users WHERE Username = 'lina_permata'), 'Jl. Hasanuddin No. 67, Medan', 'Perempuan', '1995-05-30', '081556677889'),
('P1001AS', (SELECT ID_User FROM Users WHERE Username = 'agus_saputra'), 'Jl. Kartini No. 89, Yogyakarta', 'Laki-laki', '1985-12-01', '081667788990'),
('P1002MA', (SELECT ID_User FROM Users WHERE Username = 'maria_agnes'), 'Jl. Gajah Mada No. 12, Semarang', 'Perempuan', '1993-08-18', '081778899001'),
('P1003BP', (SELECT ID_User FROM Users WHERE Username = 'bambang_prasetyo'), 'Jl. Pemuda No. 34, Malang', 'Laki-laki', '1987-11-25', '081889900112'),
('P1004NH', (SELECT ID_User FROM Users WHERE Username = 'nurul_hidayah'), 'Jl. Sultan Agung No. 56, Palembang', 'Perempuan', '1994-09-07', '081990011223'),
('P2001ES', (SELECT ID_User FROM Users WHERE Username = 'eko_susilo'), 'Jl. Pattimura No. 78, Makassar', 'Laki-laki', '1990-02-13', '082011223344'),
('P2002RM', (SELECT ID_User FROM Users WHERE Username = 'riana_maharani'), 'Jl. Kebon Jeruk No. 90, Bekasi', 'Perempuan', '1996-04-25', '082122334455'),
('P2003YK', (SELECT ID_User FROM Users WHERE Username = 'yusuf_kurniawan'), 'Jl. Diponegoro No. 11, Batam', 'Laki-laki', '1989-06-15', '082233445566'),
('P3001TA', (SELECT ID_User FROM Users WHERE Username = 'tiara_andini'), 'Jl. Sudirman No. 22, Solo', 'Perempuan', '1997-10-05', '082344556677'),
('P3002AR', (SELECT ID_User FROM Users WHERE Username = 'andi_rahman'), 'Jl. Thamrin No. 33, Manado', 'Laki-laki', '1991-03-20', '082455667788'),
('P3003AP', (SELECT ID_User FROM Users WHERE Username = 'angela_putri'), 'Jl. Asia Afrika No. 44, Denpasar', 'Perempuan', '1995-07-11', '082566778899'),
('P4001FA', (SELECT ID_User FROM Users WHERE Username = 'fikri_akbar'), 'Jl. Kartini No. 55, Banda Aceh', 'Laki-laki', '1992-01-25', '082677889900'),
('P4002MI', (SELECT ID_User FROM Users WHERE Username = 'melati_indah'), 'Jl. Pemuda No. 66, Pontianak', 'Perempuan', '1996-05-17', '082788990011'),
('P4003DF', (SELECT ID_User FROM Users WHERE Username = 'dian_firmansyah'), 'Jl. Pahlawan No. 77, Lampung', 'Laki-laki', '1988-09-09', '082899001122');

-- PERAWAT : 
INSERT INTO Perawat ( ID_User)
SELECT u.ID_User
FROM Users u
WHERE u.Roles = 'Perawat';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--PETUGAS ADMIN
INSERT INTO Petugas_Administrasi (ID_User)
SELECT u.ID_User
FROM Users u
WHERE u.Roles= 'Petugas Admin';

-- Insert data into Catatan_Vital table
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, id_perawat, Nomor_Rekam_Medis)
VALUES
('120/80', 170.00, 65.00, 36.50, 'Pusing dan lemas', 1, 'P0001RM'),
('110/70', 165.50, 55.00, 37.00, 'Demam dan sakit kepala', 2, 'P0002SN'),
('130/85', 175.00, 80.00, 36.80, 'Nyeri punggung', 3, 'P0003DR'),
('120/78', 160.00, 50.50, 37.20, 'Batuk dan pilek', 4, 'P0004LP'),
('125/80', 172.30, 68.20, 36.90, 'Sakit tenggorokan', 5, 'P1001AS'),
('115/75', 168.50, 60.00, 36.60, 'Pegal-pegal', 6, 'P1002MA'),
('135/90', 178.00, 90.00, 36.70, 'Sesak napas', 7, 'P1003BP'),
('120/80', 163.00, 58.50, 36.80, 'Sakit kepala ringan', 8, 'P1004NH'),
('118/76', 170.00, 62.00, 36.50, 'Gangguan pencernaan', 9, 'P2001ES'),
('110/70', 158.00, 48.00, 37.10, 'Demam dan batuk', 10, 'P2002RM'),
('140/95', 180.00, 95.00, 36.90, 'Nyeri dada', 11, 'P2003YK'),
('125/85', 160.00, 52.00, 36.70, 'Sakit kepala berat', 12, 'P3001TA'),
('128/82', 167.00, 63.50, 36.60, 'Pilek berkepanjangan', 13, 'P3002AR'),
('115/70', 155.00, 47.00, 36.80, 'Pusing setelah makan', 14, 'P3003AP'),
('130/80', 172.00, 68.00, 37.00, 'Nyeri sendi', 15, 'P4001FA'),
('118/76', 164.00, 58.00, 36.50, 'Sakit tenggorokan ringan', 16, 'P4002MI'),
('135/85', 176.00, 78.00, 36.90, 'Kram otot', 17, 'P4003DF');

-- Insert data into Jadwal_Dokter table
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES
-- Dokter Penyakit Dalam
(10, 'Senin', '08:00:00', '12:00:00', '013281.03.01.051792'),
(12, 'Rabu', '13:00:00', '16:00:00', '013281.03.01.051792'),
(12, 'Selasa', '09:00:00', '13:00:00', '013281.03.01.051743'),
(15, 'Kamis', '10:00:00', '14:00:00', '013281.03.01.051743'),
(15, 'Rabu', '08:00:00', '11:00:00', '013281.03.01.051784'),
(10, 'Jumat', '08:00:00', '12:00:00', '013281.03.01.051784'),
(8, 'Senin', '09:00:00', '11:00:00', '013281.03.01.051762'),
(10, 'Kamis', '10:00:00', '14:00:00', '013281.03.01.051762'),
(12, 'Selasa', '08:00:00', '11:00:00', '013281.03.01.051766'),
(15, 'Jumat', '13:00:00', '16:00:00', '013281.03.01.051766'),

-- Dokter Gigi
(10, 'Senin', '13:00:00', '17:00:00', '013281.01.01.054453'),
(12, 'Rabu', '10:00:00', '14:00:00', '013281.01.01.054453'),
(12, 'Selasa', '14:00:00', '18:00:00', '013281.01.01.054853'),
(15, 'Kamis', '08:00:00', '12:00:00', '013281.01.01.054853'),
(15, 'Rabu', '08:00:00', '11:00:00', '013281.01.01.054353'),
(10, 'Jumat', '10:00:00', '12:00:00', '013281.01.01.054353'),
(8, 'Senin', '09:00:00', '11:00:00', '013281.01.01.054903'),
(10, 'Kamis', '14:00:00', '16:00:00', '013281.01.01.054903'),
(12, 'Selasa', '10:00:00', '13:00:00', '013281.01.01.054978'),
(15, 'Jumat', '13:00:00', '17:00:00', '013281.01.01.054978'),

-- Dokter Mata
(8, 'Senin', '09:00:00', '12:00:00', '013281.02.01.051401'),
(10, 'Rabu', '14:00:00', '17:00:00', '013281.02.01.051401'),
(10, 'Selasa', '10:00:00', '14:00:00', '013281.02.01.051411'),
(12, 'Kamis', '09:00:00', '12:00:00', '013281.02.01.051411'),
(15, 'Rabu', '13:00:00', '16:00:00', '013281.02.01.051441'),
(8, 'Jumat', '07:00:00', '10:00:00', '013281.02.01.051441'),
(8, 'Senin', '10:00:00', '13:00:00', '013281.02.01.051422'),
(10, 'Kamis', '08:00:00', '12:00:00', '013281.02.01.051422'),
(12, 'Selasa', '09:00:00', '12:00:00', '013281.02.01.051442'),
(15, 'Jumat', '13:00:00', '16:00:00', '013281.02.01.051442'),

-- Dokter Anak
(15, 'Senin', '08:00:00', '12:00:00', '013281.08.01.051638'),
(10, 'Kamis', '14:00:00', '18:00:00', '013281.08.01.051638'),
(12, 'Selasa', '09:00:00', '13:00:00', '013281.08.01.051634'),
(15, 'Rabu', '10:00:00', '14:00:00', '013281.08.01.051634'),
(10, 'Rabu', '08:00:00', '11:00:00', '013281.08.01.051627'),
(8, 'Jumat', '08:00:00', '10:00:00', '013281.08.01.051627'),
(8, 'Senin', '13:00:00', '16:00:00', '013281.08.01.051621'),
(10, 'Kamis', '08:00:00', '12:00:00', '013281.08.01.051621'),
(12, 'Selasa', '08:00:00', '11:00:00', '013281.08.01.051611'),
(15, 'Jumat', '14:00:00', '17:00:00', '013281.08.01.051611');


-- Insert data into Diagnosa table
INSERT INTO Diagnosa (Keterangan, Nomor_Rekam_Medis, NPA)
VALUES
('Pusing dan lemas, tekanan darah normal. Kemungkinan vertigo ringan.', 'P0001RM', '013281.03.01.051792'),
('Demam dan sakit kepala, suhu tubuh tinggi. Diagnosa awal: infeksi virus.', 'P0002SN', '013281.03.01.051743'),
('Nyeri punggung, tekanan darah tinggi. Kemungkinan spondilosis atau nyeri otot.', 'P0003DR', '013281.03.01.051784'),
('Batuk dan pilek, suhu tubuh tinggi. Kemungkinan ISPA atau alergi.', 'P0004LP', '013281.03.01.051762'),
('Sakit tenggorokan, suhu tubuh sedikit meningkat. Diagnosa awal: radang tenggorokan.', 'P1001AS', '013281.03.01.051766'),
('Pegal-pegal, tekanan darah rendah. Kemungkinan kelelahan otot atau stres.', 'P1002MA', '013281.01.01.054453'),
('Sesak napas, tekanan darah tinggi. Kemungkinan asma atau hipertensi akut.', 'P1003BP', '013281.01.01.054853'),
('Sakit kepala ringan, tekanan darah normal. Kemungkinan migrain ringan.', 'P1004NH', '013281.02.01.051401'),
('Gangguan pencernaan, suhu tubuh normal. Diagnosa awal: gastritis.', 'P2001ES', '013281.02.01.051411'),
('Demam dan batuk, suhu tubuh tinggi. Diagnosa awal: bronkitis akut.', 'P2002RM', '013281.08.01.051638'),
('Nyeri dada, tekanan darah sangat tinggi. Diagnosa awal: angina pektoris.', 'P2003YK', '013281.08.01.051634'),
('Sakit kepala berat, tekanan darah tinggi. Kemungkinan hipertensi kronis.', 'P3001TA', '013281.08.01.051627'),
('Pilek berkepanjangan, tekanan darah sedikit tinggi. Diagnosa awal: sinusitis.', 'P3002AR', '013281.08.01.051621'),
('Pusing setelah makan, tekanan darah rendah. Kemungkinan hipoglikemia.', 'P3003AP', '013281.08.01.051611'),
('Nyeri sendi, tekanan darah normal. Kemungkinan arthritis ringan.', 'P4001FA', '013281.03.01.051792'),
('Sakit tenggorokan ringan, tekanan darah normal. Kemungkinan infeksi ringan.', 'P4002MI', '013281.03.01.051743'),
('Kram otot, tekanan darah tinggi. Kemungkinan dehidrasi atau kekurangan elektrolit.', 'P4003DF', '013281.03.01.051784');

-- Insert dummy data into Files_RiwayatMedis table
INSERT INTO Files_RiwayatMedis (File_Name, File_Path, id_perawat, Nomor_Rekam_Medis)
VALUES
('riwayat_medis_P0001RM.pdf', '/uploads/riwayat_medis_P0001RM.pdf', 1, 'P0001RM'),
('riwayat_medis_P0003DR.pdf', '/uploads/riwayat_medis_P0003DR.pdf', 3, 'P0003DR'),
('riwayat_medis_P1002MA.pdf', '/uploads/riwayat_medis_P1002MA.pdf', 6, 'P1002MA'),
('riwayat_medis_P1004NH.pdf', '/uploads/riwayat_medis_P1004NH.pdf', 8, 'P1004NH'),
('riwayat_medis_P2003YK.pdf', '/uploads/riwayat_medis_P2003YK.pdf', 11, 'P2003YK'),
('riwayat_medis_P3001TA.pdf', '/uploads/riwayat_medis_P3001TA.pdf', 12, 'P3001TA'),
('riwayat_medis_P4002MI.pdf', '/uploads/riwayat_medis_P4002MI.pdf', 16, 'P4002MI');

-- Insert dummy data into Buat_Janji table
-- Insert dummy data into Buat_Janji table
INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian)
VALUES
-- Pasien dengan 2 janji dalam satu hari
('2024-12-12', 'P0001RM', 1, 1),  -- Dokter pertama
('2024-12-12', 'P0001RM', 2, 2),  -- Dokter kedua

('2024-12-13', 'P0003DR', 3, 1),  -- Dokter pertama
('2024-12-13', 'P0003DR', 4, 2),  -- Dokter kedua

('2024-12-14', 'P1002MA', 5, 1),  -- Dokter pertama
('2024-12-14', 'P1002MA', 6, 2),  -- Dokter kedua

('2024-12-15', 'P2003YK', 7, 1),  -- Dokter pertama
('2024-12-15', 'P2003YK', 8, 2),  -- Dokter kedua

('2024-12-16', 'P3001TA', 9, 1),  -- Dokter pertama
('2024-12-16', 'P3001TA', 10, 2), -- Dokter kedua

-- Pasien dengan 1 janji dalam satu hari
('2024-12-12', 'P0002SN', 11, 1),
('2024-12-13', 'P0004LP', 12, 1),
('2024-12-14', 'P1001AS', 13, 1),
('2024-12-15', 'P1003BP', 14, 1),
('2024-12-16', 'P1004NH', 15, 1),
('2024-12-17', 'P2001ES', 16, 1),
('2024-12-17', 'P2002RM', 17, 1),
('2024-12-18', 'P3002AR', 18, 1),
('2024-12-18', 'P3003AP', 19, 1),
('2024-12-19', 'P4001FA', 20, 1),
('2024-12-19', 'P4002MI', 21, 1),
('2024-12-19', 'P4003DF', 22, 1);

-- Insert data ke tabel Transaksi
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT 
    'Lunas' AS Status_Pembayaran,
    bj.Tanggal_Janji AS Tanggal_Transaksi,
    SUM(d.Tarif) AS Jumlah_Pembayaran,
    bj.Nomor_Rekam_Medis,
    FLOOR(RANDOM() * 5 + 1)::INTEGER AS ID_Petugas_Admin  -- Random ID untuk Petugas Admin (1-5)
FROM 
    Buat_Janji bj
JOIN 
    Jadwal_Dokter jd ON bj.ID_Jadwal = jd.ID_Jadwal
JOIN 
    Dokter d ON jd.NPA = d.NPA
GROUP BY 
    bj.Nomor_Rekam_Medis, bj.Tanggal_Janji;