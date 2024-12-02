from selenium.webdriver.common.by import By
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
time.sleep(15)
gridItemXpath = "//*[@class='f_tileGrid-item']/a"
gridItemElements = driver.find_elements(By.XPATH, gridItemXpath)
#print(URL_poznavaciho_hotelu)
linksToCheck_List = []
pozice=0
for _ in gridItemElements:
    odkazLink = gridItemElements[pozice].get_attribute("href")
    linksToCheck_List.append(odkazLink)
    print(odkazLink)
    pozice = pozice+1
print(linksToCheck_List)


def generalized_list_of_url_checker(inputListOfURLStoCheck):
    poziceURLvListu = 0
    test_passed = True
    for _ in inputListOfURLStoCheck:
        requestURL = inputListOfURLStoCheck[poziceURLvListu]
        response = requests.get((requestURL), timeout=5)
        #print(requestURL)
        print(response.status_code)
        #print("-------------")
        if response.status_code != 200:
            #print("FAILURE")
            print(response.status_code)
            print(requestURL)
            test_passed = False
        poziceURLvListu = poziceURLvListu+1

    if test_passed == False:
        assert 1 == 2

generalized_list_of_url_checker(linksToCheck_List)



