from FW.to_import import print_lock
import time
from FW.to_import import print_lock
from FW.pobocky import *
from FW.Detail_D import *
from FW.Detail_C import *
from FW.DetskeKluby_D import *
from FW.dovolena_D import *
from FW.FM_D import *
from FW.fulltext_C import *
from FW.groupsearch_D import *
from FW.HP_D import *
from FW.LM_D import *
from FW.poznavacky import *
from FW.SDO_C import *
from FW.SRL_C import *
from FW.SRL_D import *
from FW.HP_C import *
#import HtmlTestRunner
#import HTMLTestRunner   as   HtmlTestRunner  ##at office PC gotta be set up like that (???)
from FW.SRL_results_comparer import *
from FW.darkove_poukazy import *

def suite_FW_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url))
    suite.addTest(TestDovolena_D("test_dovolena_D", URL=url))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))
    suite.addTest(TestHP_D("test_homePage_D", URL=url))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url))
    suite.addTest(TestSDO_C('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    # suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch', URL=url))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    ############################
    ## Test branch
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_C', URL=url))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_C', URL=url)) ## Experiences are no longer on the web, tests always fail
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url))  ###
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url))
    # suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze', URL=url))
    suite.addTest(TestSDO_C('test_SDO_zlutak_to_SRL_R', URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check', URL=url))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky', URL=url))

    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase', URL=url))
    return suite

def suite_FW_full2(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    return suite

def suite_HP_bannery():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(TestDetskeKluby_D("test_kluby_D"))
    suite.addTest(TestSDO_C('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    return suite

def SRL_suite_full():
    suite = unittest.TestSuite()
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    return suite

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
   # runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "FISCHER"
    version = "FW-EW release 2024-07-23"
    runner_tests_generalized(suite_FW_full, web_brand, version, URL, "qa.digital@dertouristik.cz")

    #runner_tests_generalized(SRL_suite_full, web_brand, version, URL)
    #runner_tests_generalized(suite2, web_brand, version, URL)