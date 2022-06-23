#! /bin/python3

from recognizer import *
from commands import *

while 1:
    tekst = takeCommand()
    if tekst != "ERROR":
        komendy(tekst)
    else:
        say("BŁĄD")