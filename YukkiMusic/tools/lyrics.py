#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import random
import re
import string
import aiohttp

import lyricsgenius as lg
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from config import BANNED_USERS, lyrical
from strings import get_command
from YukkiMusic import app
from YukkiMusic.utils.decorators.language import language

###Commands
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

@app.on_message(
    filters.command(LYRICS_COMMAND) & ~filters.edited & ~BANNED_USERS
)
@language
async def lrsearch(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(_["lyrics_1"])
    title = message.text.split(None, 1)[1]
    m = await message.reply_text(_["lyrics_2"])

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://techzbotsapi.herokuapp.com/lyrics?query={title}") as resp:
            if resp.status == 200:
                lyrics = await resp.json()
                lyrics = lyrics["lyrics"]
            else:
                lyrics = None

    if lyrics is None:
        return await m.edit(_["lyrics_3"].format(title))
    return await m.edit(lyrics)