import requests
import base64
import json
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

def get_song_josn(uri,token):
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = 	"https://api.spotify.com/v1/audio-features/"
    lookup_url  = f"{endpoint}{uri}"
    r = requests.get(lookup_url,headers = headers)
    return r.json()
    

def get_playlist_json(uri,token):
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = 	"https://api.spotify.com/v1/playlists/"
    lookup_url  = f"{endpoint}{uri}"+"/tracks"
    r = requests.get(lookup_url,headers = headers)
    return = r.json()
    #for key in r_json["items"]:
    #    print(key["track"]["name"])
    #print(r_json["items"][0]["track"]["name"])

def get_tracks_from_playlist_json(playlist):
    track = {}
    tracks = {"uri": ""}
    for key in 

token = get_token()
#print(get_songs_from_playlist_data("3saqvuBi9fmCTu22uu1ZMN", token))
get_songs_from_playlist_data("3saqvuBi9fmCTu22uu1ZMN", token)