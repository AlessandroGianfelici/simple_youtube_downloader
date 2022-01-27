from pytube import YouTube
import os

APP_PATH = os.path.dirname(os.path.abspath(__file__))

link = "https://www.youtube.com/watch?v=odgkCMPAsig"
my_video = YouTube(link)
best_stream = sorted(filter(lambda x : ('mp' in x.mime_type), 
                            my_video.streams.filter(only_audio=True)), 
                     key=lambda x : x.abr)[0].download(APP_PATH)