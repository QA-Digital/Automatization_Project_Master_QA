from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, sendEmail, URL_SRL, setUp, tearDown
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from email.mime.text import MIMEText
import smtplib


SRLhotelyKartyXpath= "//*[@class='f_searchResult-content-item relative']"
SRLfotkyKartyXpath = "//*[@class='f_searchResult-content'and not(@style='display: none;')]//*[@class='f_tileGallery']"
SRLcenaKartyXpath = "//*[@class='f_price']"
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://fischer.cz"

def sendEmailv2(msg, recipient):
  fromx = 'alertserverproblem@gmail.com'
  to = recipient
  msg = MIMEText(msg)
  msg['Subject'] = "HP CHECK"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

filip="Filip.RYTYCH@dertouristik.cz"
ondraOsobniMail = "ooo.kadoun@gmail.com"

def SRL_D(driver):
    wait = WebDriverWait(driver, 15)
    driver.implicitly_wait(100)
    hotelySingle = driver.find_element_by_xpath(SRLhotelyKartyXpath)
    try:
        hotelySingle = driver.find_element_by_xpath(SRLhotelyKartyXpath)
        hotelyAll = driver.find_elements_by_xpath(SRLhotelyKartyXpath)
        wait.until(EC.visibility_of(hotelySingle))
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " + url
                    sendEmail(msg, filip)
                    sendEmail(msg, ondraOsobniMail)
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg, filip)
        sendEmail(msg, ondraOsobniMail)

    assert hotelySingle.is_displayed() == True

    try:
        driver.implicitly_wait(15)
        fotkyAll = driver.find_elements_by_xpath(SRLfotkyKartyXpath)
        fotkaSingle = driver.find_element_by_xpath(SRLfotkyKartyXpath)
        wait.until(EC.visibility_of(fotkaSingle))
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg, filip)
                    sendEmail(msg, ondraOsobniMail)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg, filip)
        sendEmail(msg, ondraOsobniMail)

    try:
        driver.implicitly_wait(100)
        cenaAll = driver.find_elements_by_xpath(SRLcenaKartyXpath)
        cenaSingle = driver.find_element_by_xpath(SRLcenaKartyXpath)
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    print("ceny")
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s cenami hotelu v searchi " + url
                    sendEmail(msg, filip)
                    sendEmail(msg, ondraOsobniMail)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg, filip)
        sendEmail(msg, ondraOsobniMail)

    assert cenaAll[0].is_displayed() == True

    verticalFilterXpath = "//*[@class='f_additionalFilter']"
    try:
        driver.implicitly_wait(100)
        verticalFilterElement = driver.find_element_by_xpath(verticalFilterXpath)
        wait.until(EC.visibility_of(verticalFilterElement))
        assert verticalFilterElement.is_displayed() == True

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg, filip)
        sendEmail(msg, ondraOsobniMail)

    try:
        loadingImgSingle = driver.find_element_by_xpath(
            "//*[@class='splide__spinner']")  ##loading classa obrazku, jestli tam je = not gud
        if loadingImgSingle.is_displayed():
            url = driver.current_url
            msg = " Problem s načítáná fotek v SRL  //*[@class='splide__spinner']" + url
            sendEmail(msg, filip)
            sendEmail(msg, ondraOsobniMail)
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

tourTableXpath = "//*[@class='f_tourTable-tour-item f_tourTable-tour-item--date']"

driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)
tourTablesElement = driver.find_element_by_xpath(tourTableXpath)

driver.execute_script("arguments[0].scrollIntoView(true);", tourTablesElement)
#tourTablesElement.click()
driver.execute_script("arguments[0].click();", tourTablesElement)
SRL_D(driver)

