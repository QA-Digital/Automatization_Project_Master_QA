from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.to_import import acceptConsent,sendEmail, URL, URL_faq, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

HPbanneryXpath = "//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']"
from DERRO.to_import import URL_local
class TestHP_D(unittest.TestCase):
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

    def test_homePage_banners(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        bannerSingle = self.driver.find_element(By.XPATH, HPbanneryXpath)
        try:
            bannerSingle = self.driver.find_element(By.XPATH, HPbanneryXpath)
            bannerAll = self.driver.find_elements(By.XPATH, HPbanneryXpath)
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
            nejnabidkyLMsingle = self.driver.find_element(By.XPATH, "(//*[@class='f_content-item page-widget js-filteredWidget'])[1]")
            self.driver.execute_script("arguments[0].scrollIntoView();", nejnabidkyLMsingle)
            time.sleep(3)
            nejnabidkyLMall = self.driver.find_elements(By.XPATH, "(//*[@class='f_content-item page-widget js-filteredWidget'])[1]")
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

        nejnabidkyLMsingle = self.driver.find_element(By.XPATH, "(//*[@class='f_content-item page-widget js-filteredWidget'])[1]")
        assert nejnabidkyLMsingle.is_displayed() == True

        self.test_passed = True
