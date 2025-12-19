from pyrogram import filters
from pyrogram.types import Message

from AviaxMusic import app
from AviaxMusic.utils.database import get_loop, set_loop
from AviaxMusic.utils.decorators import AdminRightsCheck
from AviaxMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def loop_command(cli, message: Message, _, chat_id):
    usage = _["admin_17"]  
    if len(message.command) != 2:
        return await message.reply_text(usage)
    user_input = message.text.split(None, 1)[1].strip()
    if user_input.isnumeric():
        requested_loop = int(user_input)
        if 1 <= requested_loop <= 10:
            current_loop = await get_loop(chat_id)
            if current_loop != 0:
                new_loop_count = current_loop + requested_loop
            else:
                new_loop_count = requested_loop
            if new_loop_count > 10:
                new_loop_count = 10
            await set_loop(chat_id, new_loop_count)
            return await message.reply_text(
                text=_["admin_18"].format(new_loop_count, message.from_user.mention),
                reply_markup=close_markup(_),
            )
        else:
            return await message.reply_text(_["admin_17"])

    elif user_input.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            text=_["admin_18"].format(10, message.from_user.mention),
            reply_markup=close_markup(_),
        )
    elif user_input.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(
            _["admin_19"].format(message.from_user.mention),
            reply_markup=close_markup(_),
        )
    else:
        return await message.reply_text(usage)
