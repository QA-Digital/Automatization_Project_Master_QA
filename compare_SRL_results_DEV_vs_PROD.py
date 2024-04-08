import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

##open SRLS , take h1, compare pocet vysledku VS dev ENV
from random_printer import checked_URLs_list

#driver = webdriver.Chrome(ChromeDriverManager().install())
URL_prod = "https://www.fischer.cz/"
URL_dev = "https://fischer.web2.dtweb.cz/"
#URL_dev = "https://fischer.web3.dtweb.cz/"
# URL1 = URL+ "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2022-12-01&nn=7&rd=2023-01-31&to=4312|4305|2682|4308&tt=1"
# URL2 = URL+ "vysledky-vyhledavani?ac1=2&d=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL3 = URL+ "vysledky-vyhledavani?ac1=2&d=1006|1007|1008&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL4 = URL+ "vysledky-vyhledavani?ac1=2&d=664&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL5 = URL+ "vysledky-vyhledavani?ac1=2&d=756&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL6 = URL+ "vysledky-vyhledavani?ac1=2&d=661&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL7 = URL+ "vysledky-vyhledavani?ac1=2&d=1111&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL8 = URL+ "vysledky-vyhledavani?ac1=2&d=790&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL9 = URL+ "vysledky-vyhledavani?ac1=2&d=633|994&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL10 = URL+ "vysledky-vyhledavani?ac1=2&d=634&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL11 = URL+ "vysledky-vyhledavani?ac1=2&d=631&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL12 = URL+ "vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL13 = URL+ "vysledky-vyhledavani?ac1=2&d=638&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"

URL1 = "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2022-12-01&nn=7&rd=2023-01-31&to=4312|4305|2682|4308&tt=1"
URL2 = "vysledky-vyhledavani?ac1=2&d=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL3 = "vysledky-vyhledavani?ac1=2&d=1006|1007|1008&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL4 = "vysledky-vyhledavani?ac1=2&d=664&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL5 =  "vysledky-vyhledavani?ac1=2&d=756&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL6 = "vysledky-vyhledavani?ac1=2&d=661&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL7 = "vysledky-vyhledavani?ac1=2&d=1111&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL8 =  "vysledky-vyhledavani?ac1=2&d=790&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL9 ="vysledky-vyhledavani?ac1=2&d=633|994&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL10 = "vysledky-vyhledavani?ac1=2&d=634&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL11 = "vysledky-vyhledavani?ac1=2&d=631&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL12 ="vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL13 =  "vysledky-vyhledavani?ac1=2&d=638&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL14 = "vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1"

####
URL15 = "vysledky-vyhledavani?ac1=2&d=958|664|687|604|1005|1008|1007|653|819|724|634|756|751|605|677|680|1108|953|611|610|592|612|590|726|609|1066|1006|745|1061|965|822|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-07-01&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL16 = "vysledky-vyhledavani?ac1=2&d=958|664|687|604|1005|1008|1007|653|819|724|634|756|751|605|677|680|1108|953|611|610|592|612|590|726|609|790|607|591|627|974|712|596|1066|1006|745|1061|965|822|621|1009|622|669|1086|1194|670|978|594|675|1010|683|636|950|980|945|951|947|946&dd=2023-07-01&ka1=12|4&kc1=2&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL17 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=860|1050|1039|859|875|1043|1044|1057&dd=2022-12-22&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=1|2|3|4|5|6|7|8|9|10|11|12&rd=2023-02-21&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL18 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=1182|1190|1184|1183|1178&dd=2022-12-22&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=1|2|3|4|5|6|7|8|9|10|11|12&rd=2023-02-21&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL19 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=1051&dd=2023-08-01&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=7|8|9&rd=2023-09-30&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL20 = "vysledky-vyhledavani?ac1=3&d=664|687|604|1225|623|741|735|618|619|624|973|993|595|648|972|620|746|680|1108|953|611|610|592|612|590|726|609|607|591|627|974|712|596|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-04-01&ic1=1&ka1=11&kc1=1&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL21 = "vysledky-vyhledavani?ac1=3&d=1008|1007|1111|661|605|677|1225|623|741|735|618|619|624|973|993|595|648|972|620|746|1066|1006|745|1061|965|822|636|950|980|945|951|947|946&dd=2023-04-01&ic1=1&ka1=11&kc1=1&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL22 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=626|957|589&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"
URL23 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=608&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"
URL24 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=1133|606|860|870|1098|770|1050|1134|823|1039|1109|644|643|674|871|1172|805|875|791|815|1040|1041|869|629|642|1078|616|859|1079|962|1042|1043|1044|1045|1057&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"

URL_List = [URL1,URL2, URL3, URL4, URL5,URL6, URL7,URL8,URL9,URL10,URL11,URL12,URL13, URL14, URL15, URL16, URL17, URL18, URL19, URL20, URL21, URL22, URL23, URL24]
#URL_List = [URL1,URL2]

URL_dev_EXPL = "https://eximpl.web11.dtweb.cz/"
URL_PL1 = "/wyszukanie?ac1=2&d=63484|63483|64419|64420|64425&dd=2023-11-01&nn=6|7|8|9|10|11|12|13|14&rd=2023-11-30&tt=1"
URL_PL2 = "/wyszukanie?ac1=2&d=63448|63288&dd=2024-01-15&nn=7|8|9|10|11|12|13&rd=2024-02-25&tt=1"
URL_PL3 = "/wyszukanie?ac1=2&d=63252|63447&dd=2024-01-15&ic1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&tt=1"
URL_PL4 = "/wyszukanie?ac1=2&d=63213|63241|74459|74460|74463|74464|74465&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL5 = "/wyszukanie?ac1=2&d=63580|63581&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL6 = "/wyszukanie?ac1=2&d=63738&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL7 = "/wyszukanie?ac1=2&d=64126|64127|64128&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL8 = "/wyszukanie?ac1=2&d=64076&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL9 = "/wyszukanie?ac1=2&d=63252&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL10 = "/wyszukanie?ac1=2&d=63864|63865&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL11 = "/wyszukanie?ac1=2&d=64246&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL12 = "/wyszukanie?ac1=2&d=63757|63758|63759&dd=2024-01-15&ds=0&ic1=1&ifm=0&ilm=0&ka1=9&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-02-25&sc=residential&tt=1"
URL_PL13 = "/wyszukanie?ac1=2&d=64419|64420|64425&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_PL14 = "/wyszukanie?ac1=2&d=63213|63241|74459|74460|74463|74464|74465&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_PL15 = "/wyszukanie?ac1=2&d=63707|63710&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_PL16 = "/wyszukanie?ac1=2&d=64126|64127|64128&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_PL17 = "/wyszukanie?ac1=2&d=63252&dd=2024-01-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=9|5&kc1=2&nn=7|8|9|10|11|12|13&rd=2024-02-29&sc=residential&tt=1"
URL_PL18 = "/wyszukanie?ac1=2&d=63343|63348&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"
URL_PL19 = "/wyszukanie?ac1=2&d=63982&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"
URL_PL20 = "/wyszukanie?ac1=2&d=64419|64420|64425&dd=2024-03-01&ds=0&ifm=0&ilm=0&ka1=8&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&sc=residential&tt=1"

URL_dev_List_PL = [URL_PL1, URL_PL2, URL_PL3, URL_PL4, URL_PL5, URL_PL6, URL_PL7, URL_PL8, URL_PL9, URL_PL10, URL_PL11, URL_PL12, URL_PL13, URL_PL14, URL_PL15, URL_PL16, URL_PL17, URL_PL18, URL_PL19, URL_PL20]

URL_dev_DERRO = "https://dertourro.web11.dtweb.cz/"
URL_DERRO1 = "/rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2023-11-01&nn=7|8|9|10|11|12|13&rd=2024-01-01&sortby=PriceTotal&sortorder=1&tt=1"
URL_DERRO2 = "/rezultatele-cautarii?ac1=2&d=64421|64422|64426|64424|64423|64419|64420|64425&dd=2023-11-01&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-01-01&tt=1"
URL_DERRO3 = "/rezultatele-cautarii?ac1=2&d=64087|64089|64090|64091|64086&dd=2024-02-29&ic1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO4 = "/rezultatele-cautarii?ac1=2&d=64087|64089|64090|64091|64086&dd=2024-02-29&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO5 = "/rezultatele-cautarii?ac1=2&d=63885|63890|63891|63889|63892|63888|63886|63887&dd=2024-02-29&ic1=1&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO6 = "rezultatele-cautarii?ac1=2&d=63885|63890|63891|63889|63892|63888|63886|63887&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO7 = "/rezultatele-cautarii?ac1=2&d=64168|64162|64161|64167|64171|64166|64169|64172|64174|64159|64170|64164|64176|64160|64173|64175|64163|64165&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO8 = "/rezultatele-cautarii?ac1=2&d=64168|64162|64161|64167|64171|64166|64169|64172|64174|64159|64170|64164|64176|64160|64173|64175|64163|64165&dd=2024-02-29&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO9 = "/rezultatele-cautarii?ac1=2&d=63738&dd=2024-02-29&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO10 = "/rezultatele-cautarii?ac1=2&d=63738&dd=2024-02-29&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO11 = "/rezultatele-cautarii?ac1=2&d=63972|63984|63977|63979|63981|64037|63976|63988|63978|63975|63980|63982|63974|63973|63985|63987|63986|63983&dd=2024-02-29&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO12 = "/rezultatele-cautarii?ac1=2&d=63972|63984|63977|63979|63981|64037|63976|63988|63978|63975|63980|63982|63974|63973|63985|63987|63986|63983&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO13 = "/rezultatele-cautarii?ac1=2&d=64102|64099&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO14 = "/rezultatele-cautarii?ac1=2&d=63992|63994|63995|75728|75729|63993|75730|77252|75731|77253&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO15 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-05-01&nn=7|8|9|10|11|12|13&rd=2024-06-30&tt=1"
URL_DERRO16 = "/rezultatele-cautarii?ac1=2&d=63763|63764|63767|63766|63765&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO17 = "/rezultatele-cautarii?ac1=2&d=64144|64128|64126|64127|64133|64130&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO18 = "/rezultatele-cautarii?ac1=2&d=64144|64128|64126|64127|64133|64130&dd=2024-02-29&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO19 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-02-29&ka1=6&kc1=1&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"
URL_DERRO20 = "/rezultatele-cautarii?ac1=2&d=64157|63288|212113|211801|63260|63448|64152|64153|64154|211814&dd=2024-02-29&nn=7|8|9|10|11|12|13&rd=2024-04-30&tt=1"

URL_dev_List_DERRO = [URL_DERRO1, URL_DERRO2, URL_DERRO3, URL_DERRO4, URL_DERRO5, URL_DERRO6, URL_DERRO7, URL_DERRO8, URL_DERRO9, URL_DERRO10, URL_DERRO11, URL_DERRO12, URL_DERRO13, URL_DERRO14, URL_DERRO15, URL_DERRO16, URL_DERRO17, URL_DERRO18, URL_DERRO19, URL_DERRO20]

URL_dev_ND = "https://nev-dama.web11.dtweb.cz/"
URL_ND01 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2023-12-20&nn=6|7|8&rd=2024-02-19&tt=3"
URL_ND02 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2024-03-01&nn=4|5|6|7&rd=2024-04-30&tt=3"
URL_ND03 = "/zima/vysledky-vyhledavani?ac1=2&d=86544|213248|86560|213249|213250|213251|213253|213252|213247|213255|86549|86550|86551|198035|213258|86547|86552|86553|213266|86557|86558|217571|86546|213254&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"
URL_ND04 = "/zima/vysledky-vyhledavani?ac1=2&d=85305|85311|85336|85350|85372|85377|85324|85333|85367|85369|85374&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"
URL_ND05 = "/zima/vysledky-vyhledavani?ac1=2&d=85383|85385|85394|85407|85413|108815|85434|85436&dd=2024-03-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-04-30&tt=3"
URL_ND06 = "/zima/vysledky-vyhledavani?ac1=2&d=213243|213244|86483|213242|85199|85202&dd=2024-04-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-05-31&tt=3"
URL_ND07 = "/zima/vysledky-vyhledavani?ac1=2&d=85272|85278|85294|85298|85301|85268|85226|85286&dd=2024-04-01&ic1=1&ka1=5&kc1=1&nn=4|5|6|7&rd=2024-05-31&tt=3"
URL_ND08 = "/leto/vysledky-vyhledavani?ac1=2&d=217142|217071|217093|217098|217101|217136|217127|217085|217106|217110|217146|217112|217117|217074|217125|217528|217525|217530|217134&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND09 = "/leto/vysledky-vyhledavani?ac1=2&d=108939|108938|108941|109497|108940|108942&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND10 = "/leto/vysledky-vyhledavani?ac1=2&d=109011&dd=2024-06-01&ic1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND11 = "/leto/vysledky-vyhledavani?ac1=2&d=217207|217192|217211|217200|217230|217220|217222|217213|217216&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND12 = "/leto/vysledky-vyhledavani?ac1=2&d=108905|108908|108911|217152&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND13 = "/leto/vysledky-vyhledavani?ac1=2&d=108914|108916|108918|217161|108915|108917|217189&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND14 = "/leto/vysledky-vyhledavani?ac1=2&d=217238|217317|217314&dd=2024-06-01&ic1=1&ka1=5&kc1=1&nn=6|7|8&rd=2024-07-31&tt=0"
URL_ND15 = "/leto/vysledky-vyhledavani?ac1=2&d=217238|217317|217314&dd=2024-06-01&nn=6|7|8&rd=2024-07-31&tt=0"

URL_dev_List_ND = [URL_ND01, URL_ND02, URL_ND03, URL_ND04, URL_ND05, URL_ND06, URL_ND07, URL_ND08, URL_ND09, URL_ND10, URL_ND11, URL_ND12, URL_ND13, URL_ND14, URL_ND15]


def list_SRL_number_of_results(driver, URL_default, URL_dev ,URL_parameters_list):
    driver.get(URL_default)
    time.sleep(1)
    driver.maximize_window()
    acceptConsent(driver)
    time.sleep(5)
    windowHandle = 1
    listPosition = 0

    ##default pocitejme jako PROD

    global pocet_vysledku_list_default
    pocet_vysledku_list_default = []


    global checked_URLs_list_default
    checked_URLs_list_default = []

    global pocet_vysledku_list_dev
    pocet_vysledku_list_dev = []

    global checked_URLs_list_dev
    checked_URLs_list_dev = []


    #print(len(URL_parameters_list))
    for _ in URL_parameters_list:
        #driver.execute_script("window.open("");")
        #driver.switch_to.window(driver.window_handles[windowHandle])
        linkActualUrl = URL_default + URL_parameters_list[listPosition]
        time.sleep(3)
        driver.get(linkActualUrl)
        time.sleep(3)
        SRL_H1textPocetNalezenychZajezduXpath = "//h1"

        pocetNalezenychZajezduElement = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        pocet_vysledku_list_default.append(pocetNalezenychZajezduElement)

        checked_URLs_list_default.append(linkActualUrl)

        #print(pocetNalezenychZajezduElement)
        #print(linkActualUrl)
        windowHandle = windowHandle + 1
        listPosition = listPosition + 1

    windowHandle = 1
    listPosition = 0
    for _ in URL_parameters_list:
        #driver.execute_script("window.open("");")
        #driver.switch_to.window(driver.window_handles[windowHandle])
        linkActualUrl = URL_dev + URL_parameters_list[listPosition]
        #driver.get(URL_dev + "/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
        time.sleep(3)
        driver.get(linkActualUrl)
        SRL_H1textPocetNalezenychZajezduXpath = "//h1"

        pocetNalezenychZajezduElement = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        pocet_vysledku_list_dev.append(pocetNalezenychZajezduElement)

        checked_URLs_list_dev.append(linkActualUrl)

        #print(pocetNalezenychZajezduElement)
        #print(linkActualUrl)
        windowHandle = windowHandle + 1
        listPosition = listPosition + 1

    starterPosition = 0
    print("len(pocet_vysledku_list_default)")
    print(len(pocet_vysledku_list_default))

    print("             ")

    print("len(pocet_vysledku_list_dev))")
    print(len(pocet_vysledku_list_dev))

    for _ in pocet_vysledku_list_default:
        if pocet_vysledku_list_default[starterPosition] == pocet_vysledku_list_dev[starterPosition]:
            #starterPosition=starterPosition+1
            print(pocet_vysledku_list_default[starterPosition])
            print(pocet_vysledku_list_dev[starterPosition])
            print(checked_URLs_list_default[starterPosition])
            print(checked_URLs_list_dev[starterPosition])
            print("             ")


        if pocet_vysledku_list_default[starterPosition] != pocet_vysledku_list_dev[starterPosition]:
            print(pocet_vysledku_list_default[starterPosition])
            print(pocet_vysledku_list_dev[starterPosition])
            print(checked_URLs_list_default[starterPosition])
            print(checked_URLs_list_dev[starterPosition])
            print("             ")


        print(starterPosition)
        starterPosition = starterPosition + 1

    print(len(pocet_vysledku_list_default))


#list_SRL_number_of_results(driver, URL_prod, URL_dev ,URL_List)














































# windowHandle = 1
# listPosition = 0
# for _ in URL_List:
#     driver.execute_script("window.open("");")
#     driver.switch_to.window(driver.window_handles[windowHandle])
#     linkActualUrl = URL_List[listPosition]
#     driver.get(URL+"/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
#     time.sleep(3)
#     driver.get(linkActualUrl)
#     SRL_H1textPocetNalezenychZajezduXpath = "//h1"
#     pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
#     print(pocetNalezenychZajezduElement_PROD)
#     print(linkActualUrl)
#     windowHandle = windowHandle + 1
#     listPosition = listPosition + 1
#
# for _ in URL_List:
#     driver.execute_script("window.open("");")
#     driver.switch_to.window(driver.window_handles[windowHandle])
#     linkActualUrl = URL_List[listPosition]
#     driver.get(URL_dev+"/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
#     time.sleep(3)
#     driver.get(linkActualUrl)
#     SRL_H1textPocetNalezenychZajezduXpath = "//h1"
#     pocetNalezenychZajezduElement_DEV = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
#     print(pocetNalezenychZajezduElement_DEV)
#     print(linkActualUrl)
#     windowHandle = windowHandle + 1
#     listPosition = listPosition + 1