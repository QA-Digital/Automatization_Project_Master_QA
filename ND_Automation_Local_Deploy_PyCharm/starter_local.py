from ND_Automation_Local_Deploy_PyCharm.pobocky import *
from ND_Automation_Local_Deploy_PyCharm.Detail_D import *
from ND_Automation_Local_Deploy_PyCharm.Detail_C import *
from ND_Automation_Local_Deploy_PyCharm.FM_D import *
from ND_Automation_Local_Deploy_PyCharm.fulltext_C import *
from ND_Automation_Local_Deploy_PyCharm.groupsearch_D import *
from ND_Automation_Local_Deploy_PyCharm.HP_C import *
from ND_Automation_Local_Deploy_PyCharm.HP_D import *
from ND_Automation_Local_Deploy_PyCharm.LM_D import *
from ND_Automation_Local_Deploy_PyCharm.SDO_D import *
from ND_Automation_Local_Deploy_PyCharm.SRL_C import *
from ND_Automation_Local_Deploy_PyCharm.SRL_D import *
from ND_Automation_Local_Deploy_PyCharm.SRL_results_comparer import *
#import HtmlTestRunner
import HTMLTestRunner

def suite_ND_full():
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D_leto"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D_zima"))
    suite.addTest(Test_HP_C('test_HP_bannery_check_leto'))
    suite.addTest(Test_HP_C('test_HP_bannery_check_zima'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt'))
    suite.addTest(Test_HP_C('test_oblibene_destinace'))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_HP_LMnabidky"))
    suite.addTest(TestPobocky_C('test_pobocky_D'))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check'))
    suite.addTest(TestSDO_D('test_SDO_D_leto'))
    suite.addTest(TestSDO_D('test_SDO_D_zima'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_map'))
    suite.addTest(Test_SRL_C_Zima('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))

    return suite

def suite2():
    suite = unittest.TestSuite()

    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(Test_SRL_C_Zima('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C_Zima('test_srl_C'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

def suite3():
    suite = unittest.TestSuite()

    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(TestPobocky_C('test_pobocky_D'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_sort_cheapest'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))

    return suite

def suite4():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

def SRL_suite_full():
    suite = unittest.TestSuite()
    suite.addTest(Test_SRL_C_Zima('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_map'))
    suite.addTest(Test_SRL_C_Zima('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C_Zima('test_srl_C'))
    return suite
from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "NEVDAMA"
    runner_tests_generalized(suite_ND_full, web_brand, "hotifx", URL)
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)