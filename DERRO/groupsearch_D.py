from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

def groupSearch_D(self, driver):
    wait = WebDriverWait(self.driver, 200)
    generalDriverWaitImplicit(driver)
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, "(//div[@class= 'f_teaser f_teaser--grid'])[1]")))
    teaserItems = driver.find_elements(By.XPATH, "(//div[@class= 'f_teaser f_teaser--grid'])[1]")
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

    srlItems = driver.find_elements(By.XPATH, "//*[@class='f_searchResult'and not(@style='display: none;')]")
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


from DERRO.to_import import URL_local
class Test_Groupsearch_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()
        URL_groupsearch_lp = f"{self.URL}{URL_groupsearch}"
        self.driver.get(URL_groupsearch_lp)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(2.5)
        self.driver.find_element(By.XPATH, '//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True