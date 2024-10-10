import asyncio
from pyrogram import filters
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.database import get_assistant
from AviaxMusic import app

@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & filters.user(SUDOERS))
async def leave_all(client, message):
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
            except Exception as e:
                failed += 1
                print(f"Failed to leave chat {dialog.chat.id}: {e}")
            
            await lol.edit(
                f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
            await asyncio.sleep(3)
    
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ: {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ: {failed} chats."
        )
