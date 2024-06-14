import os
import re

def modify_driver_get_statements(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        # Modify self.driver.get statements
        match = re.search(r'self\.driver\.get\((URL_\w+)\)', line)
        if match:
            url_variable = match.group(1)
            url_variable_lp = f"{url_variable}_lp"
            replacement_line = f'        {url_variable_lp} = f"{{self.URL}}{{{url_variable}}}"\n'
            line = line.replace(url_variable, url_variable_lp)
            new_lines.append(replacement_line)

        new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modify_driver_get_statements(file_path)
                print(f'Updated {file_path}')

if __name__ == '__main__':
    project_directory = r'C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\FW_Automation_Local_Deploy_PyCharm'  # Update with your project path
    process_directory(project_directory)
