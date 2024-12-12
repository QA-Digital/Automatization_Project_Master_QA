from FW.to_import import acceptConsent,  setUp, tearDown,URL_local, URL_detail_HDP, URL_detail_HDP_no_parameters
import time
import unittest
from helpers.helper import *
from selenium.webdriver.common.action_chains import ActionChains


filterStartXpath = "//*[@id='hotelDetailFilterStart']"
placeXpath = "//*[@id='hotelDetailPlace']"
sedivkaXpath = "//*[@class='w-full lg:w-[376px] shrink-0 sticky bottom-0']"
roomSelectAvailableChoiceXpath = "//*[@class='flex justify-between mx-4 mb-4 @lg:m-0 mt-4 gap-4 items-start']"

businessFlightBoxXpath = "//*[@id='hotelDetailChooseFlight']//*[@class='border border-1 rounded-[--abnb-roundedLg] @lg:p-4 transition-all flex flex-col gap-y-4 cursor-pointer border-yellow-700']"


vyprodanoSedivkaString = "Žádný dostupný termín   Litujeme! Pro tento termín nemáme žádný zájezd. Prosím, vyberte si zájezd v některém z dalších termínů. Vybrat jiný hotel"
vyprodanoSedivkaXpath = "//div[@class='whitespace-nowrap'][normalize-space()='Vybrat jiný hotel']"
class TestDetailHotelu_HDP(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName, URL=None, run_number=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL
        self.run_number = run_number

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HDP_change_flight_change_meal_gg(self):
        ## viz task https://dtee.atlassian.net/browse/FW-4463

        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_HDP}"
        self.driver.get(URL_detail_lp)
        time.sleep(3.33)
        acceptConsent(self.driver)
        time.sleep(4)

        businessFlightElement = self.driver.find_element(By.XPATH, businessFlightBoxXpath)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", businessFlightElement)
        time.sleep(2)
        businessFlightElement.click()

        Helpers.detail_HDP_display_check(self.driver, vyprodanoSedivkaXpath, self.logger)

        roomSelectAvailableChoiceElement = self.driver.find_elements(By.XPATH, roomSelectAvailableChoiceXpath)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
                                   roomSelectAvailableChoiceElement[1])
        time.sleep(3)
        roomSelectAvailableChoiceElement[1].click()

        time.sleep(10)
        Helpers.detail_HDP_display_check(self.driver, vyprodanoSedivkaXpath, self.logger)

    def test_HDP_URL_no_parameters(self):
        self.driver.maximize_window()
        URL_detail_nopara = f"{self.URL}{URL_detail_HDP_no_parameters}"
        self.driver.get(URL_detail_nopara)
        time.sleep(3.33)
        acceptConsent(self.driver)
        time.sleep(4)
        Helpers.detail_HDP_display_check(self.driver, vyprodanoSedivkaXpath, self.logger)

