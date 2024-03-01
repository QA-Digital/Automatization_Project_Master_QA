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
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False


URL = "https://etravel.web1.dtweb.cz/"
#URL = "https://etravel.stg.dtweb.cz/"
#URL = "https://www.etravel.cz/"
URL_pobocky = URL +"/kontakty/nase-pobocky"
URL_detail = URL + "/egypt/hurghada/hurghada/mirage-bay-resort-a-aqua-park-hurghada?DS=8192&GIATA=16351&D=64419|64420|64425|64422|64423&HID=5057&MT=5&RC=DR01&NN=7&DF=2024-08-01|2024-09-30&RD=2024-09-10&DD=2024-09-03&ERM=0&AC1=2&KC1=0&IC1=0&DP=4312&TO=4312|4305|2682|4308|4309&TOM=4312|4305|2682|4308|4309&MNN=7&NNM=7|8|9|10|11|12|13|14&TT=1&TTM=1&PID=HRG90015&DPR=EXIM%20TOURS%20ATCOM&ILM=0&IFM=0"
URL_faq = URL + "/dulezite-informace"
URL_FT_results = URL +"/hledani-vysledky?q="
URL_LM = URL + "/last-minute"
URL_stat = URL + "/egypt"
URL_SRL = URL +"/vysledky-vyhledavani?ac1=2&d=64419|64420|64425|64422|64423&dd=2024-08-01&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4309&tt=1"
URL_FM = URL + "/first-minute"
URL_groupsearch = URL + "/vysledky-vyhledavani?ac1=2&dd=2024-08-01&nn=7|8|9|10|11|12|13|14&rd=2024-09-29&to=4312|4305|2682|4308|4309&tt=1"


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


