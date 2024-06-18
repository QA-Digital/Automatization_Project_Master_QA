from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter

hotelyKartyXpath = "//*[@class='f_tile-item f_tile-item--content']"
cenaZajezduXpath = "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']"
sorterCheapXpath = "(//span[contains(text(),'de la cele mai ieftine')])[1]"
sorterExpensiveXpath = "(//span[contains(text(),'de la cele mai scumpe')])[1]"
totalPriceXpath = "//*[@class='price-amount']"

from DERRO.to_import import URL_local
class Test_SRL_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)

    def test_SRL_sort_cheapest(self):

        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        wait = WebDriverWait(self.driver, 150)
        time.sleep(5)
        acceptConsent(self.driver)
        time.sleep(4)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(sorterCheapXpath))).click()
        cenaZajezduAllList = []
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
        poziceHotelu = 0
        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            cenaZajezduAllString = cenaZajezduAllString.replace(".", "")
            cenaZajezduAllString = int(cenaZajezduAllString)
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort()

        if cenaZajezduAllListSorted == cenaZajezduAllList:
            print("Razeni od nejlevnejsiho je OK")
        else:
            print("Razeni od nejlevnejsiho je spatne")

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True

    def test_SRL_sort_expensive(self):

        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        time.sleep(5)
        acceptConsent(self.driver)
        time.sleep(4)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(sorterExpensiveXpath))).click()
        cenaZajezduAllList = []
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
        poziceHotelu = 0
        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            cenaZajezduAllString = cenaZajezduAllString.replace(".", "")
            cenaZajezduAllString = int(cenaZajezduAllString)
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort(reverse=True)

        if cenaZajezduAllListSorted == cenaZajezduAllList:
            print("Razeni od nejdrazsiho je OK")
        else:
            print("Razeni od nejdrazsiho je spatne")

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True

    def test_SRL_map(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        generalized_map_test_click_through_circles(self.driver, zobrazitNaMapeXpath)
        time.sleep(2.5)

        generalized_map_test_click_on_pin_and_hotel_bubble(self.driver)
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[1])  ##gotta switch to new window
        currentUrl = self.driver.current_url
        print(currentUrl)
        print(URL_SRL)
        assert currentUrl != URL_SRL

        self.test_passed = True

    def test_SRL_filtr_strava(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)

        time.sleep(5)
        acceptConsent(self.driver)
        time.sleep(2)
        stravaMenuXpath = "(//span[contains(text(),'All inclusive')])[1]"
        generalized_SRL_choose_meal_filter_EW_like(self.driver, stravaMenuXpath)
        stravaZajezduSrlXpath = "//*[@class='f_list-item f_icon f_icon--cutlery']"
        assertion_strava = "all inclusive"
        generalized_list_string_sorter(self.driver, stravaZajezduSrlXpath, assertion_strava)

        self.test_passed = True

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        wait = WebDriverWait(self.driver, 25)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("//*[@class='f_searchResult-content-item relative']")

            wait.until(EC.visibility_of(hotelyAllKarty[0]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        for _ in range(6):
            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)
            terminZajezdu = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
            terminZajezduSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

            wait.until(EC.visibility_of(terminZajezduSingle))
            ##print(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            ##print(linkDetailActualUrl)

            stravaZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
            stravaZajezduString = stravaZajezdu[x].text

            pokojZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
            pokojZajezduString = pokojZajezdu[x].text
            ##print(pokojZajezduString)

            cenaZajezduAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
            cenaZajezduAllString = cenaZajezduAll[x].text
            ##print(cenaZajezduAllString)

            cenaZajezduAdult = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
            cenaZajezduAdultString = cenaZajezduAdult[x].text
            # print(cenaZajezduAdultString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[windowHandle])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(2.5)  ##natvrdo aby se to neposralo

            try:
                detailStravaSedivka = self.driver.find_element_by_xpath(
                    "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/span")
            except NoSuchElementException:
                try:
                    detailStravaSedivka = self.driver.find_element_by_xpath(
                        "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/span")
                except NoSuchElementException:
                    pass

            detailStravaSedivkaString = detailStravaSedivka.text
            print(detailStravaSedivkaString)

            detailPokojSedivka = self.driver.find_element_by_xpath(
                "//*[@class='f_box-item f_icon f_icon--bed']//strong")
            detailPokojSedivkaString = detailPokojSedivka.text
            print(detailPokojSedivkaString)

            detailCenaAll = self.driver.find_element_by_xpath("//*[@class='f_column-item']//*[@class='f_price']")
            detailCenaAllString = detailCenaAll.text
            print(detailCenaAllString)
            try:
                detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between mb-2']//*[@class='text-right bold']")
                detailCenaAdultString = detailCenaAdult.text
                print(detailCenaAdultString)

            except NoSuchElementException:
                pass

            assert pokojZajezduString in detailPokojSedivkaString  ##cuz v SRL je kratsi nazev?
            if detailPokojSedivkaString == pokojZajezduString:
                print("pokoje sedi srl vs detail")
            else:
                print(" NESEDÍ pokoj SRL vs sedivka")

            assert detailStravaSedivkaString == stravaZajezduString

            if detailStravaSedivkaString == stravaZajezduString:
                print("stravy sedi srl vs detail")
            else:
                print("NESEDÍ strava srl vs ssedika")

            assert detailCenaAllString == cenaZajezduAllString

            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")
            else:
                print("ceny all NESEDÍ srl vs detail")

            assert detailCenaAdultString == cenaZajezduAdultString

            if detailCenaAdultString == cenaZajezduAdultString:
                print(" cena adult sedi srl vs detail")
            else:
                print("cena adult NESEDÍ srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            print(x)
            windowHandle = windowHandle + 1
            print(windowHandle)

            self.test_passed = True