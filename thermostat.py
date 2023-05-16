import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from flask import Flask, render_template, request, jsonify

# Set up GPIO pins for the relay module
RELAY_PINS = [27, 22, 23, 24]
GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering mode to BCM
for pin in RELAY_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Set up the DHT sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Create Flask app
app = Flask(__name__)

# Function to read temperature and humidity
def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return int(humidity), temperature

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(temperature_celsius):
    temperature_fahrenheit = round((temperature_celsius * 9/5) + 32, 1)
    return temperature_fahrenheit

# Function to round temperature to the nearest 0.5 degrees
def round_temperature(temperature):
    rounded_temperature = round(temperature * 2) / 2
    return rounded_temperature

# Function to control the relay
def set_relay_state(relay_number, state):
    GPIO.output(RELAY_PINS[relay_number], state)

# Function to check and control the thermostat
def check_thermostat(target_temperature_celsius):
    while True:
        humidity, current_temperature = read_temperature_humidity()
        if current_temperature < target_temperature_celsius:
            set_relay_state(0, GPIO.HIGH)
            set_relay_state(1, GPIO.HIGH)
            set_relay_state(2, GPIO.HIGH)
            set_relay_state(3, GPIO.HIGH)
        else:
            set_relay_state(0, GPIO.LOW)
            set_relay_state(1, GPIO.LOW)
            set_relay_state(2, GPIO.LOW)
            set_relay_state(3, GPIO.LOW)
        time.sleep(5)  # Wait for 5 seconds before checking the temperature again

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to retrieve temperature and humidity data
@app.route('/data', methods=['GET'])
def get_data():
    humidity, temperature_celsius = read_temperature_humidity()
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    rounded_temperature = round_temperature(temperature_fahrenheit)
    data = {
        'temperature': rounded_temperature,
        'humidity': humidity
    }
    return jsonify(data)

# Thermostat control route
@app.route('/thermostat', methods=['POST'])
def thermostat():
    target_temperature_fahrenheit = float(request.form['temperature'])
    target_temperature_celsius = (target_temperature_fahrenheit - 32) * 5/9
    print("Target temperature set to:", target_temperature_celsius)
    check_thermostat(target_temperature_celsius)
    return "Thermostat set to {}°F".format(target_temperature_fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
