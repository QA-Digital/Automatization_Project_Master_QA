import os
import re
import codecs

# Define the root folder where your "FW" folder is located
project_root = "C:/Users/KDK/Desktop/DTCZ/kod/Automatization_Project_Master_QA/"
# Path to the "FW" folder
fw_folder = os.path.join(project_root, 'FW')

# Pattern to match print statements, capturing the indentation
print_pattern = re.compile(r'^(\s*)print\((.*)\)\s*$', re.MULTILINE)

# Import statements to be added
import_statements = (
    'from FW.to_import import print_lock\n'
    'import time\n'
)

# Replace function with UTF-8 encoding handling and proper indentation
def replace_print_statements_and_add_import(file_path):
    try:
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the import statements are already present
        if 'from FW.to_import import print_lock' not in content:
            # Add import statements at the beginning of the file
            if not content.startswith(import_statements):
                content = import_statements + content

        # Replace all print statements with the locked version including time.sleep and lock release
        new_content = print_pattern.sub(
            r'\1print_lock.acquire()\n'
            r'\1try:\n'
            r'\1    print(\2)\n'
            r'\1    time.sleep(0.1)\n'
            r'\1finally:\n'
            r'\1    print_lock.release()',
            content
        )

        with codecs.open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
    except UnicodeDecodeError:
        print(f"Skipping file due to encoding error: {file_path}")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

# Walk through the "FW" folder and find all .py files
for root, dirs, files in os.walk(fw_folder):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            replace_print_statements_and_add_import(file_path)

print("Refactoring completed successfully.")
