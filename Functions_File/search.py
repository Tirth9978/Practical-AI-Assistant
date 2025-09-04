import wikipedia
from duckduckgo_search import DDGS
import speech_recognition as sr
import pyttsx3
import os

def get_answer(query):
     try:
          # First try Wikipedia
          return wikipedia.summary(query, sentences=2, auto_suggest=True, redirect=True)

     except wikipedia.exceptions.DisambiguationError as e:
          # Pick the first option if multiple meanings
          return wikipedia.summary(e.options[0], sentences=2)

     except wikipedia.exceptions.PageError:
          # If Wikipedia can’t find it, try DuckDuckGo
          with DDGS() as ddgs:
               results = list(ddgs.text(query, max_results=1))
               if results:
                    return results[0]["body"]  # short answer
               else:
                    return "Sorry, I couldn't find anything."

     except Exception as e:
          print("⚠️ Error:", e)
          return "Something went wrong while searching."     