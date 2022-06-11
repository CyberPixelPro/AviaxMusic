from itertools import count
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from YukkiMusic import app
from YukkiMusic.misc import SUDO_USERS as SUDOERS
from YukkiMusic.plugins.techzbots.database.limitsdb import add_to_approved_user, remove_approved_user, get_approved_users, is_approved
from YukkiMusic.utils.decorators.language import language

@app.on_message(
    filters.command("approve") & filters.user(SUDOERS)
)
@language
async def userapprove(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, You can't manage sudo users when you're using Yukki's Database.\n\n Please fill your MONGO_DB_URI in your vars to use this feature**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("💠 Give me username of the user...")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if await is_approved(user.id):
            return await message.reply_text(
                "{} is already approved".format(user.mention)
            )
        added = await add_to_approved_user(user.id)
        if added:            
            await message.reply_text("Added **{0}** to Approved Users.".format(user.mention))
        else:
            await message.reply_text("Failed")
        return
    if await is_approved(message.reply_to_message.from_user.id):
        return await message.reply_text(
            "{} is already approved".format(
                message.reply_to_message.from_user.mention
            )
        )
    added = await add_to_approved_user(message.reply_to_message.from_user.id)
    if added:
        await message.reply_text(
            "Added **{0}** to Approved Users".format(
                message.reply_to_message.from_user.mention
            )
        )
    else:
        await message.reply_text("Failed")
    return


@app.on_message(
    filters.command("unapprove") & filters.user(SUDOERS)
)
@language
async def userunapprove(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, You can't manage sudo users when you're using Yukki's Database.\n\n Please fill your MONGO_DB_URI in your vars to use this feature**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("💠 Give me username of the user...")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if await is_approved(user.id):
            return await message.reply_text("{} is not approved".format(
                message.from_user.mention
            ))
        removed = await remove_approved_user(user.id)
        if removed:
            await message.reply_text("Removed **{0}** to From Approved Users".format(
                message.from_user.mention
            ))
            return
        await message.reply_text(f"Something wrong happened.")
        return
    user_id = message.reply_to_message.from_user.id
    if await is_approved(user_id):
        return await message.reply_text("{} is not approved".format(
                message.reply_to_message.from_user.mention
            ))
    removed = await remove_approved_user(user_id)
    if removed:
        await message.reply_text("Removed **{0}** to From Approved Users".format(
                message.reply_to_message.from_user.mention
            ))
        return
    await message.reply_text(f"Something wrong happened.")


@app.on_message(filters.command("approved") & filters.user(SUDOERS))
@language
async def approved_list(client, message: Message, _):
    count = 0
    smex = 0
    text = ""
    for user_id in await get_approved_users():
        if 1 == 1:
            try:
                user = await app.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if smex == 0:
                    smex += 1
                    text += "\n⭐️<u> **Approved Users:**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("No Approved Users")
    else:
        await message.reply_text(text)