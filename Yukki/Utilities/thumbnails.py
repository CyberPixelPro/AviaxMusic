from Yukki import BOT_NAME
import os
import random
from os import path

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np


def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""    
    for i in list:
        if len(text1) + len(i) < 24:        
            text1 += " " + i
        elif len(text2) + len(i) < 24:        
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()     
    return [text1,text2]

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(thumbnail, title, userid, status, views, duration, channel):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"cache/thumb{userid}.jpg", mode="wb")
                await f.write(await resp.read())
                await f.close()
    
    image = Image.open(f"cache/thumb{userid}.jpg")
    black = Image.open("Utils/black.jpg")
    circle = Image.open("Utils/circle.png")
    image1 = changeImageSize(1280, 720, image)
    image1 = image1.filter(ImageFilter.BoxBlur(10))
    image11 = changeImageSize(1280, 720, image)
    image1 = image11.filter(ImageFilter.BoxBlur(10))
    image2 = Image.blend(image1,black,0.6)

    # Cropping circle from thubnail
    image3 = image11.crop((280,0,1000,720))
    lum_img = Image.new('L', [720,720] , 0)
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
    img_arr =np.array(image3)
    lum_img_arr =np.array(lum_img)
    final_img_arr = np.dstack((img_arr,lum_img_arr))
    image3 = Image.fromarray(final_img_arr)
    image3 = image3.resize((600,600))

    image2.paste(image3, (50,70), mask = image3)
    image2.paste(circle, (0,0), mask = circle)

    # fonts
    font1 = ImageFont.truetype(r'Utils/arial_bold.ttf', 30)
    font2 = ImageFont.truetype(r'Utils/arial_black.ttf', 60)
    font3 = ImageFont.truetype(r'Utils/arial_black.ttf', 40)
    font4 = ImageFont.truetype(r'Utils/arial_bold.ttf', 35)

    image4 = ImageDraw.Draw(image2)
    image4.text((10, 10), BOT_NAME, fill="white", font = font1, align ="left") 
    image4.text((670, 150), status, fill="white", font = font2, align ="left") 

    # title
    title1 = truncate(title)
    image4.text((670, 300), text=title1[0], fill="white", font = font3, align ="left") 
    image4.text((670, 350), text=title1[1], fill="white", font = font3, align ="left") 

    # description
    views = f"Views : {views}"
    duration = f"Duration : {duration} Mins"
    channel = f"Channel : {channel}"

    image4.text((670, 450), text=views, fill="white", font = font4, align ="left") 
    image4.text((670, 500), text=duration, fill="white", font = font4, align ="left") 
    image4.text((670, 550), text=channel, fill="white", font = font4, align ="left")

    image2.save(f"cache/final{userid}.png")
    os.remove(f"cache/thumb{userid}.jpg")
    final = f"cache/final{userid}.png"
    return final
