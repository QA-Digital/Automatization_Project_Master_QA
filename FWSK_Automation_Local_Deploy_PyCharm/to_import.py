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
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False
#URL = "https://www.fischer.sk/"
URL = "https://fischersk.web1.dtweb.cz/"
URL_poznavacky = URL+"poznavacie-zajazdy/okruhy-a-kombinovane"
URL_poznavacky_vikendy = URL+"poznavacie-zajazdy/predlzene-vikendy"
URL_poznavacky_rodiny = URL+"poznavacie-zajazdy/pre-rodiny"
URL_poznavacky_zazitky = URL+"poznavacie-zajazdy/zazitkove"
URL_pobocky = URL+"kontakty/seznam-pobocek"
URL_kluby = URL+"dovolena-animacni-kluby"
#URL_detail = URL+"/recko/zakynthos/laganas/aktypis-deluxe-sk-7?DS=1&D=623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|826|1225|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=724764&MT=3&DI=1980&RT=22&NN=7&RD=2022-09-08&DD=2022-09-01&DP=483&TO=483|1837|2933|3437&MNN=7&TT=1&PID=ZAKDSSK7&DPR=Fischer&TTM=1&TOM=483|1837|2933|3437&DF=2022-09-01|2022-09-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=0&ic1=0"
#URL_detail = URL+"/grecko/rhodos/kolymbia/memphis-beach-7?DS=1&GIATA=5706&D=623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|826|1225|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=110412&MT=5&DI=13&RT=16&NN=7&RD=2022-09-13&DD=2022-09-06&DP=1837&TO=1837&MNN=7&TT=1&PID=RMEMB&DPR=Fischer&TTM=1&DF=2022-09-01|2022-09-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=0&ic1=0#"
#URL_detail = URL+"/turecko/turecka-riviera/alanya/white-gold-hotel?KEY=0x335E59D27D8155FAD8C7A717CB9800BCE41DA5DB&DS=1&GIATA=233527&D=596&HID=722883&MT=5&DI=13&RT=15&NN=7&RD=2022-09-25&DD=2022-09-18&DP=1837&TO=1837&MNN=7&TT=1&PID=AYWGH&DPR=Fischer&TTM=1&DF=2022-09-12|2022-09-30&ERM=0&NNM=7|8|9|18&ac1=2&kc1=0&ic1=0#/prehled"

#URL_SRL = URL+"vysledky-vyhledavani?d=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"

##URL ATCOM
#URL_SRL = URL+"/vysledky-vyhledavani?d=664&tt=1&to=483&dd=2022-11-01&rd=2022-12-31&nn=7|8|9&pf=0&pt=900000&qf=108_1_0|109_1_0|386_1_0&ac1=2&ds=256"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=627|974|712|684|955|596&dd=2023-09-01&ds=0&ic1=1&ka1=10&kc1=1&nn=7|8|9&pf=0&pt=900000&qf=108_1_0|109_1_0|386_1_0&rd=2023-09-30&to=483|1837|2933|3437&tt=1"
URL_SRL = URL + "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-31&ds=0&ifm=0&ilm=0&nn=7|8|9|10|11|12|13&rd=2023-12-31&sc=residential&to=483|1837|2933|3437|4305|2682|4308|4312&tt=1"
#URL_detail = URL + "/arabske-emiraty/arabske-emiraty/dubaj/riu-hotel-dubai?DS=256&GIATA=1226537&D=664&HID=128620&MT=5&NN=7&RD=2022-12-11&DD=2022-12-04&DP=483&TO=483&MNN=7&TT=1&PID=DXB10206&DPR=FISCHER%20ATCOM&TTM=1&DF=2022-12-04|2023-01-04&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0#/prehled"
#URL_detail = URL + "/egypt/egypt-hurghada/hurghada/amc-royal-hotel-a-spa?AC1=1&D=653|819|724&DD=2023-04-18&DP=483&DPR=FISCHER+ATCOM&DS=256&GIATA=228143&HID=139807&IC1=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG90002&RD=2023-04-26&TO=483|1837|2933|3437&acm1=1&df=2023-04-01|2023-04-30&nnm=7|8|9|10|11|12|13&sortby=Departure&tt=1&ttm=1#/terminy-a-ceny"
#URL_detail = URL + "/turecko/turecka-riviera/side-kumkoy/belek/tui-magic-life-belek?D=627|974|712|684|955|596&DD=2023-07-03&DP=1837&DPR=FISCHER+ATCOM&DS=256&GIATA=4717&HID=263&IFM=0&ILM=0&MNN=7&MT=5&NN=7&PID=AYT90031&RD=2023-07-10&TO=1837&df=2023-07-01|2023-08-31&nnm=7|8|9|10|11|12|13|14|15&tt=1&ttm=1#/prehľad"
URL_detail = URL + "/egypt/egypt-hurghada/hurghada/sentido-mamlouk-palace?AC1=2&D=653|819|724&DD=2023-10-01&DP=1837&DPR=FISCHER+SK+ATCOM&DS=256&GIATA=78630&HID=145866&IC1=0&IFM=0&ILM=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG22103&RD=2023-10-08&TO=1837&acm1=2&df=2023-10-01|2023-10-15&nnm=7&tt=1&ttm=1#/prehľad"

URL_covidInfo = URL+"covid-info"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_fmExotika = URL+"first-minute"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhladavania?dd=2023-07-01&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437&tt=1"
URL_FT_results = URL+"hladanie-vysledky?q="


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

