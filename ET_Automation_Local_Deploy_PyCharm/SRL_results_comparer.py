from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ET_Automation_Local_Deploy_PyCharm.to_import import URL, closeExponeaBanner, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://www.etravel.cz/"
URL_SRL_ET1 = "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425|64422|64423&dd=2024-06-01&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET2 = "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425|64422|64423&dd=2024-10-01&nn=7|8|9|10|11|12|13|14&rd=2024-11-30&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET3 = "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425|64422|64423&dd=2024-10-01&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-11-30&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET4 = "/vysledky-vyhledavani?ac1=2&d=63252|63447|63260|63448|63288|64154|64152|64153|64157&dd=2024-10-31&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13|14&rd=1970-01-01&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET5 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64087|64094|64089|64090|64091|64092|64095|64086|64096|64093&dd=2024-09-01&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET6 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63865|63862|63863|63866|63864&dd=2024-09-01&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET7 = "/vysledky-vyhledavani?ac1=2&d=63865|63862|63863|63866|63864&dd=2024-09-01&ic1=1&ka1=8&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET8 = "/vysledky-vyhledavani?ac1=2&d=63220|63281|63311|63314|63316|63319|63324|63333|63373|63390|63402|63408|63409|63442|63471|63219|63341|63428|63472&dd=2024-09-01&ic1=1&ka1=8&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET9 = "/vysledky-vyhledavani?ac1=2&d=63232|63247|63249|63250|63251|63280|63289|63528|63325|63326|77802|63527|63345|63361|63381|63526|63401|63450|77804|63461|63470&dd=2024-09-01&ic1=1&ka1=8&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET10 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63720|63719|63716&dd=2024-09-01&ic1=1&ka1=8&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET11 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63720|63719|63716&dd=2024-09-01&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET12 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63213|63226|63241|63267|74459|74460|63284|74464|63350|63354|63360|74465|63216|63242|63244|74462|63313|74461|74463|63349|63455&dd=2024-09-01&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET13 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63972|63973|63974|63975|63976|63977|63978|63979|63980|63981|63982|63983|63984|63985|63986|63987|63988|64037&dd=2024-11-01&ds=0&ifm=0&ilm=0&nn=7|8|9|10|11|12|13|14&rd=2024-12-31&sc=residential&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET14 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64077&dd=2024-11-01&ds=0&ifm=0&ilm=0&nn=7|8|9|10|11|12|13|14&rd=2024-12-31&sc=residential&to=4312|4305|2682|4308|4309&tt=1"

URL_SRL_ET15 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64075|64076|64447&dd=2024-11-01&ds=0&ifm=0&ilm=0&nn=7|8|9|10|11|12|13|14&rd=2024-12-31&sc=residential&to=4312|4305|2682|4308|4309&tt=1"

URL_SRLs_list_ET = [URL_SRL_ET1, URL_SRL_ET2, URL_SRL_ET3, URL_SRL_ET4, URL_SRL_ET5, URL_SRL_ET6, URL_SRL_ET7, URL_SRL_ET8, URL_SRL_ET9, URL_SRL_ET10, URL_SRL_ET11, URL_SRL_ET12, URL_SRL_ET13, URL_SRL_ET14, URL_SRL_ET15]

class Test_SRL_C_comparer(unittest.TestCase):
    def setUp(self):
        setUp(self)


    def tearDown(self):
        tearDown(self)


    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, URL, URL_public_prod, URL_SRLs_list_ET)



        self.test_passed = True