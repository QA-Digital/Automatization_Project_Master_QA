from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent,URL_detail, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest


##there is new SRL rn so gotta prepare that, for now I created this test just for the detail of hotel it self, hard url

def detail_D(self, driver):
    wait = WebDriverWait(self.driver, 12)
    driver.implicitly_wait(10)
    detailWrapperXpath = "//*[@class='grd-row']"
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


def detail_D2(self, driver):
    wait = WebDriverWait(self.driver, 150000)
    driver.implicitly_wait(100)
    try:
        detailFotka = self.driver.find_element_by_xpath("//*[@id='gallery01Trigger']")
        # detailFotka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-content grd-col grd-col--9 grd-col--lg-8 grd-col--slg-12']")
        # detailFotka = self.driver.find_element_by_xpath("//*[@id='divHotelDetailWrapper']")

        wait.until(EC.visibility_of(detailFotka))
        print(detailFotka.is_displayed)

        if detailFotka.is_displayed():
            pass
    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s fotkami na detailu hotelu " + url
        sendEmail(msg)
    # detailFotka = self.driver.find_element_by_xpath("//*[@id='gallery01Trigger']")

    assert detailFotka.is_displayed() == True

    try:
        sedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
        wait.until(EC.visibility_of(sedivka))
        if sedivka.is_displayed():
            pass


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)

    try:
        terminyCeny = self.driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
        wait.until(EC.visibility_of(terminyCeny))
        self.driver.execute_script("arguments[0].click();", terminyCeny)
        try:
            potvrdit = self.driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
            self.driver.execute_script("arguments[0].click();", potvrdit)

        except NoSuchElementException:
            pass


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem prepnuti na terminy a ceny na detailu hotelu " + url
        sendEmail(msg)

    try:
        terminySingle = self.driver.find_element_by_xpath("//*[@data-hotel]")
        wait.until(EC.visibility_of(terminySingle))

        if terminySingle.is_displayed():
            pass
        else:
            url = self.driver.current_url
            msg = "Problem s terminy a ceny na detailu hotelu " + url
            sendEmail(msg)


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s terminy a ceny na detailu hotelu " + url
        sendEmail(msg)

    assert terminySingle.is_displayed() == True

from FWSK.to_import import URL_local
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
        time.sleep(2.5)
        acceptConsent(self.driver)
        detail_D(self, self.driver)

        self.test_passed = True