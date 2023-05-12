import sys
import os
sys.path.insert(0, '/home/stephen/stevostat')

# Add the virtual environment's site-packages to the sys.path
venv_path = '/home/stephen/stevostat/venv'
site_packages = os.path.join(venv_path, 'lib', 'python3.9', 'site-packages')
sys.path.append(site_packages)

# Import the Flask application
from thermostat import app as application

# Set the application callable for Apache
application = application.wsgi_app
