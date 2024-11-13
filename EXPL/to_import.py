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
 # self.driver = webdriver.Chrome(ChromeDriverManager().install())

  self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

  self.test_passed = False


URL_local = "https://eximpl.web13.dtweb.cz/"
#URL = "https://eximpl.stg.dtweb.cz/"
URL = "http://eximpl.web13.dtweb.cz/"
URL_pobocky = "punkty-sprzedazy"
URL_detail = "/kierunki/egipt/hurghada/safaga/sentido-caribbean-world-soma-bay?AC1=2&D=64419|64420|64425&DD=2025-06-03&DI=GT06-AI&DP=298&DPR=EXIM+TOURS+POLAND&DS=1024&GIATA=79878&HID=161716&IC1=0&IFM=0&ILM=0&KC1=0&KEY=MTQ2NDEzM3wxNDYzNTU4ODc4fDgxOTE2Nw%3D%3D&MNN=7&MT=5&NN=7&PID=405138&RD=2025-06-10&RT=0&acm1=2&df=2025-06-01|2025-07-31&nnm=6|7|8|9|10|11|12|13|14&ptm=0&sortby=Departure&tom=298&tt=1&ttm=1#/prehled"
URL_leto = "lato"
URL_zima = "zima"
URL_faq = "faq"
URL_lm = "last-minute"
URL_egzotyka = "egzotyka"
URL_allInclusive = "all-inclusive"
URL_stat = "kierunki/egipt"
URL_groupsearch = "wyszukanie?dd=2024-06-24&nn=7|8|9|10|11|12|13&rd=2024-09-01&tt=1"
URL_FT_results = "wyniki-wyszukiwania?q="
URL_SRL= "/wyszukanie?ac1=2&d=64419|64420|64425&dd=2025-06-01&nn=6|7|8|9|10|11|12|13|14&rd=2025-07-31&tt=1"
URL_vlastniDoprava = "dojazd-wlasny"




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

def acceptLetak(driver):
  time.sleep(5)
  # driver.switch_to.frame(1)
  iframe = driver.find_element_by_class("bhr-ip__b")
  driver.switch_to.frame(iframe)
  driver.find_element(By.XPATH, "//a[@class='bhr-ip__c__a']").click()
  driver.switch_to.default_content()


def closeExponeaBanner(driver):
    pass


