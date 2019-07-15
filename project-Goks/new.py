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
def speechToText():
    r = sr.Recognizer()
    filename = sr.AudioFile('jj.wav')
    with filename as source:
        audio = r.listen(source)
    s = r.recognize_google(audio)
    return s

t=0
s = speechToText()
try:
    arr = s.split()
    if arr[0] == 'search':
        arr.pop(0)
        for j in search(" ".join(arr), tld="co.in", stop=1, pause=2):
            web.open_new(j)
            page=requests.get(j)
            soup=BeautifulSoup(page.content, 'html.parser')
            for a in soup.findAll('p'):
                if len(a.text)!=0:
                    t=t+1
                    if(t==1):
                        s=a.text

    myobj = gTTS(s, lang='en')
    myobj.save("welcome.mp3")
    pl = vlc.MediaPlayer("welcome.mp3")
    pl.play()
    time.sleep(50)
    s=speechToText()
    #if s=='close':
    os.system("taskkill /im chrome.exe /f")
except Exception:
    print("something went wrong")
