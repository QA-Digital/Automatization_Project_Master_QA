from selenium.webdriver.common.by import By
#zlutak to srl

# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakReckoDestinaceXpath))).click()
#
#
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakPokracovatButtonXpath))).click()
# time.sleep(1.5)
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakPokracovatButtonXpathStep2))).click()
#
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakLetniPrazdninyXpath))).click()
# time.sleep(1)
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakPokracovatButtonXpathStep3))).click()
#
#
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakObsazenost2plus1Xpath))).click()
#
# time.sleep(1)
# wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, HPzlutakPotvrditAvyhledatXpath))).click()
# time.sleep(1)





#####zajimavy mista pic check

#obrazekZajimavaMistaXpath = "//*[@class='w-full relative pt-[60%]']"
#obrazekZajimavaMistaXpath = "//*[@class='absolute inset-0 object-cover w-full h-full']"
obrazekZajimavaMistaXpath ="//*[@class='shadow-lg transition-shadow rounded-md overflow-hidden flex flex-col justify-between no-underline text-inherit hover:shadow-[0_7px_20px_0px_rgba(0,0,0,0.16)]']"
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent


URL = "https://www.fischer.cz/arabske-emiraty/arabske-emiraty/dubaj/grand-hyatt-dubai#/zajimava-mista"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)

time.sleep(5)

acceptConsent(driver)
y=0
for _ in driver.find_elements(By.XPATH, obrazekZajimavaMistaXpath):
    print(driver.find_elements(By.XPATH, obrazekZajimavaMistaXpath)[y].is_displayed())
    y=y+1

time.sleep(20)


