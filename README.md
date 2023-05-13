# stevostat
A custom thermostat


This project is a Raspberry Pi-based thermostat application that utilizes a DHT22 temperature and humidity sensor. It allows you to control the thermostat temperature and view real-time temperature and humidity data through a web interface. The application also logs the sensor data to an SQL database for future analysis.

Features

Control the thermostat temperature through the web interface.
View real-time temperature and humidity data on the web page.
Store temperature and humidity data in an SQL database every 5 minutes.
Celsius to Fahrenheit conversion for temperature display.
Rounded temperature values to the nearest 0.5 for better accuracy.
Prerequisites

Raspberry Pi (tested on Raspberry Pi 3 Model B)
DHT22 temperature and humidity sensor
Python 3
Flask
Flask-SQLAlchemy
RPi.GPIO
Adafruit_DHT
SQLite (or any other supported SQL database)
Installation

Clone this repository to your Raspberry Pi:
bash
Copy code
git clone https://github.com/yourusername/raspberry-pi-thermostat.git
Install the required Python libraries:
Copy code
pip3 install Flask Flask-SQLAlchemy RPi.GPIO Adafruit_DHT
Connect the DHT22 sensor to your Raspberry Pi's GPIO pins. Refer to the sensor documentation for wiring instructions.
Modify the app.config['SQLALCHEMY_DATABASE_URI'] value in app.py to point to your desired SQL database URI.
Start the application:
Copy code
python3 app.py
Access the web interface by entering your Raspberry Pi's IP address in a web browser.
Usage

The home page displays the current temperature and humidity readings from the DHT22 sensor.
Use the temperature input field to set the desired thermostat temperature and click the "Set" button to apply the changes.
The temperature and humidity data is automatically logged to the SQL database every 5 minutes.
The stored sensor data can be accessed and analyzed using appropriate SQL queries.
Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please submit an issue or create a pull request.

License

This project is licensed under the MIT License.

Acknowledgements

This project is inspired by various Raspberry Pi thermostat and sensor data logging projects available online.
Special thanks to the authors and contributors of the Flask, Flask-SQLAlchemy, RPi.GPIO, and Adafruit_DHT libraries.
