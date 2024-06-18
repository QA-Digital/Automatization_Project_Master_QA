import os
import re

def add_init_method_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    import_statement = 'from DERRO.to_import import URL_local\n'
    init_method = [
        '    URL = URL_local  # Default value\n',
        '    def __init__(self, methodName="runTest", URL=None):\n',
        '        super().__init__(methodName)\n',
        '        if URL:\n',
        '            self.URL = URL\n\n'
    ]

    # Check if the import statement or init method are already in the file
    if import_statement in lines:
        import_added = True
    else:
        import_added = False

    init_added = any(init_method[0] in line for line in lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if not import_added and line.startswith('class '):
                file.write(import_statement)
                import_added = True

            file.write(line)

            # Check if line contains a class definition
            if re.match(r'^\s*class\s+\w+', line):
                if not init_added:
                    # Add the init method after the class definition
                    for init_line in init_method:
                        file.write(init_line)
                    init_added = True

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_init_method_to_file(file_path)
                print(f'Updated {file_path}')

if __name__ == '__main__':
    project_directory = r'C:\Users\KDK\Desktop\DTCZ\kod\Automatization_Project_Master_QA\DERRO_Automation_Local_Deploy_PyCharm'  # Update with your project path
    process_directory(project_directory)
