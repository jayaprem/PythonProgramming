import speech_recognition as sr
from googlesearch import search
import os
import webbrowser as web
import sys


def speechToText():
    r = sr.Recognizer()
    filename = sr.AudioFile('Modi.wav')
    with filename as source:
        audio = r.listen(source)
    s = r.recognize_google(audio)
    return s


s = speechToText()
try:
    arr = s.split()
    if arr[0] == 'search':
        arr.pop(0)
        for j in search(" ".join(arr), tld="co.in", stop=2, pause=2):
            web.open_new_tab(j)
            audio = speechToText()
            s = speechToText()
            if s == 'close':
                os.system("taskkill /im chrome.exe /f")
            else:
                print('esrtrytuio')

except Exception:
    print("something went wrong")
