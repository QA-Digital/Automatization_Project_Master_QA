import logging
import os
import sys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from webdriver_manager.chrome import ChromeDriverManager

from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

brand_name_project = "EXIM"

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
from definitions import EDGE_DRIVER_PATH
from selenium import webdriver


def setUp(self):
  self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

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

URL = "https://exim.web12.dtweb.cz/"
#URL_local = "https://www.eximtours.cz/"
URL_local =  "https://exim.web12.dtweb.cz/"
#URL_local = "https://exim.stg.dtweb.cz/"
URL_poznavacky = "poznavaci-zajezdy"
URL_poznavacky_vikendy = "poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = "poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = "poznavaci-zajezdy#rodiny"
URL_pobocky = "kontakty/nase-pobocky"
URL_kluby = "/kluby/mango-zima"
URL_detail = "/hotely/egypt/hurghada/hurghada/minamark?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2024-10-17&DI=AI&DP=4305&DPR=OTSCKF&DS=2&GIATA=17487&HID=145043&IC1=0&IFM=0&ILM=0&KC1=0&MNN=7&MT=5&NN=7&PID=AEGHRG10SU&RC=RMCLDB0000&RCS=RMCLDB0000&RD=2024-10-24&RT=0&TO=4305&acm1=2&df=2024-10-14|2024-10-31&nnm=7|8|9|10|11|12|13|14&ptm=0&sortby=Departure&tt=1&ttm=1#/prehled"
URL_detail_old = "/egypt/hurghada/hurghada/egypt-plavba-po-nilu-s-pobytem-u-rudeho-more-4-hurghada?AC1=2&D=64419|64420|64425&DD=2025-03-08&DI=IT&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=0&HID=160534&IC1=1&IFC=64388256%2F316211&IFM=0&ILM=0&KC1=0&MNN=7&MT=7&NN=7&OFC=64387089%2F316210&PC=78913989%2F2%2F1893%2F7&PID=EGR00026&RC=DR01&RCS=DR01&RD=2025-03-15&TO=4312|4305|2682|4308|4392|4309&acm1=2&dd=2024-09-18&df=2024-09-18|2025-07-18&icm1=1&nnm=7|8|9|10|11|12|13|14&ptm=0&rd=2025-07-18&sortby=Departure&tt=1&ttm=0#/prehled"
URL_SRL = "/vysledky-vyhledavani?ac1=2&d=64419|64420|64423|64425&dd=2025-03-01&nn=7|8|9|10|11|12|13|14&rd=2025-04-30&to=4312|4305|2682|4308&tt=1"
URL_covidInfo = "covid-info"
URL_FM = "first-minute"
URL_faq = "faq"
URL_lm = "last-minute"
URL_stat = "spanelsko"
URL_groupsearch = "vysledky-vyhledavani?tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ic1=1&ac1=2"
URL_FT_results = "hledani-vysledky?q="
URL_SRL_kuba_regres = "/vysledky-vyhledavani?ac1=2&d=63888&dd=2025-03-01&nn=7|8|9|10|11|12|13|14&rd=2025-04-30&to=4312|4305|2682|4308&tt=1"
URL_darkove_poukazy =  "/informace-pro-klienty/poukazky/darkove-poukazky"


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
   # self.logger.info(element)
  except NoSuchElementException:
    pass
   # self.logger.info("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    #self.logger.info("consent pass")
    pass


def closeExponeaBanner(driver):
    pass


