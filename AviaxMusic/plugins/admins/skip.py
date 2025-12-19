from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from AviaxMusic import YouTube, app
from AviaxMusic.core.call import Aviax
from AviaxMusic.misc import db
from AviaxMusic.utils.database import get_loop
from AviaxMusic.utils.decorators import AdminRightsCheck
from AviaxMusic.utils.inline import close_markup, stream_markup
from AviaxMusic.utils.stream.autoclear import auto_clean
from AviaxMusic.utils.thumbnails import gen_thumb
from config import BANNED_USERS


@app.on_message(
    filters.command(["skip", "cskip", "next", "cnext"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    loop = await get_loop(chat_id)
    if loop != 0:
        return await message.reply_text(_["admin_8"])
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    queue_len = len(check)
    if len(message.command) > 1:
        query = message.text.split(None, 1)[1].strip()
        if not query.isnumeric():
            return await message.reply_text(_["admin_9"])
        skip_count = int(query)
        skippable_tracks = queue_len - 1
        if queue_len > 2:
            if 1 <= skip_count <= skippable_tracks:
                for count in range(skip_count):
                    if not check: break
                    popped = check.pop(0)
                    if popped:
                        await auto_clean(popped)
                if not check:
                    await message.reply_text(
                        text=_["admin_6"].format(
                            message.from_user.mention, message.chat.title
                        ),
                        reply_markup=close_markup(_),
                    )
                    try:
                        return await Aviax.stop_stream(chat_id)
                    except:
                        return
            else:
                return await message.reply_text(_["admin_11"].format(skippable_tracks))
        else:
            return await message.reply_text(_["admin_10"])
    else:
        popped = check.pop(0)
        if popped:
            await auto_clean(popped)
        if not check:
            await message.reply_text(
                text=_["admin_6"].format(
                    message.from_user.mention, message.chat.title
                ),
                reply_markup=close_markup(_),
            )
            try:
                return await Aviax.stop_stream(chat_id)
            except:
                return
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None
    db[chat_id][0]["played"] = 0
    if "old_dur" in check[0]:
        db[chat_id][0]["dur"] = check[0]["old_dur"]
        db[chat_id][0]["seconds"] = check[0]["old_second"]
        db[chat_id][0]["speed_path"] = None
        db[chat_id][0]["speed"] = 1.0
    try:
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await message.reply_text(_["admin_7"].format(title))
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            try:
                await Aviax.skip_stream(chat_id, link, video=status, image=image)
            except:
                return await message.reply_text(_["call_6"])
            await send_now_playing(message, videoid, title, check[0]["dur"], user, _, chat_id, "tg")

        elif "vid_" in queued:
            mystic = await message.reply_text(_["call_7"], disable_web_page_preview=True)
            try:
                file_path, direct = await YouTube.download(
                    videoid, mystic, videoid=True, video=status
                )
            except:
                return await mystic.edit_text(_["call_6"])
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            try:
                await Aviax.skip_stream(chat_id, file_path, video=status, image=image)
            except:
                return await mystic.edit_text(_["call_6"])
            await mystic.delete()
            await send_now_playing(message, videoid, title, check[0]["dur"], user, _, chat_id, "stream")

        elif "index_" in queued:
            try:
                await Aviax.skip_stream(chat_id, videoid, video=status)
            except:
                return await message.reply_text(_["call_6"])
            button = stream_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.STREAM_IMG_URL,
                caption=_["stream_2"].format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"

        else:
            if videoid == "telegram":
                image = None
            elif videoid == "soundcloud":
                image = None
            else:
                try:
                    image = await YouTube.thumbnail(videoid, True)
                except:
                    image = None
            try:
                await Aviax.skip_stream(chat_id, queued, video=status, image=image)
            except:
                return await message.reply_text(_["call_6"])
            
            if videoid == "telegram":
                await send_custom_ui(message, config.TELEGRAM_AUDIO_URL, config.TELEGRAM_VIDEO_URL, streamtype, config.SUPPORT_GROUP, title, check[0]["dur"], user, _, chat_id)
            elif videoid == "soundcloud":
                await send_custom_ui(message, config.SOUNCLOUD_IMG_URL, config.TELEGRAM_VIDEO_URL, streamtype, config.SUPPORT_GROUP, title, check[0]["dur"], user, _, chat_id)
            else:
                await send_now_playing(message, videoid, title, check[0]["dur"], user, _, chat_id, "stream")
    except Exception:
        return await message.reply_text(_["call_6"])

async def send_now_playing(message, videoid, title, duration, user, _, chat_id, markup_type):
    button = stream_markup(_, chat_id)
    img = await gen_thumb(videoid)
    run = await message.reply_photo(
        photo=img,
        caption=_["stream_1"].format(
            f"https://t.me/{app.username}?start=info_{videoid}",
            title[:23],
            duration,
            user,
        ),
        reply_markup=InlineKeyboardMarkup(button),
    )
    db[chat_id][0]["mystic"] = run
    db[chat_id][0]["markup"] = markup_type

async def send_custom_ui(message, audio_img, video_img, streamtype, link, title, duration, user, _, chat_id):
    button = stream_markup(_, chat_id)
    photo = audio_img if str(streamtype) == "audio" else video_img
    run = await message.reply_photo(
        photo=photo,
        caption=_["stream_1"].format(
            link, title[:23], duration, user
        ),
        reply_markup=InlineKeyboardMarkup(button),
    )
    db[chat_id][0]["mystic"] = run
    db[chat_id][0]["markup"] = "tg"