import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

def groupSearch_D(self, driver):
    wait = WebDriverWait(self.driver, 200)
    generalDriverWaitImplicit(driver)
    wait.until(EC.visibility_of(driver.find_element_by_xpath("(//div[@class= 'f_teaser f_teaser--grid'])[1]")))
    teaserItems = driver.find_elements_by_xpath("(//div[@class= 'f_teaser f_teaser--grid'])[1]")
    try:
        for WebElement in teaserItems:
            jdouvidet = WebElement.is_displayed()
            if jdouvidet == True:
                pass
            else:
                pass

    except NoSuchElementException:
        pass

    assert teaserItems[0].is_displayed() == True
    driver.implicitly_wait(100)
    time.sleep(3)

    srlItems = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]")
    try:
        for WebElement in srlItems:
            jdouvidet = WebElement.is_displayed()
            if jdouvidet == True:
                pass
            else:
                pass

    except NoSuchElementException:
        pass
        print("no such")

    assert srlItems[0].is_displayed() == True


class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(URL_groupsearch)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(2.5)
        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True