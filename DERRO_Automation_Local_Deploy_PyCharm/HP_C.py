from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit, sendEmail
import unittest
from selenium.webdriver.support import expected_conditions as EC
from DERRO_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from DERRO_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web

URL_deploying_web = "https://dertourro.web11.dtweb.cz/"
URL_prod_public = "https://www.dertour.ro/"
banneryXpath = "//*[@class='f_teaser-item']/a"

vyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Cauta acum'])[1]"
kamPojedeteButtonXpath = "//div[@class='f_button-title' and contains(text(), 'Destinatie')]"
zlutakEgiptDestinaceXpath= "//body[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/label[1]/span[2]/span[1]"
zlutakPokracovatButtonXpath = "(//span[contains(text(),'Continua')])[1]"
zlutakPokracovatButtonXpathStep2 ="(//a[@class='f_button f_button--common'])[2]"
zlutakVyberTerminuXpath = "//div[contains(text(),'Perioada')]"
zlutakZima2024Xpath = "//span[contains(text(), 'calatorie de iarna 2024')]"
zlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Continua')])[3]"
zlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Familie 2+1')]"
zlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Confirma si cauta')]"
nejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"

VyletyEgipt = "(//span[contains(text(),'Descopera')])[4]"
VyletyThailanda = "(//span[contains(text(),'Descopera')])[5]"
VyletyDubai = "(//span[contains(text(),'Descopera')])[6]"



class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(vyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep( 0.3)
        acceptConsent(self.driver)
        time.sleep(3.5)
        self.driver.find_element_by_xpath(kamPojedeteButtonXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakEgiptDestinaceXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpath).click()
        time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep2).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakZima2024Xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep3).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakObsazenost2plus1Xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakPotvrditAvyhledatXpath).click()

        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_top_hotely(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)

        try:
            topHotely = self.driver.find_element_by_xpath("//*[@class='f_tileGrid f_tileGrid--quad']")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", topHotely)
            time.sleep(2.5)
            topHotelyAll = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid f_tileGrid--quad']")
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

        VyletyEgiptElement = self.driver.find_element_by_xpath(VyletyEgipt)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyEgiptElement)
        time.sleep(5)
        VyletyEgiptElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("(//div[@class='f_searchResult-content'])[1]")
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

        VyletyThailandaElement = self.driver.find_element_by_xpath(VyletyThailanda)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyThailandaElement)
        time.sleep(5)
        VyletyThailandaElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("(//div[@class='f_searchResult-content'])[1]")
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

        VyletyDubaiElement = self.driver.find_element_by_xpath(VyletyDubai)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyDubaiElement)
        time.sleep(5)
        VyletyDubaiElement.click()
        time.sleep(2)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath("(//div[@class='f_searchResult-content'])[1]")
            wait.until(EC.visibility_of(hotelyAllKarty[0]))

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)




