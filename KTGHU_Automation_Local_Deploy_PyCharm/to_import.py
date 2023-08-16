from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

URL = "https://kartagohu.web3.dtweb.cz/"
#URL = "https://www.kartagotours.hu/"
URL_pobocky = URL+"irodaink"
#URL_detail = URL + "/egyesult-arab-emirsegek/ras-al-khaimah/ras-al-khaimah/bin-majid-beach-hotel-ai?KEY=2324196473&DS=32768&GIATA=42262&D=64089|64091|64087&HID=128559&MT=5&MMT=5&RT=15&NN=7&RD=2022-08-30&DD=2022-08-23&DP=489&TO=489|4371&MNN=7&TT=1&PID=346971&DPR=KARTAGO-HU&TTM=1&TOM=489|4371&DF=2022-08-23|2022-09-23&ERM=0&NNM=7|8|9&ac1=2&kc1=1&ka1=8&ic1=0"
#URL_detail = URL+"spanielsko/costa-almeria/roquetas-de-mar/ar-almerimar?KEY=2207812211&DS=32768&GIATA=0&D=63350|211764&HID=142164&MT=2&RT=15&NN=7&RD=2022-08-01&DD=2022-07-25&DP=483&TO=483|1837|2933|3437&MNN=7&TT=1&PID=359709&DPR=KARTAGO-SK&TTM=1&DF=2022-07-25|2022-08-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=1&ka1=6&ic1=0#/prehled"
#URL_detail = URL+"torokorszag/torok-riviera/tekirova/pirates-beach?KEY=2263569953&DS=32768&GIATA=4818&D=64089|64091|64419|64420|64425|63324|63402|63471|63448|211801|211814|63260|63281|63311|63314|63316|63319|63333|63362|63373|63390|63409|63442|63431|64087|64094|64095|64090|64086|64092|63288&HID=8542&MT=-1&RT=15&NN=7&DF=2022-10-01|2022-10-16&RD=2022-10-14&DD=2022-10-07&AC1=2&KC1=0&IC1=0&DP=489&TO=489|4371&TOM=489|4371&MNN=7&NNM=7&TT=1&TTM=1&PID=28962&DPR=KARTAGO-HU"
#URL_detail = URL+"tunezia/tunezia-(szarazfold)/mahdia/nour-palace?KEY=2258518250&DS=32768&GIATA=28170&D=63252|63447&HID=4751&MT=5&RT=15&NN=7&RD=2022-10-14&DD=2022-10-07&DP=489&TO=489|4371&MNN=7&TT=1&PID=4580&DPR=KARTAGO-HU&TTM=1&DF=2022-10-07|2022-10-14&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "torokorszag/torok-riviera/tekirova/pirates-beach?KEY=2294508106&DS=32768&GIATA=4818&D=64419|64420|64425|63448|211801|211814|63260|63288&HID=8542&MT=-1&RT=15&NN=7&RD=2022-10-26&DD=2022-10-19&DP=489&TO=489|4371&MNN=7&TT=1&PID=28962&DPR=KARTAGO-HU&TTM=1&DF=2022-10-19|2022-11-19&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "egyiptom/hurghada/hurghada/hawaii-caesar-palace?KEY=2213360863&DS=32768&GIATA=411448&D=64419|64420|64425&HID=9198&MT=5&RT=15&NN=7&RD=2022-09-18&DD=2022-09-11&DP=489&TO=489|4371&MNN=7&TT=1&PID=334962&DPR=KARTAGO-HU&TTM=1&TOM=489|4371&DF=2022-09-11|2022-10-12&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
#URL_detail = URL + "/egyiptom/hurghada/hurghada/hawaii-dreams?KEY=2213358835&DS=32768&GIATA=978047&D=64419|64420|64425&HID=9188&MT=5&RT=15&NN=7&RD=2022-09-18&DD=2022-09-11&DP=489&TO=489|4371&MNN=7&TT=1&PID=335867&DPR=KARTAGO-HU&TTM=1&DF=2022-09-11|2022-09-18&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "/egyiptom/hurghada/safaga/caribbean-world-soma-bay?KEY=2212884352&DS=32768&GIATA=79878&D=64419|64420|64425&HID=5006&MT=5&RT=15&NN=7&RD=2022-10-05&DD=2022-09-28&DP=489&TO=489|4371&MNN=7&TT=1&PID=5598&DPR=KARTAGO-HU&TTM=1&DF=2022-09-28|2022-10-29&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "/hotely/egyesult-arab-emirsegek/ras-al-khaimah/ras-al-khaimah/hampton-by-hilton-marjan-island?DS=2&GIATA=1009408&D=64087|64089|64091|64090|64086&HID=1397&MT=5&MMT=5&RT=15&NN=7&RD=2023-08-06&DD=2023-07-29&DP=489&TO=489|4371&MNN=7&TT=1&PID=AAEDXBDFW0&DPR=OTSCKF&TTM=1&TOM=489|4371&DF=2023-07-29|2023-08-29&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "/tunezia/tunezia-(szarazfold)/hammamet/samira-club-spa-a-aqua-park?DS=65536&GIATA=20914&D=63252|63447&HID=4765&MT=5&NN=7&RD=2023-06-09&DD=2023-06-02&DP=489&MNN=7&TT=1&PID=MIR10020&DPR=KARTAGO-HU-ATCOM&TTM=1&DF=2023-06-02|2023-07-03&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0"
#URL_detail = URL + "egyiptom/marsa-alam/marsa-alam/sol-y-mar-reef-resort?DS=65536&GIATA=126426&D=64419|64420|64425&HID=141936&MT=5&NN=7&RD=2023-06-21&DD=2023-06-14&DP=489&MNN=7&TT=1&PID=RMF90016&DPR=KARTAGO-HU-ATCOM&TTM=1&DF=2023-06-14|2023-07-15&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0"
URL_detail = URL+ "egyiptom/marsa-alam/marsa-alam/blue-reef-resort?AC1=2&D=64419|64420|64425&DD=2023-10-04&DP=489&DPR=KARTAGO-HU-ATCOM&DS=65536&GIATA=100548&HID=3968&IC1=0&KC1=0&MNN=7&MT=5&NN=7&PID=RMF20022&RD=2023-10-11&TO=489|4371&acm1=2&df=2023-10-01|2023-10-31&nnm=7&tt=1&ttm=1#/prehled"


#URL_SRL = URL + "keresesi-eredmenyek?qf=108_1_0|386_1_0|108_1_0&d=64089|64091|64419|64420|64087|64094|64095|64090|64086|64092|64425&tt=1&to=489&dd=2022-09-01&rd=2022-10-31&ka1=6&kc1=1&ac1=2"
##Dynamix search result
#URL_SRL = URL + "keresesi-eredmenyek?d=64089|64091|64419|64420|64425|63324|63402|63471|63448|211801|211814|63260|63252|63447|74459|74460|74465|64087|64094|64095|64090|64086|64092|63288|63281|63311|63314|63316|63319|63333|63362|63373|63390|63409|63442|63431|63213|63226|211764|63241|63267|63284|74464|63349|63350|63354|63360&tt=1&to=489|4371|2033|3418|3789|483|1837|2933|3437|3248|4305|4309|2682|4308|4312|298|874|892|983|1091|1293|1956|2397|2563|3352|1862|1825|3850&dd=2022-08-01&rd=2022-09-30&ka1=5&kc1=1&ac1=2&DS=2"
#URL_SRL = URL + "keresesi-eredmenyek?d=64419|64420|64425&tt=1&dd=2023-06-01&rd=2023-07-31&ac1=2"

URL_SRL = URL + "keresesi-eredmenyek?ac1=2&d=63252|63447&dd=2023-06-01&nn=7|8|9&rd=2023-07-31&to=489|4371&tt=1"

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

