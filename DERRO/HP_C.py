from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.Detail_D import detail_D
from DERRO.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit, sendEmail
import unittest
from selenium.webdriver.support import expected_conditions as EC
from DERRO.groupsearch_D import groupSearch_D
import time
from DERRO.SRL_D import SRL_D
from EW.HP_C import letenkyVeFiltruSwitchXpath
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from helpers.helper import Helpers

URL_deploying_web = URL
URL_prod_public = "https://www.dertour.ro/"
banneryXpath = "//*[@class='f_teaser-item']/a"

vyhledatZajezdyButtonXpath = "//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Gaseste o vacanta']"
kamPojedeteButtonXpath = "//div[normalize-space()='Unde mergi?']"
#zlutakEgiptDestinaceXpath= "//body[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/label[1]/span[2]/span[1]"
zlutakEgiptDestinaceXpath= "//*[@value='st63042']"
zlutakPokracovatButtonXpath = "(//span[contains(text(),'Continua')])[1]"
zlutakPokracovatButtonXpathStep2 ="(//a[@class='f_button f_button--common'])[2]"
zlutakVyberTerminuXpath = "//span[@class='f_input-label !block font-semibold']"
zlutakZima2024Xpath = "//span[contains(text(), 'Vara 2025')]"
zlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Continua')])[3]"
zlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Familie 2+1')]"
zlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Confirma si cauta')]"
nejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"

VyletyEgipt = "(//span[contains(text(),'Descopera')])[4]"
VyletyThailanda = "(//span[contains(text(),'Descopera')])[5]"
VyletyDubai = "(//span[contains(text(),'Descopera')])[6]"
dlazdiceXpath = "//*[@class='f_searchResult-content'])"


from DERRO.to_import import URL_local
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
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, vyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep( 3.3)
        acceptConsent(self.driver)
        time.sleep(3.5)
        self.driver.find_element(By.XPATH, kamPojedeteButtonXpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, zlutakEgiptDestinaceXpath).click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, zlutakPokracovatButtonXpath).click()
        time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, zlutakPokracovatButtonXpathStep2).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, zlutakVyberTerminuXpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, zlutakPokracovatButtonXpathStep3).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, zlutakObsazenost2plus1Xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, zlutakPotvrditAvyhledatXpath).click()

        Helpers.search_results_list_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_top_hotely(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)

        try:
            topHotely = self.driver.find_element(By.XPATH, "//*[@class='f_tileGrid f_tileGrid--quad']")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", topHotely)
            time.sleep(2.5)
            topHotelyAll = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid f_tileGrid--quad']")
            wait.until(EC.visibility_of(topHotely))
            if topHotely.is_displayed():
                for WebElement in topHotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem s hotely, nezobrazuji se" + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s hotely, nezobrazuji se " + url
            sendEmail(msg)

        assert topHotely.is_displayed() == True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath)

        self.test_passed = True

    def test_HP_vyletyEgipt(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        wait = WebDriverWait(self.driver, 25)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyEgiptElement = self.driver.find_element(By.XPATH, VyletyEgipt)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyEgiptElement)
        time.sleep(5)
        VyletyEgiptElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements(By.XPATH, dlazdiceXpath)
            wait.until(EC.visibility_of(hotelyAllKarty[0]))

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

    def test_HP_vyletyThajsko(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        wait = WebDriverWait(self.driver, 25)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyThailandaElement = self.driver.find_element(By.XPATH, VyletyThailanda)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyThailandaElement)
        time.sleep(5)
        VyletyThailandaElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements(By.XPATH, dlazdiceXpath)
            wait.until(EC.visibility_of(hotelyAllKarty[0]))

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

    def test_HP_vyletyDubai(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        wait = WebDriverWait(self.driver, 25)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyDubaiElement = self.driver.find_element(By.XPATH, VyletyDubai)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyDubaiElement)
        time.sleep(5)
        VyletyDubaiElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements(By.XPATH, dlazdiceXpath)
            wait.until(EC.visibility_of(hotelyAllKarty[0]))

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

    def test_HP_zlutak_to_SRL_circuite(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        circuitXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Circuite')]"
        circuitSwitchElement =  self.driver.find_element(By.XPATH, circuitXpath)

        self.driver.execute_script("arguments[0].click();", circuitSwitchElement)
        destinaceItalieXpath = "//*[@value='st63081']"
        time.sleep(3)

        Helpers.hp_zlutak_to_SRL(self.driver, kamPojedeteButtonXpath, destinaceItalieXpath,
                                 zlutakPokracovatButtonXpath, zlutakPokracovatButtonXpathStep2,
                                 zlutakVyberTerminuXpath
                                 , zlutakPokracovatButtonXpathStep3, zlutakObsazenost2plus1Xpath,
                                 zlutakPotvrditAvyhledatXpath, self.logger)
        time.sleep(3)
        Helpers.search_results_list_check(self.driver, self.logger)
        #Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_circuite(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            3.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        circuitXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Circuite')]"
        circuitSwitchElement =  self.driver.find_element(By.XPATH, circuitXpath)

        self.driver.execute_script("arguments[0].click();", circuitSwitchElement)
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, vyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_letenky(self):
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(3.3) ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.3)
        letenkyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Bilete avion')]"
        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, vyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        Helpers.group_search_check(self.driver, self.logger)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_letenky(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        destinaceSAEXpath = "//*[@value='st62984']"

        self.driver.find_element(By.XPATH, letenkyVeFiltruSwitchXpath).click()

        time.sleep(3)
        letenkySrlResultsXpath = "//*[@class='f_searchResult-content-item relative']"
        Helpers.hp_zlutak_to_SRL(self.driver, kamPojedeteButtonXpath, destinaceSAEXpath,
                                 zlutakPokracovatButtonXpath, zlutakPokracovatButtonXpathStep2,
                                 zlutakVyberTerminuXpath
                                 , zlutakPokracovatButtonXpathStep3, zlutakObsazenost2plus1Xpath,
                                 zlutakPotvrditAvyhledatXpath, self.logger)

        time.sleep(4)
        Helpers.SRL_D_letenky(self.driver, letenkySrlResultsXpath, self.logger)
        self.test_passed = True

