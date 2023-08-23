from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from EXPL_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from EXPL_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
#from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check, generalized_list_of_url_checker

URL_deploying_web = "https://eximpl.web11.dtweb.cz/"
URL_prod_public = "https://www.exim.pl/"
banneryXpath_EWPL = "//*[@class='f_teaser-item']/a"

HPvyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Szukaj'])[1]"
HPkamPojedeteButtonXpath = "//div[contains(text(),'Kierunek')]"
HPzlutakTurcjaDestinaceXpath= "//body[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[4]/div[1]/span[1]/label[1]/span[1]"
HPzlutakPokracovatButtonXpath = "(//span[contains(text(),'Kontynuuj')])[1]"
HPzlutakPokracovatButtonXpathStep2 ="(//span[contains(text(),'Kontynuuj')])[2]"
HPzlutakPokracovatVyberTerminuXpath = "//div[contains(text(),'Termin')]"
HPzlutakZima2024Xpath = "//span[contains(text(), 'Ferie zimowe 2024')]"
HPzlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Kontynuuj')])[3]"
HPzlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Rodzina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potwierdź i wyszukaj')]"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

VyletyPoznan = "(//span[@class='f_button f_button--important'])[1]"
VyletyLublin = "(//span[@class='f_button f_button--important'])[2]"
VyletyGdansk = "(//span[@class='f_button f_button--important'])[3]"


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
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
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
        self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath).click()
        self.driver.find_element_by_xpath(HPzlutakTurcjaDestinaceXpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2).click()
        self.driver.find_element_by_xpath(HPzlutakZima2024Xpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep3).click()
        self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath).click()
        self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath).click()

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
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
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
        HPkartaHoteluSliderElement.click()
        time.sleep(1)
        #self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EWPL)

        self.test_passed = True

    def test_HP_nabidka_Podroze_marzen(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        time.sleep(2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1)

        Offer1 = self.driver.find_elements_by_xpath("(//a)[59]")[0].get_attribute('href')
        Offer2 = self.driver.find_elements_by_xpath("(//a)[60]")
        Offer3 = self.driver.find_elements_by_xpath("(//a)[61]")
        Offer4 = self.driver.find_elements_by_xpath("(//a)[62]")

        HPtopNabidkaElements = [Offer1, Offer2, Offer3, Offer4]
        print(HPtopNabidkaElements)
        time.sleep(4)
        linksToCheck_List = []
        for _ in HPtopNabidkaElements:
           odkazLink = HPtopNabidkaElements
           linksToCheck_List.append(odkazLink)
           print(odkazLink)

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

    def test_HP_vyletyLublin(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyLublinElement = self.driver.find_element_by_xpath(VyletyLublin)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyLublinElement)
        time.sleep(5)
        VyletyLublinElement.click()

        try:
            destinationLublin = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationLublinAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationLublin.is_displayed():
                for WebElement in destinationLublinAll:
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

        assert destinationLublin.is_displayed() == True

    def test_HP_vyletyGdansk(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyGdanskElement = self.driver.find_element_by_xpath(VyletyGdansk)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyGdanskElement)
        time.sleep(5)
        VyletyGdanskElement.click()

        try:
            destinationGdansk = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationGdanskAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationGdansk.is_displayed():
                for WebElement in destinationGdanskAll:
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

        assert destinationGdansk.is_displayed() == True


