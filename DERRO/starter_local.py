from DERRO.pobocky import *
from DERRO.Detail_D import *
from DERRO.Detail_C import *
from DERRO.fulltext_C import *
from DERRO.groupsearch_D import *
from DERRO.HP_C import *
from DERRO.HP_D import *
from DERRO.LM_D import *
from DERRO.SDO_D import *
from DERRO.SRL_C import *
from DERRO.SRL_D import *
#import HtmlTestRunner
import HTMLTestRunner
from DERRO.SRL_results_comparer import *

def suite_DERRO_full():
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D"))

    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap"))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive"))

    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))

    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))

    #suite.addTest(TestHP_D("test_homePage_D"))

    suite.addTest(TestLM_D("test_lM_isDisplayed"))

    suite.addTest(TestPobocky_C('test_pobocky_D'))

    suite.addTest(TestSDO_D('test_SDO_D'))

    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))

    suite.addTest(TestSRL_D('test_SRL_D'))

    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt'))  ###
    #suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))  ###
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))  ###
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    #suite.addTest(Test_HP_C('test_HP_nabidka_Podroze_marzen'))
    suite.addTest(Test_HP_C('test_HP_vyletyDubai'))
    suite.addTest(Test_HP_C('test_HP_vyletyEgipt'))
    suite.addTest(Test_HP_C('test_HP_vyletyThajsko'))
    suite.addTest(Test_HP_C('test_HP_top_hotely'))

    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))

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
    web_brand = "DERRO"
    runner_tests_generalized(suite_DERRO_full, web_brand, "hotifx", URL, "qa.digital@dertouristik.cz")
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)