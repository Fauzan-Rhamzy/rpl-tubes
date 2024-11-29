import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Abaikan validasi, langsung redirect ke homepage
        return redirect(url_for('homepage'))
    return render_template("LoginPage/index.html")

@app.route('/HomePage')
def homepage():
    return render_template("HomepagePasien/index.html")

@app.route('/JadwalTemu')
def jadwaltemu():
    return render_template("JadwalTemu/index.html")

@app.route('/Booking')
def booking():
    return render_template("Booking/index.html")

@app.route('/Profile')
def profile():
    return render_template("Profile/index.html")

@app.route('/Tagihan')
def tagihan():
    return render_template("Tagihan/index.html")