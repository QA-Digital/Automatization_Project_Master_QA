from selenium.webdriver.common.by import By
import glob
import os
import smtplib
import unittest

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from to_import_secret_master import emailPass

#import HtmlTestRunner
import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)

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

def runner_tests_generalized2(suite_general, web_brand, version, URL):
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title=web_brand + " ||| " + URL,
                                           report_name="WEB Suite Report - version --- " + version + " ---",
                                           open_in_browser=True, description=web_brand+ " WEB Suite Report - version --- " + version + " ---")
    runner.run(suite_general())


def runner_tests_generalized_last(suite_general, web_brand, version, URL, email):
    runner = unittest.TextTestRunner()
    report_title = f"{web_brand} ||| {URL}"
    report_name = f"WEB_Suite_Report_version_{version}"
    report_description = f"{web_brand} WEB Suite Report - version --- {version} ---"

    # Ensure the report directory exists
    report_dir = 'report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Generate the report
    runner = unittest.TextTestRunner()
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )
    runner.run(suite_general(URL))

    # Find the latest generated report file
    report_files = glob.glob(f"{report_dir}/{report_name}*.html")
    if not report_files:
        raise FileNotFoundError("Report file not found")

    # Sort the files by modified time and pick the latest one
    report_files.sort(key=os.path.getmtime)
    report_file = report_files[-1]  # Get the latest file

    # Define additional file paths
    stylesheet_file = os.path.join(report_dir, "stylesheet.css")
    script_file = os.path.join(report_dir, "script.js")
    files = [report_file, stylesheet_file, script_file]

    # Read the main report file to include in the email body
    with open(report_file, 'r') as f:
        report_content = f.read()

    # Send the email with the latest report
    sendEmailv2(report_title, report_content, email, files)


import unittest
import os
import glob
import logging


def runner_tests_generalized_last2(suite_general, web_brand, version, URL, email):
    # Set up logging configuration
    log_file = f'logs_{web_brand}.log'
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    # Start of test run
    logger.info(f"Starting test suite for {web_brand}, URL: {URL}, Version: {version}")

    # Ensure the report directory exists
    report_dir = 'report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    report_title = f"{web_brand} ||| {URL}"
    report_name = f"WEB_Suite_Report_version_{version}"
    report_description = f"{web_brand} WEB Suite Report - version --- {version} ---"

    # Set up HTMLTestRunner with logging enabled
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )

    # Run the test suite
    result = runner.run(suite_general(URL))

    # Log end of test suite
    logger.info(f"Completed test suite for {web_brand}.")

    # Find the latest generated report file
    report_files = glob.glob(f"{report_dir}/{report_name}*.html")
    if not report_files:
        raise FileNotFoundError("Report file not found")

    # Sort the files by modified time and pick the latest one
    report_files.sort(key=os.path.getmtime)
    report_file = report_files[-1]  # Get the latest file

    # Define additional file paths
    stylesheet_file = os.path.join(report_dir, "stylesheet.css")
    script_file = os.path.join(report_dir, "script.js")
    files = [report_file, stylesheet_file, script_file, log_file]

    # Read the main report file to include in the email body
    with open(report_file, 'r') as f:
        report_content = f.read()

    # Send the email with the latest report
    sendEmailv2(report_title, report_content, email, files)

def runner_tests_generalized(suite_general, web_brand, version, URL, email):
    # Set up suite-level logging configuration
    log_file = f'{web_brand}_suite_{version}.log'
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    # Start of test run
    logger.info(f"Starting test suite for {web_brand}, URL: {URL}, Version: {version}")

    # Ensure the report directory exists
    report_dir = 'report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    report_title = f"{web_brand} ||| {URL}"
    report_name = f"WEB_Suite_Report_version_{version}"
    report_description = f"{web_brand} WEB Suite Report - version --- {version} ---"

    # Set up HTMLTestRunner with logging enabled
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )

    # Run the test suite
    result = runner.run(suite_general(URL))

    # Log end of test suite
    logger.info(f"Completed test suite for {web_brand}.")

    # Collect and append logs to HTML report
    append_logs_to_html_report(report_dir, log_file, report_name)

    # Send the report via email
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

import os
import glob
