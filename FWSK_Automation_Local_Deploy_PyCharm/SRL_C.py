from FWSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown
from FW_Automation_Local_Deploy_PyCharm.to_import import generalDriverWaitImplicit
import time
import unittest
from FW_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from generalized_test_functions import *

hotelyKartyXpath = "//*[@class='f_tile-item f_tile-item--content']"
cenaZajezduXpath = "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']"
sorterCheapXpath = "//*[contains(text(), 'od najlacnejšieho')]"
sorterExpensiveXpath = "//*[contains(text(), 'od najdrahšieho')]"


class Test_SRL_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_SRL_sort_cheapest(self):

        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)

        typeOfSort = "cheap"

        generalized_SRL_price_sorter(self.driver, sorterCheapXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort, "SK")

        self.test_passed = True

    def test_SRL_sort_expensive(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)

        typeOfSort = "expensive"

        generalized_SRL_price_sorter(self.driver, sorterExpensiveXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort, "SK")
        self.test_passed = True

    def test_SRL_map(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_SRL)
        wait = WebDriverWait(driver, 15)
        time.sleep(2.3)
        acceptConsent(driver)
        time.sleep(8)
        generalDriverWaitImplicit(self.driver)
        # zobrazitNaMape = driver.find_element_by_xpath("//*[@class='f_bar-item f_bar-map']")
        # zobrazitNaMape.click()
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath)
        time.sleep(2)
        generalized_map_test_click_on_pin_and_hotel_bubble(driver)
        time.sleep(2)

        ###EXECUTION DISPLAY TEST NA DETAIL HOTELU -> pokud se vyassertuje že jsem na detailu a vše je ok můžu předpokládat že mapka je OK

        detail_D(self, driver)

        self.test_passed = True

    def test_SRL_filtr_strava(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)

        stravaMenuXpath = "//*[@class='f_input-label']//*[contains(text(), 'All inclusive')]"
        generalized_SRL_choose_meal_filter_EW_like(driver, stravaMenuXpath)

        stravaZajezduSrlXpath = "//*[@class='f_list-item f_icon f_icon--cutlery']"
        assertion_strava = "all inclusive"
        generalized_list_string_sorter(driver, stravaZajezduSrlXpath, assertion_strava)

        self.test_passed = True

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1

        #URL_SRL = "https://fischer.web2.dtweb.cz/vysledky-vyhledavani?d=1009|953|1108|592|611|610|612|1010|590|726|609|621|680|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=8&kc1=1&ac1=2"
        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 25)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)


        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("//*[@class='f_tile-item f_tile-item--content']")

            wait.until(EC.visibility_of(hotelyAllKarty[0]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        #for WebElement in hotelyAllKarty:
        for _ in range(6):

            print("|||||HOTEL CISLO|||||||" )
            print(x+1)
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
            #print(cenaZajezduAdultString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[windowHandle])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(1)  ##natvrdo aby se to neposralo

            #detailTerminSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
            ##print(detailTerminSedivka.text)

            detailStravaSedivka = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/span")
            # detailStravaSedivkaString = detailStravaSedivka[1].text  ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully
            detailStravaSedivkaString = detailStravaSedivka.text
            print(detailStravaSedivkaString)

            # detailPokojSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
            detailPokojSedivka = self.driver.find_element_by_xpath(
                "//*[@class='f_box-item f_icon f_icon--bed']//strong")
            detailPokojSedivkaString = detailPokojSedivka.text
            # detailPokojSedivkaString = detailPokojSedivkaString[:-3]  ##need to be edited cuz there is random spaces and "?" in the element
            print(detailPokojSedivkaString)

            # detailCenaAll = self.driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
            detailCenaAll = self.driver.find_element_by_xpath("//*[@class='f_column-item']//*[@class='f_price']")
            detailCenaAllString = detailCenaAll.text
            print(detailCenaAllString)

                # detailCenaAdult = self.driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
            detailCenaAdult = self.driver.find_element_by_xpath(
                    "//*[@class='flex justify-between mb-2']//*[@class='text-right bold']")
            detailCenaAdultString = detailCenaAdult.text
            print(detailCenaAdultString)


            assert detailPokojSedivkaString == pokojZajezduString

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
