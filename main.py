import logging  # Used to write logs throughout the application
from app import create_app # Used to create my application

#Setting default logging configuration
logging.basicConfig(filename='logs/flask_logs.log',
    format='%(asctime)-s [%(levelname)s] %(funcName)s: %(message)s',
    level=logging.DEBUG)

app = create_app() # Creating my application