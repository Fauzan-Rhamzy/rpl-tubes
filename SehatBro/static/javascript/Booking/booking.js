// Fungsi untuk menampilkan daftar dokter sesuai spesialisasi
function showDoctors() {
  const specialization = document.getElementById("specialization").value;
  const doctorList = document.getElementById("doctor-list");
  const doctorsContainer = document.getElementById("doctors");

  // Menyembunyikan daftar dokter jika spesialisasi belum dipilih
  if (!specialization) {
    doctorList.style.display = "none";
    return;
  }

  // Menampilkan daftar dokter berdasarkan spesialisasi
  doctorList.style.display = "block";
  doctorsContainer.innerHTML = ""; // Menghapus daftar dokter sebelumnya

  const doctors = getDoctorsBySpecialization(specialization);

  // Menampilkan dokter yang sesuai dengan spesialisasi
  doctors.forEach((doctor) => {
    const doctorCard = document.createElement("div");
    doctorCard.classList.add("doctor-card");

    doctorCard.innerHTML = `
        <h3>${doctor.name}</h3>
        <p>Spesialis: ${doctor.specialization}</p>
        <p class="schedule">Jadwal: ${doctor.schedule}</p>
        <button onclick="bookAppointment('${doctor.name}')">Booking</button>
      `;

    doctorsContainer.appendChild(doctorCard);
  });
}

// Fungsi untuk mendapatkan daftar dokter berdasarkan spesialisasi
function getDoctorsBySpecialization(specialization) {
  const doctorData = {
    umum: [
      {
        name: "Dr. Andi",
        specialization: "Dokter Umum",
        schedule: "Senin - Jumat, 09:00 - 15:00",
      },
      {
        name: "Dr. Budi",
        specialization: "Dokter Umum",
        schedule: "Senin - Jumat, 10:00 - 16:00",
      },
    ],
    gigi: [
      {
        name: "Dr. Siti",
        specialization: "Dokter Gigi",
        schedule: "Senin, Rabu, Jumat, 08:00 - 12:00",
      },
      {
        name: "Dr. Dwi",
        specialization: "Dokter Gigi",
        schedule: "Selasa, Kamis, Sabtu, 09:00 - 13:00",
      },
    ],
    spesialis: [
      {
        name: "Dr. Zaki",
        specialization: "Dokter Spesialis Jantung",
        schedule: "Senin - Kamis, 08:00 - 14:00",
      },
      {
        name: "Dr. Maya",
        specialization: "Dokter Spesialis Kulit",
        schedule: "Selasa - Jumat, 09:00 - 17:00",
      },
      {
        name: "Dr. test",
        specialization: "Dokter Spesialis Test",
        schedule: "Selasa - minggu, 09:00 - 17:00",
      },
    ],
  };

  return doctorData[specialization] || [];
}

// Fungsi untuk melakukan booking janji temu
function bookAppointment(doctorName) {
  alert(`Anda berhasil melakukan booking janji temu dengan ${doctorName}.`);
}
