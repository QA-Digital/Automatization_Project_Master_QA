from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from EXPL.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

NejHotely = "//*[@class='f_tileGrid-item']"
from EXPL.to_import import URL_local
class TestSDO_D(unittest.TestCase):
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

    def test_SDO_D(self):
        driver = self.driver
        URL_stat_lp = f"{self.URL}{URL_stat}"
        self.driver.get(URL_stat_lp)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        Offer1 = self.driver.find_elements(By.XPATH, "(//a)[59]")[0].get_attribute('href')
        Offer2 = self.driver.find_elements(By.XPATH, "(//a)[60]")
        Offer3 = self.driver.find_elements(By.XPATH, "(//a)[61]")
        Offer4 = self.driver.find_elements(By.XPATH, "(//a)[62]")

        HPtopNabidkaElements = [Offer1, Offer2, Offer3, Offer4]
        self.logger.info(HPtopNabidkaElements)
        time.sleep(4)
        linksToCheck_List = []
        for _ in HPtopNabidkaElements:
           odkazLink = HPtopNabidkaElements
           linksToCheck_List.append(odkazLink)
           self.logger.info(odkazLink)

    def test_SDO_NejHotely(self):
        self.driver.maximize_window()
        URL_stat_lp = f"{self.URL}{URL_stat}"
        self.driver.get(URL_stat_lp)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        NejHotelyElement = self.driver.find_element(By.XPATH, NejHotely)
        self.driver.execute_script("arguments[0].scrollIntoView();", NejHotelyElement)
        time.sleep(5)
        NejHotelyElement.click()

        try:
            NejHotelyS = self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']")
            NejHotelyAll = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid-item']")
            if NejHotelyS.is_displayed():
                for WebElement in NejHotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        self.logger.info("Hotely jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, hotely se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, hotely se nezobrazuji " + url
            sendEmail(msg)

        assert NejHotelyS.is_displayed() == True

