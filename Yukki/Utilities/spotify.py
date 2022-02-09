# dont steal these
client_id = "817ef3b667ae41fa904568b4eeaee96d"
client_secret = "8130539ee3cf4b30bc24d2f694a60838"

from Yukki import BOT_USERNAME
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track_info(url):
    try:
        track_info = sp.track(url)
        track_name = track_info["name"]
        artist = track_info["artists"][0]["name"]
        search = track_name + " " + artist
        return search
    except Exception as e:
        return "errrorrr" + str(e)

def get_playlist_info(url):
    try:
        playlist_info = sp.playlist(url)
        name = playlist_info["name"]
        owner = playlist_info["owner"]["display_name"]
        tracks = playlist_info["tracks"]["items"]        
        tracks_list = []
        for item in tracks:
            track_name = item["track"]["name"]
            artist = item["track"]["artists"][0]["name"]
            search = track_name + " " + artist
            tracks_list.append(search)
        return [name,owner,tracks_list]
    except Exception as e:
        return "errrorrr" + str(e)

def get_spotify_url(text):
    text = text.replace(f"/spotify@{BOT_USERNAME}","")
    text = text.replace(f"/spotify","")
    text = text.strip()
    if "spotify.com" in text:
        return text
    else:
        return ""

a =  sp.track("https://open.spotify.com/track/4qeHV9T5N3S7KAKryZQp8s?si=8ed7d1425efb4edd")
print(a["artists"][0]["name"])