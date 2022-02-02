from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
✨ **Hello MENTION !**

**You can use [{BOT_NAME}](https://t.me/{BOT_USERNAME}) to play Music or Videos in your Group Video Chat.**

💡 **Find out all the Bot's commands and how they work by clicking on the ➤ 📚 Commands button**
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 Advanced Commands", callback_data="commands"
            ),
            InlineKeyboardButton(
                text="🔧 Settings", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📣 Updates Channel", url="https://t.me/TechZBots"
            ),
            InlineKeyboardButton(
                text="💬 Support Group", url="https://t.me/TechZBots_Support"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Add me to Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   InlineKeyboardButton(
                text="🔍 Basic Commands", callback_data="basic_cmd"
            ),  
            InlineKeyboardButton(
                text="📚 Advanced Commands", callback_data="commands"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="📣 Updates Channel", url="https://t.me/TechZBots"
            ),
            InlineKeyboardButton(
                text="💬 Support Group", url="https://t.me/TechZBots_Support"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Commands", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="start_menu_back"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="back_btn"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_TEXT = f"""
Here is the help for **Admin Commands:**


--**ADMIN ONLY COMMANDS WITH MANAGE VC RIGHT:**--

/pause 
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.


--**Authorised Users List:**--

**{BOT_NAME} has a additional feature for non-admin users who want to use admin commands**
- Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.


/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.

/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.

/authusers 
- Check AUTH LIST of the group.
"""

BOT_TEXT = """
Here is the help for **Bot Commands:**


/start 
- Start the Yukki Music Bot.

/help 
- Get Commands Helper Menu with detailed explanations of commands.

/settings 
- Get Settings dashboard of a group. You can manage Auth Users Mode. Commands Mode from here.

/ping
- Ping the Bot and check Ram, Cpu etc stats of Yukki."""

PLAY_TEXT = """
Here is the help for **Play Commands:**

**Note:** Yukki Music Bot works on a single merged commands for Music and Video

--**Youtube and Telegram Files:**--

/play __[Music Name]__(Yukki will search on Youtube)
/play __[Youtube Track link or Playlist]__
/play __[Video, Live, M3U8 Links]__
/play __[Reply to a Audio or Video File]__
- Stream Video or Music on Voice Chat by selecting inline Buttons you get


--**Playlists:**--

/playplaylist 
- Start playing Your Saved Playlist.

/playlist 
- Check Your Saved Playlist On Servers.

/delmyplaylist
- Delete any saved music in your playlist

/delgroupplaylist
- Delete any saved music in your group's playlist [Requires Admin Rights.]
"""

SUDO_TEXT = """
Here is the help for **Play Commands:**

**Note:** Only for sudo users.


/leavebot (group id) -> Order bot to leave a chat

/sudolist -> Show the sudo member list

/addsudo (owner only) - Add user to the sudo list

/delsudo (owner only) - Remove user from sudo list

/eval or /sh -> Dev Commands

/stats -> Show the bot statistic

/clean -> Clears temp(s) files.

/restart -> Restart Bot.

/gban -> Globally banned a user from all served chat and from using bot

/ungban -> Unblock User who is blocked from using.

/speedtest -> Test download / upload speed of bot.

/update -> Update Bot.

/broadcast -> Broadcast a message in all the served chats

/broadcast_pin -> Broadcast a message with pin in all the served chats

/maintenance [enable & disable] -> Turn on / off maintenance mode
"""

EXTRA_TEXT = """
Here is the help for **Extra Commands:**


/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of Yukki Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via Yukki.

/queue
- Check Queue List of Music.
"""

BASIC_TEXT = """
💠 **Basic Commands:**

/start - start the bot
/help - get help message
/play - play songs or videos in vc
/mplay - play songs directly in vc
/vplay - play videos directly in vc
/lyrics - get lyrics of song
/ping - ping the bot
/playlist - play your playlist
/song - download a song as music or video
/settings - settings of the group
/theme - set theme for your group
/queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="start_menu_back"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)