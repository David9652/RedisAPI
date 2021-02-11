import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from errors import HandlingErrors # Used to raise errors
from api.redisconn import create_redis_connection # Used to create a redis connection
from api.server.healthstatus import get_health_status # Used to get the health status of redis server
from api.server.constant import STATUS, INFO # Used to verifiy the status sent

class TestIntHealthStatus(unittest.TestCase):
    """ Used to test scenarios for the integration between create_redis_connection and get_health_status functions """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()
        self.redis = create_redis_connection(0)

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_get_redis_health_status_allowed_sections(self):
        """ Used to test when redis connection has been established and get the information for each value allowed """ 
        for section in STATUS:
            self.assertTrue(get_health_status(self.redis,INFO,section))

    def test_get_redis_health_status_no_section(self):
        """ Used to test when redis connection has been established and the section does not exist """ 
        self.assertTrue(get_health_status(self.redis,INFO,"notexists"))

    def test_get_redis_health_status_command_not_found(self):
        """ Used to test when redis connection has been established and the command does not exist """ 
        with self.assertRaises(HandlingErrors) as e:
            get_health_status(self.redis,"test",STATUS[0])
        self.assertEqual(f'Command not found',e.exception.message)