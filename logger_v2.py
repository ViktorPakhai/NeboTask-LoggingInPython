import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define the log format
log_format = '[%(asctime)s] %(levelname)s [%(filename)s %(name)s %(funcName)s (%(lineno)d)]: %(message)s'
formatter = logging.Formatter(log_format)

# Create a file handler
log_file = 'my_log_file.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Example log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
