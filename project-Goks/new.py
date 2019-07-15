import speech_recognition as sr
from googlesearch import search
import os
import webbrowser as web
import sys
from bs4 import BeautifulSoup
from gtts import gTTS
import requests
import vlc
import time


def speechToText(chioce):
    if chioce == 0:
        au = 'jj.wav'
    if chioce == 1:
        au = 'close.wav'  #kindly make this and use
    r = sr.Recognizer()
    filename = sr.AudioFile(au)
    with filename as source:
        audio = r.listen(source)
    s = r.recognize_google(audio)
    return s


t = 0
s = speechToText(0)
try:
    arr = s.split()
    if arr[0] == 'search':
        arr.pop(0)
        for j in search(" ".join(arr), tld="co.in", stop=1, pause=2):
            web.open_new(j)
            page = requests.get(j)
            soup = BeautifulSoup(page.content, 'html.parser')
            for a in soup.findAll('p'):
                if len(a.text) != 0:
                    t = t + 1
                    if (t == 1):
                        s = a.text

    myobj = gTTS(s, lang='en')
    myobj.save("welcome.mp3")
    pl = vlc.MediaPlayer("welcome.mp3")
    pl.play()
    time.sleep(50)
    s = speechToText(1)
    if s == 'close':
        os.system("taskkill /im chrome.exe /f")
except Exception:
    print("something went wrong")

#next task => is to say information in one line eg:- weather == 39 deg or gold price == 3000 etc.,