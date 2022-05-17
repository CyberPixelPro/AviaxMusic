from YukkiMusic.utils.inline.play import playlist_markup
import random
import string
from config import BANNED_USERS
from YukkiMusic.plugins.techzbots.spotify import getsp_categories, getsp_categories_info
from YukkiMusic import app, Spotify
import pyrogram
from pyrogram import filters
from YukkiMusic.plugins.techzbots.strings import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

uname = app.username
from config import BANNED_USERS, lyrical

@app.on_message(
    filters.command(["browse",f"browse@{uname}"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def browse_menu(_, message):
    try:        
        buttons = getsp_categories()        
        return await message.reply_text("**⭐️ Select the Category from which you want to listen songs !!!**",reply_markup=InlineKeyboardMarkup(buttons[0]))
    except:
        pass

@app.on_callback_query(filters.regex("cat"))
async def browse_menu(_, query):
    try:
        data = query.data.replace("cat","").strip()
        buttons = getsp_categories()
        await query.answer()
        if data == "pg1":
            return await query.message.edit("**⭐️ Select the Category from which you want to listen songs !!!**",reply_markup=InlineKeyboardMarkup(buttons[0]))
        elif data == "pg2":
            return await query.message.edit("**⭐️ Select the Category from which you want to listen songs !!!**",reply_markup=InlineKeyboardMarkup(buttons[1]))
        elif data == "pg3":
            return await query.message.edit("**⭐️ Select the Category from which you want to listen songs !!!**",reply_markup=InlineKeyboardMarkup(buttons[2]))

        category_pl_buttons = getsp_categories_info(data)
        category_pl_buttons.append([
                InlineKeyboardButton(
                    text="↪️ Refresh", callback_data=f"refbrowse {data}"
                ),
                InlineKeyboardButton(
                    text="↪️ Back", callback_data="cat pg1"
                ),            
            ],)
        return await query.message.edit("**⭐️ Now Select the playlist you want to listen from your choosed category !!!**",reply_markup=InlineKeyboardMarkup(category_pl_buttons))
    except:
        pass

@app.on_callback_query(filters.regex("refbrowse"))
async def refresh_browse(_, query):
    try:
        await query.answer(
                    f"🔄 Refreshed", show_alert=True
                )
        data = query.data.replace("refbrowse","").strip()
        
        category_pl_buttons = getsp_categories_info(data)
        category_pl_buttons.append([
                InlineKeyboardButton(
                    text="🔄 Refresh", callback_data=f"refbrowse {data}"
                ),
                InlineKeyboardButton(
                    text="↪️ Back", callback_data="cat pg1"
                ),            
            ],)
        return await query.message.edit("**⭐️ Now Select the playlist you want to listen from your choosed category !!!**",reply_markup=InlineKeyboardMarkup(category_pl_buttons))
    except:
        pass

@app.on_callback_query(filters.regex("psppl"))
async def psppl(_, query):
    ran_hash = "".join(
        random.choices(
            string.ascii_uppercase + string.digits, k=10
        )
    )
    lyrical[ran_hash] = query.data.replace("psppl","").strip()    
    buttons = playlist_markup(
        _,
        ran_hash,
        query.from_user.id,
        "spplay",
        "g",
        "d",
    )   
    a = "**Spotify Play Mode**\n\nRequested By:- {0}" 
    await query.message.reply_photo(
        photo=config.START_IMG_URL,
        caption=a.format(
                    query.from_user.first_name
                ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    await query.message.delete()
