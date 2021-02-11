import logging  # Used to write logs throughout the application
from api.queue.mapping import MapQueryParameters # Used to map query parameters
from errors import HandlingErrors # Used to raise errors

def validate(incoming_message,incoming_query_parameters):
    """ Used to validate incoming data """
    logging.info('START')

    # Validating body structure
    message = validate_body(incoming_message)
    # Validating query parameters
    incoming_query_parameters = validate_query(incoming_query_parameters)

    logging.info('END')

    return message,incoming_query_parameters

def validate_body(incoming_message):
    """ Used to validate body structure """

    logging.info('START')
    logging.info('Validating body structure')

    message = incoming_message.get('message') # Getting value from body
    if not message: # Validating if 'message' parameter exists
        raise HandlingErrors('Your request does not have a valid structure',404)

    logging.info('Body structure validated')
    logging.info('END')

    return message

def validate_query(request_query_parameters):
    """ Used to validate and serialize queue query parameters"""

    logging.info('START')
    logging.info('Validating queue query structure')

    incoming_query_parameters = MapQueryParameters() # Instancing default data model 
    if(request_query_parameters): # Validating if query parameters exist
        try: 
            # Getting and casting values from query parameters
            incoming_queue_times = request_query_parameters.get('times',default=False,type=int) 
            incoming_queue_list = request_query_parameters.get('list',default=False,type=str)
            incoming_queue_database = request_query_parameters.get('db',default=False,type=int)
            incoming_queue_start = request_query_parameters.get('start',default=False,type=int)
            incoming_queue_end = request_query_parameters.get('end',default=False,type=int)
            # Setting new values from query parameters
            incoming_query_parameters = MapQueryParameters(incoming_queue_times=incoming_queue_times, incoming_queue_list=incoming_queue_list, incoming_queue_database=incoming_queue_database, incoming_queue_start =incoming_queue_start, incoming_queue_end=incoming_queue_end)
        except:
            raise HandlingErrors('Error mapping queue query parameters',404)

    logging.info('Queue query structure validated')
    logging.info('END')

    return incoming_query_parameters