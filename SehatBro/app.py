import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor()

# sql = '''CREATE TABLE articals(
#                 publisher_id SERIAL PRIMARY KEY,
#                 publisher_name VARCHAR(255) NOT NULL,
#                 publisher_estd INT,
#                 publsiher_location VARCHAR(255),
#                 publsiher_type VARCHAR(255)
# )'''
# cursor.execute(sql)
# connection.commit()

@app.route('/HomePage')
def homepage():
    return render_template("HomepagePasien/index.html")

@app.route('/JadwalTemu')
def jadwaltemu():
    return render_template("JadwalTemu/index.html")

@app.route('/Booking')
def booking():
    return render_template("Booking/index.html")

@app.route('/Login')
def login():
    return render_template("LoginPage/index.html")