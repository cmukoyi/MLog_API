import requests
import json
import csv

url = "https://live.scopemlog.net/api/public/unit/"

# Read values from CSV file
csv_file_path = "C:/Users/Carlos Mukoyi/Documents/code/MLog_API/file.csv"

# Assuming the CSV file has columns "UnitNo" and "Type"
data = []
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append({
            "UnitNo": row["UnitNo"],
            "Type": int(row["Type"])  # Assuming "Type" is an integer in the CSV
        })

# Convert data to JSON format
payload = json.dumps(data)

# API request headers
headers = {
    'Authorization': '',
    'Content-Type': 'application/json'
}

# Make API request
response = requests.post(url, headers=headers, data=payload)

# Print the response
print(response.text)
