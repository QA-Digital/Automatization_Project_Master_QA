import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
from EW_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import unittest
from selenium.webdriver.support import expected_conditions as EC

class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(URL_groupsearch)
        time.sleep(3)
        acceptConsent(self.driver)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True