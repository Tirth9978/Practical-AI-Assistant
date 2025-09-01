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

client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key=os.getenv("CHAT_GPT_KEY"),
)

def aiRunning(comtent):
     
     
     completion = client.chat.completions.create(
          model="openai/gpt-4o-mini",
          messages=[
          {
               "role": "user",
               "content": f"{comtent}"
          }
    ]
     )
     print(completion.choices[0].message.content)
     talk(completion.choices[0].message.content)

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
          time = datetime.datetime.now().strftime('%I:%M %p')
          talk("Time is " + time)

     elif "play" in command:
          song = command.replace("play" , "")
          talk("playing" + song)
          pywhatkit.playonyt(song)   # Open default browser, search on YouTube, play the top result

     elif "thank" in command :
          talk("Most Welcome sir I am here to help you sir")
          os._exit(0)
     elif command != "" :
          aiRunning(command)
          
     gettingCPUUse()
          

while True :
     run_brain()