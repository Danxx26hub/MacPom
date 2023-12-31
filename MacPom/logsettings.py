import logging
from functools import wraps
import time


def log_settings(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename="timer.log")
        schedule_logger = logging.getLogger("schedule")
        schedule_logger.setLevel(level=logging.DEBUG)
        start_timestamp = time.time()
        schedule_logger.debug('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        schedule_logger.debug(
            'LOG: Job "%s" completed in %d seconds'
            % (func.__name__, time.time() - start_timestamp)
        )
        return result

    return wrapper
