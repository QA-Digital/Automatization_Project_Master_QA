from selenium.webdriver.common.by import By
from KTGSK.to_import import URL, setUp, tearDown
import unittest
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results
from helpers.helper import Helpers

URL_public_prod = "https://kartago.sk"


URL_SRL_KTGSK1 = "/vysledky-vyhladavania?ac1=2&d=64086|64087|64089|64090|64091|64092|64093|64094|64095|64096&dd=2024-07-01&ic1=1&ka1=12&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-08-31&to=483|1837|2933|3437|4312|4305|2682|4308&tt=1"

URL_SRL_KTGSK2 = "/vysledky-vyhladavania?ac1=2&d=64419|64420|211814|63448|64425|211801|63260&dd=2023-10-01&nn=7|8|9|10|11|12|13&rd=2023-11-30&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK3 = "/vysledky-vyhladavania?ac1=2&ac2=4&d=63715|63716|63717|63718|63719|63720|63721|63722|63723|63724&dd=2024-07-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=12&ka2=4|16&kc1=1&kc2=2&nn=7|8|9|10|11|12|13&rd=2024-08-31&sc=residential&to=483|1837|2933|3437|4312|4305|2682|4308&tt=1"

URL_SRL_KTGSK4 = "/vysledky-vyhladavania?ac1=2&d=63316|63319|63324|63333|63402|63471|211764|63350|63220|63281|63311|63314|63373|63390|63408|63409|63442|63213|63216|63218|63226|63227|63231|64429|63241|63242|63243|63244|63245|74462|63263|63267|74459|63272|74460|63284|63299|63334|63312|63313|74461|77806|74463|63328|74464|63349|64430|63354|63360|63363|74465|63455&dd=2023-09-01&ic1=1&ka1=10&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK5 = "/vysledky-vyhladavania?ac1=2&d=63252|63447&dd=2023-09-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=4&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK6 = "/vysledky-vyhladavania?ac1=2&ac2=4&d=63484|64420|64423|63220|63316|63319|63324|63333|63402|63471|63719|63483|63281|63311|63314|63373|63390|63408|63409|63442&dd=2024-07-01&ic1=1&ka1=12&ka2=4|16&kc1=1&kc2=2&nn=7|8|9|10|11|12|13&rd=2024-08-31&to=483|1837|2933|3437|4312|4305|2682|4308&tt=1"

URL_SRL_KTGSK7 = "/vysledky-vyhladavania?ac1=2&d=63205|63212|63215|63229|63255|63265|63271|63287|63296|63298|63329|63330|63339|63356|63376|63391|63404|63406|63410|63422|63425|63426|63429|63436|63444|63453|63454|63456|63457|63459|63537|63538|63539|64427|64428&dd=2023-09-01&ds=0&ic1=1&ifm=0&ilm=0&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK8 = "/vysledky-vyhladavania?ac1=2&d=63715|63716|63717|63718|63719|63720|63721|63722|63723|63724&dd=2023-09-01&ds=0&ic1=1&ifm=0&ilm=0&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK9 = "/vysledky-vyhladavania?ac1=2&d=63260|63288|63448|64152|64153|64154|64157|211801|211814&dd=2023-09-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=4|7&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_KTGSK10 = "/vysledky-vyhladavania?ac1=2&ac2=3&d=64161|64167|64171|64166|64169|64172|64174|64159|64168|64162|64170|64164|64176|64160|64173|64175|64163|64165|63582|63581|63580|63707|63708|63710|63972|63984|63977|63979|63981|63976|63988|63978|63975|63980|63982|63974|63973|63985|63987|63986|64037|63983&dd=2024-07-01&ic1=1&ka1=12&ka2=4|16&kc1=1&kc2=2&nn=7|8|9|10|11|12|13&rd=2024-08-31&to=483|1837|2933|3437|4312|4305|2682|4308&tt=1"

URL_SRL_KTGSK11 = "/vysledky-vyhladavania?ac1=1&ac2=3&d=64419|64420|64423|211764|63350|64425|63582|63581|63580|63213|63216|63218|63226|63227|63231|64429|63241|63242|63243|63244|63245|74462|63263|63267|74459|63272|74460|63284|63299|63334|63312|63313|74461|77806|74463|63328|74464|63349|64430|63354|63360|63363|74465|63455&dd=2024-07-01&ic1=1&ka1=12&ka2=4|16&kc1=1&kc2=2&nn=7|8|9|10|11|12|13&rd=2024-08-31&to=483|1837|2933|3437|4312|4305|2682|4308&tt=1"

URL_SRL_KTGSK12 = "/vysledky-vyhladavania?ac1=4&d=64419|64420|64421|64422|64423|64424|64425|64426&dd=2023-10-01&ds=0&ifm=0&ilm=0&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&sc=residential&to=483|1837|2933|3437&tt=1"


URL_SRLs_list_KTGSK = [URL_SRL_KTGSK1, URL_SRL_KTGSK2, URL_SRL_KTGSK3, URL_SRL_KTGSK4, URL_SRL_KTGSK5, URL_SRL_KTGSK6, URL_SRL_KTGSK7, URL_SRL_KTGSK8, URL_SRL_KTGSK9, URL_SRL_KTGSK10, URL_SRL_KTGSK11, URL_SRL_KTGSK12]

from FW.SRL_results_comparer import destinations, airports
base_url = "/vysledky-vyhladavania/"
URL_SRLs_list_KTGSK = Helpers.generate_srl_urls(base_url, destinations,airports, 25)


from KTGSK.to_import import URL_local
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
       # list_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_KTGSK)

        Helpers.compare_SRL_number_of_results(self.driver, self.URL, URL_public_prod, URL_SRLs_list_KTGSK, self.logger)

        self.test_passed = True