import requests

username = "your_username"
password = "your_password"
company_id = 1 # replace with actual company ID
device_id = 1 # replace with actual device ID
url = f"https://example.com/devices/{device_id}/timestamps/"

# retrieve the device
device = Device.objects.get(id=device_id)

# check if the user is the owner of the associated company
company = device.company
user = request.user
if company.owner == user:
    # create a Milldata instance
    milldata = Milldata(device=device, circle=21, feed_time=6,
                        circle_hold=15, actual_hold=900,
                        feed_status=True, overload_status=False)

    # serialize the instance
    serialized_milldata = MilldataSerializer(milldata).data

    # add company ID to the payload
    serialized_milldata['company_id'] = company_id

    # send the serialized data as a POST request to the API URL
    response = requests.post(url, json=serialized_milldata, auth=(username, password))

    # check if the request was successful
    if response.status_code == 201:
        print("Milldata instance created successfully.")
    else:
        print("Error creating Milldata instance:", response.json())
else:
    print("You are not authorized to access this device's data.")