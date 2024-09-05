from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import acceptConsent, setUp, tearDown
import time
import unittest
from selenium.webdriver import ActionChains
import requests

from FW.to_import import URL_local

class TestDovolena_D(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_dovolena_D(self):
        wait = WebDriverWait(self.driver, 150000)

        self.driver.get(self.URL)
        self.driver.maximize_window()

        time.sleep(1.5)
        acceptConsent(self.driver)

        dovolena_menu_item_anchor = self.driver.find_element_by_xpath('//a[@href="/dovolena"]')

        if dovolena_menu_item_anchor.is_displayed():

            self.logger.info("Položka menu existuje")
            hover = ActionChains(self.driver).move_to_element(dovolena_menu_item_anchor)
            hover.perform()
            time.sleep(1)

            dovolena_popup_div = self.driver.find_element_by_xpath("//a[@href='/dovolena']/following-sibling::div")
            all_links_within_popup = dovolena_popup_div.find_elements_by_css_selector('a[data-v-2ce750c8]')

            x = 0

            for _ in all_links_within_popup:

                href_value = all_links_within_popup[x].get_attribute('href')

                try:
                    response = requests.get(href_value)
                    self.logger.info(href_value + " " + str(response.status_code))
                except requests.exceptions.RequestException as e:
                    self.logger.info(href_value + " Error:", e)
                    pass
                assert response.status_code == 200

            time.sleep(1)
        else:
            self.logger.info("Položka menu neexistuje")

        self.test_passed = True

