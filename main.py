import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import wikipedia
import datetime
import os

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
  
    wish_me()    
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
    

takeCommand()

 
if __name__ == "__main__":
   
    #while True
  query= takeCommand().lower()
  if "wikipedia" in query:
      speak("Searching Wikipedia")
      query=query.replace("wikipedia","")
      results=wikipedia.summary(query, sentences=2)
      speak("According to wikipedia")
      print(results)
      speak(results)
      
  elif "youtube" in query:
      speak("opening youtube")
      webbrowser.open("youtube.com")
      
  elif "google" in query:
      speak("opening google")
      webbrowser.open("google.com")
      
  elif "goodbye" in query:
      speak("good byee Sir")
      exit()
  
 
    
   
   
    
    
    
               
 
