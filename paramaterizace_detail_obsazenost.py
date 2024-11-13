from selenium.webdriver.common.by import By




#detail_URL = "https://www.fischer.cz/spanelsko/mallorca/alcudia/mariant?DS=256&GIATA=21437&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&HID=21&MT=5&NN=7&DF=2023-10-01|2023-10-31&RD=2023-10-14&DD=2023-10-07&ERM=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=PMI14448&DPR=FISCHER%20ATCOM"
#detail_URL = "https://www.eximtours.cz/egypt/hurghada/hurghada/hawaii-le-jardin?DS=8192&GIATA=99925&D=64419|64420|64425&HID=9184&MT=5&NN=7&DF=2022-12-13|2023-01-31&RD=2022-12-21&DD=2022-12-14&ERM=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=HRG90008&DPR=EXIM%20TOURS%20ATCOM&ILM=0&IFM=0"
detail_URL = "https://www.fischer.cz/spanelsko/mallorca/cala-san-vicente/globales-simar?DS=256&GIATA=89104&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&HID=3482&MT=5&NN=7&DF=2023-10-07|2023-10-14&RD=2023-10-14&DD=2023-10-07&ERM=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7&TT=1&TTM=1&PID=PMI14203&DPR=FISCHER%20ATCOM&ILM=0&IFM=0"

adultcount1="&AC1=1"
kidscount1 = "&KC1=1"
kidsAge1 = "&KA1=5"

jedenPokoj1 = "&AC1=1&KC1=3&KA1=8|10|15&IC1=0"
jedenPokoj2 = "&AC1=2&KC1=2&KA1=8|15&IC1=1"
jedenPokoj3 = "&AC1=2&KC1=1&KA1=13&IC1=1"
jedenPokoj4 = "&AC1=3&KC1=0&&IC1=1"

jedenPokojListParameters = [jedenPokoj1, jedenPokoj2, jedenPokoj3, jedenPokoj4]

dvaPokoje1 = "&AC1=2&KC1=1&KA1=10&IC1=1&AC2=2&KC2=2&KA2=13|6&IC2=0"
dvaPokoje2 = "&AC1=3&KC1=1&KA1=10&IC1=1&AC2=2&KC2=2&KA2=13|6&IC2=0"
dvaPokoje3 = "&AC1=3&KC1=1&KA1=10&IC1=1&AC2=1&KC2=2&KA2=13|6&IC2=1"
dvaPokoje4 = "&AC1=1&KC1=3&KA1=8|10|15&IC1=0&AC2=3&KC2=1&KA2=6&IC2=1"

dvaPokojeListParameters = [dvaPokoje1, dvaPokoje2, dvaPokoje3, dvaPokoje4]

allPokojeListParameters = jedenPokojListParameters + dvaPokojeListParameters

# print(detail_URL+jedenPokoj4)