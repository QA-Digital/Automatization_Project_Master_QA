from Billa_Automation_Local_Deploy_PyCharm.Detail_C import TestDetailHotelu_C
from Billa_Automation_Local_Deploy_PyCharm.FM_D import Test_FM_Exotika_D
from Billa_Automation_Local_Deploy_PyCharm.fulltext_C import Test_Fulltext_C
from Billa_Automation_Local_Deploy_PyCharm.groupsearch_D import Test_Groupsearch_D
from Billa_Automation_Local_Deploy_PyCharm.HP_D import Test_HP_D
from Billa_Automation_Local_Deploy_PyCharm.LM_D import Test_LM_D
from Billa_Automation_Local_Deploy_PyCharm.SDO_D import TestSDO_D
from Billa_Automation_Local_Deploy_PyCharm.SRL_C import Test_SRL_C
from Billa_Automation_Local_Deploy_PyCharm.SRL_D import TestSRL_D
from Billa_Automation_Local_Deploy_PyCharm.HP_C import Test_HP_C
#import HtmlTestRunner
import unittest
from starter_master_browserstack import  runner_tests_generalized
from Billa_Automation_Local_Deploy_PyCharm.to_import import URL


def suite_Billa_full():
    suite = unittest.TestSuite()
    #suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(Test_FM_Exotika_D("test_FM_D"))
    suite.addTest(Test_FM_Exotika_D("test_Exotika_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(Test_HP_D("test_HP_D"))
    suite.addTest(Test_LM_D("test_LM_D"))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    suite.addTest(Test_HP_C('test_HP_banner_destination_to_SDO'))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(Test_FM_Exotika_D("test_FM_D"))
    return suite

web_brand = "Billa"
#runner_tests_generalized(suite_Billa_full, web_brand, "123", URL)
runner_tests_generalized(suite_Billa_full, web_brand, "0", URL)




