import logging

class LearndashException(Exception):

    def __init__(self, message=None):
        super().__init__(message)
        if message:
            self.message = message
        logging.error(self.message)
