from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from ET.to_import import acceptConsent
#URL_prod_public = "https://www.fischer.cz/"
#URL_deploying_web = "https://fischer.web1.dtweb.cz/"

#URL_prod_public = "https://www.eximtours.cz/"
#URL_deploying_web = "https://exim.web12.dtweb.cz/"

#SRL_H1textPocetNalezenychZajezduXpath = "//h1"


#driver = webdriver.Chrome(ChromeDriverManager().install())
def banner_check_public_prod_VS_deployed_web(driver, URL_prod_public, URL_deploying_web, banneryXpath):
    SRL_H1textPocetNalezenychZajezduXpath = "//h1"


    driver.maximize_window()
    driver.get(URL_prod_public)
    time.sleep(2)
    acceptConsent(driver)

    banneryAll = driver.find_elements_by_xpath(banneryXpath)

    x=0
    pocetNalezenychZajezduElementList_PROD = []
    bannerLinksList_PROD = []
    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        #print(bannerHref)
        x=x+1
        #print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        #time.sleep(10)
        try:
            pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_PROD.append(pocetNalezenychZajezduElement_PROD)
            bannerLinks_PROD = driver.current_url
            bannerLinksList_PROD.append(bannerLinks_PROD)
            #print (bannerLinks_PROD)
        except NoSuchElementException:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    ###deploy web start

    driver.get(URL_deploying_web)
    time.sleep(5)
    x = 0
    pocetNalezenychZajezduElementList_DEPLOY = []
    bannerLinksList_DEPLOY = []
    banneryAll = driver.find_elements_by_xpath(banneryXpath)
    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        #print(bannerHref)

        #print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        try:
            pocetNalezenychZajezduElement_DEPLOY = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_DEPLOY.append(pocetNalezenychZajezduElement_DEPLOY)
            bannerLinks_DEPLOY = driver.current_url
            bannerLinksList_DEPLOY.append(bannerLinks_DEPLOY)

            #print(pocetNalezenychZajezduElement_DEPLOY)
        except NoSuchElementException:
            pass
        driver.close()

        if pocetNalezenychZajezduElementList_PROD[x]==pocetNalezenychZajezduElementList_DEPLOY[x]:

            #print(bannerLinksList_PROD[x])
            #print(bannerLinksList_DEPLOY[x])
            pass
        else:
            print("PROBLEM BANNERS")
            print( pocetNalezenychZajezduElementList_PROD[x] + "  ||| VS |||  " + pocetNalezenychZajezduElementList_DEPLOY[x])
            print(bannerLinksList_PROD[x])
            print(bannerLinksList_DEPLOY[x])
            print("----------------------------------------")

        x = x + 1
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    print("------------------------------------------")
    print("LIST FROM PUBLIC WWW PRODUCTION " + URL_prod_public)
    print( pocetNalezenychZajezduElementList_PROD)
    print("------------------------------------------")
    print("LIST FROM DEPLOYING WEB " + URL_deploying_web)
    print(pocetNalezenychZajezduElementList_DEPLOY)

    assert pocetNalezenychZajezduElementList_DEPLOY == pocetNalezenychZajezduElementList_PROD
    print("------------------------------------------")
    print("Banners are GOOD, TEST OK " + URL_prod_public + " VS " + URL_deploying_web )

    #driver.quit()


#banner_check_public_prod_VS_deployed_web(driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)