from flask import Flask, render_template, request, flash
# import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# RELAY_PIN = 7
# GPIO.setup(RELAY_PIN, GPIO.OUT)
# GPIO.output(RELAY_PIN, True)

PATTERN = {(0, 1), (0, 3), (1, 0), (3, 0), (3, 1)}

def activate_garage_door():
    # GPIO.output(RELAY_PIN, False)
    print("opening")
    time.sleep(0.8)
    # GPIO.output(RELAY_PIN, True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected = set()

        for key in request.form.keys():
            row, col = map(int, key.split('_'))
            selected.add((row, col))

        if selected == PATTERN:
            activate_garage_door()
            
    return render_template('index.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=1234)
    finally:
        GPIO.cleanup()
