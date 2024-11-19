from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import *

##global
from helpers.helper import Helpers

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

from DERRO.to_import import URL_local
class TestDetailHotelu_C(unittest.TestCase):
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
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)


        terminyAcenyElement = driver.find_element(By.XPATH, terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element(By.XPATH, boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        #celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterXpath =  "//span[normalize-space()='tariful total']"
        celkovaCenaSorterElement = driver.find_element(By.XPATH, celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(4)

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements(By.XPATH, pocetTerminuXpath)
        poziceTerminu = 1
        celkoveCenyList = []
        #for _ in pocetTerminuElements:
        result = len(pocetTerminuElements) - 1
        for _ in range(result):
            celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']"
            celkoveCenaVterminechElements = driver.find_elements(By.XPATH, celkoveCenaVterminechXpath)
            kcIndex = 3
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(".", "")
            #cenaZajezduAllString = '.'.join(cenaZajezduAllString.split())
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
            self.logger.info(celkoveCenyList)

        time.sleep(3)
        # cheap = "expensive"
        Helpers.generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "expensive", self.logger)

    def test_detail_price_sorter_terminy_cheap(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        time.sleep(4)
        acceptConsent(self.driver)

        terminyAcenyElement = self.driver.find_element(By.XPATH, terminyAcenyTabXpath)

        self.driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", terminyAcenyElement)
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = self.driver.find_element(By.XPATH, boxTerminyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(4)

        #   celkovaCenaSorterXpath ="//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        #   celkovaCenaSorterElement = self.driver.find_element(By.XPATH, celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho
        celkovaCenaSorterXpath = "//span[normalize-space()='tariful total']"
        celkovaCenaSorterElement = self.driver.find_element(By.XPATH, celkovaCenaSorterXpath)


        celkovaCenaSorterElement.click()

        time.sleep(5)
        celkovaCenaSorterXpath2 = "//span[normalize-space()='tariful total']"
        celkovaCenaSorterElement2 = self.driver.find_element(By.XPATH, celkovaCenaSorterXpath2)
        celkovaCenaSorterElement2.click()
        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = self.driver.find_elements(By.XPATH, pocetTerminuXpath)
        poziceTerminu = 1
        celkoveCenyList = []
        result = len(pocetTerminuElements) - 1
        for _ in range(result):
            celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']"
            celkoveCenaVterminechElements = self.driver.find_elements(By.XPATH, celkoveCenaVterminechXpath)
            kcIndex = 3
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(".", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
            self.logger.info(celkoveCenyList)

        time.sleep(3)
        #generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap")
        Helpers.generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap", self.logger)

    def test_detail_fotka(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        acceptConsent(self.driver)

        time.sleep(5)
        imageDetailXpath = '//*[@class="h-full swiper-slide-active"]//img'
        imageDetail = self.driver.find_element(By.XPATH, imageDetailXpath)
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
            image = self.driver.find_element(By.XPATH, "/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                self.logger.info("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

        self.test_passed = True

    def test_detail_terminy_filtr_meal(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        time.sleep(1)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        stravovaniBoxXpath,
                                                                        valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element(By.XPATH, stravaVterminechXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        self.logger.info(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True

    def test_detail_terminy_filtr_airport(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

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
