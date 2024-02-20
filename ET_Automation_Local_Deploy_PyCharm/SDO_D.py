from selenium.common.exceptions import NoSuchElementException
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_stat_zima, URL_stat_leto, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SDO_D_zima(self):
        driver = self.driver
        self.driver.get(URL_stat_zima)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        try:
            generalDriverWaitImplicit(self.driver)
            oblastiAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 max-w-[500px] md:max-w-full mx-auto gap-4']")
            #self.driver.execute_script("arguments[0].scrollIntoView();", oblastiAll)
            oblastiSingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 max-w-[500px] md:max-w-full mx-auto gap-4']")
            if oblastiSingle.is_displayed():
                for WebElement in oblastiAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se destinace v /stat " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblasti " + url
            sendEmail(msg)
        assert oblastiAll[0].is_displayed() == True
        print("Oblasti se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            strediskaAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols-1 gap-4 md:grid-cols-2']")
            strediskaSingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols-1 gap-4 md:grid-cols-2']")
            if strediskaSingle.is_displayed():
                for WebElement in strediskaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se strediska " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se strediska " + url
            sendEmail(msg)
        assert strediskaAll[0].is_displayed() == True
        print("Strediska se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            oblHotelyAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 min-w-[320px] max-w-[500px] md:max-w-full mx-auto gap-4']")
            oblHotelySingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 min-w-[320px] max-w-[500px] md:max-w-full mx-auto gap-4']")
            if oblHotelySingle.is_displayed():
                for WebElement in strediskaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se oblibene hotely " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblibene hotely " + url
            sendEmail(msg)
        assert oblHotelyAll[0].is_displayed() == True
        print("Oblibene hotely se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            fotkyAll = self.driver.find_elements_by_xpath("//*[@class='splide__track splide__track--loop splide__track--ltr splide__track--draggable']")
            fotkySingle = self.driver.find_element_by_xpath("//*[@class='splide__track splide__track--loop splide__track--ltr splide__track--draggable']")
            if fotkySingle.is_displayed():
                for WebElement in fotkyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se fotky v galerii " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se fotky v galerii " + url
            sendEmail(msg)
        assert fotkyAll[0].is_displayed() == True
        print("Fotky v galerii se zobrazuji")

    def test_SDO_D_leto(self):
        driver = self.driver
        self.driver.get(URL_stat_leto)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(5)

        try:
            generalDriverWaitImplicit(self.driver)
            oblastiAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 max-w-[500px] md:max-w-full mx-auto gap-4']")
            #self.driver.execute_script("arguments[0].scrollIntoView();", oblastiAll)
            oblastiSingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 max-w-[500px] md:max-w-full mx-auto gap-4']")
            if oblastiSingle.is_displayed():
                for WebElement in oblastiAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se destinace v /stat " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblasti " + url
            sendEmail(msg)
        assert oblastiAll[0].is_displayed() == True
        print("Oblasti se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            strediskaAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3']")
            strediskaSingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3']")
            if strediskaSingle.is_displayed():
                for WebElement in strediskaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se strediska " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se strediska " + url
            sendEmail(msg)
        assert strediskaAll[0].is_displayed() == True
        print("Strediska se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            oblHotelyAll = self.driver.find_elements_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 min-w-[320px] max-w-[500px] md:max-w-full mx-auto gap-4']")
            oblHotelySingle = self.driver.find_element_by_xpath("//*[@class='grid grid-cols md:grid-cols-2 lg:grid-cols-3 min-w-[320px] max-w-[500px] md:max-w-full mx-auto gap-4']")
            if oblHotelySingle.is_displayed():
                for WebElement in strediskaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se oblibene hotely " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se oblibene hotely " + url
            sendEmail(msg)
        assert oblHotelyAll[0].is_displayed() == True
        print("Oblibene hotely se zobrazuji")

        try:
            generalDriverWaitImplicit(self.driver)
            fotkyAll = self.driver.find_elements_by_xpath("//*[@class='splide__track splide__track--loop splide__track--ltr splide__track--draggable']")
            fotkySingle = self.driver.find_element_by_xpath("//*[@class='splide__track splide__track--loop splide__track--ltr splide__track--draggable']")
            if fotkySingle.is_displayed():
                for WebElement in fotkyAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Nenasli se fotky v galerii " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasli se fotky v galerii " + url
            sendEmail(msg)
        assert fotkyAll[0].is_displayed() == True
        print("Fotky v galerii se zobrazuji")