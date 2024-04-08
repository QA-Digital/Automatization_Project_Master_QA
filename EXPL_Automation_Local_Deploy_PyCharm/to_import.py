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
URL = "https://eximpl.stg.dtweb.cz/"
#URL = "http://eximpl.web11.dtweb.cz/"
URL_pobocky = URL+"punkty-sprzedazy"
URL_detail = URL +"kierunki/egipt/hurghada/macadi-bay/prima-life-makadi-resort?KEY=MTI3NDIzNXwxMDA3ODYzOTMzfDYyNzU1NA%3d%3d&DS=1024&GIATA=77592&D=64419|64420|64425&HID=156229&MT=5&RT=0&NN=7&DF=2024-08-01|2024-09-30&RD=2024-09-05&DD=2024-08-29&ERM=0&DP=4382&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=391633&DPR=EXIM%20TOURS%20POLAND&ILM=0&IFM=0"
URL_leto = URL+"lato"
URL_zima = URL+"zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_egzotyka = URL+"egzotyka"
URL_allInclusive = URL+"all-inclusive"
URL_stat = URL+"kierunki/egipt"
URL_groupsearch = URL+"wyszukanie?dd=2024-06-24&nn=7|8|9|10|11|12|13&rd=2024-09-01&tt=1"
URL_FT_results = URL+"wyniki-wyszukiwania?q="
URL_SRL= URL+"wyszukanie?ac1=2&d=64419|64420|64425&dd=2024-10-14&ds=0&ifm=0&ilm=0&ka1=9&kc1=1&nn=6|7|8|9|10|11|12|13|14&rd=2024-10-31&sc=residential&tt=1"
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

def acceptLetak(driver):
  time.sleep(5)
  # driver.switch_to.frame(1)
  iframe = driver.find_element_by_class("bhr-ip__b")
  driver.switch_to.frame(iframe)
  driver.find_element_by_xpath("//a[@class='bhr-ip__c__a']").click()
  driver.switch_to.default_content()


def closeExponeaBanner(driver):
    pass


