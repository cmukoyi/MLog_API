import csv
from datetime import datetime

# Function to parse date from text
def parse_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y %I:%M %p")

# Read dates from file
file_path = "C:/Users/Carlos Mukoyi/Documents/code/General/dates.txt"  # Change this to the path of your text file
with open(file_path, "r") as file:
    dates = [parse_date(line.strip()) for line in file]

# Calculate days left from today for each date
today = datetime.now()
output_data = []
for date in dates:
    days_left = (date - today).days
    output_data.append([date.strftime('%d/%m/%Y %I:%M %p'), days_left])
    print(f"Date: {date.strftime('%d/%m/%Y %I:%M %p')}, Days left: {days_left}")

# Write output to CSV file
output_file = "C:/Users/Carlos Mukoyi/Documents/code/General/output.csv"  # Change this to the desired output file path
with open(output_file, "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Date", "Days Left"])
    writer.writerows(output_data)

print("Output saved to", output_file)
