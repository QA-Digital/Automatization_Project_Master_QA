import glob
import logging
import os

from FW.pobocky import *
from FW.Detail_D import *
from FW.Detail_C import *
from FW.DetskeKluby_D import *
from FW.dovolena_D import *
from FW.FM_D import *
from FW.fulltext_C import *
from FW.groupsearch_D import *
from FW.HP_D import *
from FW.LM_D import *
from FW.poznavacky import *
from FW.SDO_C import *
from FW.SRL_C import *
from FW.SRL_D import *
from FW.HP_C import *
#import HtmlTestRunner
import HTMLTestRunner   as   HtmlTestRunner  ##at office PC gotta be set up like that (???)
from FW.SRL_results_comparer import *
from FW.darkove_poukazy import *


def runner_tests_generalized(suite_function, URL, email):
    # Set up logging configuration with suite name
    log_file = f'./report/{suite_function.__name__}.log'
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    # Log the start of the test run
    logger.info(f"Starting test suite: {suite_function.__name__} for URL: {URL}")

    # Create the report directory if it doesn't exist
    report_dir = './report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Report setup
    report_title = f"{suite_function.__name__} ||| {URL}"
    report_name = f"WEB_Suite_Report_{suite_function.__name__}"
    report_description = f"{suite_function.__name__} WEB Suite Report"

    # Set up HTMLTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )

    # Run the suite and log any results or errors
    try:
        suite = suite_function(URL)  # Pass the URL to the suite function
        result = runner.run(suite)
        logger.info(f"Completed test suite: {suite_function.__name__}")
    except Exception as e:
        logger.error(f"Error running test suite {suite_function.__name__}: {e}")

    # Append logs to HTML report and send via email
    append_logs_to_html_report(report_dir, log_file, report_name)
    sendEmailv2(report_title, report_description, email, [f"{report_dir}/{report_name}.html", log_file])

def append_logs_to_html_report(report_dir, log_file, report_name):
    """Append logs to the HTML report."""
    # Find the report file
    report_files = glob.glob(f"{report_dir}/{report_name}*.html")
    if not report_files:
        raise FileNotFoundError("Report file not found")

    # Sort the files by modified time and pick the latest one
    report_files.sort(key=os.path.getmtime)
    report_file = report_files[-1]  # Get the latest file

    # Read the log file content
    with open(log_file, 'r') as lf:
        log_content = lf.read()

    # Append log content to the HTML report
    with open(report_file, 'a') as rf:
        rf.write('<h2>Test Suite Logs</h2>')
        rf.write('<pre>{}</pre>'.format(log_content))

def suite_FW_full1(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
   # suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url)) obsolete
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url))
    suite.addTest(TestDovolena_D("test_dovolena_D", URL=url))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url))
    suite.addTest(TestHP_D("test_homePage_D", URL=url))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url))
    suite.addTest(TestSDO_C('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    # suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch', URL=url))
    #suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    ############################
    ## Test branch
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_C', URL=url))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_C', URL=url)) ## Experiences are no longer on the web, tests always fail
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url))  ###
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url))
    # suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze', URL=url))
    suite.addTest(TestSDO_C('test_SDO_zlutak_to_SRL_R', URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check', URL=url))
    suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky', URL=url))

    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase', URL=url))
    return suite

def suite_FW_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
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

from starter_master_browserstack import sendEmailv2

if __name__ == '__main__':
   # runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "FISCHER"
    version = "FW-EW release 2024-07-23"
    runner_tests_generalized(suite_FW_full, URL, "qa.digital@dertouristik.cz")

    #runner_tests_generalized(SRL_suite_full, web_brand, version, URL)
    #runner_tests_generalized(suite2, web_brand, version, URL)