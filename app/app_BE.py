import logging
from flask import Flask, request, jsonify
# Import the necessary modules and test suite functions from your script
from flask_cors import CORS
from FW.Detail_D import *
from FW.darkove_poukazy import *
from starter_master_browserstack import runner_tests_generalized
from FW.starter_local import suite_FW_full

def suite_FW_full2(url):
    suite = unittest.TestSuite()
    suite.addTest(TestDetailHotelu_D("test_detail_D", URL=url))
    return suite

app = Flask(__name__)
CORS(app)  # Enable CORS
logging.basicConfig(level=logging.DEBUG)

@app.route('/run_suite', methods=['POST'])
def run_suite():
    data = request.json
    logging.debug(f'Received data: {data}')

    web_brand = data.get('web_brand', 'FISCHER')
    version = data.get('version', 'FW-EW release 2024-05-16')
    url = data.get('URL')  # Use URL from request
    suite_name = data.get('suiteName')  # Get suiteName from request
    email = data.get('email')

    logging.debug(f'web_brand: {web_brand}, version: {version}, URL: {url}, suiteName: {suite_name}, email: {email}')

    # Dictionary to map suite names to functions
    suite_mapping = {
        'FW Public web full suite': suite_FW_full,
        # Add other suite mappings here
    }

    # Get the suite function from the mapping
    suite_function = suite_mapping.get(suite_name)

    if not suite_function:
        return jsonify({'status': 'error', 'message': f'Suite {suite_name} not found.'}), 400

    # Run the test suite
    try:
        runner_tests_generalized(lambda: suite_function(url), web_brand, version, url, email)
        return jsonify({'status': 'success', 'message': 'Test suite executed successfully.'}), 200
    except Exception as e:
        logging.error(f'Error running test suite: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)