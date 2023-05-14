import msal
import requests

# Define the AAD authentication parameters
tenant_id = "89542121"
client_id = "3919"
client_secret = "6rj"
scope = ["api://b2/.default"]




# Create a new MSAL ConfidentialClientApplication object
app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

# Acquire an access token using MSAL
result = app.acquire_token_for_client(scopes=scope)

# Check if the access token was successfully retrieved
if "access_token" in result:
    access_token = result["access_token"]
    print(f"Access token: {access_token}")

print("================================================================")

# Call the Azure Worker API using the access token
api_endpoint = "https://<your_worker_api_endpoint>"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.post(api_endpoint, headers=headers)

# Check the response
if response.status_code == 200:
    print("API call succeeded.")
else:
    print(f"API call failed with status code {response.status_code}: {response.text}")
