from pyrogram import filters
from pyrogram.types import Message

from AviaxMusic import app
from AviaxMusic.core.call import Aviax
from AviaxMusic.utils.database import set_loop
from AviaxMusic.utils.decorators import AdminRightsCheck
from AviaxMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if len(message.command) != 1:
        return
    await Aviax.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention),
        reply_markup=close_markup(_)
    )
