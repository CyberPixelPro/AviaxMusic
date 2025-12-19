from pyrogram import filters
from pyrogram.types import Message

from AviaxMusic import app
from AviaxMusic.utils import extract_user, int_to_alpha
from AviaxMusic.utils.database import (
    delete_authuser,
    get_authuser,
    get_authuser_names,
    save_authuser,
)
from AviaxMusic.utils.decorators import AdminActual, language
from AviaxMusic.utils.inline import close_markup
from config import BANNED_USERS, adminlist
AUTH_LIMIT = 25


@app.on_message(filters.command("auth") & filters.group & ~BANNED_USERS)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    
    auth_users = await get_authuser_names(message.chat.id)
    if len(auth_users) >= AUTH_LIMIT:
        return await message.reply_text(_["auth_1"])
    
    if token in auth_users:
        return await message.reply_text(_["auth_3"].format(user.mention))

    auth_data = {
        "auth_user_id": user.id,
        "auth_name": user.first_name,
        "admin_id": message.from_user.id,
        "admin_name": message.from_user.first_name,
    }
    await save_authuser(message.chat.id, token, auth_data)

    admin_cache = adminlist.get(message.chat.id)
    if admin_cache:
        if user.id not in admin_cache:
            admin_cache.append(user.id)

    return await message.reply_text(_["auth_2"].format(user.mention))


@app.on_message(filters.command("unauth") & filters.group & ~BANNED_USERS)
@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)
    token = await int_to_alpha(user.id)

    deleted = await delete_authuser(message.chat.id, token)

    admin_cache = adminlist.get(message.chat.id)
    if admin_cache:
        if user.id in admin_cache:
            admin_cache.remove(user.id)

    if deleted:
        return await message.reply_text(_["auth_4"].format(user.mention))
    else:
        return await message.reply_text(_["auth_5"].format(user.mention))


@app.on_message(
    filters.command(["authlist", "authusers"]) & filters.group & ~BANNED_USERS
)
@language
async def authusers(client, message: Message, _):
    auth_users_list = await get_authuser_names(message.chat.id)
    
    if not auth_users_list:
        return await message.reply_text(_["setting_4"])

    mystic = await message.reply_text(_["auth_6"])
    text = _["auth_7"].format(message.chat.title)
    
    count = 0
    for token in auth_users_list:
        auth_data = await get_authuser(message.chat.id, token)
        
        user_id = auth_data["auth_user_id"]
        admin_id = auth_data["admin_id"]
        admin_name = auth_data["admin_name"]

        try:
            user_info = await app.get_users(user_id)
            user_name = user_info.first_name
            count += 1
        except Exception:
            continue

        text += f"{count}➤ {user_name} [<code>{user_id}</code>]\n"
        text += f"   {_['auth_8']} {admin_name} [<code>{admin_id}</code>]\n\n"

    await mystic.edit_text(text, reply_markup=close_markup(_))