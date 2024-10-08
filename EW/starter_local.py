from EW.pobocky import *
from EW.Detail_D import *
from EW.Detail_C import *
from EW.DetskeKluby_D import *
from EW.FM_D import *
from EW.fulltext_C import *
from EW.groupsearch_D import *
from EW.HP_D import *
from EW.LM_D import *
from EW.poznavacky import *
from EW.SDO_D import *
from EW.SRL_C import *
from EW.SRL_D import *
#import HtmlTestRunner
import HTMLTestRunner
from EW.HP_C import *
from EW.SRL_results_comparer import *
from EW.darkove_poukazy import *

def suite_EW_full():
    suite = unittest.TestSuite()
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
    suite.addTest(TestPobocky_C('test_pobocky_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D'))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    #suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch')) ##ted to tam neni zase
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))     ##ted to tam neni zase
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    ##############
    ####################
    ###########################
    suite.addTest(TestPoznavacky_D('test_poznavacky_all_URL_check'))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap"))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive"))
    suite.addTest(TestPoznavacky_D('test_poznavacky_C'))
    suite.addTest(Test_HP_C('test_HP_top_nabidka_status'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt'))  ###
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky'))
   # suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze'))
    #suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check')) ##neni zaple
    suite.addTest(Test_SRL_C('test_SRL_kuba_srl_D_R'))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky'))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy'))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani'))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase'))

    return suite

def suite2():
    suite = unittest.TestSuite()

    suite.addTest(TestFM_D("test_FM_D"))
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
    #runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "EXIM"
    version = "FW-EW release 2024-07-23"
    runner_tests_generalized(suite_EW_full, web_brand, version, URL, "qa.digital@dertouristik.cz")
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)