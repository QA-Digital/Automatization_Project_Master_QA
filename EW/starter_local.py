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
from get_run_number import get_run_number


def suite_EW_full(url, run_number):
    suite = unittest.TestSuite()
    #run_number = get_run_number()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url, run_number=run_number))
    #suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))  # Not included
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url, run_number=run_number))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url, run_number=run_number))
    suite.addTest(TestFM_D("test_FM_D", URL=url, run_number=run_number))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url, run_number=run_number))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url, run_number=run_number))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url, run_number=run_number))
    suite.addTest(TestHP_D("test_homePage_D", URL=url, run_number=run_number))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url, run_number=run_number))
    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url, run_number=run_number))
    suite.addTest(TestSDO_D('test_SDO_D', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url, run_number=run_number))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url, run_number=run_number))
    # suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))  ## Currently not included
    # suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))  ## Currently not included
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_all_URL_check', URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_C', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_top_nabidka_status', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_exotika', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url, run_number=run_number))
    # suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze'))  ## Currently not included
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url, run_number=run_number))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check'))  ## Not included
    suite.addTest(Test_SRL_C('test_SRL_kuba_srl_D_R', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky', URL=url, run_number=run_number))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy', URL=url, run_number=run_number))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani', URL=url, run_number=run_number))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase', URL=url, run_number=run_number))
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
from FW.starter_local import  runner_tests_generalized, append_logs_to_html_report
if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    #run_number = get_run_number()
    outfile = open("results.html", "w")
    web_brand = "EXIM"
    version = "FW-EW release 2024-07-23"
    runner_tests_generalized(suite_EW_full, URL, "qa.digital@dertouristik.cz")
    #runner_tests_generalized(SRL_suite_full, web_brand, "atcomcore deploy", URL)
    #runner_tests_generalized(suite4, web_brand, "220718.1", URL)