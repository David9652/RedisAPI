import os  # Used to set the environment variable FLASK_ENV
import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from app import create_app # Used to create my application

class TestIntHealthStatusViews(unittest.TestCase):
    """ Used to test scenarios for the integration for health status views """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()
        os.environ["FLASK_ENV"] = 'testing'
        self.app = create_app() # Creating my application
        self.client = self.app.test_client() # Creating client to send requests

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_test_get_redis_health_status(self):
        """ Used to test getting health status """ 
        response_data = self.client.get('/server/status') 
        response_data_json = response_data.get_json()
        self.assertIn('used_memory',response_data_json)
        self.assertEqual(200,response_data.status_code)

    def test_test_get_redis_health_status_specific_section(self):
        """ Used to test getting health status for a specific section """ 
        response_data = self.client.get('/server/status?section=server') 
        response_data_json = response_data.get_json()
        self.assertIn('arch_bits',response_data_json)
        self.assertEqual(200,response_data.status_code)

    def test_test_get_redis_health_status_invalid_section(self):
        """ Used to test getting health status for an invalid section """ 
        response_data = self.client.get('/server/status?section=test') 
        response_data_json = response_data.get_json()
        self.assertIn('used_cpu_sys',response_data_json)
        self.assertEqual(200,response_data.status_code)