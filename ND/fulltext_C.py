from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from ND.to_import import acceptConsent, URL, setUp, tearDown, URL_FT_results
import time
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

querySDO = ["Chorvatsko", "Italie", "Rakousko", "Slovensko", "Francie", "Maďarsko", "Španělsko"]
queryHotely = ["Aparthotel Der Brückenwirt", "Apartmánový dům Dick", "Landgasthof Dorferwirt", "Gasthof Lukashansl", "Hotel Heitzmann", "Spa Resort Sanssouci", "SPA Hotel Děvín", "Wellness Hotel Astra", "Apt. dům Strobl",  "Residence Silvia",
               "Active Hotel Rosat", "Hotel Trunka Lunka", "Bungalovy Club Tihany", "Hotel Magistern", "Hotel Club Tihany",  "Hotel Zenit", "Hotel Pelion", "Hotel Aphrodite"]
queryList = querySDO+queryHotely

from ND.to_import import URL_local
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
            self.driver.get(URL)

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
            time.sleep(4)
            self.logger.info(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem+1


            try:
                wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']")))
                try:

                    hotelDlazdice = self.driver.find_element(By.XPATH, "//*[@class='f_tile f_tile--tour']")
                    hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    time.sleep(2)
                    self.logger.info("hote dlazdice klik")
                    assert currentUrl != "https://nev-dama.uat.dtweb.cz/"
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
                    assert currentUrl != "https://nev-dama.uat.dtweb.cz/"
                    response = requests.get(currentUrl)
                    assert response.status_code == 200

                except NoSuchElementException:
                    self.logger.info("first no such ele except")
                    pass
                time.sleep(2)
                currentUrl = self.driver.current_url
                assert currentUrl != "https://nev-dama.uat.dtweb.cz/"
            else:
                pass

        self.test_passed = True

    def test_fulltext_results_status_check(self):
        wait = WebDriverWait(self.driver, 13)
        poziceQueryItem=0
        for _ in queryList:
            driver = self.driver
            driver.get(URL_FT_results+queryList[poziceQueryItem])
            if poziceQueryItem==0:
                time.sleep(5)
                acceptConsent(driver)
                self.driver.maximize_window()
            else:
                pass
            self.logger.info(queryList[poziceQueryItem].upper())
            time.sleep(0.6)
            linksToCheckList = []

            try:
                vysledkyDlazdiceHotelu = driver.find_elements(By.XPATH, "//*[@class='f_tileGrid-item']/a")
               # wait.until(EC.visibility_of(vysledkyDlazdiceHotelu[0]))
                x = 0
                for _ in vysledkyDlazdiceHotelu:
                    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                    x = x + 1
            except NoSuchElementException:
                pass
            vysledkyTextItems = driver.find_elements(By.XPATH, "//*[@class='f_fulltextResults-item']/a")
            vysledkyTextItemsSingle = driver.find_element(By.XPATH, "//*[@class='f_fulltextResults-item']/a")
            wait.until(EC.visibility_of(vysledkyTextItemsSingle))
            z = 0
            for _ in vysledkyTextItems:
                    linksToCheckList.append(vysledkyTextItems[0].text)
                    z = z + 1

            poziceQueryItem=poziceQueryItem+1
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            if len(linksToCheckList) > 5:
                for i in range(5):
                    response = requests.get(linksToCheckList[y])
                    self.logger.info(linksToCheckList[y])
                    self.logger.info(response)
                    assert response.status_code == 200
                    y = y + 1
            else:
                for _ in linksToCheckList:
                    assert response.status_code == 200
                    y = y + 1

            self.test_passed = True