import unittest # Used to make the test cases
from api.tests.test_unittest_redisconn import TestRedisConnection # Used to test scenarios create_redis_connection function 
from api.queue.tests.test_inttest_queue import TestIntQueue # Used to test scenarios for the integration between create_redis_connection, dequeue_messages, queue_messages, get_length_queue, get_messages_queue, response_pop_batch_message and response_pop_single_message functions
from api.queue.tests.test_inttest_queue_views import TestIntQueueViews # Used to test scenarios for the integration between create_redis_connection, dequeue_messages, queue_messages, get_length_queue, get_messages_queue, response_pop_batch_message and response_pop_single_message functions
from api.queue.tests.test_unittest_response import TestResponse # Used to test scenarios for response_pop_batch_message and response_pop_single_message functions
from api.server.tests.test_inttest_healthstatus import TestIntHealthStatus # Used to test scenarios for the integration between create_redis_connection and get_health_status functions
from api.server.tests.test_inttest_healthstatus_views import TestIntHealthStatusViews # Used to test scenarios for the integration for health status views

SUITE = (TestRedisConnection,TestIntQueue,TestIntQueueViews,TestResponse,TestIntHealthStatus,TestIntHealthStatusViews) # Collection of test classes

def test_suite_all():
    """ Used to load the scenarios for all the test cases built """
    test_suite = [] # Initialazing list
    for suite_test in SUITE:
        test_suite.append(unittest.TestLoader().loadTestsFromTestCase(suite_test)) # Loading test classes
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_inttest_queue():
    """ Used to load scenarios for the integration between create_redis_connection, dequeue_messages, queue_messages, get_length_queue, get_messages_queue, response_pop_batch_message and response_pop_single_message functions """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestIntQueue)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_inttest_queue_dequeuing():
    """ Used to load the scenarios for dequeue_messages function """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_none_values_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_empty_list_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_and_empty_list_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_none_values_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_empty_list_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_and_empty_list_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_command_not_found'))
    return test_suite

def test_suite_inttest_queue_dequeuing_lpop():
    """ Used to load the scenarios for dequeue_messages function, lpop command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_none_values_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_empty_list_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_lpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_and_empty_list_lpop'))
    return test_suite

def test_suite_inttest_queue_dequeuing_rpop():
    """ Used to load the scenarios for dequeue_messages function, rpop command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_none_values_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_batch_messages_and_empty_list_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_rpop'))
    test_suite.addTest(TestIntQueue('test_dequeuing_single_message_and_empty_list_rpop'))
    return test_suite

def test_suite_inttest_queue_queuing():
    """ Used to load the scenarios for queue_messages function"""
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_queuing_batch_messages_lpush'))
    test_suite.addTest(TestIntQueue('test_queuing_single_message_lpush'))
    test_suite.addTest(TestIntQueue('test_queuing_batch_messages_rpush'))
    test_suite.addTest(TestIntQueue('test_queuing_single_message_rpush'))
    test_suite.addTest(TestIntQueue('test_queuing_command_not_found'))
    return test_suite
    
def test_suite_inttest_queue_queuing_lpush():
    """ Used to load the scenarios for queue_messages function, lpush command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_queuing_batch_messages_lpush'))
    test_suite.addTest(TestIntQueue('test_queuing_single_message_lpush'))
    return test_suite

def test_suite_inttest_queue_queuing_rpush():
    """ Used to load the scenarios for queue_messages function, rpush command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_queuing_batch_messages_rpush'))
    test_suite.addTest(TestIntQueue('test_queuing_single_message_rpush'))
    return test_suite

def test_suite_inttest_queue_get_length_queue():
    """ Used to load the scenarios for get_length_queue function, llen command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_get_length_queue'))
    test_suite.addTest(TestIntQueue('test_get_length_queue_command_not_found'))
    return test_suite

def test_suite_inttest_queue_get_messages_queue():
    """ Used to load the scenarios for get_messages_queue function, llen command """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueue('test_get_message_queue_has_messages'))
    test_suite.addTest(TestIntQueue('test_get_message_queue_empty_list'))
    test_suite.addTest(TestIntQueue('test_get_message_queue_command_not_found'))
    return test_suite

def test_suite_unittest_redisconn():
    """ Used to load scenarios create_redis_connection function """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestRedisConnection)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_inttest_queue_views():
    """ Used to test scenarios for the integration for queue views """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestIntQueueViews)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_inttest_queue_views_lpop():
    """ Used to test scenarios for the integration for lpop queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_lpop_batch_message_default_parameters_empty_list'))
    test_suite.addTest(TestIntQueueViews('test_lpop_batch_message_has_messages_and_none_values'))
    test_suite.addTest(TestIntQueueViews('test_lpop_batch_message_specific_list_and_db_has_messages'))
    test_suite.addTest(TestIntQueueViews('test_lpop_single_message_default_parameters_has_messages'))
    test_suite.addTest(TestIntQueueViews('test_lpop_single_message_default_parameters_empty_list'))
    return test_suite

def test_suite_inttest_queue_views_rpop():
    """ Used to test scenarios for the integration for rpop queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_rpop_batch_message_default_parameters_empty_list'))
    test_suite.addTest(TestIntQueueViews('test_rpop_batch_message_has_messages_and_none_values'))
    test_suite.addTest(TestIntQueueViews('test_rpop_batch_message_specific_list_and_db_has_messages'))
    test_suite.addTest(TestIntQueueViews('test_rpop_single_message_default_parameters_has_messages'))
    test_suite.addTest(TestIntQueueViews('test_rpop_single_message_default_parameters_empty_list'))
    return test_suite

def test_suite_inttest_queue_views_lpush():
    """ Used to test scenarios for the integration for lpush queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_lpush_single_message_default_parameters'))
    test_suite.addTest(TestIntQueueViews('test_lpush_single_message_specific_list'))
    test_suite.addTest(TestIntQueueViews('test_lpush_batch_message'))
    test_suite.addTest(TestIntQueueViews('test_lpush_invalid_structure'))
    return test_suite

def test_suite_inttest_queue_views_rpush():
    """ Used to test scenarios for the integration for rpush queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_rpush_single_message_default_parameters'))
    test_suite.addTest(TestIntQueueViews('test_rpush_single_message_specific_list'))
    test_suite.addTest(TestIntQueueViews('test_rpush_batch_message'))
    test_suite.addTest(TestIntQueueViews('test_rpush_invalid_structure'))
    return test_suite

def test_suite_inttest_queue_views_llen():
    """ Used to test scenarios for the integration for llen queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_llen_get_length_queue'))
    test_suite.addTest(TestIntQueueViews('test_llen_get_length_queue_empty_list'))
    return test_suite

def test_suite_inttest_queue_views_lrange():
    """ Used to test scenarios for the integration for lrange queue view """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestIntQueueViews('test_lrange_get_messages_queue'))
    test_suite.addTest(TestIntQueueViews('test_lrange_get_half_messages_queue'))
    test_suite.addTest(TestIntQueueViews('test_lrange_get_messages_queue_empty_list'))
    return test_suite     

def test_suite_unittest_response():
    """ Used to load the scenarios for response_pop_batch_message and response_pop_single_message functions """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestResponse)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_unittest_response_pop_batch_message():
    """ Used to load the scenarios for response_pop_batch_message function """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestResponse('test_response_pop_batch_message_has_messages'))
    test_suite.addTest(TestResponse('test_response_pop_batch_message_has_messages_and_none_values'))
    test_suite.addTest(TestResponse('test_response_pop_batch_message_no_message'))
    test_suite.addTest(TestResponse('test_response_pop_batch_message_invalid'))
    return test_suite

def test_suite_unittest_response_pop_single_message():
    """ Used to load the scenarios for response_pop_single_message function """
    test_suite = unittest.TestSuite()
    # Adding test cases to the suite
    test_suite.addTest(TestResponse('test_response_pop_single_message_has_message'))
    test_suite.addTest(TestResponse('test_response_pop_single_message_no_message'))
    test_suite.addTest(TestResponse('test_response_pop_single_message_invalid'))
    return test_suite

def test_suite_inttest_healthstatus():
    """ Used to load scenarios for the integration between create_redis_connection and get_health_status functions """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestIntHealthStatus)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

def test_suite_inttest_healthstatus_views():
    """ Used to test scenarios for the integration for health status views """
    test_suite = [] # Initialazing list
    test_suite.append(unittest.TestLoader().loadTestsFromTestCase(TestIntHealthStatusViews)) # Loading test class
    test_suite = unittest.TestSuite(test_suite) # Creating a test suite
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite_all())
#   runner.run(test_suite_inttest_queue())
#   runner.run(test_suite_inttest_queue_dequeuing())
#   runner.run(test_suite_inttest_queue_dequeuing_lpop())
#   runner.run(test_suite_inttest_queue_dequeuing_rpop())
#   runner.run(test_suite_inttest_queue_queuing())
#   runner.run(test_suite_inttest_queue_queuing_lpush())
#   runner.run(test_suite_inttest_queue_queuing_rpush())
#   runner.run(test_suite_inttest_queue_get_length_queue())
#   runner.run(test_suite_inttest_queue_get_messages_queue())
#   runner.run(test_suite_unittest_redisconn())
#   runner.run(test_suite_inttest_queue_views())
#   runner.run(test_suite_inttest_queue_views_lpop())
#   runner.run(test_suite_inttest_queue_views_rpop())
#   runner.run(test_suite_inttest_queue_views_lpush())
#   runner.run(test_suite_inttest_queue_views_rpush())
#   runner.run(test_suite_inttest_queue_views_llen())
#   runner.run(test_suite_inttest_queue_views_lrange())
#   runner.run(test_suite_unittest_response())
#   runner.run(test_suite_unittest_response_pop_batch_message())
#   runner.run(test_suite_unittest_response_pop_single_message())
#   runner.run(test_suite_inttest_healthstatus())
#   runner.run(test_suite_inttest_healthstatus_views())