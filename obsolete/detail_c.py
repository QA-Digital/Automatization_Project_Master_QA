# def test_detail_open_terminy_sumUP_equal_to_full_price(self):
#     self.driver.maximize_window()
#     URL_detail = "https://www.fischer.cz/spanelsko/fuerteventura/morro-jable/blue-sea-jandia-luz?AC1=2&D=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&DD=2023-02-19&DP=4312&DPR=FISCHER+ATCOM&DS=256&GIATA=32289&HID=1629&IC1=0&KC1=0&MNN=7&MT=6&NN=7&PID=FUE90003&RD=2023-02-26&TO=4312|4305|2682|4308&acm1=2&df=2023-02-01|2023-03-31&nnm=7|8|9|10|11|12|13&tom=4312|4305|2682|4308&tt=1&ttm=1#/terminy-a-ceny"
#     URL_detail_lp = f"{self.URL}{URL_detail}"
#     self.driver.get(URL_detail_lp)
#
#
#     cestujiciXpath = "//*[@class='f_table']//*[@class='f_table-body']//*[@class='f_table-cell']"
#     time.sleep(1)
#     acceptConsent(self.driver)
#     time.sleep(15)
#     terminyXpath = "//*[@class='f_termList-header']"
#     terminyScrollInto = self.driver.find_element_by_xpath(terminyXpath)
#     self.driver.execute_script("arguments[0].scrollIntoView();", terminyScrollInto)
#
#     cestujiciElements = self.driver.find_elements_by_xpath(cestujiciXpath)
#     cestujiciElement = self.driver.find_element_by_xpath(cestujiciXpath)
#
#     cestujiciElementText = self.driver.find_element_by_xpath(cestujiciXpath).text
#     self.logger.info(cestujiciElement.text)
#     self.logger.info("priting 1St")
#     self.logger.info(cestujiciElement.text)
#     self.logger.info(cestujiciElementText)
#     self.logger.info(cestujiciElements[0].text)
#     #self.logger.info(cestujiciElements[1].text)
#     time.sleep(15)
#     ##cestujici elements = pocet cestujiich,
#     y=1
#     for _ in cestujiciElements:
#         cestujiciSinglePrice = cestujiciElements[y].text()
#         self.logger.info(cestujiciSinglePrice)
#         cestujiciSinglePriceList = []
#         cestujiciSinglePriceList.append(cestujiciSinglePrice)
#         self.logger.info(cestujiciSinglePriceList)
#         y = y + 2
#
#     self.test_passed = True