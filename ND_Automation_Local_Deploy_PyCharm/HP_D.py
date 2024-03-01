from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from ND_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from selenium.webdriver.support.wait import WebDriverWait
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,sendEmail, URL, URL_LM, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

HPbanneryXpath = "//*[@class='f_teaser-item']"
HPnextArrowXpath = "//*[@class='slick-list draggable']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

class TestHP_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_homePage_D(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        bannerSingle = self.driver.find_element_by_xpath(HPbanneryXpath)
        try:
            bannerSingle = self.driver.find_element_by_xpath(HPbanneryXpath)
            bannerAll = self.driver.find_elements_by_xpath(HPbanneryXpath)
            #wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s bannery " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s bannery " + url
            sendEmail(msg)
        assert bannerSingle.is_displayed() == True
        time.sleep(1.5)

    def test_HP_LMnabidky(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL_LM)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)

        HPnextArrowElement = self.driver.find_element_by_xpath(HPnextArrowXpath)
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
        HPnextkartaHoteluSlider = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        # HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True
