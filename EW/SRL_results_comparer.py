from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import URL, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit, URL_SRL_kuba_regres
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter
from EW.SRL_D import SRL_D
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results
from helpers.helper import Helpers

from FW.SRL_results_comparer import destinations, airports

URL_public_prod = "https://eximtours.cz"
from datetime import datetime
current_date = datetime.now().strftime('%Y-%m-%d')
new_rd_value = "2024-11-30"

URL_SRL_EW1 = "/vysledky-vyhledavani?ac1=2&d=63258|63294|63337|63443&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW2 = "/vysledky-vyhledavani?ac1=2&d=63484|63483&dd=" + current_date + "&ic1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW3 = "/vysledky-vyhledavani?ac1=1&ac2=4&d=63541|63208|63348|63220|63281|63311|63314|63316|63319|63324|63333|63341|63362|63373|63390|63402|63408|63409|63442|63471|63213|211764|63241|63242|63243|63245|74459|74460|63284|74464|63350|63354|74465|63222|63343|63395|63419|63466|63216|63218|63226|63227|63231|64429|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=" + current_date + "&ic1=1&ic2=1&ka1=5|16&ka2=7|11&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=" + new_rd_value + "&to=4312|4305|2682|4308|4392|4309|483|1837|2933|3437|3248|298|874|892|983|1091|1293|1956|2397|2563|3352|1862|1825|3850|2033|3418|3789|489&tt=1"

URL_SRL_EW4 = "/vysledky-vyhledavani?ac1=2&d=63865|63862|63863|63866|63864&dd=" + current_date + "&ic1=1&ka1=5&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW5 = "/vysledky-vyhledavani?ac1=2&d=64419|64420|64425&dd=" + current_date + "&ic1=1&ka1=5|9&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW6 = "/vysledky-vyhledavani?ac1=2&d=63287|63296|63410|63426|63205|63212|63215|63539|63229|63255|64427|63265|63271|63298|63329|63330|63339|63436|63356|63538|63376|64428|63391|63404|63406|63422|63425|63429|63444|63537|63453|63454|63456|63457|63459&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW7 = "/vysledky-vyhledavani?ac1=2&d=64204|64205|74847|64203&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW8 = "/vysledky-vyhledavani?ac1=2&d=63720|63719|64190&dd=" + current_date + "&nn=3|4|5|6|7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW9 = "/vysledky-vyhledavani?ac1=2&d=63725&dd=" + current_date + "&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW10 = "/vysledky-vyhledavani?ac1=2&d=63889|63891|63888|63890&dd=" + current_date + "&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW11 = "/vysledky-vyhledavani?ac1=2&d=63541&dd=" + current_date + "&ka1=6|3&kc1=2&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW12 = "/vysledky-vyhledavani?ac1=2&d=64161|64167|64171|64166|64169|64172|64174|64159|64168|64162|64170|64164|64176|64160|64173|64175|64163|64165|63582|63581|63580&dd=" + current_date + "&ka1=15|10&kc1=2&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW13 = "/vysledky-vyhledavani?ac1=2&d=63738&dd=" + current_date + "&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW14 = "/vysledky-vyhledavani?ac1=2&d=63982&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW15 = "/vysledky-vyhledavani?ac1=2&d=63220|63281|63311|63314|63316|63319|63324|63333|63373|63390|63402|63408|63409|63442|63471&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308&tt=1"

URL_SRL_EW16 = "/vysledky-vyhledavani?ac1=2&d=63823|63756|63757|63758|63759&dd=" + current_date + "&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308|4312&tt=1"

URL_SRL_EW17 = "/vysledky-vyhledavani?ac1=2&d=211764|63241|213028|63243|63245|74459|74460|63284|74464|63350|63354|74465|63213|63216|63218|63226|63227|63231|64429|63242|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=" + current_date + "&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308|4312&tt=1"

URL_SRL_EW18 = "/vysledky-vyhledavani?ac1=2&d=63252|63447&dd=" + current_date + "&ic1=1&ka1=6|10&kc1=2&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308|4312&tt=1"

URL_SRL_EW19 = "/vysledky-vyhledavani?ac1=2&d=211801|211814|63260|63448&dd=" + current_date + "&ic1=1&ka1=6|10&kc1=2&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308|4312&tt=1"

URL_SRL_EW20 = "/vysledky-vyhledavani?ac1=2&d=64087|64094|64089|64090|64091|64086|64092&dd=" + current_date + "&ka1=4&kc1=1&nn=7|8|9|10|11|12|13&rd=" + new_rd_value + "&to=4305|2682|4308|4312&tt=1"

URL_SRL_EW21 = "/vysledky-vyhledavani?ac1=2&d=211764|63241|213028|63243|63245|74459|74460|63284|74464|63350|63354|74465|63213|63216|63218|63226|63227|63231|64429|63242|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=2024-02-01&nn=7|8|9|10|11|12|13|14&rd=2024-03-31&to=4312&tt=1&DS=2"

URL_SRL_EW22 = "/vysledky-vyhledavani?ac1=1&ac2=4&d=63215|63287|63296|63410|63426|63881|63880|63720|63719|63582|63581|63580|63205|63212|63539|63229|63255|64427|63265|63271|63298|63329|63330|63339|63436|63356|63538|63376|64428|63391|63404|63406|63422|63425|63429|63444|63537|63453|63454|63456|63457|63459&dd=2024-08-28&ic1=1&ic2=1&ka1=5|16&ka2=7|11&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-10-28&to=4312|4305|2682|4308|4392|4309|483|1837|2933|3437|3248|298|874|892|983|1091|1293|1956|2397|2563|3352|1862|1825|3850|2033|3418|3789|489&tt=1"

URL_SRL_EW23 = "/vysledky-vyhledavani?ac1=2&d=63982&dd=2024-02-01&nn=7|8|9|10|11|12|13|14&rd=2024-03-31&sortby=PriceTotal&sortorder=1&to=4312&tt=1"

URL_SRL_EW24 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64419|64420|64425|63208|63348|63213|211764|63241|63242|63243|63245|74459|74460|63284|74464|63350|63354|74465|63222|63343|63395|63419|63466|63216|63218|63226|63227|63231|64429|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=2024-07-01&ka1=5|16&ka2=7|11&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-08-31&to=4312|4305|2682|4308|4392|4309|483|1837|2933|3437|3248|298|874|892|983|1091|1293|1956|2397|2563|3352|1862|1825|3850|2033|3418|3789|489&tt=1&ds=8448"
URL_SRL_EW25 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64419%7C64420%7C64425&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&rd=2024-09-30&to=4312%7C4305%7C2682%7C4308%7C4392%7C4309&tt=1"

URL_SRL_EW26 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64419|64420|64425&dd=2024-07-31&ic1=1&ka1=5&kc1=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309&tt=1"

URL_SRL_EW27 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64419|64420|64425&dd=2024-07-31&ic1=1&ka1=5&ka2=7&kc1=1&kc2=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309|298|874|892|983|1091|1293|1956|2397|2563|3352|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW28 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=63215|63287|63296|63410|63426|63889|63891|63888|63886|63890|63982|63213|211764|63241|63242|63243|63245|74459|74460|63284|74464|63350|63354|74465|63205|63212|63539|63229|63255|64427|63265|63271|63298|63329|63330|63339|63436|63356|63538|63376|64428|63391|63404|63406|63422|63425|63429|63444|63537|63453|63454|63456|63457|63459|63885|63892|63887|63216|63218|63226|63227|63231|64429|63244|74462|63263|63267|63272|63299|63312|63334|63313|74461|77806|74463|63328|63349|64430|63363|63455&dd=2024-07-31&ic1=1&ka1=5&ka2=7&kc1=1&kc2=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309|298|874|892|983|1091|1293|1956|2397|2563|3352|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW29 = "/vysledky-vyhledavani?ac1=2&ac2=3&d=64204|64205|74847|64203|63220|63281|63311|63314|63316|63319|63324|63333|63341|63362|63373|63390|63402|63408|63409|63442|63471|64087|64094|64089|64090|64091|64086|64092|63765&dd=2024-07-31&ic1=1&ic2=1&ka1=5&ka2=7&kc1=1&kc2=1&nn=7|8|9|10|11|12|13|14&rd=2024-09-30&to=4312|4305|2682|4308|4392|4309|298|874|892|983|1091|1293|1956|2397|2563|3352|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW30 = "/vysledky-vyhledavani?ac1=2&ac2=2&d=64087%7C64094%7C64089%7C64090%7C64091%7C64086%7C64092&dd=2024-04-10&ic1=1&ka1=5&kc1=1&nn=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&rd=2024-06-10&to=4312%7C4305%7C2682%7C4308%7C4392%7C4309&tt=1 "

URL_SRL_EW31 = "/vysledky-vyhledavani?ac1=3&ac2=4&d=63484|63483|64419|64420|64425|63982|63208|63348|63222|63343|63395|63419|63466&dd=2024-09-15&ic1=1&ic2=1&ka1=5|16&ka2=7&kc1=2&kc2=1&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4392|4309|298|874|892|983|1091|1293|1956|2397|2563|3352|483|1837|2933|3437|3248&tt=1"

URL_SRL_EW32 = "/vysledky-vyhledavani?ac1=1&ac2=4&d=64419|64420|64425|63252|63447|211801|211814|63260|63448&dd=2024-09-15&ic1=1&ic2=1&ka1=5|16&ka2=7|11&kc1=2&kc2=2&nn=7|8|9|10|11|12|13|14&rd=2024-10-31&to=4312|4305|2682|4308|4392|4309|298|874|892|983|1091|1293|1956|2397|2563|3352|483|1837|2933|3437|3248&tt=1"

# URL_SRLs_list_EW = [URL_SRL_EW1, URL_SRL_EW2, URL_SRL_EW3, URL_SRL_EW4, URL_SRL_EW5, URL_SRL_EW6, URL_SRL_EW7, URL_SRL_EW8, URL_SRL_EW9, URL_SRL_EW10, URL_SRL_EW11, URL_SRL_EW12, URL_SRL_EW13, URL_SRL_EW14, URL_SRL_EW15, URL_SRL_EW16, URL_SRL_EW17, URL_SRL_EW18, URL_SRL_EW19, URL_SRL_EW20, URL_SRL_EW21, URL_SRL_EW22, URL_SRL_EW23,
#                     URL_SRL_EW24, URL_SRL_EW25, URL_SRL_EW26, URL_SRL_EW27, URL_SRL_EW28, URL_SRL_EW29, URL_SRL_EW30, URL_SRL_EW31, URL_SRL_EW32 ]


base_url = "/vysledky-vyhledavani/"
URL_SRLs_list_EW = Helpers.generate_srl_urls(base_url, destinations,airports, 25)
from EW.to_import import URL_local
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
        Helpers.compare_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_EW, self.logger)
        #list_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_EW)



        self.test_passed = True