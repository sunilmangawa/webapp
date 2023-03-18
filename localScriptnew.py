# Import the required libraries:
import requests
from requests.auth import HTTPBasicAuth
import json

# Define the API url and endpoint:
# url = 'http://localhost:8000/milldata'
# endpoint = '/devices/{device_id}/timestamps/'
# url = 'http://localhost:8000/milldata/devices/1/timestamps/'
url = 'http://localhost:8000/milldata/devices/1/'


# Define the credentials:
username = 'testuser1'
password = 'Test4work'
# company_id = '2'
# device_id = '1'


# Define the MillData object to be sent to the API:
milldata = {
    'katta_time': '2022-03-18 12:56:00',
    'katta_weight': 100.0,
    'circle': 18,
    'feed_time': 9,
    'circle_hold': 15,
    'actual_hold': 900,
    'feed_status': True,
    'overload_status': False
}
print(f"Data is {milldata} and data type is {type(milldata)}")


# Convert the data to JSON format
json_data = json.dumps(milldata)
print(f"JSON data is {json_data} and data type is {type(json)}")

# Set the headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request to the API url with the MillData object and credentials:
response = requests.post(
    # url + endpoint.format(device_id=device_id),
    url,
    # json=milldata,
    data=json_data,
    headers=headers,
    # auth=HTTPBasicAuth(username, password),
    auth=(username, password),
    # params={'company_id': company_id}
)


# Check the response status code and print the response message:
if response.status_code == 201:
    print('MillData sent successfully.')
else:
    print('Failed to send MillData:', response.text)

# Putting it all together, the code block would look like this:
