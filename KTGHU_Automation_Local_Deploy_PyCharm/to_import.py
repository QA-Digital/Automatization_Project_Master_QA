from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

URL = "https://kartagohu.stg.dtweb.cz/"
#URL = "https://www.kartagotours.hu/"
URL_pobocky = URL+"irodaink"
URL_detail = URL + "/egyiptom/hurghada/makadi-bay/prima-life-makadi-resort-and-spa?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2024-10-02&DI=AE&DP=489&DPR=KARTAGO-HU-ATCOM&DS=65536&GIATA=77592&HID=9193&IC1=1&IFC=45774792%2F207929&IFM=0&ILM=0&KA1=11&KC1=1&MNN=7&MT=5&NN=7&OFC=45774461%2F207928&PC=10525827%2F2%2F1736%2F7&PID=HRG20068&RC=DR01&RD=2024-10-09&TO=489|4371&acm1=2&df=2024-10-01|2024-10-31&icm1=0&kam1=11&kcm1=1&nnm=7|8|9|10&ptm=0&tt=1&ttm=1#/prehled"


#URL_SRL = URL + "keresesi-eredmenyek?qf=108_1_0|386_1_0|108_1_0&d=64089|64091|64419|64420|64087|64094|64095|64090|64086|64092|64425&tt=1&to=489&dd=2022-09-01&rd=2022-10-31&ka1=6&kc1=1&ac1=2"
##Dynamix search result
#URL_SRL = URL + "keresesi-eredmenyek?d=64089|64091|64419|64420|64425|63324|63402|63471|63448|211801|211814|63260|63252|63447|74459|74460|74465|64087|64094|64095|64090|64086|64092|63288|63281|63311|63314|63316|63319|63333|63362|63373|63390|63409|63442|63431|63213|63226|211764|63241|63267|63284|74464|63349|63350|63354|63360&tt=1&to=489|4371|2033|3418|3789|483|1837|2933|3437|3248|4305|4309|2682|4308|4312|298|874|892|983|1091|1293|1956|2397|2563|3352|1862|1825|3850&dd=2022-08-01&rd=2022-09-30&ka1=5&kc1=1&ac1=2&DS=2"
#URL_SRL = URL + "keresesi-eredmenyek?d=64419|64420|64425&tt=1&dd=2023-06-01&rd=2023-07-31&ac1=2"

URL_SRL = URL + "/keresesi-eredmenyek?ac1=2&d=64419|64420|64421|64422|64423|64424|64425|64426&dd=2024-10-01&ic1=1&ka1=11&kc1=1&nn=7|8|9|10&rd=2024-10-31&to=489|4371&tt=1"

#URL_SRL = URL + "vysledky-vyhladavania?d=63350|211764&tt=1&to=483|1837|2933|3437&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=6&kc1=1&ac1=2"
URL_covidInfo = URL+"covid-info"
URL_FM = URL+"first-minute"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"egyiptom"
URL_groupsearch = URL+"keresesi-eredmenyek?tt=1&to=489&dd=2022-09-01&rd=2022-10-31"
URL_FT_results = URL+"hledani-vysledky?q="
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

desired_cap = desired_cap_Branded("KTGHU", "Optimized - Web Monitor V2")
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor, desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  # chrome_driver_path = 'C:/Users/KADOUN/Desktop/Python_utils/chromedriver.exe'
  # self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
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

