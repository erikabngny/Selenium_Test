"""
Logging Demo 1
Logging Levels
Debug
Info
Warning
Error
Critical
"""

import logging

# logging.warning("warning message")
# logging.info("info message")
# logging.error("error message")

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")