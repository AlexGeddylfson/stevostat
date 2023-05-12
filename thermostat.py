import RPi.GPIO as GPIO
import Adafruit_DHT
from flask import Flask, render_template, request

# Set up GPIO pins for the relay module
RELAY_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

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

# Function to round temperature to the nearest 0.5
def round_temperature(temperature):
    rounded_temperature = round(temperature * 2) / 2
    return rounded_temperature

# Function to control the relay
def set_relay_state(state):
    GPIO.output(RELAY_PIN, state)

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
    return data

# Thermostat control route
@app.route('/thermostat', methods=['POST'])
def thermostat():
    target_temperature_fahrenheit = float(request.form['temperature'])
    target_temperature_celsius = (target_temperature_fahrenheit - 32) * 5/9
    # Implement your thermostat logic here
    # You can compare target_temperature_celsius with the current temperature and control the relay accordingly
    set_relay_state(GPIO.HIGH)
    return "Thermostat set to {}°F".format(target_temperature_fahrenheit)


# Clean up GPIO
GPIO.cleanup()
