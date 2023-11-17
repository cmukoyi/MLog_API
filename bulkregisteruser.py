import csv
import requests
import json

url = "https://poc.connectedcar360.net/V1/api/account/RegisterWithPolicy"
headers = {
    'Content-Type': 'application/json'
}

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        payload = {
            "PolicyOrCustomerNumber": row['PolicyOrCustomerNumber'],
            "UserName": row['UserName '],  # Updated to include the extra space after 'UserName'
            "Password": row['Password'],
            "AgreementAccepted": "true"
        }

        
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful", response.status_code)
            print("Message:", response.text)
           
        else:
            print("Request failed with status code:", response.status_code)
            print("Error message:", response.text)
           

#        print("Request failed with status code:", response.status_code)
#        print(response.text)
