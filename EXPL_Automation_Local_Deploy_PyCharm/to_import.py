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


brand_name_project = "EXIM"

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
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False


#URL = "https://www.exim.pl/"
#URL = "https://eximpl.stg.dtweb.cz/"
URL = "http://eximpl.web11.dtweb.cz/"
URL_pobocky = URL+"punkty-sprzedazy"
URL_detail = URL +"/egipt/hurghada/hurghada/la-rosa-waves-resort?KEY=2887754714&DS=1024&GIATA=1272734&D=64419|64420|64425&HID=149477&MT=5&RT=0&NN=4&DF=2024-01-23|2024-02-17&RD=2024-02-03&DD=2024-01-30&ERM=0&AC1=2&KC1=0&IC1=0&DP=298&MNN=4&NNM=4&TT=1&TTM=0&PID=382005&DPR=EXIM%20TOURS%20POLAND"
URL_leto = URL+"lato"
URL_zima = URL+"zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_egzotyka = URL+"egzotyka"
URL_allInclusive = URL+"all-inclusive"
URL_stat = URL+"kierunki/egipt"
URL_groupsearch = URL+"wyszukanie?ac1=2&dd=2023-12-16&nn=7%7C8%7C9%7C10%7C11%7C12%7C13&rd=2024-01-07&tt=1"
URL_FT_results = URL+"wyniki-wyszukiwania?q="
URL_SRL= URL+"wyszukanie?ac1=2&d=64419%7C64420%7C64425&dd=2024-01-15&nn=7%7C8%7C9%7C10%7C11%7C12%7C13&rd=2024-02-25&tt=1"
URL_vlastniDoprava = URL + "dojazd-wlasny"



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


