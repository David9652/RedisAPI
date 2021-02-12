import time # Used to take the time spent in each test
import unittest # Used to make the test cases
from errors import HandlingErrors # Used to raise errors
from api.redisconn import create_redis_connection # Used to create a redis connection

class TestRedisConnection(unittest.TestCase):
    """ Used to test scenarios create_redis_connection function """
    def setUp(self):
        """  Method called to prepare the test fixture  """
        self.start = time.time()

    def tearDown(self):
        """ Method called immediately after the test method has been called and the result recorded """ 
        time_spent = time.time() - self.start
        print(f'\nTime taken for {self.id()} was: {time_spent:.6f}s')

    def test_redis_connection_success(self):
        """ Used to test when redis connection has been established """     
        self.assertTrue(create_redis_connection(database=0))

    def test_redis_connection_failed(self):
        """ Used to test when redis has not been established """ 
        with self.assertRaises(HandlingErrors) as e:
            create_redis_connection(database=18)
        self.assertEqual('Error trying to connect to redis server',e.exception.message)