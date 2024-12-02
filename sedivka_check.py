from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent
from selenium.common.exceptions import NoSuchElementException

# sedivkaXpathFw = "//*[@class='f_box h-full flex flex-col']"
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# URL = "https://www.fischer.cz/poznavaci-zajezdy/okruzni-a-kombinovane"
# driver.get(URL)
# time.sleep(1)
# driver.maximize_window()
# acceptConsent(driver)
# time.sleep(10)
# kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"
# element3=driver.find_elements(By.XPATH, kostkaPoznavackaXpath)[6]
# driver.execute_script("arguments[0].scrollIntoView();", element3)
# time.sleep(2)
# element3.click()
def sedivka_check_assert(driver,sedivkaXpath):
    try:
        sedivka = driver.find_element(By.XPATH, sedivkaXpath)
        print(sedivka.is_displayed())
        assert 1==1
        return
    except NoSuchElementException:
        print("sedivka nenalezena")
        assert 1==2
    return

# sedivka = driver.find_element(By.XPATH, sedivkaXpathFw)
# print(sedivka.is_displayed())