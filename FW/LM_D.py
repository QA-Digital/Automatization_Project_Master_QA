from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from FW.FM_D import LM_FM_vypis_rozbalit_zajezd_check
from helpers.helper import *

from FW.to_import import URL_local

class TestLM_D(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        URL_lm_lp = f"{self.URL}{URL_lm}"
        self.driver.get(URL_lm_lp)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        #LM_FM_vypis_rozbalit_zajezd_check(self, self.driver)
        Helpers.LM_FM_vypis_rozbalit_zajezd_check(self.driver, self.logger)

        self.test_passed = True

