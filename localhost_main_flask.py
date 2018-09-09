#https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-rainbow-hat-in-python
from flask import Flask, render_template
import datetime
import random
import time
from threading import Timer
import sensor_data_generator

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
        'title' : 'HELLO!',
        'time' : timeString,
        'temp' : temp,
        'press' : press, 
        }
    return render_template('index_new.html', **templateData)

@app.route('/<deviceName>/<action>')
def action(deviceName, action):
    global temp
    global press
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    if deviceName == 'temp':
        if action == 'up':
            temp += 1
        if action == 'down':
            temp -= 1
    if deviceName == 'press':
        if action == 'up':
            press += 5
        if action == 'down':
            press -= 5

    templateData = { 
        'title' : 'HELLO!',
        'time' : timeString,
        'temp' : temp,
        'press' : press, 
        }

    return render_template('index_new.html', **templateData)

def display_data():
    temp = random.randint(21, 30) #str(rh.weather.temperature())
    press = random.randint(985, 1037) #str(rh.weather.pressure())
    list = [temp, press]


if __name__ == '__main__':
    t = Timer(3.0, generate_data)
    t.start()
    app.run(debug=True, port=5000, host='0.0.0.0')
        