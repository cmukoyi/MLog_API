import requests
import json

url_template = "https://stg.mzoneweb.net/mzone62.api/Vehicles({})"
vehicle_group_ids = [
    "338b8f38-7a7d-475e-8c35-ef71f00a13ef",
    "95f11ee2-dde8-44fd-b60a-1da7f611295e"
]
authorization_token = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkZENDFDNjgxNEU2OEQyMjM5RDExRkQ5NTY0MUM2QzcyM0M3OUZBOUYiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJfVUhHZ1U1bzBpT2RFZjJWWkJ4c2NqeDUtcDgifQ.eyJuYmYiOjE2OTY4ODUyMDUsImV4cCI6MTY5Njg4ODgwNSwiaXNzIjoiaHR0cHM6Ly9sb2dpbi1zdGcubXpvbmV3ZWIubmV0IiwiYXVkIjpbImh0dHBzOi8vbG9naW4tc3RnLm16b25ld2ViLm5ldC9yZXNvdXJjZXMiLCJtejYtYXBpIl0sImNsaWVudF9pZCI6Im16NiBQS0NFIiwic3ViIjoiYzY1MjkwZDQtMzYxNS00ZGIyLTg1ZjQtZmQyYTJkYjQ2ZTRlIiwiYXV0aF90aW1lIjoxNjk2ODcyMzEwLCJpZHAiOiJsb2NhbCIsIm16X3VzZXJuYW1lIjoiVGVsdG9uaWthQHNjb3BlIiwibXpfdXNlcmdyb3VwX2lkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwibXpfc2hhcmRfY29kZSI6IkRFRkFVTFQiLCJzY29wZSI6WyJvcGVuaWQiLCJtel91c2VybmFtZSIsIm16Ni1hcGkuYWxsIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.KoEGSGUnX8LAMO5w2d1e2DNV337h1FUPuWxB9fEF0yXTf4K0whyhASUDXsosxkDVzl3ZHRFqPrtGVGeQfR7A21lKBDsjhSYK09XMPQyfTlSI-4JQonOBKzNgpRV00w3PNAEYDYKcb1OyaZNh4cCuR1SmOC4CxAeQkv5FlWQvt-8jwfdH16F94dQaYZLf0PTF97Hj3QK_bZFP76GR9yojOhWQyF6td2Cg05SpwdgBppd6x21FwXlOGooo5dM2LqKmb2RZA3hLStcf0CSByWiWqJwG6zeqpqxokVQOJSyqVuWe9ztg9-SME6cZM_csB_opaGVi9eI2d9Tj-FBtqaoCraYBv7e9jo4SZKBvKO2uhrEghtD4sTL2aAvlXwmiV2NArw-Mlxhxz8TaPftRBQGlhRbUQuwwDQcOfTMvKVt88Ier3KVcF6c3FMjLTO3j0HxDhMB1ZBUCOfIsT9PfeuBSHPqYVJQ5RLLl0H_ssSQ22--PrvaF2qCLVRevRl2Z-JPcRhDFEjLDF8rTd9IFT43qnXh7jZPxZFgoFIgasK99Pww_uSzGTcMJHBHcUGACkNPZwJzAIZ4PYBL8dbUkFRCLsraUPlgptPvI302r30TzFBALJBFR9q-rclYMCh2I3utiAZV6qhuSA_Yrxdu7K7KAxAGdsaXAXabhNkeve40nCLE'

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
