from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ET.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

from ET.to_import import URL_local
class Test_FM(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_FM(self):
        URL_FM_lp = f"{self.URL}{URL_FM}"
        self.driver.get(URL_FM_lp)
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
                pozice = pozice+1



        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem se zobrazenim stranky " + url
            sendEmail(msg)

        assert stranka[0].is_displayed() == True


