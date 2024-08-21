from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent, URL, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC
from FWSK.groupsearch_D import groupSearch_D
from FWSK.SRL_D import SRL_D
import time
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web

banneryXpath_FWSK = "//*[@class='f_teaser-item']/a"
URL_prod_public = "https://www.fischer.sk/"
URL_deploying_web = URL

HPvyhledatZajezdyButtonXpath = "//*[@class='f_button f_button--forFilter']"
#HPvyhledatZajezdyButtonXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[@class='f_filterMainSearch-content']/div[@class='f_filterMainSearch-content-item'][5]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam cestujete?')]"
HPzlutakReckoDestinaceXpath = "//*[@value='st67']"
#HPzlutakReckoDestinaceXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-content']/div[@class='f_filter f_filter--destination']/div[@class='f_customScroll js_destinationsContent']/div[1]/div[@class='f_column']/div[@class='f_column-item'][1]/div[@class='f_list']/div[@class='f_list-item'][1]/div[@class='f_input-wrapper']/label[@class='f_input f_input--checkbox']/span[@class='f_input-content']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovať')]"
HPzlutakPokracovatButtonXpathStep2 = "/html/body/header/div/div[2]/div/div/div/div/div[3]/div[2]/div[3]/div[2]/a/span"
HPzlutakLetniPrazdninyXpath = "//*[@class='f_filter-item']//*[contains(text(), 'September')]"
HPzlutakPokracovatButtonXpathStep3 ="/html/body/header/div/div[2]/div/div/div/div/div[3]/div[3]/div[3]/div[2]/a/span"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdiť a vyhľadať')]"

poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávacie zájazdy')]"


def hp_zlutak_to_SRL(driver, kamPojedete, destinace, pokracovatBtn1, pokracovatBtn2, termin, pokracovatBtn3, obsazenost,
                     potvrditAvyhledat, generalTimeSleep=1.5):
    wait = WebDriverWait(driver, 300)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(kamPojedete))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(destinace))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn1))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn2))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(termin))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(pokracovatBtn3))).click()

    wait.until(EC.visibility_of(driver.find_element_by_xpath(obsazenost))).click()

    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element_by_xpath(potvrditAvyhledat))).click()
    time.sleep(4)

from FWSK.to_import import URL_local
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
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)

        #HPzlutakPokracovatButtonXpathStep3 = "/html/body/header/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[2]/a/span"

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath, HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         ,HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath, HPzlutakPotvrditAvyhledatXpath )
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, self.URL, banneryXpath_FWSK)

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
