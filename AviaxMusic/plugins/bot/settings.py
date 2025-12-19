from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from AviaxMusic import app
from AviaxMusic.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
)
from AviaxMusic.utils import bot_sys_stats
from AviaxMusic.utils.decorators.admins import ActualAdminCB
from AviaxMusic.utils.decorators.language import language, languageCB
from AviaxMusic.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from AviaxMusic.utils.inline.start import private_panel
from config import BANNED_USERS, OWNER_ID

async def answer_callback(query: CallbackQuery, text: str, alert: bool = False):
    try:
        await query.answer(text, show_alert=alert)
    except:
        pass

@app.on_message(
    filters.command(["settings", "setting"]) & filters.group & ~BANNED_USERS
)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(app.mention, message.chat.id, message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_callback_query(filters.regex("settings_helper") & ~BANNED_USERS)
@languageCB
async def settings_cb(client, CallbackQuery, _):
    await answer_callback(CallbackQuery, _["set_cb_5"])
    buttons = setting_markup(_)   
    try:
        await CallbackQuery.edit_message_text(
            _["setting_1"].format(
                app.mention,
                CallbackQuery.message.chat.id,
                CallbackQuery.message.chat.title,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        pass

@app.on_callback_query(filters.regex("settingsback_helper") & ~BANNED_USERS)
@languageCB
async def settings_back_markup(client, CallbackQuery: CallbackQuery, _):
    await answer_callback(CallbackQuery, "")
    
    if CallbackQuery.message.chat.type == ChatType.PRIVATE:
        buttons = private_panel(_)
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await CallbackQuery.edit_message_text(
            _["start_2"].format(CallbackQuery.from_user.mention, app.mention, UP, DISK, CPU, RAM),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = setting_markup(_)
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )

@app.on_callback_query(
    filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def handle_setting_info(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        return await answer_callback(CallbackQuery, _["setting_2"], alert=True)    
    if command == "PLAYMODEANSWER":
        return await answer_callback(CallbackQuery, _["setting_5"], alert=True)    
    if command == "PLAYTYPEANSWER":
        return await answer_callback(CallbackQuery, _["setting_6"], alert=True)    
    if command == "AUTHANSWER":
        return await answer_callback(CallbackQuery, _["setting_3"], alert=True)    
    if command == "VOTEANSWER":
        return await answer_callback(CallbackQuery, _["setting_8"], alert=True)    
    if command == "ANSWERVOMODE":
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        return await answer_callback(CallbackQuery, _["setting_9"].format(current), alert=True)
    if command == "PM":
        await answer_callback(CallbackQuery, _["set_cb_2"], alert=True)    
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        playtype = await get_playtype(CallbackQuery.message.chat.id)
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        direct_state = True if playmode == "Direct" else None
        group_state = True if not is_non_admin else None
        playtype_state = None if playtype == "Everyone" else True      
        buttons = playmode_users_markup(_, direct_state, group_state, playtype_state)
    elif command == "AU":
        await answer_callback(CallbackQuery, _["set_cb_1"], alert=True)   
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        auth_state = True if not is_non_admin else None       
        buttons = auth_users_markup(_, auth_state)
    elif command == "VM":
        mode = await is_skipmode(CallbackQuery.message.chat.id)
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        buttons = vote_mode_markup(_, current, mode)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return

@app.on_callback_query(filters.regex("FERRARIUDTI") & ~BANNED_USERS)
@ActualAdminCB
async def handle_vote_count_change(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    mode = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    if not await is_skipmode(chat_id):
        return await answer_callback(CallbackQuery, _["setting_10"], alert=True)
    current = await get_upvote_count(chat_id)
    if mode == "M":
        final = current - 2
        if final == 0:
            return await answer_callback(CallbackQuery, _["setting_11"], alert=True)
        if final <= 2:
            final = 2
    else:
        final = current + 2
        if final == 17:
            return await answer_callback(CallbackQuery, _["setting_12"], alert=True)
        if final >= 15:
            final = 15
    await set_upvotes(chat_id, final)
    buttons = vote_mode_markup(_, final, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return
        
@app.on_callback_query(
    filters.regex(pattern=r"^(MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def handle_playmode_change(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(chat_id)
        if not is_non_admin:
            await add_nonadmin_chat(chat_id)
        else:
            await remove_nonadmin_chat(chat_id)
    elif command == "MODECHANGE":
        await answer_callback(CallbackQuery, _["set_cb_3"], alert=True)
        playmode = await get_playmode(chat_id)
        if playmode == "Direct":
            await set_playmode(chat_id, "Inline")
        else:
            await set_playmode(chat_id, "Direct")
    elif command == "PLAYTYPECHANGE":
        await answer_callback(CallbackQuery, _["set_cb_3"], alert=True)
        playtype = await get_playtype(chat_id)
        if playtype == "Everyone":
            await set_playtype(chat_id, "Admin")
        else:
            await set_playtype(chat_id, "Everyone")
    playmode = await get_playmode(chat_id)
    playtype = await get_playtype(chat_id)
    is_non_admin = await is_nonadmin_chat(chat_id)
    direct_state = True if playmode == "Direct" else None
    group_state = True if not is_non_admin else None
    playtype_state = None if playtype == "Everyone" else True
    buttons = playmode_users_markup(_, direct_state, group_state, playtype_state)   
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return

@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS)
@ActualAdminCB
async def handle_auth_list(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "AUTHLIST":
        auth_users = await get_authuser_names(chat_id)      
        if not auth_users:
            return await answer_callback(CallbackQuery, _["setting_4"], alert=True)     
        await answer_callback(CallbackQuery, _["set_cb_4"], alert=True)        
        await CallbackQuery.edit_message_text(_["auth_6"])
        msg = _["auth_7"].format(CallbackQuery.message.chat.title)        
        count = 0
        for token in auth_users:
            data = await get_authuser(chat_id, token)
            try:
                user_info = await app.get_users(data["auth_user_id"])
                user_name = user_info.first_name
                count += 1
                msg += f"{count}➤ {user_name}[<code>{data['auth_user_id']}</code>]\n"
                msg += f"   {_['auth_8']} {data['admin_name']}[<code>{data['admin_id']}</code>]\n\n"
            except:
                continue
        buttons = [
            [
                InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="AU"),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
            ]
        ]        
        try:
            return await CallbackQuery.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(buttons))
        except MessageNotModified:
            return
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(chat_id)
        if not is_non_admin:
            await add_nonadmin_chat(chat_id)
            auth_state = None
        else:
            await remove_nonadmin_chat(chat_id)
            auth_state = True            
        await answer_callback(CallbackQuery, _["set_cb_3"], alert=True)        
        buttons = auth_users_markup(_, auth_state)
        try:
            return await CallbackQuery.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except MessageNotModified:
            return

@app.on_callback_query(filters.regex("VOMODECHANGE") & ~BANNED_USERS)
@ActualAdminCB
async def handle_vote_toggle(client, CallbackQuery, _):
    await answer_callback(CallbackQuery, _["set_cb_3"], alert=True)    
    chat_id = CallbackQuery.message.chat.id    
    if await is_skipmode(chat_id):
        await skip_off(chat_id)
        is_enabled = None
    else:
        await skip_on(chat_id)
        is_enabled = True        
    current = await get_upvote_count(chat_id)
    buttons = vote_mode_markup(_, current, is_enabled)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return
