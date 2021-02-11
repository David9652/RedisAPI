import logging  # Used to write logs throughout the application
from redis import ConnectionError, ResponseError # Used to handle connection redis errors
from errors import HandlingErrors # Used to raise errors
from api.queue.response import response_pop_single_message, response_pop_batch_message # Used to build response message
from api.queue.constant import DEFAULT_TIMES # Use to get default queue processing

def dequeue_messages(r,command,content):
    """ Used to remove messages from the head or tail queue """
    logging.info('START')
    logging.debug(f'The command used to remove message(s) from {content.incoming_queue_list} list is command: {command} (expected to be lpop or rpop)')

    # Dequeuing messages from the head queue
    if (command == 'lpop'):
        try:
            logging.info('Dequeuing messages from the head queue')
            logging.info('Starting transaction')

            # Checking if it's queue processing
            if (content.incoming_queue_times > DEFAULT_TIMES):
                # Starting transaction
                with r.pipeline() as pipe:
                    for _ in range(content.incoming_queue_times):
                        pipe.lpop(content.incoming_queue_list)
                        logging.debug(f'Buffering {_} / {content.incoming_queue_times}')
                    message_to_user = response_pop_batch_message(content,pipe.execute()) # Getting redis list response and building a new string 
                # Transaction ended
            else:
                message_to_user = response_pop_single_message(content,r.lpop(content.incoming_queue_list)) # Getting redis bytes-string response and building a new string 

            logging.info('Transaction ended')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            return message_to_user
    # Dequeuing messages from the tail queue
    elif (command == 'rpop'):
        try:
            logging.info('Dequeuing messages from the tail queue')
            logging.info('Starting transaction')

            # Checking if it's queue processing
            if (content.incoming_queue_times > DEFAULT_TIMES):
                # Starting transaction
                with r.pipeline() as pipe:
                    for _ in range(content.incoming_queue_times):
                        pipe.rpop(content.incoming_queue_list)
                        logging.debug(f'Buffering {_} / {content.incoming_queue_times}')
                    message_to_user = response_pop_batch_message(content,pipe.execute()) # Getting redis list response and building a new string 
                # Transaction ended
            else:
                message_to_user = response_pop_single_message(content,r.rpop(content.incoming_queue_list)) # Getting redis bytes-string response and building a new string 

            logging.info('Transaction ended')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            return message_to_user
    else:
        raise HandlingErrors('Command not found',500)

def queue_messages(r,command,message,content):
    """ Used to push messages to the head or tail queue """
    logging.info('START')
    logging.debug(f'The command used to push message(s) to {content.incoming_queue_list} list is command: {command} (expected to be lpush or rpush)')

    # Pushing messages to the head queue
    if (command == 'lpush'):
        try:
            logging.info('Pushing messages to the head queue')
            logging.info('Starting transaction')

            # Checking if it's queue processing
            if (content.incoming_queue_times > DEFAULT_TIMES):
                # Starting transaction
                with r.pipeline() as pipe:
                    for _ in range(content.incoming_queue_times):
                        pipe.lpush(content.incoming_queue_list, message)
                        logging.debug(f'Buffering {_} / {content.incoming_queue_times}')
                    pipe.execute()
                # Transaction ended
            else:
                r.lpush(content.incoming_queue_list,message)

            logging.info('Transaction ended')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            message_to_user = f'The message {message} was added {content.incoming_queue_times} time(s) to {content.incoming_queue_list} list'
            return message_to_user
    # Pushing messages to the tail queue
    elif  (command == 'rpush'):
        try:
            logging.info('Pushing messages to the tail queue')
            logging.info('Starting transaction')

            # Checking if it's queue processing
            if (content.incoming_queue_times > DEFAULT_TIMES):
                # Starting transaction
                with r.pipeline() as pipe:
                    for _ in range(content.incoming_queue_times):
                        pipe.rpush(content.incoming_queue_list, message)
                        logging.debug(f'Buffering {_} / {content.incoming_queue_times}')
                    pipe.execute()
                # Transaction ended
            else:
                r.rpush(content.incoming_queue_list,message)

            logging.info('Transaction ended')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            message_to_user = f'The message {message} was added {content.incoming_queue_times} time(s) to {content.incoming_queue_list} list'
            return message_to_user
    else:
        raise HandlingErrors('Command not found',500)

def get_length_queue(r,command,content):
    """ Used to get the length of a given list """
    logging.info('START')
    logging.debug(f'The command used to get {content.incoming_queue_list} list count is command: {command} (expected to be llen)')

    if (command == 'llen'):
        try:
            logging.info('Trying to get length list')

            count = r.llen(content.incoming_queue_list)

            logging.info('Length list got')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            message_to_user = f'You have {count} message(s) in {content.incoming_queue_list} list'
            return message_to_user
    else:
        raise HandlingErrors('Command not found',500)

def get_messages_queue(r,command,content):
    """ Used to get messages of a given list """
    logging.info('START')
    logging.debug(f'The command used to get messages from {content.incoming_queue_list} list is command: {command} (expected to be lrange)')

    if (command == 'lrange'):
        try:
            logging.info('Trying to get messages')

            message_to_user = r.lrange(content.incoming_queue_list,content.incoming_queue_start,content.incoming_queue_end)

            if message_to_user:
                message_to_user = ', '.join([message.decode("utf-8") for message in message_to_user])
            else:
                message_to_user = f'No messages to show from {content.incoming_queue_list} list'

            logging.info('Messages got')
            logging.info('END')

        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            return message_to_user
    else:
        raise HandlingErrors('Command not found',500)