import glob
import logging
import os
import smtplib
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
    # Generate a unique run number for this suite
    run_number = get_run_number()

    # Get the folder name dynamically based on the test file location
    test_folder = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

    # Set up the report directory
    report_dir = './report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Clear previous logging configurations to prevent multiple log entries
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up the log file name without a timestamp
    log_file = f'{report_dir}/{suite_function.__name__}_{run_number:04d}_log.txt'

    # Configure logging
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format=f'{test_folder} - %(name)s - %(levelname)s - Run Number: {run_number:04d}')

    logger = logging.getLogger(__name__)

    # Log the start of the test run
    logger.info(f"Starting test suite: {suite_function.__name__} for URL: {URL} with run number: {run_number:04d}")

    # Report setup with run number included, no timestamp in the report name
    report_title = f"{suite_function.__name__} ||| {URL}"
    report_name = f"WEB_Suite_Report_{suite_function.__name__}_{run_number:04d}"
    report_file = f"{report_dir}/{report_name}.html"  # Desired final report file

    report_description = f"{suite_function.__name__} WEB Suite Report"

    # Set up HTMLTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,  # Ensure the output directory is consistent
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )

    # Run the suite and log any results or errors
    try:
        # Pass the URL and run number to the suite function
        suite = suite_function(URL, run_number=run_number)
        result = runner.run(suite)
        logger.info(f"Completed test suite: {suite_function.__name__}")
    except Exception as e:
        logger.error(f"Error running test suite {suite_function.__name__}: {e}")

    # After the report is generated, find the actual generated report file
    report_files = glob.glob(f"{report_dir}/WEB_Suite_Report_{suite_function.__name__}*.html")
    report_files.sort(key=os.path.getmtime)
    generated_report = report_files[-1]  # Get the latest generated report

    # Ensure we pass the correct report file to the sendEmailv2 function
    sendEmailv2(report_title, report_description, email, [generated_report, log_file])


def append_logs_to_html_report(report_dir, log_file, report_name):
    """Append logs to the HTML report."""
    report_files = glob.glob(f"{report_dir}/{report_name}*.html")
    if not report_files:
        raise FileNotFoundError("Report file not found")

    report_files.sort(key=os.path.getmtime)
    report_file = report_files[-1]  # Get the latest file

    with open(log_file, 'r') as lf:
        log_content = lf.read()

    with open(report_file, 'a') as rf:
        rf.write('<h2>Test Suite Logs</h2>')
        rf.write('<pre>{}</pre>'.format(log_content))


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