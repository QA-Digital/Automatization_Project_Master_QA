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
def setUp(self):
  self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
  self.test_passed = False


#URL = "https://www.dertour.ro/"
#URL = "https://dertourro.stg.dtweb.cz/"
URL = "https://dertourro.stg.dtweb.cz/"
URL_local = "https://dertourro.stg.dtweb.cz/"
URL_pobocky = "agentii-dertour"
URL_detail = "egipt/hurghada/makadi-bay/prima-life-makadi-spa?DS=2048&GIATA=77592&D=64421|64422|64426|64424|64423|64419|64420|64425&HID=9193&MT=5&NN=7&DF=2024-01-31|2024-04-01&RD=2024-02-11&DD=2024-02-03&ERM=0&AC1=2&KC1=0&IC1=0&DP=2691&MNN=7&NNM=3|4|5|6|7|8|9|10|11|12|13|14|15&TT=1&TTM=1&PID=HRG20068&DPR=DER%20Touristik%20RO%20ATCOM&ILM=0&IFM=0"
URL_faq = "faq"
URL_lm = "last-minute"
URL_exotika = "exotice"
URL_allInclusive = "all-inclusive"
URL_stat = "egipt"
URL_groupsearch = "rezultatele-cautarii?ac1=2&dd=2023-11-01&nn=3|4|5|6|7|8|9|10|11|12|13|14|15&rd=2024-01-01&tt=1"
URL_FT_results = "rezultate-cautare?q="
URL_SRL = "rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2024-01-01&nn=3|4|5|6|7|8|9|10|11|12|13|14|15&rd=2024-02-29&tt=1"


def tearDown(self):
  print(self.driver.current_url)
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
    print(element)
  except NoSuchElementException:
    print("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    print("consent pass")
    pass


def closeExponeaBanner(driver):
    pass


