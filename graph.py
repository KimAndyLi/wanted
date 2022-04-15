from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time,strftime
from random import random
from datetime import datetime
import psycopg2

#Init FLask application
app = Flask(__name__)

#Establishing the connection
try:
    conn = psycopg2.connect(
        database="currency",
        user="postgres",
        password="7153862",
        host='127.0.0.1', 
        port= '5432')
except psycopg2.OperationalError:
    print("Unable connect to DB")

#Init cursor for db
cursor = conn.cursor()

#Setting auto commit false
conn.autocommit = True

#Getting data from db
cursor.execute('''SELECT * from prices''')
result = cursor.fetchall();
tme = str(result[-1][0])
rub_usd_price = float(result[-1][1])
rub_eur_price = float(result[-1][2])
rub_gbp_price = float(result[-1][3])
rub_btc_price = float(result[-1][4])
rub_eth_price = float(result[-1][5])
rub_sol_price = float(result[-1][6])
rub_jpy_price = float(result[-1][7])
rub_aud_price = float(result[-1][8])
rub_cad_price = float(result[-1][9])
rub_cny_price = float(result[-1][10])

#choose currency data for previous points
value1 = [[], [], '']
value2 = [[], [], '']
value3 = [[], [], '']
value4 = [[], [], '']
value5 = [[], [], '']
value6 = [[], [], '']
value7 = [[], [], '']
value8 = [[], [], '']
value9 = [[], [], '']
value10 = [[], [], '']

#selected currency pair
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

#Choosing data for chart
@app.route('/init', methods=["GET"])
def init():
    global choosen_currency

    if choosen_currency == "RUB/USD":
        response = make_response(json.dumps(value1))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/EUR":
        response = make_response(json.dumps(value2))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/GBP":
        response = make_response(json.dumps(value3))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/BTC":
        response = make_response(json.dumps(value4))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/ETH":
        response = make_response(json.dumps(value5))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/SOL":
        response = make_response(json.dumps(value6))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/JPY":
        response = make_response(json.dumps(value7))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/AUD":
        response = make_response(json.dumps(value8))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/CAD":
        response = make_response(json.dumps(value9))
        response.content_type = 'application/json'
    elif choosen_currency == "RUB/CNY":
        response = make_response(json.dumps(value10))
        response.content_type = 'application/json'
    return response

#Passing newest data
@app.route('/data', methods=["GET", "POST"])
def data():
    global rub_usd_price
    global rub_eur_price
    global rub_gbp_price
    global rub_btc_price
    global rub_eth_price
    global rub_sol_price
    global rub_jpy_price
    global rub_aud_price
    global rub_cad_price
    global rub_cny_price
    global tme
    global choosen_currency

    #time calculating
    tme = str(strftime("%H:%M:%S"))
    value1[0].append(tme)
    value2[0].append(tme)
    value3[0].append(tme)
    value4[0].append(tme)
    value5[0].append(tme)
    value6[0].append(tme)
    value7[0].append(tme)
    value8[0].append(tme)
    value9[0].append(tme)
    value10[0].append(tme)

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

    #RUB/BTC calculating
    rub_btc_price = rub_btc_price + generate_movement()
    if rub_btc_price <=0:
        rub_btc_price = 0
    
    #RUB/eth calculating
    rub_eth_price = rub_eth_price + generate_movement()
    if rub_eth_price <=0:
        rub_eth_price = 0

    #RUB/sol calculating
    rub_sol_price = rub_sol_price + generate_movement()
    if rub_sol_price <=0:
        rub_sol_price = 0

    #RUB/JPY calculating
    rub_jpy_price = rub_jpy_price + generate_movement()
    if rub_jpy_price <=0:
        rub_jpy_price = 0

    #RUB/AUD calculating
    rub_aud_price = rub_aud_price + generate_movement()
    if rub_aud_price <=0:
        rub_aud_price = 0

    #RUB/CAD calculating
    rub_cad_price = rub_cad_price + generate_movement()
    if rub_cad_price <=0:
        rub_cad_price = 0

    #RUB/CNY calculating
    rub_cny_price = rub_cny_price + generate_movement()
    if rub_cny_price <=0:
        rub_cny_price = 0

    #Recording data sets for every currencies
    value1[1].append(rub_usd_price)
    value2[1].append(rub_eur_price)
    value3[1].append(rub_gbp_price)
    value4[1].append(rub_btc_price)
    value5[1].append(rub_eth_price)
    value6[1].append(rub_sol_price)
    value7[1].append(rub_jpy_price)
    value8[1].append(rub_aud_price)
    value9[1].append(rub_cad_price)
    value10[1].append(rub_cny_price)


    #Choosing data to plot
    if choosen_currency == 'RUB/USD':
        value1[2]='RUB/USD'
        values = [tme, rub_usd_price]
    elif choosen_currency == 'RUB/EUR':
        value2[2]='RUB/EUR'
        values = [tme, rub_eur_price]
    elif choosen_currency == 'RUB/GBP':
        value3[2]='RUB/GBP'
        values = [tme, rub_gbp_price]
    elif choosen_currency == 'RUB/BTC':
        value4[2]='RUB/BTC'
        values = [tme, rub_btc_price]
    elif choosen_currency == 'RUB/ETH':
        value5[2]='RUB/ETH'
        values = [tme, rub_eth_price]
    elif choosen_currency == 'RUB/SOL':
        value6[2]='RUB/SOL'
        values = [tme, rub_sol_price]
    elif choosen_currency == 'RUB/JPY':
        value7[2]='RUB/JPY'
        values = [tme, rub_jpy_price]
    elif choosen_currency == 'RUB/AUD':
        value8[2]='RUB/AUD'
        values = [tme, rub_aud_price]
    elif choosen_currency == 'RUB/CAD':
        value9[2]='RUB/CAD'
        values = [tme, rub_cad_price]
    elif choosen_currency == 'RUB/CNY':
        value10[2]='RUB/CNY'
        values = [tme, rub_cny_price]
    else:
        values = [0, 0]
    
    print(choosen_currency)

    #writing and commiting data to database
    cursor.execute('''INSERT INTO prices (time, rub_usd, rub_eur, rub_gbp, rub_btc, rub_eth, rub_sol, rub_jpy, rub_aud, rub_cad, rub_cny) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', [tme, rub_usd_price, rub_eur_price, rub_gbp_price, rub_btc_price, rub_eth_price, rub_sol_price, rub_jpy_price, rub_aud_price, rub_cad_price, rub_cny_price])
    conn.commit()

    response = make_response(json.dumps(values))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)