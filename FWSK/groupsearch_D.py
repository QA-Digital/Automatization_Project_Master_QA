from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent, URL_groupsearch, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC

from FW.groupsearch_D import groupSearch_D



from FWSK.to_import import URL_local
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
        URL_groupsearch_lp = f"{self.URL}{URL_groupsearch}"
        self.driver.get(URL_groupsearch_lp)
        acceptConsent(self.driver)
        # teaserItems = driver.find_elements(By.XPATH, "//*[@class='f_teaser-item']")



        groupSearch_D(self, driver)

        self.test_passed = True