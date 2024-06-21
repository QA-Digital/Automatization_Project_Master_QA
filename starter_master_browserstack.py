import glob
import os
import smtplib
import unittest

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from to_import_secret_master import emailPass

import HtmlTestRunner
#import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)

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

def runner_tests_generalized(suite_general, web_brand, version, URL, email):
    runner = unittest.TextTestRunner()
    report_title = f"{web_brand} ||| {URL}"
    report_name = f"WEB_Suite_Report_version_{version}"
    report_description = f"{web_brand} WEB Suite Report - version --- {version} ---"

    # Ensure the report directory exists
    report_dir = 'report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Generate the report
    runner = HtmlTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output=report_dir,
        title=report_title,
        report_name=report_name,
        open_in_browser=True,
        description=report_description
    )
    runner.run(suite_general())

    # Find the generated report file
    report_files = glob.glob(f"{report_dir}/{report_name}*.html")
    if not report_files:
        raise FileNotFoundError("Report file not found")
    report_file = report_files[0]

    # Define additional file paths
    stylesheet_file = os.path.join(report_dir, "stylesheet.css")
    script_file = os.path.join(report_dir, "script.js")
    files = [report_file, stylesheet_file, script_file]

    # Read the main report file to include in the email body
    with open(report_file, 'r') as f:
        report_content = f.read()

    # Send the email
    sendEmailv2(report_title, report_content, email, files)