from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ND.to_import import URL, closeExponeaBanner, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://new.nev-dama.cz/"
URL_SRL_ND1 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2023-12-20&nn=6|7|8&rd=2024-02-19&tt=3"

URL_SRL_ND2 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2024-03-01&nn=4|5|6|7&rd=2024-04-30&tt=3"

URL_SRL_ND3 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"

URL_SRL_ND4 = "/zima/vysledky-vyhledavani?ac1=2&d=85305|85311|85336|85350|85372|85377|85324|85333|85367|85369|85374&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"

URL_SRL_ND5 = "/zima/vysledky-vyhledavani?ac1=2&d=85383|85385|85394|85407|85413|108815|85434|85436&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"

URL_SRL_ND6 = "/zima/vysledky-vyhledavani?ac1=2&d=213243|213244|86483|213242|85199|85202&dd=2024-04-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-05-31&tt=3"

URL_SRL_ND7 = "/zima/vysledky-vyhledavani?ac1=2&d=85272|85278|85294|85298|85301|85268|85226|85286&dd=2024-04-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-05-31&tt=3"

URL_SRL_ND8 = "/leto/vysledky-vyhledavani?ac1=2&d=217142|217071|217093|217098|217101|217136|217127|217085|217106|217110|217146|217112|217117|217074|217125|217528|217525|217530|217134&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND9 = "/leto/vysledky-vyhledavani?ac1=2&d=108939|108938|108941|109497|108940|108942&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND10 = "/leto/vysledky-vyhledavani?ac1=2&d=109011&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND11 = "/leto/vysledky-vyhledavani?ac1=2&d=217207|217192|217211|217200|217230|217220|217222|217213|217216&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND12 = "/leto/vysledky-vyhledavani?ac1=2&d=108905|108908|108911|217152&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND13 = "/leto/vysledky-vyhledavani?ac1=2&d=108914|108916|108918|217161|108915|108917|217189&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND14 = "/leto/vysledky-vyhledavani?ac1=2&d=217238|217317|217314&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRL_ND15 = "/leto/vysledky-vyhledavani?ac1=2&d=217238|217317|217314&dd=2024-06-01&nn=6|7|8&rd=2024-07-31&tt=0"

URL_SRLs_list_ND = [URL_SRL_ND1, URL_SRL_ND2, URL_SRL_ND3, URL_SRL_ND4, URL_SRL_ND5, URL_SRL_ND6, URL_SRL_ND7, URL_SRL_ND8, URL_SRL_ND9, URL_SRL_ND10, URL_SRL_ND11, URL_SRL_ND12, URL_SRL_ND13, URL_SRL_ND14, URL_SRL_ND15]

from ND.to_import import URL_local
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
        list_SRL_number_of_results(self.driver, URL, URL_public_prod, URL_SRLs_list_ND)



        self.test_passed = True