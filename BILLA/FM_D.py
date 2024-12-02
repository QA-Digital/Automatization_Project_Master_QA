from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from BILLA.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, generalDriverWaitImplicit
from BILLA.Detail_D import detail_D
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from BILLA.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

HPnextArrowXpath = "//*[@id='splide02']"
HPkartaHoteluSliderXpath = "//*[@class='splide__arrows splide__arrows--ltr']"

from BILLA.to_import import URL_local
class Test_FM_karty(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)
    def test_click_detail_hotelu(self):

        self.driver.maximize_window()
        URL_FM_lp = f"{self.URL}{URL_FM}"
        self.driver.get(URL_FM_lp)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(0.3)
        acceptConsent(self.driver)

     # wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPnextArrowXpath))).click()

        self.driver.implicitly_wait(100)

        HPnextArrowElement = self.driver.find_element(By.XPATH, HPnextArrowXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPnextArrowElement)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        HPnextkartaHoteluSlider = self.driver.find_element(By.XPATH, HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element(By.XPATH, HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        #action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        #self.driver.implicitly_wait(100)
        HPkartaHoteluSliderElement.click()
        #time.sleep(1)
        #self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

