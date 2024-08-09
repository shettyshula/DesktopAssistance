import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import wikipedia
import datetime
import os

 
  
    #wish_me()    
#Taking voice from my system
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
#print(voices[0].id)
#print(type(voices))
engine.setProperty('voice',voices[1].id)
#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("SHALOM YAHWEH")

#Speech recognition
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(Source)
        
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said : {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    

#takeCommand()
#The function is for wish me by using time
def wish_me():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning..")
    elif hour>=12 and hour<18:
        speak("Good Afternoon..")
    else:
        speak("Good Evening")
        speak("Tell me Sir") 
