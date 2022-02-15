from unicodedata import category
from Yukki.Utilities.spotify import getsp_categories, getsp_categories_info
from Yukki import app
import pyrogram
from pyrogram import filters
from Yukki.Plugins.custom.strings import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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