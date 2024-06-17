import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
URL = "https://exim.cz/poznavaci-zajezdy"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(5)
URL1 ="https://www.eximtours.cz/vysledky-vyhledavani?d=211764|63241|63360|74459|74460|63284|74464|63350|63354|74465|63213|63226|63267|63349&tt=1&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-28&nn=7&ac1=2"
URL2 = "https://www.eximtours.cz/vysledky-vyhledavani?d=64419|64420|64425&tt=1&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-28&nn=7&ac1=2"
URL3 ="https://www.eximtours.cz/vysledky-vyhledavani?d=64087|64094|64095|64089|64090|64091|64086|64092&tt=1&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-28&nn=7&ac1=2"
URL4 ="https://www.eximtours.cz/vysledky-vyhledavani?d=63738|63824|63823&tt=1&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-28&nn=7&ac1=2"
URL5="https://www.eximtours.cz/vysledky-vyhledavani?d=63865|63862|63863|63866|63864&tt=1&to=4312|4305|2682|4308&dd=2023-02-01&rd=2023-03-28&nn=7&ac1=2"
URL_List = [URL1,URL2, URL3, URL4, URL5 ]
windowHandle = 1
listPosition = 0
for _ in URL_List:
    driver.execute_script("window.open("");")
    driver.switch_to.window(driver.window_handles[windowHandle])
    linkActualUrl = URL_List[listPosition]
    driver.get(linkActualUrl)
    windowHandle = windowHandle + 1
    listPosition = listPosition +1