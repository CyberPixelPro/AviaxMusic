from Yukki.Database.spotifylimit import add_playlist_limit_sudo, get_playlist_limit_sudoers, remove_playlist_limit_sudo
import asyncio
import os
import shutil
import subprocess
from sys import version as pyver

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import LOG_SESSION, OWNER_ID, SUDO_USERS
from Yukki import BOT_ID, BOT_USERNAME, MUSIC_BOT_NAME, OWNER_ID, SUDOERS, app

@app.on_message(filters.command("approve") & filters.user(SUDOERS))
async def useradd(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "Reply to a user's message or give username/user_id."
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDOERS:
            return await message.reply_text(
                f"{user.mention} is already approved."
            )
        added = await add_playlist_limit_sudo(user.id)
        if added:
            await message.reply_text(
                f"Added **{user.mention}** to Approved Users."
            )            
        else:
            await message.reply_text("Failed")
        return
    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"{message.reply_to_message.from_user.mention} is already approved."
        )
    added = await add_playlist_limit_sudo(message.reply_to_message.from_user.id)
    if added:
        await message.reply_text(
            f"Added **{message.reply_to_message.from_user.mention}** to Approved Users"
        )        
    else:
        await message.reply_text("Failed")
    return


@app.on_message(filters.command("unapprove") & filters.user(SUDOERS))
async def userdel(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "Reply to a user's message or give username/user_id."
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id not in SUDOERS:
            return await message.reply_text(f"Not a part of Bot's Approved Users.")
        removed = await remove_playlist_limit_sudo(user.id)
        if removed:
            return await message.reply_text(
                f"Removed **{user.mention}** from {MUSIC_BOT_NAME}'s Approved Users."
            )            
        await message.reply_text(f"Something wrong happened.")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id not in SUDOERS:
        return await message.reply_text(
            f"Not a part of {MUSIC_BOT_NAME}'s Approved Users."
        )
    removed = await remove_playlist_limit_sudo(user_id)
    if removed:
        return await message.reply_text(
            f"Removed **{mention}** from {MUSIC_BOT_NAME}'s Approved Users."
        )        
    await message.reply_text(f"Something wrong happened.")


@app.on_message(filters.command("approvedlist") & filters.user(SUDO_USERS))
async def sudoers_list(_, message: Message):
    sudoers = await get_playlist_limit_sudoers()    
    sex = 0    
    smex = 0
    text = ""
    for count, user_id in enumerate(sudoers, 1):
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n⭐️<u> **Approved Users:**</u>\n"
                sex += 1
                text += f"{sex}➤ {user}\n"
            except Exception:
                continue
    if text == "":
        await message.reply_text("No Approved Users")
    else:
        await message.reply_text(text)