import json
import os

def get_run_number():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)).split('Automatization_Project_Master_QA')[0], 'Automatization_Project_Master_QA', 'run_number.json')  # Adjust the path as needed

    # Check if the file exists; if not, create it with initial run number
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({'run_number': 1}, f)
        return 1  # First run

    # Read the current run number
    with open(file_path, 'r') as f:
        data = json.load(f)

    current_run_number = data['run_number']

    # Increment the run number
    new_run_number = current_run_number + 1

    # Save the new run number back to the file
    with open(file_path, 'w') as f:
        json.dump({'run_number': new_run_number}, f)

    return new_run_number