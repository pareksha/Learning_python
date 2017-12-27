import logging

# logging.basicConfig(level=logging.DEBUG, format='%(name)s:%(message)s', filename='log_statements.log')
#
# logging.debug('First log statement')
# logging.debug('Second log statement')

"""
logging can be configured only once (for a particular logger)
means logging.basicConfig can be done only once for a specific logger
"""

# logging.basicConfig(filename='get_logger_code_run.log', level=logging.INFO,
#                     format='%(levelname)s:%(name)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_name = logging.FileHandler('get_logger_code_run.log')
file_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_name.setFormatter(file_formatter)

logger.addHandler(file_name)

# logging into file
logger.info('Created logger, printing from logger')