from selenium.webdriver.common.by import By
from ET.pobocky import *
from ET.Detail_D import *
from ET.Detail_C import *
from ET.FM_D import *
from ET.fulltext_C import *
from ET.groupsearch_D import *
from ET.HP_C import *
from ET.HP_D import *
from ET.LM_D import *
from ET.SDO_D import *
from ET.SRL_C import *
from ET.SRL_D import *
from ET.SRL_results_comparer import *
#import HtmlTestRunner
import HTMLTestRunner

def suite_ET_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_doprava", URL=url))
    suite.addTest(Test_FM("test_FM", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_LM_vyhodneZaj', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_MestaVikendy', URL=url))
    #suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url)) - na webu tento segment není
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_plavby', URL=url))
    suite.addTest(Test_HP_C('test_oblibene_destinace', URL=url))
    suite.addTest(TestHP_D("test_homePage_D", URL=url))
    suite.addTest(TestHP_D("test_HP_LMnabidky", URL=url))
    suite.addTest(TestLM_D("test_HP_LMnabidky", URL=url))
    suite.addTest(TestLM_D("test_LM_rozbaleni_zajezdu", URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check', URL=url))
    suite.addTest(TestSDO_D('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))

    return suite

def suite2():
    suite = unittest.TestSuite()

    suite.addTest(TestDetailHotelu_D("test_detail_D"))
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
    web_brand = "ET"
    runner_tests_generalized(suite_ET_full, web_brand, "hotifx", URL, "qa.digital@dertouristik.cz")
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)