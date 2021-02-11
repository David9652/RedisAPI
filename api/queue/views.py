import logging  # Used to write logs throughout the application
from flask import Blueprint # Used to handle routing
from flask import request, jsonify  # Used to get incoming data and serialize response
from errors import HandlingErrors # Used to handle errors
from api.redisconn import create_redis_connection # Used to create a redis connection
from api.queue.queue import dequeue_messages, queue_messages, get_length_queue, get_messages_queue # Used to send commands to redis
from api.queue.validate import validate, validate_query # Used to validate incoming data
from api.queue.constant import LPOP, RPOP, LPUSH, RPUSH, LLEN, LRANGE # Commands to send to redis

queue = Blueprint('queue', __name__, url_prefix="/queue") # Instancing Blueprint

# Routing LPOP requests
@queue.route('/lpop', methods=['POST'])
def show_lpop():
    """ View used to show the result of running LPOP command """
    logging.info('START')

    # Validating query parameters
    incoming_query_parameters = validate_query(request.args)
    # Creating connection to redis and dequeuing messages
    response_queue = dequeue_messages(create_redis_connection(incoming_query_parameters.incoming_queue_database),LPOP,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

# Routing RPOP requests
@queue.route('/rpop', methods=['POST'])
def show_rpop():  
    """ View used to show the result of running RPOP command """
    logging.info('START')

    # Validating query parameters
    incoming_query_parameters = validate_query(request.args)
    # Creating connection to redis and dequeuing messages
    response_queue = dequeue_messages(create_redis_connection(incoming_query_parameters.incoming_queue_database),RPOP,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

# Routing LPUSH requests
@queue.route('/lpush', methods=['POST'])
def show_lpush():
    """ View used to show the result of running LPUSH command """
    logging.info('START')

    # Validating incoming information
    message,incoming_query_parameters = validate(request.json,request.args)
    # Creating connection to redis and queuing messages
    response_queue = queue_messages(create_redis_connection(incoming_query_parameters.incoming_queue_database),LPUSH,message,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

# Routing RPUSH requests
@queue.route('/rpush', methods=['POST'])
def show_rpush():
    """ View used to show the result of running RPUSH command """
    logging.info('START')

    # Validating incoming information
    message,incoming_query_parameters = validate(request.json,request.args)
    # Creating connection to redis and queuing messages
    response_queue = queue_messages(create_redis_connection(incoming_query_parameters.incoming_queue_database),LPUSH,message,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

# Routing COUNT requests
@queue.route('/count', methods=['GET'])
def show_count():
    """ View used to show the result of running COUNT command """
    logging.info('START')

    # Validating query parameters
    incoming_query_parameters = validate_query(request.args)
    # Creating connection to redis and get lenght of a given list
    response_queue = get_length_queue(create_redis_connection(incoming_query_parameters.incoming_queue_database),LLEN,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

# Routing LRANGE requests
@queue.route('/lrange', methods=['GET'])
def show_lrange():
    """ View used to show the result of running LRANGE command """
    logging.info('START')

    # Validating query parameters
    incoming_query_parameters = validate_query(request.args)
    # Creating connection to redis and getting messages
    response_queue = get_messages_queue(create_redis_connection(incoming_query_parameters.incoming_queue_database),LRANGE,incoming_query_parameters)

    logging.info('END')

    return jsonify(message=response_queue),200

@queue.errorhandler(HandlingErrors)
def queue_error_handler(error):
    """ Used to handle queue route errors """
    return error.to_json()