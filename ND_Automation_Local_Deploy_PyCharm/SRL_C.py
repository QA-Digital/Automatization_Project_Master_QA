from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, closeExponeaBanner, URL_SRL_zima, URL_SRL_leto, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter


hotelyKartyXpath = "//*[@class='f_searchResult-content f_searchResult-content--grid']"
cenaZajezduXpath = "//*[@class='leading-tight text-xl']"
sorterCheapXpath = "//*[@class='f_tabBar-text' and contains(text(), 'od nejlevnějšího')]"
sorterExpensiveXpath = "//*[@class='f_tabBar-text' and contains(text(), 'od nejdražšího')]"


class Test_SRL_C_Zima(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)

    def test_SRL_sort_cheapest(self):

        self.driver.maximize_window()
        self.driver.get(URL_SRL_zima)
        wait = WebDriverWait(self.driver, 5)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        typeOfSort = "cheap"

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high
        time.sleep(3)
        sorter_Element = self.driver.find_element_by_xpath(sorterCheapXpath)
        wait.until(EC.visibility_of(sorter_Element))
        sorter_Element.click()
        time.sleep(6)
        hotelyKarty = self.driver.find_element_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyKarty))
        # time.sleep(4)
        list_web_elements_Position = 0
        cenaZajezduAll = self.driver.find_elements_by_xpath(cenaZajezduXpath)
        wait.until(EC.visibility_of(cenaZajezduAll[0]))

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[list_web_elements_Position].text
            cenaZajezduAllString = cenaZajezduAllString
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            list_web_elements_Position = list_web_elements_Position + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        if typeOfSort == "cheap":
            cenaZajezduAllListSorted.sort()  ##sorting second list low to high

            if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
                print("Cheap sorter is OK")
            else:
                print("Cheap sorter is NOT OK")

        if typeOfSort == "expensive":
            cenaZajezduAllListSorted.sort(reverse=True)

            if cenaZajezduAllListSorted == cenaZajezduAllList:
                print("Expensive sorter is OK")
            else:
                print("Expensive sorter is NOT OK")

        print("LIST FROM WEB:")
        print(cenaZajezduAllList)
        print("CORRECTLY SORTED LIST")
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True

    def test_SRL_sort_expensive(self):

        self.driver.maximize_window()
        self.driver.get(URL_SRL_leto)
        wait = WebDriverWait(self.driver, 5)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        typeOfSort = "expensive"

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high
        time.sleep(3)
        sorter_Element = self.driver.find_element_by_xpath(sorterExpensiveXpath)
        wait.until(EC.visibility_of(sorter_Element))
        sorter_Element.click()
        time.sleep(6)
        hotelyKarty = self.driver.find_element_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyKarty))
        # time.sleep(4)
        list_web_elements_Position = 0
        cenaZajezduAll = self.driver.find_elements_by_xpath(cenaZajezduXpath)
        wait.until(EC.visibility_of(cenaZajezduAll[0]))

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[list_web_elements_Position].text
            cenaZajezduAllString = cenaZajezduAllString
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            list_web_elements_Position = list_web_elements_Position + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        if typeOfSort == "cheap":
            cenaZajezduAllListSorted.sort()  ##sorting second list low to high

            if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
                print("Cheap sorter is OK")
            else:
                print("Cheap sorter is NOT OK")

        if typeOfSort == "expensive":
            cenaZajezduAllListSorted.sort(reverse=True)

            if cenaZajezduAllListSorted == cenaZajezduAllList:
                print("Expensive sorter is OK")
            else:
                print("Expensive sorter is NOT OK")

        print("LIST FROM WEB:")
        print(cenaZajezduAllList)
        print("CORRECTLY SORTED LIST")
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True


    def test_SRL_map(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_SRL_zima)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        #zobrazitNaMape.click()
        generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath)
        time.sleep(2.5)

        generalized_map_test_click_on_pin_and_hotel_bubble(driver)
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[1])  ##gotta switch to new window
        currentUrl = self.driver.current_url
        print(currentUrl)
        print(URL_SRL_zima)
        assert currentUrl != URL_SRL_zima

        self.test_passed = True

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1
        self.driver.maximize_window()
        self.driver.get(URL_SRL_zima)
        wait = WebDriverWait(self.driver, 25)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("//*[@class='f_searchResult-content f_searchResult-content--grid']")
            wait.until(EC.visibility_of(hotelyAllKarty[0]))

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        # for WebElement in hotelyAllKarty:
        for _ in range(6):
            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)
            terminZajezdu = self.driver.find_elements_by_xpath("//*[@class='flex justify-between gap-2']")
            terminZajezduSingle = self.driver.find_element_by_xpath("//*[@class='flex justify-between gap-2']")

            wait.until(EC.visibility_of(terminZajezduSingle))
            print(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            print(linkDetailActualUrl)

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
            #self.driver.switch_to.window(self.driver.window_handles[windowHandle])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(2.5)  ##natvrdo aby se to neposralo

            # detailTerminSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
            ##print(detailTerminSedivka.text)
            try:
                detailStravaSedivka = self.driver.find_element_by_xpath(
                    "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/span")
            except NoSuchElementException:
                try:
                    detailStravaSedivka = self.driver.find_element_by_xpath(
                        "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/span")
                except NoSuchElementException:
                    pass

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
            try:
                # detailCenaAdult = self.driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
               # detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between']//*[@class='text-right bold']")
                detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between mb-2']//*[@class='text-right bold']")
                detailCenaAdultString = detailCenaAdult.text
                print(detailCenaAdultString)

            except NoSuchElementException:
                pass
            # assert detailPokojSedivkaString == pokojZajezduString
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
