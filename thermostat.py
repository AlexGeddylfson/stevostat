import RPi.GPIO as GPIO
import Adafruit_DHT
from flask import Flask, render_template, request

# Set up GPIO pins for the relay module
RELAY_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Set up the DHT sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# Create Flask app
app = Flask(__name__)

# Function to read temperature and humidity
def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

# Function to control the relay
def set_relay_state(state):
    GPIO.output(RELAY_PIN, state)

# Home page route
@app.route('/')
def home():
    humidity, temperature = read_temperature_humidity()
    return render_template('index.html', temperature=temperature, humidity=humidity)

# Thermostat control route
@app.route('/thermostat', methods=['POST'])
def thermostat():
    target_temperature = float(request.form['temperature'])
    # Implement your thermostat logic here
    # You can compare target_temperature with the current temperature and control the relay accordingly
    set_relay_state(GPIO.HIGH)
    return "Thermostat set to {}°C".format(target_temperature)

if __name__ == '__main__':
    app.run()

# Clean up GPIO
GPIO.cleanup()
