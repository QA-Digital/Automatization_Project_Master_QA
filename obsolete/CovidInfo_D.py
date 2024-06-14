from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, closeExponeaBanner, URL_covidInfo, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestCovidInfo_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_covidInfo_D(self):
        wait = WebDriverWait(self.driver, 150000)
        self.driver.get(URL_covidInfo)
        time.sleep(1)
        acceptConsent(self.driver)
        time.sleep(1)
        closeExponeaBanner(self.driver)

        wholeGridsAll = self.driver.find_elements_by_xpath("//*[@class='flex justify-between shadow-lg box-border text-sm bg-white p-4 flex-col']")
        wholeGridsSingle = self.driver.find_element_by_xpath("//*[@class='flex justify-between shadow-lg box-border text-sm bg-white p-4 flex-col']")
        try:
            wait.until(EC.visibility_of(wholeGridsSingle))
            for WebElement in wholeGridsAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                    print("gridy jdou videt")
                else:
                    url = self.driver.current_url
                    msg = " Problem s gridy cocid info wholeGridsAll " + url
                    sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s gridy covid info wholeGridsAll " + url
            sendEmail(msg)

        contentItemsAll = self.driver.find_elements_by_xpath("//*[@class='mt-3 mb-4 -mx-4 h-full']")
        contentItemsSingle = self.driver.find_element_by_xpath("//*[@class='mt-3 mb-4 -mx-4 h-full']")

        try:
            wait.until(EC.visibility_of(contentItemsSingle))
            for WebElement in contentItemsAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                    print("content jdou videt")
                else:
                    url = self.driver.current_url
                    msg = " Problem s content vocid info " + url
                    sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s content covid info contentItemsAll " + url
            sendEmail(msg)

        self.test_passed = True