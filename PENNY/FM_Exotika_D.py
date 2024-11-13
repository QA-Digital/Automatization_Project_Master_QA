from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from PENNY.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, URL_exotika, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from PENNY.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

from PENNY.to_import import URL_local
class Test_FM_Exotika_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_D(self):
        URL_FM_lp = f"{self.URL}{URL_FM}"
        self.driver.get(URL_FM_lp)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        assert (self.driver.find_element(By.XPATH, imgHotelKartaXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, destinationXpath)).is_displayed() == True
        #assert (self.driver.find_element(By.XPATH, gridDestinationXpath)).is_displayed() == True
        self.test_passed = True


    def test_Exotika_D(self):
        URL_exotika_lp = f"{self.URL}{URL_exotika}"
        self.driver.get(URL_exotika_lp)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        assert (self.driver.find_element(By.XPATH, imgHotelKartaXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, gridDestinationXpath)).is_displayed() == True
        self.test_passed = True
