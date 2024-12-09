import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, json, session

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('homepage'))
    return render_template("LoginPage/index.html")

# PASIEN #################################################################
@app.route('/HomePage')
def homepage():
    return render_template("Pasien/HomepagePasien/index.html")

@app.route('/JadwalTemu')
def jadwaltemu():
    return render_template("Pasien/JadwalTemu/index.html")

@app.route('/Booking')
def booking():
    query = """
        SELECT d.Spesialisasi, d.Nama, STRING_AGG(j.Hari || ' ' || j.Jam::TEXT, ', ') AS Jadwal
        FROM Dokter d
        JOIN Jadwal_Dokter j ON d.ID_Dokter = j.ID_Dokter
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

    return render_template("Pasien/Booking/index.html", doctors_data=doctors_data)
    # return render_template("Booking/index.html")

@app.route('/Profile')
def profile():
    return render_template("Pasien/Profile/index.html")

@app.route('/Tagihan')
def tagihan():
    return render_template("Pasien/Tagihan/index.html")

###########################################################

