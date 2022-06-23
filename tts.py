from visualizer import *
from gtts import gTTS
import os

def say(text):
    tts = gTTS(text=text, lang='pl')
    filename = "temp.mp3"
    tts.save(filename)
    vis(filename)
    os.remove(filename)
    #keyboard.press(Key.alt_l)
    #keyboard.press(Key.f4)
    #keyboard.release(Key.alt_l)
    #keyboard.release(Key.f4)
