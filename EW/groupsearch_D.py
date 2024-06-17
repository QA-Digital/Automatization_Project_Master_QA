import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

from FW.groupsearch_D import groupSearch_D


from FW.to_import import URL_local
class Test_Groupsearch_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
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
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(2.5)
        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True