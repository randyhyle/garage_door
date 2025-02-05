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

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        selected = set()

        for key in request.form.keys():
            row, col = map(int, key.split('_'))
            selected.add((row, col))
        
        if selected == PATTERN:
            open_garage()
        else:
            return "❌ Incorrect Pattern! Try Again.", 403


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
