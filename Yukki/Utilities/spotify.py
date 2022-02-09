# dont steal these
client_id = "817ef3b667ae41fa904568b4eeaee96d"
client_secret = "8130539ee3cf4b30bc24d2f694a60838"

from Yukki import BOT_USERNAME
from pyfy import ClientCreds, Spotify

client = ClientCreds(client_id=client_id, client_secret=client_secret)
spt = Spotify(client_creds=client)
spt.authorize_client_creds()

def get_track_info(track_id):
    try:
        track_info = spt.tracks(track_id)
        track_name = track_info["name"]
        return track_name
    except Exception as e:
        return "errrorrr" + e

def get_playlist_info(playlist_id):
    try:
        playlist_info = spt.playlist(playlist_id)
        name = playlist_info["name"]
        owner = playlist_info["owner"]
        tracks = playlist_info["tracks"]["items"]        
        tracks_list = []
        for item in tracks:
            a = item["track"]["name"]
            tracks_list.append(a)
        return [name,owner,tracks_list]
    except Exception as e:
        return "errrorrr" + e

def get_spotify_url(text):
    text = text.replace(f"/spotify@{BOT_USERNAME}","")
    text = text.replace(f"/spotify","")
    text = text.strip()
    if "spotify.com" in text:
        return text
    else:
        return ""