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

brand_name_project = "BILLA"
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


URL = "https://www.billatravel.cz/"
#URL = "https://billa.web3.dtweb.cz/"
#URL = "https://billa.stg.dtweb.cz/"
URL_FM = URL+"first-minute"
URL_LM = URL+"last-minute"
#URL_SRL = "https://billa.dev.dtweb.cz/vysledky-vyhledavani?d=63213|63216|63218|63349|63226|63227|63231|64429|63241|63242|63243|63244|63245|74462|63263|63267|74459|63272|74460|63284|63299|63334|63313|74461|78291|74463|63328|74464|63350|64430|63354|63360|63363|74465|63455&tt=1&dd=2022-06-15&rd=2022-06-23&nn=7&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63448|63260|63213|63241|63360|63267|74459|74460|63284|74464|63350|63354|74465|63216|63226|63242|63244|74462|63313|74461|74463|63349|63455|63288|64154|64152|64153|64157&tt=0&dd=2022-08-12&rd=2022-09-30&nn=7|8|9&ac1=2"
#URL_SRL = URL + "/vysledky-vyhledavani?sortby=ByRecommedation&d=64419|64420|64425|63213|63241|63360|63267|74459|74460|63284|74464|63350|63354|74465|64422|64423|63216|63226|63242|63244|74462|63313|74461|74463|63349|63455&tt=0&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-31&nn=7|8|9&ka1=10&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=64419|64420|64425|64422|64423&tt=0&dd=2023-02-01&rd=2023-02-26&nn=7|8|9&ac1=2&ds=8192"
URL_SRL = URL + "/vysledky-vyhledavani?sortby=ByRecommedation&d=64419|64420|64425|63213|63241|63267|74459|74460|63284|74464|63350|63354|63360|63226|74465|64422|64423|63216|63242|63244|74462|63313|74461|74463|63349|63455&tt=0&dd=2023-08-20&rd=2023-09-30&nn=7|8|9&ka1=8|6&kc1=2&ac1=2"

URL_SRL_all_inclusive = URL_SRL + "&m=5"

#URL_detail = URL + "egypt/hurghada/hurghada/mirage-bay-resort-a-aqua-park-hurghada?KEY=2257927099&DS=1024&GIATA=16351&D=64419|64420|64425|64422|64423&HID=5057&MT=5&RT=15&NN=7&DF=2022-07-13|2022-09-12&RD=2022-08-15&DD=2022-08-08&AC1=2&KC1=1&KA1=4&IC1=0&DP=4308&MNN=7&NNM=7|8|9&TT=1&TTM=0&PID=33040&DPR=EXIM%20TOURS"
#URL_detail = URL+"recko/lefkada/nidri/delfini-penzion?ds=1024&giata=538958&hid=141090&nn=7&df=2022-07-01|2022-09-01&rd=2022-09-01&dd=2022-08-25&ac1=2&kc1=1&ka1=5&tt=1&pid=335821&d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|63219|63341|63428&mt=2&rt=15&dp=4305&mnn=7&nnm=7|8|9&ttm=1&dpr=EXIM%20TOURS&sortby=Price&sortorder=0"
URL_detail = URL +"/egypt/hurghada/hurghada/la-rosa-waves?DS=256&GIATA=1272734&D=64419|64420|64425|64422|64423&HID=128528&MT=5&NN=7&DF=2023-03-01|2023-03-31&RD=2023-03-25&DD=2023-03-18&ERM=0&AC1=2&KC1=0&IC1=0&DP=4305&MNN=7&NNM=7|8|9&TT=1&TTM=0&PID=HRG90011&DPR=FISCHER%20ATCOM"
#URL_detail = URL+ "spanelsko/mallorca/mariant-55?ds=256&giata=21437&hid=21&df=2023-07-01|2023-08-31&rd=2023-08-31&dd=2023-08-23&pid=PMI14448&dpr=FISCHER%20ATCOM&d=63242|63244|63350|74459|74460|74461|74462|74464|74465|63213|63216|63218|63226|63227|63231|63241|63243|63245|63263|63267|63272|63284|63299|63313|63328|63334|63349|63354|63360|63363|63455|64429|64430|74463&mt=5&nn=7&dp=4305&to=4305&mnn=7&nnm=7|8|9&tt=1&ttm=0&sortby=Departure&sortorder=0"
URL_detail_all_inclusive = URL_detail + "&mmt=5"
URL_detail_airport_praha = URL_detail + "&tom=4312"
URL_FT_results = URL + "hledani-vysledky?q="
URL_groupsearch = URL + "vysledky-vyhledavani?tt=1&dd=2022-08-04&rd=2022-09-30&nn=7|8|9&ka1=5&kc1=1&ac1=2"
URL_SDO = URL + "spanelsko"





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