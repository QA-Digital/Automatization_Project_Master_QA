import os
import re


def update_imports_in_file(file_path, old_project_name, new_project_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Create the patterns dynamically based on the provided project names
    from_pattern = fr'from\s+{old_project_name}'
    import_pattern = fr'import\s+{old_project_name}'

    updated_content = re.sub(from_pattern, f'from {new_project_name}', content)
    updated_content = re.sub(import_pattern, f'import {new_project_name}', updated_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)


def update_imports_in_directory(directory_path, old_project_name, new_project_name):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                update_imports_in_file(file_path, old_project_name, new_project_name)


if __name__ == "__main__":
    # Set the path to your project directory
    #project_directory_path = r'/DERRO'  # Update with your project path
    project_directory_path =  r'C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\EXPL_Automation_Local_Deploy_PyCharm'


    # Old and new project names
    old_project_name = 'EXPL_Automation_Local_Deploy_PyCharm'
    new_project_name = 'EXPL'

    update_imports_in_directory(project_directory_path, old_project_name, new_project_name)

    print("All import statements have been updated.")
