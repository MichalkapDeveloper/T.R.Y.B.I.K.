from todo import *
from tts import say
import wikipedia
wikipedia.set_lang("pl")
import pywhatkit as kit
import sys
import pygame
from random import *
import os
import time
from datetime import date
import recognizer as rec

powitania = ["Cześć", "Witaj", "Dzień dobry"]
pożegnania = ["Do widzenia", "Pa", "Pa Pa", "Papa", "Do zobaczenia"]
mmts = ["Miło mi to słyszeć!", "Dziękuję"]
#żarty = ['''Kierowca przejechał kurę.
#- Baco to wasza kura?
#- Ni, my takiej chudej nie mieliśmy.''']

def komendy(txt):
    txt = txt.lower()
    # Opowiadanie o sobie
    if "jak się nazywasz" == txt or "kim jesteś" == txt:
        say("Nazywam się trybik")
        say("Jest to skrót podobny do imienia filmowego jarvisa Aj ron mena")
        say("Oznacza on Tylko Raczej Bardzo Inteligentny Program Komputerowy.")
        say("Y jest dodany, a P wycięte.")

    # Pochwały
    if "jesteś świetny" == txt or "jesteś super" == txt:
        say(choice(mmts))

    # Powitania
    if "cześć" == txt or "cześć trybik" == txt or "witaj" == txt or "witaj trybik" == txt or "dzień dobry" == txt:
        say(choice(powitania))

    # Pożegnania
    if "do widzenia" == txt or "pa" == txt or "papa" == txt or "pa pa" == txt or "do zobaczenia" == txt or "żegnaj" == txt:
        say(choice(pożegnania))
        pygame.quit()
        sys.exit()

    # Wyszukiwanie w wikipedii
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

    # Wyszukiwanie w YouTube
    if "youtube" in txt:
        say("Wyszukuję w YouTube hasło: %s" % txt.split("youtube",1)[1])
        print(txt.split("youtube",1)[1])
        kit.playonyt(txt.split("youtube",1)[1])

    # Wyszukiwanie w domyślnej przeglądarce
    if "wyszukaj" in txt:
        say("Wyszukuję hasło: %s" % txt.split("wyszukaj",1)[1])
        print(txt.split("wyszukaj",1)[1])
        kit.search(txt.split("wyszukaj",1)[1])

    # Godzina
    if "która godzina" == txt:
        godzina = time.strftime("%H:%M:%S", time.localtime())
        print(godzina)
        say(godzina)
    # Dzień
    if "który jest dzisiaj" == txt or "którego dzisiaj mamy" == txt:
        data = str(date.today().strftime("%d/%m/%Y"))
        print(data)
        say(data)

    # Todo add
    if "dodaj" in txt and "do listy" in txt:
        if "dodaj do listy" in txt:
            dod = txt.split("dodaj do listy ",1)[1]
            say("Dodaję do listy %s" % dod)
            add(dod)
            print(todo)
        else:
            dod = txt.split("dodaj ",1)[1]
            dod = dod.rsplit(" do listy", 1)
            dod = dod[0]
            say("Dodaję do listy %s" % dod)
            add(dod)
            print(todo)
    
    # Todo remove
    if "usuń" in txt and "z listy" in txt and "wszystko" not in txt:
        if "usuń z listy" in txt:
            us = txt.split("usuń z listy ",1)[1]
            say("Usuwam z listy %s" % us)
            re = remove(us)
            say(re)
            print(todo)
        else:
            us = txt.split("usuń ",1)[1]
            us = us.rsplit(" z listy", 1)
            us = us[0]
            say("Usuwam z listy %s" % us)
            re = remove(us)
            say(re)
            print(todo)

    # Todo say
    if "co mam zrobić" == txt or "co mam dzisiaj zrobić" == txt or "pokaż listę" == txt or "pokaż listę zadań" == txt or "pokaż listę obowiązków" == txt:
        say(list())

    # Todo del all
    #if "usuń wszystko z listy" == txt or "wyczyść listę" == txt or "wyczyść liste" == txt:
    #    say("Czy na pewno chcesz to zrobić?")
    #    txt = rec.takeCommand()
    #    txt = txt.lower()
    #    if "tak" == txt or "tak na pewno" == txt:
    #        re = delall()
    #        say(re)
    
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
