import psutil
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speek(str):
     a = pyttsx3.init()
     a.say(str)
     a.runAndWait()
     return 

cpu_interval = psutil.cpu_percent(interval=1)

if (cpu_interval > 85):
     speek(f"Oh not your CPU is facing the difficultys becuase your are using the {cpu_interval}%")