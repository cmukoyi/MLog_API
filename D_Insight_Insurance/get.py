import hashlib
import hmac
from datetime import datetime
from urllib.parse import urlparse
import base64
import requests



def create_signature(request_uri, utc_date_now, method, content, api_key):
    signature = sign(
        method,                                     # POST or GET
        content,                                    # Request content
        "application/json",                         # JSON or XML
        get_rfc822_formatted_timestamp(utc_date_now),  # Current UTC timestamp
        request_uri,                                # Request URI
        api_key                                     # API Key
    )
    return signature

def sign(verb, content, content_type, date, request_uri, secret_key):
    to_sign = build_signing_string(verb, generate_checksum_for_content(content), content_type, date, request_uri)
    algorithm = hashlib.sha1
    return hmac_sign(to_sign, secret_key, algorithm)

def hmac_sign(data, key, algorithm):
    return base64.b64encode(hmac.new(key.encode('utf-8'), data.encode('utf-8'), algorithm).digest()).strip()

def build_signing_string(verb, content_checksum, content_type, date, request_uri):
    return f"{verb}\n{content_checksum}\n{content_type}\n{date}\n{request_uri}"

def generate_checksum_for_content(content):
    if content is None:
        return ""
    return hashlib.sha1(content).hexdigest()


def get_rfc822_formatted_timestamp(utc_datetime):
    return utc_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')

# Example usage
api_service_url = "https://stg.driveprofiler.net/api/v1/"
query = "DriverRatingPlatform/DriverTripExpressions?profileId=c368a0fd-8d44-4dfd-8107-8e8a1602ea39&driverKeyCode=17142&startTimestamp=2024-03-29T15:21:03&endTimestamp=2024-03-29T15:54:09"
api_key = "4559150C-FA81-4EDD-8D21-6CAB9FE6A76B"
tenant_name = "EFU STG DRP"
data = None
method = "GET"  # or "POST" if needed

# Parameters
params = {
    'profileId': 'c368a0fd-8d44-4dfd-8107-8e8a1602ea39',
    'driverKeyCode': '17142',
    'startTimestamp': '2024-03-29T15:21:03',
    'endTimestamp': '2024-03-29T15:54:09'
}

rq_uri = urlparse(api_service_url + query)

content = None if method == "GET" or data is None else data.encode('utf-8')

utc_date_now = datetime.utcnow()

signature = create_signature(rq_uri, utc_date_now, method, content, api_key)
print('Signature: ',signature)

headers = {
    'X-SCP-Authentication': tenant_name,
    'X-SCP-ContentSigned': signature,
    'X-SCP-Date': get_rfc822_formatted_timestamp(utc_date_now)
}

# Making the GET request
response = requests.get(api_service_url, params=params, headers=headers)

# Print the response
print('API Uri:',api_service_url)
print('Parameters: ',params)
print(response.json())


#print(headers)
