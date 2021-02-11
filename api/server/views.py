import logging  # Used to write logs throughout the application
from flask import Blueprint # Used to handle routing
from flask import request, jsonify  # Used to get incoming data and serialize response
from errors import HandlingErrors # Used to handle errors
from api.redisconn import create_redis_connection # Used to create a redis connection
from api.server.healthstatus import get_health_status # Used to get the health status of redis server
from api.config import DEFAULT_DB # Used to set the default database for redis connection
from api.server.constant import INFO # Command to send to redis

server = Blueprint('server', __name__, url_prefix="/server") # Instancing Blueprint

# Routing STATUS
@server.route('/status', methods=['GET'])
def show_status():
    """ View used to show redis server information """
    logging.info('START')

    # Getting Redis Server health based on the parameter captured
    redis_status = get_health_status(create_redis_connection(DEFAULT_DB),INFO,request.args.get('section',default=False,type=str))

    logging.info('END')

    return jsonify(redis_status),200

@server.errorhandler(HandlingErrors)
def server_error_handler(error):
    """ Used to handle server route errors """
    return error.to_json()