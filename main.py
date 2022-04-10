from shutil import move
from flask import Flask, render_template, jsonify, request
from random import random
import time


app = Flask(__name__)

rub_usd_price=0


#think that this code should be parallel
def generate_movement(value):
    movement = -1 if random() < 0.5 else 1
    value=value+movement
    return value


@app.route('/_stuff', methods = ['GET'])
def stuff():
    rub_usd_price=generate_movement(rub_usd_price)
    return jsonify(result=rub_usd_price)


#Probably shoyld add classes for currencies pairs
@app.route("/")
def index():
    
    return render_template("chart.html")



# class currencies(self):

if __name__ == "__main__":
    app.run(debug=True)