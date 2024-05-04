# ATLEAST GIVE CREDITS IF YOU STEALING :(((((((((((((((((((((((((((((((((((((
# ELSE NO FURTHER PUBLIC THUMBNAIL UPDATES

import os
import aiohttp
import aiofiles

from config import YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/AviaxAPI_{videoid}.png"): 
        return f"cache/AviaxAPI_{videoid}.png"

    url = f"http://5.161.84.77:8000/thumb/random?videoid={videoid}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/AviaxAPI_{videoid}.png", mode="wb" ) 
                    await f.write(await resp.read()) 
                    await f.close()

        return f"cache/AviaxAPI_{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
