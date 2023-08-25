import time
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky, setUp, tearDown
from FW_Automation_Local_Deploy_PyCharm.poznavacky import proklik_kostkaHotelu_toDetail_check_sedivka
from generalized_test_functions import generalized_list_of_url_checker
import unittest

from sedivka_check import sedivka_check_assert
sedivkaXpathFw = "//*[@class='f_box h-full flex flex-col']"

class TestPoznavacky_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_poznavacky_all_URL_check(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_poznavacky)
        time.sleep(4)

        acceptConsent(driver)
        time.sleep(8)
        gridItemXpath = "//*[@class='f_tileGrid-item']/a"
        gridItemElements = driver.find_elements_by_xpath(gridItemXpath)
        # print(URL_poznavaciho_hotelu)
        linksToCheck_List = []
        pozice = 0
        for _ in gridItemElements:
            odkazLink = gridItemElements[pozice].get_attribute("href")
            linksToCheck_List.append(odkazLink)
            print(odkazLink)
            pozice = pozice + 1
        print(linksToCheck_List)



        generalized_list_of_url_checker(linksToCheck_List)

    def test_poznavacky_okruzni_D(self):
            self.driver.maximize_window()
            self.driver.get(URL_poznavacky)
            time.sleep(2)
            acceptConsent(self.driver)

            self.driver.execute_script("window.scrollTo(0, 1080);")

            time.sleep(6)
            self.driver.implicitly_wait(100)


            gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")

            y=0
            for _ in gridItems:

                gridItemDisplayed = gridItems[y].is_displayed()
                assert gridItemDisplayed == True
                y=y+1
                print("grid true")
            assert gridItems[0].is_displayed() == True


            gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
            a=0
            assert gridBig[0].is_displayed() == True
            for _ in gridBig:
                gridBigDisplayed = gridBig[a].is_displayed()
                assert gridBigDisplayed == True
                a=a+1
                print("big grid ture")

            self.test_passed = True

    def test_poznavacky_vikendy_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_vikendy)
        time.sleep(2)
        acceptConsent(self.driver)

        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(6)
        self.driver.implicitly_wait(100)

        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")

        y = 0
        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")
        assert gridItems[0].is_displayed() == True


        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")

        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True

        self.test_passed = True

    def test_poznavacky_rodiny_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_rodiny)
        time.sleep(2)
        acceptConsent(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(8)


        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0

        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")
        assert gridItems[0].is_displayed() == True

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")

        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True
        self.test_passed = True

    def test_poznavacky_zazitky_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_zazitky)
        time.sleep(2)
        acceptConsent(self.driver)

        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(8)
        self.driver.implicitly_wait(100)


        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0

        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")

        assert gridItems[0].is_displayed() == True

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
        a = 0

        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True
        self.test_passed = True

    def test_poznavacky_C(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky)
        time.sleep(1)

        acceptConsent(self.driver)
        time.sleep(9)
        kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"
        element3 = self.driver.find_elements_by_xpath(kostkaPoznavackaXpath)[6]
        self.driver.execute_script("arguments[0].scrollIntoView();", element3)
        time.sleep(2)
        element3.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2.5)
        print(self.driver.current_url)
        sedivka_check_assert(self.driver, sedivkaXpathFw)
        self.test_passed = True