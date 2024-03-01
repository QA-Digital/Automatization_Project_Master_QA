from selenium.common.exceptions import NoSuchElementException
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_stat_zima, URL_stat_leto, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SDO_D_zima(self):
        driver = self.driver
        self.driver.get(URL_stat_zima)
        self.driver.maximize_window()
        time.sleep(5)
        acceptConsent(self.driver)
        time.sleep(5)

        try:
            generalDriverWaitImplicit(self.driver)
            oblastiAll = self.driver.find_elements_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
            element = self.driver.find_element_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            oblastiSingle = self.driver.find_element_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            strediskaAll = self.driver.find_elements_by_xpath("//*[@class='border border-neutral-200 flex flex-col']")
            element = self.driver.find_element_by_xpath("//*[@class='border border-neutral-200 flex flex-col']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            strediskaSingle = self.driver.find_element_by_xpath("//*[@class='border border-neutral-200 flex flex-col']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            oblHotelyAll = self.driver.find_elements_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
            element = self.driver.find_element_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            oblHotelySingle = self.driver.find_element_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            fotkyAll = self.driver.find_elements_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
            element = self.driver.find_element_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            fotkySingle = self.driver.find_element_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
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
            oblastiAll = self.driver.find_elements_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
            element = self.driver.find_element_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            oblastiSingle = self.driver.find_element_by_xpath("//*[@class='group h-[250px] block relative overflow-hidden']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            strediskaAll = self.driver.find_elements_by_xpath("//*[@class='border border-neutral-200']")
            element = self.driver.find_element_by_xpath("//*[@class='border border-neutral-200']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            strediskaSingle = self.driver.find_element_by_xpath("//*[@class='border border-neutral-200']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            oblHotelyAll = self.driver.find_elements_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
            element = self.driver.find_element_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            oblHotelySingle = self.driver.find_element_by_xpath("//*[@class='flex flex-col group no-underline p-4 w-full box-border']")
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

        time.sleep(5)
        try:
            generalDriverWaitImplicit(self.driver)
            fotkyAll = self.driver.find_elements_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
            element = self.driver.find_element_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            fotkySingle = self.driver.find_element_by_xpath("//*[@class='splide is-overflow splide--grid splide--loop splide--ltr splide--draggable is-active is-initialized']")
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
