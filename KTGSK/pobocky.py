from webdriver_manager.chrome import ChromeDriverManager
from KTGSK.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

from KTGSK.to_import import URL_local
class TestPobocky_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
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
        mapa = self.driver.find_element_by_xpath("//*[@class='leaflet-pane leaflet-tile-pane']")    ## jen jeden element, no need to call find_elementS

        mapaDisplayed = mapa.is_displayed()
        assert mapaDisplayed == True


        mapaKolecka = self.driver.find_elements_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
        y=0
        for _ in mapaKolecka:
            mapaKoleckaDisplayed = mapaKolecka[y].is_displayed()

            y=y+1
            print("mapa kolecka")
            assert mapaKoleckaDisplayed == True




        generalDriverWaitImplicit(self.driver)
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