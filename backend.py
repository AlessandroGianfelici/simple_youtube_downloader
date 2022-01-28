import sys
import time
import telepot
import os, sys
from bot_token import bot_token
import validators
import logging
from pytube import YouTube

APP_PATH = os.path.dirname(os.path.abspath(__file__))


def handle(msg):
    chat_id = msg['chat']['id']
    print(msg)
    if 'text' in msg.keys() and validators.url(link := msg['text']):
        my_video = YouTube(link)
        best_stream = sorted(filter(lambda x : ('mp' in x.mime_type), 
                            my_video.streams.filter(only_audio=True)), 
                     key=lambda x : x.abr)[0].download(APP_PATH)
        logger.info(f"File scaricato al percorso {best_stream}")
    else:
        bot.sendMessage(chat_id, f"Mandami un link youtube valido!")
    return None

if __name__ == '__main__':
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S%p")
    logger = logging.getLogger(__name__)

    bot = telepot.Bot(bot_token)
    bot.message_loop(handle)

    while(1):
        time.sleep(1)