import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from errors import HandlingErrors # Used to raise errors
from api.queue.response import response_pop_single_message, response_pop_batch_message # Used to build response message

class TestResponse(unittest.TestCase):
    """ Used to test scenarios for response_pop_batch_message and response_pop_single_message functions """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()
        self.content = type('MapQueryParameters', (object,), {})() # Creating an empty object to test
        self.content.incoming_queue_list = 'meli'

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_response_pop_batch_message_has_messages(self):
        """ Used to test the response when the list has messages (Batch Message) """
        redis_response_message = [b'test_1', b'test_2', b'test_3']
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test_1, test_2, test_3', response_pop_batch_message(self.content,redis_response_message))

    def test_response_pop_batch_message_has_messages_and_none_values(self):
        """ Used to test the response when the list has messages and none values (Batch Message) """
        redis_response_message = [b'test_1', b'test_2', b'test_3', None, None,]
        self.assertEqual(f'The following message(s) was(were) were removed from meli list: test_1, test_2, test_3', response_pop_batch_message(self.content,redis_response_message))

    def test_response_pop_batch_message_no_message(self):
        """ Used to test the response when the list doesn't have messages to delete (Batch Message) """
        redis_response_message = [None, None, None]
        self.assertEqual(f'No messages to delete from meli list', response_pop_batch_message(self.content,redis_response_message))

    def test_response_pop_batch_message_invalid(self):
        """ Used to test the response when there is an attribute error (Batch Message) """ 
        redis_response_message = 3
        with self.assertRaises(HandlingErrors) as e:
            response_pop_batch_message(self.content,redis_response_message)
        self.assertEqual('Error building response for a batch pop message',e.exception.message)

    def test_response_pop_single_message_has_message(self):
        """ Used to test the response when the list has a message (Single Message) """
        redis_response_message = b'test'
        self.assertEqual(f'The message test was removed from meli list', response_pop_single_message(self.content,redis_response_message))

    def test_response_pop_single_message_no_message(self):
        """ Used to test the response when the list doesn't have a message to delete (Single Message) """ 
        redis_response_message = None
        self.assertEqual(f'No messages to delete from meli list', response_pop_single_message(self.content,redis_response_message))

    def test_response_pop_single_message_invalid(self):
        """ Used to test the response when there is an attribute error (Single Message) """ 
        redis_response_message = 3
        with self.assertRaises(HandlingErrors) as e:
            response_pop_single_message(self.content,redis_response_message)
        self.assertEqual('Error building response for pop single message',e.exception.message)