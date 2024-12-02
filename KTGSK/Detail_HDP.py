from EW.to_import import acceptConsent,  setUp, tearDown,URL_local, URL_detail_HDP
import time
import unittest
from helpers.helper import *


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
