import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_groupsearch_leto,URL_groupsearch_zima, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

def groupSearch_D(self, driver):
    wait = WebDriverWait(self.driver, 150)
    #driver.implicitly_wait(100)
    generalDriverWaitImplicit(driver)
    groupSearchDlazdiceXpath = "//*[@class='box-border relative pt-[100%]']"
    teaserItems = driver.find_elements_by_xpath(groupSearchDlazdiceXpath)

    wait.until(EC.visibility_of(teaserItems[0]))


    try:
        for WebElement in teaserItems:
            ##print(len(teaserItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                ##print("Else")
                ##emailfunciton


    except NoSuchElementException:
        pass
        ##print("no such")
        ##email fnction

    assert teaserItems[0].is_displayed() == True

    driver.implicitly_wait(100)
    srlItems = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]")
    try:
        for WebElement in srlItems:
            ##print(len(srlItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                print("Else")



    except NoSuchElementException:
        pass
        print("no such")
    assert srlItems[0].is_displayed() == True


class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D_zima(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(URL_groupsearch_zima)
        time.sleep(10)
        acceptConsent(self.driver)
        time.sleep(13)
        self.driver.find_element_by_xpath('//span[@class="f_button-text"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True

    def test_groupsearch_D_leto(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(URL_groupsearch_leto)
        time.sleep(10)
        acceptConsent(self.driver)
        time.sleep(13)
        self.driver.find_element_by_xpath('//span[@class="f_button-text"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True