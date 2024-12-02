from selenium.webdriver.common.by import By
from FW.starter_local import *

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "FISCHER"
    version = "pouze   u nas"
    runner_tests_generalized(suite_FW_full, web_brand, version, URL)