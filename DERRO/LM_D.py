from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO.to_import import acceptConsent, sendEmail,URL_lm, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

from DERRO.to_import import URL_local
class TestLM_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None, run_number=None):
        self.run_number = run_number
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_lM_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        URL_lm_lp = f"{self.URL}{URL_lm}"
        self.driver.get(URL_lm_lp)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationLM = self.driver.find_element(By.XPATH, "(//*[@class='f_teaser f_teaser--hp'])[1]")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationLM)
            time.sleep(3)
            destinationLMall = self.driver.find_elements(By.XPATH, "(//*[@class='f_teaser f_teaser--hp'])[1]")
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



