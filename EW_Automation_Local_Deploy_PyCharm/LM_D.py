from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from FW.FM_D import LM_FM_vypis_rozbalit_zajezd_check

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
        #
        # try:
        #     rozbal = self.driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
        #     wait.until(EC.visibility_of(rozbal))
        #     self.driver.execute_script("arguments[0].click();", rozbal)
        #     time.sleep(2)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = " Nepodarilo se rozbalit LM zajezd " + url
        #     sendEmail(msg)
        #
        # try:
        #     rozbalenyZajezd = self.driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
        #     rozbalenyZajezdAll = self.driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
        #     wait.until(EC.visibility_of(rozbalenyZajezd))
        #     if rozbalenyZajezd.is_displayed():
        #         for WebElement in rozbalenyZajezdAll:
        #             jdouvidet = WebElement.is_displayed()
        #             assert jdouvidet == True
        #             if jdouvidet == True:
        #                 pass
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu v last minute " + url
        #     sendEmail(msg)
        LM_FM_vypis_rozbalit_zajezd_check(self, self.driver)

      #  assert rozbalenyZajezd.is_displayed() == True

        self.test_passed = True


