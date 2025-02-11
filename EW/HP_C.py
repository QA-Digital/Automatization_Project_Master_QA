from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from EW.Detail_D import detail_D
from EW.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from EW.groupsearch_D import groupSearch_D
import time
from EW.SRL_D import SRL_D
from FW.HP_C import hp_zlutak_to_SRL
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check, generalized_list_of_url_checker
from helpers.helper import Helpers

URL_deploying_web = URL
URL_prod_public = "https://www.eximtours.cz/"
banneryXpath_EW = "//*[@class='f_teaser-item']/a"

HPvyhledatZajezdyButtonXpath = "//*[@class='f_filterMainSearch']//*[contains(text(), 'Vyhledat dovolenou')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam se chystáte?')]"
HPzlutakReckoDestinaceXpath ="//*[@value='st63184']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
HPzlutakPokracovatButtonXpathStep2 = "//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovat')]"
HPzlutakPokracovatButtonXpathStep3 ="//div[@class='f_filterHolder js_filterHolder f_set--active']//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][contains(text(),'Pokračovat')]"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"



HPzlutakPokracovatVyberTerminuXpath = "/html/body/header/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div[2]/a/span"



HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
# HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']"
#HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']/a"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"


#HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Letní prázdniny 2023')]"


poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávací zájezdy')]"
exVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Exotická dovolená')]"
HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Březen / Duben 2025')]"
letenkyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Letenky')]"
lyzeVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Lyžování')]"


def SRL_D_letenky(driver, SRLresultsLetenkyXpath):
    letenekySRLresultsElements = driver.find_elements(By.XPATH, SRLresultsLetenkyXpath)
    pozice = 0
    for i in letenekySRLresultsElements:
        assert letenekySRLresultsElements[pozice].is_displayed() == True
        pozice = pozice + 1

from EW.to_import import URL_local
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

    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            4.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_poznavacky(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element(By.XPATH, poznavackyVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_lyze(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            1.6)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        #self.driver.find_element(By.XPATH, lyzeVeFiltruSwitchXpath).click()
        time.sleep(3.5)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(4.5)
        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath,
                                 HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2,
                                 HPzlutakLetniPrazdninyXpath
                                 , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                                 HPzlutakPotvrditAvyhledatXpath, self.logger)
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_poznavacky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(6.5)
        HPzlutakBrezenDubenXpath = "//*[contains(text(), 'Březen / Duben 2025')]"
        destinacetXpath = "//*[@value='st63147']"
        HPzlutakObsazenost2Xpath = "//*[contains(text(), 'Pár')]"
        self.driver.find_element(By.XPATH, poznavackyVeFiltruSwitchXpath).click()

        time.sleep(5)

        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinacetXpath,
                                 HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2,
                                 HPzlutakBrezenDubenXpath
                                 , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2Xpath,
                                 HPzlutakPotvrditAvyhledatXpath, self.logger)
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_exotika(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        exVeFiltruSwitchElement =  self.driver.find_element(By.XPATH, exVeFiltruSwitchXpath)

        self.driver.execute_script("arguments[0].click();", exVeFiltruSwitchElement)
        HPzlutakJarniPrazdninyXpath = "//*[contains(text(), 'Květen / Červen 2025')]"
        destinaceItalieXpath = "//*[@value='st63042']"
        time.sleep(3)

        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceItalieXpath,
                                 HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2,
                                 HPzlutakJarniPrazdninyXpath
                                 , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                                 HPzlutakPotvrditAvyhledatXpath, self.logger)
        time.sleep(3)
        #Helpers.search_results_list_check(self.driver, self.logger)
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
           2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements(By.XPATH, HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            # print (nejlepsiNabidkyTextList)
            positionOfCurrentElement = positionOfCurrentElement + 1

        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPnejlepsiZajezdySwitchButtonXpath)))
        HPnejlepsiZajezdySwitchButtonElement = self.driver.find_element(By.XPATH, HPnejlepsiZajezdySwitchButtonXpath)
        self.driver.execute_script("arguments[0].click();", HPnejlepsiZajezdySwitchButtonElement)
        time.sleep(6)
        time.sleep(6)
        self.driver.implicitly_wait(10)
        nejlepsiNabidkyElement = self.driver.find_elements(By.XPATH, HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement2 = 0
        nejlepsiNabidkyTextList2 = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement2].text
            nejlepsiNabidkyTextList2.append(nejlepsiNabidkyTextDefault)
            # self.logger.info(nejlepsiNabidkyTextList)
            positionOfCurrentElement2 = positionOfCurrentElement2 + 1

        self.logger.info(nejlepsiNabidkyTextList)
        self.logger.info(nejlepsiNabidkyTextList2)
        assert nejlepsiNabidkyTextList != nejlepsiNabidkyTextList2

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        #        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPnextArrowXpath))).click()

        self.driver.implicitly_wait(100)

        HPnextArrowElement = self.driver.find_element(By.XPATH, HPnextArrowXpath)
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
        HPnextkartaHoteluSlider = self.driver.find_element(By.XPATH, HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element(By.XPATH, HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        # HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_zlutak_to_SRL_lyze(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        self.driver.find_element(By.XPATH, lyzeVeFiltruSwitchXpath).click()
        HPzlutakJarniPrazdninyXpath = "//*[contains(text(), 'Březen / Duben')]"
        destinaceItalieXpath = "//*[@value='st62993']"
        time.sleep(3)

        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceItalieXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakJarniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath, self.logger)
        time.sleep(10)
        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)

        self.test_passed = True

    def test_HP_top_nabidka_status(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

        time.sleep(2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1)
        #HPtopNabidkaXpath = "//*[@class='page-widget js-ajaxPlaceholder--widget fshr-widget f_tileGrid-item']//*[@class='f_button-text f_icon f_icon_set--right f_icon--chevronRight']"
        HPtopNabidkaXpath= "//*[@class='js-ajaxPlaceholder--widgetContent']/a"
        HPtopNabidkaElements = self.driver.find_elements(By.XPATH, HPtopNabidkaXpath)
        HPtopNabidkaElement = HPtopNabidkaElements[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", HPtopNabidkaElement)
        time.sleep(4)
        linksToCheck_List = []
        pozice = 0
        for _ in HPtopNabidkaElements:
            odkazLink = HPtopNabidkaElements[pozice].get_attribute("href")
            #odkazLink = HPtopNabidkaElements[pozice].get_attribute("a")
            linksToCheck_List.append(odkazLink)
            self.logger.info(odkazLink)
            pozice = pozice + 1

        generalized_list_of_url_checker(linksToCheck_List)

    def test_HP_zlutak_to_SRL_letenky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        destinaceEgyptXpath = "//*[@value='st62984']"

        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        time.sleep(3)
        letenkySrlResultsXpath = "//*[@class='f_searchResult-content-item relative']"
        HPzlutakBrezenDubenXpath = "//*[contains(text(), 'Březen / Duben 2025')]"
        Helpers.hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakBrezenDubenXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath, self.logger)

        time.sleep(4)
        Helpers.SRL_D_letenky(self.driver, letenkySrlResultsXpath, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_letenky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(3.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.3)
        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

