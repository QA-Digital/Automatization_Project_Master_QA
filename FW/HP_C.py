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


def hp_zlutak_to_SRL(driver, kamPojedete, destinace, pokracovatBtn1, pokracovatBtn2, termin, pokracovatBtn3, obsazenost,
                     potvrditAvyhledat, generalTimeSleep=1.5, skipObsazenostSetting=False):
    wait = WebDriverWait(driver, 300)
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(kamPojedete))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(destinace))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn1))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn2))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(termin))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn3))).click()

    if skipObsazenostSetting == False:
        wait.until(EC.visibility_of(driver.find_element_by_xpath(obsazenost))).click()


    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(potvrditAvyhledat))).click()
    time.sleep(4)


def SRL_D_letenky(driver, SRLresultsLetenkyXpath):
    letenekySRLresultsElements = driver.find_elements_by_xpath(SRLresultsLetenkyXpath)
    pozice = 0
    for i in letenekySRLresultsElements:
        assert letenekySRLresultsElements[pozice].is_displayed() == True
        pozice = pozice + 1
from FW.to_import import URL_local
#banneryXpath_FW = "//*[@class='f_teaser-item js-priceLoading']/a"
#banneryXpath_FW = "//*[@data-pricecheck-type='banner']/a"
banneryXpath_FW = "//*[@class='f_teaser-item']/a"
URL_prod_public = "https://www.fischer.cz/"
URL_deploying_web = URL_local


#HPvyhledatZajezdyButtonXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[@class='f_filterMainSearch-content']/div[@class='f_filterMainSearch-content-item'][5]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPvyhledatZajezdyButtonXpath = "//*[@class='f_button f_button--forFilter']"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam pojedete?')]"
HPzlutakReckoDestinaceXpath = "//*[@value='st67']"
#HPzlutakReckoDestinaceXpath = "//*[@class='f_input-wrapper']//img[@alt='Španělsko']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
HPzlutakPokracovatButtonXpathStep2 = "//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovat')]"
HPzlutakPokracovatButtonXpathStep3 ="//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovat')]"


HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Září / Říjen 2024')]"
poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávací zájezdy')]"
lyzeVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Vlastní doprava')]"
letenkyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Letenky')]"

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

    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_poznavacky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element_by_xpath(poznavackyVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_lyze(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element_by_xpath(lyzeVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath, HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         ,HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath, HPzlutakPotvrditAvyhledatXpath )
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_poznavacky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        #poznavackyVeFiltruSwitchXpath = "//*[@class='f_icon f_icon--pinMap segmentation-list-anchor']"
        # poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávací zájezdy')]"
        destinaceEgyptXpath = "//*[@value='st64']"
      #  destinaceEgyptXpath = "//*[@value='st67']"


        self.driver.find_element_by_xpath(poznavackyVeFiltruSwitchXpath).click()

        time.sleep(3)

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)
        time.sleep(10)  # nevdama proste nez se nacte
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_lyze(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        #lyzeVeFiltruSwitchXpath = "//*[@class='f_icon f_icon--snowFlake segmentation-list-anchor']"

        self.driver.find_element_by_xpath(lyzeVeFiltruSwitchXpath).click()
        HPzlutakJarniPrazdninyXpath = "//*[contains(text(), 'Září / Říjen 2024')]"
        #destinaceItalieXpath = "/html/body/header/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/span/label/span/span"
        destinaceItalieXpath = "//*[@value='st110']"
        time.sleep(3)

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceItalieXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakJarniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(self.URL)
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

        time.sleep(1.5)
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
        self.driver.maximize_window()
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

#        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnextArrowXpath))).click()

        self.driver.implicitly_wait(100)

        HPnextArrowElement = self.driver.find_element_by_xpath(HPnextArrowXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPnextArrowElement)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        HPnextkartaHoteluSlider = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        #HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_FW)

        self.test_passed = True

    def test_HP_zlutak_to_SRL_letenky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        destinaceEgyptXpath = "//*[@value='st185']"

        self.driver.find_element_by_xpath(letenkyVeFiltruSwitchXpath).click()

        time.sleep(3)
        letenkySrlResultsXpath = "//*[@class='f_searchResult-content-item relative']"

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)


        SRL_D_letenky(self.driver, letenkySrlResultsXpath)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_letenky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1.3)
        self.driver.find_element_by_xpath(letenkyVeFiltruSwitchXpath).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

