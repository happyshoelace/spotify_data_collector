import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from timertool import write_current_unix_time
from clientsecret import SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI # Get this from Spotify Application Dashboard

scope = "user-read-recently-played"



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI))


def getRecentTracks():
    with open('time.txt', 'r') as file:
        after_timestamp = int(file.read().strip())

    newScrobbles = []

    results = sp.current_user_recently_played(after=after_timestamp)
    for item in enumerate(results['items']):
        track = item['track']
        played_at_str = item['played_at']
        played_at_struct = time.strptime(played_at_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        unix_timestamp_ms = int(time.mktime(played_at_struct) * 1000)

        trackData = [track['artists'][0]['name'], track['album']['name'], track['name'], unix_timestamp_ms]
        newScrobbles.append(trackData)

    write_current_unix_time()
    return newScrobbles