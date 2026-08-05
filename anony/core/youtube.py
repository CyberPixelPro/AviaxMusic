import asyncio
import os
import re
import json
from typing import Union
import requests
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from py_yt import VideosSearch
from ShiviMusic.utils.database import is_on_off
from ShiviMusic import app
from ShiviMusic.utils.formatters import time_to_seconds
import os
import glob
import random
import logging
import pymongo
from pymongo import MongoClient
import aiohttp
import config
import traceback
from ShiviMusic import LOGGER

API_URL = "https://teaminflex.xyz"  # Change to your API server URL
API_KEY = "INFLEX93431728D"

# ==============================================
# 🎵 AUDIO DOWNLOAD (Safe JSON + 200 Retry)
# ==============================================
async def download_song(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    logger = LOGGER("InflexMusic/platforms/Youtube.py")
    logger.info(f"🎵 [AUDIO] Starting download process for ID: {video_id}")

    if not video_id or len(video_id) < 3:
        return

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.webm")

    if os.path.exists(file_path):
        logger.info(f"🎵 [LOCAL] Found existing audio for ID {video_id}")
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            payload = {"url": video_id, "type": "audio"}
            headers = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

            async def safe_json(resp):
                try:
                    return await resp.json(content_type=None)
                except:
                    txt = await resp.text()
                    logger.error(f"[AUDIO] Invalid JSON → {txt}")
                    return None

            # Step 1 → First request
            async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                data = await safe_json(response)

            # 🚫 STOP if API explicitly returns error
            if data and data.get("status") == "error":
                logger.error(f"[AUDIO] API ERROR → {data}")
                return

            retries = 200

            if not data or not data.get("download_url"):
                logger.warning("[AUDIO] File not ready / JSON missing → retrying...")

                for i in range(retries):
                    await asyncio.sleep(8)
                    async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                        data = await safe_json(response)

                    # 🚫 STOP retrying if error appears anytime
                    if data and data.get("status") == "error":
                        logger.error(f"[AUDIO] API ERROR during retry → {data}")
                        return

                    if data and data.get("status") == "success" and data.get("download_url"):
                        logger.info(f"[AUDIO] Got URL after retry #{i+1}")
                        break

                    logger.warning(f"[AUDIO] Retry {i+1}/{retries} → still not ready")

            if not data or not data.get("download_url"):
                logger.error(f"[AUDIO] FAILED after all retries → {data}")
                return

            download_link = API_URL + data["download_url"]

            async with session.get(download_link) as file_response:
                if file_response.status != 200:
                    logger.error(f"[AUDIO] Download failed → {file_response.status}")
                    return

                with open(file_path, "wb") as f:
                    async for chunk in file_response.content.iter_chunked(8192):
                        f.write(chunk)

        logger.info(f"🎵 [API] Audio download completed for {video_id}")
        return file_path

    except Exception as e:
        logger.error(f"[AUDIO] Exception: {e}")
        return


# ==============================================
# 🎥 VIDEO DOWNLOAD (Safe JSON + 100 Retry)
# ==============================================
async def download_video(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    logger = LOGGER("InflexMusic/platforms/Youtube.py")
    logger.info(f"🎥 [VIDEO] Starting download process for ID: {video_id}")

    if not video_id or len(video_id) < 3:
        return

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mkv")

    if os.path.exists(file_path):
        logger.info(f"🎥 [LOCAL] Found existing video for ID {video_id}")
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            payload = {"url": video_id, "type": "video"}
            headers = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

            async def safe_json(resp):
                try:
                    return await resp.json(content_type=None)
                except:
                    txt = await resp.text()
                    logger.error(f"[VIDEO] Invalid JSON → {txt}")
                    return None

            # Step 1 → First request
            async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                data = await safe_json(response)

            # 🚫 STOP if API explicitly returns error
            if data and data.get("status") == "error":
                logger.error(f"[VIDEO] API ERROR → {data}")
                return

            retries = 100

            if not data or not data.get("download_url"):
                logger.warning("[VIDEO] File not ready / JSON missing → retrying...")

                for i in range(retries):
                    await asyncio.sleep(20)
                    async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                        data = await safe_json(response)

                    # 🚫 STOP retrying if error appears anytime
                    if data and data.get("status") == "error":
                        logger.error(f"[VIDEO] API ERROR during retry → {data}")
                        return

                    if data and data.get("status") == "success" and data.get("download_url"):
                        logger.info(f"[VIDEO] Got URL after retry #{i+1}")
                        break

                    logger.warning(f"[VIDEO] Retry {i+1}/{retries} → still not ready")

            if not data or not data.get("download_url"):
                logger.error(f"[VIDEO] FAILED after all retries → {data}")
                return

            download_link = API_URL + data["download_url"]

            async with session.get(download_link) as file_response:
                if file_response.status != 200:
                    logger.error(f"[VIDEO] Download failed → {file_response.status}")
                    return

                with open(file_path, "wb") as f:
                    async for chunk in file_response.content.iter_chunked(8192):
                        f.write(chunk)

        logger.info(f"🎥 [API] Video download completed for {video_id}")
        return file_path

    except Exception as e:
        logger.error(f"[VIDEO] Exception: {e}")
        return



async def check_file_size(link):
    async def get_format_info(link):
        cookie_file = cookie_txt_file()
        if not cookie_file:
            print("No cookies found. Cannot check file size.")
            return None
            
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "--cookies", cookie_file,
            "-J",
            link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            print(f'Error:\n{stderr.decode()}')
            return None
        return json.loads(stdout.decode())

    def parse_size(formats):
        total_size = 0
        for format in formats:
            if 'filesize' in format:
                total_size += format['filesize']
        return total_size

    info = await get_format_info(link)
    if info is None:
        return None
    
    formats = info.get('formats', [])
    if not formats:
        print("No formats found.")
        return None
    
    total_size = parse_size(formats)
    return total_size

async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        return None

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["title"]

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["duration"]

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["thumbnails"][0]["url"].split("?")[0]

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        try:
            downloaded_file = await download_video(link)
            if downloaded_file:
                return 1, downloaded_file
            else:
                return 0, "Video API did not return a valid file."
        except Exception as e:
            print(f"Video API failed: {e}")
            return 0, f"Video API failed: {e}"

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid:
            link = self.listbase + link
        if "&" in link:
            link = link.split("&")[0]
        cookie_file = cookie_txt_file()
        if not cookie_file:
            return []
        playlist = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --cookies {cookie_file} --playlist-end {limit} --skip-download {link}"
        )
        try:
            result = [key for key in playlist.split("\n") if key]
        except:
            result = []
        return result

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        cookie_file = cookie_txt_file()
        if not cookie_file:
            return [], link
        ytdl_opts = {"quiet": True, "cookiefile": cookie_file}
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        with ydl:
            formats_available = []
            r = ydl.extract_info(link, download=False)
            for format in r["formats"]:
                try:
                    if "dash" not in str(format["format"]).lower():
                        formats_available.append(
                            {
                                "format": format["format"],
                                "filesize": format.get("filesize"),
                                "format_id": format["format_id"],
                                "ext": format["ext"],
                                "format_note": format["format_note"],
                                "yturl": link,
                            }
                        )
                except:
                    continue
        return formats_available, link

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            link = self.base + link

        # Simplified: API-only download
        try:
            if songvideo or songaudio:
                downloaded_file = await download_song(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
            elif video:
                downloaded_file = await download_video(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
            else:
                downloaded_file = await download_song(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
        except Exception as e:
            print(f"API download failed: {e}")
            return None, False
