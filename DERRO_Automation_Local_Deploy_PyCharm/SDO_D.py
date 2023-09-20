from selenium.common.exceptions import NoSuchElementException
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SDO_D(self):
        driver = self.driver
        self.driver.get(URL_stat)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        try:
            generalDriverWaitImplicit(self.driver)
            destinaceAll = self.driver.find_elements_by_xpath("//*[@class='fshr-listTable-content-part']")
            destinaceSingle = self.driver.find_element_by_xpath("//*[@class='fshr-listTable-content-part']")
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
            dlazdiceFotoSingle = driver.find_element_by_xpath("//*[@class='f_tile-image']")
            dlazdiceFotoAll = driver.find_elements_by_xpath("//*[@class='f_tile-image']")
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
            mapa = driver.find_element_by_xpath("//*[@class='fshr-map']")
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