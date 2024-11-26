from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from definitions import EDGE_DRIVER_PATH

URL = "https://kartagohu.stg.dtweb.cz/"
URL_local = "https://kartagohu.stg.dtweb.cz/"
URL_pobocky = "irodaink"
URL_detail = "/egyiptom/hurghada/makadi-bay/prima-life-makadi-resort-and-spa?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2024-10-02&DI=AE&DP=489&DPR=KARTAGO-HU-ATCOM&DS=65536&GIATA=77592&HID=9193&IC1=1&IFC=45774792%2F207929&IFM=0&ILM=0&KA1=11&KC1=1&MNN=7&MT=5&NN=7&OFC=45774461%2F207928&PC=10525827%2F2%2F1736%2F7&PID=HRG20068&RC=DR01&RD=2024-10-09&TO=489|4371&acm1=2&df=2024-10-01|2024-10-31&icm1=0&kam1=11&kcm1=1&nnm=7|8|9|10&ptm=0&tt=1&ttm=1#/prehled"
URL_SRL = "/keresesi-eredmenyek?ac1=2&d=64419|64420|64421|64422|64423|64424|64425|64426&dd=2024-10-01&ic1=1&ka1=11&kc1=1&nn=7|8|9|10&rd=2024-10-31&to=489|4371&tt=1"
URL_covidInfo = "covid-info"
URL_FM = "first-minute"
URL_faq = "faq"
URL_lm = "last-minute"
URL_stat = "egyiptom"
URL_groupsearch = "keresesi-eredmenyek?tt=1&to=489&dd=2022-09-01&rd=2022-10-31"
URL_FT_results = "hledani-vysledky?q="


import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
brand_name_project = "KARTAGOSK"
from desired_cap_generator import desired_cap_Branded
desired_cap2 = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized Suite For Web Monitoring",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}

import logging
import sys
import os
def setUp(self):
  # self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
  service = Service(EDGE_DRIVER_PATH)
  self.driver = webdriver.Edge(service=service)
  # Dynamically get the folder name (assuming folder is two levels up from the test file)
  test_folder = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

  # Get the current test method name (used in unique logger and log file naming)
  test_method = self._testMethodName
  if self.run_number is None:
    self.run_number = 0
  # Generate a unique logger name using folder, class name, run number, and test method
  logger_name = f'{test_folder}_{self.__class__.__name__}_{test_method}_{self.run_number:04d}'

  # Get the logger (will create a new one if it doesn't exist)
  self.logger = logging.getLogger(logger_name)

  # Remove any existing handlers to avoid log mixing
  if self.logger.hasHandlers():
    self.logger.handlers.clear()

  # Set log level
  self.logger.setLevel(logging.INFO)

  # Create a unique log file for this specific test
  log_filename = f'{test_folder}_{self.__class__.__name__}_{test_method}_test_{self.run_number:04d}.log'

  # Create file handler for logging to file
  file_handler = logging.FileHandler(log_filename, mode='w')
  file_handler.setLevel(logging.INFO)

  # Create stream handler for console output
  stream_handler = logging.StreamHandler(sys.stdout)
  stream_handler.setLevel(logging.INFO)

  # Create a simple log format
  formatter = logging.Formatter('%(levelname)s - %(message)s')
  file_handler.setFormatter(formatter)
  stream_handler.setFormatter(formatter)

  # Add handlers to the logger
  self.logger.addHandler(file_handler)
  self.logger.addHandler(stream_handler)

  # Ensure logs are flushed to the file immediately
  file_handler.flush()

  self.test_passed = False


def tearDown(self):
  self.logger.info(self.driver.current_url)
  self.driver.quit()
  if not self.test_passed:
    self.driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

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

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)
def acceptConsent(driver):

  generalDriverWaitImplicit(driver)
  time.sleep(3)
  try:
    generalDriverWaitImplicit(driver)
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
  #  self.logger.info("consent pass")
    pass


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
      exponeaBanner = driver.find_element(By.XPATH, "//*[@class='exponea-popup-banner']")
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

