import speech_recognition as sr
from googlesearch import search
import sys
r = sr.Recognizer()
filename = sr.AudioFile('Modi.wav')
with filename as source:
    audio = r.listen(source)
try:
    s = r.recognize_google(audio)
    arr = s.split()
    if arr[0] == 'search':
        arr.pop(0)
        for j in search(arr[1], tld="co.in", stop=10, pause=2):
            print(j)

except Exception:
    print("something went wrong")
