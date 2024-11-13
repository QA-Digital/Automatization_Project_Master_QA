from selenium.webdriver.common.by import By
import os
import re

# Explicit path to the FW folder
FW_FOLDER = r'C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\FW'

# Regex pattern to match test method definitions (i.e., def test_method(self))
test_method_pattern = re.compile(r"(def\s+test_\w+\(self)")


def refactor_test_methods(file_path):
    """Refactor test methods in the given file by adding a URL parameter."""
    try:
        # Open the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Could not read {file_path} due to encoding issues.")
        return

    # Check if there's any test method to refactor
    if not test_method_pattern.search(content):
        return

    # Add 'URL' to test methods' signature
    refactored_content = test_method_pattern.sub(r"\1, URL", content)

    # Write the updated content back to the file with UTF-8 encoding
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(refactored_content)
        print(f"Refactored: {file_path}")
    except Exception as e:
        print(f"Failed to write {file_path}: {e}")


def process_fw_folder(folder_path):
    """Process all Python files in the FW folder and refactor test methods."""
    if not os.path.exists(folder_path):
        print(f"The folder path {folder_path} does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        print(f"Checking directory: {root}")
        for file in files:
            if file.endswith('.py'):  # Only process Python files
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                refactor_test_methods(file_path)


if __name__ == "__main__":
    process_fw_folder(FW_FOLDER)
