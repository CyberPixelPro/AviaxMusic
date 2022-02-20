from Yukki import BOT_USERNAME
from Yukki.Database.spotifylimit import get_playlist_limit_sudoers
from config import PL_LIMIT
import requests
from bs4 import BeautifulSoup

def get_resso_track(url):
    try:        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        track_name = soup.find('title').text.replace("- Listening To Music On Resso","").strip()    
        return track_name
    except Exception as e:
        print(str(e))
        return "errrorrr"

async def get_resso_playlist(url,user):
    try:
        if PL_LIMIT == "TRUE":
            sudos = await get_playlist_limit_sudoers()
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        playlist_name = soup.find('h1').text
        owner = soup.find('h3').text
        tracks_list = []
        resso_list = soup.find_all('a', attrs = {'class':'song-wrapper'})
        for song in resso_list:
            name = song.find('h3').text
            artist = song.find('p').text
            search = name + " " + artist
            tracks_list.append(search.strip())        
        if PL_LIMIT == "TRUE":
            if user not in sudos:
                tracks_list = tracks_list[0:20]
        return [playlist_name,owner,tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"

def get_resso_url(text):
    text = text.replace(f"/resso@{BOT_USERNAME}","")
    text = text.replace(f"/resso","")
    url = text.strip()
    url = str(requests.get(url).url)
    if "resso.com" in url:
        return url
    else:
        return ""

async def get_resso_album(url,user):
    try:
        if PL_LIMIT == "TRUE":
            sudos = await get_playlist_limit_sudoers()
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        album_name = soup.find('h1').text
        owner = soup.find('a').text
        tracks_list = []
        song_list = soup.find('div', {"class" : "songs-list"})
        resso_list = song_list.find_all('h3')
        for song in resso_list:
            name = song.text
            artist = owner
            search = name + " " + artist
            tracks_list.append(search.strip())        
        if PL_LIMIT == "TRUE":
            if user not in sudos:
                tracks_list = tracks_list[0:20]
        return [album_name,owner,tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"

async def get_resso_artist(url):
    try:        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        artist = soup.find('h1').text
        owner = artist
        tracks_list = []
        resso_list = soup.find_all('h3')
        for song in resso_list:
            name = song.text
            artist = owner
            search = name + " " + artist
            tracks_list.append(search.strip())       
        tracks_list = tracks_list[0:10]
        return [artist,owner,tracks_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"