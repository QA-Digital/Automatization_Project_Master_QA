from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit, URL_SRL_kuba_regres
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter
from EW.SRL_D import SRL_D
from helpers.helper import Helpers

hotelyKartyXpath = "//*[@class='f_tile-item f_tile-item--content']"
cenaZajezduXpath = "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']"
sorterCheapXpath = "//*[@class='f_tabBar-text' and contains(text(), 'od nejlevnějšího')]"
sorterExpensiveXpath = "//*[@class='f_tabBar-text' and contains(text(), 'od nejdražšího')]"


from EW.to_import import URL_local
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

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        typeOfSort = "cheap"

        Helpers.generalized_SRL_price_sorter(self.driver, sorterCheapXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort, self.logger)


        self.test_passed = True

    def test_SRL_sort_expensive(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)


        typeOfSort = "expensive"

        Helpers.generalized_SRL_price_sorter(self.driver, sorterCheapXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort, self.logger)

        self.test_passed = True

    def test_SRL_map(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        acceptConsent(self.driver)
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        #zobrazitNaMape.click()
        Helpers.generalized_map_test_click_through_circles(self.driver, zobrazitNaMapeXpath, self.logger)
        time.sleep(2.5)

        Helpers.generalized_map_test_click_on_pin_and_hotel_bubble(self.driver, self.logger)
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[1])  ##gotta switch to new window
        currentUrl = self.driver.current_url
        self.logger.info(currentUrl)
        self.logger.info(URL_SRL)
        assert currentUrl != URL_SRL

        self.test_passed = True

    def test_SRL_filtr_strava(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        stravaMenuXpath = "//*[@class='f_input-label']//*[contains(text(), 'All Inclusive')]"
        stravaMenu = self.driver.find_element_by_xpath(stravaMenuXpath)
        stravaMenu.click()
        stravaZajezduSrlXpath = "//*[@class='f_list-item f_icon f_icon--cutlery']"
        assertion_strava = "all inclusive"
        Helpers.generalized_list_string_sorter(self.driver, stravaZajezduSrlXpath, assertion_strava, self.logger)

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
            # hotelyAllKarty = self.driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
            hotelyAllKarty = self.driver.find_elements_by_xpath("//*[@class='f_searchResult-content-item relative']")

            wait.until(EC.visibility_of(hotelyAllKarty[0]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        # for WebElement in hotelyAllKarty:
        for _ in range(12):
        #for _ in range(19):
            self.logger.info("|||||HOTEL CISLO|||||||")
            self.logger.info(x + 1)
            self.logger.info(x + 1)
            self.logger.info(x + 1)
            terminZajezdu = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
            terminZajezduSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

            wait.until(EC.visibility_of(terminZajezduSingle))
            ##self.logger.info(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            ##self.logger.info(linkDetailActualUrl)

            stravaZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
            stravaZajezduString = stravaZajezdu[x].text

            pokojZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
            pokojZajezduString = pokojZajezdu[x].text
            ##self.logger.info(pokojZajezduString)

            cenaZajezduAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
            cenaZajezduAllString = cenaZajezduAll[x].text
            ##self.logger.info(cenaZajezduAllString)

            cenaZajezduAdult = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
            cenaZajezduAdultString = cenaZajezduAdult[x].text
            # self.logger.info(cenaZajezduAdultString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(2.5)  ##natvrdo aby se to neposralo

            # detailTerminSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
            ##self.logger.info(detailTerminSedivka.text)
            try:
                detailStravaSedivka = self.driver.find_element_by_xpath(
                    "//*[@class='f_icon f_icon--cutlery before:mr-1 before:text-neutral-400']")
            except NoSuchElementException:
                try:
                    detailStravaSedivka = self.driver.find_element_by_xpath(
                        "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/span")
                except NoSuchElementException:
                    pass

            # detailStravaSedivkaString = detailStravaSedivka[1].text  ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully
            detailStravaSedivkaString = detailStravaSedivka.text
            self.logger.info(detailStravaSedivkaString)

            # detailPokojSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
            detailPokojSedivka = self.driver.find_element_by_xpath(
                "//*[@class='f_box-item f_icon f_icon--bed']//strong")
            detailPokojSedivkaString = detailPokojSedivka.text
            # detailPokojSedivkaString = detailPokojSedivkaString[:-3]  ##need to be edited cuz there is random spaces and "?" in the element
            self.logger.info(detailPokojSedivkaString)

            # detailCenaAll = self.driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
            detailCenaAll = self.driver.find_element_by_xpath("//*[@class='f_column-item']//*[@class='f_price']")
            detailCenaAllString = detailCenaAll.text
            self.logger.info(detailCenaAllString)
            try:
                # detailCenaAdult = self.driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
               # detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between']//*[@class='text-right bold']")
                detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between mb-2']//*[@class='text-right bold']")
                detailCenaAdultString = detailCenaAdult.text
                self.logger.info(detailCenaAdultString)

            except NoSuchElementException:
                pass
            # assert detailPokojSedivkaString == pokojZajezduString
            assert pokojZajezduString in detailPokojSedivkaString  ##cuz v SRL je kratsi nazev?
            self.driver.close()

            if detailPokojSedivkaString == pokojZajezduString:
                self.logger.info("pokoje sedi srl vs detail")
            else:
                self.logger.info(" NESEDÍ pokoj SRL vs sedivka")

            assert detailStravaSedivkaString == stravaZajezduString
            if detailStravaSedivkaString == stravaZajezduString:
                self.logger.info("stravy sedi srl vs detail")

            else:
                self.logger.info("NESEDÍ strava srl vs ssedika")
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                self.logger.info("ceny all sedi srl vs detail")

            else:
                self.logger.info("ceny all NESEDÍ srl vs detail")

            assert detailCenaAdultString == cenaZajezduAdultString

            if detailCenaAdultString == cenaZajezduAdultString:
                self.logger.info(" cena adult sedi srl vs detail")

            else:
                self.logger.info("cena adult NESEDÍ srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            self.logger.info(x)
            windowHandle = windowHandle + 1
            self.logger.info(windowHandle)

            self.test_passed = True

    def test_SRL_kuba_srl_D_R(self):
        ## https://jira.fischer.cz/browse/FW-1704

        self.driver.maximize_window()
        URL_SRL_kuba_regres_lp = f"{self.URL}{URL_SRL_kuba_regres}"
        self.driver.get(URL_SRL_kuba_regres_lp)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(5)
        Helpers.search_results_list_check(self.driver, self.logger)