from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail,URL_leto, URL_zima, URL_egzotyka, URL_allInclusive, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestDisplayed(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)

    def test_letoDestination_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_leto)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationLeto = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationLeto)
            destinationLetoAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationLeto))
            if destinationLeto.is_displayed():
                for WebElement in destinationLetoAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Leto, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Leto, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationLeto.is_displayed() == True

    def test_zimaDestination_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_zima)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationZima = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationZima)
            destinationZimaAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationZima))
            if destinationZima.is_displayed():
                for WebElement in destinationZimaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Zima, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Zima, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationZima.is_displayed() == True

    def test_egzotykaDestination_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_egzotyka)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationEgzotyka = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationEgzotyka)
            destinationEgzotykaAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationEgzotyka))
            if destinationEgzotyka.is_displayed():
                for WebElement in destinationEgzotykaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Egzotyka, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Egzotyka, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationEgzotyka.is_displayed() == True

    def test_allInclusiveDestination_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_allInclusive)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationAllIn = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationAllIn)
            destinationAllInAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationAllIn))
            if destinationAllIn.is_displayed():
                for WebElement in destinationAllInAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem All Inclusive, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem All Inclusive, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationAllIn.is_displayed() == True