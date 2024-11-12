from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

#URL_local = "https://www.kartago.sk/"
from definitions import EDGE_DRIVER_PATH

URL_local =  "https://kartagosk.web1.dtweb.cz/"
URL = "https://kartagosk.web1.dtweb.cz/"
URL_poznavacky = "poznavaci-zajezdy"
URL_poznavacky_vikendy = "poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = "poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = "poznavaci-zajezdy#rodiny"
URL_pobocky = "kontakty/nase-predajne"
URL_kluby = "uzitocne-informacie/mango-club"
URL_detail = "/egypt/hurghada/hurghada/hatsepsut-4?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2025-06-04&DI=IT&DP=4312&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=0&HID=9182&IC1=0&IFC=95609728%2F369282&IFM=0&ILM=0&KC1=0&MNN=7&MT=7&NN=7&OFC=95609053%2F358469&PC=6235798%2F2%2F1981%2F7&PID=EGR00007&RC=DR01&RCS=DR01&RD=2025-06-11&acm1=2&dd=2024-11-06&df=2024-11-06|2025-09-06&nnm=7|8|9|10|11|12|13|14&ptm=0&rd=2025-09-06&sortby=Departure&tt=1&ttm=1#/prehľad"
URL_detail_new = "/egypt/hurghada/makadi-bay/prima-life-makadi-resort-a-spa?DS=65536&GIATA=77592&D=64419%7C64420%7C64422%7C64423%7C64424%7C64425&HID=9193&MT=5&DI=AE&RC=DR01&RCS=DR01&NN=7&DF=2025-05-01%7C2025-07-02&RD=2025-05-29&DD=2025-05-22&ERM=0&AC1=2&KC1=0&IC1=0&DP=1837&TO=1837&TOM=1837&MNN=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&NNM=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&TT=1&TTM=1&PID=HRG20068&DPR=KARTAGO-SK-ATCOM&ILM=0&IFM=0&PC=5335723%2F2%2F1968%2F7&IFC=99810632%2F382846&OFC=99809645%2F382845"
URL_SRL = "/vysledky-vyhladavania?ac1=2&d=64419|64420|64423|64425&dd=2023-07-01&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-08-31&to=483|1837|2933|3437&tt=1"
URL_covidInfo = "covid-info"
URL_FM = "first-minute/leto"
URL_faq = "faq"
URL_lm = "last-minute"
URL_stat = "egypt"
URL_groupsearch = "vysledky-vyhladavania?tt=1&to=483|1837|2933|3437&dd=2022-09-01&rd=2022-09-25&nn=7|8|9|10|11|12|13&ka1=6&kc1=1&ac1=2"
URL_FT_results = "hladanie-vysledky?q="

import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
brand_name_project = "KARTAGOSK"
from desired_cap_generator import desired_cap_Branded
desired_cap2 = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized Suite For Web Monitoring",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}

desired_cap = desired_cap_Branded("KTGSK", "Optimized - Web Monitor V2")
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor, desired_capabilities=desired_cap)
  #self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
  self.test_passed = False


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
  time.sleep(3)
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


def acceptConsent5(driver):
  time.sleep(2)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  except NoSuchElementException:
    return

  except TimeoutException:
    pass
  try:
    element.click()
  except TimeoutException:
    pass
  except NoSuchElementException:
    return

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
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

