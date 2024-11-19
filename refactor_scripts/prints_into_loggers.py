from selenium.webdriver.common.by import By
import os
import re

FW_FOLDER = r"C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\DERRO"

def refactor_print_statements(file_path):
    """
    This function refactors the print statements in a test file to self.logger.info statements.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all the print statements and replace them with self.logger.info
    modified_content = re.sub(r'print\((.*)\)', r'self.logger.info(\1)', content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def process_fw_folder(folder_path):
    """
    This function walks through all the files in the FW folder and refactors the print statements.
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                refactor_print_statements(file_path)

if __name__ == "__main__":
    process_fw_folder(FW_FOLDER)
