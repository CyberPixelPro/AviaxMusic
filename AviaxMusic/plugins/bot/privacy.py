from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode
from AviaxMusic import app
import config

TEXT = f"""
🔒 **Privacy Policy for {app.mention} !**

Your privacy is important to us. To learn more about how we collect, use, and protect your data, please review our Privacy Policy here: [Privacy Policy]({config.PRIVACY_LINK}).

If you have any questions or concerns, feel free to reach out to our [support team](https://t.me/nexgenbotsindia).
"""

@app.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "View Privacy Policy", url=config.SUPPORT_GROUP
                )
            ]
        ]
    )
    await message.reply_text(
        TEXT, 
        reply_markup=keyboard, 
        parse_mode=ParseMode.MARKDOWN, 
        disable_web_page_preview=True
    )
