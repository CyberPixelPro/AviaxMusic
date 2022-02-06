from inspect import getfullargspec
from pydoc import cli

from pyrogram import Client, filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5, BOT_USERNAME, LOG_GROUP_ID,app)

from config import LEAVE_CHANNELS

welcome_group = 2
list1 = [LOG_GROUP_ID,-1001572029526,-1001642562293]

@Client.on_message(filters.new_chat_members)
async def essential1(client, message: Message):
    if LEAVE_CHANNELS == "True":
        chat_id = message.chat.id    
        for member in message.new_chat_members:
            try:
                if message.chat.type == "channel":
                    if not (chat_id in list1):     
                        return await client.leave_chat(chat_id) 
                else:
                    if client != app:
                        try:
                            await client.get_chat_member(chat_id, member.id)
                            return
                        except:
                            try:
                                await client.send_message(chat_id,
                                f"**Can't find Bot ({BOT_USERNAME}) in this group, Add music bot to this group first, then add me.**")
                            except:
                                pass
                            await client.leave_chat(chat_id)               
            except Exception as e:
                return print(e)

@Client.on_message(filters.left_chat_member)
async def essential2(client, message: Message):
    try:
        members_list = await client.get_chat_members(message.chat.id,limit=5)        
    except:
        try:
            members_list = await client.get_chat_members(message.chat.id)
        except Exception as e:
                return print(e)
    try:
        length = len(members_list)
        if length < 3:
            await client.leave_chat(message.chat.id)
    except Exception as e:
                return print(e)