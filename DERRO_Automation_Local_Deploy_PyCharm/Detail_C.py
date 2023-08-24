from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import *

##global
terminyAcenyTabXpath = "//span[@class='f_anchor' and contains(text(), 'Date si tarife')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

#meal filter
stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"

valueToFilterStravaAllIncXpath = "(//span[@class='f_input-label'])[3]"

zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"

stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"

#airport filter
dopravaSibiuXpath = "(//span)[2437]"
dopravaBoxXpath ="//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"

class TestDetailHotelu_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def omlouvamese_paragraph(self):
        time.sleep(1)
        try:
            omlouvameParagraph = self.driver.find_element_by_xpath(
                "//*[@class='fshr-paragraph fshr-paragraph--centered']")
            if omlouvameParagraph.is_displayed():
                return

        except NoSuchElementException:
            pass

    def test_detail_price_sorter_terminy_expensive(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)


        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(4)

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 xlg:pl-0']"
            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 3
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(".", "")
            #cenaZajezduAllString = '.'.join(cenaZajezduAllString.split())
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        print(celkoveCenyList)

        time.sleep(3)
        # cheap = "expensive"
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "expensive")

    def test_detail_price_sorter_terminy_cheap(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)


        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", terminyAcenyElement)
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(4)

    #   celkovaCenaSorterXpath ="//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
    #   celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

    #   celkovaCenaSorterElement.click()
        time.sleep(5)

        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 xlg:pl-0']"
            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 3
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(".", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        print(celkoveCenyList)

        time.sleep(3)
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap")
    def test_detail_fotka(self):

        self.driver.maximize_window()
        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(5)
        imageDetail = self.driver.find_element_by_xpath(
            "//*[@aria-roledescription='carousel']//*[@class='splide__slide is-active is-visible']//img")
        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            # time.sleep(5)
            image = self.driver.find_element_by_xpath("/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                print("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

        self.test_passed = True

    def test_detail_terminy_filtr_meal(self):
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(URL_detail)

        time.sleep(1)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        stravovaniBoxXpath,
                                                                        valueToFilterStravaAllIncXpath, True)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath(zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        print(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True

    def test_detail_terminy_filtr_airport(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)

        time.sleep(1)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        dopravaBoxXpath, dopravaSibiuXpath, True)
        time.sleep(4)
        pocetZobrazenychTerminuXpath = "//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "Sibiu"

        time.sleep(5)
        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath, departureToCompareTo, True)

        time.sleep(0.2)
        self.test_passed = True
