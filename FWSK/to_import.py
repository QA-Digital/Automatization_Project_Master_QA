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
  self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

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
URL_detail = "/egypt/egypt-hurghada/makadi-bay/xanadu-makadi-bay?AC1=2&D=653|819|1235|724&DD=2024-10-03&DP=483&DPR=FISCHER+SK+ATCOM&DS=256&GIATA=1311753&HID=143982&IC1=0&IFM=0&ILM=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG00500&RC=DR01&RD=2024-10-10&TO=483|1837|2933|3437&acm1=2&df=2024-10-01|2024-10-31&nnm=7|8|9|10|11|12|13|14|15&ptm=0&tt=1&ttm=1#/prehľad"
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

