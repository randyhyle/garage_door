from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import logging
import os

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
RELAY_PIN = 7
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, True)

PATTERN = {}

status = "Closed"

# Ensure log directory exists
log_dir = "/home/{name here}/garage/logs"
os.makedirs(log_dir, exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=os.path.join(log_dir, "garage.log"),
    level=logging.DEBUG,  # Log all levels (DEBUG, INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("🚀 Logging initialized successfully!")

def activate_garage_door():
    GPIO.output(RELAY_PIN, False)
    time.sleep(0.8)
    GPIO.output(RELAY_PIN, True)
    global status
    status = "Open" if status == "Closed" else "Closed"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected = set()

        for key in request.form.keys():
            try:
                row, col = map(int, key.split('_'))
                selected.add((row, col))
            except ValueError:
                pass

        if selected == PATTERN:
            activate_garage_door()
        else:
            return render_template('index.html', status = status, 
                                   error="Incorrect. Try again")
        
    return render_template('index.html', status = status, error=None)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=1234)
    finally:
        GPIO.cleanup()
