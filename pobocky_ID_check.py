from selenium.webdriver.common.by import By
import time
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from FW.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
URL = "https://www.fischer.cz/kontakty/seznam-pobocek"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)



start = "//*[@data-branch-id='248']"
end = "//*[@data-branch-id='493']"
stringToVerify = """Benešov
>
Zavřeno
"""
## https://webadmin-shared.stg.dtweb.cz/OfficeBranchAdmin?fragmentGuid=00000000-0000-0000-0000-000000000000
##nektere cisla v radě chybi je nutny importovat list z WA viz link nahore
## https://arraythis.com/
listIDS = [248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 466, 467, 468, 469, 470, 471, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494]
def id_creator_pobocky_xpath(idNumber):
    startXpath = "//*[@data-branch-id='"
    endXpath = "']"

    finalIdXpathLocator = startXpath + str(idNumber) + endXpath
    return finalIdXpathLocator

print(driver.find_element(By.XPATH, id_creator_pobocky_xpath(248)).text)
#print(stringToVerify)
#print(driver.find_element(By.XPATH, id_creator_pobocky_xpath(248)).text==stringToVerify)
listJmenaPobocek = []
listMissingIDsPobocek = []
CountPobocekStarter = 0
for _ in listIDS:
#
    try:
        listJmenaPobocek.append(driver.find_element(By.XPATH, id_creator_pobocky_xpath(listIDS[CountPobocekStarter])).text)
    except NoSuchElementException:
        listMissingIDsPobocek.append(id_creator_pobocky_xpath(listIDS[CountPobocekStarter]))

    CountPobocekStarter = CountPobocekStarter+1


print(listJmenaPobocek)
print(len(listJmenaPobocek))

print("Missing pobocky:::")
print(listMissingIDsPobocek)