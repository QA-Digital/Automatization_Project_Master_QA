from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from KTGHU.to_import import acceptConsent, URL, setUp, tearDown, URL_FT_results
import time
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
queryCommon = ["pojištění",  "parkování", "covid", "Funtazie" ]
queryHotely = ["Mirage bay", "mitsis", "Prima life", "Prima life makadi", "Pegasos", "Pickalbatros", "Titanic", "mirage", "Domes Aulüs", "Bay & Mare",  "A for Art",
               "Porto Skala 7", "Costa Azzurra", "La Cite", "Naftilos", "Stefanos", "Magnolia",  "White Gold", "King Tut Resort", "Blue Waters",
               "Primasol", "Doubletree"]

#queryListCz = ["Řecko", "Turecko", "Egypt", "Bulharsko"]
queryList = ["Görögország", "Törökország", "Egyiptom", "Bulgária"]
#queryList = ["covid"]
from KTGHU.to_import import URL_local
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
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass

            FTlupa = self.driver.find_element(By.XPATH, "//*[@class='f_anchor f_icon f_icon--magnifier']")
            FTlupa.click()
            inputBox = self.driver.find_element(By.XPATH, "//*[@class='f_input-item j_input']")
            #inputBox.send_keys(queryList[poziceQueryItem])
            wait.until(EC.visibility_of(inputBox)).send_keys(queryList[poziceQueryItem])
            time.sleep(2)
            # inputBox.send_keys(Keys.ENTER)
            self.logger.info(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem+1


            #if self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']").isDisplayed()==True:
            #if hotelDlazdice != 0:

            try:
                wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']")))
                try:

                    #hotelDlazdice = self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid-item']")
                    hotelDlazdice = self.driver.find_element(By.XPATH, "//*[@class='f_tile f_tile--tour']")  ##work around na EW
                    #wait.until(EC.visibility_of(hotelDlazdice)).click()
                    hotelDlazdice.click()
                    #hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    self.logger.info("hote dlazdice klik")
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
                    #prvniItem = self.driver.find_elements(By.XPATH, "//*[@class='f_item']")
                    wait.until(EC.visibility_of(self.driver.find_elements(By.XPATH, "//*[@class='f_item']")[0])).click()
                    #wait.until(EC.visibility_of(prvniItem[0])).click()
                    #prvniItem[0].click()
                    self.logger.info("last no such ele except")
                    currentUrl = self.driver.current_url
                    assert currentUrl != "https://www.eximtours.cz/"
                    response = requests.get(currentUrl)
                    assert response.status_code == 200

                except NoSuchElementException:
                    self.logger.info("first no such ele except")
                    pass
                currentUrl = self.driver.current_url
                assert currentUrl != "https://www.eximtours.cz/"
            else:
                pass

            #else:
        self.test_passed = True


    def test_fulltext_results_status_check(self):
        wait = WebDriverWait(self.driver, 13)
        poziceQueryItem=0
        for _ in queryList:
            URL_FT_results_lp = f"{self.URL}{URL_FT_results}"
            self.driver.get(URL_FT_results_lp + queryList[poziceQueryItem])
            if poziceQueryItem == 0:
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass
            self.logger.info(queryList[poziceQueryItem].upper())
            linksToCheckList = []
            try:
                vysledkyDlazdiceHotelu = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid-item']/a")
                # wait.until(EC.visibility_of(vysledkyDlazdiceHotelu[0]))
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

            #self.logger.info(linksToCheckList)
            poziceQueryItem=poziceQueryItem+1
            #self.logger.info(len(linksToCheckList))
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            url_index = 0

            # If there are more than 5 links, only check the first 5
            if len(linksToCheckList) > 5:
                for i in range(5):
                    current_url = linksToCheckList[url_index]
                    response = requests.get(current_url)

                    # Check if status is not 200, log the failed URL
                    if response.status_code != 200:
                        self.logger.error(f'Non-200 response for URL {current_url}: {response.status_code}')
                    assert response.status_code == 200, f'Failed URL: {current_url}'

                    url_index += 1
            else:
                # If 5 or fewer links, check all of them
                for current_url in linksToCheckList:
                    response = requests.get(current_url)

                    # Check if status is not 200, log the failed URL
                    if response.status_code != 200:
                        self.logger.error(f'Non-200 response for URL {current_url}: {response.status_code}')
                    assert response.status_code == 200, f'Failed URL: {current_url}'

                    url_index += 1

            # Mark the test as passed if all assertions succeed
            self.test_passed = True