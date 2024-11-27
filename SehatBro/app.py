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

@app.route('/home')
def homepage():
    return render_template("homepagetest.html")