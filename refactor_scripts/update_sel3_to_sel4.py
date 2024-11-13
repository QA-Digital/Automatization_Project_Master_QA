import os
import re

FW_FOLDER = r"C:\Users\KADOUN\Desktop\Automatization_Project_Master_QA\EW"

def refactor_selenium_commands(file_path):
    """
    Refactors old Selenium 3.x commands to Selenium 4.x compatible commands, handling multi-line cases.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Update old find_element_by_* methods to the new By format (multi-line compatible)
    content = re.sub(
        r'driver\.find_element_by_xpath\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.XPATH, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_xpath\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.XPATH, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_element_by_id\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.ID, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_id\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.ID, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_element_by_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_element_by_class_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.CLASS_NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_class_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.CLASS_NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_element_by_tag_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.TAG_NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_tag_name\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.TAG_NAME, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_element_by_css_selector\s*\(\s*(.*?)\s*\)',
        r'driver.find_element(By.CSS_SELECTOR, \1)', content, flags=re.DOTALL
    )
    content = re.sub(
        r'driver\.find_elements_by_css_selector\s*\(\s*(.*?)\s*\)',
        r'driver.find_elements(By.CSS_SELECTOR, \1)', content, flags=re.DOTALL
    )

    # Ensure `By` is imported if not already present
    if 'from selenium.webdriver.common.by import By' not in content:
        content = 'from selenium.webdriver.common.by import By\n' + content

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_folder(folder_path):
    """
    Walk through all Python files in the specified folder and refactor old Selenium commands.
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                refactor_selenium_commands(file_path)

if __name__ == "__main__":
    process_folder(FW_FOLDER)
