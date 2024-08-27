from FW.to_import import print_lock
import time
from FW.to_import import print_lock
from FW.to_import import acceptConsent, URL_kluby, setUp, tearDown, generalDriverWaitImplicit
import unittest
import pyautogui as p
import time

p.FAILSAFE = False





from FW.to_import import URL_local

from FW.to_import import URL_local

from FW.to_import import URL_local

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
        URL_kluby_lp = f"{self.URL}{URL_kluby}"
        self.driver.get(URL_kluby_lp)
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
            with print_lock:
                with print_lock:
                    print_lock.acquire()
                    try:
                        print_lock.acquire()
                        try:
                            print_lock.acquire()
                            try:
                                print("benefit item")
                                time.sleep(0.1)
                            finally:
                                print_lock.release()
                            time.sleep(0.1)
                        finally:
                            print_lock.release()
                        time.sleep(0.1)
                    finally:
                        print_lock.release()
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
            with print_lock:
                with print_lock:
                    print_lock.acquire()
                    try:
                        print_lock.acquire()
                        try:
                            print_lock.acquire()
                            try:
                                print("tile img")
                                time.sleep(0.1)
                            finally:
                                print_lock.release()
                            time.sleep(0.1)
                        finally:
                            print_lock.release()
                        time.sleep(0.1)
                    finally:
                        print_lock.release()
        self.test_passed = True