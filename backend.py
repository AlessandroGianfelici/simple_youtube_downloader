import sys
import time
import telepot
import os, sys
from bot_token import bot_token
import validators
from pytube import YouTube

APP_PATH = os.path.dirname(os.path.abspath(__file__))


def handle(msg):
    chat_id = msg['chat']['id']
    if 'text' in msg.keys() and validators.url(link := msg['text']) and 'youtube' in msg['text'].lower().replace(".", ""):
        my_video = YouTube(link)
        best_stream = sorted(filter(lambda x : ('mp' in x.mime_type), 
                            my_video.streams.filter(only_audio=True)), 
                     key=lambda x : x.abr)[0].download(APP_PATH)
        print(f"File scaricato al percorso {best_stream}")
        bot.sendDocument(chat_id, open(best_stream, 'rb'))
    else:
        return None

bot = telepot.Bot(bot_token)
bot.message_loop(handle)

while(1):
    time.sleep(1)