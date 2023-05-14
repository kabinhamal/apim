import msal
import requests

# Define the AAD authentication parameters
tenant_id = "f44-c85226657b01"
client_id = "39ac6199"
client_secret = "6r68bjj"
scope = ["api://b1b2a55d58c8d2/.default"]


# Construct the request body
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope
}

# Send the POST request to the token endpoint
response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", data=data)

# Parse the response JSON
response_json = response.json()

# Check if the access token was successfully retrieved
if "access_token" in response_json:
    access_token = response_json["access_token"]
    print(f"Access token: {access_token}")
else:
    print(f"Failed to acquire access token. Response: {response.text}")

