from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW.to_import import URL, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results
from helpers.helper import Helpers

URL_public_prod = "https://fischer.cz"
import re
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')
# Define the new value for the "rd" parameter
new_rd_value = "2024-11-30"

URL_SRL_FW1 = "/vysledky-vyhledavani?ac1=2&d=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&dd=" + current_date + "&ds=0&ic1=1&ifm=0&ilm=0&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&sc=residential&to=4312|4305|2682|4308&tt=1"

URL_SRL_FW2 = "/vysledky-vyhledavani?ac1=2&d=1225|623|741|735|618|619|624|973|993|595|648|972|620|746&dd=" + current_date + "&ic1=2&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308&tt=1"

URL_SRL_FW3 = "/vysledky-vyhledavani?ac1=2&d=653|819|724&dd=" + current_date + "&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW4 = "/vysledky-vyhledavani?ac1=2&d=650|651|649|876&dd=" + current_date + "&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW5 = "/vysledky-vyhledavani?ac1=2&d=644|674|642|616|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=" + current_date + "&ic1=1&ka1=10&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW6 = "/vysledky-vyhledavani?ac1=2&d=654|634&dd=" + current_date + "&ic1=1&ka1=10&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW7 = "/vysledky-vyhledavani?ac1=2&d=607|591&dd=" + current_date + "&ic1=1&ka1=10|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW8 = "/vysledky-vyhledavani?ac1=2&d=627|974|712|596&dd=" + current_date + "&ic1=1&ka1=10|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW9 = "/vysledky-vyhledavani?ac1=2&d=635&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW10 = "/vysledky-vyhledavani?ac1=2&d=605|677|745|1061|965|822&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW11 = "/vysledky-vyhledavani?ac1=2&d=654&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW12 = "/vysledky-vyhledavani?ac1=2&d=631&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|183"

URL_SRL_FW13 = "/vysledky-vyhledavani?ac1=2&d=638|1214|635&dd=" + current_date + "&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW14 = "/vysledky-vyhledavani?ac1=2&d=654&dd=" + current_date + "&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW15 = "/vysledky-vyhledavani?ac1=2&d=633&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW16 = "/vysledky-vyhledavani?ac1=2&d=1005&dd=" + current_date + "&ka1=15&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW17 = "/vysledky-vyhledavani?ac1=2&d=687|604&dd=" + current_date + "&ka1=15|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW18 = "/vysledky-vyhledavani?ac1=2&d=650|651|649|876|644|674|642|616|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=" + current_date + "&ka1=15|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW19 = "/vysledky-vyhledavani?ac1=2&d=653|819|724&dd=" + current_date + "&ka1=3&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW20 = "/vysledky-vyhledavani?ac1=2&d=664&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW21 = "/vysledky-vyhledavani?ac1=2&d=680|1108|953|669|670|594|611|610|592|612|590|726|609|621|1009|622|1086|1194|978|675|683&dd=2024-02-01&nn=7|8|9|10|11|12|13|14&rd=2024-03-31&sortby=PriceTotal&sortorder=1&to=4312&tt=1"

URL_SRL_FW22 = "/vysledky-vyhledavani?ac1=2&d=631&dd=2024-02-01&nn=7|8|9|10|11|12|13|14&rd=2024-03-31&sortby=PriceTotal&sortorder=1&to=4312&tt=1"

URL_SRL_FW23 = "/vysledky-vyhledavani?ac1=2&d=790&dd=2024-08-01&ic1=1&ka1=7&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312&tt=1"

URL_SRL_FW24 = "/vysledky-vyhledavani?ac1=2&ac2=3&d=653|819|724|870|644|674|642|616|1225|623|741|735|618|619|624|973|1115|709|993|595|648|972|620|746|621|680|622|1108|953|669|670|594|611|610|592|612|590|726|609|1133|606|860|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057|1009|1086|1194|978|675|683&dd=2024-06-01&ic1=1&ic2=1&ka1=5&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_FW25 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=664|1111|1225|623|741|735|618|619|624|973|1115|709|993|595|648|972|620|746&dd=2024-06-01&ic1=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_FW26 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=664|1111|1225|623|741|735|618|619|624|973|1115|709|993|595|648|972|620|746&dd=2024-06-01&ic1=1&ka1=10|15&ka2=4|13&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_FW27 = "/vysledky-vyhledavani?ac1=3&ac2=2&d=687|604|1008|1007|607|591|627|974|712|596|1066|1006&dd=2024-06-01&ic1=1&ka1=10|15&ka2=4|13&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_FW28 = "/vysledky-vyhledavani?ac1=3&ac2=2&d=661|608|605|677|764|745|965|822&dd=2024-06-01&ic1=1&ic2=1&ka1=10|15&ka2=4|13&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_FW29 ="/vysledky-vyhledavani?ac1=3&ac2=3&d=870|644|674|642|616|634|1225|623|741|735|618|619|624|973|1115|709|993|595|648|972|620|746|790|1133|606|860|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=2024-06-01&ic1=1&ic2=1&ka1=10|15&ka2=4|13&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309|483|1837|2933|3437|3248|298|874|892|983|1091|1293|1956|2397|2563|3352&tt=1"

URL_SRL_FW30 = "/vysledky-vyhledavani?ac1=3&ac2=4&d=653|819|724|650|651|649|876|756|607|591&dd=2024-06-01&ic1=1&ic2=1&ka1=10|15&ka2=4|13&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309|483|1837|2933|3437|3248|298|874|892|983|1091|1293|1956|2397|2563|3352&tt=1"

URL_SRLs_list_FW = [URL_SRL_FW1, URL_SRL_FW2, URL_SRL_FW3, URL_SRL_FW4, URL_SRL_FW5, URL_SRL_FW6, URL_SRL_FW7, URL_SRL_FW8, URL_SRL_FW9, URL_SRL_FW10, URL_SRL_FW11, URL_SRL_FW12, URL_SRL_FW13, URL_SRL_FW14, URL_SRL_FW15, URL_SRL_FW16, URL_SRL_FW17, URL_SRL_FW18, URL_SRL_FW19, URL_SRL_FW20, URL_SRL_FW21, URL_SRL_FW22, URL_SRL_FW23,
                    URL_SRL_FW24, URL_SRL_FW25, URL_SRL_FW26, URL_SRL_FW27,URL_SRL_FW28, URL_SRL_FW29,URL_SRL_FW30    ]


from FW.to_import import URL_local

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
        Helpers.compare_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_FW, self.logger)

        #list_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_FW)



        self.test_passed = True