from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from ND.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import *

##global
terminyAcenyTabXpath = "//*[@class='f_anchor' and contains(text(),'Termíny a ceny')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"


from ND.to_import import URL_local
class TestDetailHotelu_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def omlouvamese_paragraph(self):
        time.sleep(1)
        try:
            omlouvameParagraph = self.driver.find_element_by_xpath(
                "//*[@class='fshr-paragraph fshr-paragraph--centered']")
            if omlouvameParagraph.is_displayed():
                return

        except NoSuchElementException:
            pass

    def test_detail_terminy_D(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)

        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        zobrazeneTerminy = driver.find_elements_by_xpath("//*[@class='font-bold text-[--secondary] text-sm md:text-xl']")

        try:
            for WebElement in zobrazeneTerminy:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    pass

        except NoSuchElementException:
            pass

        assert zobrazeneTerminy[0].is_displayed() == True
        time.sleep(3)


    def test_detail_fotka(self):

        self.driver.maximize_window()
        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(5)
        imageDetail = self.driver.find_element_by_xpath(
            "//swiper-slide[@aria-label='1 / 16']//img")
        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            # time.sleep(5)
            image = self.driver.find_element_by_xpath("/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                print("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

        self.test_passed = True


