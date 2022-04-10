from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time
from random import random
from datetime import datetime
import psycopg2


app = Flask(__name__)


#Establishing the connection
conn = psycopg2.connect(
    database="currency",
    user="postgres",
    password="7153862",
    host='127.0.0.1', 
    port= '5432')

cursor = conn.cursor()

#Setting auto commit false
conn.autocommit = True

def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement

def record_data():
    return 0


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('chart.html')


cursor.execute('''SELECT * from currency''')
result = cursor.fetchall();
rub_usd_price = float(result[-1][0])


@app.route('/data', methods=["GET", "POST"])
def data():
    global rub_usd_price

    rub_usd_price = rub_usd_price + generate_movement()
    if rub_usd_price <=0:
        rub_usd_price = 0
    
    data = [time()*1000 , rub_usd_price]

    cursor.execute('''INSERT INTO currency (price) VALUES (%s)''', [rub_usd_price])
    conn.commit()

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)