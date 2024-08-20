import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from FW.Detail_D import TestDetailHotelu_D  # Ensure correct imports
from FW.darkove_poukazy import *
from starter_master_browserstack import runner_tests_generalized
from FW.starter_local import suite_FW_full        # FISCHER
from DERRO.starter_local import suite_DERRO_full  # Derro
from ET.starter_local import suite_ET_full        # eTravel
from EW.starter_local import suite_EW_full        # Exim
from EXPL.starter_local import suite_EXPL_full    # Eximpl
from FWSK.starter_local import suite_FWSK_full    # Fischer SK
from KTGHU.starter_local import suite_KTGHU_full  # Kartago HU
from KTGSK.starter_local import suite_KTGSK_full  # Kartago SK
from ND.starter_local import suite_ND_full        # NevDama

app = Flask(__name__)
CORS(app)  # Enable CORS
logging.basicConfig(level=logging.DEBUG)

# Define the suite functions
def suite_FW_full2(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    return suite

# Add more suite functions if needed, matching the suite names

@app.route('/run_suite', methods=['POST'])
def run_suite():
    data = request.json
    logging.debug(f'Received data: {data}')

    web_brand = data.get('web_brand', 'FISCHER')  # This will now be set correctly based on the project
    version = data.get('version', 'FW-EW release 2024-05-16')
    url = data.get('URL')
    suite_name = data.get('suiteName')
    email = data.get('email')

    logging.debug(f'web_brand: {web_brand}, version: {version}, URL: {url}, suiteName: {suite_name}, email: {email}')

    # Dictionary to map suite names to functions
    suite_mapping = {
        'FISCHER web full suite': suite_FW_full,
        'DERRO web full suite': suite_DERRO_full,
        'ETRAVEL web full suite': suite_ET_full,
        'EXIM web full suite': suite_EW_full,
        'EXIMPL web full suite': suite_EXPL_full,
        'FISCHERSK web full suite': suite_FWSK_full,
        'KARTAGOHU web full suite': suite_KTGHU_full,
        'KARTAGOSK web full suite': suite_KTGSK_full,
        'NEVDAMA web full suite': suite_ND_full,
    }

    suite_function = suite_mapping.get(suite_name)

    if not suite_function:
        return jsonify({'status': 'error', 'message': f'Suite {suite_name} not found.'}), 400

    try:
        runner_tests_generalized(lambda: suite_function(url), web_brand, version, url, email)
        return jsonify({'status': 'success', 'message': 'Test suite executed successfully.'}), 200
    except Exception as e:
        logging.error(f'Error running test suite: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
