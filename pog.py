from selenium.webdriver.common.by import By
import time

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from EW.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
#HPtopNabidkaXpath = "//*[@class='page-widget js-ajaxPlaceholder--widget fshr-widget f_tileGrid-item']"
HPtopNabidkaXpath="//*[@class='js-ajaxPlaceholder--widgetContent']/a"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)
time.sleep(
            2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
acceptConsent(driver)
time.sleep(10)

links_to_check = []
links_list_counter = 0
for _ in range(7):
#for _ in HPtopNabidkaXpath:
        #topNabidkaElementHref = driver.find_elements(By.XPATH, topNabidkaLinkXpath[links_list_counter]).get_attribute("href")
        topNabidkaElementHref = driver.find_elements(By.XPATH, HPtopNabidkaXpath)
        topNabidkaLinkText = topNabidkaElementHref[links_list_counter].get_attribute("href")
        links_to_check.append(topNabidkaLinkText )
        links_list_counter = links_list_counter+1
        #print(topNabidkaLinkText )
        #print(links_to_check)

#print(links_to_check)

links_list_counter = 0
for _ in links_to_check:

        response = requests.get(links_to_check[links_list_counter])

        if response.status_code != 200:
                print(links_to_check[links_list_counter])
                print(response.status_code)
                links_list_counter = links_list_counter + 1

        else:
                pass

        assert response.status_code == 200
        links_list_counter = links_list_counter + 1

        ##TODO: assert na list equal to, printovacka na ten list a list URL z top nabidky