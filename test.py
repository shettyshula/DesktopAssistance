from src.helper import speak, takeCommand, wish_me
import pyaudio
import webbrowser
import wikipedia
import datetime
import os
import streamlit as st



if __name__ == "__main__":
   wish_me()
while True:
    st.title("Desktop Assistant")
    
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