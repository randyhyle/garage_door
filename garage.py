from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
relay_pin = 17
GPIO.setup(relay_pin, GPIO.OUT)

def activate_garage_door():
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(relay_pin, GPIO.LOW)

@app.route('/')
def index():
    return '''<h1>Garage Door</h1>
    <form action="/open" method="POST">
        <button type="submit">Activate Garage Door</button>
    </form>
    '''

@app.route('/open', methods=['POST'])
def open_garage():
    activate_garage_door()
    return '<h1>Garage Door Activated</h1><a href="/">Back</a>'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=1234)
    finally:
        GPIO.cleanup()