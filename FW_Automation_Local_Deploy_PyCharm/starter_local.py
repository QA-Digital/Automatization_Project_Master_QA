from FW_Automation_Local_Deploy_PyCharm.pobocky import *
from FW_Automation_Local_Deploy_PyCharm.Detail_D import *
from FW_Automation_Local_Deploy_PyCharm.Detail_C import *
from FW_Automation_Local_Deploy_PyCharm.DetskeKluby_D import *
from FW_Automation_Local_Deploy_PyCharm.dovolena_D import *
from FW_Automation_Local_Deploy_PyCharm.FM_D import *
from FW_Automation_Local_Deploy_PyCharm.fulltext_C import *
from FW_Automation_Local_Deploy_PyCharm.groupsearch_D import *
from FW_Automation_Local_Deploy_PyCharm.HP_D import *
from FW_Automation_Local_Deploy_PyCharm.LM_D import *
from FW_Automation_Local_Deploy_PyCharm.poznavacky import *
from FW_Automation_Local_Deploy_PyCharm.SDO_C import *
from FW_Automation_Local_Deploy_PyCharm.SRL_C import *
from FW_Automation_Local_Deploy_PyCharm.SRL_D import *
from FW_Automation_Local_Deploy_PyCharm.HP_C import *
#import HtmlTestRunner
#import HTMLTestRunner   as   HtmlTestRunner  ##at office PC gotta be set up like that (???)
from FW_Automation_Local_Deploy_PyCharm.SRL_results_comparer import *
from FW_Automation_Local_Deploy_PyCharm.darkove_poukazy import *

def suite_FW_full():
    suite = unittest.TestSuite()
    #suite.addTest(TestCovidInfo_D('test_covidInfo_D'))
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(TestDetskeKluby_D("test_kluby_D"))
    suite.addTest(TestDovolena_D("test_dovolena_D"))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_lM_isDisplayed"))
    suite.addTest(TestPobocky_C('test_pobocky_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D'))
   # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D'))
    suite.addTest(TestSDO_C('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    #suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    ############################
    ##test vetev
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap"))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive"))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_C'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_C'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_C'))
   # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_C')) ##zazitky uz nejsou na webu dele, vzdy testy padaji
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt'))  ###
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky'))
    #suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze'))
    suite.addTest(TestSDO_C('test_SDO_zlutak_to_SRL_R'))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check'))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky'))

    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy'))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani'))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase'))

    return suite

def suite_map():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
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
    version = "FW-EW release 2024-05-16"
    runner_tests_generalized(suite_FW_full, web_brand, version, URL)

    #runner_tests_generalized(SRL_suite_full, web_brand, version, URL)
    #runner_tests_generalized(suite2, web_brand, version, URL)