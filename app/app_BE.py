from selenium.webdriver.common.by import By
import glob
import logging
import os
import smtplib

import pytest
from HTMLTestRunner import HTMLTestRunner
from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
from FW.darkove_poukazy import *
from FW.starter_local import suite_FW_full  # FISCHER
from DERRO.starter_local import suite_DERRO_full  # Derro
from ET.starter_local import suite_ET_full  # eTravel
from EW.starter_local import suite_EW_full  # Exim
from EXPL.starter_local import suite_EXPL_full  # Eximpl
from FWSK.starter_local import suite_FWSK_full  # Fischer SK
from KTGHU.starter_local import suite_KTGHU_full  # Kartago HU
from KTGSK.starter_local import suite_KTGSK_full  # Kartago SK
from ND.starter_local import suite_ND_full  # NevDama
from get_run_number import get_run_number
import HTMLTestRunner   as   HtmlTestRunner
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from to_import_secret_master import emailPass

def sendEmailv2(subject, msg, recipient, files):
    fromx = 'alertserverproblem@gmail.com'
    to = recipient

    # Create the root message
    msg_root = MIMEMultipart()
    msg_root['Subject'] = subject
    msg_root['From'] = fromx
    msg_root['To'] = to
    msg_root.preamble = 'Multipart message.\n'

    # Attach the main message
    msg_root.attach(MIMEText(msg, 'html'))

    # Attach the files
    for file in files:
        if file.endswith('.html') or os.path.basename(file) == 'stylesheet.css':
            with open(file, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file)}"')
                msg_root.attach(part)

    try:
        # Send the email using Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromx, emailPass)

        server.sendmail(fromx, to, msg_root.as_string())
        server.quit()
        print(f"Email sent successfully to {recipient}")

    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

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

        # Check if the report was created successfully
        if os.path.exists(report_file):
            sendEmailv2(report_title, report_name, email, [report_file])

            # Merge logs based on the run number
            merged_log_path = merge_logs_for_report(suite_function.__name__, run_number, report_file)

            if merged_log_path:  # Ensure merged log file was created
                # Append logs to the report
                append_logs_to_html_report(merged_log_path, report_file)
            else:
                logger.error("Merged log file was not created.")
        else:
            logger.error(f"Report file does not exist: {report_file}")

    except Exception as e:
        logger.error(f"Error running test suite {suite_function.__name__}: {e}")


import os
import re
import logging

def merge_logs_for_report(run_number, report_path):
    # Define the log pattern to match logs based on the run number
    log_pattern = re.compile(rf'_{run_number:04d}_log\.txt$')  # Match all logs ending with the run number
    logs_dir = os.getcwd()  # Assuming the log files are created in the current working directory

    merged_log_content = ""

    # Check if the logs directory exists
    if not os.path.exists(logs_dir):
        logging.error(f"Logs directory does not exist: {logs_dir}")
        return None

    # Collect all matching log files
    matching_logs = [log_file for log_file in os.listdir(logs_dir) if log_pattern.search(log_file)]

    # Merge the content of all matched log files
    if matching_logs:
        for log_file in matching_logs:
            log_path = os.path.join(logs_dir, log_file)
            with open(log_path, 'r') as f:
                merged_log_content += f"--- Log from {log_file} ---\n"
                merged_log_content += f.read() + "\n"
    else:
        logging.warning(f"No log files matched the pattern for run number: {run_number}")
        return None

    # Write the merged log content to a new file
    report_filename = os.path.basename(report_path)
    merged_log_filename = report_filename.replace('.html', '_merged_log.txt')
    merged_log_path = os.path.join(logs_dir, merged_log_filename)

    with open(merged_log_path, 'w') as merged_log_file:
        merged_log_file.write(merged_log_content)

    logging.info(f"Merged log file created: {merged_log_path}")
    return merged_log_path



def append_logs_to_html_report(merged_log_path, html_report_path):
    # Read the HTML report
    with open(html_report_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Read the merged log content
    with open(merged_log_path, 'r') as log_file:
        merged_log_content = log_file.read()

    # Create a preformatted block for logs
    pre_tag = soup.new_tag("pre")
    pre_tag.string = merged_log_content

    # Assuming there is an HTML element where you want to append the logs
    log_section = soup.find('div', {'id': 'log-section'})  # Example selector, adjust as needed
    if log_section:
        log_section.append(pre_tag)

    # Write the modified HTML back
    with open(html_report_path, 'w') as f:
        f.write(str(soup))



from bs4 import BeautifulSoup
import re




app = Flask(__name__)
CORS(app, resources={r"/run_suite": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)


def run_suite_in_thread(url, suite_function, email):
    """Runs the suite in a new thread."""
    try:
        logging.debug(f'Starting test suite for URL: {url}')
        base_report_dir = './report'
        if not os.path.exists(base_report_dir):
            os.makedirs(base_report_dir)

        suite_name = suite_function.__name__.replace('suite_', '').replace('_full', '').upper()
        log_file_name = os.path.join(base_report_dir, f'WEB_Suite_Report_{suite_name}_{time.strftime("%d-%m-%y_%H-%M-%S")}_log.txt')
        logging.debug(f'Log file name: {log_file_name}')
        logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f'Starting test suite: {suite_name} for URL: {url}')

        runner_tests_generalized(suite_function, url, email)
        logging.debug(f'Test suite {suite_name} finished for URL: {url}')

    except Exception as e:
        logging.error(f'Error running test suite {suite_name}: {e}')

@app.route('/run_suite', methods=['POST'])
def run_suite():
    """API endpoint to trigger the suite run."""
    try:
        data = request.get_json()
        if not data:
            logging.error('No data received.')
            return jsonify({'status': 'error', 'message': 'No data received.'}), 400

        logging.debug(f'Received data: {data}')

        url = data.get('URL')
        email = data.get('email')
        suite_name = data.get('suiteName')

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
            logging.error(f'Suite {suite_name} not found.')
            return jsonify({'status': 'error', 'message': f'Suite {suite_name} not found.'}), 400

        runner_tests_generalized(suite_function, url, email)
        #pytest_runner_generalized(suite_function, url, email)
        return jsonify({'status': 'success', 'message': 'Test suite execution started.'}), 200
    except Exception as e:
        logging.error(f'Error starting test suite: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)