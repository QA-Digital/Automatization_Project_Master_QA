import logging
import sys

from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

brand_name_project = "FISCHER"
desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized - Web Monitor V2",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import os

def setUp(self):
    chrome_driver_path = 'C:/Users/KADOUN/Desktop/Python_utils/chromedriver.exe'
    self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Dynamically get the folder name (assuming folder is two levels up from the test file)
    test_folder = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

    # Set up logging for each test, including the folder name in the log file
    log_filename = f'{test_folder}_{self.__class__.__name__}_test.log'
    self.logger = logging.getLogger(self.__class__.__name__)
    self.logger.setLevel(logging.INFO)

    # Create file handler for the specific folder and test class
    file_handler = logging.FileHandler(log_filename, mode='w')
    file_handler.setLevel(logging.INFO)

    # Create stream handler to capture logs in the console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    # Create formatters and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to the logger
    self.logger.addHandler(file_handler)
    self.logger.addHandler(stream_handler)

    # Ensure logs are flushed to the file immediately
    file_handler.flush()

    self.test_passed = False


  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  #self.driver = webdriver.Chrome(ChromeDriverManager().install())
  #self. driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  #options = webdriver.ChromeOptions()
  #options.add_argument("--headless")



  #self.driver = webdriver.Chrome(ChromeDriverManager().install())







  #self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

  #self.driver = webdriver.Edge(EdgeDriverManager().install())
  # https://googlechromelabs.github.io/chrome-for-testing/#stable








  # chrome_version = "118.0.5993"  # Replace this with your Chrome version
  #self.driver = webdriver.Chrome(ChromeDriverManager(version=chrome_version).install())

 # chrome_options = webdriver.ChromeOptions()
 # chrome_options.add_argument('--headless')
  #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
 #
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())



#URL = "https://www.fischer.cz/"
#URL = "https://fischer.web1.dtweb.cz/"

#URL_local = "https://fischer.stg.dtweb.cz/"
URL_local = "https://fischer.stg.dtweb.cz/"
URL = "https://www.fischer.cz/"



#URL = "https://fischer.stg.dtweb.cz/"

URL_poznavacky = "poznavaci-zajezdy/okruzni-a-kombinovane"
URL_poznavacky_vikendy = "poznavaci-zajezdy/prodlouzene-vikendy"
URL_poznavacky_rodiny = "poznavaci-zajezdy/pro-rodiny"
URL_poznavacky_zazitky = "poznavaci-zajezdy/zazitkove"
URL_pobocky = "kontakty/seznam-pobocek"
URL_detail = "/hotely/spanelsko/andalusie-costa-del-sol/benalmadena/globales-gardenia?AC1=2&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&DD=2024-10-19&DI=AI&DP=4312&DPR=Hotelbeds&DS=2&GIATA=37867&HID=162&IC1=1&IFM=0&ILM=0&KC1=0&MMT=5&MNN=7&MT=5&NN=7&PID=4195&RC=DBT-BL&RCS=DBT-BL&RD=2024-10-27&RT=15&TO=4312&acm1=2&df=2024-10-07|2024-10-31&icm1=1&nnm=7|8|9|10|11|12|13|14&ptm=0&sortby=Departure&tt=1&ttm=1#/prehled"
URL_SRL = "/vysledky-vyhledavani?ac1=2&d=622|1086|590|726|670|680|621|669|1009|1010|1108|611|610|609|953|612&dd=2024-06-11&ic1=1&nn=7|8|9|10|11|12|13|14&rd=2024-07-31&to=4312|4305|2682|4308&tt=1"
URL_covidInfo = "covid-info"
URL_kluby = "/kluby/funtazie-leto"
URL_fmExotika = "first-minute/exotika-zima"
URL_faq = "faq"
URL_lm = "last-minute"
URL_stat = "spanelsko"
URL_groupsearch = "vysledky-vyhledavani?ac1=2&dd=2023-02-01&nn=7|8|9|10|11|12|13&rd=2023-02-26&to=4312|4305|2682|4308&tt=1"
URL_FT_results = "hledani-vysledky?q="
URL_darkove_poukazy = "/poukazy-benefity/darkove-poukazy"

import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from selenium import webdriver
from to_import_secret_master import emailPass, comandExecutor

from webdriver_manager.chrome import ChromeDriverManager

def tearDown(self):
  self.logger.info(self.driver.current_url)
  self.driver.quit()
  #if not self.test_passed:self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)
def acceptConsent(driver):

  generalDriverWaitImplicit(driver)
  time.sleep(3)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    # self.logger.info(element)
  except NoSuchElementException:
    # self.logger.info("NOSUCH")
    pass

  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    # self.logger.info("consent pass")
    pass

#'ondrej.kadoun@fischer.cz'
def sendEmail(msg):
  fromx = 'alertserverproblem@gmail.com'
  to = 'ooo.kadoun@gmail.com'
  msg = MIMEText(msg)
  msg['Subject'] = "SRWEB1"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

def acceptConsent5(driver):
  time.sleep(2)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  except NoSuchElementException:
    return

  except TimeoutException:
    pass
  try:
    element.click()
  except TimeoutException:
    pass
  except NoSuchElementException:
    return

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
      if exponeaBanner.is_displayed():
        wait.until(EC.visibility_of(exponeaBanner))
        exponeaCrossAndBanner = driver.find_element_by_xpath(
          "//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
        exponeaCrossAndBanner.click()
        time.sleep(2)

    except NoSuchElementException:
      pass
     # self.logger.info("nenasle se exponea banner")

def acceptConsent3(driver):
  time.sleep(2)

  element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  if element !=0:

      pass

  else:
      element.click()

