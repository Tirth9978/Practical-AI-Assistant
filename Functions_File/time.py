import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
from openai import OpenAI
from dotenv import load_dotenv
import psutil


load_dotenv()

# Main String
wikipedia.set_lang("en")
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# Talk functions 
def talk(text):
    engine.say(text)                # Queue `text` into the TTS engine’s buffer
    engine.runAndWait() 

def forTime():
     time = datetime.datetime.now().strftime('%I:%M %p')
     talk("Time is " + time)
     
     