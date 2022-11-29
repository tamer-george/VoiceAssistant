"""
Simple Program that record your voice and search on YouTube or google for what u requested without typing.
if you mention YouTube it will search for you on YouTube
else it will search on Google.
for example:
say: play music on YouTube
or
say: The best chocolate brownie recipe
"""

import speech_recognition as sr
import pywhatkit
from gtts import gTTS
from playsound import playsound
import pyaudio


def speech(txt):
    print(txt)
    language = "en"
    output = gTTS(text=txt, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        speech("say something")
        audio = recorder.listen(source)
    text1 = recorder.recognize_google(audio)
    print("You Said :", text1)
    return text1


text2 = get_audio()

if "youtube" in text2.lower():
    pywhatkit.playonyt(text2)
else:
    pywhatkit.search(text2)