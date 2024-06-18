from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from KTGHU.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from KTGHU.groupsearch_D import groupSearch_D
import time
from KTGHU.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web

URL_deploying_web = URL
URL_prod_public = "https://www.kartagotours.hu/"
banneryXpath_EW = "//*[@class='f_teaser-item']/a"

#HPvyhledatZajezdyButtonXpath = "//*[@class='f_button f_button--highlighted']//*[contains(text(), 'Ajánlatok keresése')]"
HPvyhledatZajezdyButtonXpath = "//*[@class='f_filterMainSearch']//*[contains(text(), 'Ajánlatok keresése')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Hova?')]"
HPzlutakReckoDestinaceXpath = "//*[@class='f_input-wrapper']//img[@alt='Španělsko']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Továbblépés')]"
HPzlutakPokracovatButtonXpathStep2 = "//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Továbblépés')]"
HPzlutakPokracovatButtonXpathStep3 = "//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Továbblépés')]"

#HPzlutakLetniPrazdninyXpath = "//*[contains(text(), '2022 Szeptember / Október')]"
HPzlutakLetniPrazdninyXpath = "//*[@class='f_filter-item']//*[contains(text(), 'First Minute - Nyár')]"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Családi elhelyezés 2 felnőtt + 1 gyerek')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Keresés indítása')]"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPzlutakPokracovatVyberTerminuXpath =HPzlutakPokracovatButtonXpathStep2

from KTGHU.to_import import URL_local
class Test_HP_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HP_zlutak_to_groupsearch(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click()
        time.sleep(0.3)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakReckoDestinaceXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakLetniPrazdninyXpath))).click()
        time.sleep(0.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatVyberTerminuXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath))).click()

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click()
        time.sleep(2.789)
        SRL_D(self, self.driver)

        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(1.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            # print (nejlepsiNabidkyTextList)
            positionOfCurrentElement = positionOfCurrentElement + 1

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)))
        HPnejlepsiZajezdySwitchButtonElement = self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)
        self.driver.execute_script("arguments[0].click();", HPnejlepsiZajezdySwitchButtonElement)
        time.sleep(6)
        self.driver.implicitly_wait(10)
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement2 = 0
        nejlepsiNabidkyTextList2 = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement2].text
            nejlepsiNabidkyTextList2.append(nejlepsiNabidkyTextDefault)
            # print(nejlepsiNabidkyTextList)
            positionOfCurrentElement2 = positionOfCurrentElement2 + 1

        print(nejlepsiNabidkyTextList)
        print(nejlepsiNabidkyTextList2)
        assert nejlepsiNabidkyTextList != nejlepsiNabidkyTextList2

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        # wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnextArrowXpath))).click()
        # time.sleep(10)
        self.driver.implicitly_wait(100)
        topNabidkaBigHotelCardXpath = "//*[@class='f_carousel-item slick-slide slick-active']//*[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
        topNabidkaBigHotelCardElement = self.driver.find_element_by_xpath(topNabidkaBigHotelCardXpath)

        self.driver.execute_script("arguments[0].scrollIntoView();", topNabidkaBigHotelCardElement)
        # self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        # action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(8)
        topNabidkaBigHotelCardElement.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        curURL = self.driver.current_url

        assert curURL != URL

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)

        self.test_passed = True