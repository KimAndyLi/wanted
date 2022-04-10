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

value = [[], [], 'name']

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

cursor.execute('''SELECT * from currency''')
result = cursor.fetchall();
rub_usd_price = float(result[-1][0])
tme = float(result[-1][1])

@app.route('/init', methods=["GET"])
def init():

    response = make_response(json.dumps(value))
    response.content_type = 'application/json'
    return response

@app.route('/data', methods=["GET"])
def data():
    global rub_usd_price
    global tme
    rub_usd_price = rub_usd_price + generate_movement()
    if rub_usd_price <=0:
        rub_usd_price = 0
    
    tme = tme + 1000
    value[0].append(tme)
    value[1].append(rub_usd_price)
    a = [tme, rub_usd_price]
    
 #  data = [tme , rub_usd_price]


    # cursor.execute('''INSERT INTO currency (price, time) VALUES (%s, %s)''', [rub_usd_price, tme])
    # conn.commit()

    response = make_response(json.dumps(a))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)