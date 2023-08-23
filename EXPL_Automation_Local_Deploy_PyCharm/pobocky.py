from webdriver_manager.chrome import ChromeDriverManager
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

warszawaAnchorOblibeneVolbyXpath = "(//span[contains(text(),'Warszawa')])[1]"
pobockaBoxXpath = "//*[@data-branch-id='519']"
detailPobockyXpath = pobockaBoxXpath + "//*[contains(text(), 'Szczegóły oddziału')]"

class TestPobocky_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_pobocky_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_pobocky)

        time.sleep(6)
        acceptConsent(self.driver)

        time.sleep(2)
        mapa = self.driver.find_element_by_xpath("//*[@class='leaflet-pane leaflet-tile-pane']")    ## jen jeden element, no need to call find_elementS
        self.driver.execute_script("arguments[0].scrollIntoView();", mapa)

        mapaDisplayed = mapa.is_displayed()
        assert mapaDisplayed == True
        print("Map is displayed")


        mapaKolecka = self.driver.find_elements_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
        y=0
        for y in mapaKolecka:
            mapaKoleckaDisplayed = mapaKolecka[y].is_displayed()

            y=y+1
            print("mapa kolecka")
            assert mapaKoleckaDisplayed == True

        generalDriverWaitImplicit(self.driver)
        time.sleep(3.5)
        basicInfo = self.driver.find_elements_by_xpath("//*[@class='f_branch-basicInfo']")
        a=0
        assert basicInfo[0].is_displayed() == True
        for _ in basicInfo:
            basicInfoDisplay = basicInfo[a].is_displayed()

            print("basic info ")
            assert basicInfoDisplay == True
            a=a+1

        generalDriverWaitImplicit(self.driver)
        pobockaBoxiky = self.driver.find_elements_by_xpath("//*[@class='f_branch-header-item']")
        x = 0
        for _ in pobockaBoxiky:
            pobockaBoxikyDisplay = pobockaBoxiky[x].is_displayed()

            print("boxiky")
            assert pobockaBoxikyDisplay == True
            x = x + 1

        assert pobockaBoxiky[0].is_displayed() == True

        self.test_passed = True
