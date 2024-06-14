import os
import re

def add_init_method_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        added_init = False
        added_import = False
        init_added = False  # Flag to check if __init__ method is already added
        import_added = False  # Flag to check if import statement is already added
        for line in lines:
            if not import_added and line.startswith('from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local'):
                import_added = True

            if not added_import and line.startswith('class '):
                file.write(f'from FW_Automation_Local_Deploy_PyCharm.to_import import URL_local\n\n')
                added_import = True

            file.write(line)

            # Check if line contains a class definition
            if re.match(r'^\s*class\s+\w+', line):
                if not init_added:
                    init_added = True
                    # Add the init method after the class definition
                    file.write(f'\n    URL = URL_local  # Default value\n')
                    file.write('    def __init__(self, methodName="runTest", URL=None):\n')
                    file.write('        super().__init__(methodName)\n')
                    file.write('        if URL:\n')
                    file.write('            self.URL = URL\n\n')

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_init_method_to_file(file_path)
                print(f'Updated {file_path}')

if __name__ == '__main__':
    project_directory = r'C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\FW_Automation_Local_Deploy_PyCharm'  # Update with your project path
    process_directory(project_directory)
