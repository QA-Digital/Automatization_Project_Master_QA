from selenium.common.exceptions import NoSuchElementException
from ET.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

from DERRO.to_import import URL_local
class TestSDO_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SDO_D(self):
        driver = self.driver
        URL_stat_lp = f"{self.URL}{URL_stat}"
        self.driver.get(URL_stat_lp)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        try:
            generalDriverWaitImplicit(self.driver)
            oblastiAll = self.driver.find_elements_by_xpath("//*[contains(@class,'grd-col grd-col--3 grd-col--md-6 grd-col--sm-12')]")
            oblastiSingle = self.driver.find_element_by_xpath("//*[contains(@class,'grd-col grd-col--3 grd-col--md-6 grd-col--sm-12')]")
            if oblastiSingle.is_displayed():
                for WebElement in oblastiAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se destinace v /stat " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblasti " + url
            sendEmail(msg)
        assert oblastiAll[0].is_displayed() == True
        print("Oblasti se zobrazuji")


        try:
            generalDriverWaitImplicit(self.driver)
            oblHotelyAll = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
            oblHotelySingle = self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
            if oblHotelySingle.is_displayed():
                for WebElement in oblHotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se oblibene hotely " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblibene hotely " + url
            sendEmail(msg)
        assert oblHotelyAll[0].is_displayed() == True
        print("Oblibene hotely se zobrazuji")
