from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from ET.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import *

#global
terminyAcenyTabXpath = "//*[@class='f_anchor' and contains(text(),'Termíny a ceny')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"
#meal filter
stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"
valueToFilterStravaAllIncXpath = "//*[@class='f_input--checkbox f_input']//*[@value=5]"
zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"
stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"
#airport filter
dopravaBoxXpath ="//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"
dopravaBrnoXpath = "//*[@class='f_filterHolder f_set--active']//*[@value='4305']"

celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 min-[1101px]:pl-0']"

from ET.to_import import URL_local
class TestDetailHotelu_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
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

    def test_detail_terminy_D(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
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

        zobrazeneTerminy = driver.find_elements_by_xpath("//*[@class='f_termList-header-item f_termList-header-item--dateRange']")

        try:
            for WebElement in zobrazeneTerminy:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    pass

        except NoSuchElementException:
            pass

        assert zobrazeneTerminy[0].is_displayed() == True
        time.sleep(3)

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

        celkovaCenaSorterXpath = "//span[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)

        celkovaCenaSorterElement.click()
        time.sleep(4)

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        print(celkoveCenyList)

        time.sleep(3)
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
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//span[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)

        #celkovaCenaSorterElement.click()
        time.sleep(5)

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
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

        time.sleep(10)
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
                                                                        valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath(zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        print(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True

    def test_detail_terminy_filtr_doprava(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)

        time.sleep(5)
        acceptConsent(self.driver)

        terminyAcenyTabElement = self.driver.find_element_by_xpath(terminyAcenyTabXpath)
        self.driver.execute_script("arguments[0].click();", terminyAcenyTabElement)
        time.sleep(2.5)

        dopravaBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"
        boxElement = self.driver.find_element_by_xpath(dopravaBoxXpath)
        self.driver.execute_script("arguments[0].click();", boxElement)
        time.sleep(2)

        boxCrOdskrtnout = "(//label[@class='relative select-none cursor-pointer flex items-center gap-2'])[740]"
        boxElement2 = self.driver.find_element_by_xpath(boxCrOdskrtnout)
        self.driver.execute_script("arguments[0].click();", boxElement2)
        time.sleep(2)

        boxPrahaZaskrtnout = "(//label)[756]"
        boxElement3 = self.driver.find_element_by_xpath(boxPrahaZaskrtnout)
        self.driver.execute_script("arguments[0].click();", boxElement3)
        time.sleep(2)

        buttonVyhledat = "(//span[@class='f_button-text'][normalize-space()='Potvrdit a vyhledat'])[2]"
        buttonVyhledatKlik = self.driver.find_element_by_xpath(buttonVyhledat)
        self.driver.execute_script("arguments[0].click();", buttonVyhledatKlik)
        time.sleep(2)

        zvolenaDoprava = "Praha"
        dopravaBoxXpath = "//*[@class='f_icon f_icon--plane']"

        dopravaVterminech = self.driver.find_elements_by_xpath(dopravaBoxXpath)
        dopravaVterminechString = []

        x = 0
        for _ in dopravaVterminech:
            stringos = dopravaVterminech[x].text
            dopravaVterminechString.append(stringos)
            x = x + 1

        time.sleep(1)

        print(dopravaVterminechString)

        y = 0
        for _ in dopravaVterminechString:
            assert zvolenaDoprava in dopravaVterminechString[y]
            if zvolenaDoprava in dopravaVterminechString[y]:
                print("ok")
                y = y + 1
                print("Zvolena doprava souhlasi")
            else:
                url = self.driver.current_url
                msg = "Zvolena doprava nesedi " + url
                sendEmail(msg)
                y = y + 1

        self.test_passed = True

