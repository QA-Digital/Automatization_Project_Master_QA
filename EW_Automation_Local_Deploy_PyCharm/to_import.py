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
URL = "https://exim.web11.dtweb.cz/"
#URL = "http://exim.uat.dtweb.cz/"
URL_poznavacky = URL+"poznavaci-zajezdy"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy#rodiny"
URL_pobocky = URL+"kontakty/nase-pobocky"
URL_kluby = URL+"informace-pro-klienty/mango-club"
#URL_detail = URL+"/egypt/hurghada/hurghada/hawaii-caesar-palace-egypt-2?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2023-06-06&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=411448&HID=9198&IC1=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG90006&RD=2023-06-13&TO=4305&acm1=2&df=2023-06-01|2023-06-30&nnm=7|8|9|10|11|12|13&tt=1&ttm=1#/prehled"
URL_detail = URL + "/turecko/turecka-riviera/avsallar/incekum-su?D=63260|63288|63448|64152|64153|64154|64157|211801|211814&DD=2023-08-28&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=59394&HID=374&MNN=7&MT=5&NN=7&PID=AYT19071&RD=2023-09-04&TO=4305&df=2023-08-21|2023-09-30&nnm=7|8|9|10|11|12|13&sortby=Departure&tt=1&ttm=1#/prehled"
#URL_SRL = URL+"vysledky-vyhledavani?d=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=64419|64420|64425&tt=1&to=4312|4305|2682|4308&dd=2022-09-01&rd=2022-10-19&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63213|63226|211764|63241|63360|63267|74459|74460|63284|74464|63349|63350|63354|74465&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=64419|64420|64425|63213|63226|211764|63241|63360|63267|74459|74460|63284|74464|63349|63350|63354|74465|63484|63483|63485&tt=1&to=4312|4305|2682|4308&dd=2022-08-01&rd=2022-09-30&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63448|211801|211814|63252|63260|63288|64154|64152|64153|64157&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "/vysledky-vyhledavani?d=64419|64420|64425&tt=1&to=4312|4305|2682|4308&dd=2023-03-02&rd=2023-03-26&nn=7&ac1=2"
URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425&dd=2023-09-01&ka1=11&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2023-10-31&to=4312|4305|2682|4308&tt=1"
URL_covidInfo = URL+"covid-info"
URL_FM = URL+"first-minute"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhledavani?tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ic1=1&ac1=2"
URL_FT_results = URL+"hledani-vysledky?q="
URL_SRL_kuba_regres = URL+"vysledky-vyhledavani?ac1=2&d=63888&dd=2023-07-01&nn=7|8|9|10|11|12|13|14|15|16|17|18|19|20|21&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"



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


