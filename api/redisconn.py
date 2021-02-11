import logging  # Used to write logs throughout the application
from redis import Redis # Used to connect and send commands to redis
from redis import ConnectionError, ResponseError # Used to handle connection redis errors
from errors import HandlingErrors # Used to raise errors
from api.config import HOST, PORT # Used to get default configuration

def create_redis_connection(database):
    """ Used to create a redis connection """
    try:
        logging.info('START')
        logging.info('Trying to connect to redis server')

        r = Redis(host=HOST, port=PORT, db=database) # Instancing redis connection
        r.ping() # Testing redis connection

        logging.info('Connection to redis established')
        logging.info('END')
    except (ConnectionError, ResponseError):
        raise HandlingErrors('Error trying to connect to redis server',500)
    except:
        raise HandlingErrors('Something else failed trying to connect to redis server',500)
    else:
        return r