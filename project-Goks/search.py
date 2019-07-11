import speech_recognition as sr
from googlesearch import search
import os
import webbrowser


def speechToText():
    filename = sr.AudioFile('Modi.wav')
    with filename as source:
        audio = r.listen(source)
    return audio


r = sr.Recognizer()
audio = speechToText()

try:
    a = []
    s = r.recognize_google(audio)
    arr = s.split()
    if arr[0] == 'search':
        arr.pop(0)
        for j in search(" ".join(arr), tld="co.in", stop=2, pause=2):
            a.append(j)
        webbrowser.open_new_tab(a[0])
        s = speechToText()
        if s == 'next':
            webbrowser.open_new_tab(a[1])
        if s == 'close':
            os.system("taskkill /im chrome.exe /f")

except Exception:
    print("something went wrong")
