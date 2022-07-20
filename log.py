import logging
import sys

'''
Logging Request and Responses from Database 
and Program
'''
class Logger:
    def __init__(self):
        # Initiating the logger object
        self.logger = logging.getLogger(__name__)
        
        #type of log
        self.logger.setLevel(logging.DEBUG)
        
        # Create the log file
        handler = logging.FileHandler('logs.log')

        # Format the logs
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Adding the format handler
        self.logger.addHandler(handler)
        
        # And printing the logs to the console as well
        self.logger.addHandler(logging.StreamHandler(sys.stdout))


# Usage example for future reference:
#logger = Logger().logger
#logger.debug("This log's level is 'DEBUG'")
#logger.info("This log's level is 'info'")
#logger.error("This log's level is 'error'")
