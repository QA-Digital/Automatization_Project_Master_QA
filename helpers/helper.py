# sorting_utilities.py
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Helpers:
    @staticmethod
    def generalized_price_sorter_expensive_cheap_assert(inputList, typeOfSort, logger):
        logger.info(f"Starting price sorting test for type: {typeOfSort}")
        inputListSorted = inputList.copy()

        if typeOfSort == "cheap":
            inputListSorted.sort()
            if inputList == inputListSorted:
                logger.info("Cheap sorter is OK")
            else:
                logger.info("Cheap sorter is NOT OK")

        elif typeOfSort == "expensive":
            inputListSorted.sort(reverse=True)
            if inputList == inputListSorted:
                logger.info("Expensive sorter is OK")
            else:
                logger.info("Expensive sorter is NOT OK")

        logger.info(f"Original List from Web: {inputList}")
        logger.info(f"Correctly Sorted List: {inputListSorted}")
        assert inputList == inputListSorted

    @staticmethod
    def generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(driver, terminyAcenyTabXpath, boxFiltrXpath,
                                                                        valueToFilterXpath, filterType, logger=None):
        """
        Apply filters on the detail page based on the type ("meal" or "airport").

        Args:
            driver: Selenium WebDriver instance.
            terminyAcenyTabXpath: Xpath of the terminy a ceny tab element.
            boxFiltrXpath: Xpath of the filter box element.
            valueToFilterXpath: Xpath of the value to filter.
            filterType: Either "meal" or "airport", determines the logic block.
            logger: Optional logger instance for logging actions.
        """

        # Log the start of the filtering process
        if logger:
            logger.info(f"Starting filtering process with filter type: {filterType}")
        else:
            print(f"Starting filtering process with filter type: {filterType}")

        # Open the terminy a ceny tab
        terminyAcenyTabElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].click();", terminyAcenyTabElement)
        time.sleep(2.5)

        # Open the filter box
        boxElement = driver.find_element_by_xpath(boxFiltrXpath)
        driver.execute_script("arguments[0].click();", boxElement)
        time.sleep(3.5)

        if filterType == "airport":
            if logger:
                logger.info("Filter type is 'airport'. Executing airport filter logic.")
            else:
                print("Filter type is 'airport'. Executing airport filter logic.")

            # Scroll and click the airport value
            valueToFilterElement = driver.find_element_by_xpath(valueToFilterXpath)
            driver.execute_script("arguments[0].scrollIntoView();", valueToFilterElement)
            time.sleep(0.5)
            valueToFilterElement.click()
            time.sleep(0.5)

        elif filterType == "meal":
            if logger:
                logger.info("Filter type is 'meal'. Executing meal filter logic.")
            else:
                print("Filter type is 'meal'. Executing meal filter logic.")

            # Scroll and click the meal value
            time.sleep(5)
            driver.execute_script("arguments[0].scrollIntoView();", boxElement)
            valueToFilterElement = driver.find_element_by_xpath(valueToFilterXpath)
            driver.execute_script("arguments[0].scrollIntoView();", valueToFilterElement)
            time.sleep(0.5)
            valueToFilterElement.click()
            time.sleep(0.5)

        # Close the filter box
        driver.execute_script("arguments[0].click();", boxElement)
        time.sleep(1)

        # Log the end of the filtering process
        if logger:
            logger.info(f"Completed filtering process for filter type: {filterType}")
        else:
            print(f"Completed filtering process for filter type: {filterType}")

    @staticmethod
    def generalized_detail_departure_check(driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath,
                                           departureToCompareTo, logger=None):
        """
        Checks the departure filter on the detail page and compares it to the expected departure value.

        Args:
            driver: Selenium WebDriver instance.
            pocetZobrazenychTerminuXpath: Xpath to locate the number of visible departure terms.
            odletyTerminyXpath: Xpath to locate departure terms to compare.
            departureToCompareTo: The expected departure location to compare against.
            logger: Optional logger instance for logging actions.
        """

        # Log start of the departure check
        if logger:
            logger.info("Starting departure check.")
        else:
            print("Starting departure check.")

        try:
            pocetZobrazenychTerminu = driver.find_elements_by_xpath(pocetZobrazenychTerminuXpath)
            if logger:
                logger.info(f"Found {len(pocetZobrazenychTerminu)} visible departure terms.")
        except NoSuchElementException:
            url = driver.current_url
            msg = f"Could not find visible departure terms: NoSuchElementException on {url}"
            if logger:
                logger.error(msg)
            else:
                print(msg)
            return

        try:
            odletyTerminy = driver.find_elements_by_xpath(odletyTerminyXpath)
            if logger:
                logger.info(f"Found {len(odletyTerminy)} departure terms.")
        except NoSuchElementException:
            url = driver.current_url
            msg = f"Could not find departure terms: NoSuchElementException on {url}"
            if logger:
                logger.error(msg)
            else:
                print(msg)
            return

        # Proceed to compare the departure terms
        time.sleep(3)
        poziceTerminu = 1  # Assuming departure terms start from index 1
        for _ in range(len(pocetZobrazenychTerminu) - 2):  # Loop through all visible terms, except the last two
            current_departure = odletyTerminy[poziceTerminu].text.lower()

            if current_departure == departureToCompareTo:
                if logger:
                    logger.info(f"Departure term at position {poziceTerminu} matches {departureToCompareTo}.")
                else:
                    print(f"Departure term at position {poziceTerminu} matches {departureToCompareTo}.")
                poziceTerminu += 1
                assert current_departure == departureToCompareTo
            else:
                url = driver.current_url
                msg = f"Departure term mismatch at {poziceTerminu}: expected {departureToCompareTo}, got {current_departure}. URL: {url}"
                if logger:
                    logger.error(msg)
                else:
                    print(msg)
                assert current_departure == departureToCompareTo

        # Log completion of the departure check
        if logger:
            logger.info("Completed departure check.")
        else:
            print("Completed departure check.")

    @staticmethod
    def LM_FM_vypis_rozbalit_zajezd_check(driver, logger=None):
        """
        Expands the 'First Minute/Last Minute' (FM/LM) tour section and checks if the expanded tour is visible.

        Args:
            driver: Selenium WebDriver instance.
            logger: Optional logger instance for logging actions.
        """

        wait = WebDriverWait(driver, 150)  # Adjusted wait time to a more reasonable limit (seconds).
        driver.implicitly_wait(10)

        # Log start of FM/LM tour expansion check
        if logger:
            logger.info("Starting FM/LM tour expansion check.")
        else:
            print("Starting FM/LM tour expansion check.")

        try:
            # Find and click the "expand" button for FM/LM tours
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            wait.until(EC.visibility_of(rozbal))
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(2)

            if logger:
                logger.info("Successfully clicked to expand FM/LM tour section.")
            else:
                print("Successfully clicked to expand FM/LM tour section.")

        except NoSuchElementException:
            url = driver.current_url
            msg = f"Could not expand FM/LM tour section. URL: {url}"
            if logger:
                logger.error(msg)
            else:
                print(msg)
            assert False, msg

        try:
            # Verify if the expanded tour is displayed
            rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
            rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
            wait.until(EC.visibility_of(rozbalenyZajezd))

            if rozbalenyZajezd.is_displayed():
                for webElement in rozbalenyZajezdAll:
                    is_displayed = webElement.is_displayed()
                    assert is_displayed is True

                    if logger:
                        logger.info(f"Tour element {webElement} visibility: {is_displayed}")
                    else:
                        print(f"Tour element {webElement} visibility: {is_displayed}")

                    if not is_displayed:
                        url = driver.current_url
                        msg = f"No tour found when expanding FM/LM tour section. URL: {url}"
                        if logger:
                            logger.error(msg)
                        else:
                            print(msg)
                        assert False, msg

        except NoSuchElementException:
            url = driver.current_url
            msg = f"No tour found after expanding FM/LM tour section. URL: {url}"
            if logger:
                logger.error(msg)
            else:
                print(msg)
            assert False, msg

        # Final assertion to ensure the expanded tour is displayed
        assert rozbalenyZajezd.is_displayed() is True
        if logger:
            logger.info("FM/LM tour expansion check completed successfully.")
        else:
            print("FM/LM tour expansion check completed successfully.")

    @staticmethod
    def group_search_check(driver, logger=None):
        """
        Checks the visibility of elements in the group search section and search results.

        Args:
            driver: Selenium WebDriver instance.
            logger: Optional logger instance for logging actions.
        """

        # Initialize an explicit wait
        wait = WebDriverWait(driver, 150)
        logger.info("Starting group search check.") if logger else print("Starting group search check.")

        # XPath for group search tiles
        groupSearchDlazdiceXpath = "//*[@class='box-border relative pt-[100%]']"
        time.sleep(2)

        # Find the group search teaser items
        teaserItems = driver.find_elements_by_xpath(groupSearchDlazdiceXpath)
        wait.until(EC.visibility_of(teaserItems[0]))

        try:
            logger.info(f"Found {len(teaserItems)} teaser items in the group search section.") if logger else print(
                f"Found {len(teaserItems)} teaser items.")
            for webElement in teaserItems:
                is_visible = webElement.is_displayed()
                if is_visible:
                    logger.info(f"Teaser item is visible: {webElement}.") if logger else print(
                        f"Teaser item is visible: {webElement}.")
                else:
                    logger.warning(f"Teaser item is NOT visible: {webElement}.") if logger else print(
                        f"Teaser item is NOT visible: {webElement}.")
        except NoSuchElementException:
            msg = "No teaser items found in the group search section."
            logger.error(msg) if logger else print(msg)
            assert False, msg

        assert teaserItems[0].is_displayed() is True
        logger.info("First teaser item is displayed.") if logger else print("First teaser item is displayed.")

        # Reset implicit wait
        driver.implicitly_wait(100)

        # XPath for search result items
        srlItemsXpath = "//*[@class='f_searchResult' and not(@style='display: none;')]"
        srlItems = driver.find_elements_by_xpath(srlItemsXpath)

        try:
            logger.info(f"Found {len(srlItems)} Groupsearch items.") if logger else print(
                f"Found {len(srlItems)} Groupsearch items.")
            for webElement in srlItems:
                is_visible = webElement.is_displayed()
                if is_visible:
                    logger.info(f"Groupsearch is visible: {webElement}.") if logger else print(
                        f"Groupsearch is visible: {webElement}.")
                else:
                    logger.warning(f"Groupsearch NOT visible: {webElement}.") if logger else print(
                        f"Groupsearch  is NOT visible: {webElement}.")
        except NoSuchElementException:
            msg = "No Groupsearch items found."
            logger.error(msg) if logger else print(msg)
            assert False, msg

        # Final assertion for visibility
        assert srlItems[0].is_displayed() is True
        logger.info("Groupsearch is displayed.") if logger else print(
            "Groupsearch is displayed.")

        logger.info("Group search check completed.") if logger else print("Group search check completed.")

    @staticmethod
    def search_results_list_check(driver, logger=None):
        """
        Checks the visibility of hotel cards and their prices in the search result listing (SRL).

        Args:
            driver: Selenium WebDriver instance.
            logger: Optional logger instance for logging actions.
        """
        wait = WebDriverWait(driver, 150)
        logger.info("Starting search results listing check.") if logger else print(
            "Starting search results listing check.")
        time.sleep(6)

        # Hotel card elements
        SRLhotelyKartyXpath = "//*[@class='f_searchResult-content-item relative']"  # Placeholder for the actual XPath
        hotelySingle = driver.find_element_by_xpath(SRLhotelyKartyXpath)

        try:
            hotelyAll = driver.find_elements_by_xpath(SRLhotelyKartyXpath)
            wait.until(EC.visibility_of(hotelySingle))
            logger.info(f"Found {len(hotelyAll)} hotel cards in the search results.") if logger else print(
                f"Found {len(hotelyAll)} hotel cards.")

            if hotelySingle.is_displayed():
                for webElement in hotelyAll:
                    is_visible = webElement.is_displayed()
                    logger.info(f"Hotel card visible: {is_visible}") if logger else print(
                        f"Hotel card visible: {is_visible}")
                    assert is_visible is True
            else:
                url = driver.current_url
                logger.error(f"Problem with hotel cards in search results - HotelCard at {url}.") if logger else print(
                    f"Problem with hotel cards in search results - HotelCard at {url}.")
                assert False, "Hotel cards are not displayed in the search results."

        except NoSuchElementException:
            url = driver.current_url
            logger.error(
                f"Hotel cards not found in search results - NoSuchElementException at {url}.") if logger else print(
                f"Hotel cards not found in search results - NoSuchElementException at {url}.")
            assert False, "No hotel cards found."

        time.sleep(3)
        assert hotelySingle.is_displayed() is True
        logger.info("First hotel card is displayed.") if logger else print("First hotel card is displayed.")

        # Checking hotel prices
        SRLcenyHoteluXpath = "your-hotel-price-xpath"  # Placeholder for the actual XPath

        try:
            driver.implicitly_wait(100)
            cenaAll = driver.find_elements_by_xpath(SRLcenyHoteluXpath)
            cenaSingle = driver.find_element_by_xpath(SRLcenyHoteluXpath)
            wait.until(EC.visibility_of(cenaSingle))

            if cenaSingle.is_displayed():
                for webElement in cenaAll:
                    is_visible = webElement.is_displayed()
                    logger.info(f"Hotel price visible: {is_visible}") if logger else print(
                        f"Hotel price visible: {is_visible}")
                    assert is_visible is True
            else:
                url = driver.current_url
                logger.error(f"Problem with hotel prices in search results at {url}.") if logger else print(
                    f"Problem with hotel prices in search results at {url}.")
                assert False, "Hotel prices are not displayed."

        except NoSuchElementException:
            url = driver.current_url
            logger.error(
                f"Hotel prices not found in search results - NoSuchElementException at {url}.") if logger else print(
                f"Hotel prices not found in search results - NoSuchElementException at {url}.")
            assert False, "No hotel prices found."

        assert cenaAll[0].is_displayed() is True
        logger.info("First hotel price is displayed.") if logger else print("First hotel price is displayed.")

        # Checking for loading images (bad state if found)
        try:
            driver.implicitly_wait(5)
            loadingImgSingle = driver.find_element_by_xpath(
                "//*[@class='splide__spinner']")  # Spinner for loading images

            if loadingImgSingle.is_displayed():
                url = driver.current_url
                logger.error(f"There is a loading image in the SRL at {url}.") if logger else print(
                    f"There is a loading image in the SRL at {url}.")
                assert False, "Loading image is present in the search results."

        except NoSuchElementException:
            logger.info("No loading images found in the SRL.") if logger else print(
                "No loading images found in the SRL.")

        logger.info("Search results listing check completed.") if logger else print(
            "Search results listing check completed.")

    @staticmethod
    def poznavacky_display_check(driver, logger=None):
            """
            Checks the visibility of tiles and images in the 'Poznavacky' section.

            Args:
                driver: Selenium WebDriver instance.
                logger: Optional logger instance for logging actions.
            """
            logger.info("Starting 'Poznavacky' tiles and images check.") if logger else print(
                "Starting 'Poznavacky' tiles and images check.")

            # Wait for the page to load and images to be ready
            time.sleep(5)

            # Image elements
            imgs = driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
            logger.info(f"Found {len(imgs)} images to check.") if logger else print(
                f"Found {len(imgs)} images to check.")

            # Assert the first image is displayed
            assert imgs[0].is_displayed() is True, "The first image is not displayed."
            logger.info("The first image is displayed correctly.") if logger else print(
                "The first image is displayed correctly.")

            # Loop through images and check visibility
            for index, img in enumerate(imgs):
                imgsDisplayed = img.is_displayed()
                logger.info(f"Image {index + 1}/{len(imgs)} visibility: {imgsDisplayed}") if logger else print(
                    f"Image {index + 1}/{len(imgs)} visibility: {imgsDisplayed}")
                assert imgsDisplayed is True, f"Image {index + 1} is not displayed."

            # Grid items
            gridItems = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
            driver.execute_script("arguments[0].scrollIntoView();", gridItems[0])
            assert gridItems[0].is_displayed() is True, "The first grid item is not displayed."
            logger.info(f"First grid item is displayed correctly.") if logger else print(
                f"First grid item is displayed correctly.")

            # Loop through grid items and check visibility
            for index, gridItem in enumerate(gridItems):
                gridItemDisplayed = gridItem.is_displayed()
                logger.info(
                    f"Grid item {index + 1}/{len(gridItems)} visibility: {gridItemDisplayed}") if logger else print(
                    f"Grid item {index + 1}/{len(gridItems)} visibility: {gridItemDisplayed}")
                assert gridItemDisplayed is True, f"Grid item {index + 1} is not displayed."

            # Big grid elements
            gridBig = driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
            assert gridBig[0].is_displayed() is True, "The main grid is not displayed."
            logger.info(f"Main grid is displayed correctly.") if logger else print(f"Main grid is displayed correctly.")

            # Loop through big grids and check visibility
            for index, bigGrid in enumerate(gridBig):
                gridBigDisplayed = bigGrid.is_displayed()
                logger.info(f"Big grid {index + 1}/{len(gridBig)} visibility: {gridBigDisplayed}") if logger else print(
                    f"Big grid {index + 1}/{len(gridBig)} visibility: {gridBigDisplayed}")
                assert gridBigDisplayed is True, f"Big grid {index + 1} is not displayed."

            logger.info("'Poznavacky' tiles and images check completed.") if logger else print(
                "'Poznavacky' tiles and images check completed.")

    @staticmethod
    def generalized_SRL_price_sorter(driver, sorter_Xpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort, logger,
                                     web_language=None):
        wait = WebDriverWait(driver, 25)
        cenaZajezduAllList = []
        cenaZajezduAllListSorted = []

        time.sleep(3)
        sorter_Element = driver.find_element_by_xpath(sorter_Xpath)
        wait.until(EC.visibility_of(sorter_Element))
        sorter_Element.click()

        time.sleep(6)
        hotelyKarty = driver.find_element_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyKarty))

        time.sleep(4)
        cenaZajezduAll = driver.find_elements_by_xpath(cenaZajezduXpath)
        wait.until(EC.visibility_of(cenaZajezduAll[0]))

        for webElement in cenaZajezduAll:
            cenaZajezduAllString = webElement.text

            if web_language in [None, "SK"]:
                cenaZajezduAllString = cenaZajezduAllString[:-2]
            elif web_language == "PL":
                cenaZajezduAllString = cenaZajezduAllString.replace(",", ".").replace(" ", "")
                numeric_part = ''.join(filter(str.isdigit, cenaZajezduAllString))
                cenaZajezduAllString = int(numeric_part)

            cenaZajezduAllString = int(''.join(cenaZajezduAllString.split()))
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        Helpers.generalized_price_sorter_expensive_cheap_assert(cenaZajezduAllList, typeOfSort, logger)

        logger.info(f"LIST FROM WEB: {cenaZajezduAllList}")
        logger.info(f"CORRECTLY SORTED LIST: {cenaZajezduAllListSorted}")

    @staticmethod
    def generalized_map_test_click_on_pin_and_hotel_bubble(driver, logger):
        logger.info("Starting map test: clicking on pin and checking hotel bubble.")

        try:
            # Locate and click the hotel pin on the map
            actualHotelPin = driver.find_element_by_xpath(
                "//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
            driver.execute_script("arguments[0].click();", actualHotelPin)
            logger.info("Hotel pin clicked successfully.")

            # Check if there's a missing image in the hotel bubble
            try:
                imgMissing = driver.find_element_by_xpath("//*[@class='f_image f_image--missing']")
                if imgMissing.is_displayed():
                    hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
                    msg = "V mape v bublibně hotelu se nezobrazuje fotka hotelu " + hotelBubble.text
                    logger.error(msg)
                else:
                    logger.info("Image is correctly displayed in hotel bubble.")
            except NoSuchElementException:
                logger.info("No missing image found, everything is OK.")

            time.sleep(2)
            hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
            hotelBubble.click()
            logger.info("Hotel bubble clicked successfully.")

        except Exception as e:
            logger.error(f"An error occurred during the map test: {e}")

    @staticmethod
    def generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath, logger):
        logger.info("Starting map test: Clicking through map circles.")

        def click_on_map_circle(driver, circlexpath):
            try:
                driver.find_element_by_xpath(circlexpath).click()
                logger.info(f"Clicked on circle with XPath: {circlexpath}")
            except Exception as e:
                logger.error(f"Failed to find or click circle with XPath: {circlexpath}. Error: {e}")
            time.sleep(1.2)

        try:
            zobrazitNaMape = driver.find_element_by_xpath(zobrazitNaMapeXpath)
            zobrazitNaMape.click()
            logger.info(f"Clicked on 'Zobrazit na Mapě' element with XPath: {zobrazitNaMapeXpath}")
        except Exception as e:
            logger.error(f"Failed to click on 'Zobrazit na Mapě' element. Error: {e}")

        largeCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"
        mediumCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"
        smallCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']"

        logger.info("Waiting for map circles to load (10 seconds).")
        time.sleep(10)  # Loading time

        logger.info("Clicking on large circles.")
        click_on_map_circle(driver, largeCircleXpath)
        time.sleep(2)
        click_on_map_circle(driver, largeCircleXpath)
        time.sleep(2)
        click_on_map_circle(driver, largeCircleXpath)

        logger.info("Clicking on medium circles.")
        click_on_map_circle(driver, mediumCircleXpath)
        time.sleep(2)
        click_on_map_circle(driver, mediumCircleXpath)

        logger.info("Clicking on small circles.")
        click_on_map_circle(driver, smallCircleXpath)
        time.sleep(2)
        click_on_map_circle(driver, smallCircleXpath)

        logger.info("Finished map test: Clicking through circles.")

    @staticmethod
    def generalized_list_string_sorter(driver, web_elements_Xpath, variable_to_assert_to, logger, plusPozice=None,
                                       list_web_element_starter=None):
        logger.info("Starting list string sorter test.")
        time.sleep(2)

        if plusPozice is None:
            plusPozice = 1
        elif plusPozice == 2:
            plusPozice = 2
        else:
            plusPozice = 1

        if list_web_element_starter is None:
            list_web_elements_Position = 0
        elif list_web_element_starter == 1:
            list_web_elements_Position = 1
        else:
            list_web_elements_Position = 0

        logger.info(f"Initial list_web_elements_Position: {list_web_elements_Position}")
        web_elements = driver.find_elements_by_xpath(web_elements_Xpath)
        logger.info(f"Found {len(web_elements)} web elements with XPath: {web_elements_Xpath}")

        list_web_elements = []

        for _ in web_elements:
            list_web_elements_String = web_elements[list_web_elements_Position].text.lower()
            list_web_elements.append(list_web_elements_String)
            logger.debug(f"Appended text: {list_web_elements_String} at position {list_web_elements_Position}")

            list_web_elements_Position += plusPozice

        list_web_elements_Position = 0
        logger.info(f"List of web elements after processing: {list_web_elements}")

        for index, element in enumerate(list_web_elements):
            logger.info(f"Checking if '{variable_to_assert_to}' is in element {index}: {element}")
            assert variable_to_assert_to in element
            if variable_to_assert_to in element:
                logger.info(
                    f"Assertion passed for element at position {index}: '{element}' contains '{variable_to_assert_to}'")
            else:
                logger.error(
                    f"Assertion failed for element at position {index}: '{element}' does NOT contain '{variable_to_assert_to}'")

            list_web_elements_Position += plusPozice

        logger.info("Completed list string sorter test.")