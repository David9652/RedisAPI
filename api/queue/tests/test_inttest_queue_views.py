import os  # Used to set the environment variable FLASK_ENV
import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from app import create_app # Used to create my application

class TestIntQueueViews(unittest.TestCase):
    """ Used to test scenarios for the integration for queue views """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()
        os.environ["FLASK_ENV"] = 'testing'
        self.app = create_app() # Creating my application
        self.client = self.app.test_client() # Creating client to send requests

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        self.client.post('/queue/lpop?times=200') # Cleaning queue
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_lpop_batch_message_default_parameters_empty_list(self):
        """ Used to test the response for batch message with default parameters and empty list using lpop command """
        response_data = self.client.post('/queue/lpop?times=15') 
        response_data_json = response_data.get_json()
        self.assertEqual('No messages to delete from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpop_batch_message_has_messages_and_none_values(self):
        """ Used to test the response for batch message with none values using lpop command """
        response_data_push = self.client.post('/queue/lpush?times=2', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 2 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/lpop?times=5') 
        response_data_json = response_data.get_json()
        self.assertEqual('The following message(s) was(were) were removed from meli list: test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpop_batch_message_specific_list_and_db_has_messages(self):
        """ Used to test the response for batch message with a specific list and database using lpop command """
        response_data_push = self.client.post('/queue/lpush?times=10&list=david&db=7', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 10 time(s) to david list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/lpop?times=5&list=david&db=7') 
        response_data_json = response_data.get_json()
        self.assertEqual('The following message(s) was(were) were removed from david list: test, test, test, test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpop_single_message_default_parameters_has_messages(self):
        """ Used to test the response for a single message with default parameters using lpop command """
        response_data_push = self.client.post('/queue/lpush', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 1 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/lpop') 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was removed from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpop_single_message_default_parameters_empty_list(self):
        """ Used to test the response for a single message with default parameters and empty list using lpop command """
        response_data = self.client.post('/queue/lpop') 
        response_data_json = response_data.get_json()
        self.assertEqual('No messages to delete from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpop_batch_message_default_parameters_empty_list(self):
        """ Used to test the response for batch message with default parameters and empty list using rpop command """
        response_data = self.client.post('/queue/rpop?times=15') 
        response_data_json = response_data.get_json()
        self.assertEqual('No messages to delete from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpop_batch_message_has_messages_and_none_values(self):
        """ Used to test the response for batch message with none values using rpop command """
        response_data_push = self.client.post('/queue/rpush?times=2', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 2 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/rpop?times=5') 
        response_data_json = response_data.get_json()
        self.assertEqual('The following message(s) was(were) were removed from meli list: test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpop_batch_message_specific_list_and_db_has_messages(self):
        """ Used to test the response for batch message with a specific list and database using rpop command """
        response_data_push = self.client.post('/queue/rpush?times=10&list=david&db=7', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 10 time(s) to david list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/rpop?times=5&list=david&db=7') 
        response_data_json = response_data.get_json()
        self.assertEqual('The following message(s) was(were) were removed from david list: test, test, test, test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpop_single_message_default_parameters_has_messages(self):
        """ Used to test the response for a single message with default parameters using rpop command """
        response_data_push = self.client.post('/queue/rpush', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 1 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.post('/queue/rpop') 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was removed from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpop_single_message_default_parameters_empty_list(self):
        """ Used to test the response for a single message with default parameters and empty list using rpop command """
        response_data = self.client.post('/queue/rpop') 
        response_data_json = response_data.get_json()
        self.assertEqual('No messages to delete from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpush_single_message_default_parameters(self):
        """ Used to test the response for a single message with default parameters using lpush command """
        response_data = self.client.post('/queue/lpush', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 1 time(s) to meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpush_single_message_specific_list(self):
        """ Used to test the response for a single message with a specific list using lpush command """
        response_data = self.client.post('/queue/lpush?list=david', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 1 time(s) to david list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpush_batch_message(self):
        """ Used to test the response for a batch message using lpush command """
        response_data = self.client.post('/queue/lpush?times=10', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 10 time(s) to meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lpush_invalid_structure(self):
        """ Used to test the response for an invalid structure using lpush command """
        response_data = self.client.post('/queue/lpush', json={
        'invalid': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('Your request does not have a valid structure',response_data_json['message'])
        self.assertEqual(404,response_data.status_code)

    def test_rpush_single_message_default_parameters(self):
        """ Used to test the response for a single message with default parameters using rpush command """
        response_data = self.client.post('/queue/rpush', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 1 time(s) to meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpush_single_message_specific_list(self):
        """ Used to test the response for a single message with a specific list using rpush command """
        response_data = self.client.post('/queue/rpush?list=david', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 1 time(s) to david list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpush_batch_message(self):
        """ Used to test the response for a batch message using rpush command """
        response_data = self.client.post('/queue/rpush?times=10', json={
        'message': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('The message test was added 10 time(s) to meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_rpush_invalid_structure(self):
        """ Used to test the response for an invalid structure using rpush command """
        response_data = self.client.post('/queue/rpush', json={
        'invalid': 'test'
         }) 
        response_data_json = response_data.get_json()
        self.assertEqual('Your request does not have a valid structure',response_data_json['message'])
        self.assertEqual(404,response_data.status_code)

    def test_llen_get_length_queue(self):
        """ Used to test getting the length of a given list using llen command """
        response_data_push = self.client.post('/queue/lpush?times=10', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 10 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.get('/queue/count') 
        response_data_json = response_data.get_json()
        self.assertEqual('You have 10 message(s) in meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_llen_get_length_queue_empty_list(self):
        """ Used to test getting the length of an empty list using llen command """
        response_data = self.client.get('/queue/count?list=david&db=10')
        response_data_json = response_data.get_json()
        self.assertEqual('You have 0 message(s) in david list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lrange_get_messages_queue(self):
        """ Used to test getting all the messages of a given list using lrange command """
        response_data_push = self.client.post('/queue/lpush?times=10', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 10 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.get('/queue/lrange') 
        response_data_json = response_data.get_json()
        self.assertEqual('test, test, test, test, test, test, test, test, test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lrange_get_half_messages_queue(self):
        """ Used to test getting half of the messages of a given list using lrange command """
        response_data_push = self.client.post('/queue/lpush?times=10', json={
        'message': 'test'
        }) 
        response_data_push_json = response_data_push.get_json()
        self.assertEqual('The message test was added 10 time(s) to meli list',response_data_push_json['message'])
        self.assertEqual(200,response_data_push.status_code)
        response_data = self.client.get('/queue/lrange?start=2&end=-3') 
        response_data_json = response_data.get_json()
        self.assertEqual('test, test, test, test, test, test',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)

    def test_lrange_get_messages_queue_empty_list(self):
        """ Used to test getting messages of a given list when it's empty using lrange command """
        response_data = self.client.get('/queue/lrange?start=2&end=-3') 
        response_data_json = response_data.get_json()
        self.assertEqual('No messages to show from meli list',response_data_json['message'])
        self.assertEqual(200,response_data.status_code)