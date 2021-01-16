import json
import requests
from secrets import client_id, clinet_secret


def get_spotify_uri(self, song_name, artist):

    # TODO Figure out what query should be
    # query = "".format{song_name, artist}
    response = requests.get{
        query,
        heaers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(client_id)
        }
    }

    response_json = response.json()
    songs = response_json["tracks"]["items"]

    uri = songs[0]["url"]
