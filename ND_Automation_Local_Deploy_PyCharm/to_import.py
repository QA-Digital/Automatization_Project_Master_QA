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


#URL = "https://www.eximtours.cz/"
#URL = "https://nev-dama.web11.dtweb.cz/"
URL = "https://nev-dama.uat.dtweb.cz"
URL_pobocky = URL +"/kontakty/seznam-pobocek"
URL_detail = URL + "/zima/rakousko/korutany/gerlitzen/gasthof-zur-post?KEY=29849&DS=8&D=85383|85385|85394|85407|85413|108815|85434|85436&HID=3514&MT=-1&NN=4&DF=2024-02-01|2024-02-29&RD=2024-02-29&DD=2024-02-25&ERM=0&AC1=2&KC1=0&IC1=0&DP=4333&MNN=4&NNM=4&TT=3&TTM=3&PID=3514&DPR=NevDama&ILM=0&IFM=0"
URL_faq = URL +"/faq"
URL_FT_results = URL +"/hledani-vysledky?q="
URL_LM = URL + "/last-minute"
URL_stat_zima = URL + "/rakousko"

URL_zima = "https://nev-dama.uat.dtweb.cz/zima"

URL_SRL_zima = URL_zima + "/vysledky-vyhledavani?ac1=2&d=85383|85385|85394|85407|85413|108815|85434|85436&dd=2023-08-31&nn=2|3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&tt=0"
URL_FM_zima = URL +"/first-minute"
URL_lm_zima = URL_zima +"/last-minute"
URL_stat_zima = URL_zima +"/rakousko"
URL_groupsearch_zima = URL_zima +"/vysledky-vyhledavani?ac1=2&dd=2023-08-31&nn=2|3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&tt=0"
URL_stat_zima = URL_zima + "/rakousko"

URL_leto = "https://nev-dama.uat.dtweb.cz/leto"

URL_SRL_leto = URL_leto + "/vysledky-vyhledavani?ac1=2&d=108939|108938|108941|109497|108940|108942&dd=2023-08-31&nn=2|3|4|5|6|7|8|9&rd=2023-10-31&tt=0"
URL_FM_leto = URL +"/first-minute-leto"
URL_lm_leto = URL_leto +"/last-minute"
URL_stat_leto = URL_leto +"/chorvatsko"
URL_groupsearch_leto = URL_leto +"/vysledky-vyhledavani?ac1=2&dd=2023-08-31&nn=2|3|4|5|6|7|8|9&rd=2023-10-31&tt=0"
URL_stat_leto = URL_leto + "/chorvatsko"



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


