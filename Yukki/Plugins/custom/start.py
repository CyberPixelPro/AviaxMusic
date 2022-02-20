from config import THUMBNAIL
from Yukki import SUDOERS, app
from pyrogram import filters
from Yukki.Plugins.custom.strings import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start_menu_private(message):
    mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    await message.reply_photo(photo=THUMBNAIL,caption=text,reply_markup=START_BUTTON_PRIVATE,parse_mode="markdown")

async def start_menu_group(message):
    mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    await message.reply_photo(photo=THUMBNAIL,caption=text,reply_markup=START_BUTTON_GROUP,parse_mode="markdown")

@app.on_callback_query(filters.regex("advanced_cmd"))
async def commands_menu(_, query):
    await query.answer()
    mention = "[" + query.from_user.first_name + "](tg://user?id=" + str(query.from_user.id) + ")"
    text = COMMANDS_TEXT.replace("MENTION",mention)
    if (query.from_user.id in SUDOERS):
        buttons = COMMANDS_BUTTON_SUDO
    else:
        buttons = COMMANDS_BUTTON_USER
    await query.message.edit(text=text,reply_markup=buttons)

@app.on_callback_query(filters.regex("admin_cmd"))
async def admin_menu(_, query):
    await query.answer()    
    await query.message.edit(text=ADMIN_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("play_cmd"))
async def play_menu(_, query):
    await query.answer()    
    await query.message.edit(text=PLAY_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("bot_cmd"))
async def bot_menu(_, query):
    await query.answer()    
    await query.message.edit(text=BOT_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("sudo_cmd"))
async def sudo_menu(_, query):
    await query.answer()    
    await query.message.edit(text=SUDO_TEXT,reply_markup=SUDO_BACK_BUTTON)

@app.on_callback_query(filters.regex("extra_cmd"))
async def extra_menu(_, query):
    await query.answer()    
    await query.message.edit(text=EXTRA_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("close_btn"))
async def closer_menu(_, query):
    await query.answer()    
    await query.message.delete()

@app.on_callback_query(filters.regex("open_start_menu"))
async def open_start_menu(_, query):
    await query.answer()
    if query.message.chat.type == "group":
        button = START_BUTTON_GROUP
    elif query.message.chat.type == "supergroup":
        button = START_BUTTON_GROUP
    elif query.message.chat.type == "private":
        button = START_BUTTON_PRIVATE

    mention = "[" + query.from_user.first_name + "](tg://user?id=" + str(query.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    await query.message.edit(text=text,reply_markup=button,parse_mode="markdown")
    
    
@app.on_callback_query(filters.regex("basic_cmd"))
async def basic_cmd(_, query): 
    await query.answer()   
    await query.message.edit(text=BASIC_TEXT,reply_markup=BASIC_BACK_BUTTON,parse_mode="markdown")    
    
    
    
@app.on_callback_query(filters.regex("command_menu"))
async def command_menu(_, query):
    await query.answer()   
    await query.message.edit(text="**Choose Basic Command to get Basic Bot Commands\nAnd Advanved Command to get Advanved Bot Commands.**",reply_markup=COMMAND_MENU_BUTTON,parse_mode="markdown")    