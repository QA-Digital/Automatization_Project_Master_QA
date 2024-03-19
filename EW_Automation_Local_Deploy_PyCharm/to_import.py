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
from webdriver_manager.firefox import GeckoDriverManager
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)




  # self.driver = webdriver.Chrome(ChromeDriverManager().install())

   chrome_driver_path = 'C:/Users/KADOUN/Desktop/Python_utils/chromedriver.exe'
   self.driver = webdriver.Chrome(executable_path=chrome_driver_path)





#  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  # options = webdriver.ChromeOptions()
  # options.add_argument("--headless")
  # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  #self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

   self.test_passed = False

#URL = "https://www.eximtours.cz/"
#URL = "https://exim.web11.dtweb.cz/"
URL = "http://exim.stg.dtweb.cz/"

#URL = "https://exim.stg.dtweb.cz/"
#URL = "http://exim.uat.dtweb.cz/"
URL_poznavacky = URL+"poznavaci-zajezdy"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy#rodiny"
URL_pobocky = URL+"kontakty/nase-pobocky"
URL_kluby = URL+"/kluby/mango-leto"
#URL_detail = URL+"/egypt/hurghada/hurghada/hawaii-caesar-palace-egypt-2?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2023-06-06&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=411448&HID=9198&IC1=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG90006&RD=2023-06-13&TO=4305&acm1=2&df=2023-06-01|2023-06-30&nnm=7|8|9|10|11|12|13&tt=1&ttm=1#/prehled"
URL_detail = URL + "/egypt/hurghada/hurghada/amarina-abu-soma-resort?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2024-10-16&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=85&HID=9156&IC1=1&IFM=0&ILM=0&KA1=10&KC1=1&MNN=7&MT=5&NN=7&PID=HRG90013&RC=DR01&RD=2024-10-23&TO=4305&acm1=2&df=2024-10-14|2024-10-31&icm1=1&kam1=10&kcm1=1&nnm=7|8|9|10|11|12|13|14&ptm=0&sortby=Departure&tt=1&ttm=1#/prehled"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=64419|64420|64425&tt=1&to=4312|4305|2682|4308&dd=2022-09-01&rd=2022-10-19&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63213|63226|211764|63241|63360|63267|74459|74460|63284|74464|63349|63350|63354|74465&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=64419|64420|64425|63213|63226|211764|63241|63360|63267|74459|74460|63284|74464|63349|63350|63354|74465|63484|63483|63485&tt=1&to=4312|4305|2682|4308&dd=2022-08-01&rd=2022-09-30&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63448|211801|211814|63252|63260|63288|64154|64152|64153|64157&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "/vysledky-vyhledavani?d=64419|64420|64425&tt=1&to=4312|4305|2682|4308&dd=2023-03-02&rd=2023-03-26&nn=7&ac1=2"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425&dd=2023-09-01&ka1=11&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2023-10-31&to=4312|4305|2682|4308&tt=1"
URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=211764|63241|63242|213028|63243|63245|74459|74460|63284|74464|63350|63354|74465|63213|63216|63218|63226|63227|63231|64429|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=2024-09-01&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4392|4309&tt=1"
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


