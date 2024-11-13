from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText
import requests
import time
from to_import_secret_master import emailPass

mujMail = 'ooo.kadoun@gmail.com'
filipMail = 'filip.rytych@seznam.cz'
FW_list_of_emails_to_notify = ["ooo.kadoun@gmail.com", "Filip.RYTYCH@fischer.cz"]
justMeList = ["ooo.kadoun@gmail.com"]


def sendEmailv2(msg, recipient):
  fromx = 'alertserverproblem@gmail.com'
  to = recipient
  msg = MIMEText(msg)
  msg['Subject'] = "HP CHECK"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()
pocetChecku = 0
timerToNotify = 0

FW_start_of_URL = "https://fischer.web"
EW_start_of_URL = "https://exim.web"
def URL_maker(brand_start_of_URL, srweb_number):

    final_URL = brand_start_of_URL+srweb_number+".dtweb.cz"
    #print(final_URL)
    return(final_URL)

def generalized_URL_status_check(brand, email_list_to_notify, start_of_URL):
    timerToNotify = 0
    pocetChecku = 0
    while True:
            if brand == "Exim Tours":
                cisloNodu=11
            else:
                cisloNodu=1
            for i in range(3):
                email_list_position = 0
                try:
                    requestURL = URL_maker(start_of_URL, str(cisloNodu))
                    response = requests.get((requestURL), timeout=65)
                    #print(response)
                    #print(response.status_code)

                except requests.exceptions.Timeout:
                    for _ in email_list_to_notify:
                        msg = brand + " HomePage vrací TIME OUT Exception " + "SRWEB " + str(cisloNodu) + "  " + requestURL
                        sendEmailv2(msg, email_list_to_notify[email_list_position])
                        email_list_position = email_list_position + 1
                except requests.exceptions.ConnectionError:
                    for _ in email_list_to_notify:
                        msg = brand + " HomePage vrací ConnectionError Exception " + "SRWEB " + str(cisloNodu) + "  " + requestURL
                        sendEmailv2(msg, email_list_to_notify[email_list_position])
                        email_list_position = email_list_position + 1
                except:
                        pass

                if response.status_code == 500:
                    for _ in email_list_to_notify:
                        msg = brand + " HomePage vrací status code 500 " + "SRWEB " + str(cisloNodu) + "  " + requestURL
                        sendEmailv2(msg, email_list_to_notify[email_list_position])
                        email_list_position = email_list_position + 1

                if response.status_code == 404:     ##404
                    for _ in email_list_to_notify:
                        msg = brand + " HomePage vrací status code 500 " + "SRWEB " + str(cisloNodu) + "  " + requestURL
                        sendEmailv2(msg, email_list_to_notify[email_list_position])
                        email_list_position = email_list_position + 1

                print(requestURL)
                print(response.status_code)
                cisloNodu = cisloNodu + 1
                time.sleep(20)

            timerToNotify = timerToNotify + 1
            pocetChecku = pocetChecku + 1
            if timerToNotify == 1000:
                msg = "check byl spusten 1000 " + brand
                sendEmailv2(msg, mujMail)
                timerToNotify = 0
            print("CHECK NUMERO  " + str(pocetChecku))
            print("CHECK NUMERO  " + str(pocetChecku))
            print("CHECK NUMERO  " + str(pocetChecku))
            time.sleep(55)

#generalized_URL_status_check("Exim Tours", justMeList)
