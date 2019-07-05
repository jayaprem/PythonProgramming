import speech_recognition as sr
import sys
r=sr.Recognizer()
filename=sr.AudioFile('jaya.wav')
with filename as source:
    audio=r.listen(source)
try:
    print("System predicts: "+r.recognize_google(audio))
except Exception:
    print("something went wrong")
    
NOTE:INSTALL
pip install SpeechRecognition
