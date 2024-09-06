import time

from EW.to_import import acceptConsent, URL_kluby, setUp, tearDown
import unittest
import pyautogui as p
p.FAILSAFE = False



from EW.to_import import URL_local
class TestDetskeKluby_D(unittest.TestCase):
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
        self.driver.maximize_window()
        URL_kluby_lp = f"{self.URL}{URL_kluby}"
        self.driver.get(URL_kluby_lp)
        time.sleep(4)
        acceptConsent(self.driver)

        time.sleep(3)
        benefitItem = self.driver.find_elements_by_xpath("//*[@class='f_benefit-item splide__slide']")

        a=0
        for _ in benefitItem:
            benefitItemDisplay = benefitItem[a].is_displayed()
            a=a+1
            assert benefitItemDisplay == True
            self.logger.info("benefit item")
        assert benefitItem[0].is_displayed() == True

        p.press("pagedown", presses=3)
        gridContainer = self.driver.find_elements_by_xpath("//*[@class='grd-container']")
        b=0

        for _ in gridContainer:
            gridContainerDisplay = gridContainer[b].is_displayed()
            assert  gridContainerDisplay == True
            b=b+1
            print ("grind container")

        assert gridContainer[0].is_displayed() == True
        ##aktualne nejsou karty hotelu
        # p.press("pagedown", presses=2)
        # tileImg = self.driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        # c=0
        #
        # for _ in tileImg:
        #     tileImgDisplay = tileImg[c].is_displayed()
        #     assert tileImgDisplay == True
        #     c=c+1
        #     self.logger.info("tile img")
        # assert tileImg[0].is_displayed() == True


        self.test_passed = True