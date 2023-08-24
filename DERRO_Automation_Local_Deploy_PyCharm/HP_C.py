from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from DERRO_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from DERRO_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web

URL_deploying_web = "https://dertourro.web11.dtweb.cz/"
URL_prod_public = "https://www.dertour.ro/"
bannerKdoJsi = "(//div[@class='in_singleCol-item'])[1]"
banneryXpath = "//*[@class='f_teaser-item']/a"

vyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Cauta acum'])[1]"
kamPojedeteButtonXpath = "//div[@class='f_button-title' and contains(text(), 'Destinatie')]"
zlutakEgiptDestinaceXpath= "//body[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/label[1]/span[2]/span[1]"
zlutakPokracovatButtonXpath = "(//span[contains(text(),'Continua')])[1]"
zlutakPokracovatButtonXpathStep2 ="(//*[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right' and contains(text(), 'Continua')])[2]"
zlutakVyberTerminuXpath = "//div[contains(text(),'Perioada')]"
zlutakZima2024Xpath = "//span[contains(text(), 'calatorie de iarna 2024')]"
zlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Continua')])[3]"
zlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Familie 2+1')]"
zlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Confirma si cauta')]"
nejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
nextArrowXpath = "//*[@class='slick-next slick-arrow']"
kartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

#VyletyPoznan = "(//span[@class='f_button f_button--important'])[1]"

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
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        self.driver.find_element_by_xpath(kamPojedeteButtonXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakEgiptDestinaceXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep2).click()
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].scrollIntoView();", zlutakPokracovatButtonXpathStep2)
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

    def test_HP_zlutak_to_SRL(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(kamPojedeteButtonXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakEgiptDestinaceXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakPokracovatButtonXpath))).click()
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakZima2024Xpath))).click()
        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep3))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakObsazenost2plus1Xpath))).click()

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zlutakPotvrditAvyhledatXpath))).click()
        time.sleep(1)
        SRL_D(self, self.driver)

        self.test_passed = True


    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
           2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(nejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(nejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            positionOfCurrentElement = positionOfCurrentElement + 1

        print(nejlepsiNabidkyTextList)

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.implicitly_wait(100)

        nextArrowElement = self.driver.find_element_by_xpath(nextArrowXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", nextArrowElement)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", nextArrowElement)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", nextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", nextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", nextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", nextArrowElement)

        nextkartaHoteluSlider = self.driver.find_element_by_xpath(kartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", nextkartaHoteluSlider)
        action = ActionChains(self.driver)
        kartaHoteluSliderElement = self.driver.find_element_by_xpath(kartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", kartaHoteluSliderElement)
        action.move_to_element(kartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        kartaHoteluSliderElement.click()
        time.sleep(1)
        #self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath)

        self.test_passed = True

    def test_HP_vyletyPoznan(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyPoznanElement = self.driver.find_element_by_xpath(VyletyPoznan)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyPoznanElement)
        time.sleep(5)
        VyletyPoznanElement.click()

        try:
            destinationPoznan = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationPoznanAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationPoznan.is_displayed():
                for WebElement in destinationPoznanAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        print("Destinace jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationPoznan.is_displayed() == True


