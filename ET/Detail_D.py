from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ET.to_import import acceptConsent, URL_detail, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest


def detail_D(self, driver):
    wait = WebDriverWait(self.driver, 12)
    driver.implicitly_wait(10)
    detailWrapperXpath = "//*[@class='grd-row']"
    try:
        detailWrapper = self.driver.find_element(By.XPATH, detailWrapperXpath)
        wait.until(EC.visibility_of(detailWrapper))
        if detailWrapper.is_displayed():
            pass

    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)
    detailWrapper = self.driver.find_element(By.XPATH, detailWrapperXpath)

    assert detailWrapper.is_displayed() == True

from ET.to_import import URL_local
class TestDetailHotelu_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_detail_D(self):
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        detail_D(self, self.driver)
        self.test_passed = True

