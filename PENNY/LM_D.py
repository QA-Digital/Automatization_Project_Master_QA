from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from PENNY.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, URL_LM, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from PENNY.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

from PENNY.to_import import URL_local
class Test_LM_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_LM_D(self):
        URL_LM_lp = f"{self.URL}{URL_LM}"
        self.driver.get(URL_LM_lp)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        generalDriverWaitImplicit(self.driver)
        assert (self.driver.find_element_by_xpath(destinationXpath)).is_displayed() == True
        self.test_passed = True
