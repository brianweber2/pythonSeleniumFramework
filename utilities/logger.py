import logging


# https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(filename)s[%(lineno)d] : %(funcName)s : %(message)s")
file_handler = logging.FileHandler('logfile.log')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
