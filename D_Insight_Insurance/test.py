import hashlib
import hmac
from datetime import datetime
from urllib.parse import urlparse
import base64
import requests


def create_signature(request_method, content, content_type, date, request_path, api_key):
    signature = sign(
        request_method,                # Request method (currently only GET is supported)
        content,                      # Request content
        content_type,                 # Request content type
        date,                         # Request date
        request_path,                 # Request path
        api_key                       # API Key
    )
    return signature

def sign(request_method, content, content_type, date, request_path, api_key):
    to_sign = build_signing_string(request_method, generate_checksum_for_content(content), content_type, date, request_path)
    return hmac_sign(to_sign, api_key.encode('utf-8'))

def hmac_sign(data, key):
    return base64.b64encode(hmac.new(key, data.encode('utf-8'), hashlib.sha1).digest()).decode()

def build_signing_string(request_method, content_checksum, content_type, date, request_path):
    return f"{request_method}|{content_checksum}|{content_type}|{date}|{request_path}"

def generate_checksum_for_content(content):
    if content is None:
        return hashlib.md5(b'').hexdigest()
    return hashlib.md5(content).hexdigest()

def get_rfc822_formatted_timestamp(utc_datetime):
    return utc_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')

# Example usage
api_service_url = "https://stg.driveprofiler.net/api/v1/"
query = "DriverRatingPlatform/CheckApiSettings"
api_key = "359BF04B-C5F1-4A9C-A7AE-269CED4E39E9"
tenant_name = "Scope_test"
data = None
method = "GET"  # or "POST" if needed

# Parameters
params = {}

rq_uri = urlparse(api_service_url + query)
content_type = "application/json"  # Assuming JSON content type for demonstration

content = None if method == "GET" or data is None else data.encode('utf-8')

utc_date_now = datetime.utcnow()
signature = create_signature(method, content, content_type, get_rfc822_formatted_timestamp(utc_date_now), rq_uri.path, api_key)
print('Signature:', signature)

headers = {
    'X-SCP-Authentication': tenant_name,
    'X-SCP-ContentSigned': signature,
    'X-SCP-Date': get_rfc822_formatted_timestamp(utc_date_now)
}

# Making the GET request
response = requests.get(api_service_url + query, params=params, headers=headers)

# Print the response
print('API Uri:', api_service_url + query)
print('Parameters:', params)
print(response.json())
