
from KTGSK.pobocky import *
from KTGSK.Detail_D import *
from KTGSK.Detail_C import *
from KTGSK.DetskeKluby_D import *
from KTGSK.FM_D import *
from KTGSK.fulltext_C import *
from KTGSK.groupsearch_D import *
from KTGSK.HP_D import *
from KTGSK.LM_D import *
from KTGSK.poznavacky import *
from KTGSK.SDO_D import *
from KTGSK.SRL_C import *
from KTGSK.SRL_D import *
from KTGSK.HP_C import *
from KTGSK.SRL_results_comparer import *

#import HTMLTestRunner
import HtmlTestRunner
import HTMLTestRunner   as   HtmlTestRunner
def suite_KTGSK_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url))
    suite.addTest(TestFM_D("test_FM_D", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))
    suite.addTest(TestHP_D("test_homePage_D", URL=url))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url))
    suite.addTest(TestPobocky_D('test_pobocky_D', URL=url))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url))
    suite.addTest(TestSDO_D('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch', URL=url))
    suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch', URL=url))
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))
    return suite


def suite2():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    web_brand = "KARTAGO SK"
    version = "KTGSK- FWSK release 2024-07-01"
    outfile = open("results.html", "w")

    runner_tests_generalized(suite_KTGSK_full, web_brand, version, URL, "qa.digital@dertouristik.cz")

    #runner.run(suite2())