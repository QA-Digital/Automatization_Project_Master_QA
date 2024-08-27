from FW.to_import import print_lock
import time
from FW.to_import import print_lock
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from FW.groupsearch_D import groupSearch_D
from FW.Detail_D import detail_D
from FW.SRL_D import SRL_D
import time
from selenium.webdriver.common.action_chains import ActionChains
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web

#banneryXpath_FW = "//*[@class='f_teaser-item js-priceLoading']/a"
#banneryXpath_FW = "//*[@data-pricecheck-type='banner']/a"
banneryXpath_FW = "//*[@class='f_teaser-item']/a"
URL_prod_public = "https://www.fischer.cz/"
URL_deploying_web = URL

#HPvyhledatZajezdyButtonXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[@class='f_filterMainSearch-content']/div[@class='f_filterMainSearch-content-item'][5]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPvyhledatZajezdyButtonXpath = "//*[@class='f_button f_button--forFilter']"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam pojedete?')]"
HPzlutakReckoDestinaceXpath = "//*[@class='f_input-content'] //*[contains(text(), 'Řecko')]"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
#HPzlutakPokracovatButtonXpathStep2 = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-footer js_filter-footer']/div[@class='f_filterHolder-footer-item'][2]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPzlutakPokracovatButtonXpathStep2 ="/html/body/header/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/a/span"

HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Jarní prázdniny 2023')]"
#HPzlutakPokracovatButtonXpathStep3 = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-footer js_filter-footer']/div[@class='f_filterHolder-footer-item'][2]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPzlutakPokracovatButtonXpathStep3 = "/html/body/header/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[2]/a/span"

HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdyVypisXpath = "//*[@class='fshr-lm-table-item-content']"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

from FW.to_import import URL_local

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
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)

        self.test_passed = True
    ##TODO underthis, setup for STG2
    def test_HP_zlutak_to_SRL(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakReckoDestinaceXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click()
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakLetniPrazdninyXpath))).click()
        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep3))).click()


        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath))).click()

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click()
        time.sleep(1)
        SRL_D(self, self.driver)

        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 500)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            #print (nejlepsiNabidkyTextList)
            positionOfCurrentElement = positionOfCurrentElement+1

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
            #print(nejlepsiNabidkyTextList)
            positionOfCurrentElement2 = positionOfCurrentElement2 + 1

        with print_lock:

            with print_lock:

                print_lock.acquire()

                try:

                    print_lock.acquire()

                    try:

                        print_lock.acquire()

                        try:

                            print(nejlepsiNabidkyTextList)

                            time.sleep(0.1)

                        finally:

                            print_lock.release()
                        time.sleep(0.1)

                    finally:

                        print_lock.release()
                    time.sleep(0.1)

                finally:

                    print_lock.release()
        with print_lock:
            with print_lock:
                print_lock.acquire()
                try:
                    print_lock.acquire()
                    try:
                        print_lock.acquire()
                        try:
                            print(nejlepsiNabidkyTextList2)
                            time.sleep(0.1)
                        finally:
                            print_lock.release()
                        time.sleep(0.1)
                    finally:
                        print_lock.release()
                    time.sleep(0.1)
                finally:
                    print_lock.release()
        assert nejlepsiNabidkyTextList != nejlepsiNabidkyTextList2

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnextArrowXpath))).click()
        #time.sleep(10)
        self.driver.implicitly_wait(100)

        # HPnextArrowElement = self.driver.find_element_by_xpath(HPnextArrowXpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", HPnextArrowElement)
        # time.sleep(1)
        # self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        # time.sleep(0.3)
        # self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        # time.sleep(0.5)
        # self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        # time.sleep(0.5)
        # self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        # time.sleep(0.5)
        # self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        #HPnextkartaHoteluSlider = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        time.sleep(1)
        #self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        #self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        #action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_FW)

        self.test_passed = True
