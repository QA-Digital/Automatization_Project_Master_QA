from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from BILLA.to_import import acceptConsent, URL_groupsearch, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC
emptyImgInTeaserDestinationXpath = """//*[@style='background-image: url("https://cdn.fischer.cz/Images/000000/1200x0.jpg");']"""
empty1 = ''
teaserItemsXpath = "//*[@class='c_tile-category']"
destinationsHighlightXpath = "//*[@class='c_title large center']"

def groupSearch_D(self, driver):
    driver.implicitly_wait(100)
    teaserItems = driver.find_elements(By.XPATH, teaserItemsXpath)
    wait = WebDriverWait(self.driver, 150)
    wait.until(EC.visibility_of(teaserItems[0]))
    try:
        for WebElement in teaserItems:
            ##print(len(teaserItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                ##print("Else")
                ##emailfunciton



    except NoSuchElementException:
        pass
        ##print("no such")
        ##email fnction

    assert teaserItems[0].is_displayed() == True

    driver.implicitly_wait(100)
    destinationsHL = driver.find_elements(By.XPATH, destinationsHighlightXpath)
    try:
        for WebElement in destinationsHL:
            ##print(len(srlItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                print("Else")
    except NoSuchElementException:
        pass


    except NoSuchElementException:
        pass
        print("no such")
    assert destinationsHL[0].is_displayed() == True

    emptyImgsList = []
    emptyImgsListCounter = 0
    emptyImgs = driver.find_elements(By.XPATH, emptyImgInTeaserDestinationXpath)
    try:
        emptyImgs = driver.find_elements(By.XPATH, emptyImgInTeaserDestinationXpath)
        for WebElement in emptyImgs:
            emptyImgsList.append(emptyImgs[emptyImgsListCounter].text)
            print(emptyImgs[emptyImgsListCounter].text)
            emptyImgsListCounter = emptyImgsListCounter + 1

    except NoSuchElementException:
        pass

    print("následující destinace mají prázdný teaser obrazek")
    print(emptyImgsList)


from BILLA.to_import import URL_local
class Test_Groupsearch_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()

        URL_groupsearch_lp = f"{self.URL}{URL_groupsearch}"
        self.driver.get(URL_groupsearch_lp)

        acceptConsent(self.driver)

        groupSearch_D(self, driver)

        self.test_passed = True