#! /bin/python3



import librosa
import numpy as np
import pygame
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
import playsound
import wikipedia
wikipedia.set_lang("pl")
from random import *
import pywhatkit as kit
#import urllib.request as request
#import re
from pynput.keyboard import Key, Controller
keyboard = Controller()
import psutil
import sys

multiplier = 3.5

pygame.init()
infoObject = pygame.display.Info()
screen_w = int(infoObject.current_w/8)
screen_h = int(infoObject.current_w/8)
# Set up the drawing window
screen = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption('T.R.Y.B.I.K.')
Icon = pygame.image.load('trybik.png')
pygame.display.set_icon(Icon)
screen.fill((49, 78, 11,5))
pygame.display.flip()
def pkill(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()


def clamp(min_value, max_value, value):

    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):

        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)

    def render(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))


def vis(filename):
    
    time_series, sample_rate = librosa.load(filename)  # getting information from the file
    
    # getting a matrix which contains amplitude values according to frequency and time indexes
    stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
    
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  # converting the matrix to decibel matrix
    
    frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies
    
    # getting an array of time periodic
    times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)
    
    time_index_ratio = len(times)/times[len(times) - 1]
    
    frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]
    
    
    def get_decibel(target_time, freq):
        return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]
    
    
    bars = []


    frequencies = np.arange(100, 8000, 100)
    
    r = len(frequencies)
    
    
    width = screen_w/r*multiplier
    
    
    x = (screen_w - width*r)/2
    
    for c in frequencies:
        bars.append(AudioBar(x, (screen_h/(multiplier*2))-100, c, (98, 156, 23), max_height=400, width=width))
        x += width
    
    t = pygame.time.get_ticks()
    getTicksLastFrame = t
    
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)

    while pygame.mixer.music.get_busy():
    
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
    
        # Fill the background with white
        screen.fill((49, 78, 11,5))
    
        for b in bars:
            b.update(deltaTime, get_decibel(pygame.mixer.music.get_pos()/1000.0, b.freq))
            b.render(screen)
    
        # Flip the display
        pygame.display.flip()
    pygame.draw.rect(screen, (49, 78, 11,5), pygame.Rect(0, 0, screen_w, screen_h))
    pygame.display.flip()
    # Done! Time to quit.





powitania = ["Cześć", "Witaj", "Dzień dobry"]
pożegnania = ["Do widzenia", "Pa", "Pa Pa", "Papa", "Do zobaczenia"]
mmts = ["Miło mi to słyszeć!", "Dziękuję"]
#żarty = ['''Kierowca przejechał kurę.
#- Baco to wasza kura?
#- Ni, my takiej chudej nie mieliśmy.''']



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='pl-PL')
        print("User said: %s" % query)

    except Exception as e:
        print(e)
        print("Google was unable to hear")
        return "ERROR"

    return query.lower()

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
    

def komendy(txt):
    if "jak się nazywasz" == txt or "kim jesteś" == txt:
        say("Nazywam się trybik")
        say("Jest to skrót podobny do imienia filmowego jarvisa Aj ron mena")
        say("Oznacza on Tylko Raczej Bardzo Inteligentny Program Komputerowy.")
        say("Y jest dodany, a P wycięte.")
    if "jesteś świetny" == txt or "jesteś super" == txt:
        say(choice(mmts))
    if "cześć" == txt or "cześć trybik" == txt or "witaj" == txt or "witaj trybik" == txt or "dzień dobry" == txt:
        say(choice(powitania))
    if "do widzenia" == txt or "pa" == txt or "papa" == txt or "pa pa" == txt or "do zobaczenia" == txt or "żegnaj" == txt:
        say(choice(pożegnania))
        pygame.quit()
        sys.exit()
    if "wyszukaj w wikipedii" in txt:
        say("Wyszukuję w wikipedii hasło: %s" % txt.split("wyszukaj w wikipedii",1)[1])
        print(txt.split("wyszukaj w wikipedii",1)[1])
        say(wikipedia.summary((txt.split("wyszukaj w wikipedii",1)[1]), sentences = 3))
    if "co to jest" in txt:
        say("Wyszukuję w wikipedii hasło: %s" % txt.split("co to jest",1)[1])
        print(txt.split("co to jest",1)[1])
        say(wikipedia.summary((txt.split("co to jest",1)[1]), sentences = 3))
    elif "co to" in txt:
        say("Wyszukuję w wikipedii hasło: %s" % txt.split("co to",1)[1])
        print(txt.split("co to",1)[1])
        say(wikipedia.summary((txt.split("co to",1)[1]), sentences = 3))
    if "youtube" in txt:
        #say("Wyszukuję w wikipedii hasło: %s" % txt.split("co to jest",1)[1])
        #print(txt.split("co to jest",1)[1])
        kit.playonyt(txt.split("youtube",1)[1])
    if "wyszukaj" in txt:
        say("Wyszukuję hasło: %s" % txt.split("wyszukaj",1)[1])
        print(txt.split("wyszukaj",1)[1])
        kit.search(txt.split("wyszukaj",1)[1])
    #if "opowiedz mi żart" == txt or "opowiedz mi kawał" == txt:
    #    żart = choice(żarty)
    #    print(żart)
    #    say(żart)
    #if "youtube" in txt:
    #    html = request.urlopen("https://www.youtube.com/results?search_query=%s" % txt.split("youtube",1)[1])
    #    #say("Wyszukuję w wikipedii hasło: %s" % txt.split("co to jest",1)[1])
    #    #print(txt.split("co to jest",1)[1])
    #    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #    print("https://www.youtube.com/watch?v=" + video_ids[0])

say("Cześć")

while 1:
    tekst = takeCommand()
    if tekst != "ERROR":
        komendy(tekst)
    else:
        say("BŁĄD")
