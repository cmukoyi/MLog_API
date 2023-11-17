import requests
import json

url_template = "https://stg.mzoneweb.net/mzone62.api/Vehicles({})"
vehicle_group_ids = [
    "338b8f38-7a7d-475e-8c35-ef71f00a13ef",
    "95f11ee2-dde8-44fd-b60a-1da7f611295e"
]
authorization_token = 'Bearer'

def generate_payload(vehicle_id):
    payload = {
        "monthlyDistanceLimit": 0,
        "beacon_Id": None,
        "vehicleGroupIds": vehicle_group_ids,
        "driverAuthorizationOverrideDriverIds": [],
        # Add any other fields specific to the vehicle ID here
    }
    return json.dumps(payload)

with open('C:/Users/Carlos Mukoyi/Documents/code\mzoneAPi/vehicle_ids.txt', 'r') as file:
    vehicle_ids = [id.strip() for line in file for id in line.split(',')]

headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization_token,
}

for vehicle_id in vehicle_ids:
    # Construct the URL with the specific vehicle_id
    api_url = url_template.format(vehicle_id)

    # Generate the payload for this vehicle_id
    payload = generate_payload(vehicle_id)

    # Send the API request
    response = requests.patch(api_url, headers=headers, data=payload)

    # Print the response for each vehicle_id
    print(f"Vehicle ID: {vehicle_id}")
    print(response.text)
    print("=" * 50)  # Separating each response with a line

print("All API requests completed.")
