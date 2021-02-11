import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from errors import HandlingErrors # Used to raise errors
from api.redisconn import create_redis_connection # Used to create a redis connection
from api.queue.queue import dequeue_messages, queue_messages, get_length_queue, get_messages_queue # Used to send commands to redis
from api.queue.constant import LPOP, RPOP, LPUSH, RPUSH, LLEN, LRANGE # Commands to send to redis

class TestIntQueue(unittest.TestCase):
    """ Used to test scenarios for the integration between create_redis_connection, dequeue_messages, queue_messages, get_length_queue, get_messages_queue, response_pop_batch_message and response_pop_single_message functions """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()
        self.redis = create_redis_connection(0) # Creating redis connection
        self.content = type('MapQueryParameters', (object,), {})() # Initializing empty object
        self.content.incoming_queue_list = 'meli'

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        self.content.incoming_queue_times = 100
        dequeue_messages(self.redis,RPOP,self.content) # Cleaning queue
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_dequeuing_batch_messages_lpop(self):
        """ Used to test the response when there is batch proccesing using lpop command """
        self.content.incoming_queue_times = 3
        self.assertEqual(f'The message test was added 3 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test, test, test',dequeue_messages(self.redis,LPOP,self.content))

    def test_dequeuing_batch_messages_and_none_values_lpop(self):
        """ Used to test the response when there is batch proccesing and none values using lpop command """
        self.content.incoming_queue_times = 2
        self.assertEqual(f'The message test was added 2 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.content.incoming_queue_times = 4
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test, test',dequeue_messages(self.redis,LPOP,self.content))

    def test_dequeuing_batch_messages_and_empty_list_lpop(self):
        """ Used to test the response when there is batch proccesing and no messages to delete using lpop command """
        self.content.incoming_queue_times = 4
        self.assertEqual(f'No messages to delete from meli list',dequeue_messages(self.redis,LPOP,self.content))
    
    def test_dequeuing_single_message_lpop(self):
        """ Used to test the response when a single message wants to be removed using lpop command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'The message test was added 1 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'The message test was removed from meli list',dequeue_messages(self.redis,LPOP,self.content))

    def test_dequeuing_single_message_and_empty_list_lpop(self):
        """ Used to test the response when the list doesn't have messages using lpop command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'No messages to delete from meli list',dequeue_messages(self.redis,LPOP,self.content))

    def test_dequeuing_batch_messages_rpop(self):
        """ Used to test the response when there is batch proccesing using rpop command """
        self.content.incoming_queue_times = 3
        self.assertEqual(f'The message test was added 3 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test, test, test',dequeue_messages(self.redis,RPOP,self.content))

    def test_dequeuing_batch_messages_and_none_values_rpop(self):
        """ Used to test the response when there is batch proccesing and none values using rpop command """
        self.content.incoming_queue_times = 2
        self.assertEqual(f'The message test was added 2 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.content.incoming_queue_times = 4
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test, test',dequeue_messages(self.redis,RPOP,self.content))

    def test_dequeuing_batch_messages_and_empty_list_rpop(self):
        """ Used to test the response when there is batch proccesing and no messages to delete using rpop command """
        self.content.incoming_queue_times = 4
        self.assertEqual(f'No messages to delete from meli list',dequeue_messages(self.redis,RPOP,self.content))
    
    def test_dequeuing_single_message_rpop(self):
        """ Used to test the response when a single message wants to be removed using rpop command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'The message test was added 1 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'The message test was removed from meli list',dequeue_messages(self.redis,RPOP,self.content))

    def test_dequeuing_single_message_and_empty_list_rpop(self):
        """ Used to test the response when the list doesn't have messages using rpop command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'No messages to delete from meli list',dequeue_messages(self.redis,RPOP,self.content))

    def test_dequeuing_command_not_found(self):
        """ Used to test the dequeuing response when the command does not exist """ 
        with self.assertRaises(HandlingErrors) as e:
            dequeue_messages(self.redis,"notexists",self.content)
        self.assertEqual(f'Command not found',e.exception.message)

    def test_queuing_batch_messages_lpush(self):
        """ Used to test the response when there is batch proccesing using lpush command """
        self.content.incoming_queue_times = 3
        self.assertEqual(f'The message test was added 3 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))

    def test_queuing_single_message_lpush(self):
        """ Used to test the response when a single message is send using lpush command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'The message test was added 1 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))

    def test_queuing_batch_messages_rpush(self):
        """ Used to test the response when there is batch proccesing using rpush command """
        self.content.incoming_queue_times = 3
        self.assertEqual(f'The message test was added 3 time(s) to meli list',queue_messages(self.redis,RPUSH,"test",self.content))

    def test_queuing_single_message_rpush(self):
        """ Used to test the response when a single message is send using rpush command """
        self.content.incoming_queue_times = 1
        self.assertEqual(f'The message test was added 1 time(s) to meli list',queue_messages(self.redis,RPUSH,"test",self.content))

    def test_queuing_command_not_found(self):
        """ Used to test the queuing response when the command does not exist """ 
        with self.assertRaises(HandlingErrors) as e:
            queue_messages(self.redis,"notexists","test",self.content)
        self.assertEqual(f'Command not found',e.exception.message)

    def test_get_length_queue(self):
        """ Used to test geting count messages of a given list """
        self.content.incoming_queue_times = 5
        self.assertEqual(f'The message test was added 5 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'You have 5 message(s) in meli list',get_length_queue(self.redis,LLEN,self.content))

    def test_get_length_queue_command_not_found(self):
        """ Used to test the get length queue response when the command does not exist """ 
        with self.assertRaises(HandlingErrors) as e:
            get_length_queue(self.redis,"notexists",self.content)
        self.assertEqual(f'Command not found',e.exception.message)

    def test_get_message_queue_has_messages(self):
        """ Used to test geting messages of a given list """
        self.content.incoming_queue_times = 2
        self.content.incoming_queue_start = 0
        self.content.incoming_queue_end = -1
        self.assertEqual(f'The message test was added 2 time(s) to meli list',queue_messages(self.redis,LPUSH,"test",self.content))
        self.assertEqual(f'test, test',get_messages_queue(self.redis,LRANGE,self.content))

    def test_get_message_queue_empty_list(self):
        """ Used to test geting messages when the list is empty """
        self.content.incoming_queue_start = 0
        self.content.incoming_queue_end = -1
        self.assertEqual(f'No messages to show from meli list',get_messages_queue(self.redis,LRANGE,self.content))

    def test_get_message_queue_command_not_found(self):
        """ Used to test the get message queue response when the command does not exist """ 
        with self.assertRaises(HandlingErrors) as e:
            get_messages_queue(self.redis,"notexists",self.content)
        self.assertEqual(f'Command not found',e.exception.message)