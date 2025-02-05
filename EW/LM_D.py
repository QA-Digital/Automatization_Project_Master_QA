from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from FW.FM_D import LM_FM_vypis_rozbalit_zajezd_check

from EW.to_import import URL_local
from helpers.helper import Helpers


class TestLM_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None, run_number=None):
        self.run_number = run_number
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayed(self):
        URL_lm_lp = f"{self.URL}{URL_lm}"
        self.driver.maximize_window()

        self.driver.get(URL_lm_lp)

        time.sleep(4.5)
        acceptConsent(self.driver)
        time.sleep(10)
        Helpers.LM_FM_vypis_rozbalit_zajezd_check(self.driver, self.logger)

        self.test_passed = True


