from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from FW.HP_C import *
from FW.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown
import time
import unittest
from FW.groupsearch_D import groupSearch_D

from FW.to_import import URL_local

class TestSDO_C(unittest.TestCase):

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
        self.driver.maximize_window()
        URL_stat_lp = f"{self.URL}{URL_stat}"
        self.driver.get(URL_stat_lp)

        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(3.5)
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

            #mapa = driver.find_element(By.XPATH, "//*[@id='google-map']")
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


    def test_SDO_zlutak_to_SRL_R(self): ### https://jira.fischer.cz/browse/FW-1689
        self.driver.maximize_window()
        URL_stat_lp = f"{self.URL}{URL_stat}"
        self.driver.get(URL_stat_lp)

        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(3.5)
        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath, 2, True)

        Helpers.search_results_list_check(self.driver, self.logger)
        #groupSearch_D(self, self.driver)