from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EXPL.to_import import URL, acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod_EXPL = "https://www.exim.pl"
URL_SRL_EXPL1 = "/wyszukanie?ac1=2&d=63484|63483|64419|64420|64425&dd=2023-11-01&nn=6|7|8|9|10|11|12|13|14&rd=2023-11-30&tt=1"
URL_SRL_EXPL2 = "/wyszukanie?ac1=2&d=63448|63288&dd=2024-01-15&nn=7|8|9|10|11|12|13&rd=2024-02-25&tt=1"
URL_SRL_EXPL3 = "/wyszukanie?ac1=2&d=63252|63447&dd=2024-01-15&ic1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&tt=1"
URL_SRL_EXPL4 = "/wyszukanie?ac1=2&d=63213|63241|74459|74460|74463|74464|74465&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL5 = "/wyszukanie?ac1=2&d=63580|63581&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL6 = "/wyszukanie?ac1=2&d=63738&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL7 = "/wyszukanie?ac1=2&d=64126|64127|64128&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL8 = "/wyszukanie?ac1=2&d=64076&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL9 = "/wyszukanie?ac1=2&d=63252&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL10 = "/wyszukanie?ac1=2&d=63864|63865&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL11 = "/wyszukanie?ac1=2&d=64246&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL12 = "/wyszukanie?ac1=2&d=63757|63758|63759&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_SRL_EXPL13 = "/wyszukanie?ac1=2&d=64419|64420|64425&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_SRL_EXPL14 = "/wyszukanie?ac1=2&d=63213|63241|74459|74460|74463|74464|74465&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_SRL_EXPL15 = "/wyszukanie?ac1=2&d=63707|63710&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_SRL_EXPL16 = "/wyszukanie?ac1=2&d=64126|64127|64128&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_SRL_EXPL17 = "/wyszukanie?ac1=2&d=63252&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_SRL_EXPL18 = "/wyszukanie?ac1=2&d=63343|63348&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"
URL_SRL_EXPL19 = "/wyszukanie?ac1=2&d=63982&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"
URL_SRL_EXPL20 = "/wyszukanie?ac1=2&d=64419|64420|64425&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"

URL_SRL_list_EXPL = [URL_SRL_EXPL1, URL_SRL_EXPL2, URL_SRL_EXPL3, URL_SRL_EXPL4, URL_SRL_EXPL5, URL_SRL_EXPL6, URL_SRL_EXPL7, URL_SRL_EXPL8, URL_SRL_EXPL9, URL_SRL_EXPL10, URL_SRL_EXPL11, URL_SRL_EXPL12, URL_SRL_EXPL13, URL_SRL_EXPL14, URL_SRL_EXPL15, URL_SRL_EXPL16, URL_SRL_EXPL17, URL_SRL_EXPL18, URL_SRL_EXPL19, URL_SRL_EXPL20]

from EXPL.to_import import URL_local
class Test_SRL_C_comparer(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, self.URL, URL_public_prod_EXPL, URL_SRL_list_EXPL)


        self.test_passed = True