from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from KTGHU.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

##global
from generalized_test_functions import generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail, \
    generalized_list_string_sorter, generalized_detail_departure_check

#terminyAcenyTabXpath = "//*[@id='terminyaceny-tab']"
terminyAcenyTabXpath = "//*[@class='f_menu f_menu--inline f_menu--sticky']//*[contains(text(),'Időpontok és Árak')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

from KTGHU.to_import import URL_local
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

    def test_detail_fotka(self):

        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        acceptConsent(self.driver)

        time.sleep(1)
        closeExponeaBanner(self.driver)
        #imageDetailXpath = '//*[@id="pageContent"]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/swiper-container/swiper-slide[1]/img'
        imageDetailXpath = "/html/body/section/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/swiper-container/swiper-slide[1]/img"
        #imageDetail = self.driver.find_element(By.XPATH, "//*[@aria-roledescription='carousel']//*[@class='splide__slide is-active is-visible']//img")
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
        ##funkčně už je to ok ale musím pak updatnout url na detail, pockam na tcom

        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(URL_detail)

        stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"

        valueToFilterStravaAllIncXpath_V1 = "//*[@id='filtr-stravy-detail']//*[contains(text(),'All inclusive')]"
        # valueToFilterStravaAllIncXpath = "//*[@class='f_holder']//*[contains(text(),'All inclusive')]"
        valueToFilterStravaAllIncXpath = "//*[@class='f_input--checkbox f_input']//*[@value=5]"

        zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"

        stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"

        time.sleep(1)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        stravovaniBoxXpath,
                                                                        valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element(By.XPATH, zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        self.logger.info(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True









        # self.driver.get(URL_detail)
        # wait = WebDriverWait(self.driver, 150)
        # acceptConsent(self.driver)
        #
        # time.sleep(1)
        # closeExponeaBanner(self.driver)
        #
        #
        # try:
        #     terminyCeny = self.driver.find_element(By.XPATH, "//*[@id='terminyaceny-tab']")
        #     wait.until(EC.visibility_of(terminyCeny))
        #     ##terminyCeny.click()
        #     self.driver.execute_script("arguments[0].click();", terminyCeny)
        #     time.sleep(3)
        #     try:
        #         generalDriverWaitImplicit(self.driver)
        #         potvrdit = self.driver.find_element(By.XPATH, "//*[@data-testid='popup-closeButton']")
        #
        #         self.driver.execute_script("arguments[0].click();", potvrdit)
        #
        #     except NoSuchElementException:
        #         url = self.driver.current_url
        #         msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
        #         sendEmail(msg)
        #
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
        #     sendEmail(msg)
        #
        # time.sleep(2)
        # try:
        #     stravovaniBox = self.driver.find_element_by_xpath(
        #         "//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']")
        #     wait.until(EC.visibility_of(stravovaniBox))
        #     self.driver.execute_script("arguments[0].click();", stravovaniBox)
        #     try:
        #         # allInclusiveBox =
        #         # driver.find_element(By.XPATH, "//*[contains(text(), 'All
        #         # inclusive')]")
        #         # wait.until(EC.visibility_of(allInclusiveBox))
        #         ##allInclusiveBox.click()
        #         stravyBox = self.driver.find_elements(By.XPATH, "//*[@name='detailFilterCatering']")
        #
        #         self.driver.execute_script("arguments[0].click();", stravyBox[1])
        #
        #         try:
        #             ##potvrditButtonBox =
        #             ##driver.find_element_by_xpath("//*[@class='fshr-filter-footer']
        #             ##//*[contains(text(), 'Potvrdit')]")
        #
        #             # potvrditButtonBox.click()
        #             self.driver.execute_script("arguments[0].click();",
        #                                        stravovaniBox)  ##workaround, klikni na box to confirm the choice
        #
        #         except NoSuchElementException:
        #             url = self.driver.current_url
        #             msg = "stravaBox, potvrzeni stravy na detailu hotelu problém, NoSuchElementException " + url
        #             sendEmail(msg)
        #
        #     except NoSuchElementException:
        #         url = self.driver.current_url
        #         msg = "allInclusiveBox, zvolení stravy na detailu hotelu problém, NoSuchElementException " + url
        #         sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "stravovaniBox, otevření filtru stravování detail hotelu, NoSuchElementException " + url
        #     sendEmail(msg)
        #
        # #omlouvamese_paragraph(self)
        #
        # zvolenaStravaVboxu = self.driver.find_element(By.XPATH, "//*[@class='js-subvalue f_text--highlighted']")
        # zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        #
        # self.logger.info(zvolenaStravaVboxuString)
        #
        # stravaVterminech = self.driver.find_elements_by_xpath(
        #     "//*[@class='fshr-termin-catering js-tooltip js-tooltip--onlyDesktop']")
        # stravaVterminechString = []
        #
        # ##ty for loopy se nezapnou pokud pocet vysledku bude 0
        # ##takze treba exim a dx bude casto takto jelikoz se tam nabizi vsechny
        # ##stravy, ne jen ty available
        # time.sleep(2)
        # x = 0
        # for _ in stravaVterminech:
        #     stringos = stravaVterminech[x].text.lower()
        #     stravaVterminechString.append(stringos)
        #     x = x + 1
        #
        # time.sleep(1)  ###eroror element is not attached ?  tak chvilku cekacka mozna to solvne
        #
        # self.logger.info(stravaVterminechString)
        # y = 0
        # for _ in stravaVterminechString:
        #     assert zvolenaStravaVboxuString in stravaVterminechString[y]
        #     if zvolenaStravaVboxuString in stravaVterminechString[y]:
        #         self.logger.info("ok")
        #         ##self.logger.info(y)
        #         y = y + 1
        #     else:
        #         url = self.driver.current_url
        #         msg = "na detailu jsem vyfiltroval stravu " + zvolenaStravaVboxuString + "ale pry to nesedi říká python" + url
        #         sendEmail(msg)
        #         y = y + 1
        # time.sleep(1)
        # ##self.logger.info(stravaVterminech)
        # ##self.logger.info(stravaVterminechString)
        #
        # self.test_passed = True

        time.sleep(20)

    def test_detail_terminy_filtr_airport(self):

        self.driver.maximize_window()
        self.driver.get(URL_detail)

        time.sleep(1)
        acceptConsent(self.driver)

        dopravaBrnoXpath = "//*[@class='f_filterHolder f_set--active']//*[@value='489']"
        dopravaBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"

        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        dopravaBoxXpath, dopravaBrnoXpath, True)
        time.sleep(4)
        pocetZobrazenychTerminuXpath = "//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "budapest"

        time.sleep(5)
        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath,
                                           departureToCompareTo, True)

        time.sleep(0.2)
        self.test_passed = True


        # def omlouvamese_paragraph(self, driver):
        #     time.sleep(1)
        #     try:
        #         omlouvameParagraph = self.driver.find_element_by_xpath(
        #             "//*[@class='fshr-paragraph fshr-paragraph--centered']")
        #         if omlouvameParagraph.is_displayed():
        #             return
        #
        #     except NoSuchElementException:
        #         pass
        #
        #
        # self.driver.get(URL_detail)
        #
        # acceptConsent(self.driver)
        #
        #

        #
        #
        # time.sleep(1)
        # closeExponeaBanner(self.driver)
        # wait = WebDriverWait(self.driver, 150)
        #
        # try:
        #     generalDriverWaitImplicit(self.driver)
        #     terminyCeny = self.driver.find_element(By.XPATH, terminyAcenyTabXpath)
        #     wait.until(EC.visibility_of(terminyCeny))
        #     ##terminyCeny.click()
        #     self.driver.execute_script("arguments[0].click();", terminyCeny)
        #     time.sleep(0.5)
        #     try:
        #         generalDriverWaitImplicit(self.driver)
        #         time.sleep(2)
        #         potvrdit = self.driver.find_element(By.XPATH, "//*[@data-testid='popup-closeButton']")
        #         ##wait.until(EC.visibility_of(potvrdit))
        #         self.driver.execute_script("arguments[0].click();", potvrdit)
        #
        #     except NoSuchElementException:
        #         url = self.driver.current_url
        #         msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
        #         sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
        #     sendEmail(msg)
        #
        # try:
        #     dopravaBox = self.driver.find_element_by_xpath(
        #         "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']")
        #     wait.until(EC.visibility_of(dopravaBox))
        #     self.driver.execute_script("arguments[0].click();", dopravaBox)
        #     try:
        #         dopravaKosice = self.driver.find_element_by_xpath(
        #             "//*[@data-value='489']")  ##natvrdo brno, no list shenanigans
        #         self.driver.execute_script("arguments[0].click();", dopravaKosice)
        #
        #         time.sleep(0.5)
        #         try:
        #
        #             self.driver.execute_script("arguments[0].click();",
        #                                        dopravaBox)  ##workaround, proste klikne znova na doprava box aby se to propsalo, potvrdit
        #             ##button mi nejak blbnul
        #             ##driver.execute_script("arguments[0].click();",
        #             ##potvrditButtonBox)
        #
        #         except NoSuchElementException:
        #             url = self.driver.current_url
        #             msg = "potvrditButtonBox, potvrzeni dopravy na detailu hotelu problém, NoSuchElementException " + url
        #             sendEmail(msg)
        #
        #     except NoSuchElementException:
        #         url = self.driver.current_url
        #         msg = "dopravaBrno, zvolení dopravy na detailu hotelu problém, NoSuchElementException " + url
        #         sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "dopravaBox, zvolení dopravy na detailu hotelu problém, NoSuchElementException " + url
        #     sendEmail(msg)
        #
        # time.sleep(1)  ##cekacka na terminy load
        # omlouvamese_paragraph(self, self.driver)
        #
        # try:
        #     pocetZobrazenychTerminu = self.driver.find_elements_by_xpath(
        #         "//*[@class='fshr-termins-table-item-header js-toggleSlide']")  ##locator jen na pocet odletu alokuje vic veci nez je actual terminu tak
        #     ##pro
        #     ##for
        #     ##loop
        #     ##pouziju
        #     ##tohle
        #     ##=
        #     ##20
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "pocetZobrazenychTerminu, filtrovani dle letu detail hotelu, mozna jen nema odlety na X, NoSuchElementException " + url
        #     sendEmail(msg)
        #
        # try:
        #     odletyTerminy = self.driver.find_elements_by_xpath(
        #         "//*[@class='fshr-termin-departure-from']")  ##prvni locator je "odlet" takze zacnu na pozici jedna, vyloopuje se to podle
        #     ##poctu terminu, should be ok
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "odletyTerminy, nejsou odlety na brno, most likely not a bad thing, NoSuchElementException " + url
        #     sendEmail(msg)
        # y = 1
        # for _ in pocetZobrazenychTerminu:
        #     assert odletyTerminy[y].text == "Budapest"
        #     if odletyTerminy[y].text == "Budapest":  ##tady je nutny pricitat +2 protoze je tam 41 results (s tim ze jeden
        #         ##je "odlet"), kazdy sudy cislo je mezera/blank space for some reason
        #         ##self.logger.info(odletyTerminy[y].text)
        #         y = y + 2
        #     else:
        #         url = self.driver.current_url
        #         ##self.logger.info(odletyTerminy[y].text)
        #         msg = "na detailu jsem vyfiltroval odlet na Budapest ale pry to nesedi říká python " + url
        #         sendEmail(msg)
        #         y = y + 2
        # self.test_passed = True


