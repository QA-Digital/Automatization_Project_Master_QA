from selenium.common.exceptions import NoSuchElementException
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_stat, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

NejHotely = "//*[@class='f_tileGrid-item']"
class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SDO_D(self):
        driver = self.driver
        self.driver.get(URL_stat)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        Offer1 = self.driver.find_elements_by_xpath("(//a)[59]")[0].get_attribute('href')
        Offer2 = self.driver.find_elements_by_xpath("(//a)[60]")
        Offer3 = self.driver.find_elements_by_xpath("(//a)[61]")
        Offer4 = self.driver.find_elements_by_xpath("(//a)[62]")

        HPtopNabidkaElements = [Offer1, Offer2, Offer3, Offer4]
        print(HPtopNabidkaElements)
        time.sleep(4)
        linksToCheck_List = []
        for _ in HPtopNabidkaElements:
           odkazLink = HPtopNabidkaElements
           linksToCheck_List.append(odkazLink)
           print(odkazLink)

    def test_SDO_NejHotely(self):
        self.driver.maximize_window()
        self.driver.get(URL_stat)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        NejHotelyElement = self.driver.find_element_by_xpath(NejHotely)
        self.driver.execute_script("arguments[0].scrollIntoView();", NejHotelyElement)
        time.sleep(5)
        NejHotelyElement.click()

        try:
            NejHotelyS = self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
            NejHotelyAll = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
            if NejHotelyS.is_displayed():
                for WebElement in NejHotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        print("Hotely jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, hotely se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, hotely se nezobrazuji " + url
            sendEmail(msg)

        assert NejHotelyS.is_displayed() == True

