from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from EW_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from EW_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from EW_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from FW_Automation_Local_Deploy_PyCharm.HP_C import hp_zlutak_to_SRL
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check, generalized_list_of_url_checker

URL_deploying_web = URL
URL_prod_public = "https://www.eximtours.cz/"
banneryXpath_EW = "//*[@class='f_teaser-item']/a"

HPvyhledatZajezdyButtonXpath = "//*[@class='f_filterMainSearch']//*[contains(text(), 'Vyhledat dovolenou')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam se chystáte?')]"
#HPzlutakReckoDestinaceXpath = "//*[@class='f_input-content'] //*[contains(text(), 'Řecko')]"
HPzlutakReckoDestinaceXpath= "/html/body/header/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[5]/div[1]/span/label/span/span"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
#HPzlutakPokracovatButtonXpathStep2 = "//*[@class='f_filterHolder f_set--active'] //*[@class=('f_button-text f_icon f_icon--chevronRight f_icon_set--right')]"
HPzlutakPokracovatButtonXpathStep2 ="/html/body/header/div/div[2]/div/div/div/div[3]/div[2]/div[3]/div[2]/a/span"
HPzlutakPokracovatVyberTerminuXpath = "/html/body/header/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div[2]/a/span"
#HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Letní prázdniny 2023')]" ##30x to definuju ne omg
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
# HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']"
#HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']/a"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"


#HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Letní prázdniny 2023')]"
HPzlutakPokracovatButtonXpathStep3 ="/html/body/header/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div[2]/a/span"

poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávací zájezdy')]"
lyzeVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Lyžování')]"
HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Září / Říjen 2023')]"

class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    # def test_HP_zlutak_to_groupsearch(self):
    #     self.driver.maximize_window()
    #     self.driver.get(URL)
    #     wait = WebDriverWait(self.driver, 300)
    #
    #     acceptConsent(self.driver)
    #     time.sleep(1.5)
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
    #     time.sleep(3.5)     ##time sleep not the best not pog but it works =)
    #     groupSearch_D(self, self.driver)
    #
    #     self.test_passed = True
    #
    # def test_HP_zlutak_to_SRL(self):
    #     self.driver.maximize_window()
    #     self.driver.get(URL)
    #     wait = WebDriverWait(self.driver, 300)
    #     time.sleep(2.5)
    #     acceptConsent(self.driver)
    #     time.sleep(2)
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click()
    #     time.sleep(1.3)
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakReckoDestinaceXpath))).click()
    #
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click()
    #     time.sleep(1.5)
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()
    #
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakLetniPrazdninyXpath))).click()
    #     time.sleep(3.5) ##+1
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatVyberTerminuXpath))).click()
    #     time.sleep(1.4)
    #
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath))).click()
    #
    #     time.sleep(1)
    #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click()
    #     time.sleep(2.789)
    #     SRL_D(self, self.driver)
    #
    #     self.test_passed = True


    HPzlutakPokracovatButtonXpathStep3 = "/html/body/header/div/div[2]/div/div/div/div[3]/div[3]/div[3]/div[2]/a/span"



    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_poznavacky(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element_by_xpath(poznavackyVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_groupsearch_lyze(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.find_element_by_xpath(lyzeVeFiltruSwitchXpath).click()
        time.sleep(2.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, HPzlutakReckoDestinaceXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_poznavacky(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        #poznavackyVeFiltruSwitchXpath = "//*[@class='f_icon f_icon--pinMap segmentation-list-anchor']"
        # poznavackyVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Poznávací zájezdy')]"
        destinaceEgyptXpath = "/html/body/header/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/span/label/span/span"

        self.driver.find_element_by_xpath(poznavackyVeFiltruSwitchXpath).click()

        time.sleep(5)

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceEgyptXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakLetniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_lyze(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        #lyzeVeFiltruSwitchXpath = "//*[@class='f_icon f_icon--snowFlake segmentation-list-anchor']"
        # lyzeVeFiltruSwitchXpath = "//*[@class='segmentation-list-text' and contains(text(), 'Lyžování')]"
        self.driver.find_element_by_xpath(lyzeVeFiltruSwitchXpath).click()
        HPzlutakJarniPrazdninyXpath = "//*[contains(text(), 'Březen / Duben  2023')]"
        destinaceItalieXpath = "/html/body/header/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/span/label/span/span"
        time.sleep(3)

        hp_zlutak_to_SRL(self.driver, HPkamPojedeteButtonXpath, destinaceItalieXpath,
                         HPzlutakPokracovatButtonXpath, HPzlutakPokracovatButtonXpathStep2, HPzlutakJarniPrazdninyXpath
                         , HPzlutakPokracovatButtonXpathStep3, HPzlutakObsazenost2plus1Xpath,
                         HPzlutakPotvrditAvyhledatXpath)
        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
           2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            # print (nejlepsiNabidkyTextList)
            positionOfCurrentElement = positionOfCurrentElement + 1

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)))
        HPnejlepsiZajezdySwitchButtonElement = self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)
        self.driver.execute_script("arguments[0].click();", HPnejlepsiZajezdySwitchButtonElement)
        time.sleep(6)
        time.sleep(6)
        self.driver.implicitly_wait(10)
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement2 = 0
        nejlepsiNabidkyTextList2 = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement2].text
            nejlepsiNabidkyTextList2.append(nejlepsiNabidkyTextDefault)
            # print(nejlepsiNabidkyTextList)
            positionOfCurrentElement2 = positionOfCurrentElement2 + 1

        print(nejlepsiNabidkyTextList)
        print(nejlepsiNabidkyTextList2)
        assert nejlepsiNabidkyTextList != nejlepsiNabidkyTextList2

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        #        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnextArrowXpath))).click()

        self.driver.implicitly_wait(100)

        HPnextArrowElement = self.driver.find_element_by_xpath(HPnextArrowXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPnextArrowElement)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        HPnextkartaHoteluSlider = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        # HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)

        self.test_passed = True



    def test_HP_top_nabidka_status(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        time.sleep(2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1)
        #HPtopNabidkaXpath = "//*[@class='page-widget js-ajaxPlaceholder--widget fshr-widget f_tileGrid-item']//*[@class='f_button-text f_icon f_icon_set--right f_icon--chevronRight']"
        HPtopNabidkaXpath= "//*[@class='js-ajaxPlaceholder--widgetContent']/a"
        HPtopNabidkaElements = self.driver.find_elements_by_xpath(HPtopNabidkaXpath)
        HPtopNabidkaElement = HPtopNabidkaElements[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", HPtopNabidkaElement)
        time.sleep(4)
        linksToCheck_List = []
        pozice = 0
        for _ in HPtopNabidkaElements:
            odkazLink = HPtopNabidkaElements[pozice].get_attribute("href")
            #odkazLink = HPtopNabidkaElements[pozice].get_attribute("a")
            linksToCheck_List.append(odkazLink)
            print(odkazLink)
            pozice = pozice + 1

        generalized_list_of_url_checker(linksToCheck_List)

