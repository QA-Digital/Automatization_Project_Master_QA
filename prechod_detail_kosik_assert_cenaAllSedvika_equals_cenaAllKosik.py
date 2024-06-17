import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent
from paramaterizace_detail_obsazenost import allPokojeListParameters


driver = webdriver.Chrome(ChromeDriverManager().install())

time.sleep(1)
driver.maximize_window()

#URL_detail = "https://www.fischer.cz/spanelsko/mallorca/alcudia/mariant?DS=256&GIATA=21437&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&HID=21&MT=5&NN=7&DF=2023-10-01|2023-10-31&RD=2023-10-14&DD=2023-10-07&ERM=0&AC1=2&KC1=1&KA1=10&IC1=1&AC2=2&KC2=2&KA2=13|6&IC2=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=PMI14448&DPR=FISCHER%20ATCOM"
sedivkaCenaAllXpath = "//*[@class='f_column-item']//*[@class='f_price']"
mamZajemDetailXpath = "//*[@class='f_section-content'] //*[@class='f_button f_button--important f_set--fullWidth']"
URL_detail_base = "https://www.fischer.cz/spanelsko/mallorca/cala-san-vicente/globales-simar?DS=256&GIATA=89104&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&HID=3482&MT=5&NN=7&DF=2023-10-07|2023-10-14&RD=2023-10-14&DD=2023-10-07&ERM=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7&TT=1&TTM=1&PID=PMI14203&DPR=FISCHER%20ATCOM&ILM=0&IFM=0"

def prechod_detail_kosik_assert_cenaAllSedvika_equals_cenaAllKosik(URL_detail, sedivkaCenaAllXpath, mamZajemDetailXpath):
    ##find cena detail, all
    driver.get(URL_detail)
    time.sleep(5)
    acceptConsent(driver)

    detailSedivkaCenaAll = driver.find_element_by_xpath(sedivkaCenaAllXpath)
    detailSedivkaCenaAllString = detailSedivkaCenaAll.text
    # print("CENA NA DETAILU V SEDIVCE:  ")
    # print(detailSedivkaCenaAllString)

    ##proklik do kosiku
    time.sleep(15)
    mamZajemDetailElement = driver.find_element_by_xpath(mamZajemDetailXpath)
    mamZajemDetailElement.click()

    ##tento locator alokuje 2x elementy ktere se sami sobe rovnaji
    kosikCenaAllXpath = "//*[@class='f_box f_box--price']//*[@class='f_price']"
    kosikCenaAllElement = driver.find_element_by_xpath(kosikCenaAllXpath)
    kosikCenaAllString = kosikCenaAllElement.text
    # print("             ")
    # print("CENA V KOSIKU:")
    # print(kosikCenaAllString)

    if kosikCenaAllString != detailSedivkaCenaAllString:
        print(URL_detail)
        print("             ")
        print("CENA NA DETAILU V SEDIVCE:  ")
        print(detailSedivkaCenaAllString)


        print("             ")
        print("CENA V KOSIKU:")
        print(kosikCenaAllString)
        print ("----------------------------------------------")

    #assert kosikCenaAllString == detailSedivkaCenaAllString

##2 seperat funkce
##1big fnc
##list failed asserts -> print obsazenost


poziceListu = 0
for _ in allPokojeListParameters:

    URL_detail = URL_detail_base + allPokojeListParameters[poziceListu]



    prechod_detail_kosik_assert_cenaAllSedvika_equals_cenaAllKosik(URL_detail, sedivkaCenaAllXpath, mamZajemDetailXpath)
    poziceListu=poziceListu+1