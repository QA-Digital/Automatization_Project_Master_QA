from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_detail, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_Detail_terminyAceny_potvrdit_chooseFiltr, generalized_list_string_sorter, generalized_detail_departure_check, generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail
from generalized_test_functions import generalized_price_sorter_expensive_cheap_assert
##global
terminyAcenyTabXpath_V1 = "//*[@id='terminyaceny-tab']"
terminyAcenyTabXpath_old = "//*[@class='f_bar-item f_tabBar']//*[contains(text(),'Termíny a ceny')]"
terminyAcenyTabXpath = "//*[@class='f_menu f_menu--inline f_menu--sticky']//*[contains(text(),'Termíny a ceny')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

#meal filter
stravovaniBoxXpath_V1 = "//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']"
stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"

valueToFilterStravaAllIncXpath_V1 = "//*[@id='filtr-stravy-detail']//*[contains(text(),'All inclusive')]"
#valueToFilterStravaAllIncXpath = "//*[@class='f_holder']//*[contains(text(),'All inclusive')]"
valueToFilterStravaAllIncXpath = "//*[@class='f_input--checkbox f_input']//*[@value=5]"

zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"

stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"

#airport filter
dopravaBoxXpath_V1 = "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']"
dopravaBrnoXpath_V1 = "//*[@data-value='4305']"
dopravaBrnoXpath = "//*[@class='f_filterHolder f_set--active']//*[@class='f_input--checkbox f_input']"
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
        acceptConsent(driver)
        time.sleep(4)

        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(4)
        celkovaCenaSorterAfterOneClickXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterAfterOneClickElement = driver.find_element_by_xpath(celkovaCenaSorterAfterOneClickXpath)

        celkovaCenaSorterAfterOneClickElement.click()
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
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        print(celkoveCenyList)

        time.sleep(3)
        #cheap = "expensive"
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "expensive")

    def test_detail_price_sorter_terminy_cheap(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)
        driver = self.driver
        acceptConsent(driver)
        time.sleep(4)

        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
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
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        print(celkoveCenyList)

        time.sleep(3)
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap")

    def test_detail_open_terminy_sumUP_equal_to_full_price(self):
        self.driver.maximize_window()
        URL_detail = "https://www.fischer.cz/spanelsko/fuerteventura/morro-jable/blue-sea-jandia-luz?AC1=2&D=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&DD=2023-02-19&DP=4312&DPR=FISCHER+ATCOM&DS=256&GIATA=32289&HID=1629&IC1=0&KC1=0&MNN=7&MT=6&NN=7&PID=FUE90003&RD=2023-02-26&TO=4312|4305|2682|4308&acm1=2&df=2023-02-01|2023-03-31&nnm=7|8|9|10|11|12|13&tom=4312|4305|2682|4308&tt=1&ttm=1#/terminy-a-ceny"
        self.driver.get(URL_detail)


        cestujiciXpath = "//*[@class='f_table']//*[@class='f_table-body']//*[@class='f_table-cell']"
        time.sleep(1)
        acceptConsent(self.driver)
        time.sleep(15)
        terminyXpath = "//*[@class='f_termList-header']"
        terminyScrollInto = self.driver.find_element_by_xpath(terminyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", terminyScrollInto)

        cestujiciElements = self.driver.find_elements_by_xpath(cestujiciXpath)
        cestujiciElement = self.driver.find_element_by_xpath(cestujiciXpath)

        cestujiciElementText = self.driver.find_element_by_xpath(cestujiciXpath).text
        print(cestujiciElement.text)
        print("priting 1St")
        print(cestujiciElement.text)
        print(cestujiciElementText)
        print(cestujiciElements[0].text)
        #print(cestujiciElements[1].text)
        time.sleep(15)
        ##cestujici elements = pocet cestujiich,
        y=1
        for _ in cestujiciElements:
            cestujiciSinglePrice = cestujiciElements[y].text()
            print(cestujiciSinglePrice)
            cestujiciSinglePriceList = []
            cestujiciSinglePriceList.append(cestujiciSinglePrice)
            print(cestujiciSinglePriceList)
            y = y + 2

        self.test_passed = True

    def test_detail_fotka(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(10)
        imageDetail = self.driver.find_element_by_xpath("//*[@aria-roledescription='carousel']//*[@class='splide__slide is-active is-visible']//img")
        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            #time.sleep(5)
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
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,stravovaniBoxXpath, valueToFilterStravaAllIncXpath, False)
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

        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath, dopravaBoxXpath, dopravaBrnoXpath, True)
        time.sleep(4)
        pocetZobrazenychTerminuXpath="//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "brno"

        time.sleep(5)
        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath, departureToCompareTo, True)

        time.sleep(0.2)
        self.test_passed = True

