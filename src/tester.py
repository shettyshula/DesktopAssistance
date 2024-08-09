import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS


GOOGLE_API_KEY="AIzaSyCgAPbO3a_qzV67TInMIR5Cwyua09Y0Rtk"
os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY

def voice_input():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening...")
        audio=r.listen(Source)
        try:
            text=r.recognize_google(audio)
            print("You Said :", text)
            return text
        except sr.UnknownValueError:
            print("sorry, could not understanf audio")
        except sr.RequestError as e:
            print("Could not request from Google Speech Recognition service; {0}".format(e))
            
            
def text_to_speech(text):
    tts=gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    
def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(user_text)
    result=response.text
    return result
        