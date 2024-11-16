
import telebot
import libtorrent as lt
import os
import time
import requests
import re

# Bot initialization
API_TOKEN = "YOUR_BOT_API_TOKEN"  # Replace with your actual bot token
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

        # Optionally remove the file after sending it to the user
        os.remove(download_file)

    except Exception as e:
        bot.reply_to(message, f"Error occurred while downloading torrent: {str(e)}")

def download_torrent(torrent_link):
    # Initialize the session for torrent download
    ses = lt.session()

    # Handle magnet link or .torrent file URL
    if torrent_link.startswith('magnet:'):
        print("Handling Magnet Link...")
        handle = lt.add_magnet(ses, torrent_link)
    else:
        print("Handling .torrent URL...")
        response = requests.get(torrent_link)
        torrent_data = response.content
        handle = lt.add_torrent(ses, torrent_data)

    # Set download path (you can customize this to suit your needs)
    download_path = "./downloads"
    os.makedirs(download_path, exist_ok=True)
    handle.set_download_path(download_path)

    # Start downloading and print download progress
    print(f"Downloading: {handle.name()}")
    while not handle.is_seed():
        print(f"Downloading {handle.name()}... {handle.status().download_rate / 1000:.1f} kB/s")
        time.sleep(1)

    # Return the downloaded file path
    downloaded_file = os.path.join(download_path, handle.name())
    print(f"Download complete: {downloaded_file}")
    return downloaded_file

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)
