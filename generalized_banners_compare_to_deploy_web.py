from selenium.webdriver.common.by import By
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
    """
    This function compares the number of search results (from an H1 element) for banners between the public production website
    and the deployed version of the website. It iterates through banners on both versions, opens them, extracts the H1 text,
    and checks if they match.
    """

    # XPath locator for the H1 element displaying the number of search results
    SRL_H1textPocetNalezenychZajezduXpath = "//h1"

    # Start by opening the production public website
    driver.maximize_window()
    driver.get(URL_prod_public)
    time.sleep(2)  # Allow the page to load
    acceptConsent(driver)  # Handle any consent pop-up

    # Find all banner elements on the production site
    banneryAll = driver.find_elements(By.XPATH, banneryXpath)

    # Lists to store banner information from the production site
    pocetNalezenychZajezduElementList_PROD = []
    bannerLinksList_PROD = []

    for index, banner in enumerate(banneryAll):
        # Extract the link from the banner
        bannerHref = banner.get_attribute("href")

        # Open the link in a new tab
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)

        try:
            # Try to find the H1 element and extract its text
            pocetNalezenychZajezduElement_PROD = driver.find_element(By.XPATH,
                                                                     SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        except NoSuchElementException:
            # If the H1 element is not found, append '0' instead of failing
            pocetNalezenychZajezduElement_PROD = '0'

        pocetNalezenychZajezduElementList_PROD.append(pocetNalezenychZajezduElement_PROD)
        bannerLinksList_PROD.append(driver.current_url)

        driver.close()  # Close the tab
        driver.switch_to.window(driver.window_handles[0])  # Switch back to the main window
        time.sleep(0.5)  # Small delay before proceeding

    # Now, repeat the process for the deployed version of the website
    driver.get(URL_deploying_web)
    time.sleep(5)  # Allow the page to load

    pocetNalezenychZajezduElementList_DEPLOY = []
    bannerLinksList_DEPLOY = []

    banneryAll = driver.find_elements(By.XPATH, banneryXpath)

    for index, banner in enumerate(banneryAll):
        # Extract the banner link
        bannerHref = banner.get_attribute("href")

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)

        try:
            # Try to find the H1 element and extract its text
            pocetNalezenychZajezduElement_DEPLOY = driver.find_element(By.XPATH,
                                                                       SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        except NoSuchElementException:
            # If the H1 element is not found, append '0'
            pocetNalezenychZajezduElement_DEPLOY = '0'

        pocetNalezenychZajezduElementList_DEPLOY.append(pocetNalezenychZajezduElement_DEPLOY)
        bannerLinksList_DEPLOY.append(driver.current_url)

        driver.close()  # Close the tab
        driver.switch_to.window(driver.window_handles[0])  # Switch back to the main window
        time.sleep(0.5)  # Small delay before proceeding

        # Compare the extracted H1 text between production and deployed versions
        if pocetNalezenychZajezduElementList_PROD[index] != pocetNalezenychZajezduElementList_DEPLOY[index]:
            print("PROBLEM BANNERS")
            print(pocetNalezenychZajezduElementList_PROD[index] + "  ||| VS |||  " +
                  pocetNalezenychZajezduElementList_DEPLOY[index])
            print(bannerLinksList_PROD[index])
            print(bannerLinksList_DEPLOY[index])
            print("----------------------------------------")

    # Print results from both versions
    print("------------------------------------------")
    print("LIST FROM PUBLIC WWW PRODUCTION " + URL_prod_public)
    print(pocetNalezenychZajezduElementList_PROD)
    print("------------------------------------------")
    print("LIST FROM DEPLOYING WEB " + URL_deploying_web)
    print(pocetNalezenychZajezduElementList_DEPLOY)

    # Assert that the lists match
    assert pocetNalezenychZajezduElementList_DEPLOY == pocetNalezenychZajezduElementList_PROD

    print("------------------------------------------")
    print("Banners are GOOD, TEST OK " + URL_prod_public + " VS " + URL_deploying_web)

#banner_check_public_prod_VS_deployed_web(driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)