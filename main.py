import requests
import base64
from urllib.parse import urlencode

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

def get_song_data(uri,token):
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = 	"https://api.spotify.com/v1/audio-features/"
    lookup_url  = f"{endpoint}{uri}"
    r = requests.get(lookup_url,headers = headers)
    return r.json()
    
token = get_token()
get_song_data("3Fzlg5r1IjhLk2qRw667od", token)