from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

brnoAnchorOblibeneVolbyXpath = "//*[@class='f_anchor'and contains(text(), 'Brno')]"
pobockaBoxXpath = "//*[@data-branch-id='262']"
detailPobockyXpath = pobockaBoxXpath + "//*[contains(text(), 'Detail pobočky')]"
objednatSchuzkuBtnXpath = "//*[@class='f_button f_button--important js-popupWindow--show js-gtm-eventClick']"
popUpObjednavkaNavstevyXpath = "//*[@class='fshr-popupWindow fshr-popupWindow--centered js-form js-popupWindow fshr-icon fshr-icon--man js-sendByAjax js-gtm-trackGoal']"

def open_pobocka_box_to_detail_open_popup_navstevy(driver, AnchorOblibeneVolbyXpath, pobockaBoxXpath, detailPobockyXpath,objednatSchuzkuBtnXpath, popUpObjednavkaNavstevyXpath):

    AnchorOblibeneVolbyElement = driver.find_element_by_xpath(AnchorOblibeneVolbyXpath)
    AnchorOblibeneVolbyElement.click()

    time.sleep(2)

    pobockaBoxElement = driver.find_element_by_xpath(pobockaBoxXpath)
    pobockaBoxElement.click()

    detailPobockyElement = driver.find_element_by_xpath(detailPobockyXpath)
    driver.execute_script("arguments[0].scrollIntoView();", detailPobockyElement)
    detailPobockyElement.click()
    time.sleep(2)
    objednatSchuzkuBtnElement = driver.find_element_by_xpath(objednatSchuzkuBtnXpath)
    objednatSchuzkuBtnElement.click()

    time.sleep(2)

    popUpObjednavkaNavstevyElement = driver.find_element_by_xpath(popUpObjednavkaNavstevyXpath)
    print("Popup formulář je zobrazený:    ")
    print(popUpObjednavkaNavstevyElement.is_displayed())
    assert popUpObjednavkaNavstevyElement.is_displayed() == True


from FW.to_import import URL_local

class TestPobocky_C(unittest.TestCase):

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
        generalDriverWaitImplicit(self.driver)
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


        basicInfo = self.driver.find_elements_by_xpath("//*[@class='f_branch-basicInfo']")
        a=0
        assert basicInfo[0].is_displayed() == True
        for _ in basicInfo:
            basicInfoDisplay = basicInfo[a].is_displayed()

            print("basic info ")
            assert basicInfoDisplay == True
            a=a+1
        generalDriverWaitImplicit(self.driver)
        pobockaBoxiky = self.driver.find_elements_by_xpath("//*[@class='f_branch-header f_anchor']")
        x = 0
        for _ in pobockaBoxiky:
            pobockaBoxikyDisplay = pobockaBoxiky[x].is_displayed()

            print("boxiky")
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
        open_pobocka_box_to_detail_open_popup_navstevy(self.driver, brnoAnchorOblibeneVolbyXpath, pobockaBoxXpath, detailPobockyXpath,objednatSchuzkuBtnXpath, popUpObjednavkaNavstevyXpath)

        self.test_passed = True