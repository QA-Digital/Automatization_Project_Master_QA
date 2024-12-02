from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PENNY.to_import import acceptConsent, setUp, tearDown, URL
from selenium.webdriver.support import expected_conditions as EC
import unittest

hlavickaMenuXpath = "//*[@class='inner']"
zlutakHPXpath = "//*[@class='f_filterMainSearch']"
teaserFotkaMainXpath = "//*[@class='object-cover w-full h-full']"
destinationKostkyHPXpath = "//*[@class='c_tile-destination']"
itemsHPXpath ="//*[@class='items']"  ##destination items+3ikony nad patou
footerXpath = "//*[@class='footer-links']"

from PENNY.to_import import URL_local
class Test_HP_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)
        self.test_passed = False

    def tearDown(self):
        tearDown(self)

    def test_HP_D(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        wait = WebDriverWait(self.driver, 25)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, hlavickaMenuXpath)))
        assert (self.driver.find_element(By.XPATH, hlavickaMenuXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, zlutakHPXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, teaserFotkaMainXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, itemsHPXpath)).is_displayed() == True
        assert (self.driver.find_element(By.XPATH, footerXpath)).is_displayed() == True
        #assert(1==2)
        self.test_passed = True