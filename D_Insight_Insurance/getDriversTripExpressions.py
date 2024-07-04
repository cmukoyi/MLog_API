import requests
from datetime import datetime

# API endpoint
url = 'https://stg.driveprofiler.net/api/v1/DriverRatingPlatform/DriverTripExpressions'

# Parameters
params = {
    'profileId': 'c368a0fd-8d44-4dfd-8107-8e8a1602ea39',
    'driverKeyCode': '17142',
    'startTimestamp': '2024-03-29T15:21:03',
    'endTimestamp': '2024-03-29T15:54:09'
}

# Custom HTTP headers
headers = {
    'Content-Type': 'application/json',
    'X-SCP-Authentication': 'EFU STG DRP',
    'X-SCP-ContentSigned': 'F78lWm1YasMloplKqQqr/jLK4aU=',
    'X-SCP-Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

}
print(datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))

# Making the GET request
response = requests.get(url, params=params, headers=headers)

# Print the response
print(response.json())
