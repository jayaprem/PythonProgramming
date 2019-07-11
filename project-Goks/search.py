import speech_recognition as sr
from googlesearch import search
import sys
r=sr.Recognizer()
filename=sr.AudioFile('Modi.wav')
with filename as source:
    audio=r.listen(source)
try:
    s=r.recognize_google(audio)
    arr=s.split()
    if arr[0]=='search':
        for j in search(arr[1], tld="co.in",stop=10,pause=2):
            print(j)

except Exception:
    print("something went wrong")

NOTE:INSTALL ------ https://www.geeksforgeeks.org/performing-google-search-using-python-code/(refer)
pip install beautifulsoup4 //python library for pulling data out of html and xml files
pip install google
