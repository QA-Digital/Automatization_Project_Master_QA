from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from FWSK_Automation_Local_Deploy_PyCharm.FM_D import LM_FM_vypis_rozbalit_zajezd_check


class TestLM_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_lm)
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
