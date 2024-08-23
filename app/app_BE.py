import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
import unittest

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

# Ensure that a report directory exists for the project
def ensure_report_directory(project_name):
    report_dir = os.path.join('app', 'report', project_name)
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        logging.debug(f'Created report directory: {report_dir}')
    else:
        logging.debug(f'Report directory already exists: {report_dir}')
    return report_dir

# Function to run the test suite in a separate thread
def run_suite_in_thread(url, web_brand, version, suite_function, email):
    try:
        logging.debug(f'Starting test suite with URL: {url}')
        # Create the project-specific report directory
        report_dir = ensure_report_directory(web_brand.lower())
        # Pass the report directory path to the test runner if needed
        runner_tests_generalized(lambda: suite_function(url), web_brand, version, url, email, report_dir=report_dir)
        logging.debug(f'Test suite finished for URL: {url}')
    except Exception as e:
        logging.error(f'Error running test suite: {e}')

@app.route('/run_suite', methods=['POST'])
def run_suite():
    data = request.json
    logging.debug(f'Received data: {data}')

    web_brand = data.get('web_brand', 'FISCHER')
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
        # Start a new thread to run the test suite, isolating variables for each suite run
        thread = Thread(target=run_suite_in_thread, args=(url, web_brand, version, suite_function, email))
        thread.start()
        logging.debug(f'Started thread for suite: {suite_name} with URL: {url}')
        return jsonify({'status': 'success', 'message': 'Test suite execution started.'}), 200
    except Exception as e:
        logging.error(f'Error starting test suite thread: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
