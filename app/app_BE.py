import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
import unittest

from FW.Detail_D import TestDetailHotelu_D  # Ensure correct imports
from FW.darkove_poukazy import *
from FW.starter_local import runner_tests_generalized
from FW.starter_local import suite_FW_full  # FISCHER
from DERRO.starter_local import suite_DERRO_full  # Derro
from ET.starter_local import suite_ET_full  # eTravel
from EW.starter_local import suite_EW_full  # Exim
from EXPL.starter_local import suite_EXPL_full  # Eximpl
from FWSK.starter_local import suite_FWSK_full  # Fischer SK
from KTGHU.starter_local import suite_KTGHU_full  # Kartago HU
from KTGSK.starter_local import suite_KTGSK_full  # Kartago SK
from ND.starter_local import suite_ND_full  # NevDama

# Flask app setup
from starter_master_browserstack import sendEmailv2

app = Flask(__name__)
CORS(app, resources={r"/run_suite": {"origins": "*"}})  # Enable CORS for /run_suite

logging.basicConfig(level=logging.DEBUG)


def run_suite_in_thread(url, suite_function, email):
    try:
        logging.debug(f'Starting test suite for URL: {url}')

        # Create the base report directory if it does not exist
        base_report_dir = os.path.join('app', 'report')
        if not os.path.exists(base_report_dir):
            os.makedirs(base_report_dir)
            logging.debug(f'Created base report directory: {base_report_dir}')

        # Extract the suite name from the function name (optional, can be customized based on need)
        suite_name = suite_function.__name__.replace('suite_', '').replace('_full', '').upper()

        # Create a specific report directory for the suite
        report_dir = os.path.join(base_report_dir, suite_name.lower())
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
            logging.debug(f'Created report directory: {report_dir}')

        # Create log file with timestamp
        log_file_name = os.path.join(report_dir,
                                     f'WEB_Suite_Report_{suite_name}_{time.strftime("%d-%m-%y_%H-%M-%S")}_log.txt')
        logging.debug(f'Log file name: {log_file_name}')

        # Configure logging to write to the log file
        logging.basicConfig(filename=log_file_name, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Log start of the test suite
        logging.info(f'Starting test suite: {suite_name} for URL: {url}')

        # Run the test suite using runner_tests_generalized
        runner_tests_generalized(suite_function, url, email)

        # Define the path to the expected HTML report without timestamp
        html_report_path = os.path.join(report_dir,
                                        f'WEB_Suite_Report_{suite_name}.html')

        # Check if the HTML report exists and send email
        if os.path.exists(html_report_path):
            sendEmailv2(subject='Test Suite Report', msg='Please find the attached report.', recipient=email,
                        files=[html_report_path])
            logging.info(f'Email sent successfully to {email} with report: {html_report_path}')
        else:
            logging.error(f'HTML report file {html_report_path} does not exist.')
            sendEmailv2(subject='Test Suite Report', msg='HTML report file not generated.', recipient=email, files=[])

        logging.debug(f'Test suite {suite_name} finished for URL: {url}')
    except Exception as e:
        logging.error(f'Error running test suite {suite_name}: {e}')

@app.route('/run_suite', methods=['POST'])
def run_suite():
    try:
        data = request.json
        logging.debug(f'Received data: {data}')

        url = data.get('URL')
        email = data.get('email')

        logging.debug(f'URL: {url}, email: {email}')

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

        suite_name = data.get('suiteName')
        suite_function = suite_mapping.get(suite_name)

        if not suite_function:
            logging.error(f'Suite {suite_name} not found.')
            return jsonify({'status': 'error', 'message': f'Suite {suite_name} not found.'}), 400

        # Start a new thread to run the test suite
        thread = Thread(target=run_suite_in_thread, args=(url, suite_function, email))
        thread.start()
        logging.debug(f'Started thread for suite with URL: {url}')
        return jsonify({'status': 'success', 'message': 'Test suite execution started.'}), 200
    except Exception as e:
        logging.error(f'Error starting test suite: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)