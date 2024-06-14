import os
import re


def modify_driver_get_statements(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    added_url_variables = set()

    for line in lines:
        # Check for existing URL_*_lp variables
        match_existing_lp = re.match(r'\s*(URL_\w+_lp) = f"\{self\.URL\}\{(\w+)\}"', line)
        if match_existing_lp:
            added_url_variables.add(match_existing_lp.group(2))

        # Modify self.driver.get and driver.get statements
        match_get = re.search(r'(self\.)?driver\.get\((URL_\w+)\)', line)
        if match_get:
            url_variable = match_get.group(2)
            if url_variable not in added_url_variables:
                url_variable_lp = f"{url_variable}_lp"
                replacement_line = f'        {url_variable_lp} = f"{{self.URL}}{{{url_variable}}}"\n'
                new_lines.append(replacement_line)
                added_url_variables.add(url_variable)
                line = line.replace(url_variable, url_variable_lp)

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
