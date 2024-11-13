import os
import re

FW_FOLDER = r"C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA"

def refactor_selenium_commands(file_path):
    """
    Refactors old Selenium 3.x commands to Selenium 4.x compatible commands.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Refactoring old find_element_by_* methods to find_element(By.*, value)
    content = re.sub(r'\bfind_element_by_xpath\((.*?)\)', r'find_element(By.XPATH, \1)', content)
    content = re.sub(r'\bfind_elements_by_xpath\((.*?)\)', r'find_elements(By.XPATH, \1)', content)
    content = re.sub(r'\bfind_element_by_id\((.*?)\)', r'find_element(By.ID, \1)', content)
    content = re.sub(r'\bfind_element_by_name\((.*?)\)', r'find_element(By.NAME, \1)', content)
    content = re.sub(r'\bfind_element_by_class_name\((.*?)\)', r'find_element(By.CLASS_NAME, \1)', content)
    content = re.sub(r'\bfind_element_by_tag_name\((.*?)\)', r'find_element(By.TAG_NAME, \1)', content)
    content = re.sub(r'\bfind_element_by_css_selector\((.*?)\)', r'find_element(By.CSS_SELECTOR, \1)', content)

    # Add necessary imports if not present
    if 'from selenium.webdriver.common.by import By' not in content:
        content = 'from selenium.webdriver.common.by import By\n' + content

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_fw_folder(folder_path):
    """
    Walks through all Python files in the FW folder and refactors old Selenium commands.
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                refactor_selenium_commands(file_path)

if __name__ == "__main__":
    process_fw_folder(FW_FOLDER)
