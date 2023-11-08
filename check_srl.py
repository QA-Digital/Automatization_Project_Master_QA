from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL_SRL, setUp, tearDown
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
SRLhotelyKartyXpath= "//*[@class='f_searchResult-content-item relative']"
SRLfotkyKartyXpath = "//*[@class='f_searchResult-content'and not(@style='display: none;')]//*[@class='f_tileGallery']"
SRLcenaKartyXpath = "//*[@class='f_price']"
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://fischer.cz"
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

    try:
        self.driver.implicitly_wait(15)
        fotkyAll = self.driver.find_elements_by_xpath(SRLfotkyKartyXpath)  ##
        fotkaSingle = self.driver.find_element_by_xpath(SRLfotkyKartyXpath)
        wait.until(EC.visibility_of(fotkaSingle))
        ##print(fotkaSingle)
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                else:
                    url = self.driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = self.driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg)



    try:
        self.driver.implicitly_wait(100)
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
def acceptConsent(driver):

  time.sleep(3)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    # print(element)
  except NoSuchElementException:
    # print("NOSUCH")
    pass

  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    # print("consent pass")
    pass

tourTableXpath = "//*[@class='f_tourTable-tour']"

driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)
driver.find_element_by_xpath(tourTableXpath).click()
SRL_D(driver)

