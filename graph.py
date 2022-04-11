from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time
from random import random
from datetime import datetime
import psycopg2

#Init FLask application
app = Flask(__name__)

#Establishing the connection
conn = psycopg2.connect(
    database="currency",
    user="postgres",
    password="7153862",
    host='127.0.0.1', 
    port= '5432')

#Init cursor for db
cursor = conn.cursor()

#Setting auto commit false
conn.autocommit = True

#Getting data from db
cursor.execute('''SELECT * from prices''')
result = cursor.fetchall();
rub_usd_price = float(result[-1][1])
rub_eur_price = float(result[-1][2])
rub_gbp_price = float(result[-1][3])
tme = float(result[-1][0])

#const for points
value = [[], [], '']

#global empty unselected currency
choosen_currency = ''

#Price movoment initation
def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement

#Core page
@app.route('/', methods=["GET", "POST"])
def main():
    global choosen_currency

    if request.method == 'POST':
        result = request.form
        choosen_currency=result['currency']

    return render_template('index.html')

#saving previous data
@app.route('/init', methods=["GET"])
def init():
    response = make_response(json.dumps(value))
    response.content_type = 'application/json'
    return response

#passing newest data
@app.route('/data', methods=["GET", "POST"])
def data():
    global rub_usd_price
    global rub_eur_price
    global rub_gbp_price
    global tme
    global choosen_currency

    #time calculating
    tme = tme + 1000
    value[0].append(tme)

    #RUB/USD calculating
    rub_usd_price = rub_usd_price + generate_movement()
    if rub_usd_price <=0:
        rub_usd_price = 0

    #RUB/EUR calculating
    rub_eur_price = rub_eur_price + generate_movement()
    if rub_eur_price <=0:
        rub_eur_price = 0

    #RUB/GBP calculating
    rub_gbp_price = rub_gbp_price + generate_movement()
    if rub_gbp_price <=0:
        rub_gbp_price = 0
    
    #Choosing data to plot
    if choosen_currency == 'RUB/USD':
        value[1].append(rub_usd_price)
        value[2]='RUB/USD'
        values = [tme, rub_usd_price]
    elif choosen_currency == 'RUB/EUR':
        value[1].append(rub_eur_price)
        value[2]='RUB/EUR'
        values = [tme, rub_eur_price]
    elif choosen_currency == 'RUB/GBP':
        value[1].append(rub_gbp_price)
        value[2]='RUB/GBP'
        values = [tme, rub_gbp_price]
    else:
        values = [0, 0]
    
    print(choosen_currency)

    #writing and commiting data to database
    cursor.execute('''INSERT INTO prices (time, rub_usd, rub_eur, rub_gbp) VALUES (%s, %s, %s, %s)''', [tme, rub_usd_price, rub_eur_price, rub_gbp_price])
    conn.commit()

    response = make_response(json.dumps(values))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)