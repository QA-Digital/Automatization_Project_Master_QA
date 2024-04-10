from KTGSK_Automation_Local_Deploy_PyCharm.CovidInfo_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.pobocky import *
from KTGSK_Automation_Local_Deploy_PyCharm.Detail_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.Detail_C import *
from KTGSK_Automation_Local_Deploy_PyCharm.DetskeKluby_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.FM_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.fulltext_C import *
from KTGSK_Automation_Local_Deploy_PyCharm.groupsearch_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.HP_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.LM_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.poznavacky import *
from KTGSK_Automation_Local_Deploy_PyCharm.SDO_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.SRL_C import *
from KTGSK_Automation_Local_Deploy_PyCharm.SRL_D import *
from KTGSK_Automation_Local_Deploy_PyCharm.HP_C import *
from KTGSK_Automation_Local_Deploy_PyCharm.SRL_results_comparer import *

#import HTMLTestRunner
import HtmlTestRunner
import HTMLTestRunner   as   HtmlTestRunner
def suite_KTGSK_full():
    suite = unittest.TestSuite()
    suite.addTest(TestCovidInfo_D('test_covidInfo_D'))
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(TestDetskeKluby_D("test_kluby_D"))
    suite.addTest(TestFM_D("test_FM_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_lM_isDisplayed"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D'))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D'))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D'))
    #suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D'))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    web_brand = "KARTAGO SK"
    version = "KTGSK- FWSK release 2024-04-15"
    outfile = open("results.html", "w")

    runner_tests_generalized(suite_KTGSK_full, web_brand, version, URL)

    #runner.run(suite2())