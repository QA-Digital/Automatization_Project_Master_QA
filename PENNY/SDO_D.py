from selenium.webdriver.common.by import By
from PENNY.to_import import acceptConsent,URL_SDO, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest
from PENNY.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D

SDOsectionXpath = "//*[@class='sdo-section']"
zobrazitHotelyXpath = "//*[@class='c_title mb-0 center']"
def SDO_D(self, driver):
    generalDriverWaitImplicit(driver)
    rowKarty_imgHoteluKarty_D(self, driver)

    SDOsectionElement = driver.find_element(By.XPATH, SDOsectionXpath)

    assert SDOsectionElement.is_displayed() == True
    print("sdo section visible true :  " + str(SDOsectionElement.is_displayed()))
from PENNY.to_import import URL_local
class TestSDO_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SDO_D(self):
        self.driver.maximize_window()
        URL_SDO_lp = f"{self.URL}{URL_SDO}"
        self.driver.get(URL_SDO_lp)

        time.sleep(0.3)
        acceptConsent(self.driver)
        time.sleep(2)
        zobrazitHotelyElement = self.driver.find_element(By.XPATH, zobrazitHotelyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", zobrazitHotelyElement)
        time.sleep(2.7)
        SDO_D(self, self.driver)

        self.test_passed = True


