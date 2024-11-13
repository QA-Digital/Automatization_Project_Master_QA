from selenium.webdriver.common.by import By
import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
URL = "https://www.fischer.cz/"
#URL = "https://www.exim.cz/"
#URL = "https://fischer.web1.dtweb.cz/"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(5)
URL1 = URL+ "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2022-12-01&nn=7&rd=2023-01-31&to=4312|4305|2682|4308&tt=1"
URL2 = URL+ "vysledky-vyhledavani?ac1=2&d=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL3 = URL+ "vysledky-vyhledavani?ac1=2&d=1006|1007|1008&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL4 = URL+ "vysledky-vyhledavani?ac1=2&d=664&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL5 = URL+ "vysledky-vyhledavani?ac1=2&d=756&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL6 = URL+ "vysledky-vyhledavani?ac1=2&d=661&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL7 = URL+ "vysledky-vyhledavani?ac1=2&d=1111&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL8 = URL+ "vysledky-vyhledavani?ac1=2&d=790&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL9 = URL+ "vysledky-vyhledavani?ac1=2&d=633|994&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL10 = URL+ "vysledky-vyhledavani?ac1=2&d=634&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL11 = URL+ "vysledky-vyhledavani?ac1=2&d=631&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL12 = URL+ "vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL13 = URL+ "vysledky-vyhledavani?ac1=2&d=638&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"

URL_List = [URL1,URL2, URL3, URL4, URL5,URL6, URL7,URL8,URL9,URL10,URL11,URL12,URL13]
windowHandle = 1
listPosition = 0
for _ in URL_List:
    driver.execute_script("window.open("");")
    driver.switch_to.window(driver.window_handles[windowHandle])
    linkActualUrl = URL_List[listPosition]
    driver.get(URL+"/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
    time.sleep(3)
    driver.get(linkActualUrl)
    windowHandle = windowHandle + 1
    listPosition = listPosition + 1