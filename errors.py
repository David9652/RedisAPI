import logging  # Used to write logs throughout the application
from flask import jsonify # Used to build a flask response

class HandlingErrors(Exception): # 
    """ All user-defined exceptions should be derived from 'Exception' class. Used to handle any unexpected behavior """

    def __init__(self, message, status_code):
        """ Used to define the HandlingErrors constructor """

        super().__init__(self) # Calling 'Exception' constructor
        self.message = message
        self.status_code = status_code

    def to_json(self):
        """ Used to build a flask response object and show an error """

        logging.info('START')
        logging.info('Building response error message')

        error_message = {}
        error_message['message'] = self.message
        response = jsonify(error_message) 
        response.status_code = self.status_code

        logging.error(f"message: {self.message}, status code: {self.status_code}")
        logging.info('Response built')
        logging.info('END')

        return response