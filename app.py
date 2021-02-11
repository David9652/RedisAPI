import logging  # Used to write logs throughout the application
import os # Used to get environment variable
from flask import Flask # Used to create the application instance
from api.queue.views import queue # Used to import queue blueprint 
from api.server.views import server # Used to import server blueprint 

def create_app():
    """ Used to create a Flask application """

    logging.info('START')
    logging.info('Building new application')

    app = Flask(__name__) # Instancing my application

    logging.debug(f'Application instantiated app.name:{app.name} (expected to be app)')
    logging.debug('Setting flask configuration')

    # Setting configuration depending on enviroment variable 'FLASK_ENV'
    if app.config['ENV'] == 'production':
        # Setting configuration for 'production environment'
        app.config.from_object('config.ProductionConfig')
    elif app.config['ENV'] == 'development':
        # Setting configuration for 'development environment'
        app.config.from_object('config.DevelopmentConfig')
    else:
        # Setting configuration for 'testing environment'
        app.config.from_object('config.TestingConfig')

    logging.debug(f"Configuration for {os.getenv('FLASK_ENV')} environment applied")

    register(app, queue, server) # Registering blueprints

    logging.info('Application was successfully built')
    logging.info('END')

    return app

def register(app, *argv):
    """ Used to register the blueprints that will use the application """

    logging.info('START')
    logging.info('Registering blueprints')

    for arg in argv:
        logging.debug(f'Registering {arg.name} blueprint')
        app.register_blueprint(arg) # Registering each blueprint
        logging.debug(f'Blueprint {arg.name} registered')

    logging.info('Blueprints were successfully registered')
    logging.info('END')