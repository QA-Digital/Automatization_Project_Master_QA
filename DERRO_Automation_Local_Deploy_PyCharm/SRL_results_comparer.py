from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from DERRO_Automation_Local_Deploy_PyCharm.to_import import URL, acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod_DERRO = "https://www.dertour.ro/"
URL_SRL_DERRO1 = "/rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2023-11-01&nn=7|8|9|10|11|12|13&rd=2024-01-01&sortby=PriceTotal&sortorder=1&tt=1"
URL_SRL_DERRO2 = "/rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2023-11-01&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-01-01&tt=1"
URL_SRL_DERRO3 = "/rezultatele-cautarii?ac1=2&d=64087|64089|64090|64091|64086&dd=2024-02-29&ic1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO4 = "/rezultatele-cautarii?ac1=2&d=64087|64089|64090|64091|64086&dd=2024-02-29&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO5 = "/rezultatele-cautarii?ac1=2&d=63885|63890|63891|63889|63892|63888|63886|63887&dd=2024-02-29&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO6 = "rezultatele-cautarii?ac1=2&d=63885|63890|63891|63889|63892|63888|63886|63887&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO7 = "/rezultatele-cautarii?ac1=2&d=64168|64162|64161|64167|64171|64166|64169|64172|64174|64159|64170|64164|64176|64160|64173|64175|64163|64165&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO8 = "/rezultatele-cautarii?ac1=2&d=64168|64162|64161|64167|64171|64166|64169|64172|64174|64159|64170|64164|64176|64160|64173|64175|64163|64165&dd=2024-02-29&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO9 = "/rezultatele-cautarii?ac1=2&d=63738&dd=2024-02-29&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO10 = "/rezultatele-cautarii?ac1=2&d=63738&dd=2024-02-29&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO11 = "/rezultatele-cautarii?ac1=2&d=63972|63984|63977|63979|63981|64037|63976|63988|63978|63975|63980|63982|63974|63973|63985|63987|63986|63983&dd=2024-02-29&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO12 = "/rezultatele-cautarii?ac1=2&d=63972|63984|63977|63979|63981|64037|63976|63988|63978|63975|63980|63982|63974|63973|63985|63987|63986|63983&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO13 = "/rezultatele-cautarii?ac1=2&d=64102|64099&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO14 = "/rezultatele-cautarii?ac1=2&d=63992|63994|63995|75728|75729|63993|75730|77252|75731|77253&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO15 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-05-01&nn=7|8|9|10|11|12|13&rd=2024-06-30&tt=1"
URL_SRL_DERRO16 = "/rezultatele-cautarii?ac1=2&d=63763|63764|63767|63766|63765&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO17 = "/rezultatele-cautarii?ac1=2&d=64144|64128|64126|64127|64133|64130&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO18 = "/rezultatele-cautarii?ac1=2&d=64144|64128|64126|64127|64133|64130&dd=2024-02-29&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO19 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-02-29&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_SRL_DERRO20 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"

URL_SRL_list_DERRO = [URL_SRL_DERRO1, URL_SRL_DERRO2, URL_SRL_DERRO3, URL_SRL_DERRO4, URL_SRL_DERRO5, URL_SRL_DERRO6, URL_SRL_DERRO7, URL_SRL_DERRO8, URL_SRL_DERRO9, URL_SRL_DERRO10, URL_SRL_DERRO11, URL_SRL_DERRO12, URL_SRL_DERRO13, URL_SRL_DERRO14, URL_SRL_DERRO15, URL_SRL_DERRO16, URL_SRL_DERRO17, URL_SRL_DERRO18, URL_SRL_DERRO19, URL_SRL_DERRO20]

class Test_SRL_C_comparer(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, URL, URL_public_prod_DERRO, URL_SRL_list_DERRO)


        self.test_passed = True