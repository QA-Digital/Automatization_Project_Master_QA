from KTGHU.pobocky import *
from KTGHU.Detail_D import *
from KTGHU.Detail_C import *
from KTGHU.FM_D import *
from KTGHU.fulltext_C import *
from KTGHU.groupsearch_D import *
from KTGHU.HP_D import *
from KTGHU.LM_D import *
from KTGHU.SDO_D import *
from KTGHU.SRL_C import *
from KTGHU.SRL_D import *
from KTGHU.HP_C import *
from KTGHU.SRL_results_comparer import *

import HTMLTestRunner
#import HtmlTestRunner

def suite_KTGHU_full():
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    #suite.addTest(TestFM_D("test_FM_D")) ##ATM tam nic neni neni smysl to poustest
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_lM_isDisplayed"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
   # suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))
    return suite

def suite_SRL_C():
    suite = unittest.TestSuite()
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    return suite

from starter_master_browserstack import  runner_tests_generalized

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    outfile = open("results.html", "w")
    web_brand = "KTGHU"
    version = "KTGHU release 2024-04-29"
    runner_tests_generalized(suite_KTGHU_full, web_brand, version, URL, "qa.digital@dertouristik.cz")

    #runner_tests_generalized(suite_SRL_C, web_brand, version, URL)
    #runner.run(suite2())