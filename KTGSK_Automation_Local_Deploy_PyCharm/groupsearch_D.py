from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from KTGSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

from FW_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D



class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.get(URL_groupsearch)
        acceptConsent(self.driver)
        #teaserItems = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        self.driver.maximize_window()
        groupSearch_D(self, driver)
        self.test_passed = True