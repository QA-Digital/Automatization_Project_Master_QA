from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ND.to_import import acceptConsent, URL_FM_leto, URL_FM_zima, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

from ND.to_import import URL_local
class Test_FM(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None, run_number=None):
        self.run_number = run_number
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_FM_leto(self):
        URL_FM_leto_lp = f"{self.URL}{URL_FM_leto}"
        self.driver.get(URL_FM_leto_lp)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        strankaFM_letoXpath = "//*[@class='grd-row']"
        try:
            stranka = self.driver.find_elements(By.XPATH, strankaFM_letoXpath)
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
        URL_FM_zima_lp = f"{self.URL}{URL_FM_zima}"
        self.driver.get(URL_FM_zima_lp)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        strankaFM_zimaXpath = "//*[@class='grd-row']"
        try:
            stranka = self.driver.find_elements(By.XPATH, strankaFM_zimaXpath)
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


