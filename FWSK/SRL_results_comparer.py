from selenium.webdriver.common.by import By
from FWSK.to_import import URL, setUp, tearDown
import unittest

from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://fischer.sk"

URL_SRL_FWSK1 = "/vysledky-vyhladavania?ac1=2&ac2=3&d=654|1005|953|590|621|1009|680|622|1108|669|1086|978|594|611|610|592|675|612|1010|726|683|609&dd=2024-08-01&ic1=1&ka1=12&ka2=15|4&kc1=1&kc2=2&nn=7|8|9|10|11|12|13|14|15&rd=2024-09-30&to=483|1837|3437&tt=1"

URL_SRL_FWSK2 = "/vysledky-vyhladavania?ac1=2&d=687|654|604&dd=2023-09-01&ka1=5|2&kc1=2&nn=7|8|9|10|11|12|13&rd=2023-10-01&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK3 = "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-01&ka1=5|2&kc1=2&nn=4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK4 = "/vysledky-vyhladavania?ac1=2&d=618|619|624|973|595|746|1225|623|741|735|993|648|972|620&dd=2023-09-01&nn=4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK5 = "/vysledky-vyhladavania?ac1=2&d=1111&dd=2023-08-01&ka1=7&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-09-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK6 = "/vysledky-vyhladavania?ac1=4&ac2=3&d=819|1235|1225|618|619|624|973|595|746|1111|623|741|735|993|648|972|620&dd=2024-08-01&ic1=1&ka1=12&ka2=15|4&kc1=1&kc2=2&nn=7|8|9|10|11|12|13|14|15&rd=2024-09-30&to=483|1837|3437&tt=1"

URL_SRL_FWSK7 = "/vysledky-vyhladavania?ac1=4&ac2=3&d=619|973|746|1111|607|591|627|974|712|596&dd=2024-06-15&ic1=1&ka1=12|10&ka2=15|4|4&kc1=2&kc2=3&nn=7|8|9|10|11|12|13|14|15&rd=2024-07-31&to=483|1837|3437&tt=1"

URL_SRL_FWSK8 = "/vysledky-vyhladavania?ac1=2&d=627|974|712|684|955|596&dd=2023-10-01&ds=0&ifm=0&ilm=0&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-11-30&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK9 = "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-01&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-11-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK10 = "/vysledky-vyhladavania?ac1=4&ac2=3&d=619|973|746|1111|607|591|627|974|712|596&dd=2024-06-15&ic1=1&ka1=12|10&ka2=15|4|4&kc1=2&kc2=3&nn=7|8|9|10|11|12|13|14|15&rd=2024-07-31&to=483|1837|3437&tt=1"

URL_SRL_FWSK11 = "/vysledky-vyhladavania?ac1=2&d=621|1009|680|622|1108|953|669|1086|978|594|611|610|592|675|612|1010|590|726|683|609&dd=2023-09-01&ds=0&ifm=0&ilm=0&nn=5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK12 = "/poznavacie-zajazdy/vysledky-vyhladavania?ac1=2&d=653|819|1235|724|826|1225|623|1059|741|735|618|619|624|973|1132|709|711|603|1116|993|595|614|648|972|1093|1198|1114|620|746|1074|1075|698|953|621|1009|680|622|1108|669|1086|978|594|611|610|592|675|612|1010|590|726|683|609|627|974|712|684|955|596&dd=2024-07-01&ka1=10&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-08-31&to=4305|2682|4308|4312|1837|2933|3437|483&tt=1"

URL_SRLs_list_FWSK = [URL_SRL_FWSK1, URL_SRL_FWSK2, URL_SRL_FWSK3, URL_SRL_FWSK4, URL_SRL_FWSK5, URL_SRL_FWSK6, URL_SRL_FWSK7, URL_SRL_FWSK8, URL_SRL_FWSK9, URL_SRL_FWSK10, URL_SRL_FWSK11, URL_SRL_FWSK12]



from FWSK.to_import import URL_local
class Test_SRL_C_comparer(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None, run_number=None):
        self.run_number = run_number
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)


    def tearDown(self):
        tearDown(self)


    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_FWSK)



        self.test_passed = True