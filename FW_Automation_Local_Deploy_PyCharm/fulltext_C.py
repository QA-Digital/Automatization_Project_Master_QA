from selenium.common.exceptions import NoSuchElementException
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, URL_FT_results
import time
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_master import queryListOptimizedMonitor
query = "Mirage bay"


querySDO = ["Zanzibar", "Řecko", "Turecko", "Egypt", "Kapverdy", "Oman" , "Maledivy", "Dubaj", "Mallorca", "Bulharsko", "Chorvatsko", "Kefalonia", "Attika" ]
queryCommon = ["pojištění",  "parkování", "covid", "Funtazie" ]
queryHotely = ["Mirage bay", "mitsis", "Prima life", "Prima life makadi", "Pegasos", "Pickalbatros", "Titanic", "mirage", "Domes Aulüs", "Bay & Mare",  "A for Art",
               "Porto Skala 7", "Costa Azzurra", "La Cite", "Naftilos", "Stefanos", "Magnolia",  "White Gold", "King Tut Resort", "Blue Waters",
               "Primasol", "Doubletree"]
#queryList = querySDO+queryCommon+queryHotely
queryList =queryListOptimizedMonitor
from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local

class Test_Fulltext_C(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_fulltext_naseptavac(self):
        wait = WebDriverWait(self.driver, 35)
        poziceQueryItem = 0
        for _ in queryList:

            self.driver.get(self.URL)

            if poziceQueryItem == 0:
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass

            FTlupa = self.driver.find_element_by_xpath("//*[@class='f_anchor f_icon f_icon--magnifier']")
            FTlupa.click()
            inputBox = self.driver.find_element_by_xpath("//*[@class='f_input-item j_input']")
            # inputBox.send_keys(queryList[poziceQueryItem])
            wait.until(EC.visibility_of(inputBox)).send_keys(queryList[poziceQueryItem])
            time.sleep(2)
            # inputBox.send_keys(Keys.ENTER)
            print(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem + 1

            # if self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']").isDisplayed()==True:
            # if hotelDlazdice != 0:

            try:
                wait.until(EC.visibility_of(self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")))
                try:

                    # hotelDlazdice = self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
                    hotelDlazdice = self.driver.find_element_by_xpath(
                        "//*[@class='f_tile f_tile--tour']")  ##work around na EW
                    # wait.until(EC.visibility_of(hotelDlazdice)).click()
                    hotelDlazdice.click()
                    # hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    print("hote dlazdice klik")
                    assert currentUrl != URL
                    testOK_asserted = True
                except NoSuchElementException:
                    print("first no such ele except")
                    testOK_asserted = False
                    pass
            except NoSuchElementException:
                testOK_asserted = False
                pass

            if testOK_asserted == False:
                try:
                    #prvniItem =
                    wait.until(EC.visibility_of(self.driver.find_elements_by_xpath("//*[@class='f_item']")[0])).click()
                    # prvniItem[0].click()
                    print("last no such ele except")
                    currentUrl = self.driver.current_url
                    assert currentUrl != URL
                    response = requests.get(currentUrl)
                    assert response.status_code == 200

                except NoSuchElementException:
                    print("first no such ele except")
                    pass
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
            if poziceQueryItem == 0:
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass
            print(queryList[poziceQueryItem].upper())
            linksToCheckList = []
            try:
                vysledkyDlazdiceHotelu = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']/a")
                # wait.until(EC.visibility_of(vysledkyDlazdiceHotelu[0]))
                x = 0
                for _ in vysledkyDlazdiceHotelu:
                    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                    x = x + 1
            except NoSuchElementException:
                pass
            vysledkyTextItems = self.driver.find_elements_by_xpath("//*[@class='f_fulltextResults-item']/a")
            vysledkyTextItemsSingle = self.driver.find_element_by_xpath("//*[@class='f_fulltextResults-item']/a")

            wait.until(EC.visibility_of(vysledkyTextItemsSingle))
            z = 0
            for _ in vysledkyTextItems:
                    linksToCheckList.append(vysledkyTextItems[0].text)
                    z = z + 1

            #print(linksToCheckList)
            poziceQueryItem=poziceQueryItem+1
            #print(len(linksToCheckList))
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            #for _ in linksToCheckList:
            if len(linksToCheckList) > 5:
                for i in range(5):
                    response = requests.get(linksToCheckList[y])


                    #print(response.status_code)
                    #print(response.status_code == 200)
                    if response.status_code != 200:
                        print(linksToCheckList[y])

                    y = y + 1
                    assert response.status_code == 200
            else:
                for _ in linksToCheckList:
                    #print(response.status_code)
                    #print(response.status_code == 200)

                    y = y + 1
                    assert response.status_code == 200

            self.test_passed = True