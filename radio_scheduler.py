import os
from datetime import datetime
import time

def play_music(playlist):
    os.system("cvlc --no-dbus --no-globalhotkeys --intf dummy --alsa-audio-device default --file-caching=1000 {playlist}*.mp3")

morning_start = "06:00"
morning_end = "08:00"
evening_start = "16:00"
evening_end = "19:00"

morning_playlist = "/home/pi/music/morning/"
evening_playlist = "/home/pi/music/evening/"

while True:
    current_time = datetime.now().strftime("%H:%M")
    if morning_start <= current_time < morning_end:
        play_music(morning_playlist)
    elif evening_start <= current_time < evening_end:
        play_music(evening_playlist)
    time.sleep(60)
