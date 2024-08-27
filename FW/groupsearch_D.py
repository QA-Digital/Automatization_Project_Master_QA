from FW.to_import import print_lock
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, URL_groupsearch, setUp, tearDown,generalDriverWaitImplicit
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
                with print_lock:
                    with print_lock:
                        print_lock.acquire()
                        try:
                            print_lock.acquire()
                            try:
                                print("Else")
                                time.sleep(0.1)
                            finally:
                                print_lock.release()
                            time.sleep(0.1)
                        finally:
                            print_lock.release()
    except NoSuchElementException:
        pass
        with print_lock:
            with print_lock:
                print_lock.acquire()
                try:
                    print_lock.acquire()
                    try:
                        print("no such")
                        time.sleep(0.1)
                    finally:
                        print_lock.release()
                    time.sleep(0.1)
                finally:
                    print_lock.release()
    assert srlItems[0].is_displayed() == True


from FW.to_import import URL_local

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
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True