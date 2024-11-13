from selenium.webdriver.common.by import By
import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from EW.to_import import acceptConsent


URL = "https://eximpl.stg.dtweb.cz/"
xpath123 = '//a/@href'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)

acceptConsent(driver)
time.sleep(10)
from lxml import etree

links_to_check = []
links_list_counter = 0
#for _ in range(7):
response = requests.get(URL)
html = response.content

# Parse the HTML content
tree = etree.HTML(html)

# Use XPath to get all link URLs
link_urls = tree.xpath("//a/@href")
print(link_urls)
# for _ in driver.find_elements(By.XPATH, xpath123):
#         #topNabidkaElementHref = driver.find_elements(By.XPATH, topNabidkaLinkXpath[links_list_counter]).get_attribute("href")
#         ElementHref = driver.find_elements(By.XPATH, xpath123)
#         topNabidkaLinkText = ElementHref[links_list_counter].get_attribute("href")
#         links_to_check.append(topNabidkaLinkText )
#         links_list_counter = links_list_counter+1
#         #print(topNabidkaLinkText )
#         #print(links_to_check)


#print(links_to_check)

links_list_counter = 0
#for _ in links_to_check:
for _ in link_urls:
        try:
            response = requests.get(links_to_check[links_list_counter])
        except Exception as e:
            print(type(e))


        if response.status_code != 200:
                print(link_urls[links_list_counter])
                print(response.status_code)
                links_list_counter = links_list_counter + 1

        else:
                print(link_urls[links_list_counter])
                print(response.status_code)
                links_list_counter = links_list_counter + 1
                pass

        #assert response.status_code == 200
        links_list_counter = links_list_counter + 1