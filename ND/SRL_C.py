from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ND.to_import import acceptConsent, closeExponeaBanner, URL_SRL_zima, URL_SRL_leto, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter


hotelyKartyXpath = "//*[@class='f_searchResult-content f_searchResult-content--grid']"
cenaZajezduXpath = "//*[@class='leading-tight text-xl']"
sorterCheapXpath = "//*[@class='f_tabBar-item f_set--active']"
sorterExpensiveXpath = "//*[@class='f_tabBar-text' and contains(text(), 'od nejdražšího')]"


from ND.to_import import URL_local
class Test_SRL_C_Zima(unittest.TestCase):
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
        URL_SRL_zima_lp = f"{self.URL}{URL_SRL_zima}"
        self.driver.get(URL_SRL_zima_lp)
        wait = WebDriverWait(self.driver, 5)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        typeOfSort = "cheap"

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high
        time.sleep(3)
        element = self.driver.find_element_by_xpath("//*[@class='f_tabBar-item f_set--active']")
        self.driver.execute_script("arguments[0].click();", element)
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
        URL_SRL_leto_lp = f"{self.URL}{URL_SRL_leto}"
        self.driver.get(URL_SRL_leto_lp)
        wait = WebDriverWait(self.driver, 5)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(5)

        typeOfSort = "expensive"

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high
        element = self.driver.find_element_by_xpath("//*[@class='f_tabBar-text' and contains(text(), 'od nejdražšího')]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(6)
        hotelyKarty = self.driver.find_element_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyKarty))
        time.sleep(4)
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
        time.sleep(3)
        acceptConsent(driver)
        time.sleep(3)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath)
        time.sleep(5)

        generalized_map_test_click_on_pin_and_hotel_bubble(driver)
        time.sleep(5)

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

            terminZajezdu = self.driver.find_elements_by_xpath("(//span[@class='font-bold'])")
            print(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_button f_button--important']")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            print(linkDetailActualUrl)

            cenaZajezduAll = self.driver.find_elements_by_xpath("//*[@class='whitespace-nowrap text-[--primary] font-bold']")
            cenaZajezduAllString = cenaZajezduAll[x].text
            #print(cenaZajezduAllString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(2.5)  ##natvrdo aby se to neposralo


            detailCenaAll = self.driver.find_element_by_xpath("//span[@class='f_price']")
            detailCenaAllString = detailCenaAll.text
            print(detailCenaAllString)

            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")
            else:
                print("ceny all NESEDÍ srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            print(x)
            windowHandle = windowHandle + 1
            print(windowHandle)

            self.test_passed = True
