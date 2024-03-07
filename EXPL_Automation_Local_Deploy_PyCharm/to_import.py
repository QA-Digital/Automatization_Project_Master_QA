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
URL_detail = URL +"/kierunki/egipt/marsa-alam/marsa-alam/jaz-amara?AC1=2&D=64419|64420|64425&DD=2024-10-19&DP=3850&DPR=EXIM+TOURS+POLAND&DS=1024&GIATA=1376500&HID=152967&IC1=0&IFM=0&ILM=0&KA1=9&KC1=1&KEY=MTIyMDMzNnw4NjgxMTgzNjF8NjI3ODIx&MNN=7&MT=5&NN=7&PID=386344&RD=2024-10-26&RT=0&TO=3850&acm1=2&df=2024-10-14|2024-10-31&icm1=0&kam1=9&kcm1=1&nnm=6|7|8|9|10|11|12|13|14&ptm=0&sortby=Departure&tt=1&ttm=1#/prehled"
URL_leto = URL+"lato"
URL_zima = URL+"zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_egzotyka = URL+"egzotyka"
URL_allInclusive = URL+"all-inclusive"
URL_stat = URL+"kierunki/egipt"
URL_groupsearch = URL+"wyszukanie?ac1=2&dd=2023-12-16&nn=7%7C8%7C9%7C10%7C11%7C12%7C13&rd=2024-01-07&tt=1"
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


