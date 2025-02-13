from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent, URL, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC
from FWSK.groupsearch_D import groupSearch_D
from FWSK.SRL_D import SRL_D
import time
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from helpers.helper import Helpers

banneryXpath_FWSK = "//*[@class='f_teaser-item']/a"
URL_prod_public = "https://www.fischer.sk/"
URL_deploying_web = URL

HPvyhledatZajezdyButtonXpath = "//*[@class='f_button f_button--forFilter']"
#HPvyhledatZajezdyButtonXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[@class='f_filterMainSearch-content']/div[@class='f_filterMainSearch-content-item'][5]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam cestujete?')]"
HPzlutakReckoDestinaceXpath = "//*[@value='st63184']"
#HPzlutakReckoDestinaceXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-content']/div[@class='f_filter f_filter--destination']/div[@class='f_customScroll js_destinationsContent']/div[1]/div[@class='f_column']/div[@class='f_column-item'][1]/div[@class='f_list']/div[@class='f_list-item'][1]/div[@class='f_input-wrapper']/label[@class='f_input f_input--checkbox']/span[@class='f_input-content']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovať')]"
HPzlutakPokracovatButtonXpathStep2 = "//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovať')]"
HPzlutakLetniPrazdninyXpath = "//*[@class='f_filter-item']//*[contains(text(), 'Leto 2025')]"
HPzlutakPokracovatButtonXpathStep3 ="//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovať')]"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdiť a vyhľadať')]"

poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávacie zájazdy')]"
letenkyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Letenky')]"

def hp_zlutak_to_SRL(driver, kamPojedete, destinace, pokracovatBtn1, pokracovatBtn2, termin, pokracovatBtn3, obsazenost,
                     potvrditAvyhledat, generalTimeSleep=1.5):
    wait = WebDriverWait(driver, 300)
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, kamPojedete))).click()

    wait.until(EC.visibility_of(driver.find_element(By.XPATH, destinace))).click()

    wait.until(EC.visibility_of(driver.find_element(By.XPATH, pokracovatBtn1))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, pokracovatBtn2))).click()

    wait.until(EC.visibility_of(driver.find_element(By.XPATH, termin))).click()
    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, pokracovatBtn3))).click()

    wait.until(EC.visibility_of(driver.find_element(By.XPATH, obsazenost))).click()

    time.sleep(generalTimeSleep)
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, potvrditAvyhledat))).click()
    time.sleep(4)

from FWSK.to_import import URL_local
class Test_HP_C(unittest.TestCase):
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

    def test_HP_zlutak_to_groupsearch(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath, HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         ,HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath, HPzlutakPotvrditAvyhledatXpath )
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, self.URL, banneryXpath_FWSK)

        self.test_passed = True

    def test_HP_zlutak_to_SRL_lyze(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        lyzeVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Lyžovanie')]"
        self.driver.find_element(By.XPATH, lyzeVeFiltruSwitchXpath).click()
        HPzlutakJarniPrazdninyXpath = "//*[contains(text(), 'Marec a apríl')]"
        destinaceItalieXpath = "//*[@value='st63081']"
        time.sleep(3)

        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceItalieXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakJarniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath, self.logger)
        time.sleep(10)
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_poznavacky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element(By.XPATH, poznavackyVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_poznavacky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        destinaceEgyptXpath = "//*[@value='st63042']"
        self.driver.find_element(By.XPATH, poznavackyVeFiltruSwitchXpath).click()
        HPzlutakBrezenDubenXpath = "//*[contains(text(), 'Leto 2025')]"
        time.sleep(3)
        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                                 HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2,
                                 HPzlutakBrezenDubenXpath
                                 , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                                 HPzlutakPotvrditAvyhledatXpath, self.logger)
        time.sleep(10)  # nevdama proste nez se nacte
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_letenky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        destinaceEgyptXpath = "//*[@value='st63038']"

        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        time.sleep(3)
        letenkySrlResultsXpath = "//*[@class='f_searchResult-content-item relative']"
        HPzlutakBrezenDubenXpath = "//*[contains(text(), 'Máj a jún')]"
        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakBrezenDubenXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath, self.logger)


        Helpers.SRL_D_letenky(self.driver, letenkySrlResultsXpath, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_letenky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1.3)
        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True
