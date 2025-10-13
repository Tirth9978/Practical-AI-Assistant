import speech_recognition as sr
import pyttsx3
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speek(str):
     a = pyttsx3.init()
     a.say(str)
     a.runAndWait()
     return 

def findingLink(name):
     with open("Src/Globla_Instructions/Links.txt") as file : 
          for line in file :
               line = line.strip()
               line = line.lower()
               print("Tirth")
               print(line[:line.find(":")])
               if (name.find(line[:line.find(";")]) != -1):
                    print(line[:line.find(";")])
                    speek(f"Opening the {line[:line.find(";")]}")
                    webbrowser.open(line[line.find(";") + 1 : ])
                    
                    
def Open(name):
     link = findingLink(name)
     return 
     