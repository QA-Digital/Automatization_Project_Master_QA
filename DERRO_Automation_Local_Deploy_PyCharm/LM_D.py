from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLM_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayedd(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_lm)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationLM = self.driver.find_element_by_xpath("(//*[@class='f_teaser f_teaser--hp'])[1]")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationLM)
            time.sleep(3)
            destinationLMall = self.driver.find_elements_by_xpath("(//*[@class='f_teaser f_teaser--hp'])[1]")
            wait.until(EC.visibility_of(destinationLM))
            if destinationLM.is_displayed():
                for WebElement in destinationLMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem s LM, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s LM, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationLM.is_displayed() == True



