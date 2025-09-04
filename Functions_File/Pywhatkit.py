import pywhatkit
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)                # Queue `text` into the TTS engine’s buffer
    engine.runAndWait() 

def play(song):
     talk("playing" + song)
     pywhatkit.playonyt(song) 