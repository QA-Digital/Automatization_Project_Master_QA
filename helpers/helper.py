# sorting_utilities.py

class SortingUtilities:
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