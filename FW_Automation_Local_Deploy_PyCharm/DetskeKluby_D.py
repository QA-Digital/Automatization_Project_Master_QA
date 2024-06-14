from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_kluby, setUp, tearDown, generalDriverWaitImplicit
import unittest
import pyautogui as p
import time

p.FAILSAFE = False





from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local

from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local

from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local

class TestDetskeKluby_D(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL


    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL


    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_kluby_D(self):
        self.driver.get(URL_kluby)
        acceptConsent(self.driver)
        self.driver.maximize_window()
        generalDriverWaitImplicit(self.driver)
        time.sleep(5)
        benefitItem = self.driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        assert benefitItem[0].is_displayed() == True
        a=0
        for _ in benefitItem:
            benefitItemDisplay = benefitItem[a].is_displayed()
            a=a+1
            assert benefitItemDisplay == True
            print("benefit item")
        #p.press("pagedown", presses=3)
        generalDriverWaitImplicit(self.driver)

        gridContainer = self.driver.find_elements_by_xpath("//*[@class='grd-container']")
        self.driver.execute_script("arguments[0].scrollIntoView();", gridContainer[0])
        b=0
        assert gridContainer[0].is_displayed() == True
        for _ in gridContainer:
            gridContainerDisplay = gridContainer[b].is_displayed()
            assert  gridContainerDisplay == True
            b=b+1
            print ("grind container")
        #p.press("pagedown", presses=2)
        tileImg = self.driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        kartyHoteluBottom = self.driver.find_element_by_xpath("//*[@class='f_tile f_tile--tour']")
        self.driver.execute_script("arguments[0].scrollIntoView();", kartyHoteluBottom)
        c=0
        assert tileImg[0].is_displayed() == True
        for _ in tileImg:
            tileImgDisplay = tileImg[c].is_displayed()
            assert tileImgDisplay == True
            c=c+1
            print("tile img")

        self.test_passed = True