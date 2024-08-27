from FW.to_import import print_lock
import time
from FW.to_import import print_lock
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from FW.FM_D import LM_FM_vypis_rozbalit_zajezd_check


from FW.to_import import URL_local

class TestLM_D(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        URL_lm_lp = f"{self.URL}{URL_lm}"
        self.driver.get(URL_lm_lp)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        # try:
        #     zajezdyLMsingle = self.driver.find_element_by_xpath("//*[@class='page-tour']")
        #     zajezdyLMall = self.driver.find_elements_by_xpath("//*[@class='page-tour']")
        #     wait.until(EC.visibility_of(zajezdyLMsingle))
        #     if zajezdyLMsingle.is_displayed():
        #         for WebElement in zajezdyLMall:
        #             jdouvidet = WebElement.is_displayed()
        #             assert jdouvidet == True
        #             if jdouvidet == True:
        #                 pass
        #
        #             else:
        #                 url = self.driver.current_url
        #                 msg = "Problem s LM  zajezdy se neukazuji " + url
        #                 sendEmail(msg)
        #
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem s LM  zajezdy se neukazuji " + url
        #     sendEmail(msg)
        # assert zajezdyLMsingle.is_displayed() == True

        LM_FM_vypis_rozbalit_zajezd_check(self, self.driver)

        self.test_passed = True

