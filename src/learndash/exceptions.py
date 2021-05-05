class LearndashException(Exception):

    def __init__(self, message):
        super().__init__(message)
        if message:
            self.message = message
        logging.error(self.message)
