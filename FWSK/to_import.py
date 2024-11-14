from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from definitions import EDGE_DRIVER_PATH
from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

brand_name_project = "FISCHERSK"
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
  from selenium.webdriver.edge.service import Service
  service = Service(EDGE_DRIVER_PATH)
  self.driver = webdriver.Edge(service=service)

  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  #self.driver = webdriver.Chrome(ChromeDriverManager().install())
  #chrome_driver_path = 'C:/Users/KADOUN/Desktop/Python_utils/chromedriver.exe'
  #self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
  self.test_passed = False


URL_local =  "https://fischersk.stg.dtweb.cz/"
URL = "https://fischersk.stg.dtweb.cz/"
URL_poznavacky = "poznavacie-zajazdy/okruhy-a-kombinovane"
URL_poznavacky_vikendy = "poznavacie-zajazdy/predlzene-vikendy"
URL_poznavacky_rodiny = "poznavacie-zajazdy/pre-rodiny"
URL_poznavacky_zazitky = "poznavacie-zajazdy/zazitkove"
URL_pobocky = "kontakty/seznam-pobocek"
URL_kluby = "dovolena-animacni-kluby"
URL_SRL = "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-31&ds=0&ifm=0&ilm=0&nn=7|8|9|10|11|12|13&rd=2023-12-31&sc=residential&to=483|1837|2933|3437|4305|2682|4308|4312&tt=1"
URL_detail_new = "/spanielsko/almeria/roquetas-de-mar/mediterraneo-bay-hotel-spa-a-resort?DS=256&GIATA=2458&D=621%7C1009%7C680%7C622%7C1108%7C953%7C669%7C1086%7C1194%7C670%7C978%7C594%7C611%7C610%7C592%7C675%7C612%7C1010%7C590%7C726%7C609&HID=13048&MT=2&DI=HB&RC=DR01&RCS=DR01&NN=7&DF=2025-08-08%7C2025-08-31&RD=2025-08-18&DD=2025-08-11&ERM=0&AC1=1&KC1=0&IC1=0&DP=483&TO=483&TOM=483&MNN=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&NNM=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&TT=1&TTM=1&PID=LEI90003&DPR=FISCHER+SK+ATCOM&ILM=0&IFM=0&PC=12824027%2F2%2F2049%2F7&IFC=99281825%2F379154&OFC=99280838%2F379153"
URL_detail = "/egypt/egypt-hurghada/hurghada/horus-4?AC1=1&D=653|819&DD=2025-09-10&DI=IT&DP=4312&DPR=FISCHER+ATCOM&DS=16384&GIATA=0&HID=143635&IC1=0&IFC=95616028%2F369279&IFM=0&ILM=0&KC1=0&MNN=7&MT=7&NN=7&OFC=95615353%2F358466&PC=9915025%2F2%2F2079%2F7&PID=EGR00005&RC=DR01&RCS=DR01&RD=2025-09-17&TO=4305|4392|4309|2682|4308|4312|483|1837|2933|3437|3248&acm1=2&dd=2024-11-06&df=2024-11-06|2025-09-06&nnm=7|8|9|10|11|12|13|14&ptm=0&rd=2025-09-06&sortby=Departure&tt=1&ttm=1#/prehľad"
URL_covidInfo = "covid-info"
URL_fmExotika = "first-minute"
URL_faq = "faq"
URL_lm = "last-minute"
URL_stat = "spanelsko"
URL_groupsearch = "vysledky-vyhladavania?dd=2023-07-01&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437&tt=1"
URL_FT_results = "hladanie-vysledky?q="



def tearDown(self):
  print(self.driver.current_url)
  self.driver.quit()
  if not self.test_passed:
    self.driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

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

  generalDriverWaitImplicit(driver)
  generalDriverWaitImplicit(driver)
  time.sleep(2.5)
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

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element(By.XPATH, "//*[@class='exponea-popup-banner']")
      if exponeaBanner.is_displayed():
        wait.until(EC.visibility_of(exponeaBanner))
        exponeaCrossAndBanner = driver.find_element_by_xpath(
          "//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
        exponeaCrossAndBanner.click()
        time.sleep(2)

    except NoSuchElementException:
      print("nenasle se exponea banner")

def acceptConsent3(driver):
  time.sleep(2)

  element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  if element !=0:

      pass

  else:
      element.click()

