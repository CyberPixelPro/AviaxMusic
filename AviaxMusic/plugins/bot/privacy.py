from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app

@app.on_message(filters.command("privacy"))
async def privacy(_, message):
    babes = f"""
    ✨ Welcome to {app.mention}! Your privacy is important to us.

    **• Information Collection and Use:**

    - **User IDs and Chat IDs:** Collected and stored solely for maintaining our database and providing services.
    - **Non-Sensitive Data:** No collection or storage of personal messages, media files, or PII.
    - **Bot Role:** Automated bot account that cannot read or store group chats.
    - **Limited Access:** Neither the bot nor the owner can access group chat content.

    **• Key Points:**

    - Reasonable measures to protect collected data.
    - No sharing or selling of collected data.
    - Right to request access, deletion, or correction of data.
    - For questions, contact us at @NexGenSpam.

    By using {app.mention}, you acknowledge that you have read and understood this Privacy Policy.
    """

    await message.reply_text(
        text=babes,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• More info •", url="https://telegra.ph/Privacy-Policy-for-Aviax-Music-08-11")]]
        )
    )
