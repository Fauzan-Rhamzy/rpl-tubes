--BUAT DATA STYLE TANGGAL LAHIR
SHOW datestyle;
SET datestyle = 'DMY';

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

--PASIEN : Total 50 pasien
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
('nina_kusuma', 'nina456', 'Pasien', 'Nina Kusuma'),
('ronald_tobing', 'ronald789', 'Pasien', 'Ronald Tobing'),
('silvia_anjani', 'silvia321', 'Pasien', 'Silvia Anjani'),
('joko_santoso', 'joko123', 'Pasien', 'Joko Santoso'),
('widya_anggraini', 'widya456', 'Pasien', 'Widya Anggraini'),
('ferdiansyah_nur', 'ferdi789', 'Pasien', 'Ferdiansyah Nur'),
('kurnia_sari', 'kurnia321', 'Pasien', 'Kurnia Sari'),
('reza_maulana', 'reza123', 'Pasien', 'Reza Maulana'),
('dina_mariana', 'dina456', 'Pasien', 'Dina Mariana'),
('arif_budiman', 'arif789', 'Pasien', 'Arif Budiman'),
('mega_pratiwi', 'mega321', 'Pasien', 'Mega Pratiwi'),
('fitri_ayuningtyas', 'fitri123', 'Pasien', 'Fitri Ayuningtyas'),
('hendra_purwanto', 'hendra456', 'Pasien', 'Hendra Purwanto'),
('budi_pramudya', 'budi101', 'Pasien', 'Budi Pramudya'),
('yanti_suryani', 'yanti202', 'Pasien', 'Yanti Suryani'),
('ramli_zulkarnain', 'ramli303', 'Pasien', 'Ramli Zulkarnain'),
('citra_sulistyo', 'citra404', 'Pasien', 'Citra Sulistyo'),
('ikhsan_jusuf', 'ikhsan505', 'Pasien', 'Ikhsan Jusuf'),
('nina_surya', 'nina606', 'Pasien', 'Nina Surya'),
('tommy_haris', 'tommy707', 'Pasien', 'Tommy Haris'),
('tiwi_amalia', 'tiwi808', 'Pasien', 'Tiwi Amalia'),
('veronica_budiman', 'veronica909', 'Pasien', 'Veronica Budiman'),
('putra_sanjoyo', 'putra010', 'Pasien', 'Putra Sanjoyo'),
('yuliana_sari', 'yuliana111', 'Pasien', 'Yuliana Sari'),
('felix_aziz', 'felix212', 'Pasien', 'Felix Aziz'),
('steven_hendrawan', 'steven313', 'Pasien', 'Steven Hendrawan'),
('melvin_adi', 'melvin414', 'Pasien', 'Melvin Adi'),
('siska_rumahluhur', 'siska515', 'Pasien', 'Siska Rumahluhur'),
('alvin_setiawan', 'alvin616', 'Pasien', 'Alvin Setiawan'),
('marwan_santosa', 'marwan717', 'Pasien', 'Marwan Santosa'),
('linda_sari', 'linda818', 'Pasien', 'Linda Sari'),
('agung_wijaya', 'agung919', 'Pasien', 'Agung Wijaya'),
('susan_dwi', 'susan020', 'Pasien', 'Susan Dwi'),
('bayu_nugraha', 'bayu121', 'Pasien', 'Bayu Nugraha'),
('rina_wardani', 'rina222', 'Pasien', 'Rina Wardani'),
('daniel_tan', 'daniel323', 'Pasien', 'Daniel Tan'),

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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--ADMIN : Memasukkan data ke tabel Admin dan mengambil Nama dari tabel Users berdasarkan Role = 'Admin'
INSERT INTO Admins (ID_User, Nama)
SELECT ID_User, Nama
FROM Users
WHERE Roles = 'Admin';

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--DOKTER : Menambahkan dokter
--PENYAKIT DALAM
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.03.01.051792',   -- NPA (input oleh admin)
    'Penyakit Dalam',  -- Spesialisasi (input oleh admin)
    200000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_andreas'; --Username yang diinput Admin
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.03.01.051743',   
    'Penyakit Dalam',  
    300000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_maria';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.03.01.051784',   
    'Penyakit Dalam', 
    150000.00,  
    u.ID_User,  
    u.Nama      
FROM Users u
WHERE u.Username = 'dokter_fauziah';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.03.01.051762',   
    'Penyakit Dalam',  
    200000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_kevin';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.03.01.051766',   
    'Penyakit Dalam',  
    250000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_yuliana';

--GIGI
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.01.01.054453',   -- NPA (input oleh admin)
    'Gigi',  -- Spesialisasi (input oleh admin)
    199000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_alexsander';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.01.01.054853',   
    'Gigi',  
    150000.00,    
    u.ID_User,  
    u.Nama     
FROM Users u
WHERE u.Username = 'dokter_novita';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.01.01.054353',   
    'Gigi',  
    145000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_dian';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.01.01.054903',  
    'Gigi',  
    150000.00,    
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_amelia';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.01.01.054978',   
    'Gigi',  
    200000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_ronald';

--MATA
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.02.01.051401',   -- NPA (input oleh admin)
    'Mata',  -- Spesialisasi (input oleh admin)
    190000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_lukman';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.02.01.051411',  
    'Mata', 
    150000.00, 
    u.ID_User, 
    u.Nama     
FROM Users u
WHERE u.Username = 'dokter_silvia';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.02.01.051441',  
    'Mata', 
    200000.00, 
    u.ID_User, 
    u.Nama     
FROM Users u
WHERE u.Username = 'dokter_james';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.02.01.051422',  
    'Mata', 
    160000.00, 
    u.ID_User, 
    u.Nama     
FROM Users u
WHERE u.Username = 'dokter_angela';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.02.01.051442',  
    'Mata', 
    170000.00, 
    u.ID_User, 
    u.Nama     
FROM Users u
WHERE u.Username = 'dokter_felix';

--ANAK
--1
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.08.01.051638',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    100000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_reza';
--2
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.08.01.051634',  
    'Anak', 
    130000.00,
    u.ID_User,
    u.Nama    
FROM Users u
WHERE u.Username = 'dokter_nurul';
--3
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.08.01.051627',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    150000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_gabriel';
--4
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.08.01.051621',   -- NPA (input oleh admin)
    'Anak',  -- Spesialisasi (input oleh admin)
    180000.00,    -- Tarif (input oleh admin)
    u.ID_User,   -- ID_User diambil dari Users berdasarkan username
    u.Nama       -- Nama diambil dari Users berdasarkan username
FROM Users u
WHERE u.Username = 'dokter_jessica';
--5
INSERT INTO Dokter (NPA, Spesialisasi, Tarif, ID_User, Nama)
SELECT
    '013281.08.01.051611',  
    'Anak',  
    175000.00,   
    u.ID_User,   
    u.Nama       
FROM Users u
WHERE u.Username = 'dokter_alvina';
		
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Santosa, NO.121', --di input admin/pasien baru
    'Male', --di input admin/pasien baru
    '12/12/1998', --di input admin/pasien baru
    '081356789312' --di input admin/pasien baru
FROM Users u
WHERE u.Username = 'ahmad_fauzi';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Melati No.5',  -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '01/01/1995',         -- diinput admin/pasien baru
    '081234567890'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'siti_nurhaliza';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Raya No.23',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '05/07/1990',         -- diinput admin/pasien baru
    '081567890123'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'deni_ramadhan';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Mawar No.8',   -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '10/11/1992',         -- diinput admin/pasien baru
    '082134567890'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'lina_permata';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Jambu No.12',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '03/03/1985',         -- diinput admin/pasien baru
    '081987654321'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'agus_saputra';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Anggrek No.9', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '25/12/1990',         -- diinput admin/pasien baru
    '081276543210'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'maria_agnes';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kenanga No.3', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '15/06/1975',         -- diinput admin/pasien baru
    '081345678901'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'bambang_prasetyo';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Dahlia No.7',  -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '20/05/2000',         -- diinput admin/pasien baru
    '081678901234'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'nurul_hidayah';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Sawo No.10',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '09/09/1988',         -- diinput admin/pasien baru
    '081890123456'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'eko_susilo';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Cempaka No.2', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '02/02/1993',         -- diinput admin/pasien baru
    '081901234567'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'riana_maharani';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Cemara No.4',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '15/08/1987',         -- diinput admin/pasien baru
    '081345678901'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'yusuf_kurniawan';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Sakura No.6',  -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '20/02/1994',         -- diinput admin/pasien baru
    '081234567892'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'tiara_andini';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Merpati No.11',-- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '05/06/1990',         -- diinput admin/pasien baru
    '081456789012'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'andi_rahman';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Mawar No.7',   -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '12/03/1996',         -- diinput admin/pasien baru
    '081567890123'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'angela_putri';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kenanga No.8', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '10/10/1992',         -- diinput admin/pasien baru
    '081678901234'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'fikri_akbar';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Cendana No.2',-- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '08/09/1985',         -- diinput admin/pasien baru
    '081890123456'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'melati_indah';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Dahlia No.9',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '03/04/1991',         -- diinput admin/pasien baru
    '081901234567'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'dian_firmansyah';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Anggrek No.3', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '17/05/1997',         -- diinput admin/pasien baru
    '081234567891'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'nina_kusuma';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Jambu No.1',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '11/11/1980',         -- diinput admin/pasien baru
    '081567890124'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'ronald_tobing';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Sakura No.10',-- diinput admin/pasien baru
    'Female',            -- diinput admin/pasien baru
    '25/12/1993',        -- diinput admin/pasien baru
    '081234567893'       -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'silvia_anjani';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Durian No.5',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '18/09/1982',         -- diinput admin/pasien baru
    '081345678901'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'joko_santoso';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Anggrek No.2', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '12/05/1990',         -- diinput admin/pasien baru
    '081234567892'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'widya_anggraini';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Melati No.4',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '03/03/1991',         -- diinput admin/pasien baru
    '081456789012'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'ferdiansyah_nur';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Mawar No.1',   -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '15/02/1988',         -- diinput admin/pasien baru
    '081567890123'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'kurnia_sari';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Cemara No.7',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '20/10/1993',         -- diinput admin/pasien baru
    '081678901234'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'reza_maulana';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Jambu No.3',   -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '07/11/1986',         -- diinput admin/pasien baru
    '081890123456'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'dina_mariana';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Merpati No.8', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '12/04/1992',         -- diinput admin/pasien baru
    '081901234567'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'arif_budiman';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Sakura No.10',-- diinput admin/pasien baru
    'Female',            -- diinput admin/pasien baru
    '09/09/1995',        -- diinput admin/pasien baru
    '081234567891'       -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'mega_pratiwi';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Dahlia No.2', -- diinput admin/pasien baru
    'Female',            -- diinput admin/pasien baru
    '18/06/1998',        -- diinput admin/pasien baru
    '081345678902'       -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'fitri_ayuningtyas';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kenanga No.9',-- diinput admin/pasien baru
    'Male',              -- diinput admin/pasien baru
    '30/12/1990',        -- diinput admin/pasien baru
    '081567890124'       -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'hendra_purwanto';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Mangga No.7',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '01/01/1980',         -- diinput admin/pasien baru
    '081234567890'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'budi_pramudya';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Melon No.9',   -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '10/05/1985',         -- diinput admin/pasien baru
    '081345678901'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'yanti_suryani';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Jeruk No.3',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '15/08/1990',         -- diinput admin/pasien baru
    '081456789012'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'ramli_zulkarnain';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Semangka No.2', -- diinput admin/pasien baru
    'Female',              -- diinput admin/pasien baru
    '07/03/1988',          -- diinput admin/pasien baru
    '081567890123'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'citra_sulistyo';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Alpukat No.5', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '22/11/1992',         -- diinput admin/pasien baru
    '081678901234'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'ikhsan_jusuf';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Pisang No.8',  -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '30/07/1991',         -- diinput admin/pasien baru
    '081890123456'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'nina_surya';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Pepaya No.10', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '09/12/1986',         -- diinput admin/pasien baru
    '081901234567'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'tommy_haris';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Duku No.6',    -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '17/06/1993',         -- diinput admin/pasien baru
    '081234567891'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'tiwi_amalia';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Manggis No.4', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '14/02/1997',         -- diinput admin/pasien baru
    '081345678902'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'veronica_budiman';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kelapa No.11', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '25/09/1995',         -- diinput admin/pasien baru
    '081567890124'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'putra_sanjoyo';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Durian No.12', -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '11/11/1993',         -- diinput admin/pasien baru
    '081123456789'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'yuliana_sari';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Salak No.9',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '12/02/1989',         -- diinput admin/pasien baru
    '081234567892'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'felix_aziz';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Sawo No.15',   -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '21/04/1990',         -- diinput admin/pasien baru
    '081345678903'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'steven_hendrawan';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Duku No.8',    -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '18/03/1995',         -- diinput admin/pasien baru
    '081456789904'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'melvin_adi';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Apel No.5',    -- diinput admin/pasien baru
    'Female',             -- diinput admin/pasien baru
    '07/09/1996',         -- diinput admin/pasien baru
    '081567890905'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'siska_rumahluhur';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Melati No.13', -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '28/06/1988',         -- diinput admin/pasien baru
    '081678901906'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'alvin_setiawan';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Rambutan No.7', -- diinput admin/pasien baru
    'Male',                -- diinput admin/pasien baru
    '11/05/1992',          -- diinput admin/pasien baru
    '081789012345'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'marwan_santosa';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Nangka No.3',   -- diinput admin/pasien baru
    'Female',              -- diinput admin/pasien baru
    '15/08/1993',          -- diinput admin/pasien baru
    '081890123456'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'linda_sari';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Jeruk No.11',   -- diinput admin/pasien baru
    'Male',                -- diinput admin/pasien baru
    '22/12/1990',          -- diinput admin/pasien baru
    '081901234567'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'agung_wijaya';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kelapa No.4',   -- diinput admin/pasien baru
    'Female',              -- diinput admin/pasien baru
    '09/03/1994',          -- diinput admin/pasien baru
    '081234567898'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'susan_dwi';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Mawar No.20',  -- diinput admin/pasien baru
    'Male',               -- diinput admin/pasien baru
    '15/07/1991',         -- diinput admin/pasien baru
    '081234567899'        -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'bayu_nugraha';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Kenanga No.18', -- diinput admin/pasien baru
    'Female',              -- diinput admin/pasien baru
    '22/11/1993',          -- diinput admin/pasien baru
    '081345678900'         -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'rina_wardani';

INSERT INTO Pasien (ID_User, Nama, Alamat, Gender, Tanggal_Lahir, Kontak)
SELECT 
    u.ID_User,
    u.Nama,
    'Jalan Flamboyan No.9', -- diinput admin/pasien baru
    'Male',                 -- diinput admin/pasien baru
    '10/05/1995',           -- diinput admin/pasien baru
    '081456789901'          -- diinput admin/pasien baru
FROM Users u
WHERE u.Username = 'daniel_tan';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- PERAWAT : 
INSERT INTO Perawat (Nama, ID_User)
SELECT u.Nama, u.ID_User
FROM Users u
WHERE u.Roles = 'Perawat';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--PETUGAS ADMIN
INSERT INTO Petugas_Administrasi (Nama, ID_User)
SELECT u.Nama, u.ID_User
FROM Users u
WHERE u.Roles= 'Petugas Admin';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- CATATAN VITAL : YANG DIMASUKKAN CATATAN VITAL 20 PASIEN AJA
-- Pasien 1: Ahmad Fauzi
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '130/85',              -- Tekanan Darah
    175.00,                -- Tinggi Badan
    72.00,                 -- Berat Badan
    36.6,                  -- Suhu Badan
    'Merasa sakit pada bagian perut yang cukup mengganggu dan berlangsung beberapa jam terakhir. Gejala ini semakin terasa setelah makan makanan yang sedikit pedas.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ahmad_fauzi';

-- Pasien 2: Siti Nurhaliza
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '125/80',              -- Tekanan Darah
    160.00,                -- Tinggi Badan
    60.00,                 -- Berat Badan
    36.8,                  -- Suhu Badan
    'Mengalami pusing kepala yang cukup berat disertai dengan rasa mual. Kondisi ini mulai terasa setelah bangun tidur dan berlangsung sepanjang hari.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'siti_nurhaliza';

-- Pasien 3: Deni Ramadhan
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '120/75',              -- Tekanan Darah
    168.00,                -- Tinggi Badan
    68.00,                 -- Berat Badan
    36.7,                  -- Suhu Badan
    'Mengalami rasa lelah yang sangat setelah beraktivitas seharian. Kondisi ini tidak kunjung membaik meskipun sudah beristirahat.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'deni_ramadhan';

-- Pasien 4: Lina Permata
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '135/85',              -- Tekanan Darah
    162.00,                -- Tinggi Badan
    62.50,                 -- Berat Badan
    36.5,                  -- Suhu Badan
    'Merasakan nyeri pada beberapa bagian sendi, terutama di bagian lutut dan pergelangan tangan. Nyeri ini datang secara tiba-tiba dan cukup mengganggu aktivitas.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'lina_permata';

-- Pasien 5: Agus Saputra
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '128/80',              -- Tekanan Darah
    170.00,                -- Tinggi Badan
    75.00,                 -- Berat Badan
    37.0,                  -- Suhu Badan
    'Mengalami sakit kepala yang sangat berat dan berdenyut, terutama di bagian dahi. Rasa sakit ini disertai dengan mual dan sangat mengganggu konsentrasi.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'agus_saputra';

-- Pasien 6: Maria Agnes
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '130/85',              -- Tekanan Darah
    155.00,                -- Tinggi Badan
    58.00,                 -- Berat Badan
    36.9,                  -- Suhu Badan
    'Batuk yang berlangsung cukup lama dan disertai dengan flu yang membuat tubuh terasa sangat lemas. Gejala ini semakin parah pada malam hari dan sangat mengganggu tidur.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'maria_agnes';

-- Pasien 7: Bambang Prasetyo
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '140/90',              -- Tekanan Darah
    175.00,                -- Tinggi Badan
    80.00,                 -- Berat Badan
    36.8,                  -- Suhu Badan
    'Merasa mual yang datang secara tiba-tiba, disertai dengan rasa pusing yang sangat mengganggu dan sulit untuk berdiri dalam waktu lama.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'bambang_prasetyo';

-- Pasien 8: Nurul Hidayah
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '120/80',              -- Tekanan Darah
    162.00,                -- Tinggi Badan
    62.00,                 -- Berat Badan
    36.6,                  -- Suhu Badan
    'Merasa nyeri pada bagian punggung bawah setelah melakukan aktivitas berat seharian. Nyeri ini cukup mengganggu dan tidak hilang meskipun sudah beristirahat.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nurul_hidayah';

-- Pasien 9: Eko Susilo
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '130/85',              -- Tekanan Darah
    180.00,                -- Tinggi Badan
    85.00,                 -- Berat Badan
    37.0,                  -- Suhu Badan
    'Mengalami sakit kepala yang sangat intens dan tubuh terasa sangat lelah, membuat sulit untuk beraktivitas secara normal. Sakit kepala ini datang secara tiba-tiba dan berlangsung lama.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'eko_susilo';

-- Pasien 10: Riana Maharani
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '125/80',              -- Tekanan Darah
    155.00,                -- Tinggi Badan
    55.00,                 -- Berat Badan
    36.7,                  -- Suhu Badan
    'Mengalami rasa lelah yang berkepanjangan, meskipun sudah tidur cukup lama. Rasa lelah ini disertai dengan sedikit pusing dan kehilangan nafsu makan.',  -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'riana_maharani';

-- Pasien 11: Yusuf Kurniawan
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '130/85',              -- Tekanan Darah
    168.00,                -- Tinggi Badan
    70.50,                 -- Berat Badan
    36.7,                  -- Suhu Badan
    'Mengalami sedikit pusing di pagi hari, tetapi tidak terlalu mengganggu aktivitas.',   -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'yusuf_kurniawan';

-- Pasien 12: Tiara Andini
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '125/80',              -- Tekanan Darah
    160.50,                -- Tinggi Badan
    55.00,                 -- Berat Badan
    36.8,                  -- Suhu Badan
    'Mengeluh merasa mual dan sering pusing terutama saat berdiri terlalu lama, terasa sedikit lemas.',     -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'tiara_andini';

-- Pasien 13: Andi Rahman
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '120/75',              -- Tekanan Darah
    170.00,                -- Tinggi Badan
    72.00,                 -- Berat Badan
    37.0,                  -- Suhu Badan
    'Merasa sedikit pegal di bagian punggung bawah dan leher setelah aktivitas fisik yang cukup berat.',   -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'andi_rahman';

-- Pasien 14: Angela Putri
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '135/88',              -- Tekanan Darah
    165.00,                -- Tinggi Badan
    65.50,                 -- Berat Badan
    36.6,                  -- Suhu Badan
    'Mengalami nyeri kepala yang cukup mengganggu, terutama pada bagian dahi dan pelipis.',        -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'angela_putri';

-- Pasien 15: Fikri Akbar
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '128/80',              -- Tekanan Darah
    173.00,                -- Tinggi Badan
    74.50,                 -- Berat Badan
    36.9,                  -- Suhu Badan
    'Sering merasa pusing dan mual, terutama setelah makan, serta merasa kelelahan lebih cepat dari biasanya.',     -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'fikri_akbar';

-- Pasien 16: Melati Indah
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '125/78',              -- Tekanan Darah
    160.00,                -- Tinggi Badan
    58.00,                 -- Berat Badan
    36.5,                  -- Suhu Badan
    'Merasa lelah dan sedikit pusing, terutama setelah bekerja terlalu lama di depan layar komputer.',               -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'melati_indah';

-- Pasien 17: Dian Firmansyah
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '140/90',              -- Tekanan Darah
    167.00,                -- Tinggi Badan
    78.50,                 -- Berat Badan
    37.0,                  -- Suhu Badan
    'Mengalami sakit kepala yang sangat berat, terutama di area belakang kepala, disertai dengan pusing yang sangat mengganggu.',        -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'dian_firmansyah';

-- Pasien 18: Nina Kusuma
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '118/76',              -- Tekanan Darah
    162.00,                -- Tinggi Badan
    63.00,                 -- Berat Badan
    36.7,                  -- Suhu Badan
    'Sering merasa pusing dan lemas, terutama setelah beraktivitas berat atau setelah berdiri terlalu lama.',              -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nina_kusuma';

-- Pasien 19: Ronald Tobing
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '132/85',              -- Tekanan Darah
    180.00,                -- Tinggi Badan
    80.00,                 -- Berat Badan
    36.9,                  -- Suhu Badan
    'Mengalami nyeri punggung bagian bawah yang sangat mengganggu, serta kesulitan tidur karena rasa sakit tersebut.',      -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ronald_tobing';

-- Pasien 20: Silvia Anjani
INSERT INTO Catatan_Vital (Tekanan_Darah, Tinggi_Badan, Berat_Badan, Suhu_Badan, Keluhan, Nomor_Rekam_Medis)
SELECT 
    '120/80',              -- Tekanan Darah
    155.00,                -- Tinggi Badan
    50.50,                 -- Berat Badan
    36.5,                  -- Suhu Badan
    'Tidak ada keluhan yang berarti, hanya merasa sedikit lelah setelah beraktivitas seharian.',   -- Keluhan
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'silvia_anjani';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--JADWAL DOKTER
-- dr. Andreas Siregar, SpPD
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Senin', '08:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Selasa', '08:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Rabu', '08:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Kamis', '08:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Jumat', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Sabtu', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Minggu', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Andreas Siregar, SpPD'));

-- dr. Maria Eva, SpPD
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Senin', '08:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Selasa', '08:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (25, 'Rabu', '10:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (25, 'Kamis', '10:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (15, 'Jumat', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Sabtu', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Minggu', '13:00', '15:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Maria Eva, SpPD'));

-- dr. Fauziah Heny, SpPD
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Senin', '13:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Selasa', '13:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (25, 'Rabu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (25, 'Kamis', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (20, 'Jumat', '13:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Sabtu', '08:00', '11:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Minggu', '08:00', '11:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Fauziah Heny, SpPD'));

-- dr. Kevin Wibisono, SpPD
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (15, 'Senin', '08:00', '10:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (15, 'Selasa', '10:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Rabu', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Kamis', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (15, 'Jumat', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Sabtu', '13:00', '15:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Minggu', '14:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Kevin Wibisono, SpPD'));

-- dr. Yuliana Kurniawan, SpPD
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (12, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Selasa', '09:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (15, 'Rabu', '10:00', '16:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (8, 'Kamis', '07:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (18, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (14, 'Sabtu', '08:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES (10, 'Minggu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Yuliana Kurniawan, SpPD'));

-- **Dokter Gigi: drg. Alexander Tampubolon**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(8, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(10, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(6, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(12, 'Kamis', '08:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(9, 'Jumat', '14:00', '18:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(10, 'Sabtu', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon')),
(8, 'Minggu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Alexander Tampubolon'));

-- **Dokter Gigi: drg. Novita Afni**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(12, 'Senin', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(10, 'Selasa', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(8, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(15, 'Kamis', '07:30', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(9, 'Jumat', '13:30', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(7, 'Sabtu', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni')),
(10, 'Minggu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Novita Afni'));


-- **Dokter Gigi: drg. Dian Prasetyo**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(11, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(9, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(8, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(14, 'Kamis', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(12, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(10, 'Sabtu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo')),
(9, 'Minggu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Dian Prasetyo'));


-- **Dokter Gigi: drg. Amelia Wijaya**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(9, 'Senin', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(12, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(10, 'Rabu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(8, 'Kamis', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(14, 'Jumat', '13:30', '17:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(7, 'Sabtu', '09:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya')),
(11, 'Minggu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Amelia Wijaya'));


-- **Dokter Gigi: drg. Ronald Hutapea**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(12, 'Senin', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(10, 'Selasa', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(8, 'Rabu', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(10, 'Kamis', '09:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(7, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(6, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea')),
(9, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'drg. Ronald Hutapea'));

-- **Dokter Mata: dr. Lukman Hakim, SpM(K)**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(10, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(12, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(8, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(15, 'Kamis', '07:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(14, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(10, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)')),
(11, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Lukman Hakim, SpM(K)'));


-- **Dokter Mata: dr. Silvia Tjandra, SpM**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(12, 'Senin', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(10, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(9, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(14, 'Kamis', '07:30', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(10, 'Jumat', '13:30', '17:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(8, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM')),
(12, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Silvia Tjandra, SpM'));


-- **Dokter Mata: dr. James Kusuma, SpM**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(14, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(12, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(10, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(13, 'Kamis', '07:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(9, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(11, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM')),
(10, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. James Kusuma, SpM'));


-- **Dokter Mata: dr. Angela Putri, SpM**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(12, 'Senin', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(14, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(9, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(13, 'Kamis', '07:30', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(10, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(8, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM')),
(12, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Angela Putri, SpM'));


-- **Dokter Mata: dr. Felix Sudarmono, SpM**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(10, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(12, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(11, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(15, 'Kamis', '07:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(13, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(9, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM')),
(10, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Felix Sudarmono, SpM'));

-- **Dokter Anak: dr. Reza Mahendra, SpA**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(12, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(10, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(8, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(15, 'Kamis', '07:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(12, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(10, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA')),
(14, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Reza Mahendra, SpA'));


-- **Dokter Anak: dr. Nurul Arifah, SpA**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(10, 'Senin', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(12, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(9, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(14, 'Kamis', '07:30', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(13, 'Jumat', '13:30', '17:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(12, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA')),
(10, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Nurul Arifah, SpA'));


-- **Dokter Anak: dr. Gabriel Manulang, SpA**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(11, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(13, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(12, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(10, 'Kamis', '07:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(9, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(14, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA')),
(13, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Gabriel Manulang, SpA'));


-- **Dokter Anak: dr. Jessica Anggraeni, SpA**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(14, 'Senin', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(13, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(11, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(12, 'Kamis', '07:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(10, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(14, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA')),
(12, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Jessica Anggraeni, SpA'));


-- **Dokter Anak: dr. Alvina Tarigan, SpA**
INSERT INTO Jadwal_Dokter (Kuota_Pasien, Hari, Jam_Mulai, Jam_Selesai, NPA)
VALUES 
(10, 'Senin', '08:30', '12:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(9, 'Selasa', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(12, 'Rabu', '10:00', '14:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(11, 'Kamis', '07:30', '13:30', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(14, 'Jumat', '13:00', '17:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(12, 'Sabtu', '08:00', '12:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA')),
(13, 'Minggu', '09:00', '13:00', (SELECT NPA FROM Dokter WHERE Nama = 'dr. Alvina Tarigan, SpA'));

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--RIWAYAT MEDIS : ISINYA 20 DATA dari 20 PASIEN
-- 1. Riwayat Medis untuk Pasien 'Ahmad Fauzi' (username: ahmad_fauzi)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pertama pasien dengan keluhan umum dan gejala ringan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ahmad_fauzi';

-- 2. Riwayat Medis untuk Pasien 'Siti Nurhaliza' (username: siti_nurhaliza)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pemeriksaan rutin dengan keluhan pusing dan lemas', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'siti_nurhaliza';

-- 3. Riwayat Medis untuk Pasien 'Deni Ramadhan' (username: deni_ramadhan)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa dengan keluhan batuk berkepanjangan disertai sesak napas', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'deni_ramadhan';

-- 4. Riwayat Medis untuk Pasien 'Lina Permata' (username: lina_permata)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pasien datang dengan keluhan nyeri sendi dan pembengkakan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'lina_permata';

-- 5. Riwayat Medis untuk Pasien 'Agus Saputra' (username: agus_saputra)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pasien dengan keluhan demam tinggi dan nyeri tubuh', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'agus_saputra';

-- 6. Riwayat Medis untuk Pasien 'Maria Agnes' (username: maria_agnes)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pasien dengan keluhan sakit kepala hebat dan mual', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'maria_agnes';

-- 7. Riwayat Medis untuk Pasien 'Bambang Prasetyo' (username: bambang_prasetyo)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa dengan keluhan sakit perut dan tidak nafsu makan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'bambang_prasetyo';

-- 8. Riwayat Medis untuk Pasien 'Nurul Hidayah' (username: nurul_hidayah)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pasien mengalami gejala demam dan sakit tenggorokan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nurul_hidayah';

-- 9. Riwayat Medis untuk Pasien 'Eko Susilo' (username: eko_susilo)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pasien dengan keluhan pusing', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'eko_susilo';

-- 10. Riwayat Medis untuk Pasien 'Riana Maharani' (username: riana_maharani)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Diagnosa pasien dengan keluhan sesak napas', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'riana_maharani';

-- 11. Riwayat Medis untuk Pasien 'Yusuf Kurniawan' (username: yusuf_kurniawan)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pemeriksaan rutin dengan keluhan kelelahan berlebih', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'yusuf_kurniawan';

-- 12. Riwayat Medis untuk Pasien 'Tiara Andini' (username: tiara_andini)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Keluhan mual, pusing, dan nyeri perut', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'tiara_andini';

-- 13. Riwayat Medis untuk Pasien 'Andi Rahman' (username: andi_rahman)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pasien datang dengan keluhan nyeri dada dan sulit bernafas', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'andi_rahman';

-- 14. Riwayat Medis untuk Pasien 'Angela Putri' (username: angela_putri)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pasien mengeluh nyeri pada persendian dan kelelahan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'angela_putri';

-- 15. Riwayat Medis untuk Pasien 'Fikri Akbar' (username: fikri_akbar)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Keluhan pusing dan penglihatan kabur', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'fikri_akbar';

-- 16. Riwayat Medis untuk Pasien 'Melati Indah' (username: melati_indah)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Keluhan mual dan perasaan tidak enak badan', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'melati_indah';

-- 17. Riwayat Medis untuk Pasien 'Dian Firmansyah' (username: dian_firmansyah)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Keluhan demam dan pusing disertai batuk', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'dian_firmansyah';

-- 18. Riwayat Medis untuk Pasien 'Nina Kusuma' (username: nina_kusuma)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pemeriksaan rutin dengan keluhan pusing dan gangguan tidur', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nina_kusuma';

-- 19. Riwayat Medis untuk Pasien 'Ronald Tobing' (username: ronald_tobing)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Keluhan sesak napas dan batuk', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ronald_tobing';

-- 20. Riwayat Medis untuk Pasien 'Silvia Anjani' (username: silvia_anjani)
INSERT INTO Riwayat_Medis (Keterangan, Nomor_Rekam_Medis)
SELECT 
    'Pasien mengeluh sakit tenggorokan dan demam', 
    p.Nomor_Rekam_Medis
FROM Pasien p
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'silvia_anjani';


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--FILE RIWAYAT MEDIS
-- 1. Menambahkan file riwayat medis untuk Pasien 'Ahmad Fauzi' (username: ahmad_fauzi)
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_ahmad_fauzi.pdf',  
    '/SehatBroKlinik/Diagnosa/Ahmad_Fauzi/diagnosa_ahmad_fauzi.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ahmad_fauzi';

-- Menambahkan file riwayat medis untuk 19 pasien
-- 2. Pasien 'Siti Nurhaliza'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_siti_nurhaliza.pdf',  
    '/SehatBroKlinik/Diagnosa/Siti_Nurhaliza/diagnosa_siti_nurhaliza.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'siti_nurhaliza';

-- 3. Pasien 'Deni Ramadhan'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_deni_ramadhan.pdf',  
    '/SehatBroKlinik/Diagnosa/Deni_Ramadhan/diagnosa_deni_ramadhan.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'deni_ramadhan';

-- 4. Pasien 'Lina Permata'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_lina_permata.pdf',  
    '/SehatBroKlinik/Diagnosa/Lina_Permata/diagnosa_lina_permata.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'lina_permata';

-- 5. Pasien 'Agus Saputra'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_agus_saputra.pdf',  
    '/SehatBroKlinik/Diagnosa/Agus_Saputra/diagnosa_agus_saputra.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'agus_saputra';

-- 6. Pasien 'Maria Agnes'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_maria_agnes.pdf',  
    '/SehatBroKlinik/Diagnosa/Maria_Agnes/diagnosa_maria_agnes.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'maria_agnes';

-- 7. Pasien 'Bambang Prasetyo'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_bambang_prasetyo.pdf',  
    '/SehatBroKlinik/Diagnosa/Bambang_Prasetyo/diagnosa_bambang_prasetyo.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'bambang_prasetyo';

-- 8. Pasien 'Nurul Hidayah'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_nurul_hidayah.pdf',  
    '/SehatBroKlinik/Diagnosa/Nurul_Hidayah/diagnosa_nurul_hidayah.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nurul_hidayah';

-- 9. Pasien 'Eko Susilo'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_eko_susilo.pdf',  
    '/SehatBroKlinik/Diagnosa/Eko_Susilo/diagnosa_eko_susilo.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'eko_susilo';

-- 10. Pasien 'Riana Maharani'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_riana_maharani.pdf',  
    '/SehatBroKlinik/Diagnosa/Riana_Maharani/diagnosa_riana_maharani.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'riana_maharani';

-- 11. Pasien 'Yusuf Kurniawan'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_yusuf_kurniawan.pdf',  
    '/SehatBroKlinik/Diagnosa/Yusuf_Kurniawan/diagnosa_yusuf_kurniawan.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'yusuf_kurniawan';

-- 12. Pasien 'Tiara Andini'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_tiara_andini.pdf',  
    '/SehatBroKlinik/Diagnosa/Tiara_Andini/diagnosa_tiara_andini.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'tiara_andini';

-- 13. Pasien 'Andi Rahman'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_andi_rahman.pdf',  
    '/SehatBroKlinik/Diagnosa/Andi_Rahman/diagnosa_andi_rahman.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'andi_rahman';

-- 14. Pasien 'Angela Putri'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_angela_putri.pdf',  
    '/SehatBroKlinik/Diagnosa/Angela_Putri/diagnosa_angela_putri.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'angela_putri';

-- 15. Pasien 'Fikri Akbar'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_fikri_akbar.pdf',  
    '/SehatBroKlinik/Diagnosa/Fikri_Akbar/diagnosa_fikri_akbar.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'fikri_akbar';

-- 16. Pasien 'Melati Indah'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_melati_indah.pdf',  
    '/SehatBroKlinik/Diagnosa/Melati_Indah/diagnosa_melati_indah.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'melati_indah';

-- 17. Pasien 'Dian Firmansyah'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_dian_firmansyah.pdf',  
    '/SehatBroKlinik/Diagnosa/Dian_Firmansyah/diagnosa_dian_firmansyah.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'dian_firmansyah';

-- 18. Pasien 'Nina Kusuma'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_nina_kusuma.pdf',  
    '/SehatBroKlinik/Diagnosa/Nina_Kusuma/diagnosa_nina_kusuma.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'nina_kusuma';

-- 19. Pasien 'Ronald Tobing'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_ronald_tobing.pdf',  
    '/SehatBroKlinik/Diagnosa/Ronald_Tobing/diagnosa_ronald_tobing.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'ronald_tobing';

-- 20. Pasien 'Silvia Anjani'
INSERT INTO Files_RiwayatMedis (ID_Diagnosa, File_Name, File_Path)
SELECT 
    rm.ID_Diagnosa,
    'diagnosa_silvia_anjani.pdf',  
    '/SehatBroKlinik/Diagnosa/Silvia_Anjani/diagnosa_silvia_anjani.pdf' 
FROM Riwayat_Medis rm
JOIN Pasien p ON rm.Nomor_Rekam_Medis = p.Nomor_Rekam_Medis
JOIN Users u ON p.ID_User = u.ID_User
WHERE u.Username = 'silvia_anjani';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- TRANSAKSI 
-- 1. Pasien: Ahmad Fauzi, Dokter: dr. Andreas Siregar, SpPD, Admin: Rizki Amelia
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-01',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Andreas Siregar, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rizki')
WHERE p.Nama = 'Ahmad Fauzi';

-- 2. Pasien: Siti Nurhaliza, Dokter: dr. Maria Eva, SpPD, Admin: Hendra Wijaya
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-02',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Maria Eva, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_hendra')
WHERE p.Nama = 'Siti Nurhaliza';

-- 3. Pasien: Deni Ramadhan, Dokter: dr. Fauziah Heny, SpPD, Admin: Amelia Yuliana
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-03',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Fauziah Heny, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_amelia')
WHERE p.Nama = 'Deni Ramadhan';

-- 4. Pasien: Lina Permata, Dokter: dr. Kevin Wibisono, SpPD, Admin: Rian Setiawan
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-04',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Kevin Wibisono, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rian')
WHERE p.Nama = 'Lina Permata';

-- 5. Pasien: Agus Saputra, Dokter: dr. Yuliana Kurniawan, SpPD, Admin: Dian Prakoso
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-05',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Yuliana Kurniawan, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_dian')
WHERE p.Nama = 'Agus Saputra';

-- 6. Pasien: Maria Agnes, Dokter: drg. Alexander Tampubolon, Admin: Silvia Hartono
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-06',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Alexander Tampubolon'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_silvia')
WHERE p.Nama = 'Maria Agnes';

-- 7. Pasien: Bambang Prasetyo, Dokter: drg. Novita Afni, Admin: Firman Sutrisno
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-07',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Novita Afni'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_firman')
WHERE p.Nama = 'Bambang Prasetyo';

-- 8. Pasien: Nurul Hidayah, Dokter: drg. Dian Prasetyo, Admin: Linda Pratiwi
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-08',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Dian Prasetyo'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_linda')
WHERE p.Nama = 'Nurul Hidayah';

-- 9. Pasien: Eko Susilo, Dokter: drg. Amelia Wijaya, Admin: Rizki Amelia
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-09',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Amelia Wijaya'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rizki')
WHERE p.Nama = 'Eko Susilo';

-- 10. Pasien: Riana Maharani, Dokter: drg. Ronald Hutapea, Admin: Hendra Wijaya
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-10',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Ronald Hutapea'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_hendra')
WHERE p.Nama = 'Riana Maharani';

-- 11. Pasien: Yusuf Kurniawan, Dokter: dr. Lukman Hakim, SpM(K), Admin: Amelia Yuliana
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-11',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Lukman Hakim, SpM(K)'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_amelia')
WHERE p.Nama = 'Yusuf Kurniawan';

-- 12. Pasien: Tiara Andini, Dokter: dr. Silvia Tjandra, SpM, Admin: Rian Setiawan
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-12',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Silvia Tjandra, SpM'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rian')
WHERE p.Nama = 'Tiara Andini';

-- 13. Pasien: Andi Rahman, Dokter: dr. James Kusuma, SpM, Admin: Dian Prakoso
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-13',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. James Kusuma, SpM'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_dian')
WHERE p.Nama = 'Andi Rahman';

-- 14. Pasien: Angela Putri, Dokter: dr. Angela Putri, SpM, Admin: Silvia Hartono
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-14',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Angela Putri, SpM'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_silvia')
WHERE p.Nama = 'Angela Putri';

-- 15. Pasien: Fikri Akbar, Dokter: dr. Angela Putri, SpM, Admin: Linda Pratiwi
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-15',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Angela Putri, SpM'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_linda')
WHERE p.Nama = 'Fikri Akbar';

-- 16. Pasien: Melati Indah, Dokter: dr. Kevin Wibisono, SpPD, Admin: Rian Setiawan
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-16',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Kevin Wibisono, SpPD'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rian')
WHERE p.Nama = 'Melati Indah';

-- 17. Pasien: Dian Firmansyah, Dokter: drg. Novita Afni, Admin: Rizki Amelia
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-17',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Novita Afni'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_rizki')
WHERE p.Nama = 'Dian Firmansyah';

-- 18. Pasien: Nina Kusuma, Dokter: dr. Nurul Arifah, SpA, Admin: Silvia Hartono
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-18',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Nurul Arifah, SpA'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_silvia')
WHERE p.Nama = 'Nina Kusuma';

-- 19. Pasien: Ronald Tobing, Dokter: dr. Reza Mahendra, SpA, Admin: Firman Sutrisno
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-19',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'dr. Reza Mahendra, SpA'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_firman')
WHERE p.Nama = 'Ronald Tobing';

-- 20. Pasien: Silvia Anjani, Dokter: drg. Amelia Wijaya, Admin: Dian Prakoso
INSERT INTO Transaksi (Status_Pembayaran, Tanggal_Transaksi, Jumlah_Pembayaran, Nomor_Rekam_Medis, ID_Petugas_Admin)
SELECT
    'Lunas',
    '2024-12-20',
    d.Tarif,
    p.Nomor_Rekam_Medis,
    pa.ID_Petugas_Admin
FROM Pasien p
JOIN Dokter d ON d.Nama = 'drg. Amelia Wijaya'
JOIN Petugas_Administrasi pa ON pa.ID_User = (SELECT ID_User FROM Users WHERE Username = 'admin_dian')
WHERE p.Nama = 'Silvia Anjani';

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--BUAT JANJI
-- Ambil nomor rekam medis berdasarkan nama pasien dan insert ke Buat_Janji
-- Misalkan dokter tersedia di jadwal Senin (ID_Jadwal = 1) dan Selasa (ID_Jadwal = 2)

-- Pasien 1 dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Joko Santoso'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Pasien 2 dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Widya Anggraini'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Pasien 3 dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Ferdiansyah Nur'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Pasien 4 dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Kurnia Sari'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien kelima dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Reza Maulana'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien keenam dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Dina Mariana'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ketujuh dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Arif Budiman'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien kedelapan dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Mega Pratiwi'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien kesembilan dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Fitri Ayuningtyas'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien kesepuluh dengan penambahan counts otomatis
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Hendra Purwanto'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-11'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-11', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-11 
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Budi Pramudya'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 1 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 1 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 1, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-12 
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Yanti Suryani'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 2 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 2 AND Hari = 'Selasa'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 2 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 2, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-13
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Ramli Zulkarnain'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 3 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 3 AND Hari = 'Rabu'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 3 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 3, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;
	
-- Insert pasien ke-14
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Citra Sulistyo'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 4 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 4 AND Hari = 'Kamis'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 4 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 4, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-15
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Ikhsan Jusuf'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 5 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 5 AND Hari = 'Jumat'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 5 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 5, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-16
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Nina Surya'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 6 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 6 AND Hari = 'Sabtu'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 6 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 6, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-17
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Tommy Haris'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 7 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 7 AND Hari = 'Minggu'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 7 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 7, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-18
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Tiwi Amalia'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 8 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 8 AND Hari = 'Senin'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 8 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 8, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-19
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Veronica Budiman'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 9 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 9 AND Hari = 'Selasa'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 9 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 9, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;

-- Insert pasien ke-20
	WITH pasien_data AS (
	  SELECT Nomor_Rekam_Medis
	  FROM Pasien
	  WHERE nama = 'Putra Sanjoyo'
	),
	antrian_data AS (
	  SELECT COALESCE(MAX(Nomor_Antrian), 0) + 1 AS Nomor_Antrian
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 10 AND Tanggal_Janji = '2024-12-12'
	),
	kuota_pasien AS (
	  SELECT Kuota_Pasien
	  FROM Jadwal_Dokter
	  WHERE ID_Jadwal = 10 AND Hari = 'Rabu'
	),
	pasien_terdaftar AS (
	  SELECT COUNT(*) AS jumlah_pasien
	  FROM Buat_Janji
	  WHERE ID_Jadwal = 10 AND Tanggal_Janji = '2024-12-12'
	)
	-- Mengecek apakah jumlah pasien yang terdaftar sudah melebihi kuota
	INSERT INTO Buat_Janji (Tanggal_Janji, Nomor_Rekam_Medis, ID_Jadwal, Nomor_Antrian, Counts)
	SELECT '2024-12-12', Nomor_Rekam_Medis, 10, Nomor_Antrian, pasien_terdaftar.jumlah_pasien + 1
	FROM pasien_data, antrian_data, kuota_pasien, pasien_terdaftar
	WHERE pasien_terdaftar.jumlah_pasien < kuota_pasien.Kuota_Pasien;
