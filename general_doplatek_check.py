from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from ET.to_import import acceptConsent

Rekapitulace_ZaplatitNyniXpath = "//*[@class='box box--invisible forDesktop']//*[@class='list-item']/a"

Doplatek_ZaplatitButtonXpath = "//*[@class='f_button f_button--important']"
Doplatek_AmountToPayBoxXpath = "//*[@name='amount']"
Doplatek_CanceledStatusBackToPaymentXpath = "//*[@class='fshr-paragraph--centered']/a"


PaymentGateway_CSOBczCardPaymentBackToShopXpath = "//*[@class='button-with-icon button-cancel']"
PaymentGateway_CSOBczCardPaymentTotalPrice = "//*[@class='total-price']"  ##result = 1234,00 CZK
                                                                            ##vzit jen prvni 4cislice?
#URL = "https://www.eximtours.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=588b8483-2eae-48d4-bf96-04b0fa0edba6"
#URL = "https://kartagohu.stg.dtweb.cz/megrendeles/megrendeles-reszletei?hash=ff56d191-863d-4397-a41e-042f50f643b5"
#URL = "https://kartagohu.web3.dtweb.cz/megrendeles/megrendeles-reszletei?hash=4c2c5a0c-431b-457f-b4f8-cbe6fad5b87c"
#URL = "https://kartagohu.web1.dtweb.cz/megrendeles/megrendeles-reszletei?hash=76e1a8a2-c872-462a-853f-fea18bb6ad4e"
#URL = "https://kartagosk.web3.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=1e0aaf8e-3902-4fbf-8d22-792ee324acca"
#URL = "https://exim.web13.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=b0520f5d-ba3b-418c-8a4a-ffb754baa225"
#URL = "https://kartagohu.stg.dtweb.cz/megrendeles/megrendeles-reszletei?hash=bf1faa27-c99b-41ec-9969-84150ab0ab44"
#URL = "https://kartagosk.web1.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=83ca2369-3cb8-462d-8af4-dace48c2c2fc"
#URL = "https://exim.web11.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=2adcc106-e654-4048-9133-4950ad940949"
#URL = "https://exim.web12.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=e0a556d3-9f16-4cbb-b600-ac6a52641366"
#URL = "https://exim.web13.dtweb.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=a2f3526d-9f2b-4a03-b43c-4f136e59b8a0"
URL = "https://kartagohu.web3.dtweb.cz/megrendeles/potdij-belepes?hash=fb9b150e-d092-40fe-b7a2-4831b48b45a0"
driver = webdriver.Chrome(ChromeDriverManager().install())
amountToPay = "965"
def rekapitulace_proklik_doplatek(driver, URL_rekapitulace):


    driver.maximize_window()
    driver.get(URL_rekapitulace)
    time.sleep(2)
    acceptConsent(driver)
    driver.find_element(By.XPATH, Rekapitulace_ZaplatitNyniXpath).click()
##after execution of above im at doplatek

rekapitulace_proklik_doplatek(driver, URL)
time.sleep(5)
Doplatek_AmountToPayBoxElement = driver.find_element(By.XPATH, Doplatek_AmountToPayBoxXpath)
Doplatek_AmountToPayBoxElement.clear()
time.sleep(0.5)
Doplatek_AmountToPayBoxElement.send_keys(amountToPay)
time.sleep(2)
driver.find_element(By.XPATH, Doplatek_ZaplatitButtonXpath).click()
time.sleep(3)


driver.find_element(By.XPATH, PaymentGateway_CSOBczCardPaymentBackToShopXpath).click()
time.sleep(3)

driver.find_element(By.XPATH, Doplatek_CanceledStatusBackToPaymentXpath).click()