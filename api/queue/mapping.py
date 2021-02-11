from api.config import DEFAULT_DB # Used to set default database value
from api.queue.constant import DEFAULT_TIMES, DEFAULT_LIST, MIN_DB, MAX_DB, START, END # Used to set and validate default values

class MapQueryParameters():
    """ Used to map incoming query information"""

    # Initializing default values
    incoming_queue_times = DEFAULT_TIMES
    incoming_queue_list = DEFAULT_LIST
    incoming_queue_database = DEFAULT_DB
    incoming_queue_start = START
    incoming_queue_end = END

    # Defining constructor and validating incoming query information
    def __init__(self, incoming_queue_times=DEFAULT_TIMES, incoming_queue_list=DEFAULT_LIST, incoming_queue_database=DEFAULT_DB, incoming_queue_start=START, incoming_queue_end=END):
        """ Used to define the MapQueryParameters constructor """

        if incoming_queue_times > DEFAULT_TIMES:
            self.incoming_queue_times = incoming_queue_times
        if incoming_queue_list != False:
            self.incoming_queue_list = incoming_queue_list
        if incoming_queue_database > MIN_DB and incoming_queue_database <= MAX_DB:
            self.incoming_queue_database = incoming_queue_database
        if incoming_queue_start != False:
            self.incoming_queue_start = incoming_queue_start
        if incoming_queue_end != False:
            self.incoming_queue_end = incoming_queue_end