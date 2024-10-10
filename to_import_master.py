import smtplib, ssl
from email.mime.text import MIMEText
from selenium import webdriver
from to_import_secret_master import comandExecutor, emailPass

queryListOptimizedMonitor = ["Zanzibar", "Řecko", "Turecko", "Egypt", "Kapverdy", "Oman" , "Kefalonia","Dominikánská republika" , "Porto Skala 7", "Doubletree"]

def sendEmail(msg):
  fromx = 'alertserverproblem@gmail.com'
  to = 'ooo.kadoun@gmail.com'
  msg = MIMEText(msg)
  msg['Subject'] = "SRWEB1"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

def setUp(self):
  #self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.driver = webdriver.Remote(
      command_executor=comandExecutor,
      desired_capabilities="desired_cap")
  #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  #webdriver.Safari(executable_path=SafariDriverManager().install())
  #generalDriverWaitImplicit(self.driver)