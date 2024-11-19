from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from EXPL.to_import import acceptConsent, URL, setUp, tearDown, URL_FT_results
import time
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

querySDO = ["Grecja", "Turcja", "Egipt", "Oman", "Malediwy", "Dubaj", "Bulgaria", "Chorwacja", "Portugalia"]
queryHotely = ["Falcon hills", "Aprilis hotel", "Prima life makadi resort", "Myrto hotel", "Cocoon maldives", "Titanic palace"]
queryList = querySDO+queryHotely

from EXPL.to_import import URL_local
class Test_Fulltext_C(unittest.TestCase):
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

    def test_fulltext_naseptavac(self):
        wait = WebDriverWait(self.driver, 25)
        poziceQueryItem = 0
        for _ in queryList:
            self.driver.get(self.URL)

            if poziceQueryItem==0:
                time.sleep(5)
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass

            FTlupa = self.driver.find_element(By.XPATH, "//*[@class='f_anchor f_icon f_icon--magnifier']")
            FTlupa.click()
            inputBox = self.driver.find_element(By.XPATH, "//*[@class='f_input-item j_input']")
            wait.until(EC.visibility_of(inputBox)).send_keys(queryList[poziceQueryItem])
            time.sleep(2)
            self.logger.info(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem+1


            #if self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']").isDisplayed()==True:
            #if hotelDlazdice != 0:

            try:
                wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']")))
                try:

                    hotelDlazdice = self.driver.find_element(By.XPATH, "//*[@class='f_tile f_tile--tour']")  ##work around na EW
                    hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    time.sleep(0.5)
                    self.logger.info("hotel dlazdice klik")
                    assert currentUrl != "https://www.eximtours.cz/"
                    testOK_asserted = True
                except NoSuchElementException:
                    self.logger.info("first no such ele except")
                    testOK_asserted = False
                    pass
            except NoSuchElementException:
                testOK_asserted = False
                pass

            if testOK_asserted == False:
                try:
                    wait.until(EC.visibility_of(self.driver.find_elements(By.XPATH, "//*[@class='f_item']")[0])).click()
                    self.logger.info("last no such ele except")
                    currentUrl = self.driver.current_url
                    assert currentUrl != URL
                    response = requests.get(currentUrl)
                    assert response.status_code == 200

                except NoSuchElementException:
                    self.logger.info("first no such ele except")
                    pass
                time.sleep(0.5)
                currentUrl = self.driver.current_url
                assert currentUrl != URL
            else:
                pass

        self.test_passed = True

    def test_fulltext_results_status_check(self):
        wait = WebDriverWait(self.driver, 13)
        poziceQueryItem=0
        for _ in queryList:
            URL_FT_results_lp = f"{self.URL}{URL_FT_results}"
            self.driver.get(URL_FT_results_lp + queryList[poziceQueryItem])
            if poziceQueryItem==0:
                time.sleep(5)
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass
            self.logger.info(queryList[poziceQueryItem].upper())
            time.sleep(0.6)
            linksToCheckList = []
            try:
                vysledkyDlazdiceHotelu = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid-item']/a")
                x = 0
                for _ in vysledkyDlazdiceHotelu:
                    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                    x = x + 1
            except NoSuchElementException:
                pass
            vysledkyTextItems = self.driver.find_elements(By.XPATH, "//*[@class='f_fulltextResults-item']/a")
            vysledkyTextItemsSingle = self.driver.find_element(By.XPATH, "//*[@class='f_fulltextResults-item']/a")
            wait.until(EC.visibility_of(vysledkyTextItemsSingle))
            z = 0
            for _ in vysledkyTextItems:
                    linksToCheckList.append(vysledkyTextItems[0].text)
                    z = z + 1

            poziceQueryItem=poziceQueryItem+1
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            #for _ in linksToCheckList:
            if len(linksToCheckList) > 5:
                for i in range(5):
                    response = requests.get(linksToCheckList[y])
                    assert response.status_code == 200
                    y = y + 1
            else:
                for _ in linksToCheckList:
                    assert response.status_code == 200
                    y = y + 1

            self.test_passed = True