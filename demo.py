from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
# logging.info("Demo script started.")
# print("Logging has started. Check the logs folder.")


try:
    a = 1 / 0
except Exception as e:
    logging.error("An error occurred", exc_info=True)
    raise USvisaException(e, sys) from e

