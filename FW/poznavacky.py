from selenium.webdriver.common.by import By
import time
from FW.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky, setUp, tearDown, generalDriverWaitImplicit
import unittest

from helpers.helper import Helpers
from sedivka_check import sedivka_check_assert
sedivkaXpathFw = "//*[@class='f_box h-full flex flex-col']"
kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"

def poznavacky_check_D(self, driver):

    generalDriverWaitImplicit(self.driver)
    generalDriverWaitImplicit(self.driver)

    imgs = self.driver.find_elements(By.XPATH, "//*[@class='f_tile-image-content']")
    self.logger.info(imgs)
    x = 0
    assert imgs[0].is_displayed() == True
    for _ in imgs:
        imgsDisplayed = imgs[x].is_displayed()
        x = x + 1

        assert imgsDisplayed == True
        self.logger.info("true imgdisplay")

    gridItems = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid-item']")
    self.driver.execute_script("arguments[0].scrollIntoView();", gridItems[0])
    assert gridItems[0].is_displayed() == True
    y = 0
    for _ in gridItems:
        gridItemDisplayed = gridItems[y].is_displayed()
        assert gridItemDisplayed == True
        y = y + 1
        self.logger.info("grid true")

    gridBig = self.driver.find_elements(By.XPATH, "//*[@class='f_tileGrid']")
    a = 0
    assert gridBig[0].is_displayed() == True
    for _ in gridBig:
        gridBigDisplayed = gridBig[a].is_displayed()
        assert gridBigDisplayed == True
        a = a + 1
        self.logger.info("big grid ture")

def proklik_kostkaHotelu_toDetail_check_sedivka(driver):
            element = driver.find_element(By.XPATH, kostkaPoznavackaXpath)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            element.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[2])
            time.sleep(1)
            self.logger.info(driver.current_url)
            sedivka_check_assert(driver, sedivkaXpathFw)


from FW.to_import import URL_local

kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"


class TestPoznavacky_D(unittest.TestCase):

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

    def test_poznavacky_okruzni_D(self):
        self.driver.maximize_window()
        URL_poznavacky_lp = f"{self.URL}{URL_poznavacky}"
        self.driver.get(URL_poznavacky_lp)
        acceptConsent(self.driver)
        time.sleep(3)
        Helpers.poznavacky_display_check(self.driver, self.logger)
        self.test_passed = True

    def test_poznavacky_vikendy_D(self):
        self.driver.maximize_window()
        URL_poznavacky_vikendy_lp = f"{self.URL}{URL_poznavacky_vikendy}"
        self.driver.get(URL_poznavacky_vikendy_lp)
        acceptConsent(self.driver)
        time.sleep(3)
        Helpers.poznavacky_display_check(self.driver, self.logger)
        self.test_passed = True

    def test_poznavacky_rodiny_D(self):
        self.driver.maximize_window()
        URL_poznavacky_rodiny_lp = f"{self.URL}{URL_poznavacky_rodiny}"
        self.driver.get(URL_poznavacky_rodiny_lp)
        acceptConsent(self.driver)
        time.sleep(3)
        Helpers.poznavacky_display_check(self.driver, self.logger)
        self.test_passed = True

    def test_poznavacky_zazitky_D(self):
        self.driver.maximize_window()
        URL_poznavacky_zazitky_lp = f"{self.URL}{URL_poznavacky_zazitky}"
        self.driver.get(URL_poznavacky_zazitky_lp)

        acceptConsent(self.driver)
        time.sleep(3)
        Helpers.poznavacky_display_check(self.driver, self.logger)
        self.test_passed = True

    def test_poznavacky_okruzni_C(self):
        URL_poznavacky_lp = f"{self.URL}{URL_poznavacky}"
        self.driver.get(URL_poznavacky_lp)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(10)
        kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"
        element3 = self.driver.find_elements(By.XPATH, kostkaPoznavackaXpath)[6]
        self.driver.execute_script("arguments[0].scrollIntoView();", element3)
        time.sleep(2)
        element3.click()
        self.driver.switch_to.window(
            self.driver.window_handles[1])
        time.sleep(1)
        self.logger.info(self.driver.current_url)
        sedivka_check_assert(self.driver, sedivkaXpathFw)
        self.test_passed = True

    def test_poznavacky_vikendy_C(self):
        URL_poznavacky_vikendy_lp = f"{self.URL}{URL_poznavacky_vikendy}"
        self.driver.get(URL_poznavacky_vikendy_lp)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(5)
        Helpers.proklik_kostkaHotelu_toDetail_check_sedivka(self.driver, kostkaPoznavackaXpath, sedivkaXpathFw, self.logger)

        self.test_passed = True

    def test_poznavacky_rodiny_C(self):
        URL_poznavacky_rodiny_lp = f"{self.URL}{URL_poznavacky_rodiny}"
        self.driver.get(URL_poznavacky_rodiny_lp)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(5)
        Helpers.proklik_kostkaHotelu_toDetail_check_sedivka(self.driver, kostkaPoznavackaXpath, sedivkaXpathFw, self.logger)

        self.test_passed = True

    def test_poznavacky_zazitky_C(self):
        URL_poznavacky_zazitky_lp = f"{self.URL}{URL_poznavacky_zazitky}"
        self.driver.get(URL_poznavacky_zazitky_lp)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(5)
        Helpers.proklik_kostkaHotelu_toDetail_check_sedivka(self.driver, kostkaPoznavackaXpath, sedivkaXpathFw, self.logger)

        self.test_passed = True