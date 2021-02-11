import logging  # Used to write logs throughout the application
from errors import HandlingErrors # Used to raise errors

def response_pop_batch_message(content, redis_response_message):
    """ Used to build a response for a batch pop message """
    try:
        logging.info('START')
        logging.info('Building response for a batch pop message')
        logging.debug(f'The redis response is: {redis_response_message}')

        # Filtering None Values from the list received
        if None in redis_response_message:
            redis_response_message = list(filter(None, redis_response_message))
            logging.debug(f'The redis response after removing None values is: {redis_response_message}')

            # Validating new list to return meessage
            if not redis_response_message:
                message_to_user = f'No messages to delete from {content.incoming_queue_list} list'
                logging.info('Response built')
                logging.info('END')
                return message_to_user

        # Casting list to string 
        redis_response_message = ', '.join([message.decode("utf-8") for message in redis_response_message])

        message_to_user = f'The following message(s) was(were) were removed from {content.incoming_queue_list} list: {redis_response_message}'

        logging.info('Response built')
        logging.info('END')
    except (TypeError, AttributeError):
        raise HandlingErrors('Error building response for a batch pop message',500)
    except:
        raise HandlingErrors('Something else failed building response for a batch pop message',500)
    else:
        return  message_to_user

def response_pop_single_message(content, redis_response_message):
    """ Used to build a response for a single pop message """
    try:
        logging.info('START')
        logging.info('Building response for pop single message')
        logging.debug(f'The redis response is: {redis_response_message}')

        if redis_response_message == None:
            message_to_user = f'No messages to delete from {content.incoming_queue_list} list'
        else:
            message_to_user = f'The message {redis_response_message.decode("utf-8")} was removed from {content.incoming_queue_list} list'

        logging.info('Response built')
        logging.info('END')
    except AttributeError:
        raise HandlingErrors('Error building response for pop single message',500)
    except:
        raise HandlingErrors('Something else failed building response for pop single message',500)
    else:
        return message_to_user