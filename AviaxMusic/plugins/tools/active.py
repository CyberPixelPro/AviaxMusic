from pyrogram import filters
from pyrogram.types import Message

from AviaxMusic import app
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def active_vc(_, message: Message):
    achats = len(await get_active_chats())
    vchats = len(await get_active_video_chats())
    await message.reply_text(f"<b>» ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs:</b>\n\nᴠᴏɪᴄᴇ: {achats}\nᴠɪᴅᴇᴏ: {vchats}")


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        chat = await app.get_chat(x)
        try:
            title = chat.title
        except:
            await remove_active_chat(x)
            continue
        try:
            if chat.username:
                user = chat.username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{title}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {title} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        chat = await app.get_chat(x)
        try:
            title = chat.title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if chat.username:
                user = chat.username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{title}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {title} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
