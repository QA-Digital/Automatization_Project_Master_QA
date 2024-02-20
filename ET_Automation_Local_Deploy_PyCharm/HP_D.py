from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from ET_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from selenium.webdriver.support.wait import WebDriverWait
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,sendEmail, URL, URL_LM, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

HPbanneryXpath = "//*[@class='f_teaser-item']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

class TestHP_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_homePage_D(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        bannerSingle = self.driver.find_element_by_xpath(HPbanneryXpath)
        try:
            bannerSingle = self.driver.find_element_by_xpath(HPbanneryXpath)
            bannerAll = self.driver.find_elements_by_xpath(HPbanneryXpath)
            #wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s bannery " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s bannery " + url
            sendEmail(msg)
        assert bannerSingle.is_displayed() == True
        time.sleep(1.5)

    def test_HP_LMnabidky(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)

        try:
            nejnabidkyLMsingle = self.driver.find_element_by_xpath("//*[@class='page-tour']")
            nejnabidkyLMall = self.driver.find_elements_by_xpath("//*[@class='page-tour']")
            wait.until(EC.visibility_of(nejnabidkyLMsingle))
            if nejnabidkyLMsingle.is_displayed():
                for WebElement in nejnabidkyLMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s nej. nabidky LM " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s nej. nabidky LM " + url
            sendEmail(msg)

        assert nejnabidkyLMsingle.is_displayed() == True

        self.test_passed = True


