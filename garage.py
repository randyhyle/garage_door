from flask import Flask, render_template, request
# import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# RELAY_PIN = 7
# GPIO.setup(RELAY_PIN, GPIO.OUT)
# GPIO.output(RELAY_PIN, True)
# open = False

PATTERN = {(0, 1), (0, 3), (1, 1), (1, 4), (3, 0)}

def activate_garage_door():
    # GPIO.output(RELAY_PIN, False)
    time.sleep(0.8)
    # GPIO.output(RELAY_PIN, True)

@app.route('/', methods=['GET', 'POST'])
def index():
    # garage_door_button = '''<h1>Garage Door</h1>
    # <form action="/open" method="POST">
    #     <button type="submit">Activate Garage Door</button>
    # </form>
    # '''
    if request.method == 'POST':
        selected = set()


    return render_template('index.html')

@app.route('/open', methods=['POST'])
def open_garage():
    activate_garage_door()
    message = '<h1>Garage Door Activated</h1><a href="/">Back</a>'
    return message

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=1234)
    finally:
        GPIO.cleanup()
