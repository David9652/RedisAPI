import logging  # Used to write logs throughout the application
from redis import ConnectionError, ResponseError # Used to handle connection redis errors
from errors import HandlingErrors # Used to raise errors
from api.server.constant import STATUS # Used to verifiy the status sent

def get_health_status(r,command,section):
    """ Used to get the redis server health based on the parameter captured """

    logging.info('START')
    logging.debug(f'The command used to get the information is command: {command} (expected to be info)')
    logging.debug(f'The specific section to get the information is section: {section} used to get the information is command: {command} (expected to be one of them: server, clients, memory, persistance, stats, replication, cpu, cluster, keyspace)')

    if (command == 'info'):
        try:
            logging.info('Trying to get redis server health')

            if section in STATUS:
                redis_status = r.info(section=section)
            else:
                redis_status = r.info()

            logging.info('Redis server health got')
            logging.info('END')
        except (ConnectionError, ResponseError):
            raise HandlingErrors('Error trying to connect to redis server',500)
        except:
            raise HandlingErrors(f'Error executing {command} command',500)
        else:
            return redis_status
    else:
        raise HandlingErrors('Command not found',500)