'''
Author: Sohaib Mohiuddin
Date: Winter 2025
Description: This application will test the sending of an email using the smtplib library. This application will use Testmail.app to send the email and receive it.
'''

import os, json, requests
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

API_KEY = os.getenv('TESTMAIL_API')
NAMESPACE = os.getenv('TESTMAIL_NS')

# api-endpoint
URL = "https://api.testmail.app/api/json"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'apikey':API_KEY, 'namespace':NAMESPACE}

# sending get request and saving the response as response object
response = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = response.json()
print(json.dumps(data, indent=4))