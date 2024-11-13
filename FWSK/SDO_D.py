from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FWSK.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown
import time
import unittest

from FWSK.to_import import URL_local
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
        destinaceXpath = "//*[@class='fshr-listTable-item']"
        try:
            destinaceAll = self.driver.find_elements(By.XPATH, destinaceXpath)
            destinaceSingle = self.driver.find_element(By.XPATH, destinaceXpath)
            if destinaceSingle.is_displayed():
                for WebElement in destinaceAll:
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
            msg = "Nenasli se destinace v /stat " + url
            sendEmail(msg)
        assert destinaceAll[0].is_displayed() == True


        try:
            dlazdiceFotoSingle = driver.find_element(By.XPATH, "//*[@class='f_tile-image']")
            dlazdiceFotoAll = driver.find_elements(By.XPATH, "//*[@class='f_tile-image']")
            if dlazdiceFotoSingle.is_displayed():
                for WebElement in dlazdiceFotoAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = driver.current_url
                        msg = "Nenasli se fotky v dlazdicich v /stat " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasli se fotky v dlazdicich v /stat " + url
            sendEmail(msg)

        assert dlazdiceFotoSingle.is_displayed() == True

        try:
            mapa = driver.find_element(By.XPATH, "//*[@class='fshr-map']")
            assert mapa.is_displayed() == True
            if mapa.is_displayed():
                pass
            else:
                url = driver.current_url
                msg = "Nenasli se mapa v /stat " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasli se mapa v /stat " + url
            sendEmail(msg)

        assert mapa.is_displayed() == True

        self.test_passed = True