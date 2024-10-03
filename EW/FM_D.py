from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest



from EW.to_import import URL_local
class TestFM_D(unittest.TestCase):
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

    def test_FM_D(self):
        URL_FM_lp = f"{self.URL}{URL_FM}"
        self.driver.get(URL_FM_lp)
        wait = WebDriverWait(self.driver, 150)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)


        # try:
        #     self.driver.implicitly_wait(100)
        #     bannerItems = self.driver.find_elements_by_xpath("//*[@class='f_tile f_tile--simple']")
        #     wait.until(EC.visibility_of(bannerItems[0]))
        #     if bannerItems[0].is_displayed():
        #         for WebElement in bannerItems:
        #             jdouvidet = WebElement.is_displayed()
        #             assert jdouvidet == True
        #             if jdouvidet == True:
        #                 pass
        #
        #             else:
        #                 url = self.driver.current_url
        #                 msg = "Problem s FM - zajezdy se neukazuji " + url
        #                 sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem s FM - zajezdy se neukazuji " + url
        #     sendEmail(msg)
        #
        # assert bannerItems[0].is_displayed() == True

        # bannerItems[0].click()
        #time.sleep(1.5)
        # assert self.driver.current_url != URL_FM
        # self.driver.implicitly_wait(100)
        teaserItems = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")

        try:
            for WebElement in teaserItems:
                ##self.logger.info(len(teaserItems))
                jdouvidet = WebElement.is_displayed()
                ##self.logger.info(jdouvidet)
                if jdouvidet == True:
                    ##self.logger.info(jdouvidet)
                    ##self.logger.info(WebElement)
                    pass

                else:
                    pass
                    ##self.logger.info("Else")
                    ##emailfunciton

        except NoSuchElementException:
            pass
            ##self.logger.info("no such")
            ##email fnction

        assert teaserItems[0].is_displayed() == True

        self.driver.implicitly_wait(10)
        #not rly benefit items anymore but 2lazy to update var name
        benefitItemsAll = self.driver.find_elements_by_xpath(
            "//*[@class='in_teaser-wrapper']")
        benefitItemsSingle = self.driver.find_element_by_xpath(
            "//*[@class='in_teaser-wrapper']")
        try:
            wait.until(EC.visibility_of(benefitItemsSingle))
            for WebElement in benefitItemsAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                    self.logger.info("benefit items jdou videt")
                else:
                    url = self.driver.current_url
                    msg = " Problem s benefit items    benefitItemsAll " + url
                    sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s gridy covid info wholeGridsAll " + url
            sendEmail(msg)

        # self.driver.implicitly_wait(100)
        # contentItemsAll = self.driver.find_elements_by_xpath("//*[@class='mt-3 mb-4 -mx-4 h-full']")
        # contentItemsSingle = self.driver.find_element_by_xpath("//*[@class='mt-3 mb-4 -mx-4 h-full']")
        #
        # try:
        #     wait.until(EC.visibility_of(contentItemsSingle))
        #     for WebElement in contentItemsAll:
        #         jdouvidet = WebElement.is_displayed()
        #         assert jdouvidet == True
        #         if jdouvidet == True:
        #             pass
        #             self.logger.info("content jdou videt")
        #         else:
        #             url = self.driver.current_url
        #             msg = " Problem s content vocid info " + url
        #             sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem s content covid info contentItemsAll " + url
        #     sendEmail(msg)
        #
        #
        # self.driver.get(URL_FM)
        # time.sleep(1.5)
        # bannerItemsDiffLocator = self.driver.find_elements_by_xpath("//*[@class='f_tile-footer']")
        # wait.until(EC.visibility_of(bannerItemsDiffLocator[1])).click()
        #
        #
        # assert self.driver.current_url != URL_FM
        # self.driver.implicitly_wait(100)
        # teaserItems = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        #
        # try:
        #     for WebElement in teaserItems:
        #         ##self.logger.info(len(teaserItems))
        #         jdouvidet = WebElement.is_displayed()
        #         ##self.logger.info(jdouvidet)
        #         if jdouvidet == True:
        #             ##self.logger.info(jdouvidet)
        #             ##self.logger.info(WebElement)
        #             pass
        #
        #         else:
        #             pass
        #             ##self.logger.info("Else")
        #             ##emailfunciton
        #
        # except NoSuchElementException:
        #     pass
        #     ##self.logger.info("no such")
        #     ##email fnction
        #
        # assert teaserItems[0].is_displayed() == True
        #
        #
        # self.driver.implicitly_wait(100)
        ##benefit items
        # contentItemsAll = self.driver.find_elements_by_xpath("//*[@class='f_benefit-item']")
        # contentItemsSingle = self.driver.find_element_by_xpath("//*[@class='f_benefit-item']")
        #
        # try:
        #     wait.until(EC.visibility_of(contentItemsSingle))
        #     for WebElement in contentItemsAll:
        #         jdouvidet = WebElement.is_displayed()
        #         assert jdouvidet == True
        #         if jdouvidet == True:
        #             pass
        #             self.logger.info("content jdou videt")
        #         else:
        #             url = self.driver.current_url
        #             msg = " Problem s content vocid info " + url
        #             sendEmail(msg)
        #
        # except NoSuchElementException:
        #     url = self.driver.current_url
        #     msg = "Problem s content covid info contentItemsAll " + url
        #     sendEmail(msg)
        self.test_passed = True