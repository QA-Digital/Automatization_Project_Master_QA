from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,URL_detail, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest


##there is new SRL rn so gotta prepare that, for now I created this test just for the detail of hotel it self, hard url
def detail_D(self, driver):
    wait = WebDriverWait(self.driver, 12)
    driver.implicitly_wait(10)
    detailWrapperXpath = "//div[contains(@class,'grayBox')]"
    try:
        detailWrapper = self.driver.find_element_by_xpath(detailWrapperXpath)
        wait.until(EC.visibility_of(detailWrapper))
        if detailWrapper.is_displayed():
            pass


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)
    detailWrapper = self.driver.find_element_by_xpath(detailWrapperXpath)
    assert detailWrapper.is_displayed() == True
class TestDetailHotelu_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_detail_D(self):
        self.driver.get(URL_detail)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        detail_D(self, self.driver)
        self.test_passed = True