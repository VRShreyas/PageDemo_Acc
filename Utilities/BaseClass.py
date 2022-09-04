import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp1")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)
        # the above code __name__ will be replaced by loggerName , coz in logs it will update correct  method name
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\Shreyas_Ratnakar\\PycharmProjects\\PageDemo1\\Utilities'
                                          '\\RunLog.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        # logger.debug("Command executed Successfully.")
        # logger.info("Information statement")
        # logger.debug("A debug statement is executed")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happened")
        # logger.critical("Critical issue")
        return logger
