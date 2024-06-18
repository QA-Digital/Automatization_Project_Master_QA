from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent,sendEmail, URL, URL_faq, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

bannerXpath = "//*[@class='f_teaser-item']"
from FWSK.to_import import URL_local
class TestHP_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_homePage_D(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        try:
            bannerSingle = self.driver.find_element_by_xpath(bannerXpath)
            bannerAll = self.driver.find_elements_by_xpath(bannerXpath)
            wait.until(EC.visibility_of(bannerSingle))
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

        try:
            nejnabidkyLMsingleXpath = "//*[@class='f_tourTable-tour']"
            nejnabidkyLMsingle = self.driver.find_element_by_xpath(nejnabidkyLMsingleXpath)
            nejnabidkyLMall = self.driver.find_elements_by_xpath(nejnabidkyLMsingleXpath)
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

