from selenium.webdriver.common.by import By
from EXPL.pobocky import *
from EXPL.Detail_D import *
from EXPL.Detail_C import *
from EXPL.fulltext_C import *
from EXPL.groupsearch_D import *
from EXPL.HP_C import *
from EXPL.HP_D import *
from EXPL.LM_D import *
from EXPL.SDO_D import *
from EXPL.SRL_C import *
from EXPL.SRL_D import *
#import HtmlTestRunner
import HTMLTestRunner
from EXPL.SRL_results_comparer import *

def suite_EXPL_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))

    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url))
    #suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url)) #nefunguje a možná ani nebude, info od Vojty
    #suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url)) #nefunguje a možná ani nebude, info od Vojty

    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))

    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))

    suite.addTest(TestHP_D("test_homePage_D", URL=url))

    suite.addTest(TestLM_D("test_LM_D", URL=url))

    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url))

    suite.addTest(TestSDO_D('test_SDO_D', URL=url))
    suite.addTest(TestSDO_D('test_SDO_NejHotely', URL=url))

    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url)) #nefunguje a možná ani nebude, info od Vojty
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url)) #nefunguje a možná ani nebude, info od Vojty
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))

    suite.addTest(TestSRL_D('test_SRL_D', URL=url))

    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url))  ###
    suite.addTest(Test_HP_C('test_HP_slider_NasiKlienci', URL=url))  ###
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    suite.addTest(Test_HP_C('test_HP_vyletyPoznan', URL=url))
    suite.addTest(Test_HP_C('test_HP_vyletyWroclaw', URL=url))
    suite.addTest(Test_HP_C('test_HP_vyletyGdansk', URL=url))
    suite.addTest(Test_HP_C('test_letoDestination_D', URL=url))
    suite.addTest(Test_HP_C('test_zimaDestination_D', URL=url))
    suite.addTest(Test_HP_C('test_egzotykaDestination_D', URL=url))
    suite.addTest(Test_HP_C('test_allInclusiveDestination_D', URL=url))

    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url))

    return suite


def suite2():
    suite = unittest.TestSuite()

    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

def suite3():
    suite = unittest.TestSuite()

    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(TestPobocky_C('test_pobocky_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))

    return suite

def suite4():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
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
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "EXIM PL"
    version = "EXPL-ET release 2024-07-22"
    runner_tests_generalized(suite_EXPL_full, web_brand, version, URL, "qa.digital@dertouristik.cz")
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)