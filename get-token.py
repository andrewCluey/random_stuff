import requests

client_id = ''
client_secret = ''
scope = "api://6af8xxxxxxxxxxxxxxxxxxxxxxxx/.default"
tenant_id = input("enter your tenant ID")
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

http_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
http_body = {
    "client_id": {client_id},
    "scope": {scope},
    "client_secret": {client_secret},
    "grant_type": "client_credentials",
}
response = requests.post(token_url, data=http_body, headers=http_headers)
print(response.json()["access_token"])

# check if succesful
#if response.returncode == 0:
#    try:
#        token_response = json.loads(response.stdout)
#        access_token = token_response.get('access_token')#

        #if access_token:
         #   print(f"Access token: {access_token}")
        #else:
       #     print("Access token not found in response.")
    #except json.JSONDecodeError:
     #   print("Failed to parse JSON response.")
#else:
 #   print(f"Error executing curl command: {response.stderr}")
