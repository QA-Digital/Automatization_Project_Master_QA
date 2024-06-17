import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://www.fischer.cz/spanelsko/fuerteventura/morro-jable/blue-sea-jandia-luz?AC1=2&D=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&DD=2023-02-19&DP=4312&DPR=FISCHER+ATCOM&DS=256&GIATA=32289&HID=1629&IC1=0&KC1=0&MNN=7&MT=6&NN=7&PID=FUE90003&RD=2023-02-26&TO=4312|4305|2682|4308&acm1=2&df=2023-02-01|2023-03-31&nnm=7|8|9|10|11|12|13&tom=4312|4305|2682|4308&tt=1&ttm=1#/terminy-a-ceny"
##goal to sumup cenu dospelych v rozpisu v terminech a porovnat v prezentované ceně
#viz atcom bugy v rozpadě ceny
driver.get(URL)

cestujiciXpath = "//*[@class='f_table']//*[@class='f_table-body']//*[@class='f_table-cell']"
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)
terminyXpath = "//*[@class='f_termList-header']"
terminyScrollInto = driver.find_element_by_xpath(terminyXpath)
driver.execute_script("arguments[0].scrollIntoView();", terminyScrollInto)
time.sleep(4)
#driver.click(terminyScrollInto)
terminyScrollInto.click()
cestujiciElements = driver.find_elements_by_xpath(cestujiciXpath)
cestujiciElement = driver.find_element_by_xpath(cestujiciXpath)
# cestujiciElementText = driver.find_elements_by_xpath(cestujiciXpath).text
y=1
cestujiciSinglePriceList = []
for _ in cestujiciElements:
    cestujiciElementText = driver.find_elements_by_xpath(cestujiciXpath)[y].text
    cestujiciSinglePrice = cestujiciElementText[y]
    print(cestujiciSinglePrice)

    cestujiciSinglePriceList.append(cestujiciSinglePrice)
    print(cestujiciSinglePriceList)
    print("y je " + str(y))
    y = y + 2
# print(str(cestujiciElement.text))
# print("priting 1St")
# print(cestujiciElement.text)
# print(cestujiciElementText)
# print(cestujiciElements[0].text)
# print(cestujiciElements[1].text)
time.sleep(3)

