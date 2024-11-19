from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from DERRO.to_import import acceptConsent, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

BucurestOblibeneVolbyXpath = "(//span[normalize-space()='Bucuresti'])[1]"
pobockaBoxXpath = "(//div[contains(text(),'Agentia din Alba Iulia Avram Iancu')])[1]"
detailPobockyXpath = pobockaBoxXpath + "(//span[@class='f_button-text f_icon f_icon_set--right f_icon--chevronRight'][normalize-space()='Detalii agentie'])[1]"

from DERRO.to_import import URL_local
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

        time.sleep(6)
        acceptConsent(self.driver)

        time.sleep(2)
        mapa = self.driver.find_element(By.XPATH, "//*[@class='leaflet-pane leaflet-tile-pane']")    ## jen jeden element, no need to call find_elementS
        self.driver.execute_script("arguments[0].scrollIntoView();", mapa)

        mapaDisplayed = mapa.is_displayed()
        assert mapaDisplayed == True
        self.logger.info("Map is displayed")


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
