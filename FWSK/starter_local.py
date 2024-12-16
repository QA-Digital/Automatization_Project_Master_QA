from selenium.webdriver.common.by import By

from FWSK.pobocky import *
from FWSK.Detail_D import *
from FWSK.Detail_C import *
from FWSK.DetskeKluby_D import *
from FWSK.dovolena_D import *
from FWSK.FM_D import *
from FWSK.fulltext_C import *
from FWSK.groupsearch_D import *
from FWSK.HP_D import *
from FWSK.LM_D import *
from FWSK.poznavacky import *
from FWSK.SDO_D import *
from FWSK.SRL_C import *
from FWSK.SRL_D import *
from FWSK.HP_C import *
import HtmlTestRunner
import HTMLTestRunner   as   HtmlTestRunner  ##at office PC gotta be set up like that (???)
from FWSK.SRL_results_comparer import *
from FWSK.Detail_HDP import TestDetailHotelu_HDP


def suite_FWSK_full(url):
    suite = unittest.TestSuite()
    #suite.addTest(TestCovidInfo_D('test_covidInfo_D', URL=url))
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    #suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url))
    suite.addTest(TestDovolena_D("test_dovolena_D", URL=url))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))
    suite.addTest(TestHP_D("test_homePage_D", URL=url))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url))
    suite.addTest(TestPobocky_D('test_pobocky_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url))  # v aktualni fazi nejsou poznavacky na SK takze jen failuji anyway 5.5.23
    suite.addTest(TestSDO_D('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url))
    #suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch', URL=url))
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    #suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))

    suite.addTest(TestDetailHotelu_HDP('test_HDP_change_flight_change_meal_gg', URL=url))
    suite.addTest(TestDetailHotelu_HDP('test_HDP_DX_two_rooms_change_one_not_available_gg', URL=url))
    suite.addTest(TestDetailHotelu_HDP('test_HDP_URL_no_parameters_default', URL=url))
    suite.addTest(TestDetailHotelu_HDP('test_HDP_URL_no_parameters_DX', URL=url))
    suite.addTest(TestDetailHotelu_HDP('test_HDP_URL_no_parameters_DS65536', URL=url))

    return suite


def suite2():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    outfile = open("results.html", "w")
    web_brand = "FISCHER SK "
    version = "KTGSK- FWSK release 2024-04-24"
    runner_tests_generalized(suite_FWSK_full, web_brand, version, URL, "qa.digital@dertouristik.cz")