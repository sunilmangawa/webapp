
import requests
import json
from datetime import datetime

# Set the URL of the API endpoint to post data to
url = 'http://localhost:8000/milldata/devices/1/timestamps/'

# Set the data to be posted in JSON format
data = {
    'data': str(datetime.timestamp(datetime.now())),
    'initial_hold':600,
    'circle':21,
    'feed_time':6,
    'circle_hold':15,
    'galla_clear_time':20,
    'actual_hold':900,
}
print(f"Data is {data} and data type is {type(data)}")


# Convert the data to JSON format
json_data = json.dumps(data)
print(f"JSON data is {json_data} and data type is {type(json)}")

# Set the headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

# Set the username and password for authentication
username = 'testuser1'
password = 'Test4work'

# Send the POST request to the API endpoint with authentication
response = requests.post(url, data=json_data, headers=headers, auth=(username, password))

# Check if the request was successful
if response.status_code == 201:
    print("Data sent successfully")
else:
    print("Failed to send data")
    print(f"Status Code: {response.status_code}")

# Print the response from the API endpoint
print(response.content)