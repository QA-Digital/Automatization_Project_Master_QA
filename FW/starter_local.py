from selenium.webdriver.common.by import By
import glob
import logging
import os

from HTMLTestRunner import HTMLTestRunner

from FW.Detail_HDP import TestDetailHotelu_HDP
from FW.pobocky import *
from FW.Detail_D import *
from FW.Detail_C import *
from FW.DetskeKluby_D import *
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
from get_run_number import get_run_number


import os
import glob
import logging


# def runner_tests_generalized(suite_function, URL, email):
#     run_number = get_run_number()
#     test_folder = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
#     report_dir = './report'
#
#     # Create report directory if it doesn't exist
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     # Clear previous logging configurations to prevent multiple log entries
#     for handler in logging.root.handlers[:]:
#         logging.root.removeHandler(handler)
#
#     # Set up the log file name without a timestamp
#     log_file = f'{report_dir}/{suite_function.__name__}_{run_number:04d}_log.txt'
#
#     # Configure logging
#     logging.basicConfig(filename=log_file, level=logging.INFO,
#                         format=f'{test_folder} - %(name)s - %(levelname)s - Run Number: {run_number:04d}')
#
#     logger = logging.getLogger(__name__)
#     logger.info(f"Starting test suite: {suite_function.__name__} for URL: {URL} with run number: {run_number:04d}")
#
#     # Setup report details
#     report_title = f"{suite_function.__name__} ||| {URL}"
#     report_name = f"WEB_Suite_Report_{suite_function.__name__}_{run_number:04d}"
#     report_file = f"{report_dir}/{report_name}.html"
#
#     # Set up HTMLTestRunner
#     runner = HtmlTestRunner.HTMLTestRunner(
#         log=True,
#         verbosity=2,
#         output=report_dir,
#         title=report_title,
#         report_name=report_name,
#         open_in_browser=True,
#         description=f"{suite_function.__name__} WEB Suite Report"
#     )
#
#     try:
#         # Run the suite
#         suite = suite_function(URL)
#         logger.info(f"Running the suite: {suite}")
#         result = runner.run(suite)
#
#         # Log the result of the test execution
#         if result.wasSuccessful():
#             logger.info("Test suite executed successfully.")
#         else:
#             logger.warning("Some tests failed during the execution.")
#
#         logger.info(f"Completed test suite: {suite_function.__name__}")
#
#         # Send email only after the suite is executed
#         generated_report = report_file  # Use the expected report file directly
#         sendEmailv2(report_title, report_name, email, [generated_report, log_file])
#
#     except Exception as e:
#         logger.error(f"Error running test suite {suite_function.__name__}: {e}")
#
#
# def append_logs_to_html_report(report_dir, log_file, report_name):
#     """Append logs to the HTML report."""
#     report_files = glob.glob(f"{report_dir}/{report_name}*.html")
#     if not report_files:
#         raise FileNotFoundError("Report file not found")
#
#     report_files.sort(key=os.path.getmtime)
#     report_file = report_files[-1]  # Get the latest file
#
#     with open(log_file, 'r') as lf:
#         log_content = lf.read()
#
#     with open(report_file, 'a') as rf:
#         rf.write('<h2>Test Suite Logs</h2>')
#         rf.write('<pre>{}</pre>'.format(log_content))


def runner_tests_generalized(suite_function, URL, email):
    """Generalized function to run a test suite, generate reports, and send emails."""
    run_number = get_run_number()

    # Ensure report directory exists
    report_dir = './report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Clear previous logging handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up log file
    log_file = f'{os.getcwd()}/{suite_function.__name__}_{run_number:04d}_log.txt'
    logging.basicConfig(filename=log_file, level=logging.INFO, format=f'%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)
    logger.info(f"Starting test suite: {suite_function.__name__} for URL: {URL} with run number: {run_number:04d}")

    report_title = f"{suite_function.__name__} ||| {URL}"
    report_name = f"WEB_Suite_Report_{suite_function.__name__}_{run_number:04d}"
    report_file = f"{report_dir}/{report_name}.html"

    runner = HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=f"{suite_function.__name__} WEB Suite Report"
    )

    try:
        suite = suite_function(URL, run_number=run_number)
        result = runner.run(suite)

        if result.wasSuccessful():
            logger.info("Test suite executed successfully.")
        else:
            logger.warning("Some tests failed.")

        sendEmailv2(report_title, report_name, email, [report_file])

        # Append logs to the report
        append_logs_to_html_report(report_file, suite_function.__name__, run_number)

    except Exception as e:
        logger.error(f"Error running test suite {suite_function.__name__}: {e}")

def append_logs_to_html_report(report_file, suite_name, run_number):
    """Append logs to the HTML report."""
    # Construct the pattern to match relevant log files
    log_pattern = f"{suite_name}_*_test_{run_number:04d}.log"
    log_files = glob.glob(os.path.join(os.getcwd(), log_pattern))

    with open(report_file, 'a') as rf:
        rf.write('<h2>Test Suite Logs</h2>')
        for log_file in log_files:
            with open(log_file, 'r') as lf:
                log_content = lf.read()
                rf.write('<h3>{}</h3>'.format(os.path.basename(log_file)))
                rf.write('<pre>{}</pre>'.format(log_content))

def suite_FW_full2(url, run_number):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url, run_number=run_number))
    return suite


def suite_FW_full(url, run_number):
    #run_number = get_run_number()
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport", URL=url, run_number=run_number))
    suite.addTest(TestDetskeKluby_D("test_kluby_D", URL=url, run_number=run_number))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D", URL=url, run_number=run_number))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac", URL=url, run_number=run_number))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check", URL=url, run_number=run_number))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D", URL=url, run_number=run_number))
    suite.addTest(TestHP_D("test_homePage_D", URL=url, run_number=run_number))
    suite.addTest(TestLM_D("test_lM_isDisplayed", URL=url, run_number=run_number))
    suite.addTest(TestPobocky_C('test_pobocky_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D', URL=url, run_number=run_number))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D', URL=url, run_number=run_number))
    suite.addTest(TestSDO_C('test_SDO_D', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url, run_number=run_number))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url, run_number=run_number))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url, run_number=run_number))
    # suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch', URL=url, run_number=run_number))
    # suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url, run_number=run_number))

    ############################
    ## Test branch
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url, run_number=run_number))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_C', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_C', URL=url, run_number=run_number))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_C', URL=url, run_number=run_number))
    # suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_C', URL=url, run_number=run_number)) ## Experiences are no longer on the web, tests always fail
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_exotika', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url, run_number=run_number))
    # suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_lyze', URL=url, run_number=run_number))
    suite.addTest(TestSDO_C('test_SDO_zlutak_to_SRL_R', URL=url, run_number=run_number))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check', URL=url, run_number=run_number))
   # suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky', URL=url, run_number=run_number))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky', URL=url, run_number=run_number))

    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy', URL=url, run_number=run_number))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani', URL=url, run_number=run_number))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase', URL=url, run_number=run_number))

    suite.addTest(TestDetailHotelu_HDP('test_HDP_change_flight_change_meal_gg', URL=url, run_number=run_number))

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