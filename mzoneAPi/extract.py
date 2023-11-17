import json
import csv

# Open the JSON file for reading
with open('input.json', 'r') as json_file:
    data = json.load(json_file)['value']

# Create a CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:
    # Define the CSV writer and write the header row
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['id', 'description'])

    # Iterate through each JSON object in the 'value' array and write the 'id' and 'description' values to the CSV file
    for item in data:
        csv_writer.writerow([item['id'], item['description']])

print("CSV file has been created successfully.")
