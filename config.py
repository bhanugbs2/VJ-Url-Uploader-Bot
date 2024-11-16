# Don't Remove Credit Tg - @HollywoodGbs
# Ask Doubt on telegram @GBS_TECH

import os
import re
from os import environ, getenv

import telebot
import libtorrent as lt
import os
import time
import re
import requests

# Bot initialization
API_TOKEN = "YOUR_BOT_API_TOKEN"
bot = telebot.TeleBot(API_TOKEN)

# Pattern for recognizing magnet links or torrent file URLs
torrent_pattern = re.compile(r"^(magnet:\?xt=urn:btih:|http[s]?://.*\.torrent)$", re.IGNORECASE)

@bot.message_handler(func=lambda message: torrent_pattern.match(message.text))
def handle_torrent_link(message):
    torrent_link = message.text
    bot.reply_to(message, "Torrent link received. Downloading...")

    try:
        # Initiate the torrent download
        download_file = download_torrent(torrent_link)
        bot.reply_to(message, f"Torrent download complete: {download_file}")

        # Upload the file to Telegram
        with open(download_file, 'rb') as file:
            bot.send_document(message.chat.id, file)

    except Exception as e:
        bot.reply_to(message, f"Error occurred while downloading torrent: {str(e)}")

def download_torrent(torrent_link):
    # Initialize the session
    ses = lt.session()

    # Handle magnet link or torrent file URL
    if torrent_link.startswith('magnet:'):
        # Magnet link
        print("Handling Magnet Link...")
        handle = lt.add_magnet(ses, torrent_link)
    else:
        # .torrent file URL
        print("Handling .torrent URL...")
        response = requests.get(torrent_link)
        torrent_data = response.content
        handle = lt.add_torrent(ses, torrent_data)

    # Wait for download to complete
    ses.download_queue = [handle]
    print(f"Downloading: {handle.name()}")

    # Start downloading and print download speed
    while not handle.is_seed():
        print(f"Downloading {handle.name()}... {handle.status().download_rate / 1000} kB/s")
        time.sleep(1)

    # Return the downloaded file path
    downloaded_file = handle.name()
    print(f"Download complete: {downloaded_file}")
    return downloaded_file

if __name__ == "__main__":
    bot.polling()

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_GBS_BOT_TOKEN = os.environ.get("TECH_GBS_BOT_TOKEN", "7340673773:AAEjcW9AcoALQAD-EHAbp_RNeXDjomkgpSQ")
    TECH_GBS_BOT_USERNAME = os.environ.get("TECH_GBS_BOT_USERNAME", "MoviesLinks_bot") # Bot username without @.
    
    # The Telegram API things
    TECH_GBS_API_ID = int(os.environ.get("TECH_GBS_API_ID", "24228078"))
    TECH_GBS_API_HASH = os.environ.get("TECH_GBS_API_HASH", "64ca904789ddfa7d369a6f468d2ded8b")
    
    # the download location, where the HTTP Server runs
    TECH_GBS_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_GBS_MAX_FILE_SIZE = 50000000
    TECH_GBS_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_GBS_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_GBS_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    TECH_GBS_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_GBS_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_GBS_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_GBS_OWNER_ID = int(os.environ.get("TECH_GBS_OWNER_ID", "7236176932")) 
    TECH_GBS_SESSION_NAME = "GBS-URL-UPLOADER-BOT"
    
    # database uri (mongodb)
    TECH_GBS_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://bhanushankargbs1:Y2dSieLNZGs0EgD8@cluster0.ldmnv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    TECH_GBS_MAX_RESULTS = "50"

    # channel information
    TECH_GBS_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "7340673773")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    tech_GBS_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '') # your update channel id and make bot admin in update channel with full right
    TECH_GBS_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_GBS = bool(environ.get('TECH_VJ', True)) # Set False If you want shortlink off else True
    TECH_GBS_URL = environ.get('TECH_VJ_URL', 'moneykamalo.com') # your shortlink url domain or url without https://
    TECH_GBS_API = environ.get('TECH_VJ_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674') # your url shortner api
    TECH_GBS_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://t.me/How_To_Open_Linkl")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
