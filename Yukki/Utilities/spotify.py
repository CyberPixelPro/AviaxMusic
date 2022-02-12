# dont steal these
client_id = "817ef3b667ae41fa904568b4eeaee96d"
client_secret = "8130539ee3cf4b30bc24d2f694a60838"

from config import PL_LIMIT
from Yukki import BOT_USERNAME
from Yukki.Database.spotifylimit import get_playlist_limit_sudoers
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def getsp_track_info(url):
    try:
        track_info = sp.track(url)
        track_name = track_info["name"]
        artist = track_info["artists"][0]["name"]
        search = track_name + " " + artist
        return search
    except Exception as e:
        print(str(e))
        return "errrorrr"

async def getsp_playlist_info(url,user):
    try:
        if PL_LIMIT == "TRUE":
            sudos = await get_playlist_limit_sudoers()
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
        if PL_LIMIT == "TRUE":
            if user not in sudos:
                tracks_list = tracks_list[0:20]
        return [name,owner,tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"

def get_spotify_url(text):
    text = text.replace(f"/spotify@{BOT_USERNAME}","")
    text = text.replace(f"/spotify","")
    text = text.strip()
    if "spotify.com" in text:
        return text
    else:
        return ""

async def getsp_album_info(url,user):
    try:
        if PL_LIMIT == "TRUE":
            sudos = await get_playlist_limit_sudoers()
        album_info = sp.album(url)
        name = album_info["name"]
        owner = album_info["artists"][0]["name"]
        tracks = album_info["tracks"]["items"]        
        tracks_list = []
        for item in tracks:
            track_name = item["name"]
            artist = item["artists"][0]["name"]
            search = track_name + " " + artist
            tracks_list.append(search)
        if PL_LIMIT == "TRUE":
            if user not in sudos:
                tracks_list = tracks_list[0:20]
        return [name,owner,tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"

async def getsp_artist_info(url):
    try:        
        artist_info = sp.artist_top_tracks(url)
        name = sp.artist(url)["name"]
        tracks = artist_info["tracks"]       
        tracks_list = []
        for item in tracks:
            track_name = item["name"]
            artist = item["artists"][0]["name"]
            search = track_name + " " + artist
            tracks_list.append(search)
        return [name,"artist",tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"