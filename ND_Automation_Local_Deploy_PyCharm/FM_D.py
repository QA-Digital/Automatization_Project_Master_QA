from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_FM_leto, URL_FM_zima, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

class Test_FM(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_FM_leto(self):
        self.driver.get(URL_FM_leto)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        strankaFM_letoXpath = "//*[@class='grd-row']"
        try:
            stranka = self.driver.find_elements_by_xpath(strankaFM_letoXpath)
            wait.until(EC.visibility_of(stranka[0]))
            pozice = 0
            for i in stranka:
                assert stranka[pozice].is_displayed() == True
                pozice=pozice+1



        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem se zobrazenim stranky " + url
            sendEmail(msg)

        assert stranka[0].is_displayed() == True


    def test_FM_zima(self):
        self.driver.get(URL_FM_zima)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        strankaFM_zimaXpath = "//*[@class='grd-row']"
        try:
            stranka = self.driver.find_elements_by_xpath(strankaFM_zimaXpath)
            wait.until(EC.visibility_of(stranka[0]))
            pozice = 0
            for i in stranka:
                assert stranka[pozice].is_displayed() == True
                pozice = pozice + 1

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem se zobrazenim stranky " + url
            sendEmail(msg)

        assert stranka[0].is_displayed() == True


