# dont steal these
client_id = "817ef3b667ae41fa904568b4eeaee96d"
client_secret = "8130539ee3cf4b30bc24d2f694a60838"


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

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