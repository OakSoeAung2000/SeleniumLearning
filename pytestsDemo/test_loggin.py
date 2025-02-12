import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.debug("Debug statement is executed")
    logger.info("Information")
    logger.warning("Warning Mode")
    logger.error("Test has failed you")
    return logger
