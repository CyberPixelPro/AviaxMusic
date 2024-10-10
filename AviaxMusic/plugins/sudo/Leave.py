import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import InviteRequestSent
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.database import get_assistant
import asyncio
import time
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
from AviaxMusic import app
from AviaxMusic.core.call import Aviax
from AviaxMusic.misc import db
from AviaxMusic.utils.database import get_assistant, get_authuser_names, get_cmode
from AviaxMusic.utils.decorators import ActualAdminCB, AdminActual, language
from AviaxMusic.utils.formatters import alpha_to_int, get_readable_time
from

links = {}


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001733534088:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ: {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ: {failed} chats.",
        )
