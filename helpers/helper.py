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