# dont steal these
client_id = "817ef3b667ae41fa904568b4eeaee96d"
client_secret = "8130539ee3cf4b30bc24d2f694a60838"

from config import PL_LIMIT
from Yukki import BOT_USERNAME
from Yukki.Database.spotifylimit import get_playlist_limit_sudoers
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

def getsp_categories_info(id):
    try: 
        cinfo = sp.category_playlists(id)        
        playlists = cinfo["playlists"]["items"]        
        plist1 = []
        plist3 = []
        pos = 0
        for item in playlists:
            pname = item["name"]
            pid = item["id"]
            plist2 = [pname,pid]
            if len(plist3) == 0:
                try:
                    plist3.append(plist2)
                except:
                    pass
            elif len(plist3) == 1:
                try:
                    plist3.append(plist2)
                except:
                    pass
            elif len(plist3) == 2:
                plist1.append(plist3)
                plist3 = []        
        button1 = []
        for i in plist1:
            try:    
                button2 = [
                            InlineKeyboardButton(text=i[0][0], callback_data="psppl" + i[0][1]),
                            InlineKeyboardButton(text=i[1][0], callback_data="psppl" + i[1][1]),                                   
                        ]
                button1.append(button2)
            except:
                try:    
                    button2 = [
                                InlineKeyboardButton(text=i[0][0], callback_data="psppl" + i[0][1]),                                
                            ]
                    button1.append(button2)
                except:
                    pass        
        return button1
    except Exception as e:
        print(str(e))
        return "errrorrr"

def getsp_categories():
    buttons1 = [   
            [
                InlineKeyboardButton(
                    text="Top Lists", callback_data=f"cat toplists"
                ),
                InlineKeyboardButton(
                    text="Pop", callback_data="cat pop"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="EQUAL", callback_data=f"cat equal"
                ),
                InlineKeyboardButton(
                    text="Mood", callback_data="cat mood"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="Decades", callback_data=f"cat decades"
                ),
                InlineKeyboardButton(
                    text="Hip-Hop", callback_data="cat hiphop"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="In the car", callback_data=f"cat in_the_car"
                ),
                InlineKeyboardButton(
                    text="Gaming", callback_data="cat gaming"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="❮", callback_data=f"cat pg3"
                ),
                InlineKeyboardButton(
                    text="Close", callback_data="close_btn"
                ),
                InlineKeyboardButton(
                    text="❯", callback_data="cat pg2"
                ),                                   
            ],            
        ]
    
    buttons2 = [            
            [
                InlineKeyboardButton(
                    text="Wellness", callback_data=f"cat wellness"
                ),
                InlineKeyboardButton(
                    text="Workout", callback_data="cat workout"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="Chill", callback_data=f"cat chill"
                ),
                InlineKeyboardButton(
                    text="Focus", callback_data="cat focus"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="Sleep", callback_data=f"cat sleep"
                ),
                InlineKeyboardButton(
                    text="Party", callback_data="cat party"
                ),                                   
            ],                            
            [
                InlineKeyboardButton(
                    text="Indie", callback_data=f"cat indie_alt"
                ),
                InlineKeyboardButton(
                    text="Metal", callback_data="cat metal"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="❮", callback_data=f"cat pg1"
                ),
                InlineKeyboardButton(
                    text="Close", callback_data="close_btn"
                ),
                InlineKeyboardButton(
                    text="❯", callback_data="cat pg3"
                ),                                   
            ],
        ]
    
    buttons3 = [            
            [
                InlineKeyboardButton(
                    text="Rock", callback_data=f"cat rock"
                ),
                InlineKeyboardButton(
                    text="Dance/Electronic", callback_data="cat edm_dance"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="Cooking & Dining", callback_data=f"cat dinner"
                ),
                InlineKeyboardButton(
                    text="Jazz", callback_data="cat jazz"
                ),                                   
            ],
            [
                InlineKeyboardButton(
                    text="❮", callback_data=f"cat pg2"
                ),
                InlineKeyboardButton(
                    text="Close", callback_data="close_btn"
                ),
                InlineKeyboardButton(
                    text="❯", callback_data="cat pg1"
                ),                                   
            ],
        ]
     
    return [buttons1,buttons2,buttons3]