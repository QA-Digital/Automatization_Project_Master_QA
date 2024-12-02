from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from to_import_secret_master import emailPass




def tearDown(self):

  print(self.driver.current_url)
  self.driver.quit()
  if not self.test_passed:
    self.driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

brand_name_project = "Penny"
desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized - Web Monitor V2.1",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}
def setUp(self):
 # self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False


URL = "https://www.pennydovolena.cz/"
URL_local = "https://www.pennydovolena.cz/"
URL_FM = "first-minute"
URL_exotika = "exoticka-dovolena"
URL_LM = "last-minute"
URL_SRL = "/vysledky-vyhledavani?sortby=ByRecommedation&d=64419|64420|64425|63213|63241|63267|74459|74460|63284|74464|63350|63354|63360|63226|74465|64422|64423|63216|63242|63244|74462|63313|74461|74463|63349|63455&tt=0&dd=2023-08-20&rd=2023-09-30&nn=7|8|9&ka1=8|6&kc1=2&ac1=2"
URL_SRL_all_inclusive = URL_SRL + "&m=5"
URL_detail = "/egypt/hurghada/hurghada/la-rosa-waves?DS=256&GIATA=1272734&D=64419|64420|64425|64422|64423&HID=128528&MT=5&NN=7&DF=2023-03-01|2023-03-31&RD=2023-03-25&DD=2023-03-18&ERM=0&AC1=2&KC1=0&IC1=0&DP=4305&MNN=7&NNM=7|8|9&TT=1&TTM=0&PID=HRG90011&DPR=FISCHER%20ATCOM"
URL_detail_all_inclusive = URL_detail + "&mmt=5"
URL_detail_airport_praha = URL_detail + "&tom=4312"
URL_FT_results = "/hledani-vysledky?q="
URL_groupsearch = "/vysledky-vyhledavani?tt=1&dd=2022-08-04&rd=2022-09-30&nn=7|8|9&ka1=5&kc1=1&ac1=2"
URL_SDO = "/spanelsko"






def generalDriverWaitImplicit(driver):
  time.sleep(3)
  driver.implicitly_wait(25)
def acceptConsent(driver):
  driver.maximize_window()
  generalDriverWaitImplicit(driver)
  generalDriverWaitImplicit(driver)
  # time.sleep(5)
  try:
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
"x"
def returnLocatorForMealHotelKarty(poziceHotelu):
    #string1 = '//*[@id="app"]/pagemainsearchfilter/div/div[4]/div[2]/div/div['
    string1 = "/html/body/div[1]/div/div[4]/div[2]/div/div["
    stringVariable = poziceHotelu
    stringVariable = str(stringVariable)
    string2 = "]/a/div[3]/div[3]/div[2]/span[1]"
    #string2 = ']/a/div[3]/div[3]/div[2]/span[1]'
    finalString = string1 + stringVariable + string2
    finalString = finalString.replace(" ", "")
    #print(finalString)
    return str(finalString)

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

def closeExponeaBanner():
    pass