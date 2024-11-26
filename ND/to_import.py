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


brand_name_project = "NevDama"

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

from selenium.webdriver.edge.service import Service
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






#URL = "https://nev-dama.web13.dtweb.cz/"
URL = "https://nev-dama.stg.dtweb.cz/"
URL_local = "https://new.nev-dama.cz/"
URL_pobocky = "/pobocky"
URL_detail = "zima/rakousko/tyrolsko/silvretta-arena-ischgl-samnaun/appartementhaus-fliana?KEY=12432&DS=8&D=85383|85385|85394|85407|85413|108815|85434|85436&HID=4336&MT=-1&MMT=5|3|2|1|6&NN=6&DF=2024-03-15|2024-05-15&RD=2024-04-07&DD=2024-04-01&ERM=0&AC1=2&KC1=0&IC1=0&DP=4333&MNN=6&NNM=6|7|8&TT=3&TTM=3&PID=4336&DPR=NevDama&ILM=0&IFM=0"
URL_faq = "/faq"
URL_FT_results = "/hledani-vysledky?q="
URL_LM = "/last-minute"
URL_stat_zima = "/rakousko"


URL_zima = URL + "/zima"
URL_SRL_zima = URL_zima + "/vysledky-vyhledavani?ac1=2&d=85383|85385|85394|85407|85413|108815|85434|85436&dd=2024-04-01&nn=6&rd=2024-04-30&tt=3"
URL_FM_zima =  "/first-minute"
URL_lm_zima = URL_zima + "/last-minute"
URL_stat_zima = URL_zima + "/rakousko"
URL_groupsearch_zima = URL_zima + "/vysledky-vyhledavani?ac1=2&dd=2024-02-28&nn=6|7|8&rd=2024-04-29&tt=3"


URL_leto = "leto"

URL_SRL_leto = URL_leto + "/vysledky-vyhledavani?d=108939|108938|108941|109497|108940|108942&dd=2024-08-31&nn=6|7|8&rd=2024-10-31&sortorder=1&tt=0"
URL_FM_leto ="/first-minute-leto"
URL_lm_leto = URL_leto + "/last-minute"
URL_stat_leto = URL_leto + "/chorvatsko"
URL_groupsearch_leto = URL_leto + "/vysledky-vyhledavani?ac1=2&dd=2024-08-31&nn=2|3|4|5|6|7|8|9&rd=2024-10-31&tt=0"




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
    #self.logger.info(element)
  except NoSuchElementException:
    pass
    # self.logger.info("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    pass


def closeExponeaBanner(driver):
    pass


