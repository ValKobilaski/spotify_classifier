import requests
import base64

from secrets import client_id, client_secret

def get_token():
    token_url = "https://accounts.spotify.com/api/token"

    token_data = {"grant_type": "client_credentials"}

    client_creds = f"{client_id}:{client_secret}"
    encrypted_creds = base64.b64encode(client_creds.encode())
    token_headers = {"Authorization": f"Basic {encrypted_creds.decode()}"}

    r= requests.post(token_url,data=token_data, headers = token_headers).json()
    access_token = r['access_token']
    return access_token

print(get_token())