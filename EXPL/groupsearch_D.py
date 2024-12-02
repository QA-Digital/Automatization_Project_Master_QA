from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
from EW.groupsearch_D import groupSearch_D
import unittest
from selenium.webdriver.support import expected_conditions as EC

from EXPL.to_import import URL_local
class Test_Groupsearch_D(unittest.TestCase):
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

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()
        URL_groupsearch_lp = f"{self.URL}{URL_groupsearch}"
        self.driver.get(URL_groupsearch_lp)
        time.sleep(3)
        acceptConsent(self.driver)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True