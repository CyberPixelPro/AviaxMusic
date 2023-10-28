from AviaxMusic.core.bot import Aviax
from AviaxMusic.core.dir import dirr
from AviaxMusic.core.git import git
from AviaxMusic.core.userbot import Userbot
from AviaxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
