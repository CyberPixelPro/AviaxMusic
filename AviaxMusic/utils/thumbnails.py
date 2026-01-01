# ATLEAST GIVE CREDITS IF YOU STEALING :(((((((((((((((((((((((((((((((((((((
# ELSE NO FURTHER PUBLIC THUMBNAIL UPDATES

import os
import re
import random

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from py_yt import VideosSearch

from config import YOUTUBE_IMG_URL


def truncate(text, max_len=30):
    words = text.split()
    lines = ["", ""]
    i = 0
    for word in words:
        if len(lines[i]) + len(word) + 1 <= max_len:
            lines[i] += (" " if lines[i] else "") + word
        elif i == 0:
            i = 1

    return lines

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def circular_crop(img, size, border, color, scale=1.5):
    inner = size - 2 * border
    crop = int(size * scale)
    w, h = img.size
    img = img.crop((w//2-crop//2, h//2-crop//2, w//2+crop//2, h//2+crop//2))
    img = img.resize((inner, inner), Image.LANCZOS)

    out = Image.new("RGBA", (size, size), color)
    mask = Image.new("L", (inner, inner), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, inner, inner), 255)
    out.paste(img, (border, border), mask)

    outer = Image.new("L", (size, size), 0)
    ImageDraw.Draw(outer).ellipse((0, 0, size, size), 255)
    out.putalpha(outer)
    return out

def draw_text(draw, pos, text, font, fill):
    x, y = pos
    draw.text((x+2, y+2), text, font=font, fill="black")
    draw.text(pos, text, font=font, fill=fill)

def gen_gradient(size, start, end):
    base = Image.new("RGBA", size, start)
    top = Image.new("RGBA", size, end)
    mask = Image.linear_gradient("L").resize(size)
    base.paste(top, (0, 0), mask)
    return base


async def gen_thumb(videoid: str, thumb_size=(1280, 720)):
    path = f"cache/{videoid}.png"
    if os.path.isfile(path):
        return path
    try:
        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1, with_live=False)
        data = (await results.next())["result"][0]
        title = re.sub(r"\W+", " ", data.get("title", "Unsupported Title")).title()
        duration = data.get("duration") or "00:00"
        views = data.get("viewCount", {}).get("short", "Unknown Views")
        channel = data.get("channel", {}).get("name", "Unknown Channel")
        thumb_url = data["thumbnails"][0]["url"].split("?")[0]
        
        async with aiohttp.ClientSession() as session:
            async with session.get(thumb_url) as resp:
                content = await resp.read()

        temp_path = f"cache/thumb_{videoid}.png"
        async with aiofiles.open(temp_path, "wb") as f:
            await f.write(content)

        base_img = Image.open(temp_path).convert("RGBA")
        base_img.thumbnail(thumb_size, Image.Resampling.LANCZOS)

        bg = base_img.filter(ImageFilter.BoxBlur(20))
        bg = ImageEnhance.Brightness(bg).enhance(0.6)
        grad = gen_gradient(thumb_size, random_color(), random_color())
        bg = Image.blend(bg, grad, 0.2)

        draw = ImageDraw.Draw(bg)
        font_small = ImageFont.truetype("AviaxMusic/assets/font2.ttf", 30)
        font_title = ImageFont.truetype("AviaxMusic/assets/font3.ttf", 45)

        circle = circular_crop(base_img, 400, 20, random_color())
        circle.show()
        bg.paste(circle, (120, 160), circle)

        x, y = 565, 380
        t1, t2 = truncate(title)

        draw_text(draw, (x, 180), t1, font_title, "white")
        draw_text(draw, (x, 230), t2, font_title, "white")
        draw_text(draw, (x, 320), f"{channel} | {views[:23]}", font_small, "white")

        pct = random.uniform(0.15, 0.85)
        color_len = int(580 * pct)
        color = random_color()

        draw.line((x, y, x + color_len, y), fill=color, width=9)
        draw.line((x + color_len, y, x + 580, y), fill="white", width=8)
        draw.ellipse((x + color_len - 10, y - 10, x + color_len + 10, y + 10), fill=color)

        draw_text(draw, (x, 400), "00:00", font_small, "white")
        draw_text(draw, (1080, 400), duration, font_small, "white")

        icons = Image.open("AviaxMusic/assets/play_icons.png").convert("RGBA")
        bg.paste(icons, (x, 450), icons)
        bg.save(path)

        os.remove(temp_path)
        return path

    except Exception as ex:
        print(ex)
        return YOUTUBE_IMG_URL
