""" Used to set up redis queue settings """
DEFAULT_TIMES = 1 # Default batch proccessing
DEFAULT_LIST = 'meli' # Name of the default list/queue
MIN_DB = 0 # Minimun selectable database
MAX_DB = 15 # Maximun selectable database
LPOP = 'lpop' # Command for removing messages from the head queue
RPOP = 'rpop'  # Command for removing messages from the tail queue
LPUSH = 'lpush' # Command for adding messages to the head queue
RPUSH = 'rpush' # Command for adding messages to the head queue
LLEN = 'llen' # Command for getting the length of a queue
LRANGE = 'lrange' # Command for getting specified elements of a list
START = 0 # Start default index of the head list/queue
END = -1 # End default index of the tail list/queue