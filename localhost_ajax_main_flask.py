
from flask import Flask, render_template, jsonify
import datetime
import random
import time
from threading import Timer

app = Flask(__name__)

temp = 23
press = 1022


def generate_data():
    global temp
    global press
    while True:
        temp = temp + random.randint(-1, 1) #str
        press = press + random.randint(-10, 10) #str
        (temp, press)
        time.sleep(3)
        print(temp, press)

@app.route('/')
def index():
    global temp
    global press
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = { 
        'title' : 'LAB',
        'time' : timeString, 
        }
    return render_template('index_new.html')

@app.route('/sensor_data')
def action():
    global temp
    global press
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    data = { 
        'time' : timeString,
        'temp' : temp,
        'press' : press, 
        }

    return jsonify(data)


if __name__ == '__main__':
    t = Timer(10.0, generate_data)
    t.daemon = True
    t.start()
    app.run(debug=True, port=5000, host='0.0.0.0')
        