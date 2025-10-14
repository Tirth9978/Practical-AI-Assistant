import speech_recognition as sr
import pyttsx3
import wikipedia
from duckduckgo_search import DDGS
import pywhatkit
import os
from openai import OpenAI
from dotenv import load_dotenv
import psutil

# Functions .
from Functions_File import time,aboutYou,search,Pywhatkit,greating
from Src.Globla_Instructions import globalCall


load_dotenv()

# Initiolation
wikipedia.set_lang("en")
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)                # Queue `text` into the TTS engine’s buffer
    engine.runAndWait()   

def take_command() :
     try: 
          with sr.Microphone() as source:
               print("Listening .......")
               voice = listener.listen(source)
               command = listener.recognize_google(voice)
               command = command.lower()
               print("You said:", command)
               return command
     except : 
          return ""

def gettingCPUUse():
     cpu_usage = psutil.cpu_percent(interval=1)
     print(cpu_usage)
     if (cpu_usage > 80):
          talk("I am not feeling well there are lots of processes there ")
     
def run_brain() :
     command = take_command()
     if "time" in command :
          time.forTime()

     elif "play" in command:
          song = command.replace("play" , "")
          Pywhatkit.play(song)
          
     elif "about you" in command :
          name = aboutYou.tellMeAboutYou()
          talk(f"I am {name} . And I here to help you")
     elif "open" in command : 
          globalCall.Open(command)
     
     elif 'what is' in command or 'tell me about' in command or 'who is' in command:
          talk("Searching")
          query = command.replace('what is', '').replace('tell me about', '').replace('who is', '').strip()
          answer = search.get_answer(query)
          talk(answer)
     
     
     elif "thank" in command :
          talk(f"Most Welcome sir .")
          os._exit(0)
     
def intro():
     ans = greating.intro()
     talk(f"{ans} , How can I help you today.")
     
intro()

while True :
     run_brain()