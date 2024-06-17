import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
# Import the necessary modules and test suite functions from your script
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
from FW_Automation_Local_Deploy_PyCharm.SRL_results_comparer import *
from FW_Automation_Local_Deploy_PyCharm.darkove_poukazy import *
from starter_master_browserstack import runner_tests_generalized

# Define the test suite
def suite_FW_full(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal", URL=url))
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
    suite.addTest(TestSDO_C('test_SDO_D', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_map', URL=url))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava', URL=url))
    suite.addTest(Test_SRL_C('test_srl_C', URL=url))
    suite.addTest(TestSRL_D('test_SRL_D', URL=url))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu', URL=url))
    suite.addTest(Test_HP_C('test_HP_bannery_check', URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_cheap", URL=url))
    suite.addTest(TestDetailHotelu_C("test_detail_price_sorter_terminy_expensive", URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_C', URL=url))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_C', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_poznavacky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_lyze', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_pobyt', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_poznavacky', URL=url))
    suite.addTest(TestSDO_C('test_SDO_zlutak_to_SRL_R', URL=url))
    suite.addTest(TestPobocky_C('test_pobocky_C_click_to_detail_popup_check', URL=url))
    #suite.addTest(Test_SRL_C_comparer('test_SRL_number_of_results_comparer', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL_letenky', URL=url))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch_letenky', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_motivy', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_castka_venovani', URL=url))
    suite.addTest(Test_darkove_poukazy('test_darkove_poukazy_purchase', URL=url))
    return suite

def suite_FW_full2(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    return suite

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
logging.basicConfig(level=logging.DEBUG)


@app.route('/run_suite', methods=['POST'])
def run_suite():
    data = request.json
    logging.debug(f'Received data: {data}')

    web_brand = data.get('web_brand', 'FISCHER')
    version = data.get('version', 'FW-EW release 2024-05-16')
    url = data.get('URL', 'http://localhost')  # Use URL from request or default if not provided
    suite_name = data.get('suiteName')

    logging.debug(f'web_brand: {web_brand}, version: {version}, URL: {url}, suiteName: {suite_name}')

    # Run the test suite
    try:
        if suite_name == 'FW Public web full suite':
            runner_tests_generalized(lambda: suite_FW_full(url), web_brand, version, url)
        else:
            return jsonify({'status': 'error', 'message': 'Unknown test suite name.'}), 400

        return jsonify({'status': 'success', 'message': 'Test suite executed successfully.'}), 200
    except Exception as e:
        logging.error(f'Error running test suite: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
