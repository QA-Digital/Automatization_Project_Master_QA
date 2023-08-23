from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_vlastniDoprava, sendEmail, setUp, tearDown
from selenium.webdriver.support import expected_conditions as EC
from EXPL_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
from EXPL_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
import time
import unittest

banneryXpath = "//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']"
vyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Szukaj'])[1]"
kamPojedeteButtonXpath = "//div[contains(text(),'Kierunek')]"
zlutakPolskoDestinaceXpath= "(//span[@class='font-bold'][normalize-space()='Polska'])[1]"
zlutakPokracovatButtonXpath = "(//span[contains(text(),'Kontynuuj')])[1]"
zlutakPokracovatButtonXpathStep2 ="(//span[contains(text(),'Kontynuuj')])[2]"
zlutakPokracovatVyberTerminuXpath = "//div[contains(text(),'Termin')]"
zlutakZima2024Xpath = "//span[contains(text(), 'Ferie zimowe 2024')]"
zlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Kontynuuj')])[3]"
zlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Rodzina 2+1')]"
zlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potwierdź i wyszukaj')]"
class Test_Vlastni_Doprava(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)

    def test_Homepage_bannery(self):
        self.driver.maximize_window()
        self.driver.get(URL_vlastniDoprava)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        bannerSingle = self.driver.find_element_by_xpath(banneryXpath)
        try:
            bannerSingle = self.driver.find_element_by_xpath(banneryXpath)
            bannerAll = self.driver.find_elements_by_xpath(banneryXpath)
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem s bannery " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s bannery " + url
            sendEmail(msg)
        assert bannerSingle.is_displayed() == True

    def test_Destination_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_vlastniDoprava)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destination = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destination)
            destinationAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destination))
            if destination.is_displayed():
                for WebElement in destinationAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destination.is_displayed() == True

    def test_zlutak_to_groupsearch(self):
        self.driver.get(URL_vlastniDoprava)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(vyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_zlutak_to_SRL(self):
        self.driver.get(URL_vlastniDoprava)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        time.sleep(3.5)

        self.driver.find_element_by_xpath(kamPojedeteButtonXpath).click()
        self.driver.find_element_by_xpath(zlutakPolskoDestinaceXpath).click()
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpath).click()
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep2).click()
        self.driver.find_element_by_xpath(zlutakZima2024Xpath).click()
        self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep3).click()
        self.driver.find_element_by_xpath(zlutakObsazenost2plus1Xpath).click()
        self.driver.find_element_by_xpath(zlutakPotvrditAvyhledatXpath).click()

        SRL_D(self, self.driver)
        self.test_passed = True