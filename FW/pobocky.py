from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

from helpers.helper import Helpers

brnoAnchorOblibeneVolbyXpath = "//*[@class='f_anchor'and contains(text(), 'Brno')]"
pobockaBoxXpath = "//*[@data-branch-id='262']"
detailPobockyXpath = pobockaBoxXpath + "//*[contains(text(), 'Detail pobočky')]"
objednatSchuzkuBtnXpath = "//a[contains(@class,'f_button--important js-gtm-eventClick')]//span[@class='f_button-text'][contains(text(),'Objednat schůzku')]"
popUpObjednavkaNavstevyXpath = "//*[@class='p-[clamp(16px,5vw,22px)] flex-grow overflow-auto pt-0']"

def open_pobocka_box_to_detail_open_popup_navstevy(driver, AnchorOblibeneVolbyXpath, pobockaBoxXpath, detailPobockyXpath,objednatSchuzkuBtnXpath, popUpObjednavkaNavstevyXpath, logger):

    AnchorOblibeneVolbyElement = driver.find_element(By.XPATH, AnchorOblibeneVolbyXpath)
    AnchorOblibeneVolbyElement.click()

    time.sleep(2)

    pobockaBoxElement = driver.find_element(By.XPATH, pobockaBoxXpath)
    pobockaBoxElement.click()
    time.sleep(2)
    detailPobockyElement = driver.find_element(By.XPATH, detailPobockyXpath)
    driver.execute_script("arguments[0].scrollIntoView();", detailPobockyElement)
    detailPobockyElement.click()
    time.sleep(3.5)
    objednatSchuzkuBtnElement = driver.find_element(By.XPATH, objednatSchuzkuBtnXpath)
    #objednatSchuzkuBtnElement.click()
    driver.execute_script("arguments[0].click();", objednatSchuzkuBtnElement)

    time.sleep(2.5)

    popUpObjednavkaNavstevyElement = driver.find_element(By.XPATH, popUpObjednavkaNavstevyXpath)
    logger.info("Popup formulář je zobrazený:    ")
    logger.info(popUpObjednavkaNavstevyElement.is_displayed())
    assert popUpObjednavkaNavstevyElement.is_displayed() == True


from FW.to_import import URL_local

class TestPobocky_C(unittest.TestCase):

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


    def test_pobocky_D(self):

        URL_pobocky_lp = f"{self.URL}{URL_pobocky}"
        self.driver.get(URL_pobocky_lp)
        acceptConsent(self.driver)
        self.driver.maximize_window()
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        mapa = self.driver.find_element(By.XPATH, "//*[@class='leaflet-pane leaflet-tile-pane']")    ## jen jeden element, no need to call find_elementS

        mapaDisplayed = mapa.is_displayed()
        assert mapaDisplayed == True


        mapaKolecka = self.driver.find_elements(By.XPATH, "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
        y=0
        for _ in mapaKolecka:
            mapaKoleckaDisplayed = mapaKolecka[y].is_displayed()

            y=y+1
            self.logger.info("mapa kolecka")
            assert mapaKoleckaDisplayed == True


        basicInfo = self.driver.find_elements(By.XPATH, "//*[@class='f_branch-basicInfo']")
        a=0
        assert basicInfo[0].is_displayed() == True
        for _ in basicInfo:
            basicInfoDisplay = basicInfo[a].is_displayed()

            self.logger.info("basic info ")
            assert basicInfoDisplay == True
            a=a+1
        generalDriverWaitImplicit(self.driver)
        pobockaBoxiky = self.driver.find_elements(By.XPATH, "//*[@class='f_branch-header f_anchor']")
        x = 0
        for _ in pobockaBoxiky:
            pobockaBoxikyDisplay = pobockaBoxiky[x].is_displayed()

            self.logger.info("boxiky")
            assert pobockaBoxikyDisplay == True
            x = x + 1

        assert pobockaBoxiky[0].is_displayed() == True

        self.test_passed = True


    def test_pobocky_C_click_to_detail_popup_check(self):
        self.driver.maximize_window()
        URL_pobocky_lp = f"{self.URL}{URL_pobocky}"
        self.driver.get(URL_pobocky_lp)
        acceptConsent(self.driver)

        time.sleep(3.5)
        Helpers.open_pobocka_box_to_detail_open_popup_navstevy(self.driver, brnoAnchorOblibeneVolbyXpath, pobockaBoxXpath, detailPobockyXpath,objednatSchuzkuBtnXpath, popUpObjednavkaNavstevyXpath, self.logger)

        self.test_passed = True