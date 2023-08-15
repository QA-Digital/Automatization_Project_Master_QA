from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

brand_name_project = "FISCHER"
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

from selenium.webdriver.edge.service import Service as EdgeService
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  #self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  self.test_passed = False


#URL = "https://www.fischer.cz/"
#URL = "https://fischer.web3.dtweb.cz/"

#URL = "https://www.fischer.cz/"
#URL = "http://fischer.web1.dtweb.cz/"
URL = "https://fischer.stg.dtweb.cz/"
URL_poznavacky = URL+"poznavaci-zajezdy/okruzni-a-kombinovane"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy/prodlouzene-vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy/pro-rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy/zazitkove"
URL_pobocky = URL+"kontakty/seznam-pobocek"
URL_kluby = URL+"dovolena-animacni-kluby"
#URL_detail = "https://fischer2.stg.dtweb.cz/recko/kreta-heraklion/gouves/kalia-beach?AC1=2&D=1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|826|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&DD=2022-10-09&DI=13&DP=4312&DPR=Fischer&DS=1&GIATA=892&HID=524301&IC1=0&KC1=0&KEY=0xA43A619349C9BBE09C5EFE3E55B5AD9B1F302538&MNN=7&MT=5&NN=7&PID=KKAL&RD=2022-10-16&RT=15&TO=4305|4309|2682|4308|4312&acm1=2&df=2022-10-01|2022-11-30&nnm=7&tom=4309&tt=1&ttm=1"
#URL_detail = URL+"recko/rhodos/kalithea/amira?KEY=0xAC636C6ABB1245F78140DDD5CD0B0EAADE97E193&DS=1&GIATA=19462&D=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=65023&MT=2&DI=47&RT=15&NN=7&RD=2022-09-11&DD=2022-09-04&DP=4305&TO=4305&MNN=7&TT=1&PID=RPRI&DPR=Fischer&TTM=1&DF=2022-09-01|2022-09-18&ERM=0&NNM=7|8|9|10|11|12|13|17&ac1=2&kc1=1&ka1=7&ic1=0#/prehled"
#URL_detail= URL + "egypt/egypt-hurghada/hurghada/la-rosa-waves?D=653|819&DD=2023-03-18&DP=4305&DPR=FISCHER+ATCOM&DS=256&GIATA=1272734&HID=128528&MMT=5&MNN=7&MT=5&NN=7&PID=HRG90011&RD=2023-03-25&TO=4305&ac1=2&acm1=2&df=2023-03-18|2023-04-18&ic1=0&kc1=0&nnm=7|8|9|10|11|12|13&sortby=Departure&tt=1&ttm=1#/prehled"
#URL_detail= URL + "/spanelsko/gran-canaria/the-lago-taurito?DS=256&GIATA=2801&D=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&HID=1797&MT=5&MMT=5&NN=7&DF=2023-03-01|2023-04-30&RD=2023-04-19&DD=2023-04-12&ERM=0&AC1=2&KC1=0&IC1=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=LPA90004&DPR=FISCHER%20ATCOM"
URL_detail = URL + "/recko/korfu/roda/angela-beach?D=1126|1129|826|1225|1124|1128|623|1059|1118|1119|1121|741|735|618|619|624|1127|973|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|993|1131|595|614|648|972|1123|1093|1198|1114|1122|620|746&DD=2023-08-24&DP=4305&DPR=FISCHER+ATCOM&DS=256&GIATA=632&HID=794&MNN=7&MT=5&NN=7&PID=CFU50152&RD=2023-08-31&TO=4305&df=2023-08-01|2023-09-30&nnm=7|8|9|10|11|12|13&sortby=Departure&tt=1&ttm=1#/prehled"
#URL_detail = URL + "turecko/turecka-riviera/alanya/kleopatra-blue-hawai?AC1=2&D=596&DD=2022-10-08&DI=13&DP=4305&DPR=Fischer&DS=1&GIATA=12284&HID=171619&IC1=0&KC1=0&KEY=0xDEB99EAD455684E375DCC136849DA433BE0DE3CC&MNN=7&MT=5&NN=7&PID=AYABLH&RD=2022-10-15&RT=15&TO=4305&acm1=2&df=2022-10-01|2022-10-31&nnm=7&tt=1&ttm=1#/prehled"
##atcom spaneslko
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&dd=2023-02-01&ka1=11&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-02-26&to=4312|4305|2682|4308&tt=1"
##atcom egypt
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2023-02-01&ka1=4|14&kc1=2&nn=7|8|9|10|11|12|13&rd=2023-03-31&to=4312|4305|2682|4308&tt=1"

#URL_SRL = URL+"vysledky-vyhledavani?d=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=607|591&dd=2023-07-01&nn=7|8|9&rd=2023-08-31&to=483|1837|2933|3437|3248|4312|4305|2682|4308&tt=1"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?ac1=2&d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&dd=2022-09-01&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2022-09-30&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=653|819|724|627|974|596|680|953|1108|592|611|610|612|590|726|609|607|591|712|684|955|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-03-18&ka1=8&kc1=1&nn=7&rd=2023-03-25&to=4305|4312|2682|4308|483|1837|2933|3437|3248&tt=1"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=627|974|596|680|953|1108|592|611|610|612|590|726|609|605|677|712|684|955|745|1061|965|822|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2022-10-01&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2022-10-30&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = "https://fischer.web3.dtweb.cz/vysledky-vyhledavani?sortby=PriceTotal&d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=1225|623|741|735|618|619|624|973|993|595|972|648|620|746|687|604|644|674|642|616|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057|1126|1129|826|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&dd=2022-10-01&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2022-10-30&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=1&d=644|674|642|616|664|607|591|608|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=2022-08-30&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2022-10-30&to=4312|4305|2682|4308&tt=1"
URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=622|1086|590|726|670|680|621|669|1009|1010|1108|611|610|609|953|612&dd=2023-02-01&nn=7|8|9|10|11|12|13&rd=2023-03-31&to=4312|4305|2682|4308&tt=1"
#URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?ac1=2&ac2=2&d=664&dd=2023-03-01&ka2=2|6|8&kc2=3&nn=7&rd=2023-03-31&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=680|1108|953|611|610|592|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-09-01&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "vysledky-vyhledavani?ac1=2&d=664&dd=2023-09-01&ka1=11&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&dd=2023-04-03&nn=7|8|9|10|11|12|13&rd=2023-06-03&sa=4327&to=4312|4305|2682|4308&tt=1"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=634&dd=2023-07-01&nn=7|8|9|10|11|12|13|14&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"


##lyzovane
#URL_SRL = URL + "/dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=1085|1083&dd=2023-03-01&ds=0&ea=356&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21&rd=2023-04-30&sc=skiing&to=4312|4305|2682|4308&tt=3"

URL_covidInfo = URL+"covid-info"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_fmExotika = URL+"first-minute/exotika-zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhledavani?ac1=2&dd=2023-02-01&nn=7|8|9|10|11|12|13&rd=2023-02-26&to=4312|4305|2682|4308&tt=1"
URL_FT_results = URL+"hledani-vysledky?q="
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from selenium import webdriver
from to_import_secret_master import emailPass, comandExecutor

from webdriver_manager.chrome import ChromeDriverManager

def tearDown(self):
  print(self.driver.current_url)
  self.driver.quit()
  #if not self.test_passed:self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)
def acceptConsent(driver):

  generalDriverWaitImplicit(driver)
  time.sleep(3)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    # print(element)
  except NoSuchElementException:
    # print("NOSUCH")
    pass

  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    # print("consent pass")
    pass

#'ondrej.kadoun@fischer.cz'
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

