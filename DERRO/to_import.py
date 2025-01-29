from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from webdriver_manager.chrome import ChromeDriverManager

from definitions import EDGE_DRIVER_PATH
from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver


brand_name_project = "DERRO"

desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Chrome",
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

import logging
import os
import sys
def setUp(self):
  from selenium.webdriver.edge.service import Service
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


#URL = "https://www.dertour.ro/"
#URL = "https://dertourro.stg.dtweb.cz/"
URL = "https://dertourro.stg.dtweb.cz/"
URL_local = "https://dertourro.stg.dtweb.cz/"
URL_pobocky = "agentii-dertour"
URL_detail = "/vietnam/vietnamul-de-nord/hanoi/circuit-vietnam-si-cambodgia?AC1=2&D=64076|64447|64075&DD=2025-05-05&DI=IT&DP=2691&DPR=DER+Touristik+RO+ATCOM&DS=2048&GIATA=0&HID=160845&IC1=0&IFC=79178559%2F308897&IFM=0&ILM=0&KC1=0&MNN=12&MT=7&NN=12&OFC=79178350%2F308896&PC=79597983%2F2%2F1952%2F12&PID=VNR50080&RC=DR01&RCS=DR01&RD=2025-05-19&TO=2691|649|3620|3124|256|3364|3485|2642|175|4394|1443|270|3136|675|4383|264&acm1=2&dd=2024-11-20&df=2024-11-20|2025-09-20&nnm=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21&ptm=0&rd=2025-09-20&tt=1&ttm=1#/terms"
URL_detail_new = "/egipt/hurghada/hurghada/steigenberger-al-dau-beach?DS=2048&GIATA=76358&D=64423%7C64420%7C64426%7C64421%7C64424%7C64419%7C64425%7C64422&HID=4983&MT=5&DI=AI&RC=SU01&RCS=SU01&NN=7&DF=2025-10-01%7C2025-10-31&RD=2025-10-11&DD=2025-10-04&ERM=0&AC1=2&KC1=0&IC1=0&DP=2691&TO=2691&TOM=2691&MNN=3%7C4%7C5%7C6%7C7%7C8%7C9%7C10%7C11%7C12%7C13%7C14%7C15&NNM=3%7C4%7C5%7C6%7C7%7C8%7C9%7C10%7C11%7C12%7C13%7C14%7C15&TT=1&TTM=1&PID=HRG01123&DPR=DER+Touristik+RO+ATCOM&ILM=0&IFM=0&PC=31686145%2F2%2F2103%2F7&IFC=87817247%2F334474&OFC=87817225%2F334473"
URL_faq = "faq"
URL_lm = "last-minute"
URL_exotika = "exotice"
URL_allInclusive = "all-inclusive"
URL_stat = "egipt"
URL_groupsearch = "rezultatele-cautarii?ac1=2&dd=2023-11-01&nn=3|4|5|6|7|8|9|10|11|12|13|14|15&rd=2024-01-01&tt=1"
URL_FT_results = "rezultate-cautare?q="
URL_SRL = "rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2024-01-01&nn=3|4|5|6|7|8|9|10|11|12|13|14|15&rd=2024-02-29&tt=1"


def tearDown(self):
  self.logger.info(self.driver.current_url)
  self.driver.quit()
  #if not self.test_passed:self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

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
  try:
    generalDriverWaitImplicit(driver)
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")

  except NoSuchElementException:
    pass
  #  self.logger.info("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
   # self.logger.info("consent pass")
    pass


def closeExponeaBanner(driver):
    pass


