import winsound
import pyaudio
# import playsound
from pygame import mixer
import vlc
import os
os.add_dll_directory(os.getcwd())
os.add_dll_directory(r'C:\Program Files\VLC')

mixer.init()
mixer.music.load("au/BGmusic.mp3")
mixer.music.play()

input()

rrr = mixer.Sound("au/BGsound.mp3")
pick = mixer.Sound("au/tick.mp3")
#And then use the play method
mixer.set_num_channels(50)

rrr.play()
for i in range(30):
  pick.play()
  input()

#You can also use the methods pause() and stop if you need.
input()
input()
