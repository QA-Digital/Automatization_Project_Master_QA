from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ND.to_import import acceptConsent, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest
from FW.pobocky import open_pobocka_box_to_detail_open_popup_navstevy

brnoAnchorOblibeneVolbyXpath = "//span[contains(text(),'Brno')]"
pobockaBoxXpath = "//div[@class='f_list f_list--branch']//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]"
detailPobockyXpath = "//a[@href='/pobocky/brno-centrum']//span[@class='f_button-text f_icon f_icon_set--right f_icon--chevronRight'][contains(text(),'Detail pobočky')]"
objednatSchuzkuBtnXpath = "//*[@class='f_button f_button--important js-popupWindow--show js-gtm-eventClick']"
popUpObjednavkaNavstevyXpath = "//*[@class='fshr-popupWindow fshr-popupWindow--centered js-form js-popupWindow fshr-icon fshr-icon--man js-sendByAjax js-gtm-trackGoal']"

from ND.to_import import URL_local
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
        self.driver.maximize_window()
        URL_pobocky_lp = f"{self.URL}{URL_pobocky}"
        self.driver.get(URL_pobocky_lp)

        time.sleep(4)
        acceptConsent(self.driver)

        time.sleep(10)
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


        generalDriverWaitImplicit(self.driver)
        time.sleep(3.5)
        basicInfo = self.driver.find_elements(By.XPATH, "//*[@class='f_branch-basicInfo']")
        a=0
        assert basicInfo[0].is_displayed() == True
        for _ in basicInfo:
            basicInfoDisplay = basicInfo[a].is_displayed()

            self.logger.info("basic info ")
            assert basicInfoDisplay == True
            a=a+1

        generalDriverWaitImplicit(self.driver)
        pobockaBoxiky = self.driver.find_elements(By.XPATH, "//*[@class='f_branch-header-item']")
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
        self.driver.get(URL_pobocky)
        time.sleep(4)
        acceptConsent(self.driver)
        time.sleep(10)

        AnchorOblibeneVolbyElement = self.driver.find_element(By.XPATH, brnoAnchorOblibeneVolbyXpath)
        AnchorOblibeneVolbyElement.click()

        time.sleep(2)

        pobockaBoxElement = self.driver.find_element(By.XPATH, pobockaBoxXpath)
        pobockaBoxElement.click()

        element = self.driver.find_element(By.XPATH, "//a[@href='/pobocky/brno-centrum']//span[@class='f_button-text f_icon f_icon_set--right f_icon--chevronRight'][contains(text(),'Detail pobočky')]")
        self.driver.execute_script("arguments[0].click();", element)


        self.test_passed = True