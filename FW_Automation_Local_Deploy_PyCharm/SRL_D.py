from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_SRL, setUp, tearDown
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
SRLhotelyKartyXpath= "//*[@class='f_searchResult-content-item relative']"
#SRLfotkyKartyXpath = "//*[@class='f_searchResult-content'and not(@style='display: none;')]//*[@class='f_tileGallery']"
SRLfotkyKartyXpath ="//swiper-slide[@aria-label='1 / 24']"
SRLcenaKartyXpath = "//*[@class='f_price']"


def SRL_D(self, driver):
    wait = WebDriverWait(self.driver, 15)
    driver.implicitly_wait(100)
    hotelySingle = self.driver.find_element_by_xpath(SRLhotelyKartyXpath)
    try:
        hotelySingle = self.driver.find_element_by_xpath(SRLhotelyKartyXpath)  ##
        hotelyAll = self.driver.find_elements_by_xpath(SRLhotelyKartyXpath)
        wait.until(EC.visibility_of(hotelySingle))
        ##print(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " + url
                    sendEmail(msg)
    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)

    assert hotelySingle.is_displayed() == True

    # try:
    #     self.driver.implicitly_wait(15)
    #     fotkyAll = self.driver.find_elements_by_xpath(SRLfotkyKartyXpath)  ##
    #     fotkaSingle = self.driver.find_element_by_xpath(SRLfotkyKartyXpath)
    #     wait.until(EC.visibility_of(fotkaSingle))
    #     ##print(fotkaSingle)
    #     if fotkaSingle.is_displayed():
    #         for WebElement in fotkyAll:
    #             jdouvidet = WebElement.is_displayed()
    #             print(jdouvidet)
    #             assert jdouvidet == True
    #             if jdouvidet == True:
    #                 pass
    #             else:
    #                 url = self.driver.current_url
    #                 msg = " Problem s fotkami hotelu v searchi " + url
    #                 sendEmail(msg)
    #
    # except NoSuchElementException:
    #     url = self.driver.current_url
    #     msg = " Problem s fotkami hotelu v searchi " + url
    #     sendEmail(msg)



    try:
        self.driver.implicitly_wait(10)
        cenaAll = self.driver.find_elements_by_xpath(SRLcenaKartyXpath)  ##
        cenaSingle = self.driver.find_element_by_xpath(SRLcenaKartyXpath)
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    print("ceny")
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s cenami hotelu v searchi " + url
                    sendEmail(msg)


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)

    assert cenaAll[0].is_displayed() == True

    verticalFilterXpath = "//*[@class='f_additionalFilter']"
    try:
        self.driver.implicitly_wait(100)
        verticalFilterElement = self.driver.find_element_by_xpath(verticalFilterXpath)
        wait.until(EC.visibility_of(verticalFilterElement))
        assert verticalFilterElement.is_displayed() == True



    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)

    try:
        loadingImgSingle = self.driver.find_element_by_xpath(
            "//*[@class='splide__spinner']")  ##loading classa obrazku, jestli tam je = not gud
        if loadingImgSingle.is_displayed():
            url = self.driver.current_url
            msg = " Problem s načítáná fotek v SRL  //*[@class='splide__spinner']" + url
            sendEmail(msg)
            assert 1 == 2
    except NoSuchElementException:
        pass

class TestSRL_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SRL_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        time.sleep(0.4)
        acceptConsent(self.driver)
        SRL_D(self, self.driver)
        self.test_passed = True
